#!/usr/bin/env python3
"""Check every quoted passage in the .l4 modules against the retrieved sources.

The encoding of a judge-made doctrine rests on long verbatim quotations in its
comments -- that is what lets a reviewer check a rule against the judgment it
claims to encode.  A quotation that has drifted is worse than a paraphrase,
because it invites no checking.  So this script string-matches every quotation
back to the source text it came from.

Run from this directory:

    python3 verify-quotations.py

Exit 0 when every quotation matches, 1 otherwise.

TWO NORMALISATIONS ARE APPLIED TO BOTH SIDES, and each exists because of a real
artifact rather than to make the check pass:

  * SPACE BEFORE PUNCTUATION.  The source texts were extracted from eLitigation
    HTML by stripping tags, and an italicised span leaves a stray space behind:
    the judgment's "per se, on the other hand" arrives as "per se , on the
    other hand", and "amicus curiae's" as "amicus curiae 's".  The artifact is
    in the extraction, not in the report, so both sides are normalised and the
    quotation in the module is the correct rendering.

  * THE SECTION SIGN.  Donovan prints "§ 154"; an L4 comment is plain source
    text and writes "s 154".

Elisions ("...") and bracketed alterations ("[t]he", "[¶]") split a quotation
into fragments; every fragment of 40 characters or more must appear verbatim.
Fragments shorter than that are not checked, because a short phrase matches by
coincidence and a check that cannot fail is not a check.

Quotation marks are paired by ALTERNATION -- split the block on the quote
character, take the odd parts -- rather than by a regex scan.  A regex that
also enforces a minimum length gets this wrong: it skips a short quotation for
failing the length test and then pairs that quotation's closing mark with the
next one's opening mark, yielding a "quotation" made of this corpus's own prose
between two real ones.  Twelve such phantoms appeared on the first run of this
check and every one of them was the tool's fault, not the corpus's.
"""
import re, sys, glob, os

SOURCES = {
    "Chwee Kin Keong [2005] SGCA 2": "../../../source/2005_SGCA_2.text.txt",
    "Quoine [2020] SGCA(I) 02":      "../../../source/2020_SGCAI_2.text.txt",
    "Donovan v RRL Corp":            "../../../source/donovan-2001.justia-wayback.text.txt",
}

def norm(s):
    s = (s.replace("’", "'").replace("‘", "'")
          .replace("“", '"').replace("”", '"')
          .replace("—", "--").replace("–", "-")
          .replace(" ", " ").replace("§", "s"))
    s = s.replace("[\u00b6]", " ")          # Donovan's own editorial paragraph markers
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,.;:)\]'])", r"\1", s)
    s = re.sub(r"([(\[])\s+", r"\1", s)
    return s.strip()

def key(s):
    """The comparison key: lowercase letters and digits, nothing else.

    Typography is not part of a quotation.  A nested passage switches from " to
    ' and the reports and this corpus do not always agree which; the tag-stripped
    source leaves stray spaces inside italicised spans ("per se , on the other
    hand", "amicus curiae 's"); Donovan prints a section sign where a comment
    prints an "s".  None of that is a difference in what the court SAID, and
    every one of them produced a false alarm on an earlier run of this check.

    What survives the key is the sequence of words and their order, which is the
    thing a quotation actually asserts.  Over a fragment of 40 characters or more
    a coincidental match is not a practical concern."""
    return re.sub(r"[^a-z0-9]", "", s.lower())

def comment_blocks(path):
    blocks, cur = [], []
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.strip().startswith("--"):
            cur.append(re.sub(r"^\s*--\s?", "", line))
        elif cur:
            blocks.append(" ".join(cur)); cur = []
    if cur:
        blocks.append(" ".join(cur))
    return blocks

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    srcs = {}
    for name, rel in SOURCES.items():
        if not os.path.exists(rel):
            print(f"MISSING SOURCE: {rel}"); return 2
        srcs[name] = norm(open(rel, encoding="utf-8", errors="replace").read())

    checked = failures = 0
    for f in sorted(glob.glob("../*.l4")):
        for block in comment_blocks(f):
            # Alternating pairing: split on the quote character and take the odd
            # parts.  A regex scan gets this wrong when a short quotation sits
            # between two long ones -- it skips the short one for failing the
            # length test and then pairs its CLOSING quote with the next
            # OPENING one, producing a span made of this corpus's own prose.
            parts = norm(block).split('"')
            for q in parts[1::2]:
                if len(q) < 40:
                    continue
                frags = [norm(x).strip(" ,.;:")
                         for x in re.split(r"\s*\.\.\.\s*|\[[^\]]*\]", q)]
                frags = [x for x in frags if len(x) >= 40]
                if not frags:
                    continue
                checked += 1
                missing = [fr for fr in frags
                           if not any(key(fr) in key(s)
                                      for s in srcs.values())]
                if missing:
                    failures += 1
                    print(f"\nUNMATCHED in {os.path.basename(f)}:")
                    print(f"  {q[:120]}")
                    for fr in missing:
                        print(f"  fragment ({len(fr)}c): {fr[:160]}")
    print(f"\nquotations scanned: {checked}   unmatched: {failures}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
