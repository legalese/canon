#!/usr/bin/env python3
"""Generate the Annex VI (Phụ lục VI) table module and its tests from the raw source text.

  python3 -I tools/annex6.py ../../source/raw/nd67-congbao-1019-1020.txt

Run from the encoding directory. Writes, beside this script's parent directory:

  nd67-annex6-table.l4   one L4 row per source row of Phụ lục VI (Part A, Part B sections I-X,
                         and the 10 x 10 visual-acuity table), each preceded by the source
                         line(s) it encodes, quoted mechanically as `-- src:ID:N | ...`;
  nd67-annex6-tests.l4   one #ASSERT per source row (one per cell of the acuity table),
                         whose expected value is extracted a SECOND time, independently,
                         from the raw text (see `expected_from_raw`).

Reads the raw text as data; never executes it. Prints a summary (rows, rated rows, rows with
no rate of their own, notes, cells settled by looking at the PDF) that NOTES.md copies.

The layout decisions this script makes are listed in LAYOUT below, each with the source line
it concerns. Every one was checked against the PDF page itself (NOTES.md §5.4).
"""
import os
import re
import sys
import unicodedata

SRC_ID = "nd67-congbao-1019-1020"
FIRST, LAST = 591, 2197          # Phụ lục VI, title to the last special case
TABLE_END = 2176                 # last line of section X; the special cases follow
LIMIT = 150_000_000              # Điều 6(1): VND per person per accident (src:189, 1017-1018)

HDR = re.compile(r"CÔNG BÁO/Số")
SEC = re.compile(r"^\s*([IVX]+)\.\s+(Tỷ lệ.*?)\s+%\s*$")
PART = re.compile(r"^\s*([AB])\.\s+CÁC TRƯỜNG HỢP")
CODE = re.compile(r"^\s*(\d+(?:\.\d+)+)\.?\s+(\S.*)$|^\s*(\d+)\.\s+(\S.*)$")
# A cell: a number or a range, at the right of the line. Two spaces before it, or one space
# before a hyphenated range (the tight lines listed in LAYOUT).
VAL2 = re.compile(r"\s{2,}(\d+(?:,\d+)?)(?:\s*-\s*(\d+(?:,\d+)?))?\s*$")
VAL1 = re.compile(r"\s(\d+(?:,\d+)?)\s*-\s*(\d+(?:,\d+)?)\s*$")
MATRIX_HEAD = "TỶ LỆ TỔN THƯƠNG CƠ THỂ DO GIẢM THỊ LỰC"
MATRIX_ROW = re.compile(
    r"^\s*(10/10 - 8/10|7/10 - 6/10|5/10|4/10|3/10|2/10|1/10|1/20|dưới 1/20|ST \(-\))"
    r"((?:\s+\d+){10})\s*$")
SPECIAL = "Những trường hợp đặc biệt"

# Lines that open a note (a "Ghi chú" or an unlabelled instruction after a rated row). A note
# runs to the next coded line. Its words are quoted, and its rule is encoded or not as
# nd67-annex6.l4 and NOTES.md §2 say; it is never part of a row's rate.
NOTE_START = {622, 670, 763, 869, 930, 1129, 1425, 1641, 1774, 1816, 1832, 1845, 1860,
              1985, 2041, 2123, 2169}

# Layout decisions, each settled against the PDF page (Read tool, `pages`), NOTES.md §5.4.
LAYOUT = {
    1746: "ends 'từ 0' (part of 'từ 0 đến 20°'): text, not a cell",
    2021: "one space before '31 - 35'; the cell is 31-35 and 'từ' starts 'từ cành cao'",
    2047: "an uncoded line under heading IX.3 carrying the cell 51-55: the row is IX.3",
    2132: "one space before '16 - 20': the cell",
    2133: "one space before '36 - 40': the cell; 'cộng lùi ...' on 2134 is text",
    2148: "one space before '11 - 15': the cell; '(khó nuốt chất đặc)' wraps to 2149",
    2150: "one space before '26 - 30': the cell",
    2151: "one space before '71 - 75': the cell",
    841: "the cell sits on the middle line of a three-line row (1.1.2.1)",
    1165: "starts '1.3.2 cộng lùi': a cross-reference continuing V 1.3.3, not a new row",
    2076: "the item number '1.1.10.2' is printed without its final dot: still a row",
    1895: "the cell sits on the middle line of a three-line row (VIII 2.4)",
}
NOT_CODE = {1165}
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
MATRIX_CLASSES = [
    ("10/10 - 8/10", "`8/10 to 10/10`"),
    ("7/10 - 6/10", "`6/10 to 7/10`"),
    ("5/10", "`5/10`"),
    ("4/10", "`4/10`"),
    ("3/10", "`3/10`"),
    ("2/10", "`2/10`"),
    ("1/10", "`1/10`"),
    ("1/20", "`1/20`"),
    ("dưới 1/20", "`below 1/20`"),
    ("ST (-)", "`no light perception`"),
]


