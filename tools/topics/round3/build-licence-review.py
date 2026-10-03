#!/usr/bin/env python3
"""Collect the licence evidence the index agents gathered, for a human to decide on.

Writes, next to the agent results:
  licence-review.md              one row per jurisdiction: what the register asserts, quoted
  licence-decisions.template.json  every jurisdiction, category left empty, for a human to fill

A human copies the template to licence-decisions.json and sets each "category" to one of
open | conditional | not-open | unclear, adding "decided_by" and an optional "note" that is
copied into every SOURCE-LICENSE.md for that jurisdiction. scaffold-round3.py reads that file;
anything not decided is scaffolded as "unclear" and metadata-only.

    python tools/topics/round3/build-licence-review.py
"""
import glob, importlib.util, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "scaffold3", os.path.join(os.path.dirname(HERE), "scaffold-round3.py"))
scaffold3 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(scaffold3)
SKIP = {"licence-decisions.json", "licence-decisions.template.json", "verification.json"}


def key_of(jname):
    """The display name; scaffold3.ident() gives the key the decisions file must use."""
    return re.sub(r"\s*\((US state|US|Canada)\)$", "", jname).strip()


def main():
    res = {}
    for f in sorted(glob.glob(os.path.join(HERE, "*.json"))):
        if os.path.basename(f) in SKIP:
            continue
        res.update(json.load(open(f, encoding="utf-8")))
    rows, template = [], {}
    for jname, x in sorted(res.items(), key=lambda kv: key_of(kv[0])):
        L = x.get("licence") or {}
        acts = len(x.get("acts") or [])
        quote = re.sub(r"\s+", " ", (L.get("quote") or "")).strip()
        rows.append({
            "jurisdiction": key_of(jname),
            "key": scaffold3.ident(jname)[0],
            "country": "Canada" if jname.endswith("(Canada)") else "US",
            "acts": acts,
            "register": (x.get("register") or {}).get("name", ""),
            "terms_url": L.get("terms_url") or "",
            "agent_verdict": "reuse and adaptation permitted" if L.get("open_licence") else "not established",
            "summary": re.sub(r"\s+", " ", L.get("summary") or "").strip(),
            "quote": quote,
            "language": re.sub(r"\s+", " ", x.get("language_authenticity") or "").strip(),
        })
        template[scaffold3.ident(jname)[0]] = {"jurisdiction": key_of(jname), "category": "",
                                               "decided_by": "", "note": ""}

    out = [
        "# Round 3 licence evidence, for a human decision",
        "",
        "One row per jurisdiction, as the index agents found it on %s. **Nothing here is a decision.**"
        % "2026-09-23",
        "Record decisions in `licence-decisions.json` (copy `licence-decisions.template.json`), using",
        "one of `open`, `conditional`, `not-open`, `unclear`. `scaffold-round3.py` treats anything",
        "undecided as `unclear`, which means metadata only: no statute text is ever deposited there.",
        "",
        "For US states, remember that the text of a statute is not copyrightable at all: it is an edict",
        "of government (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). A register's copyright",
        "notice may still validly cover a publisher's annotations and numbering, and a platform's terms",
        "of use bind whoever takes text *from that platform* as a matter of contract, whatever the",
        "copyright position. Those are two different questions and this sheet keeps them apart.",
        "",
        "| jurisdiction (decisions key) | Acts | agent's reading | what the register asserts |",
        "|---|---|---|---|",
    ]
    for r in rows:
        assertion = r["summary"][:300] + ("..." if len(r["summary"]) > 300 else "")
        out.append("| **%s** (`%s`) | %d | %s | %s |" % (r["jurisdiction"], r["key"], r["acts"],
                                                         r["agent_verdict"], assertion or "nothing found"))
    out += ["", "## Quoted terms, register and language, per jurisdiction", ""]
    for r in rows:
        out += ["### %s -- `%s` (%s)" % (r["jurisdiction"], r["key"], r["country"]),
                "",
                "- **Register**: %s" % (r["register"] or "(none identified)"),
                "- **Terms page**: %s" % (r["terms_url"] or "(none found)"),
                "- **Acts indexed**: %d" % r["acts"],
                "- **Agent's reading**: %s" % r["agent_verdict"],
                "- **Quoted**: %s" % ('"%s"' % r["quote"] if r["quote"] else "(the register states no terms)"),
                "- **Language**: %s" % (r["language"] or "(not recorded)"),
                ""]
    open(os.path.join(HERE, "licence-review.md"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    with open(os.path.join(HERE, "licence-decisions.template.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(template, f, indent=2, ensure_ascii=False, sort_keys=True); f.write("\n")
    print("licence-review.md and licence-decisions.template.json: %d jurisdictions" % len(rows))


if __name__ == "__main__":
    main()
