#!/usr/bin/env python3
"""Lay out Israeli subjects from the round-4 index agents' verified results.

Input:  tools/topics/round4/*.json     one file per agent group, each keyed "Israel"
Output: one subject directory per distinct Act under subjects/israel/, with subject.json,
        SOURCE-LICENSE.md and registers/source-bundle/<id>.meta.json -- metadata only, no
        statute text. Rewrites subjects/israel/README.md and writes round4/verification.json.

    python tools/topics/scaffold-round4.py --dry-run
    python tools/topics/scaffold-round4.py

Israel differs from the other rounds in three ways this script handles:
  - Hebrew is the authoritative language, so every subject carries display_name_he.
  - Some instruments are Mandate-era Ordinances (פקודה), not Knesset Laws.
  - There is no free official consolidated text: the official version is the original
    publication in Reshumot plus every amending Act. The consolidated Hebrew text on
    Wikisource is a working text and every SOURCE-LICENSE.md says so.
Licence is settled: no copyright subsists in Israeli statutes (Copyright Act, 5768-2007, s 6),
so subjects here are scaffolded "open" rather than waiting on a human decision.
"""
import argparse, datetime, glob, importlib.util, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
R4 = os.path.join(HERE, "round4")
BASE = os.path.join(ROOT, "subjects", "israel")
TODAY = datetime.date.today().isoformat()
_s3 = importlib.util.spec_from_file_location("scaffold3", os.path.join(HERE, "scaffold-round3.py"))
s3 = importlib.util.module_from_spec(_s3); _s3.loader.exec_module(s3)

LIC = """# Source license

The text of **{title}**{he} is Israeli primary legislation.

- **Copyright**: none. Under the Israeli Copyright Act, 5768-2007, s 6, there is no copyright in
  statutes, regulations, Knesset records or judicial decisions.
- **Official version**: {official}. Israel publishes no free official *consolidated* text: the
  official version of a law is its original publication in Reshumot together with every amending Act.
- **Working text**: {url}
  ("{provider}"), a maintained consolidated Hebrew text. **Not an official version.**
- **Attribution**: none required for the statute text. Wikisource's own editorial additions, where
  any survive, are CC BY-SA 4.0.

## Consequence for this subject

Statute text may be deposited and quoted in an encoding. Record which text was used and its date:
a consolidated working text has no official status, so an encoding that relies on it must say so.

## Language

{language}

## Status of this deposit

No statute text has been deposited yet.
"""