def nfc(s):
    return unicodedata.normalize("NFC", s)


def quote(raw, n):
    t = re.sub(r"\s+", " ", nfc(raw[n - 1])).strip()
    return f"-- src:{SRC_ID}:{n} | {t}"


def num(s):
    return s.replace(",", ".")


def parse(raw):
    """The rows, notes, matrix and special cases of Phụ lục VI, in source order."""
    rows, notes, matrix = [], [], []
    part, sec, cur, note = None, None, None, None
    in_matrix = False
    for n in range(FIRST, TABLE_END + 1):
        t = raw[n - 1]
        if HDR.search(t) or not t.strip():
            continue
        if MATRIX_HEAD in t:
            in_matrix, cur, note = True, None, None
            matrix.append(("head", n))
            continue
        m = SEC.match(t)
        if m:
            in_matrix, cur, note = False, None, None
            sec = m.group(1)
            rows.append(dict(kind="section", key=f"B.{sec}", lines=[n]))
            continue
        p = PART.match(t)
        if p:
            part, sec, cur, note = p.group(1), None, None, None
            continue
        if in_matrix:
            mr = MATRIX_ROW.match(t)
            if mr:
                matrix.append(("row", n, mr.group(1), [int(x) for x in mr.group(2).split()]))
            else:
                matrix.append(("text", n))
            continue
        if part is None:
            continue
        c = CODE.match(t) if n not in NOT_CODE else None
        if n in NOTE_START:
            note = dict(lines=[n], after=cur)
            notes.append(note)
            cur = None
            continue
        if c and (part == "A" or sec):
            note = None
            code = c.group(1) or c.group(3)
            key = "A" if part == "A" else f"B.{sec}"
            cur = dict(kind="item", key=key, code=code, lines=[n], cells=[])
            rows.append(cur)
        elif note is not None:
            note["lines"].append(n)
            continue
        elif cur is not None:
            cur["lines"].append(n)
        else:
            continue      # the part headings and the formula line (597-602)
        v = VAL2.search(t) or VAL1.search(t)
        if v and n != 1746:
            lo, hi = v.group(1), v.group(2) or v.group(1)
            cur["cells"].append((n, num(lo), num(hi)))
    for r in rows:
        if r["kind"] == "item" and r["key"] == "A":
            r["cells"] = [(r["lines"][0], "100", "100")]   # Part A: 100% of the limit (src:597-598)
    return rows, notes, matrix


def expected_from_raw(raw, n_first, n_last):
    """The SECOND extraction, for the tests: scan the row's lines from the raw text again for a
    figure at the right margin, written independently of `parse` (a plain split on the last
    run of two or more spaces, with the PDF-settled tight lines named one by one)."""
    found = []
    for n in range(n_first, n_last + 1):
        line = raw[n - 1].rstrip()
        if n == 1746:
            continue
        if n in (2021, 2132, 2133, 2148, 2150, 2151, 2047):
            tail = " ".join(line.split()[-3:])
        elif re.fullmatch(r"\s*\d+(?:,\d+)?(?:\s*-\s*\d+(?:,\d+)?)?\s*", line):
            tail = line.strip()          # a line holding only the cell (841, 856, 1895, ...)
        else:
            parts = re.split(r"\s{2,}", line.strip())
            if len(parts) < 2:
                continue
            tail = parts[-1]
        mm = re.fullmatch(r"(\d+(?:,\d+)?)(?:\s*-\s*(\d+(?:,\d+)?))?", tail)
        if mm:
            found.append((num(mm.group(1)), num(mm.group(2) or mm.group(1))))
    return found


def money(pct):
    # pct is a decimal string; LIMIT * pct / 100, exact in integers for these figures
    whole, _, frac = pct.partition(".")
    scale = 10 ** len(frac)
    v = LIMIT * (int(whole) * scale + (int(frac) if frac else 0)) // (100 * scale)
    assert LIMIT * (int(whole) * scale + (int(frac) if frac else 0)) % (100 * scale) == 0
    return v


