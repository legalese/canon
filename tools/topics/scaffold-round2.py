#!/usr/bin/env python3
"""Lay out subjects for the round-2 jurisdictions from the index agents' verified results.

Input: tools/topics/round2/agent-results.json (one record per jurisdiction, produced by the
index-topic-acts workflow and spot-checked by hand). Output: one subject directory per distinct
Act (or, for the three US states, per code division/article), with subject.json,
SOURCE-LICENSE.md and registers/source-bundle/<id>.meta.json -- metadata only, no statute
text. Also writes round2/verification.json for the progress tracker. Existing directories are
never modified.
"""
import datetime, importlib.util, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
ROOT = os.path.dirname(TOOLS)
TODAY = datetime.date.today().isoformat()
spec = importlib.util.spec_from_file_location("sso", os.path.join(TOOLS, "fetch-sso-corpus.py"))
sso = importlib.util.module_from_spec(spec); spec.loader.exec_module(sso)


def slug(title, limit=64):
    """sso.slug, capped at a word boundary so paths stay inside Windows' 260-character limit."""
    s = sso.slug(title)
    if len(s) <= limit:
        return s
    cut = s[:limit].rsplit("-", 1)[0]
    return cut or s[:limit]

# agent jurisdiction string -> (key, directory, code, licence category)
J = {
    "United States (federal)":       ("us-federal", "united-states", "US", "open"),
    "California (US state)":         ("us-ca", "california", "US-CA", "open"),
    "New York (US state)":           ("us-ny", "new-york", "US-NY", "open"),
    "Texas (US state)":              ("us-tx", "texas", "US-TX", "open"),
    "Canada (federal)":              ("ca-federal", "canada", "CA", "conditional"),
    "Ontario (Canada)":              ("ca-on", "ontario", "CA-ON", "conditional"),
    "British Columbia (Canada)":     ("ca-bc", "british-columbia", "CA-BC", "open"),
    "Ireland":                       ("ie", "ireland", "IE", "open"),
    "South Africa":                  ("za", "south-africa", "ZA", "unclear"),
    "Hong Kong SAR":                 ("hk", "hong-kong", "HK", "not-open"),
    "Australian Capital Territory":  ("au-act", "australian-capital-territory", "AU-ACT", "open"),
    "Northern Territory (Australia)": ("au-nt", "northern-territory", "AU-NT", "conditional"),
    "India (central / Union legislation)": ("in-central", "india", "IN", "conditional"),
}
NOTE = {
    "in-central": "India Code publishes no reuse licence. Publishing an Act of a Legislature is not "
                  "infringement under Copyright Act 1957 s.52(1)(q)(ii) only if it is accompanied by "
                  "commentary or other original matter; whether an L4 encoding with its annotations meets "
                  "that condition is a human decision. NOT INDEPENDENTLY SPOT-CHECKED: on 2026-09-22 "
                  "India Code refused both scripted and browser access and Legal Data Hunter was "
                  "rate-limiting, so this entry rests on the index agent's evidence alone.",
    "us-ny": "Statute text is not copyrightable in the United States (government edicts doctrine, "
             "Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). The site's own CC BY-NC-ND licence, "
             "with its CC+ waiver, covers the Senate's editorial content, not the law itself.",
    "us-tx": "The register states no licence and claims no copyright. Statute text is not copyrightable "
             "in the United States (government edicts doctrine, Georgia v. Public.Resource.Org, 2020).",
}

CONSEQUENCE = {
    "open": "Statute text may be deposited and quoted in an encoding, subject to the attribution "
            "above.",
    "conditional": "Reproduction is permitted on the conditions above, but the terms do not expressly "
                   "grant a right to ADAPT. An L4 encoding that quotes the statute is arguably an "
                   "adaptation. **Confirm before depositing text or quoting it in an encoding** -- a "
                   "human decision recorded here.",
    "not-open": "**Do not deposit statute text here, or quote it in an encoding, without written "
                "permission.** The terms allow accurate copying and distribution but grant no right to "
                "adapt, and reuse in a product is licensed separately. This directory holds metadata "
                "only until permission is obtained.",
    "unclear": "**Metadata only until resolved.** The register's website terms allow only non-commercial "
               "use. Section 12(8)(a) of the Copyright Act 98 of 1978 is generally read as excluding "
               "official legislative texts from copyright, but that has not been confirmed from an "
               "official source. Resolve before depositing or quoting text.",
}

