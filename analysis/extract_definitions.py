"""
Extraction layer, pass 1: pull (term, definition, section-context) tuples out of
every WA Act's "Terms used" / interpretation section, plus the PCO's own
"Defined terms" index and any "of no further effect" / spent notes.

Deterministic, no LLM. Output: analysis/definitions.json, analysis/spent_notes.json
"""
import os, re, json, glob

CANON_ROOT = r"C:\Users\micha\canon\subjects\western-australia"
OUT_DEFS = r"C:\Users\micha\canon\analysis\definitions.json"
OUT_SPENT = r"C:\Users\micha\canon\analysis\spent_notes.json"
OUT_STATS = r"C:\Users\micha\canon\analysis\extraction_stats.json"

# anchor: a tab-indented term followed by a defining verb phrase
ANCHOR_RE = re.compile(
    r"\n\t([A-Za-z][A-Za-z0-9 /\-'()\u2019]{1,80}?)\s+"
    r"(means|has the meaning given(?: to it)?(?: in| by)|has a meaning affected by|"
    r"includes(?! but)|does not include)\b"
)

# a top-level numbered section heading in the BODY (e.g. "\n4.\tPosition of Crown")
# used to find where the interpretation section ends
SECTION_HEADING_RE = re.compile(r"\n(\d+[A-Z]{0,2})\.\t([A-Z][^\n\t]{2,80})\n")

SPENT_RE = re.compile(
    r"([^\n.]{0,200}?(?:is|are)\s+(?:a\s+)?(?:transitional provisions?|"
    r"provisions?)[^\n.]{0,120}?of no further effect[^\n.]{0,50}\.)",
    re.IGNORECASE,
)


def find_terms_used_body(text):
    """Return (start, end) char offsets of the BODY interpretation section, or None."""
    occurrences = [m.start() for m in re.finditer(r"Terms used", text)]
    if not occurrences:
        # some Acts title it "Definitions" or "Interpretation" instead
        occurrences = [m.start() for m in re.finditer(r"\b(Definitions|Interpretation)\b", text)]
        if not occurrences:
            return None
    # last occurrence = body (ToC entries always precede the body section)
    start = occurrences[-1]
    # end = the next top-level section heading after start + a bit of slack
    m = SECTION_HEADING_RE.search(text, start + 20)
    end = m.start() if m else min(start + 40000, len(text))
    return start, end


def extract_definitions_from_act(text):
    span = find_terms_used_body(text)
    if not span:
        return []
    start, end = span
    section_text = text[start:end]

    anchors = list(ANCHOR_RE.finditer(section_text))
    results = []
    for i, m in enumerate(anchors):
        term = m.group(1).strip().strip(",;")
        verb = m.group(2)
        def_start = m.start()
        def_end = anchors[i + 1].start() if i + 1 < len(anchors) else len(section_text)
        definition = section_text[def_start:def_end].strip()
        # drop overly short/garbage terms (parsing noise)
        if len(term) < 2 or len(term) > 80:
            continue
        results.append({"term": term.lower(), "term_raw": term, "verb": verb, "definition": definition})
    return results


def extract_defined_terms_index(text):
    """Parse the PCO's own 'Defined terms' index at the tail: term \t provisions."""
    idx = text.find("Defined term")
    if idx == -1:
        return {}
    tail = text[idx:idx + 60000]
    lines = tail.split("\n")
    out = {}
    for line in lines[2:]:  # skip header row(s)
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0].strip() and parts[1].strip():
            term = parts[0].strip()
            provisions = parts[1].strip()
            if len(term) < 80:
                out[term.lower()] = provisions
    return out


def extract_spent_notes(text):
    return [m.group(1).strip() for m in SPENT_RE.finditer(text)]


PROCESSED_PATH = r"C:\Users\micha\canon\analysis\_processed.json"


def load_if_exists(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def main():
    all_defs = load_if_exists(OUT_DEFS, {})
    all_index = load_if_exists(r"C:\Users\micha\canon\analysis\defined_terms_index.json", {})
    all_spent = load_if_exists(OUT_SPENT, {})
    processed = set(load_if_exists(PROCESSED_PATH, []))
    if processed:
        print(f"resuming: {len(processed)} acts already processed", flush=True)

    def compute_stats():
        return {
            "total_acts": len(processed),
            "acts_with_terms_used": len(all_defs),
            "acts_with_index": len(all_index),
            "acts_with_spent_notes": len(all_spent),
            "total_definitions": sum(len(v) for v in all_defs.values()),
        }

    def checkpoint():
        with open(OUT_DEFS, "w", encoding="utf-8") as f:
            json.dump(all_defs, f, indent=1)
        with open(r"C:\Users\micha\canon\analysis\defined_terms_index.json", "w", encoding="utf-8") as f:
            json.dump(all_index, f, indent=1)
        with open(OUT_SPENT, "w", encoding="utf-8") as f:
            json.dump(all_spent, f, indent=1)
        with open(OUT_STATS, "w", encoding="utf-8") as f:
            json.dump(compute_stats(), f, indent=1)
        with open(PROCESSED_PATH, "w", encoding="utf-8") as f:
            json.dump(sorted(processed), f)

    dirs = sorted(d for d in os.listdir(CANON_ROOT) if os.path.isdir(os.path.join(CANON_ROOT, d)))
    for i, d in enumerate(dirs, 1):
        if d in processed:
            continue
        subject_dir = os.path.join(CANON_ROOT, d)
        bundle = os.path.join(subject_dir, "registers", "source-bundle")
        txts = glob.glob(os.path.join(bundle, "*.txt")) if os.path.isdir(bundle) else []
        if not txts:
            processed.add(d)
            continue
        processed.add(d)
        with open(txts[0], encoding="utf-8", errors="replace") as f:
            text = f.read()

        defs = extract_definitions_from_act(text)
        if defs:
            all_defs[d] = defs

        index = extract_defined_terms_index(text)
        if index:
            all_index[d] = index

        spent = extract_spent_notes(text)
        if spent:
            all_spent[d] = spent

        if i % 50 == 0:
            print(f"[{i}/{len(dirs)}] checkpointing... {compute_stats()}", flush=True)
            checkpoint()

    stats = compute_stats()
    with open(OUT_DEFS, "w", encoding="utf-8") as f:
        json.dump(all_defs, f, indent=1)
    with open(r"C:\Users\micha\canon\analysis\defined_terms_index.json", "w", encoding="utf-8") as f:
        json.dump(all_index, f, indent=1)
    with open(OUT_SPENT, "w", encoding="utf-8") as f:
        json.dump(all_spent, f, indent=1)
    with open(OUT_STATS, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=1)

    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
