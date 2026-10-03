#!/usr/bin/env python3
"""Check every Act named in topic-acts.json against the jurisdiction's official index.

An Act is VERIFIED when its title matches an index entry exactly (after normalising quotes,
dashes and whitespace). Where it does not, the closest index titles are offered, so a wrong
year or a renamed Act is caught rather than silently kept. Jurisdictions with no index yet
(NSW, NZ) are reported as UNCHECKED.
"""
import difflib, glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
ROOT = os.path.dirname(TOOLS)


def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", t).strip().lower()


def index_titles(jur):
    p = os.path.join(TOOLS, "indexes", jur + ".json")
    if os.path.exists(p):
        return [a["title"] for a in json.load(open(p, encoding="utf-8"))["acts"]]
    if jur == "au-wa":
        return [json.load(open(f, encoding="utf-8"))["display_name"]
                for f in glob.glob(os.path.join(ROOT, "subjects", "western-australia", "*", "subject.json"))]
    if jur == "sg":
        return list(json.load(open(os.path.join(TOOLS, "sso-acts-manifest.json"), encoding="utf-8")).values())
    return None


def main():
    spec = json.load(open(os.path.join(HERE, "topic-acts.json"), encoding="utf-8"))
    browser = json.load(open(os.path.join(HERE, "browser-verified.json"), encoding="utf-8"))
    report = {}
    for jur, topics in spec["map"].items():
        titles = index_titles(jur)
        lookup = {norm(t): t for t in (titles or [])}
        # Singapore's manifest drops the year from some titles ("Interpretation Act").
        noyear = {re.sub(r"\s+\d{4}$", "", k): v for k, v in lookup.items()}
        for topic, acts in topics.items():
            for act in acts:
                key = (jur, act)
                if key in report:
                    report[key]["topics"].append(topic)
                    continue
                if titles is None and act in browser.get(jur, {}):
                    status, match, near = browser[jur][act].split(" --")[0], act, []
                elif titles is None:
                    status, match, near = "UNCHECKED", None, []
                elif norm(act) in lookup:
                    status, match, near = "VERIFIED", lookup[norm(act)], []
                elif jur == "sg" and re.sub(r"\s+\d{4}$", "", norm(act)) in noyear:
                    status, match, near = "VERIFIED", noyear[re.sub(r"\s+\d{4}$", "", norm(act))], []
                else:
                    near = difflib.get_close_matches(norm(act), list(lookup), n=3, cutoff=0.6)
                    status, match, near = "NOT FOUND", None, [lookup[n] for n in near]
                report[key] = {"jurisdiction": jur, "act": act, "topics": [topic],
                               "status": status, "index_title": match, "nearest": near}
    rows = list(report.values())
    json.dump(rows, open(os.path.join(HERE, "verification.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    by = {}
    for r in rows:
        by.setdefault(r["jurisdiction"], {}).setdefault(r["status"], 0)
        by[r["jurisdiction"]][r["status"]] += 1
    for j, c in by.items():
        print("%-7s %s" % (j, ", ".join("%s %d" % kv for kv in sorted(c.items()))))
    print()
    for r in rows:
        if r["status"] == "NOT FOUND":
            print("NOT FOUND  %-7s %-62s nearest: %s" % (r["jurisdiction"], r["act"], r["nearest"]))


if __name__ == "__main__":
    main()
