"""
Pass 2: cross-Act aggregation and cheap deterministic candidate flagging.
No LLM. Reads definitions.json (from extract_definitions.py) plus the raw
source text (for orphan-usage checks), writes candidate lists for review.
"""
import os, re, json, glob
from collections import defaultdict

ANALYSIS_DIR = r"C:\Users\micha\canon\analysis"
CANON_ROOT = r"C:\Users\micha\canon\subjects\western-australia"

with open(os.path.join(ANALYSIS_DIR, "definitions.json"), encoding="utf-8") as f:
    all_defs = json.load(f)


def normalize_definition(defn, term):
    d = defn.lower()
    d = re.sub(r"^\t?" + re.escape(term.lower()) + r"\s*", "", d)
    d = re.sub(r"\b(means|has the meaning given(?: to it)?(?: in| by)|"
               r"has a meaning affected by|includes|does not include)\b", "", d, count=1)
    d = re.sub(r"section\s*\d+[a-z]*(\(\d+\))*", "<SECREF>", d)
    d = re.sub(r"\s+", " ", d).strip().strip(";,. ")
    return d


# ---------- Check A: same term, different meaning across Acts ----------
term_to_acts = defaultdict(list)  # term -> [(act, normalized_def, raw_def, verb)]
for act, defs in all_defs.items():
    for entry in defs:
        term = entry["term"]
        norm = normalize_definition(entry["definition"], term)
        term_to_acts[term].append((act, norm, entry["definition"], entry["verb"]))

different_meaning_candidates = []
for term, occurrences in term_to_acts.items():
    if len(occurrences) < 2:
        continue
    clusters = defaultdict(list)
    for act, norm, raw, verb in occurrences:
        clusters[norm].append((act, raw))
    if len(clusters) > 1:
        different_meaning_candidates.append({
            "term": term,
            "num_acts": len(occurrences),
            "num_distinct_definitions": len(clusters),
            "clusters": [
                {"definition_sample": raws[0][1], "acts": [a for a, _ in raws]}
                for raws in clusters.values()
            ],
        })

different_meaning_candidates.sort(key=lambda c: -c["num_acts"])

# ---------- Check B: orphaned definitions (unused within their own Act) ----------
orphan_candidates = []
for act, defs in all_defs.items():
    bundle = os.path.join(CANON_ROOT, act, "registers", "source-bundle")
    txts = glob.glob(os.path.join(bundle, "*.txt"))
    if not txts:
        continue
    with open(txts[0], encoding="utf-8", errors="replace") as f:
        text = f.read()
    text_lower = text.lower()

    for entry in defs:
        term = entry["term"]
        if len(term) < 3:
            continue
        # count occurrences of the term as a whole phrase, case-insensitive
        pattern = re.compile(r"\b" + re.escape(term) + r"\b")
        occurrences = pattern.findall(text_lower)
        # every definition site itself produces >=1 occurrence (the anchor); if total
        # occurrences are very low (<=2), the term is essentially unused elsewhere.
        if len(occurrences) <= 2:
            orphan_candidates.append({
                "act": act, "term": term, "occurrences_in_text": len(occurrences),
                "definition_sample": entry["definition"][:200],
            })

orphan_candidates.sort(key=lambda c: c["occurrences_in_text"])

# ---------- write outputs ----------
with open(os.path.join(ANALYSIS_DIR, "candidates_different_meaning.json"), "w", encoding="utf-8") as f:
    json.dump(different_meaning_candidates, f, indent=1)
with open(os.path.join(ANALYSIS_DIR, "candidates_orphaned.json"), "w", encoding="utf-8") as f:
    json.dump(orphan_candidates, f, indent=1)

print("terms defined in >1 Act:", sum(1 for o in term_to_acts.values() if len(o) > 1))
print("candidates: different meaning across Acts:", len(different_meaning_candidates))
print("candidates: orphaned/unused-in-own-Act definitions:", len(orphan_candidates))
