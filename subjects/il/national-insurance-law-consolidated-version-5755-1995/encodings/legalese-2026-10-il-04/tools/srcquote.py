#!/usr/bin/env python3
"""Expand source-quotation markers in .l4 files, in place, from the deposited wiki text.

A line   `<indent>--@SRC 3605`      or `<indent>--@SRC 3605-3607`
or a previously expanded line `<indent>-- src:3605 | ...`
becomes one comment line per source line:
         `<indent>-- src:3605 | "מדרגת גבייה מופחתת" – ...`

Templates are reduced mechanically: subsection labels kept, link templates reduced to their
visible text, editorial notes kept and marked [note: ...], table cells separated by " |".
Nothing is typed by hand. The convention (and most of this reducer) follows the tools of row
legalese-2026-10-il-03 of the Income Tax Ordinance; this copy is self-contained so that it runs
under `python3 -I`, and it also reduces the schedule templates (ח:קטע2-4, מוקטן) that row did not meet.

Usage: python3 -I srcquote.py SOURCE.wiki.txt FILE.l4 [FILE.l4 ...]
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
    if name.startswith("ח:ת") and name.strip("ח:ת") == "":  # ח:ת ח:תת ח:תתת ח:תתתת
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


MARK = re.compile(r"^(\s*)--(?:@SRC |\s*src:)(\d+)(?:-(\d+))?(?:\s*\|.*)?$")


def main():
    src_path, files = sys.argv[1], sys.argv[2:]
    with open(src_path, encoding="utf-8") as fh:
        src = fh.read().split("\n")
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
                text = clean(src[n - 1])
                if text:
                    out.append(f"{indent}-- src:{n} | {text}")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))


if __name__ == "__main__":
    main()
