#!/usr/bin/env python3
"""Generate the L4 data rows and the L4 tests for the two annex lists, by two independent routes.

  python3 -I annexes.py data-guarantee  BBOX.html RAW.txt   rows of PHỤ LỤC 5 (guarantee list), from PDF geometry
  python3 -I annexes.py data-excluded   BBOX.html RAW.txt   rows of the excluded-facility list, from PDF geometry
  python3 -I annexes.py tests-guarantee RAW.txt             #ASSERTs for the guarantee list, from the -layout text only
  python3 -I annexes.py tests-excluded  RAW.txt             #ASSERTs for the excluded list, from the -layout text only

BBOX.html is `pdftotext -bbox SOURCE.pdf BBOX.html` (poppler) run on the deposited PDF; RAW.txt is
the deposited `pdftotext -layout` rendering, source/raw/<id>.txt. Both are read as data, never run.

WHY TWO ROUTES. The data rows are built from word positions in PDF points, where each table column
has fixed edges on every page (measured from the page images and the word positions). The tests
are built from the character columns of the -layout text, where the mark columns move from page
to page (109/120/129 on page 1, 121/125/129 on page 2, ...), so the generator finds the three mark
columns of each page from the text itself. The routes share no code beyond reading files, so an
assertion that fails is a disagreement between two readings of the same page.

The data route also reads RAW.txt, only to find which lines of it hold each row, for the
`[cell:ID:N-M]` marker that tools/vnsrc.py uses to check every Vietnamese word of the row against
the deposited text.
"""
import html
import os
import re
import sys

WORD = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>')


def pages_of(bbox_path):
    with open(bbox_path, encoding="utf-8") as f:
        t = f.read()
    out = []
    for k, p in enumerate(t.split("<page ")[1:]):
        # y is offset by 10000pt per page, so that words of a row continued over a page break
        # keep their reading order when the two parts are merged.
        off = 10000.0 * k
        out.append([(float(a), float(b) + off, float(c), float(d) + off, html.unescape(w)) for a, b, c, d, w in WORD.findall(p)])
    return out


def lines_of(raw_path):
    with open(raw_path, encoding="utf-8") as f:
        return f.read().split("\n")


def visual_lines(words):
    """Group words into visual lines (yMin within 2pt), each line's words left to right."""
    rows = []
    for w in sorted(words, key=lambda w: (w[1], w[0])):
        if rows and abs(rows[-1][0] - w[1]) < 2.0:
            rows[-1][1].append(w)
        else:
            rows.append([w[1], [w]])
    return [" ".join(x[4] for x in sorted(ws, key=lambda w: w[0])) for _, ws in rows]


def rows_by_geometry(pages, edges, first_col_max):
    """Split each page into rows. A row's number is printed on its LAST visual line (the cells are
    bottom-aligned), so a word belongs to the first row-number at or below it on its page."""
    rows = []
    for pi, ws in enumerate(pages, 1):
        head = [w for w in ws if w[4] == "STT"]
        if head:  # the title and the column headings: everything down to the STT heading's line
            ws = [w for w in ws if w[1] > head[0][3] + 1.0]
        nums = sorted([w for w in ws if w[0] < first_col_max and re.fullmatch(r"\d+", w[4])], key=lambda w: w[1])
        for w in ws:
            if w in nums:
                continue
            owner = next((n for n in nums if n[1] >= w[1] - 2.0), None)
            if owner is None:
                continue
            w_ = w
            col = sum(1 for e in edges if w_[0] >= e)
            owner_key = (pi, owner[1])
            rows.append((owner_key, int(owner[4]), col, w))
        for n in nums:
            rows.append(((pi, n[1]), int(n[4]), -1, n))
    by = {}
    for key, num, col, w in rows:
        r = by.setdefault(key, {"num": num, "cols": {}})
        if col >= 0:
            r["cols"].setdefault(col, []).append(w)
    return [by[k] for k in sorted(by)]


def number_lines(raw, pattern):
    """Line numbers (1-based) of the -layout lines that carry a row number, in order. A row number
    is printed at column 0-2; an address that begins with a house number is indented far past it."""
    out = []
    for i, l in enumerate(raw, 1):
        m = re.match(pattern, l.replace("\f", ""))
        if m:
            out.append((int(m.group(1)), i))
    return out


def q(s):
    assert '"' not in s and "\\" not in s, s
    return '"' + s + '"'


def b(x):
    return "TRUE" if x else "FALSE"


# ---------------------------------------------------------------- the guarantee list (PHỤ LỤC 5)
# Column edges in PDF points: STT | VÙNG | CƠ SỞ Y TẾ | ĐỊA CHỈ | NỘI TRÚ | NGOẠI TRÚ | RĂNG
G_EDGES = [82.0, 149.0, 332.0, 600.0, 662.0, 726.0]


def data_guarantee(bbox, rawp):
    raw = lines_of(rawp)
    rid = os.path.basename(rawp)[: -len(".txt")]
    rows = rows_by_geometry(pages_of(bbox), G_EDGES, 82.0)
    nl = number_lines(raw, r" {0,2}(\d+)\s")
    nl = [(n, i) for n, i in nl if i > 3]  # below the header
    assert [n for n, _ in nl] == list(range(1, len(nl) + 1)), "row numbers in the text are not 1..N"
    assert [r["num"] for r in rows] == [n for n, _ in nl], "geometry and text disagree on the rows"
    prev = 3
    for r, (n, i) in zip(rows, nl):
        c = r["cols"]
        region = " ".join(visual_lines(c.get(1, [])))
        name = " ".join(visual_lines(c.get(2, [])))
        addr = " ".join(visual_lines(c.get(3, [])))
        marks = [bool(c.get(k)) for k in (4, 5, 6)]
        for k in (4, 5, 6):
            assert all(w[4] == "x" for w in c.get(k, [])), (n, k)
        print(
            f"    (`A row of the guarantee list` OF {n}, {q(region)}, {q(name)}, {q(addr)}, "
            f"{b(marks[0])}, {b(marks[1])}, {b(marks[2])}){',' if n < len(nl) else ''}"
            f"   -- [cell:{rid}:{prev + 1}-{i}]"
        )
        prev = i


