#!/usr/bin/env python3
# Adapted 2026-10-09 for row IL-29 from ../../legalese-2026-10-il-28/tools/srcquote.py (template reducer copied
# unchanged). The one change: this row quotes the Ordinance and four deposited instruments, named by TAG.
"""Expand source-quotation markers in .l4 files, in place, from the deposited wiki texts.

A marker  `<indent>--@SRC TAG 1807`  or  `<indent>--@SRC TAG 1807-1808`,
or a previously expanded line  `<indent>-- src:TAG:1807 | ...`,
becomes one comment line per source line:  `<indent>-- src:TAG:1807 | <Hebrew>`.

TAG is ITO (the Income Tax Ordinance), RES (the deemed-residents Regulations 5766-2006), VEH (the vehicle
value Regulations 5747-1987), VTP (the vehicle value temporary provision Regulations 5776-2015) or TEL (the
mobile telephone value Regulations 5762-2002). Nothing is typed by hand.

Usage: srcquote.py FILE.l4 [FILE.l4 ...]
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ITO_DIR = (HERE / "../../../registers/source-bundle").resolve()
SOURCES = {
    "ITO": ITO_DIR / "income-tax-ordinance-new-version.he.wiki.txt",
    "RES": ITO_DIR / "regulations/income-tax-individuals-deemed-israeli-residents-regulations-5766-2006.he.wiki.txt",
    "VEH": ITO_DIR / "regulations/income-tax-value-of-use-of-vehicle-regulations-5747-1987.he.wiki.txt",
    "VTP": ITO_DIR / "regulations/income-tax-value-of-use-of-vehicle-temporary-provision-regulations-5776-2015.he.wiki.txt",
    "TEL": ITO_DIR / "regulations/income-tax-value-of-use-of-mobile-radio-telephone-regulations-5762-2002.he.wiki.txt",
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
    MARK = re.compile(r"^(\s*)--(?:@SRC |\s*src:)(ITO|RES|VEH|VTP|TEL)[ :](\d+)(?:-(\d+))?(?:\s*\|.*)?$")
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
