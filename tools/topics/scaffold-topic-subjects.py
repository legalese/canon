#!/usr/bin/env python3
"""Lay out a subject directory for every topic Act that does not have one yet.

Each directory follows the shape of the existing unencoded subjects (see
subjects/western-australia/*): subject.json, SOURCE-LICENSE.md, and
registers/source-bundle/<id>.meta.json. No statute text is written -- harvesting the text is a
separate, per-jurisdiction step with its own terms -- so nothing here reproduces legislation.

Singapore directories are written with the SSO harvester's own slug(), licence template and
subject.json shape, so its nightly run fills these directories rather than creating duplicates.

Existing directories are never modified: a subject that already exists is reported and skipped.
"""
import datetime, importlib.util, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
ROOT = os.path.dirname(TOOLS)
SUBJECTS = os.path.join(ROOT, "subjects")
TODAY = datetime.date.today().isoformat()

spec = importlib.util.spec_from_file_location("sso", os.path.join(TOOLS, "fetch-sso-corpus.py"))
sso = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sso)
slug = sso.slug

DIRS = {"sg": "singapore", "au-cth": "commonwealth-of-australia", "nz": "new-zealand",
        "au-wa": "western-australia", "au-sa": "south-australia", "au-nsw": "new-south-wales",
        "au-vic": "victoria", "au-qld": "queensland", "au-tas": "tasmania", "uk": "united-kingdom"}
CODES = {"sg": "SG", "au-cth": "AU-CTH", "nz": "NZ", "au-wa": "AU-WA", "au-sa": "AU-SA",
         "au-nsw": "AU-NSW", "au-vic": "AU-VIC", "au-qld": "AU-QLD", "au-tas": "AU-TAS", "uk": "UK"}
NAMES = {"sg": "Singaporean", "au-cth": "Commonwealth of Australia", "nz": "New Zealand",
         "au-wa": "Western Australian", "au-sa": "South Australian", "au-nsw": "New South Wales",
         "au-vic": "Victorian", "au-qld": "Queensland", "au-tas": "Tasmanian", "uk": "United Kingdom"}

# register ids read from the NSW Public Acts in force table in a browser, 2026-09-22
NSW_IDS = {
    "Duties Act 1997": "act-1997-123", "Electricity Supply Act 1995": "act-1995-094",
    "Energy and Utilities Administration Act 1987": "act-1987-103",
    "Fair Trading Act 1987": "act-1987-068", "Industrial Relations Act 1996": "act-1996-017",
    "Long Service Leave Act 1955": "act-1955-038", "Motor Accident Injuries Act 2017": "act-2017-010",
    "National Energy Retail Law (Adoption) Act 2012": "act-2012-037",
    "Payroll Tax Act 2007": "act-2007-021", "Residential Tenancies Act 2010": "act-2010-042",
    "Retail Leases Act 1994": "act-1994-046", "Strata Schemes Management Act 2015": "act-2015-050",
    "Superannuation Administration Act 1996": "act-1996-039",
    "Water Industry Competition Act 2006": "act-2006-104",
    "Workers Compensation Act 1987": "act-1987-070",
    "Workplace Injury Management and Workers Compensation Act 1998": "act-1998-086",
}
NZ_IDS = {"Holidays Act 2003": "2003/129"}

PROVIDERS = {
    "au-cth": ("Federal Register of Legislation", "https://www.legislation.gov.au/"),
    "au-nsw": ("NSW Legislation", "https://legislation.nsw.gov.au/"),
    "au-vic": ("Victorian Legislation", "https://www.legislation.vic.gov.au/"),
    "au-qld": ("Queensland Legislation", "https://www.legislation.qld.gov.au/"),
    "au-sa": ("South Australian Legislation", "https://www.legislation.sa.gov.au/"),
    "au-tas": ("Tasmanian Legislation Online", "https://www.legislation.tas.gov.au/"),
    "nz": ("New Zealand Legislation (Parliamentary Counsel Office)", "https://www.legislation.govt.nz/"),
    "uk": ("legislation.gov.uk (The National Archives)", "https://www.legislation.gov.uk/"),
}
OWNER = {"au-cth": "Commonwealth of Australia", "au-nsw": "State of New South Wales",
         "au-qld": "State of Queensland", "au-sa": "State of South Australia",
         "au-tas": "State of Tasmania"}

CC_BY = """# Source license

The quoted text of **{title}** is sourced from the [{provider}]({home}).

- **Copyright owner**: {owner}.
- **License**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
- **Terms checked**: {checked}, at {terms_url}
- **Source**: {url}
- **Excluded from the license**: coats of arms, logos and trade marks on the source site,
  and any material marked otherwise.

## Required attribution

Sourced from the {provider} at {today}: "{title}", {owner}, licensed under CC BY 4.0
(https://creativecommons.org/licenses/by/4.0/).

If this encoding modifies or adapts the quoted text (rather than reproducing it verbatim),
the attribution must instead read "Based on content from the {provider} ...", per the CC BY 4.0
terms.

## Status of this deposit

No statute text has been deposited yet. This file records the terms that will govern the
text when it is harvested.
"""