def tests_guarantee(rawp):
    raw = lines_of(rawp)
    rid = os.path.basename(rawp)[: -len(".txt")]
    page, by_page = 1, {}
    rows = []
    for i, l in enumerate(raw, 1):
        page += l.count("\f")
        l2 = l.replace("\f", "")
        m = re.match(r" {0,2}(\d+)\s+(.+?)(?:\s{2,}|$)", l2)
        xs = [k.start() for k in re.finditer(r"(?<=\s)x(?=\s|$)", l2)]
        by_page.setdefault(page, set()).update(xs)
        if m and i > 3:
            rows.append((int(m.group(1)), m.group(2), page, xs, i))
    cols = {}
    for p, s in by_page.items():
        s = sorted(s)
        if not s:  # the empty page after the last form feed
            continue
        assert len(s) == 3, f"page {p}: expected three mark columns in the text, found {s}"
        cols[p] = s
    for n, region, p, xs, i in rows:
        assert set(xs) <= set(cols[p]), (n, xs, cols[p])
        marks = [c in xs for c in cols[p]]
        print(
            f"#ASSERT `the marks on guarantee-list row` {n} EQUALS LIST {b(marks[0])}, {b(marks[1])}, {b(marks[2])}"
            f"   -- text line {i}, page {p}, mark columns {cols[p]}"
        )
    for n, region, p, xs, i in rows:
        print(f"#ASSERT `the region of guarantee-list row` {n} EQUALS {q(region)}   -- [in:{rid}] text line {i}")
    print(f"#ASSERT count `the guarantee list` EQUALS {len(rows)}")


# ---------------------------------------------------------------- the excluded-facility list
# Column edges in PDF points: STT | TỈNH | HỆ THỐNG CSYT | ĐỊA CHỈ CSYT
E_EDGES = [78.0, 139.0, 443.0]


def data_excluded(bbox, rawp):
    raw = lines_of(rawp)
    rid = os.path.basename(rawp)[: -len(".txt")]
    rows = rows_by_geometry(pages_of(bbox), E_EDGES, 78.0)
    nl = number_lines(raw, r" {0,2}(\d+)\s")
    nl = [(n, i) for n, i in nl if i > 5]
    # A row that runs over a page break carries its number on both pages; merge them.
    merged = []
    for r in rows:
        if merged and merged[-1]["num"] == r["num"]:
            for k, v in r["cols"].items():
                merged[-1]["cols"].setdefault(k, []).extend(v)
                merged[-1].setdefault("parts", []).append(v)
        else:
            merged.append(r)
    last = {}
    for n, i in nl:
        last[n] = i
    nums = sorted(last)
    assert nums == list(range(1, len(nums) + 1)), "row numbers in the text are not 1..N"
    assert [r["num"] for r in merged] == nums, "geometry and text disagree on the rows"
    prev = 5
    for r in merged:
        n = r["num"]
        c = r["cols"]
        prov = visual_lines(c.get(1, []))
        names = []
        for v in visual_lines(c.get(2, [])):
            v = v.rstrip(";").strip()
            if v not in names:
                names.append(v)
        addrs = []
        for v in visual_lines(c.get(3, [])):
            if v not in addrs:
                addrs.append(v)
        assert len(set(prov)) == 1, (n, prov)
        i = last[n]
        names_l = "(LIST " + ", ".join(q(x) for x in names) + ")"
        addrs_l = "(LIST " + ", ".join(q(x) for x in addrs) + ")"
        print(
            f"    (`A row of the excluded-facility list` OF {n}, {q(prov[0])}, {names_l}, {addrs_l})"
            f"{',' if n < len(nums) else ''}   -- [cell:{rid}:{prev + 1}-{i}]"
        )
        prev = i


def tests_excluded(rawp):
    raw = lines_of(rawp)
    rid = os.path.basename(rawp)[: -len(".txt")]
    provinces = ("Bình Dương", "Cần Thơ", "Đà Nẵng", "Đồng Nai", "Hà Nội", "TP HCM")
    seen = {}
    for i, l in enumerate(raw, 1):
        l2 = l.replace("\f", "")
        m = re.match(r" {0,2}(\d+)\s+(" + "|".join(provinces) + r")\s", l2)
        if m and i > 5:
            seen.setdefault(int(m.group(1)), []).append((m.group(2), i))
    for n in sorted(seen):
        provs = {p for p, _ in seen[n]}
        assert len(provs) == 1, (n, seen[n])
        lines = ", ".join(str(i) for _, i in seen[n])
        print(f"#ASSERT `the province of excluded-list row` {n} EQUALS {q(provs.pop())}   -- [in:{rid}] text line {lines}")
    print(f"#ASSERT count `the excluded-facility list` EQUALS {len(seen)}")


def main():
    cmd, args = sys.argv[1], sys.argv[2:]
    {
        "data-guarantee": lambda: data_guarantee(*args),
        "data-excluded": lambda: data_excluded(*args),
        "tests-guarantee": lambda: tests_guarantee(*args),
        "tests-excluded": lambda: tests_excluded(*args),
    }[cmd]()


if __name__ == "__main__":
    main()
