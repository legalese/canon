#!/usr/bin/env python3
# Row IL-27 (2026-10-09). Derived from ../../legalese-2026-10-il-08/tools/srcquote.py and hebcheck.py
# (which are row IL-03's scripts); the template reducer is theirs, unchanged. Two changes: it takes
# several sources, because this row quotes the Ordinance, two sets of rules and the Retirement Age
# Law; and one script both expands the markers and checks them (`--check`), because rows IL-03 to
# IL-08 used two.
"""Expand and check source quotations in .l4 files from the deposited wiki texts.

Usage:  srcquote.py [--check] ito=PATH reg35=PATH reg47=PATH ral=PATH -- FILE.l4 [FILE.l4 ...]

A marker line      `<indent>--@SRC 1778-1782`          quotes lines of the Ordinance (the first source)
                   `<indent>--@SRC reg47:12-13`        quotes lines of another source, by its tag
becomes one comment line per non-empty source line:
                   `<indent>-- src:1778 | (ב) יחיד ...`          (the first source)
                   `<indent>-- ext:[reg47:12] | ...`             (another source)
A previously expanded line is regenerated from its own number, so the script is idempotent.

--check expands nothing. It exits 1 if any expanded line differs from the source line it names, or
if a run of Hebrew outside a quotation line does not occur verbatim in some source."""
import re
import sys

args = sys.argv[1:]
check = False
if args and args[0] == "--check":
    check = True
    args = args[1:]
cut = args.index("--")
srcs = {}
order = []
for a in args[:cut]:
    tag, path = a.split("=", 1)
    with open(path, encoding="utf-8") as fh:
        srcs[tag] = fh.read().split("\n")
    order.append(tag)
files = args[cut + 1:]
DEFAULT = order[0]

INNER = re.compile(r"\{\{([^{}]*)\}\}")


def reduce_template(m):
    parts = m.group(1).split("|")
    name = parts[0]
    a = [p for p in parts[1:]]
    if name in ("ח:פנימי", "ח:חיצוני"):
        return a[-1] if a else ""
    if name == "ח:הערה":
        return "[note: " + "|".join(a) + "]"
    if name.startswith("ח:ת"):  # ח:ת ח:תת ח:תתת ח:תתתת
        labels = [x for x in a if not x.startswith("סוג=")]
        return "".join(labels)
    if name == "ח:סעיף":
        num = a[0] if a else ""
        head = a[1] if len(a) > 1 else ""
        amend = [x for x in a[2:] if x.startswith("תיקון")]
        tail = (" [" + amend[0] + "]") if amend else ""
        return (f"סעיף {num} – {head}".rstrip(" –")) + tail
    if name == "ח:סעיף*":
        return ""
    if name == "ח:קטע1":
        return a[-1] if a else ""
    return m.group(0).replace("{{", "⟦").replace("}}", "⟧")


def clean(line):
    prev = None
    while prev != line:
        prev = line
        line = INNER.sub(reduce_template, line)
    line = re.sub(r"<[^>]+>", " ", line)
    return re.sub(r"\s+", " ", line).strip()


MARK = re.compile(r"^(\s*)--(?:@SRC\s+(?:(\w+):)?|\s*src:|\s*ext:\[(\w+):)(\d+)(?:-(\d+))?(?:\]?\s*\|.*)?$")


def line_of(tag, n):
    return clean(srcs[tag][n - 1])


bad = 0
if check:
    union = ""
    for tag in order:
        raw = "\n".join(srcs[tag])
        union += raw + "\n" + "\n".join(clean(x) for x in srcs[tag]) + "\n"
    LETTER = "א-ת׳״"
    INN = LETTER + "־– 0-9,.;:"
    HEB = re.compile(f"[{LETTER}][{INN}]*[{LETTER}]|[{LETTER}]")
for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    for ln_no, ln in enumerate(lines, 1):
        m = MARK.match(ln)
        if m:
            indent, tag1, tag2, a, b = m.group(1), m.group(2), m.group(3), int(m.group(4)), int(m.group(5) or m.group(4))
            if "ext:[" in ln:
                tag = tag2
            elif "--@SRC" in ln:
                tag = tag1 or DEFAULT
            else:
                tag = DEFAULT
            if check:
                if a != b:
                    print(f"{path.split('/')[-1]}:{ln_no}: expanded line with a range")
                    bad += 1
                    continue
                want = line_of(tag, a)
                prefix = f"-- src:{a} | " if tag == DEFAULT else f"-- ext:[{tag}:{a}] | "
                if ln.strip() != prefix + want:
                    print(f"{path.split('/')[-1]}:{ln_no}: DIFFERS FROM SOURCE {tag}:{a}")
                    bad += 1
                continue
            for n in range(a, b + 1):
                text = line_of(tag, n)
                if text:
                    pre = f"-- src:{n} | " if tag == DEFAULT else f"-- ext:[{tag}:{n}] | "
                    out.append(indent + pre + text)
            continue
        if check:
            for h in HEB.finditer(ln):
                run = h.group(0).strip()
                if run not in union:
                    print(f"{path.split('/')[-1]}:{ln_no}: NOT IN ANY SOURCE: {run}")
                    bad += 1
        else:
            out.append(ln)
    if not check:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
sys.exit(1 if bad else 0)
