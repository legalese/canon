#!/usr/bin/env python3
"""Lay out subjects for the round-3 jurisdictions (the remaining US states and DC, and the
remaining Canadian provinces and territories) from the index agents' verified results.

Input:  tools/topics/round3/*.json          one file per agent group, keyed by jurisdiction name
        tools/topics/round3/licence-decisions.json   human licence categories (see below)
Output: one subject directory per distinct Act, with subject.json, SOURCE-LICENSE.md and
        registers/source-bundle/<id>.meta.json -- metadata only, no statute text. Also writes
        round3/verification.json for the progress tracker. Existing directories are never modified.

    python tools/topics/scaffold-round3.py --dry-run
    python tools/topics/scaffold-round3.py

Licence categories come from a human, not from the agents. Until a jurisdiction is listed in
licence-decisions.json it is scaffolded as "unclear" and marked metadata-only. The agents' own
open_licence flag and quote are carried into each SOURCE-LICENSE.md as evidence for that decision.
"""
import argparse, datetime, glob, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
ROOT = os.path.dirname(TOOLS)
R3 = os.path.join(HERE, "round3")
TODAY = datetime.date.today().isoformat()
spec = importlib.util.spec_from_file_location("sso", os.path.join(TOOLS, "fetch-sso-corpus.py"))
sso = importlib.util.module_from_spec(spec); spec.loader.exec_module(sso)

US = {"Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "Colorado": "CO",
      "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI",
      "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
      "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA",
      "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
      "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
      "New Mexico": "NM", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
      "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI",
      "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Utah": "UT",
      "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
      "Wisconsin": "WI", "Wyoming": "WY", "District of Columbia": "DC"}
CA = {"Alberta": "AB", "Saskatchewan": "SK", "Manitoba": "MB", "Quebec": "QC",
      "New Brunswick": "NB", "Nova Scotia": "NS", "Prince Edward Island": "PE",
      "Newfoundland and Labrador": "NL", "Yukon": "YT", "Northwest Territories": "NT",
      "Nunavut": "NU"}


def ident(jname):
    """"Alabama (US state)" -> (key, directory, jurisdiction code). Raises on an unknown name."""
    bare = re.sub(r"\s*\((US state|US|Canada)\)$", "", jname).strip()
    if bare in US:
        return "us-" + US[bare].lower(), slug(bare), "US-" + US[bare]
    if bare in CA:
        return "ca-" + CA[bare].lower(), slug(bare), "CA-" + CA[bare]
    raise SystemExit("unknown jurisdiction %r -- fix the agent output or this table" % jname)


def slug(title, limit=64):
    """sso.slug, capped at a word boundary so paths stay inside Windows' 260-character limit."""
    s = sso.slug(title)
    if len(s) <= limit:
        return s
    cut = s[:limit].rsplit("-", 1)[0]
    return cut or s[:limit]


def unique_slug(title, taken, limit=64):
    """A directory name for this Act that no other Act in the same jurisdiction has.

    US code divisions share long leading text -- "Official Code of Georgia Annotated, Title 34
    (Labor and Industrial Relations), Chapter 1 ..." and "... Chapter 4 ..." cap to the same
    64 characters -- so where the capped name is taken, keep the head and graft on the tail that
    actually distinguishes the two (the part after the last dash, comma or colon)."""
    s = slug(title, limit)
    if s not in taken:
        taken.add(s); return s
    tail = re.split(r"\s*[—–,:-]\s*", title.strip())[-1]
    tail = sso.slug(tail)
    if tail:
        head = slug(title, max(16, limit - len(tail) - 1)).rstrip("-")
        cand = (head + "-" + tail)[:limit].rstrip("-")
        if cand and cand not in taken:
            taken.add(cand); return cand
    for n in range(2, 99):
        cand = (slug(title, limit - len(str(n)) - 1).rstrip("-") + "-" + str(n))
        if cand not in taken:
            taken.add(cand); return cand
    raise SystemExit("cannot find a unique directory name for %r" % title)


CONSEQUENCE = {
    "open": "Statute text may be deposited and quoted in an encoding, subject to the attribution "
            "above.",
    "conditional": "Reproduction is permitted on the conditions above, but the terms do not "
                   "expressly grant a right to ADAPT. An L4 encoding that quotes the statute is "
                   "arguably an adaptation. **Confirm before depositing text or quoting it in an "
                   "encoding** -- a human decision recorded here.",
    "not-open": "**Do not deposit statute text here, or quote it in an encoding, without written "
                "permission.** This directory holds metadata only until permission is obtained.",
    "unclear": "**Metadata only until resolved.** No human has recorded a licence decision for "
               "this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's "
               "own terms, quoted above, are the evidence to decide on.",
}
US_DOCTRINE = ("In the United States the text of a statute is not copyrightable: it is an edict of "
               "government (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). A register's "
               "copyright notice can still cover a publisher's annotations, headnotes and "
               "numbering, which this corpus does not reproduce.")

