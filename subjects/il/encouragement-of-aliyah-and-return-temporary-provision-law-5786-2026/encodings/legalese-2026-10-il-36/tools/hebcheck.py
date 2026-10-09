#!/usr/bin/env python3
"""Every run of Hebrew in a .l4/.md file, outside a `src:N |` quotation line, must occur
verbatim in the deposited transcription.  Prints each run that does not, with file:line.
Exit 1 if any.

A run starts and ends on a Hebrew letter (or geresh/gershayim) and may contain spaces, digits,
Hebrew punctuation, the maqaf and the en dash in between.  ASCII quotes and brackets end a run,
so a run is never padded with the encoder's own punctuation.  Lines tagged `-- ext:[TAG] |`
quote a source other than the Law and are skipped (NOTES.md lists them)."""
import re
import sys

src = open(sys.argv[1], encoding="utf-8").read()
src = re.sub(r"\s+", " ", src)
LETTER = "א-ת׳״"
INNER = LETTER + "־– 0-9,.;:"
HEB = re.compile(f"[{LETTER}][{INNER}]*[{LETTER}]|[{LETTER}]")
bad = 0
for path in sys.argv[2:]:
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if re.match(r"\s*-- (src:\d+|ext:\[[^\]]*\]) \|", line):
                continue
            for run in HEB.findall(line):
                if re.sub(r"\s+", " ", run) not in src:
                    print(f"{path}:{n}: not in the transcription: {run}")
                    bad += 1
print("hebcheck:", "OK" if not bad else f"{bad} run(s) not found")
sys.exit(1 if bad else 0)
