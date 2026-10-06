#!/usr/bin/env python3
"""Quote and check Vietnamese text against a deposited source rendering.

  python3 -I vnsrc.py quote RAW.txt N [M]               print `-- src:N | <line N>` (through M) ready to paste
  python3 -I vnsrc.py quote --qualified RAW.txt N [M]   print `-- src:ID:N | <line N>`, ID = RAW's basename less `.txt`
  python3 -I vnsrc.py check RAW.txt FILE...             verify every Vietnamese quotation in FILE... against RAW.txt

RAW.txt is the `pdftotext -layout` rendering that source/fetch.sh writes to source/raw/.
`src:N` always means line N of that file.

What `check` enforces (exit 1 if any fails; each failure is printed as file:line: reason):

 1. A line of the form `-- src:N | text` or `-- src:N-M | text` (or the same inside a .md
    table cell or a quoted block) must be a verbatim slice of lines N..M of RAW.txt,
    comparing case-folded, NFC, with punctuation and whitespace collapsed. A trailing
    ellipsis (`…` or `...`) means "prefix of".
 2. On every other line, each run of Vietnamese words must occur verbatim in RAW.txt (same
    comparison). A Vietnamese word is a token carrying a Vietnamese diacritic or d-bar; a run is
    those tokens plus at most two plain tokens between them. Runs end at quotes, brackets, and
    sentence punctuation. So a paraphrase in plain English passes, and a misspelt or
    reconstructed Vietnamese phrase does not.
 3. A line containing the marker `[translator]` is exempt from rule 2: it is the encoder's own
    Vietnamese rendering of English source text, and the marker says so out loud.
    A line containing the marker `[page-read p.N]` is exempt too: it is Vietnamese read from the page
    image of page N of a scanned source, where the OCR text is wrong, and the marker says so out loud.

EXTENSION for a subject with several source files (row VN-19, enc-vn-19, 2026-10-06).
Every line that passed the original checker passes this one with the same result; the new
behaviour is reached only through the three new forms below, so a subject with one source file,
or a file that uses none of them, is checked exactly as before. A "sibling" is any `*.txt` file in
RAW.txt's own directory, RAW.txt included (so `[cell:]` can name RAW.txt's own wrapped table cells);
its ID is its basename less `.txt`.

 4. `-- src:ID:N | text` and `-- src:ID:N-M | text` (a QUALIFIED quotation) are checked as in rule 1,
    but against lines N..M of the sibling ID. An ID that names no sibling is a problem.
 5. A line carrying the marker `[in:ID]` (one or more) has its Vietnamese runs checked as in rule 2
    against RAW.txt AND each named sibling: a run passes if it occurs verbatim in any of them.
 6. A line carrying the marker `[cell:ID:N-M]` holds table cells that the `-layout` rendering of
    sibling ID wraps over several lines, interleaved with other cells (a facility name on lines 158
    and 160 with its address on 159). Each Vietnamese run on the line must be assembled from
    consecutive pieces, each piece occurring verbatim within ONE line of N..M, the pieces in line
    order (never going back to an earlier line). A misspelt or invented word still fails; only the
    contiguity across a wrap is relaxed, and only within the M-N+1 lines the marker names.

It checks that quoted words are the source's words. It does not check that the encoding is
right; that is what the tests are for.
"""
import glob
import os
import re
import sys
import unicodedata

SRC_LINE = re.compile(r"--\s*src:(\d+)(?:-(\d+))?\s*\|\s*(.*)$")
QSRC_LINE = re.compile(r"--\s*src:([A-Za-z][A-Za-z0-9_.-]*):(\d+)(?:-(\d+))?\s*\|\s*(.*)$")
IN_MARK = re.compile(r"\[in:([A-Za-z][A-Za-z0-9_.-]*)\]")
CELL_MARK = re.compile(r"\[cell:([A-Za-z][A-Za-z0-9_.-]*):(\d+)-(\d+)\]")
SPLIT = re.compile(r"[\"“”‘’'`()\[\]{}<>|;:,.!?…•]|\s[-–—]\s")
ELLIPSIS = re.compile(r"(…|\.\.\.)\s*$")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def norm(s):
    s = nfc(s).casefold()
    s = re.sub(r"[^\w]+", " ", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s).strip()


def is_vi(tok):
    d = unicodedata.normalize("NFD", tok)
    return "đ" in tok.casefold() or any(unicodedata.category(c) == "Mn" for c in d)