LIC = """# Source license

The text of **{title}** is published on the [{register}]({register_url}).

- **Terms**: {summary}
- **Terms checked**: {today}, at {terms_url}
- **From the terms**: "{quote}"
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
    res = json.load(open(os.path.join(HERE, "round2", "agent-results.json"), encoding="utf-8"))
    extra = os.path.join(HERE, "round2", "agent-results-india.json")
    if os.path.exists(extra):
        res.update(json.load(open(extra, encoding="utf-8")))
    made, skipped, ver = [], [], []
    for jname, x in res.items():
        key, dname, code, cat = J[jname]
        base = os.path.join(ROOT, "subjects", dname)
        acts = {}
        for a in x["acts"]:
            acts.setdefault(a["title"], {**a, "topics": []})["topics"].append(a["topic"])
        for title, a in acts.items():
            status = {"yes": "VERIFIED", "not yet in force": "NOT YET IN FORCE"}.get(a["in_force"], "UNVERIFIED")
            ver.append({"jurisdiction": key, "act": title, "topics": a["topics"], "status": status,
                        "index_title": title, "nearest": []})
            d = os.path.join(base, slug(title))
            if os.path.exists(os.path.join(d, "subject.json")):
                skipped.append((key, title)); continue
            os.makedirs(os.path.join(d, "registers", "source-bundle"), exist_ok=True)
            subject = {"id": slug(title), "display_name": title, "jurisdiction": code, "citation": title,
                       "source": {"provider": x["register"]["name"], "source_id": a["identifier"],
                                  "url": a["url"], "retrieved_date": TODAY},
                       "corpus_modules": [], "projections": [], "encoding_version": "0.0.0",
                       "status": "draft"}
            with open(os.path.join(d, "subject.json"), "w", encoding="utf-8") as f:
                json.dump(subject, f, indent=2, ensure_ascii=False); f.write("\n")
            meta = {"title": title, "source_id": a["identifier"], "landing_url": a["url"],
                    "indexed_date": TODAY, "text_deposited": False, "in_force": a["in_force"],
                    "verified_how": a["verified_how"], "topics": a["topics"]}
            if a.get("notes"):
                meta["notes"] = a["notes"]
            name = re.sub(r"[^A-Za-z0-9_.-]+", "-", a["identifier"]).strip("-")[:40].rstrip("-.") or slug(title)
            with open(os.path.join(d, "registers", "source-bundle", name + ".meta.json"), "w", encoding="utf-8") as f:
                json.dump(meta, f, indent=2, ensure_ascii=False); f.write("\n")
            L = x["licence"]
            lic = LIC.format(title=title, register=x["register"]["name"], register_url=x["register"]["url"],
                             summary=L["summary"], today=TODAY, terms_url=L["terms_url"],
                             quote=L["quote"].replace('"', "'"), attribution=L["attribution"], url=a["url"],
                             note=("\n" + NOTE[key] + "\n") if key in NOTE else "",
                             consequence=CONSEQUENCE[cat], language=x["language_authenticity"])
            if a["in_force"] != "yes":
                lic += "\n## In-force status\n\n%s -- %s\n" % (a["in_force"].upper(), a["notes"])
            open(os.path.join(d, "SOURCE-LICENSE.md"), "w", encoding="utf-8").write(lic)
            made.append((key, title))
        readme = os.path.join(base, "README.md")
        if not os.path.exists(readme):
            gaps = "\n".join("- **%s**: %s" % (g["topic"], g["reason"]) for g in x["topic_gaps"])
            open(readme, "w", encoding="utf-8").write(
                "# %s/\n\n%s legislation, one subject-id per body of law, following the subject-sidecar "
                "shape described in [`subjects/README.md`](../README.md).\n\nThe subjects here were laid "
                "out on %s for the legislation governing twelve everyday topics. Each was checked against "
                "the %s; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. "
                "No statute text has been deposited and nothing is encoded yet.\n\n"
                "**Licence category: %s.** %s\n\n## Topics with no legislation here\n\n%s\n"
                % (dname, jname, TODAY, x["register"]["name"], cat, CONSEQUENCE[cat], gaps or "none"))
    json.dump(ver, open(os.path.join(HERE, "round2", "verification.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("created %d, skipped %d" % (len(made), len(skipped)))
    for s in skipped: print("  skipped", s)


if __name__ == "__main__":
    main()
