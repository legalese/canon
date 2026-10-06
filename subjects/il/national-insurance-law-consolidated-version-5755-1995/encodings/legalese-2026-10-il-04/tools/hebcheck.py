#!/usr/bin/env python3
"""Every run of Hebrew in a .l4/.md/.json file, outside a `src:N |` quotation line, must occur
verbatim in the source file (raw, or as srcquote.py reduces it). Prints each run that does not,
with file:line. Exit 1 if any.

A run starts and ends on a Hebrew letter (or geresh/gershayim) and may contain spaces, digits,
Hebrew punctuation, the maqaf and the en dash in between. ASCII quotes and brackets end a run,
so a run is never padded with the encoder's own punctuation. The convention follows row
legalese-2026-10-il-03's tool of the same name; the reducer is the one in srcquote.py, repeated
here so that the script runs alone under `python3 -I`.

Usage: python3 -I hebcheck.py SOURCE.wiki.txt FILE [FILE ...]
"""
import re
import sys

INNER = re.compile(r"\{\{([^{}]*)\}\}")


def _amend(args):
    a = [x for x in args if x.startswith("תיקון")]
    return (" [" + a[0] + "]") if a else ""


def reduce_template(m):
    parts = m.group(1).split("|")
    name, args = parts[0], parts[1:]
    if name in ("ח:פנימי", "ח:חיצוני"):
        return args[-1] if args else ""
    if name == "ח:הערה":
        return "[note: " + "|".join(args) + "]"
    if name.startswith("ח:ת") and name.strip("ח:ת") == "":
        return "".join(a for a in args if not a.startswith("סוג="))
    if name == "ח:סעיף":
        num = args[0] if args else ""
        head = args[1] if len(args) > 1 else ""
        return (f"סעיף {num} – {head}".rstrip(" –")) + _amend(args[2:])
    if name == "ח:סעיף*":
        return _amend(args).strip()
    if name in ("ח:קטע1", "ח:קטע2", "ח:קטע3", "ח:קטע4"):
        vis = [a for a in args[1:] if a and not a.startswith("תיקון") and not a.startswith("אחר=")]
        return " ".join(vis) + _amend(args)
    if name == "מוקטן":
        return args[0] if args else ""
    return m.group(0).replace("{{", "⟦").replace("}}", "⟧")


def clean(line):
    prev = None
    while prev != line:
        prev = line
        line = INNER.sub(reduce_template, line)
    line = re.sub(r"(?i)</t[dh]>", " |", line)
    line = re.sub(r"<[^>]+>", " ", line)
    line = line.replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", line).strip()


def main():
    raw = open(sys.argv[1], encoding="utf-8").read()
    src = raw + "\n" + "\n".join(clean(l) for l in raw.split("\n"))
    letter = "א-ת׳״"
    inner = letter + "־– 0-9,.;:"
    heb = re.compile(f"[{letter}][{inner}]*[{letter}]|[{letter}]")
    bad = 0
    for path in sys.argv[2:]:
        with open(path, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if re.search(r"--\s*src:\d+ \|", line):
                    continue
                for m in heb.finditer(line):
                    run = m.group(0).strip()
                    if run not in src:
                        bad += 1
                        print(f"{path.split('/')[-1]}:{n}: NOT IN SOURCE: {run}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