LIC = """# Source license

The text of **{title}** is published on the [{register}]({register_url}).

- **Terms**: {summary}
- **Terms checked**: {today}, at {terms_url}
- **From the terms**: "{quote}"
- **Reuse and adaptation permitted, per the index check**: {open_licence}
- **Attribution required**: {attribution}
- **Source**: {url}
{note}
## Consequence for this subject

{consequence}

## Language

{language}

## Status of this deposit

No statute text has been deposited yet.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verification-only", action="store_true",
                    help="write round3/verification.json for the progress tracker, create nothing else")
    a = ap.parse_args()
    dec_p = os.path.join(R3, "licence-decisions.json")
    decisions = json.load(open(dec_p, encoding="utf-8")) if os.path.exists(dec_p) else {}
    res = {}
    for f in sorted(glob.glob(os.path.join(R3, "*.json"))):
        if os.path.basename(f) in ("licence-decisions.json", "licence-decisions.template.json",
                                  "verification.json"):
            continue
        for k, v in json.load(open(f, encoding="utf-8")).items():
            res[k] = v
    made, skipped, ver, no_acts = [], [], [], []
    for jname, x in sorted(res.items()):
        key, dname, code = ident(jname)
        base = os.path.join(ROOT, "subjects", dname)
        if not x.get("acts"):
            no_acts.append(jname)
        dec = decisions.get(key, {})
        cat = dec.get("category", "unclear")
        acts = {}
        for act in x["acts"]:
            acts.setdefault(act["title"], {**act, "topics": []})["topics"].append(act["topic"])
        taken = set()          # names used by THIS run; a pre-existing directory is skipped below,
                               # which keeps re-runs idempotent
        for title, act in acts.items():
            status = {"yes": "VERIFIED", "not yet in force": "NOT YET IN FORCE"}.get(act["in_force"], "UNVERIFIED")
            ver.append({"jurisdiction": key, "act": title, "topics": act["topics"], "status": status,
                        "index_title": title, "nearest": []})
            dirname = unique_slug(title, taken)
            d = os.path.join(base, dirname)
            if os.path.exists(os.path.join(d, "subject.json")):
                skipped.append((key, title)); continue
            if a.dry_run or a.verification_only:
                made.append((key, title)); continue
            os.makedirs(os.path.join(d, "registers", "source-bundle"), exist_ok=True)
            subject = {"id": dirname, "display_name": title, "jurisdiction": code,
                       "citation": act.get("identifier") or title,
                       "source": {"provider": x["register"]["name"], "source_id": act["identifier"],
                                  "url": act["url"], "retrieved_date": TODAY},
                       "corpus_modules": [], "projections": [], "encoding_version": "0.0.0",
                       "status": "draft"}
            with open(os.path.join(d, "subject.json"), "w", encoding="utf-8", newline="\n") as f:
                json.dump(subject, f, indent=2, ensure_ascii=False); f.write("\n")
            meta = {"title": title, "source_id": act["identifier"], "landing_url": act["url"],
                    "indexed_date": TODAY, "text_deposited": False, "in_force": act["in_force"],
                    "verified_how": act["verified_how"], "topics": act["topics"]}
            if act.get("notes"):
                meta["notes"] = act["notes"]
            name = re.sub(r"[^A-Za-z0-9_.-]+", "-", act["identifier"]).strip("-")[:40].rstrip("-.") or dirname
            with open(os.path.join(d, "registers", "source-bundle", name + ".meta.json"), "w",
                      encoding="utf-8", newline="\n") as f:
                json.dump(meta, f, indent=2, ensure_ascii=False); f.write("\n")
            L = x["licence"]
            note = ""
            if key.startswith("us-"):
                note = "\n" + US_DOCTRINE + "\n"
            if dec.get("note"):
                note += "\n" + dec["note"] + "\n"
            lic = LIC.format(title=title, register=x["register"]["name"], register_url=x["register"]["url"],
                             summary=L["summary"], today=TODAY, terms_url=L.get("terms_url") or "(none found)",
                             quote=(L.get("quote") or "(the register states no terms)").replace('"', "'"),
                             open_licence="yes" if L.get("open_licence") else "no, or not established",
                             attribution=L.get("attribution") or "none stated", url=act["url"],
                             note=note, consequence=CONSEQUENCE[cat],
                             language=x.get("language_authenticity") or "English.")
            if act["in_force"] != "yes":
                lic += "\n## In-force status\n\n%s -- %s\n" % (act["in_force"].upper(), act.get("notes") or "")
            open(os.path.join(d, "SOURCE-LICENSE.md"), "w", encoding="utf-8", newline="\n").write(lic)
            made.append((key, title))
        if not (a.dry_run or a.verification_only):
            readme = os.path.join(base, "README.md")
            if not os.path.exists(readme) and acts:
                gaps = "\n".join("- **%s**: %s" % (g["topic"], g["reason"]) for g in x.get("topic_gaps", []))
                open(readme, "w", encoding="utf-8", newline="\n").write(
                    "# %s/\n\n%s legislation, one subject-id per body of law, following the "
                    "subject-sidecar shape described in [`subjects/README.md`](../README.md).\n\n"
                    "The subjects here were laid out on %s for the legislation governing twelve "
                    "everyday topics. Each was checked against the %s; the check is recorded in each "
                    "subject's `registers/source-bundle/*.meta.json`. No statute text has been "
                    "deposited and nothing is encoded yet.\n\n**Licence category: %s.** %s\n\n"
                    "## Register access\n\n%s\n\n## Topics with no legislation here\n\n%s\n"
                    % (dname, jname, TODAY, x["register"]["name"], cat, CONSEQUENCE[cat],
                       x["register"].get("access_notes", ""), gaps or "none"))
    if not a.dry_run:
        with open(os.path.join(R3, "verification.json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(ver, f, indent=1, ensure_ascii=False)
    verb = "would create" if a.dry_run else ("counted" if a.verification_only else "created")
    print("%s: %d subjects, %d skipped (already there), across %d jurisdictions%s"
          % (verb, len(made), len(skipped), len(res),
             "; wrote round3/verification.json only" if a.verification_only else ""))
    undecided = sorted({ident(j)[0] for j in res} - set(decisions))
    if undecided:
        print("no licence decision yet (scaffolded as 'unclear'): %s" % ", ".join(undecided))
    if no_acts:
        print("no Acts returned (register blocked or unverifiable): %s" % ", ".join(no_acts))


if __name__ == "__main__":
    main()