def main():
    rawp = sys.argv[1]
    raw = open(rawp, encoding="utf-8").read().split("\n")
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rows, notes, matrix = parse(raw)
    items = [r for r in rows if r["kind"] == "item"]

    # Sanity: every code unique within its part/section; every parent seen first.
    problems = []
    seen = {}
    for r in items:
        k = (r["key"], r["code"])
        if k in seen:
            problems.append(f"duplicate {k} at {seen[k]} and {r['lines'][0]}")
        seen[k] = r["lines"][0]
        parts = r["code"].split(".")
        if len(parts) > 1 and (r["key"], ".".join(parts[:-1])) not in seen:
            problems.append(f"parent of {k} not seen before line {r['lines'][0]}")
        if len(r["cells"]) > 1:
            problems.append(f"{k} has {len(r['cells'])} cells")

    out = []
    w = out.append
    w("@lang en")
    w("IMPORT prelude")
    w("IMPORT `nd67-vn10-nouns`")
    w("")
    w("-- GENERATED by tools/annex6.py from ../../source/raw/nd67-congbao-1019-1020.txt,")
    w(f"-- lines {FIRST}-{TABLE_END}. Do not edit by hand: change the script and run it again.")
    w("--")
    w("-- Annex VI (Phụ lục VI) of Decree 67/2023/NĐ-CP: the table of payments for damage to")
    w("-- health and life. One L4 row per source row, in source order, each preceded by the")
    w("-- source line(s) it encodes. `src:ID:N` is line N of ../../source/raw/ID.txt.")
    w("-- A row is (part and section, item number as printed, rate). The rate is the cell of")
    w("-- the '%' column: a band 'a - b' is `a band of` a b; a single figure n is `a band of` n n;")
    w("-- a row with no figure (a heading, or a row whose text sends the assessor elsewhere)")
    w("-- is `no rate of its own`. Decimal commas are written as points (1,5 -> 1.5).")
    w("-- Notes (Ghi chú and unlabelled instructions) are quoted inert after the row they follow;")
    w("-- what is done with each is in nd67-annex6.l4 and NOTES.md.")
    w("-- This module is DATA ONLY. Its lookups are in nd67-annex6.l4.")
    w("")
    w("§ `Annex VI — the rows`")
    w("")
    w("-- " + quote(raw, 591)[3:])
    for n in range(592, 596):
        if raw[n - 1].strip():
            w(quote(raw, n))
    w("")

    groups = [("A", "Part A — the cases paid at 100% of the limit")] + [
        (f"B.{s}", f"Part B, section {s}") for s in ROMAN]
    note_after = {}
    for nt in notes:
        note_after.setdefault(id(nt["after"]), []).append(nt)
    for key, title in groups:
        sec_rows = [r for r in rows if r.get("key") == key]
        w(f"§§ `{title}`")
        if key == "A":
            for n in (597, 598, 601, 602):
                w(quote(raw, n))
        name = f"`the rows of Annex VI, {title.split(' —')[0]}`"
        w("")
        w(f"{name} MEANS")
        w("    LIST")
        body = []
        for r in sec_rows:
            if r["kind"] == "section":
                body.append(("c", quote(raw, r["lines"][0])))
                continue
            for n in r["lines"]:
                body.append(("c", quote(raw, n)))
            if r["cells"]:
                _, lo, hi = r["cells"][0]
                rate = f"`a band of` {lo} {hi}"
            else:
                rate = "`no rate of its own`"
            body.append(("r", f'(`An Annex VI row` OF "{key}", "{r["code"]}", {rate})'))
            for nt in note_after.get(id(r), []):
                body.append(("c", "-- NOTE, inert here:"))
                for n in nt["lines"]:
                    body.append(("c", quote(raw, n)))
        nrows = sum(1 for k, _ in body if k == "r")
        seen_r = 0
        for k, txt in body:
            if k == "c":
                w("        " + txt)
            else:
                seen_r += 1
                w("        " + txt + ("," if seen_r < nrows else ""))
        w("")

    # The acuity table
    w("§§ `The table of body-impairment rates for reduced visual acuity (section VIII)`")
    for item in matrix:
        if item[0] in ("head", "text"):
            w(quote(raw, item[1]))
    w("--")
    w("-- Columns, in the order the PDF page prints them (pdftotext scrambles the header; the")
    w("-- order was read off page 62 of the gazette issue, NOTES.md §5.4):")
    w("--   8/10-10/10, 6/10-7/10, 5/10, 4/10, 3/10, 2/10, 1/10, 1/20, below 1/20, ST(-)")
    w("")
    w("`the rows of the acuity table` MEANS")
    w("    LIST")
    mrows = [m for m in matrix if m[0] == "row"]
    head = "        (`An acuity table row` OF "
    width = max(len(dict(MATRIX_CLASSES)[m[2]]) for m in mrows) + 1
    cols = ["8-10", "6-7", "5", "4", "3", "2", "1/10", "1/20", "<1/20", "ST(-)"]
    lines = []
    for i, (_, n, label, cells) in enumerate(mrows):
        cls = dict(MATRIX_CLASSES)[label]
        cs = ",".join(str(c).rjust(5) for c in cells)
        lines.append((n, head + (cls + ",").ljust(width + 1) + cs[1:] + ")" + ("," if i < len(mrows) - 1 else "")))
    # the ruler: each column label right-aligned on the last digit of its cells
    first = lines[0][1]
    ends = [m.end() for m in re.finditer(r"\d+(?=[,)])", first[len(head):])][-10:]
    ruler = list(" " * (len(head) + ends[-1]))
    ruler[8:8 + 2] = list("--")
    lab = "the other eye:"
    ruler[11:11 + len(lab)] = list(lab)
    for e, c in zip(ends, cols):
        pos = len(head) + e - len(c)
        ruler[pos:pos + len(c)] = list(c)
    w("".join(ruler).rstrip())
    for n, txt in lines:
        w("        " + quote(raw, n))
        w(txt)
    w("")

    table_path = os.path.join(here, "nd67-annex6-table.l4")
    with open(table_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    # ---- tests ------------------------------------------------------------------------
    t = []
    a = t.append
    a("@lang en")
    a("IMPORT prelude")
    a("IMPORT `nd67-vn10-nouns`")
    a("IMPORT `nd67-annex6-table`")
    a("IMPORT `nd67-annex6`")
    a("")
    a("-- GENERATED by tools/annex6.py: one test per source row of Annex VI (Phụ lục VI), and one")
    a("-- per cell of its acuity table. The expected value of each is extracted from the raw text")
    a("-- a SECOND time (`expected_from_raw`), not copied from the table module, and is turned")
    a(f"-- into money by the formula the source prints (src:{SRC_ID}:602), with the Điều 6(1)")
    a("-- limit of 150,000,000 VND. A failing assertion here is a finding, never an edit.")
    a("")
    a("§ `Annex VI — one test per row`")
    a("")
    ntests = 0
    mism = []
    for r in items:
        exp = expected_from_raw(raw, r["lines"][0], r["lines"][-1]) if r["key"] != "A" else [("100", "100")]
        line = r["lines"][0]
        if exp:
            lo, hi = exp[0]
            got = r["cells"][0][1:] if r["cells"] else None
            if got != (lo, hi):
                mism.append((r["key"], r["code"], got, (lo, hi)))
            a(f'-- source line {line}')
            a(f'#ASSERT `the payment band in Annex VI for` "{r["key"]}" "{r["code"]}" '
              f'EQUALS RIGHT (`A payment band` OF {money(lo)}, {money(hi)})')
        else:
            if r["cells"]:
                mism.append((r["key"], r["code"], r["cells"][0][1:], None))
            a(f'-- source line {line}')
            a(f'#ASSERT `the payment band in Annex VI for` "{r["key"]}" "{r["code"]}" '
              f'EQUALS LEFT `the item fixes no rate of its own`')
        ntests += 1
    a("")
    a("§ `The acuity table — one test per cell`")
    a("")
    for (_, n, label, cells) in mrows:
        # second extraction: split the raw line on whitespace and take the last ten tokens
        toks = raw[n - 1].split()[-10:]
        cls = dict(MATRIX_CLASSES)[label]
        a(f"-- source line {n}")
        for j, (clab, ccls) in enumerate(MATRIX_CLASSES):
            a(f"#ASSERT `the acuity table rate for` {cls} {ccls} EQUALS {int(toks[j])}")
            ntests += 1
    tests_path = os.path.join(here, "nd67-annex6-tests.l4")
    with open(tests_path, "w", encoding="utf-8") as f:
        f.write("\n".join(t) + "\n")

    rated = [r for r in items if r["cells"]]
    print(f"annex6: {len(items)} rows ({sum(1 for r in items if r['key']=='A')} in Part A, "
          f"{sum(1 for r in items if r['key']!='A')} in Part B); "
          f"{len(rated)} with a rate, {len(items)-len(rated)} with no rate of their own")
    print(f"annex6: {len(notes)} notes; acuity table {len(mrows)} rows x 10 = {10*len(mrows)} cells")
    print(f"annex6: {ntests} tests written ({len(items)} rows + {10*len(mrows)} cells)")
    print(f"annex6: {len(LAYOUT)} layout decisions settled against the PDF")
    print(f"annex6: {len(mism)} disagreements between the two extractions")
    for x in mism:
        print("   ", x)
    print(f"annex6: {len(problems)} structural problems")
    for x in problems:
        print("   ", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
