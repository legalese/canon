#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emit the Hebrew-canonical encoding row `legalese-he` from the English row `legalese`.

The English row is the ORACLE. Nothing is re-derived here: every rule, every number and
every assertion is the English row's, with the identifiers renamed and the two heralds
swapped over. If a Hebrew module ever answers differently from its English twin, the bug
is in this script or in glossary.json, never in the English row.

    python3 subjects/il/hvac-work-licensing-2025/source/revoice.py

Reads   ../encodings/legalese/*.l4          (five modules)
        ../encodings/legalese-he/glossary.json
Writes  ../encodings/legalese-he/*.l4       (five modules, Latin basenames -- see NOTES.md)
        ../encodings/legalese-he/GLOSSARY.md

What it does, precisely:

  * Renames identifiers by EXACT TOKEN substitution. The file is tokenised (backtick spans,
    string literals, comments, annotations, bare identifiers) rather than text-searched, so
    "longest match first" never arises: a backticked name is matched as one whole token and
    a bare name only where it is a bare identifier. String literals, numbers, keywords and
    comment prose are never touched.
  * `@lang en` becomes `@lang he`.
  * Swaps the heralds. A rule reading
        DECIDE `x` @nlg <english>
                   @nlg:he <hebrew>
    is emitted as
        DECIDE `ח` @nlg <hebrew>
                   @nlg:en <english>
    so the UNTAGGED herald -- the one every annotation reader falls back to -- is the Hebrew
    one, which is what makes this row Hebrew-canonical rather than English with a translation.
  * Substitutes inside %name% placeholders in BOTH heralds, because a placeholder names a
    parameter and the parameters have been renamed.
  * Translates `@desc` and `@export` prose from the glossary's `prose` map.
  * Replaces the comment blocks that quote the statute IN TRANSLATION with the Hebrew
    original, from the glossary's `comment_blocks`. Every other comment stays English: this
    row is for Hebrew readers of the RULES; the commentary around them is addressed to
    whoever maintains the encoding.
  * Rewrites IMPORTs and the module filenames named in comments.

It refuses to write anything if the glossary is not injective, if a backticked identifier in
the English row has no entry, or if an `@nlg` has no paired `@nlg:he`.
"""

import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJECT = os.path.dirname(HERE)
EN_DIR = os.path.join(SUBJECT, "encodings", "legalese")
HE_DIR = os.path.join(SUBJECT, "encodings", "legalese-he")
GLOSSARY = os.path.join(HE_DIR, "glossary.json")

MODULES = [
    "hvac-law.l4",
    "hvac-fees.l4",
    "hvac-tests-simplex.l4",
    "hvac-tests-simplex-red.l4",
    "hvac-tests-generated.l4",
]

ANNOT = re.compile(r"@(lang|nlg:he|nlg:en|nlg|desc|export|ref)\b")
IDENT = re.compile(r"[A-Za-z][A-Za-z0-9]*")

USED = set()


class Fatal(Exception):
    pass


# --------------------------------------------------------------------------- glossary


def load_glossary():
    with open(GLOSSARY, encoding="utf-8") as fh:
        g = json.load(fh)
    names = {k: v["he"] for k, v in g["names"].items()}
    for en, he in g["modules"].items():
        names[en] = he
    keep = set(g["keep"])

    # Injectivity. Two identifiers that print the same string are one identifier to L4,
    # and the failure is a "multiple definitions" error a long way from the cause.
    seen = {}
    for en, he in names.items():
        if he in seen:
            raise Fatal(
                "glossary is not injective: %r and %r both map to %r" % (seen[he], en, he)
            )
        seen[he] = en

    # A bare identifier may carry no character L4's lexer would end the token on.
    # isAlpha/isAlphaNum, so a maqaf or a space is fatal there and fine inside backticks.
    for en, v in g["names"].items():
        if v["kind"] == "param" and en.islower() and " " not in en:
            he = v["he"]
            if not all(unicodedata.category(c) in ("Lo", "Lu", "Ll", "Nd") for c in he):
                raise Fatal(
                    "bare identifier %r maps to %r, which carries a character that would "
                    "split the token" % (en, he)
                )
    return g, names, keep


# --------------------------------------------------------------------------- the tokeniser


def split_line(line):
    """Return (code, annot_kind, annot_text, comment).

    Splits a source line at the first top-level annotation and the first top-level `--`,
    neither of which can start inside a backtick span or a string literal.
    """
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
        if c == "-" and line.startswith("--", i):
            return line[:i], None, None, line[i:]
        if c == "@":
            m = ANNOT.match(line, i)
            if m:
                return line[:i], m.group(1), line[m.end():].strip(), None
        i += 1
    return line, None, None, None


def rename_code(code, names, keep, uncovered):
    """Substitute identifiers in a stretch of CODE (no annotation, no comment)."""
    out, i, n = [], 0, len(code)
    while i < n:
        c = code[i]
        if c == "`":
            j = code.find("`", i + 1)
            if j < 0:
                out.append(code[i:])
                break
            inner = code[i + 1:j]
            if inner in names:
                USED.add(inner)
                out.append("`" + names[inner] + "`")
            else:
                if inner not in keep:
                    uncovered.add(inner)
                out.append(code[i:j + 1])
            i = j + 1
            continue
        if c == '"':
            j = code.find('"', i + 1)
            j = n - 1 if j < 0 else j
            out.append(code[i:j + 1])
            i = j + 1
            continue
        m = IDENT.match(code, i)
        if m:
            w = m.group(0)
            if w in names:
                USED.add(w)
            out.append(names.get(w, w))
            i = m.end()
            continue
        out.append(c)
        i += 1
    return "".join(out)


def rename_placeholders(text, names, keep, uncovered):
    """Rename only what sits between a matched pair of % delimiters in herald text."""

    def one(m):
        inner = m.group(1)
        if inner.startswith("`") and inner.endswith("`"):
            bare = inner[1:-1]
            if bare in names:
                USED.add(bare)
                return "%`" + names[bare] + "`%"
            if bare not in keep:
                uncovered.add(bare)
            return m.group(0)
        if inner in names:
            USED.add(inner)
            return "%" + names[inner] + "%"
        return m.group(0)

    return re.sub(r"%([^%]*)%", one, text)


# --------------------------------------------------------------------------- the pass


BANNER = [
    "-- GENERATED FILE -- DO NOT EDIT BY HAND.",
    "-- The Hebrew-canonical twin of ../legalese/%s, emitted from it by",
    "-- ../../source/revoice.py together with glossary.json in this directory.",
    "-- The English row is the oracle. Edit it, or the glossary, and re-run:",
    "--     python3 subjects/il/hvac-work-licensing-2025/source/revoice.py",
    "--",
]


def revoice(src_name, text, g, names, keep, uncovered, stats, used, hit_blocks):
    file_map = {k + ".l4": v + ".l4" for k, v in g["modules"].items()}
    blocks = [(n, b["en"], b["he"]) for n, b in enumerate(g["comment_blocks"])]
    lines = text.split("\n")

    out = []
    i = 0
    while i < len(lines):
        # 1. a comment block that quotes the statute in translation
        matched = None
        for n, en_block, he_block in blocks:
            k = len(en_block)
            if [l.strip() for l in lines[i:i + k]] == en_block:
                matched = (he_block, k)
                hit_blocks.add(n)
                stats["blocks"] += 1
                break
        if matched:
            he_block, k = matched
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())]
            out.extend(indent + l for l in he_block)
            i += k
            continue

        line = lines[i]
        code, kind, atext, comment = split_line(line)

        # 2. the herald swap: `@nlg <en>` here, `@nlg:he <he>` on the next line
        if kind == "nlg" and i + 1 < len(lines):
            nxt_code, nxt_kind, nxt_text, _ = split_line(lines[i + 1])
            if nxt_kind == "nlg:he" and nxt_code.strip() == "":
                new_code = rename_code(code, names, keep, uncovered).rstrip()
                he = rename_placeholders(nxt_text, names, keep, uncovered)
                en = rename_placeholders(atext, names, keep, uncovered)
                col = max(len(line) - len(line.lstrip()) + 1, len(new_code) + 1)
                first = new_code + " " * (col - len(new_code)) + "@nlg " + he
                out.append(first)
                out.append(" " * col + "@nlg:en " + en)
                stats["heralds"] += 1
                i += 2
                continue
            raise Fatal(
                "%s line %d: an @nlg with no @nlg:he under it -- the swap would lose a "
                "language.\n    %s" % (src_name, i + 1, line)
            )
        if kind == "nlg:he":
            raise Fatal("%s line %d: a stray @nlg:he" % (src_name, i + 1))

        # 3. everything else
        new_code = rename_code(code, names, keep, uncovered)
        rest = ""
        if kind == "lang":
            rest = "@lang he" if atext.strip() == "en" else "@lang " + atext
        elif kind in ("desc", "export"):
            if atext not in g["prose"]:
                raise Fatal("%s line %d: no translation for @%s %r" % (src_name, i + 1, kind, atext))
            rest = "@%s %s" % (kind, g["prose"][atext])
            stats["prose"] += 1
        elif kind:
            rest = "@%s %s" % (kind, rename_placeholders(atext, names, keep, uncovered))

        if rest:
            orig_col = len(line) - len(line.rstrip()) if False else line.index("@")
            head = new_code.rstrip()
            col = max(orig_col, len(head) + 1) if head else 0
            out.append(head + " " * (col - len(head)) + rest)
        elif comment is not None:
            c = comment
            for en_f, he_f in file_map.items():
                c = c.replace(en_f, he_f)
            out.append(new_code + c)
        else:
            out.append(new_code.rstrip() if new_code.strip() == "" else new_code)
        i += 1

    body = "\n".join(out)
    banner = "\n".join(l % src_name if "%s" in l else l for l in BANNER)
    return banner + "\n" + body


# --------------------------------------------------------------------------- GLOSSARY.md

KIND_ORDER = ["module", "type", "constructor", "field", "function", "param", "fixture", "section"]
KIND_TITLE = {
    "module": "Modules",
    "type": "Types",
    "constructor": "Constructors",
    "field": "Record fields",
    "function": "Rules and helper functions",
    "param": "Parameters and inputs",
    "fixture": "Fixtures",
    "section": "`§` headings",
}


def write_glossary_md(g):
    n = g["names"]
    by_source = {}
    for v in n.values():
        by_source[v["source"]] = by_source.get(v["source"], 0) + 1

    L = []
    L.append("# HVAC work licensing — the Hebrew term contract")
    L.append("")
    L.append("**GENERATED from `glossary.json` by `../../source/revoice.py`. Do not edit by hand.**")
    L.append("The JSON is the machine-readable form and the one to change; this page is the same map, readable.")
    L.append("")
    L.append("**What this is.** Every identifier of the English encoding at [`../legalese`](../legalese) — type names, constructors, record fields, rule names, parameters, fixtures and `§` headings — with the Hebrew name the Hebrew-canonical row [`.`](.) uses for it.")
    L.append("The English row is the oracle: renaming is all that happens, and every numeric assertion keeps its exact value.")
    L.append("")
    L.append("**Grounded in the instruments first.** A row marked `law`, `schedule` or `regulations` uses the instrument's own words and the note says where.")
    L.append("A row marked `composed` has no counterpart in either instrument and the note says why; those are the rows a Hebrew reviewer should read first.")
    L.append("")
    L.append("| provenance | entries |")
    L.append("| --- | --- |")
    for s in ("law", "schedule", "regulations", "composed"):
        if s in by_source:
            L.append("| `%s` | %d |" % (s, by_source[s]))
    L.append("| **total** | **%d** |" % len(n))
    L.append("")
    L.append("Two names are deliberately **not** renamed, because they are not ours: `add years` and `add months`, which the `daydate` library defines.")
    L.append("")

    for kind in KIND_ORDER:
        rows = [(k, v) for k, v in n.items() if v["kind"] == kind]
        if kind == "module":
            continue
        if not rows:
            continue
        L.append("## " + KIND_TITLE[kind])
        L.append("")
        L.append("| English | Hebrew | source | note |")
        L.append("| --- | --- | --- | --- |")
        for k, v in sorted(rows, key=lambda r: r[0].lower()):
            note = v["note"].replace("|", "\\|")
            L.append("| `%s` | `%s` | %s | %s |" % (k, v["he"], v["source"], note))
        L.append("")

    L.append("## Modules")
    L.append("")
    L.append("Hebrew module basenames do not work: an `IMPORT` of one resolves to nothing, silently.")
    L.append("See `NOTES.md` § 4 for the measurement. The Hebrew row therefore keeps Latin filenames with a `-he` suffix.")
    L.append("")
    L.append("| English module | Hebrew module |")
    L.append("| --- | --- |")
    for k, v in g["modules"].items():
        L.append("| `%s.l4` | `%s.l4` |" % (k, v))
    L.append("")
    L.append("## Prose that is translated, not renamed")
    L.append("")
    L.append("`@export` and `@desc` carry sentences, not identifiers, so they are translated whole from the glossary's `prose` map rather than composed out of renamed parts. There are %d of them." % len(g["prose"]))
    L.append("")
    L.append("## Comments")
    L.append("")
    L.append("%d comment blocks quote the statute or the regulations in ENGLISH TRANSLATION in the English row; each is replaced by the Hebrew original from `source/law.wiki` or `source/regulations-fees.wiki`." % len(g["comment_blocks"]))
    L.append("Every other comment stays English on purpose: the rules are for Hebrew readers, the commentary around them is addressed to whoever maintains the encoding.")
    L.append("The one place the Hebrew original could not be used is the **SimpLEX draft** vintage of regulation 2, whose only witness is a screen capture in a published paper; those comments stay in the English translation the English row made, and say so.")
    L.append("")
    with open(os.path.join(HE_DIR, "GLOSSARY.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


# --------------------------------------------------------------------------- main


def main():
    g, names, keep = load_glossary()
    uncovered = set()
    hit_blocks = set()
    stats = {"heralds": 0, "prose": 0, "blocks": 0}
    outputs = {}

    for m in MODULES:
        with open(os.path.join(EN_DIR, m), encoding="utf-8") as fh:
            text = fh.read()
        stem = m[:-3]
        outputs[g["modules"][stem] + ".l4"] = revoice(
            m, text, g, names, keep, uncovered, stats, USED, hit_blocks)

    if uncovered:
        raise Fatal(
            "the glossary does not cover %d identifier(s):\n  %s"
            % (len(uncovered), "\n  ".join(sorted(uncovered)))
        )

    for name, body in outputs.items():
        with open(os.path.join(HE_DIR, name), "w", encoding="utf-8") as fh:
            fh.write(body)

    write_glossary_md(g)

    # Drift warnings. The English row is edited by hand and this row follows it, so a
    # glossary entry nothing uses, or a comment block that no longer matches, means the
    # oracle moved. Neither is fatal -- the output is still correct -- but both are the
    # signal to prune or re-quote.
    stale = sorted(set(names) - USED - set(g["modules"]))
    for s_ in stale:
        sys.stderr.write("warning: glossary entry %r is no longer used by any module\n" % s_)
    for n, b in enumerate(g["comment_blocks"]):
        if n not in hit_blocks:
            sys.stderr.write("warning: comment block %d (%s) no longer matches the English row\n"
                             % (n, b.get("_why", "")[:60]))

    print("wrote %d modules to %s" % (len(outputs), os.path.relpath(HE_DIR, SUBJECT)))
    print("  %d identifiers renamed, %d herald pairs swapped, %d prose strings translated,"
          " %d statute-quoting comment blocks restored to Hebrew"
          % (len(names), stats["heralds"], stats["prose"], stats["blocks"]))
    print("  GLOSSARY.md regenerated from glossary.json")


def unmap():
    """Read the Hebrew row's output on stdin, write it with English names, on stdout.

    This is what makes the two rows COMPARABLE. `check.sh` runs both rows, maps the Hebrew
    one back through the inverse of the same glossary, and diffs the `Result:` blocks: any
    difference at all is then a real disagreement about the law, not a difference of
    vocabulary. The inverse is well defined because `load_glossary` refuses a glossary that
    is not injective.
    """
    g, names, _ = load_glossary()
    inverse = {v: k for k, v in names.items()}
    data = sys.stdin.read()

    def one(m):
        return "`" + inverse.get(m.group(1), m.group(1)) + "`"

    sys.stdout.write(re.sub(r"`([^`]*)`", one, data))


if __name__ == "__main__":
    try:
        if "--unmap" in sys.argv[1:]:
            unmap()
            sys.exit(0)
        main()
    except Fatal as exc:
        sys.stderr.write("revoice.py: %s\n" % exc)
        sys.exit(1)
