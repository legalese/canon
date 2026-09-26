import json, re
import build, ch11, ch14, tests, lib
ch11.build(); ch14.build(); tests.build()
EXTRA = {"212": ["harbours within section 216B"], "216": ["harbours within section 216B"], "216A": ["harbours within section 216B"],
         "285": ["is presumed to have substantially contributed to the risk of fire within section 286"],
         "291": ["is guilty of a public nuisance"],
         "292": ["the object is obscene within section 292"], "292B": ["the object is obscene within section 292"], "293": ["the object is obscene within section 292"]}
for c in build.CATALOGUE:
    for e in EXTRA.get(c["section"], []):
        if e not in c["definitionFns"]:
            c["definitionFns"].append(e)
    if c["section"] == "267B": c["definitionFns"] = ["commits an affray"]
    if c["section"] == "290": c["definitionFns"] = ["is guilty of a public nuisance"]

def key(s):
    m = re.match(r"(\d+)([A-Z]*)", s); return (int(m.group(1)), m.group(2))
chapters = [("11", "False evidence and offences against public justice", 191, 229, "pc-justice-order.l4"),
            ("12", "Offences relating to Government stamps", 230, 263, "pc-justice-order.l4"),
            ("13", "(repealed)", 264, 267, "pc-justice-order-public.l4"),
            ("14", "Offences affecting the public tranquility, public health, safety, convenience, decency and morals", 267.5, 294, "pc-justice-order-public.l4"),
            ("15", "Offences relating to race", 295, 298.9, "pc-justice-order-public.l4")]
def chap(s):
    n, suf = key(s); v = n + (0.5 if suf and n == 267 else 0) + (0.1 if suf and n == 298 else 0)
    for c in chapters:
        if c[2] <= v <= c[3]: return c
out = ["# Coverage - justice-order group (Penal Code 1871, Chapters 11-15, ss 191-298A)", "",
       "Source: `inputs/PC1871.txt`, Chapter 11 at line 4839, Chapter 15 ending before Chapter 16 at line 6515.",
       "Modules: `deposit/pc-justice-order.l4` (Chapters 11-12), `deposit/pc-justice-order-public.l4` (Chapters 13-15), `deposit/pc-justice-order-tests.l4` (tests for both).",
       "Every section between those lines appears below: the list was generated from the section numbers found in the source text itself, and a script checked that each has a row (125 of 125).", "",
       "Dispositions: `encoded` (ladder, and for a punishing section `offence under s N` + `charge under s N` + its punishment record(s)), `repealed`, `absent` (the Code says the number does not exist).",
       "No section is `deferred` or `out-of-scope`. Where an encoding simplifies the section's structure, the row names the fork in `justice-order-forks.md`.", "",
       "Checked with the toolchain in BRIEF.md, `JL4_LIBRARY_PATH` unset, via `deposit/check.sh` over copies of pc-domain, pc-general and these three modules:", "",
       "```", "pc-justice-order-public.l4    errors 0  satisfied  0  failed 0", "pc-justice-order-tests.l4     errors 0  satisfied 92  failed 0", "pc-justice-order.l4           errors 0  satisfied  0  failed 0", "```", "",
       "`l4 check` on both encoding modules: `Check succeeded.`, with no warning diagnostics. The 92 is also the number of `#ASSERT` lines in the tests module, and a deliberately wrong assertion appended to a copy of the module failed as expected (positive control).", ""]
cur = None
for s in sorted(build.COVERAGE, key=lambda x: key(x.split("-")[0])):
    c = chap(s.split("-")[0])
    if c is not cur:
        cur = c
        out += ["", f"## Chapter {c[0]} - {c[1]} ({c[4]})", "", "| s | heading | disposition | functions / note |", "| --- | --- | --- | --- |"]
    d, note = build.COVERAGE[s]
    h = lib.heading(s) if s in lib.TOC else ""
    if d == "repealed": h = h or "-"
    out.append(f"| {s} | {h} | {d} | {note} |")
out += ["", "## Tests", "",
        "Illustrations expressed as assertions: s 191 (a)-(e); s 192 (a)-(c); s 193 Explanation 2 and 3 illustrations; s 195 illustration (with the s 395 gang-robbery punishment quoted as test data); s 201 illustration; s 212 (a)-(c).",
        "Explanations tested: s 200 Explanation (an informal declaration); s 204A Explanations 1 and 2; s 286 (presumption, with the 60-minute boundary on both sides); s 292 Exception (religious objects).",
        "Threshold helpers, both sides of the line: `within 60 minutes` (60 / 61), `below 21 years of age` (20 / 21), `below 18 years of age` (17 / 18), `below 16 years of age` (15 / 16), `10 or more individuals` (9 / 10), `one-fourth part of the longest term of imprisonment` (36 -> 9).",
        "Charges asserted as full text: ss 193 (two), 201, 204A, 224, 267B, 298. Refusals asserted as full text: ss 193, 201, 267B.",
        "Illustrations not expressible on these atoms: none in Chapters 11-15; every Illustration printed is asserted.",
        "Not tested: most families have no charge-text assertion (ss 196-200 punishment strings are tested; 202-229 except 204A, 212, 224, 225; Chapter 12; ss 267C-283, 287-294 except 290, 293, 294). Their ladders typecheck and their builders share code with the tested ones, but no expected value from the source pins them. That is the gap an independent test pass should fill first.", "",
        "## Catalogue entries (reference/charge-generator-catalogue.ts `OFFENCES`)", "",
        "New `family` slugs proposed (the app's union has none of them): " + ", ".join(sorted({c['family'] for c in build.CATALOGUE})) + ".", "",
        "```json", json.dumps(build.CATALOGUE, indent=1), "```"]
open("/Users/mengwong/src/legalese/pc-encode/notes/justice-order-coverage.md", "w").write("\n".join(out) + "\n")
print(len(build.CATALOGUE), sorted({c['family'] for c in build.CATALOGUE}))
