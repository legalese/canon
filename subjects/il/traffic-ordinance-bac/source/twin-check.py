#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove the Hebrew-canonical row is the English row, renamed.

    python3 subjects/il/traffic-ordinance-bac/source/twin-check.py          # structural check
    ... | python3 subjects/il/traffic-ordinance-bac/source/twin-check.py --unmap   # filter

Both rows are written by hand (the encoding is ~150 lines), so something mechanical has
to hold them together. This script does two things:

  1. STRUCTURAL. It tokenises each English module and its Hebrew twin -- backtick spans,
     string literals and bare words -- after dropping comments (`--` to end of line) and
     annotation text (`@nlg`, `@desc`, `@export` to end of line). It maps every English
     token through ../encodings/legalese-he/glossary.json and requires the result to be
     IDENTICAL, token for token, to the Hebrew module. So the two rows can differ in
     names, comments and heralds, and in nothing else: not a number, not a keyword, not
     the shape of a CONSIDER. The first divergence is reported with both line numbers.

  2. `--unmap`. Reads the Hebrew row's `l4 run` output on stdin and writes it with the
     English names, so check.sh can diff the two rows' Result blocks. The inverse is well
     defined because the glossary is checked for injectivity first.

The English row is the ORACLE. A failure here is fixed in the Hebrew row or the glossary.
Python 3 standard library only.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJECT = os.path.dirname(HERE)
EN_DIR = os.path.join(SUBJECT, "encodings", "legalese")
HE_DIR = os.path.join(SUBJECT, "encodings", "legalese-he")
GLOSSARY = os.path.join(HE_DIR, "glossary.json")

ANNOT = re.compile(r"@(nlg|desc|export|ref)\b")


def load_glossary():
    with open(GLOSSARY, encoding="utf-8") as fh:
        g = json.load(fh)
    names = {k: v["he"] for k, v in g["names"].items()}
    names.update(g["modules"])
    seen = {}
    for en, he in names.items():
        if he in seen:
            sys.exit("glossary is not injective: %r and %r both map to %r" % (seen[he], en, he))
        seen[he] = en
    return g, names


def strip_line(line):
    """Drop a trailing comment or annotation, neither of which starts inside backticks or quotes."""
    i, n = 0, len(line)
    while i < n:
        c = line[i]
        if c == "`":
            j = line.find("`", i + 1)
            i = n if j < 0 else j + 1
            continue
        if c == '"':
            j = line.find('"', i + 1)
            i = n if j < 0 else j + 1
            continue
        if line.startswith("--", i):
            return line[:i]
        if c == "@" and ANNOT.match(line, i):
            return line[:i]
        i += 1
    return line


TOKEN = re.compile(r"`[^`]*`|\"[^\"]*\"|'s\b|[^\s`\"']+|'")


def tokens(path):
    """Yield (line_number, token) for every code token in the file."""
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            for m in TOKEN.finditer(strip_line(line)):
                yield n, m.group(0)


def rename(tok, names):
    if tok.startswith("`") and tok.endswith("`"):
        inner = tok[1:-1]
        return "`" + names.get(inner, inner) + "`"
    return names.get(tok, tok)


def structural(g, names):
    status = 0
    for en_stem, he_stem in g["modules"].items():
        en_path = os.path.join(EN_DIR, en_stem + ".l4")
        he_path = os.path.join(HE_DIR, he_stem + ".l4")
        en = list(tokens(en_path))
        he = list(tokens(he_path))
        k = 0
        bad = None
        for k in range(max(len(en), len(he))):
            e = en[k] if k < len(en) else (None, "<end of file>")
            h = he[k] if k < len(he) else (None, "<end of file>")
            if rename(e[1], names) != h[1]:
                bad = (e, h)
                break
        if bad:
            status = 1
            (el, et), (hl, ht) = bad
            print("%-30s DIVERGES from %s at token %d:" % (he_stem + ".l4", en_stem + ".l4", k + 1))
            print("    %s line %s: %s  ->  expected %s" % (en_stem + ".l4", el, et, rename(et, names)))
            print("    %s line %s: %s" % (he_stem + ".l4", hl, ht))
        else:
            renamed = sum(1 for _, t in en if rename(t, names) != t)
            print("%-30s is %s renamed: %d tokens identical, %d of them through the glossary"
                  % (he_stem + ".l4", en_stem + ".l4", len(en), renamed))
    # Every glossary entry should be earning its keep.
    used = set()
    for en_stem in g["modules"]:
        for _, t in tokens(os.path.join(EN_DIR, en_stem + ".l4")):
            used.add(t[1:-1] if t.startswith("`") else t)
    for k in sorted(set(g["names"]) - used):
        print("warning: glossary entry %r is not used by any English module" % k)
    return status


def unmap_bare(names):
    """Rewrite the Hebrew row's run output with English names. A one-word enum constructor
    prints bare (שיכור), a multi-word one backticked (`אינו שיכור`); both are mapped."""
    inverse = {v: k for k, v in names.items()}
    out = []
    for line in sys.stdin.read().split("\n"):
        s = line.strip()
        if s in inverse:
            line = line.replace(s, "`" + inverse[s] + "`") if " " in inverse[s] else line.replace(s, inverse[s])
        out.append(re.sub(r"`([^`]*)`", lambda m: "`" + inverse.get(m.group(1), m.group(1)) + "`", line))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    g, names = load_glossary()
    if "--unmap" in sys.argv[1:]:
        unmap_bare(names)
        sys.exit(0)
    sys.exit(structural(g, names))
