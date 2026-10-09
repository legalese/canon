#!/usr/bin/env python3
# Adapted 2026-10-09 for row IL-28 from ../../legalese-2026-10-il-08/tools/srcquote.py (template reducer copied
# unchanged). The one change: this row quotes four deposited sources, so a marker names its source.
"""Expand source-quotation markers in .l4 files, in place, from the deposited wiki texts.

A marker  `<indent>--@SRC TAG 1807`  or  `<indent>--@SRC TAG 1807-1808`,
or a previously expanded line  `<indent>-- src:TAG:1807 | ...`,
becomes one comment line per source line:  `<indent>-- src:TAG:1807 | <Hebrew>`.

TAG is ITO (the Income Tax Ordinance), ORD (the Area order of 5755-1995), REG (the foreign worker regulations
of 5775-2014) or FWL (the Foreign Workers Law 5751-1991). Nothing is typed by hand.

Usage: srcquote.py FILE.l4 [FILE.l4 ...]
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ITO_DIR = (HERE / "../../../registers/source-bundle").resolve()
SOURCES = {
    "ITO": ITO_DIR / "income-tax-ordinance-new-version.he.wiki.txt",
    "ORD": ITO_DIR / "regulations/income-tax-credits-for-residents-of-the-area-order-5755-1995.he.wiki.txt",
    "REG": ITO_DIR / "regulations/income-tax-credits-for-foreign-worker-regulations-5775-2014.he.wiki.txt",
    "FWL": (HERE / "../../../../foreign-workers-law-5751-1991/registers/source-bundle/foreign-workers-law-5751-1991.he.wiki.txt").resolve(),
}
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


def load(tag):
    return SOURCES[tag].read_text(encoding="utf-8").split("\n")


if __name__ == "__main__":
    cache = {}
    MARK = re.compile(r"^(\s*)--(?:@SRC |\s*src:)(ITO|ORD|REG|FWL)[ :](\d+)(?:-(\d+))?(?:\s*\|.*)?$")
    for path in sys.argv[1:]:
        lines = pathlib.Path(path).read_text(encoding="utf-8").split("\n")
        out = []
        for ln in lines:
            m = MARK.match(ln)
            if not m:
                out.append(ln)
                continue
            indent, tag, a, b = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
            src = cache.setdefault(tag, load(tag))
            for n in range(a, b + 1):
                text = clean(src[n - 1])
                if text:
                    out.append(f"{indent}-- src:{tag}:{n} | {text}")
        pathlib.Path(path).write_text("\n".join(out), encoding="utf-8")
