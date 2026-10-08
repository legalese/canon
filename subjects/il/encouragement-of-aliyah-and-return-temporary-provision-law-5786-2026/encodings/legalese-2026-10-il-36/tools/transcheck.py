#!/usr/bin/env python3
"""Check the deposited transcription of the Law against the PDF's own text layer.

The PDF's pdftotext extraction has Hebrew words in logical order but scrambles digits,
hyphens and the parentheses around numerals (bidi reordering), so the Law's text was
transcribed by reading the page images (PDF pp. 4-6) and is checked here: the multiset of
Hebrew words and the multiset of digit runs of the transcription must equal those of the
extraction's chapter D region (from the heading of chapter D to the heading of chapter E),
page furniture removed.  It does not check word order or the order of digits.

Usage: transcheck.py PDF TRANSCRIPTION      (needs pdftotext)
Exit 1 if the multisets differ; each difference is printed."""
import re
import subprocess
import sys
from collections import Counter

pdf, trans = sys.argv[1], sys.argv[2]
raw = subprocess.run(["pdftotext", "-layout", "-f", "4", "-l", "6", pdf, "-"],
                     capture_output=True, text=True, check=True).stdout
raw = re.sub("[‪-‮‎‏⁦-⁩]", "", raw)
lines = raw.split("\n")
start = next(i for i, l in enumerate(lines) if "פרק ד'" in l)
end = next(i for i, l in enumerate(lines) if "פרק ה'" in l)
region = [l for l in lines[start:end] if "םיקוחה" not in l]
# the two folio numbers 416 / 417 stand alone on furniture lines that were removed above
text = "\n".join(region)
mine = open(trans, encoding="utf-8").read()
# the transcriber's own label line, not in the PDF
mine = "\n".join(l for l in mine.split("\n") if l.strip() != "הערות שוליים:")
# the superscript footnote reference marks 6, 7, 8 and 9 stand in the extract's running text once
# each and are not transcribed (the footnotes themselves are)
FOOTNOTE_MARKS = Counter({"6": 1, "7": 1, "8": 1, "9": 1})


def tokens(s):
    s = s.replace("״", '"').replace("׳", "'")
    he = Counter(re.findall(r"[א-ת]+", s))
    num = Counter(n.replace(",", "") for n in re.findall(r"\d[\d,]*\d|\d", s))
    return he, num


he_p, num_p = tokens(text)
he_t, num_t = tokens(mine)
num_t = num_t + FOOTNOTE_MARKS
bad = 0
for label, a, b in (("word", he_p, he_t), ("number", num_p, num_t)):
    for k in sorted(set(a) | set(b)):
        if a[k] != b[k]:
            print(f"{label} {k!r}: pdf extract {a[k]}, transcription {b[k]}")
            bad += 1
print("transcheck:", "OK" if not bad else f"{bad} difference(s)")
sys.exit(1 if bad else 0)
