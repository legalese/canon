#!/usr/bin/env python3
"""Expand the quotation markers of templates/*.l4.in into the generated `-- src:` lines of *.l4.

This is the encoder's own helper (not part of the lead's toolkit). The Vietnamese in the
modules is never typed: a template line

    @@q   N [M]     becomes  -- src:N | <line N>  ...  of law08-2022-qh15.txt
    @@qb  N [M]     becomes  -- src:law08-2022-qh15-577-578:N | ...
    @@qa  N [M]     becomes  -- src:law139-2025-qh15:N | ...

by calling tools/vnsrc.py's own quote routine, with the marker's indentation kept.

A test fixture line

    @@fx `fixture name` : `Record type` ; `field` = VALUE ; `field` = VALUE

becomes `fixture name` MEANS `Record type` WITH followed by EVERY field of the record, as
declared in law08-nouns.l4, with the given VALUEs and FALSE / 0 / YMD 2000 1 1 / NOTHING / EMPTY
for a BOOLEAN / NUMBER / DATE / MAYBE / LIST field not given. A field of any other type must be
given. This keeps a fixture short without hiding a field the reader should see.

  python3 -I tools/expand.py            expand every templates/*.l4.in into ./NAME.l4
  python3 -I tools/expand.py NAME ...   expand only templates/NAME.l4.in
"""
import glob, importlib.util, io, contextlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEPOSIT = os.path.dirname(HERE)
RAW = os.path.normpath(os.path.join(DEPOSIT, "..", "..", "source", "raw"))
FILES = {
    "q": os.path.join(RAW, "law08-2022-qh15.txt"),
    "qb": os.path.join(RAW, "law08-2022-qh15-577-578.txt"),
    "qa": os.path.join(RAW, "law139-2025-qh15.txt"),
}

spec = importlib.util.spec_from_file_location("vnsrc", os.path.join(HERE, "vnsrc.py"))
vnsrc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vnsrc)

FX = re.compile(r"^(\s*)@@fx\s+(`[^`]+`)\s*:\s*(`[^`]+`)\s*(.*)$")
_records = None


def records():
    """{record name: [(field, type)]} for every DECLARE ... HAS in law08-nouns.l4."""
    global _records
    if _records is None:
        _records, cur = {}, None
        for line in open(os.path.join(DEPOSIT, "law08-nouns.l4"), encoding="utf-8"):
            m = re.match(r"^DECLARE\s+(`[^`]+`|\w+)\s+HAS\s*$", line.rstrip())
            if m:
                cur = m.group(1)
                _records[cur] = []
                continue
            f = re.match(r"^\s+(`[^`]+`)\s+IS\s+(?:A|AN)\s+(.+?)\s*$", line.rstrip())
            if f and cur:
                _records[cur].append((f.group(1), f.group(2)))
            elif line.strip() and not line.startswith((" ", "\t", "--")):
                cur = None
    return _records


def default(ty):
    if ty == "BOOLEAN":
        return "FALSE"
    if ty == "NUMBER":
        return "0"
    if ty == "DATE":
        return "YMD 2000 1 1"
    if ty == "STRING":
        return '""'
    if ty.startswith("MAYBE "):
        return "NOTHING"
    if ty.startswith("LIST OF"):
        return "EMPTY"
    return None


def fixture(m, path, ln):
    ind, name, rec, rest = m.groups()
    fields = records().get(rec)
    if fields is None:
        sys.exit(f"{path}:{ln}: no record {rec} in law08-nouns.l4")
    given, cur, depth = {}, "", False
    parts = []
    for ch in rest:
        if ch == "`":
            depth = not depth
        if ch == ";" and not depth:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        k = re.match(r"^(`[^`]+`)\s*=\s*(.+)$", part)
        if not k:
            sys.exit(f"{path}:{ln}: cannot read override {part!r}")
        if k.group(1) not in [f for f, _ in fields]:
            sys.exit(f"{path}:{ln}: {rec} has no field {k.group(1)}")
        given[k.group(1)] = k.group(2).strip()
    out = [f"{ind}{name} MEANS {rec} WITH"]
    for f, ty in fields:
        v = given.get(f, default(ty))
        if v is None:
            sys.exit(f"{path}:{ln}: field {f} of {rec} ({ty}) has no default: give it")
        out.append(f"{ind}    {f} IS {v}")
    return out


MARK = re.compile(r"^(\s*)@@(q|qb|qa)\s+(\d+)(?:\s+(\d+))?\s*$")


def quote(kind, n, m):
    args = [FILES[kind], str(n)] + ([str(m)] if m else [])
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        vnsrc.cmd_quote(args, qualified=(kind != "q"))
    return buf.getvalue().splitlines()


def expand(path):
    out = []
    for ln, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        fx = FX.match(line)
        if fx:
            out += fixture(fx, path, ln)
            continue
        m = MARK.match(line)
        if not m:
            out.append(line)
            continue
        got = quote(m.group(2), m.group(3), m.group(4))
        if not got:
            sys.exit(f"{path}:{ln}: marker quotes no non-blank line")
        out += [m.group(1) + g for g in got]
    return "\n".join(out)


def main():
    names = sys.argv[1:] or [os.path.basename(p)[: -len(".l4.in")] for p in sorted(glob.glob(os.path.join(DEPOSIT, "templates", "*.l4.in")))]
    for name in names:
        src = os.path.join(DEPOSIT, "templates", name + ".l4.in")
        dst = os.path.join(DEPOSIT, name + ".l4")
        open(dst, "w", encoding="utf-8").write(expand(src))
        print(f"expanded {name}.l4.in -> {name}.l4")


if __name__ == "__main__":
    main()