def load(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    return lines


def vi_runs(text):
    """Yield each maximal run of Vietnamese words in `text` (a string with no src: marker)."""
    for seg in SPLIT.split(text):
        toks = seg.split()
        i = 0
        while i < len(toks):
            if not is_vi(toks[i]):
                i += 1
                continue
            j, last, gap = i, i, 0
            while j + 1 < len(toks):
                if is_vi(toks[j + 1]):
                    j += 1
                    last, gap = j, 0
                elif gap < 2 and any(is_vi(t) for t in toks[j + 2 : j + 4]):
                    j += 1
                    gap += 1
                else:
                    break
            yield " ".join(toks[i : last + 1])
            i = last + 1


def cmd_quote(args):
    qualified = False
    if args and args[0] == "--qualified":
        qualified, args = True, args[1:]
    raw = load(args[0])
    n = int(args[1])
    m = int(args[2]) if len(args) > 2 else n
    tag = os.path.basename(args[0])[: -len(".txt")] + ":" if qualified else ""
    for k in range(n, m + 1):
        t = re.sub(r"\s+", " ", nfc(raw[k - 1])).strip()
        if t:
            print(f"-- src:{tag}{k} | {t}")
    return 0


def slice_ok(raw, a, b, text):
    body = ELLIPSIS.sub("", text)
    body = re.sub(r"\s*\|\s*$", "", body)
    window = " " + norm(" ".join(raw[a - 1 : b])) + " "
    return not norm(body) or (" " + norm(body)) in window or norm(body) in window


def assembled(toks, lines):
    """Can `toks` be split into consecutive pieces, each found in one of `lines`, in reading order?

    Reading order: each piece lies on a later line than the one before it, or on the same line
    to its right."""
    padded = [" " + norm(l) + " " for l in lines]
    memo = {}

    def go(i, lmin, pos):
        if i == len(toks):
            return True
        key = (i, lmin, pos)
        if key not in memo:
            memo[key] = False
            for j in range(len(toks), i, -1):
                piece = " " + " ".join(toks[i:j]) + " "
                for li in range(lmin, len(padded)):
                    k = padded[li].find(piece, pos if li == lmin else 0)
                    if k >= 0 and go(j, li, k + len(piece) - 1):
                        memo[key] = True
                        return True
        return memo[key]

    return go(0, 0, 0)


def cmd_check(args):
    raw = load(args[0])
    hay = " " + norm(" ".join(raw)) + " "
    rawdir = os.path.dirname(os.path.abspath(args[0]))
    rawid = os.path.basename(args[0])[: -len(".txt")]
    sib = {}
    for p in sorted(glob.glob(os.path.join(rawdir, "*.txt"))):
        sid = os.path.basename(p)[: -len(".txt")]
        sib[sid] = raw if sid == rawid else load(p)
    sibhay = {k: " " + norm(" ".join(v)) + " " for k, v in sib.items()}
    bad = 0
    nsrc = nqsrc = nrun = nin = ncell = 0
    for path in args[1:]:
        for ln, line in enumerate(load(path), 1):
            if "[translator]" in line or "[page-read" in line:
                continue
            m = QSRC_LINE.search(line)
            if m:
                sid, a = m.group(1), int(m.group(2))
                b = int(m.group(3) or a)
                nsrc += 1
                nqsrc += 1
                if sid not in sib:
                    print(f"{path}:{ln}: src:{sid}: no sibling source of that id beside {args[0]}")
                    bad += 1
                elif not slice_ok(sib[sid], a, b, m.group(4)):
                    print(f"{path}:{ln}: src:{sid}:{a}-{b} quotation is not a slice of those lines")
                    bad += 1
                continue
            m = SRC_LINE.search(line)
            if m:
                a = int(m.group(1))
                b = int(m.group(2) or a)
                nsrc += 1
                if not slice_ok(raw, a, b, m.group(3)):
                    print(f"{path}:{ln}: src:{a}-{b} quotation is not a slice of those lines")
                    bad += 1
                continue
            cells = CELL_MARK.findall(line)
            ins = IN_MARK.findall(line)
            text = IN_MARK.sub(" ", CELL_MARK.sub(" ", line))
            for sid in [c[0] for c in cells] + ins:
                if sid not in sib:
                    print(f"{path}:{ln}: marker names {sid!r}, which is no sibling source beside {args[0]}")
                    bad += 1
            if cells:
                sid, a, b = cells[0][0], int(cells[0][1]), int(cells[0][2])
                lines = sib.get(sid, [])[a - 1 : b]
                for run in vi_runs(text):
                    nrun += 1
                    ncell += 1
                    if not assembled(norm(run).split(), lines):
                        print(f"{path}:{ln}: Vietnamese run not assembled from {sid} lines {a}-{b}: {run!r}")
                        bad += 1
                continue
            hays = [hay] + [sibhay[s] for s in ins if s in sibhay]
            for run in vi_runs(text):
                nrun += 1
                if ins:
                    nin += 1
                nr = norm(run)
                if nr and not any((" " + nr + " ") in h for h in hays):
                    print(f"{path}:{ln}: Vietnamese run not found verbatim in source: {run!r}")
                    bad += 1
    print(
        f"vnsrc check: {nsrc} src: lines ({nqsrc} qualified), {nrun} Vietnamese runs "
        f"({ncell} in [cell:] lines, {nin} in [in:] lines), {bad} problems"
    )
    return 1 if bad else 0


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("quote", "check"):
        print(__doc__)
        return 2
    return (cmd_quote if sys.argv[1] == "quote" else cmd_check)(sys.argv[2:])


if __name__ == "__main__":
    sys.exit(main())
