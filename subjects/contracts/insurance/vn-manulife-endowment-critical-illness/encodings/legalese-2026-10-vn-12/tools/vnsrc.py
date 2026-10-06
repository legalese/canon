#!/usr/bin/env python3
"""Quote and check Vietnamese text against a deposited source rendering.

  python3 -I vnsrc.py quote RAW.txt N [M]    print `-- src:N | <line N>` (through M) ready to paste
  python3 -I vnsrc.py check RAW.txt FILE...  verify every Vietnamese quotation in FILE... against RAW.txt

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

It checks that quoted words are the source's words. It does not check that the encoding is
right; that is what the tests are for.
"""
import re
import sys
import unicodedata

SRC_LINE = re.compile(r"--\s*src:(\d+)(?:-(\d+))?\s*\|\s*(.*)$")
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
    raw = load(args[0])
    n = int(args[1])
    m = int(args[2]) if len(args) > 2 else n
    for k in range(n, m + 1):
        t = re.sub(r"\s+", " ", nfc(raw[k - 1])).strip()
        if t:
            print(f"-- src:{k} | {t}")
    return 0


def cmd_check(args):
    raw = load(args[0])
    hay = " " + norm(" ".join(raw)) + " "
    bad = 0
    nsrc = nrun = 0
    for path in args[1:]:
        for ln, line in enumerate(load(path), 1):
            if "[translator]" in line:
                continue
            m = SRC_LINE.search(line)
            if m:
                a = int(m.group(1))
                b = int(m.group(2) or a)
                body = ELLIPSIS.sub("", m.group(3))
                body = re.sub(r"\s*\|\s*$", "", body)
                window = " " + norm(" ".join(raw[a - 1 : b])) + " "
                nsrc += 1
                if norm(body) and (" " + norm(body)) not in window and norm(body) not in window:
                    print(f"{path}:{ln}: src:{a}-{b} quotation is not a slice of those lines")
                    bad += 1
                continue
            for run in vi_runs(line):
                nrun += 1
                nr = norm(run)
                if nr and (" " + nr + " ") not in hay:
                    print(f"{path}:{ln}: Vietnamese run not found verbatim in source: {run!r}")
                    bad += 1
    print(f"vnsrc check: {nsrc} src: lines, {nrun} Vietnamese runs, {bad} problems")
    return 1 if bad else 0


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("quote", "check"):
        print(__doc__)
        return 2
    return (cmd_quote if sys.argv[1] == "quote" else cmd_check)(sys.argv[2:])


if __name__ == "__main__":
    sys.exit(main())
