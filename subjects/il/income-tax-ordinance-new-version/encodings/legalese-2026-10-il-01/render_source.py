#!/usr/bin/env python3
"""Render lines of the deposited Wikisource source to plain Hebrew text, mechanically.

Usage:  python3 -I render_source.py LINE [LINE ...]      print each rendered line
        python3 -I render_source.py --check FILE.l4 ...   check every double-quoted Hebrew string in code
                                                          occurs verbatim in the rendered source,
                                                          and every "line N: <Hebrew>" comment
                                                          occurs verbatim in rendered line N
                                                          (" ... " separates elided parts)

Rendering rules (the only transformations applied, so a reviewer can redo them by hand):
  {{ח:פנימי|target|display}} and {{ח:חיצוני|target|display}}  -> display
  {{ח:הערה|text}}                                              -> [הערת עורך: text]
  <sup>a</sup><span ...>⁄</span><sub>b</sub>                   -> a⁄b  (n a⁄b after a digit n)
  {{ח:קטעN|anchor|heading|...}}                                -> heading
  {{ח:סעיף|n|heading|...}}                                     -> סעיף n: heading
  {{ח:ת...}}, {{ח:תת|(x)}} and similar layout templates        -> (x) or nothing
  <wbr> and other bare tags                                    -> removed
"""
import pathlib, re, sys

SRC = (pathlib.Path(__file__).resolve().parent / "../../registers/source-bundle/"
       "income-tax-ordinance-new-version.he.wiki.txt").resolve()

def render(s: str) -> str:
    s = re.sub(r"(\d)?<sup>(\d+)</sup><span[^>]*>⁄</span><sub>(\d+)</sub>",
               lambda m: (m.group(1) + " " if m.group(1) else "") + m.group(2) + "⁄" + m.group(3), s)
    s = s.replace("<wbr>", "")
    for _ in range(5):  # innermost templates first, repeatedly
        s = re.sub(r"\{\{ח:(?:פנימי|חיצוני)\|[^{}|]*\|([^{}]*)\}\}", r"\1", s)
        s = re.sub(r"\{\{ח:הערה\|([^{}]*)\}\}", r"[הערת עורך: \1]", s)
        s = re.sub(r"\{\{ח:סעיף\|([^{}|]*)\|([^{}|]*)(?:\|[^{}]*)?\}\}", r"סעיף \1: \2", s)
        s = re.sub(r"\{\{ח:ת+\|(?:סוג=הגדרה)\}\}", "", s)
        s = re.sub(r"\{\{ח:ת+\|(\([^{}|]*\))(?:\|(\([^{}|]*\)))?\}\}",
                   lambda m: m.group(1) + (m.group(2) or ""), s)
        s = re.sub(r"\{\{ח:ת+\}\}", "", s)
        s = re.sub(r"\{\{ח:סעיף\*\}\}", "", s)
        s = re.sub(r"\{\{ח:קטע\d\|[^{}|]*\|([^{}|]*)(?:\|[^{}]*)?\}\}", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()

def lines():
    return SRC.read_text(encoding="utf-8").split("\n")

def main(argv):
    src = lines()
    if argv and argv[0] == "--check":
        corpus = "\n".join(render(l) for l in src)
        bad = 0
        for f in argv[1:]:
            text = pathlib.Path(f).read_text(encoding="utf-8")
            # Double-quoted strings in code only: comments may quote other documents.
            code = "\n".join(l.split("--", 1)[0] for l in text.split("\n"))
            for m in re.finditer(r'"([^"\n]*[֐-׿][^"\n]*)"', code):
                q = m.group(1)
                ok = q in corpus
                bad += not ok
                print(("ok      " if ok else "MISSING ") + f"{pathlib.Path(f).name}: {q[:70]}")
            # A comment of the form "line N: <quotation>" is pinned to line N itself.
            for m in re.finditer(r"line (\d+): (.*[\u0590-\u05FF].*)$", text, re.M):
                n, q = int(m.group(1)), m.group(2).strip()
                q = re.sub(r"\s*\.\.\.\s*$", "", q)
                for part in [x.strip() for x in q.split(" ... ") if x.strip()]:
                    ok = part in render(src[n - 1])
                    bad += not ok
                    print(("ok      " if ok else "MISSING ") + f"{pathlib.Path(f).name}: line {n}: {part[:60]}")
        print(f"{bad} Hebrew quotation(s) not found verbatim in the rendered source")
        return 1 if bad else 0
    for a in argv:
        n = int(a)
        print(f"{n}: {render(src[n - 1])}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