OGL = """# Source license

The quoted text of **{title}** is sourced from [legislation.gov.uk](https://www.legislation.gov.uk/),
published by The National Archives.

- **Copyright owner**: Crown copyright.
- **License**: [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
- **Terms checked**: {checked}, at https://www.legislation.gov.uk/help
- **Source**: {url}

## Required attribution

Contains public sector information licensed under the Open Government Licence v3.0.

## Status of this deposit

No statute text has been deposited yet.
"""

NZ = """# Source license

The quoted text of **{title}** is sourced from the [New Zealand Legislation website](https://www.legislation.govt.nz/),
published by the Parliamentary Counsel Office.

- **Copyright owner**: none. Under section 27 of the Copyright Act 1994 there is no copyright in
  New Zealand legislation, so no licence is needed and none is granted.
- **Terms checked**: {checked}, at https://www.legislation.govt.nz/copyright/
- **Source**: {url}

## Required attribution

None is legally required. Provenance is recorded in `registers/source-bundle/` so that any
encoded rule can be traced to the text it encodes.

## Status of this deposit

No statute text has been deposited yet. The register's listing pages refuse scripted
clients; bulk retrieval should go through the PCO API (key from contact@pco.govt.nz), which is
also how the register id for this Act will be confirmed.
"""

VIC = """# Source license

The text of **{title}** is published on the [Victorian Legislation website](https://www.legislation.vic.gov.au/)
by the Office of the Chief Parliamentary Counsel.

- **Copyright owner**: the Government Printer for the State of Victoria.
- **License**: **none. Not openly licensed.** The site's copyright notice (checked {checked},
  https://www.legislation.vic.gov.au/copyright) states that no part may be reproduced except in
  accordance with the Copyright Act 1968 (Cth), and that authorised electronic versions are
  published for personal use only.
- **Source**: {url}

## Consequence for this subject

**Do not deposit Victorian statute text here, and do not quote it in an encoding, without
written permission** from the Office of the Chief Parliamentary Counsel (ocpc@ocpc.vic.gov.au).
Canon's inert style quotes the statute inline, which is reproduction. This directory holds
metadata only until permission is obtained, and the permission, when granted, belongs in this
file.
"""