def acts_from_results():
    """Merge the groups, keyed by Hebrew title: one Act listed under two topics appears once."""
    merged, register, licence, lang, gaps = {}, None, None, None, []
    for f in sorted(glob.glob(os.path.join(R4, "*.json"))):
        if os.path.basename(f) in ("verification.json",):
            continue
        for _, x in json.load(open(f, encoding="utf-8")).items():
            register = register or x.get("register") or {}
            licence = licence or x.get("licence") or {}
            lang = lang or x.get("language_authenticity")
            gaps += x.get("topic_gaps") or []
            for a in x.get("acts") or []:
                k = a.get("title_he") or a["title"]
                if k in merged:
                    if a["topic"] not in merged[k]["topics"]:
                        merged[k]["topics"].append(a["topic"])
                    continue
                merged[k] = {**a, "topics": [a["topic"]]}
    return merged, register or {}, licence or {}, lang, gaps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    merged, register, licence, lang, gaps = acts_from_results()
    if not merged:
        raise SystemExit("no agent results in %s" % R4)
    taken = set()
    made, skipped, ver = [], [], []
    rows = []
    for he, act in sorted(merged.items(), key=lambda kv: kv[1]["title"]):
        dirname = s3.unique_slug(act["title"], taken)
        d = os.path.join(BASE, dirname)
        ver.append({"jurisdiction": "il", "act": act["title"], "topics": act["topics"],
                    "status": {"yes": "VERIFIED", "not yet in force": "NOT YET IN FORCE"}.get(
                        act.get("in_force"), "UNVERIFIED"),
                    "index_title": act["title"], "nearest": []})
        rows.append((dirname, act))
        if os.path.exists(os.path.join(d, "subject.json")):
            skipped.append(act["title"]); continue
        if a.dry_run:
            made.append((dirname, act["title"])); continue
        os.makedirs(os.path.join(d, "registers", "source-bundle"), exist_ok=True)
        subject = {"id": dirname, "display_name": act["title"], "display_name_he": he,
                   "jurisdiction": "IL", "citation": act.get("identifier") or act["title"],
                   "language": "he",
                   "source": {"provider": register.get("name", "Hebrew Wikisource, the Open Book of Laws"),
                              "source_id": act.get("identifier") or he,
                              "url": act.get("official_url") or act["url"],
                              "working_text_url": act["url"], "retrieved_date": TODAY},
                   "corpus_modules": [], "projections": [], "encoding_version": "0.0.0",
                   "status": "draft"}
        with open(os.path.join(d, "subject.json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(subject, f, indent=2, ensure_ascii=False); f.write("\n")
        meta = {"title": act["title"], "title_he": he, "source_id": act.get("identifier"),
                "landing_url": act["url"], "official_url": act.get("official_url"),
                "indexed_date": TODAY, "text_deposited": False, "in_force": act.get("in_force"),
                "verified_how": act.get("verified_how"), "topics": act["topics"]}
        if act.get("notes"):
            meta["notes"] = act["notes"]
        name = (re.sub(r"[^A-Za-z0-9_.-]+", "-", act.get("identifier") or "").strip("-")[:40]
                .rstrip("-.") or dirname)
        with open(os.path.join(d, "registers", "source-bundle", name + ".meta.json"), "w",
                  encoding="utf-8", newline="\n") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False); f.write("\n")
        official = act.get("official_url") or (
            "the publication in Reshumot cited as %s" % act["identifier"] if act.get("identifier")
            else "the publication in Reshumot (citation not established by the index check)")
        lic = LIC.format(title=act["title"], he=" (%s)" % he if he != act["title"] else "",
                         official=official, url=act["url"],
                         provider=register.get("name", "Hebrew Wikisource, the Open Book of Laws"),
                         language=lang or "Hebrew is authoritative; English translations are unofficial.")
        if act.get("in_force") != "yes":
            lic += "\n## In-force status\n\n%s -- %s\n" % (str(act.get("in_force")).upper(),
                                                          act.get("notes") or "")
        open(os.path.join(d, "SOURCE-LICENSE.md"), "w", encoding="utf-8", newline="\n").write(lic)
        made.append((dirname, act["title"]))

    if not a.dry_run:
        with open(os.path.join(R4, "verification.json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(ver, f, indent=1, ensure_ascii=False)
        existing = sorted(n for n in os.listdir(BASE)
                          if os.path.isdir(os.path.join(BASE, n)) and n not in {d for d, _ in rows})
        out = ["# israel/", "",
               "Israeli legislation, one subject-id per body of law, following the subject-sidecar shape",
               "described in [`subjects/README.md`](../README.md).", "",
               "**Licence: open.** There is no copyright in Israeli statutes, regulations, Knesset records",
               "or court decisions (Copyright Act, 5768-2007, s 6). Hebrew is the authoritative language;",
               "English translations are unofficial. Israel publishes no free official *consolidated* text:",
               "the official version is the original publication in Reshumot plus every amending Act, so the",
               "consolidated Hebrew text each subject points to is a working text, not an official one.", "",
               "| subject | Law | Hebrew title | topics |", "|---|---|---|---|"]
        for dirname, act in sorted(rows, key=lambda r: r[1]["title"]):
            out.append("| [`%s/`](%s/) | %s | %s | %s |"
                       % (dirname, dirname, act["title"], act.get("title_he", ""),
                          "; ".join(act["topics"])))
        for n in existing:
            sj = os.path.join(BASE, n, "subject.json")
            nm = json.load(open(sj, encoding="utf-8")).get("display_name", n) if os.path.exists(sj) else n
            out.append("| [`%s/`](%s/) | %s | | |" % (n, n, nm))
        if gaps:
            out += ["", "## Topics with no statute here", ""]
            seen = set()
            for g in gaps:
                line = "- **%s**: %s" % (g.get("topic"), g.get("reason"))
                if line not in seen:
                    seen.add(line); out.append(line)
        open(os.path.join(BASE, "README.md"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print("%s: %d subjects, %d already there, %d Acts in the index"
          % ("would create" if a.dry_run else "created", len(made), len(skipped), len(merged)))


if __name__ == "__main__":
    main()
