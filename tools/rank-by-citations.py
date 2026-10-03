#!/usr/bin/env python3
"""Rank a jurisdiction's Acts by how many other in-force Acts of the same jurisdiction cite them.

Measure: for each Act, the number of DISTINCT other Acts whose text contains its exact short
title ("Residential Tenancies Act 1987"). Self-citation is excluded. It measures legal
centrality -- how much of the statute book depends on an Act -- rather than public interest.

Known limits, stated because they move the ranking:
  - Exact short-title matching misses Acts cited by a popular name. WA's Criminal Code is
    enacted as the "Criminal Code Act Compilation Act 1913" but cited as "The Criminal Code".
    Such aliases are listed in ALIASES and counted under the Act they name.
  - Framework Acts (Interpretation Acts, the Constitution) are cited by nearly everything, so
    they rank first by construction. They are real dependencies, and are kept.
  - It needs the text of every Act. It runs only where the source bundle has been harvested.

Usage:
    python tools/rank-by-citations.py au-wa --top 40
"""
import argparse, collections, glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDERS = {"au-wa": "western-australia", "sg": "singapore"}
ALIASES = {
    "au-wa": {"The Criminal Code": "Criminal Code Act Compilation Act 1913"},
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jurisdiction")
    ap.add_argument("--top", type=int, default=40)
    a = ap.parse_args()
    jur = a.jurisdiction
    subjects = []
    for sj in glob.glob(os.path.join(ROOT, "subjects", FOLDERS[jur], "*", "subject.json")):
        s = json.load(open(sj, encoding="utf-8"))
        texts = glob.glob(os.path.join(os.path.dirname(sj), "registers", "source-bundle", "*.txt"))
        if texts:
            subjects.append((s["id"], (s.get("display_name") or s["citation"]).strip(), texts[0]))
    by_suffix = collections.defaultdict(list)       # "Act 1987" -> titles ending that way
    for sid, title, _ in subjects:
        m = re.search(r"(Act,?\s+\d{4})$", title)
        if m:
            by_suffix[re.sub(r"[,\s]+", " ", m.group(1))].append((sid, title))
    aliases = ALIASES.get(jur, {})
    title_to_id = {t: sid for sid, t, _ in subjects}
    cited_by = collections.defaultdict(set)
    for sid, title, path in subjects:
        text = re.sub(r"\s+", " ", open(path, encoding="utf-8", errors="replace").read())
        for m in re.finditer(r"Act,? (\d{4})", text):
            suffix = "Act " + m.group(1)
            window = text[max(0, m.start() - 200):m.end()]
            for cid, ctitle in by_suffix.get(suffix, ()):
                if cid != sid and window.endswith(ctitle[-len(window):] if len(ctitle) > len(window) else ctitle):
                    cited_by[cid].add(sid)
        for alias, target in aliases.items():
            tid = title_to_id.get(target)
            if tid and tid != sid and alias in text:
                cited_by[tid].add(sid)
    rows = sorted(({"id": sid, "title": t, "cited_by": len(cited_by.get(sid, ()))}
                   for sid, t, _ in subjects), key=lambda r: (-r["cited_by"], r["title"]))
    os.makedirs(os.path.join(HERE, "rankings"), exist_ok=True)
    json.dump({"jurisdiction": jur, "measure": "distinct in-force Acts citing by exact short title",
               "acts_with_text": len(subjects), "ranking": rows},
              open(os.path.join(HERE, "rankings", jur + "-citations.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("%s: %d Acts with text" % (jur, len(subjects)))
    for i, r in enumerate(rows[:a.top], 1):
        print("%3d %5d  %s" % (i, r["cited_by"], r["title"]))


if __name__ == "__main__":
    main()
