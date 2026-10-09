#!/usr/bin/env python3
"""Every Hebrew run in a `-- act: <label> | <text>` comment must occur in the text layer of
one of the deposited amending-law PDFs (pdftotext, bidi controls, spaces and quotation marks
removed on both sides). The Acts' text layers scramble digits and parentheses, so only runs of
Hebrew letters are checked here; figures and parentheses were read from the page images
(NOTES.md section 7). Prints each run that does not occur, with file:line. Exit 1 if any.

Usage: actcheck.py AMENDING_LAWS_DIR FILE.l4 [FILE.l4 ...]
"""
import glob
import re
import subprocess
import sys

amend_dir, files = sys.argv[1], sys.argv[2:]
STRIP = re.compile(r"[\s‎‏‪-‮⁦-⁩﻿\"'׳״“”‘’]")
HEB = re.compile(r"[֐-׿]+(?:[ ־\-]+[֐-׿]+)*")


def norm(s):
    return STRIP.sub("", s)


layers = []
for pdf in sorted(glob.glob(amend_dir + "/*.pdf")):
    txt = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
    layers.append(norm(txt))
big = "\n".join(layers)

bad = 0
n = 0
for path in files:
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        m = re.match(r"\s*-- act: [^|]*\|(.*)$", line)
        if not m:
            continue
        for run in HEB.findall(m.group(1)):
            n += 1
            if norm(run) not in big:
                bad += 1
                print(f"{path}:{i}: not in any text layer: {run}")
print(f"{n} runs checked, {bad} not found")
sys.exit(1 if bad else 0)
