#!/usr/bin/env python3
"""Expand source-quotation markers in .l4 files, in place, from the deposited transcription.

A line   `<indent>--@SRC 12`      or `<indent>--@SRC 12-14`
or a previously expanded line `<indent>-- src:12 | ...`
becomes one comment line per source line:
         `<indent>-- src:12 | (1) בשנת המס 2026 – ...`

The transcription (registers/source-bundle/*.he.txt) is one printed clause per line; nothing is
reduced or typed by hand.  Adapted from the srcquote.py of row legalese-2026-10-il-06, which
reduced MediaWiki templates; this source has none.

Usage: srcquote.py TRANSCRIPTION.he.txt FILE.l4 [FILE.l4 ...]"""
import re
import sys

src_path, files = sys.argv[1], sys.argv[2:]
with open(src_path, encoding="utf-8") as fh:
    SRC = fh.read().split("\n")
if SRC and SRC[-1] == "":
    SRC.pop()

MARK = re.compile(r"^(\s*)--@SRC (\d+)(?:-(\d+))?\s*$")
OLD = re.compile(r"^(\s*)-- src:(\d+) \|.*$")

for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out, i = [], 0
    while i < len(lines):
        m = MARK.match(lines[i])
        if m:
            indent, a = m.group(1), int(m.group(2))
            b = int(m.group(3)) if m.group(3) else a
            for n in range(a, b + 1):
                out.append(f"{indent}-- src:{n} | {SRC[n - 1]}")
            i += 1
            continue
        o = OLD.match(lines[i])
        if o:
            indent, n = o.group(1), int(o.group(2))
            out.append(f"{indent}-- src:{n} | {SRC[n - 1]}")
            i += 1
            continue
        out.append(lines[i])
        i += 1
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