def main():
    ver = json.load(open(os.path.join(HERE, "verification.json"), encoding="utf-8"))
    idx = {}
    for j in ("au-cth", "au-qld", "au-tas", "au-vic", "au-sa", "uk"):
        idx[j] = {a["title"].replace("’", "'"): a
                  for a in json.load(open(os.path.join(TOOLS, "indexes", j + ".json"),
                                          encoding="utf-8"))["acts"]}
    manifest = json.load(open(os.path.join(TOOLS, "sso-acts-manifest.json"), encoding="utf-8"))
    by_title = {}
    for k, t in manifest.items():
        by_title[t] = k
        by_title[re.sub(r"\s+\d{4}$", "", t)] = k
    made, skipped = [], []
    for r in ver:
        jur, act = r["jurisdiction"], r["act"]
        d = os.path.join(SUBJECTS, DIRS[jur], slug(act))
        existing = [x for x in os.listdir(os.path.join(SUBJECTS, DIRS[jur]))
                    if os.path.exists(os.path.join(SUBJECTS, DIRS[jur], x, "subject.json"))
                    and json.load(open(os.path.join(SUBJECTS, DIRS[jur], x, "subject.json"),
                                       encoding="utf-8")).get("display_name") == act] \
            if os.path.isdir(os.path.join(SUBJECTS, DIRS[jur])) else []
        if existing or os.path.exists(os.path.join(d, "subject.json")):
            skipped.append((jur, act, existing[0] if existing else slug(act)))
            continue
        os.makedirs(os.path.join(d, "registers", "source-bundle"), exist_ok=True)
        sid, url, extra = None, None, {}
        if jur == "sg":
            sid = by_title.get(act) or by_title.get(re.sub(r"\s+\d{4}$", "", act))
            url = "https://sso.agc.gov.sg/Act/%s" % sid
        elif jur in idx:
            a = idx[jur][act.replace("’", "'")]
            sid, url = a["source_id"], a["url"]
            if jur == "au-sa":
                sid = None; extra["note"] = "SA register id not yet resolved; listed in the SA Current Titles list"
        elif jur == "au-nsw":
            sid = NSW_IDS[act]; url = "https://legislation.nsw.gov.au/view/html/inforce/current/" + sid
        elif jur == "nz":
            sid = NZ_IDS.get(act)
            url = ("https://www.legislation.govt.nz/act/public/%s/en/latest/" % sid if sid else
                   "https://www.legislation.govt.nz/items/?legislation_type=act&search_field=title&search_term="
                   + act.replace(" ", "+"))
            if not sid:
                extra["note"] = "register id not yet resolved; url is the official title search"
        if r["status"] == "NOT YET IN FORCE":
            extra["in_force"] = False
            extra["note"] = (extra.get("note", "") + "; " if extra.get("note") else "") + \
                "enacted but not yet in force at %s" % TODAY
        # ---- subject.json
        if jur == "sg":
            subject = {"id": slug(act), "display_name": act, "jurisdiction": "SG", "citation": act,
                       "act_id": sid,
                       "source": {"provider": "Singapore Statutes Online (AGC)", "source_id": sid,
                                  "url": url, "retrieved_date": TODAY},
                       "corpus_modules": [], "projections": [], "encoding_version": "0.0.0",
                       "status": "draft"}
        else:
            subject = {"id": slug(act), "display_name": act, "jurisdiction": CODES[jur], "citation": act,
                       "source": {"provider": PROVIDERS[jur][0], "source_id": sid, "url": url,
                                  "retrieved_date": TODAY},
                       "corpus_modules": [], "projections": [], "encoding_version": "0.0.0",
                       "status": "draft"}
        json.dump(subject, open(os.path.join(d, "subject.json"), "w", encoding="utf-8"), indent=2)
        open(os.path.join(d, "subject.json"), "a", encoding="utf-8").write("\n")
        # ---- source-bundle metadata (no text)
        meta = {"title": act, "source_id": sid, "landing_url": url, "indexed_date": TODAY,
                "text_deposited": False, **extra}
        name = (sid or slug(act)).replace("/", "-")
        json.dump(meta, open(os.path.join(d, "registers", "source-bundle", name + ".meta.json"), "w",
                             encoding="utf-8"), indent=2)
        # ---- SOURCE-LICENSE.md
        if jur == "sg":
            lic = sso.LICENSE.format(title=act, url=url, retrieved=TODAY,
                                     provenance="- **Extraction window** (cl.13(d)(i)): not yet engaged. "
                                     "No text has been\n  deposited; the nightly harvest will fetch it inside "
                                     "the 3 a.m. to 7 a.m. window.")
        elif jur == "uk":
            lic = OGL.format(title=act, checked=TODAY, url=url)
        elif jur == "nz":
            lic = NZ.format(title=act, checked=TODAY, url=url)
        elif jur == "au-vic":
            lic = VIC.format(title=act, checked=TODAY, url=url)
        else:
            terms = {"au-cth": "https://www.legislation.gov.au/terms-of-use",
                     "au-nsw": "https://legislation.nsw.gov.au/copyright",
                     "au-qld": "https://www.legislation.qld.gov.au/copyright",
                     "au-sa": "https://www.legislation.sa.gov.au/copyright",
                     "au-tas": "https://www.legislation.tas.gov.au/copyrightanddisclaimer"}[jur]
            lic = CC_BY.format(title=act, provider=PROVIDERS[jur][0], home=PROVIDERS[jur][1],
                               owner=OWNER[jur], checked=TODAY, terms_url=terms, url=url, today=TODAY)
        open(os.path.join(d, "SOURCE-LICENSE.md"), "w", encoding="utf-8").write(lic)
        made.append((jur, act, slug(act)))
    # ---- a README for each jurisdiction directory that lacks one
    for jur, dname in DIRS.items():
        p = os.path.join(SUBJECTS, dname, "README.md")
        if os.path.isdir(os.path.dirname(p)) and not os.path.exists(p):
            open(p, "w", encoding="utf-8").write(
                "# %s/\n\n%s Acts, one subject-id per body of law, following the subject-sidecar "
                "shape described in [`subjects/README.md`](../README.md).\n\nThe subjects here were "
                "laid out on %s for the Acts that govern twelve everyday topics -- payroll, leave, "
                "termination, pensions, government benefits, personal tax, insurance claims, utility "
                "billing, passenger compensation, consumer and tenancy, customs and duties, and work "
                "permits. The mapping and the check of each Act against the official register are in "
                "`tools/topics/`. No statute text has been deposited and nothing is encoded yet.\n"
                % (dname, NAMES[jur], TODAY))
    print("created %d, skipped %d (already present)" % (len(made), len(skipped)))
    for s in skipped:
        print("  skipped %-7s %-55s -> %s" % s)
    json.dump({"created": made, "skipped": skipped}, open(os.path.join(HERE, "scaffold-report.json"),
              "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
