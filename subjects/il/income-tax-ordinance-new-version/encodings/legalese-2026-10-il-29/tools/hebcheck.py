#!/usr/bin/env python3
# Adapted 2026-10-09 for row IL-29 from ../../legalese-2026-10-il-28/tools/hebcheck.py (itself from IL-08; reducer copied unchanged).
# Changes: five deposited sources (the union is checked), and `-- src:TAG:N |` quotation lines are skipped
# for the run check but each is checked to be exactly the reduction of that source line.
"""Every run of Hebrew in a .l4/.md file, outside a `src:TAG:N |` line, must occur verbatim in one of the five
sources; every `src:TAG:N | text` line must equal the reduction of line N of source TAG. Exit 1 if any fails.

Usage: hebcheck.py FILE [FILE ...]"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import srcquote as sq  # noqa: E402  (importing runs nothing: its work is under __main__)

LINES = {t: sq.load(t) for t in sq.SOURCES}
RAW = "\n".join("\n".join(v) for v in LINES.values())
SRC = RAW + "\n" + "\n".join(sq.clean(l) for v in LINES.values() for l in v)
LETTER = "א-ת׳״"
INNER = LETTER + "־– 0-9,.;:"
HEB = re.compile(f"[{LETTER}][{INNER}]*[{LETTER}]|[{LETTER}]")
SRCLINE = re.compile(r"--\s*src:(ITO|RES|VEH|VTP|TEL):(\d+) \| (.*)$")
bad = 0
nq = 0
for path in sys.argv[1:]:
    for n, line in enumerate(pathlib.Path(path).read_text(encoding="utf-8").split("\n"), 1):
        m = SRCLINE.search(line)
        if m:
            nq += 1
            want = sq.clean(LINES[m.group(1)][int(m.group(2)) - 1])
            if m.group(3).strip() != want:
                bad += 1
                print(f"{pathlib.Path(path).name}:{n}: QUOTATION DIFFERS FROM {m.group(1)} LINE {m.group(2)}")
            continue
        for h in HEB.finditer(line):
            run = h.group(0).strip()
            if run not in SRC:
                bad += 1
                print(f"{pathlib.Path(path).name}:{n}: NOT IN SOURCE: {run}")
print(f"hebcheck: {nq} source quotations verified line by line; {bad} problem(s)")
sys.exit(1 if bad else 0)
