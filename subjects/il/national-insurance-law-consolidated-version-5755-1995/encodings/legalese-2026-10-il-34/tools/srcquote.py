#!/usr/bin/env python3
# Copied unchanged (below this line) from ../../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/tools/srcquote.py on 2026-10-06.
"""Expand source-quotation markers in .l4 files, in place, from the deposited wiki text.

A line   `<indent>--@SRC 4351`      or `<indent>--@SRC 4351-4353`
or a previously expanded line `<indent>-- src:4351 | ...`
becomes one comment line per source line:
         `<indent>-- src:4351 | (1) על כל שקל חדש ...`

Templates are reduced mechanically: subsection labels kept, link templates reduced to their
visible text, editorial notes kept and marked [note: ...]. Nothing is typed by hand.

Usage: srcquote.py SOURCE.wiki.txt FILE.l4 [FILE.l4 ...]
"""
import re
import sys

src_path, files = sys.argv[1], sys.argv[2:]
with open(src_path, encoding="utf-8") as fh:
    SRC = fh.read().split("\n")

INNER = re.compile(r"\{\{([^{}]*)\}\}")


def reduce_template(m):
    parts = m.group(1).split("|")
    name = parts[0]
    args = [p for p in parts[1:]]
    if name in ("ח:פנימי", "ח:חיצוני"):
        return args[-1] if args else ""
    if name == "ח:הערה":
        return "[note: " + "|".join(args) + "]"
    if name.startswith("ח:ת"):  # ח:ת ח:תת ח:תתת ח:תתתת
        labels = [a for a in args if not a.startswith("סוג=")]
        return "".join(labels)
    if name == "ח:סעיף":
        num = args[0] if args else ""
        head = args[1] if len(args) > 1 else ""
        amend = [a for a in args[2:] if a.startswith("תיקון")]
        tail = (" [" + amend[0] + "]") if amend else ""
        return (f"סעיף {num} – {head}".rstrip(" –")) + tail
    if name == "ח:סעיף*":
        return ""
    if name == "ח:קטע1":
        return args[-1] if args else ""
    return m.group(0).replace("{{", "⟦").replace("}}", "⟧")


def clean(line):
    prev = None
    while prev != line:
        prev = line
        line = INNER.sub(reduce_template, line)
    line = re.sub(r"<[^>]+>", " ", line)
    return re.sub(r"\s+", " ", line).strip()


MARK = re.compile(r"^(\s*)--(?:@SRC |\s*src:)(\d+)(?:-(\d+))?(?:\s*\|.*)?$")

for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    for ln in lines:
        m = MARK.match(ln)
        if not m:
            out.append(ln)
            continue
        indent, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        for n in range(a, b + 1):
            text = clean(SRC[n - 1])
            if text:
                out.append(f"{indent}-- src:{n} | {text}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
