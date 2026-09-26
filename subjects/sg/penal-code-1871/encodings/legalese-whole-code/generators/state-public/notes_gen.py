"""Write notes/state-public-coverage.md from the part files (dispositions are hand-set below)."""
import re, sys, json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lib, part_contempts, part_assembly, part_servants, part_state
for m in [part_contempts, part_assembly, part_servants, part_state]:
    m.module()

FAMILY = {}
for s in ["121","121A","121B","121C","121D","122","123","124","125","126","127","128","129","130"]: FAMILY[s]="state"
for s in ["130B(2)","130C"]: FAMILY[s]="piracy"
FAMILY["130E"]="genocide"
for s in ["131","132","133","134","135","136","137","138","140"]: FAMILY[s]="armed-forces"
for s in ["143","144","145","147","148","150","151","152","153","154","155","156","157","158"]: FAMILY[s]="unlawful-assembly"
for s in ["161","162","163","164","165","166","167","168","169","170","171"]: FAMILY[s]="public-servant"

def calls(name, seen=None):
    seen = seen if seen is not None else []
    body = lib.RULE_BODIES.get(name, "")
    for c in re.findall(r"`([^`]+)` f\b", body):
        if c in lib.RULE_BODIES and c not in seen and c != name:
            seen.append(c)
            calls(c, seen)
    return seen

def defines(sec, offfn):
    base = re.match(r"\d+[A-Z]*", sec).group(0)
    d = calls(offfn)
    secs = []
    for c in d:
        m = re.search(r"section (\d+[A-Z]*)", c)
        if m: secs.append(m.group(1))
    extra = {"guilty of rioting": "146", "commits piracy": "130B(1)", "commits genocide": "130D",
             "takes a gratification to influence a public servant by corrupt means": "162",
             "takes a gratification for personal influence with a public servant": "163"}
    for c in d:
        if c in extra: secs.append(extra[c])
    secs = sorted(set(secs) | {base}, key=lambda x: (int(re.match(r"\d+", x).group(0)), x))
    return "s " + ", ".join(secs) if len(secs) == 1 else "ss " + ", ".join(secs)

entries = []
for sec, offname, offfn, ftype in lib.CHARGES:
    fam = FAMILY.get(sec) or ("contempt" if int(re.match(r"\d+", sec).group(0)) >= 172 else "?")
    entries.append(dict(section=sec, title=offname, defines=defines(sec, offfn), family=fam,
                        offenceFn=offfn, chargeFn=f"charge under s {sec}", definitionFns=calls(offfn),
                        factsType=ftype, factsParam="f"))
open(__file__.rsplit("/", 1)[0] + "/catalogue.json", "w").write(json.dumps(entries, indent=2))
print(len(entries), "catalogue entries")


# ---------------------------------------------------------------- coverage
toc = []
cur = None
chap = None
for line in open(lib.SRC, encoding="utf-8").read().split("\n")[265:455]:
    s = line.strip()
    if not s or "Singapore Statutes Online" in s:
        continue
    m = re.match(r"Chapter (\S+) — (.*)", s)
    if m:
        chap = m.group(1); continue
    m = re.match(r"(\d+[A-Z]?) (.*)", s)
    if m:
        cur = [chap, m.group(1), m.group(2)]; toc.append(cur)
    elif cur:
        cur[2] += " " + s

by_base = {}
for e in entries:
    base = re.match(r"\d+[A-Z]*", e["section"]).group(0)
    by_base.setdefault(base, []).append(e)

SPECIAL = {
    "130A": ("encoded", "definition, no charge", ["harbours within section 130A"]),
    "140A": ("encoded", "definition, no charge", ["harbours within section 140A"]),
    "140B": ("encoded", "application rule, no charge: the leaf `a member of the Singapore Police Force or any volunteer, auxiliary or special force attached to it`, ORed beside the armed-forces leaf in every Chapter 7 ladder", []),
    "139": ("encoded", "saving (bar to punishment), no charge; not repeated in the Chapter 7 ladders (FORK SP-139)", ["not subject to punishment under this Code within section 139"]),
    "141": ("encoded", "definition, no charge; read by ss 143-158 and by other groups", ["unlawful assembly within section 141", "5 or more persons"]),
    "142": ("encoded", "definition, no charge", ["member of an unlawful assembly within section 142"]),
    "146": ("encoded", "definition of rioting, no charge (punished by ss 147, 148)", ["guilty of rioting"]),
    "149": ("encoded", "deeming rule, no charge of its own: charged as the other offence read with s 149", ["guilty of that offence within section 149"]),
    "130D": ("encoded", "definition, no charge (punished by s 130E)", ["commits genocide"]),
    "151A": ("repealed", "[Repealed by Act 51 of 2007]", []),
    "159": ("repealed", "[Repealed by Act 51 of 2007]", []),
    "160": ("repealed", "[Repealed by Act 51 of 2007]", []),
}
rows = []
for ch, sec, head in toc:
    head = lib.to_ascii(head)
    if sec in SPECIAL:
        disp, note, fns = SPECIAL[sec]
    elif sec in by_base:
        disp, note = "encoded", "offence"
        fns = []
        for e in by_base[sec]:
            for f in e["definitionFns"] + [e["offenceFn"], e["chargeFn"]]:
                if f not in fns:
                    fns.append(f)
    else:
        disp, note, fns = "deferred", "NOT FOUND - check", []
    rows.append(f"| {ch} | {sec} | {head} | {disp} | {note} | " + ", ".join(f"`{f}`" for f in fns) + " |")

cov = open(__file__.rsplit("/", 1)[0] + "/coverage-head.md").read()
cov += "\n| Ch | s | heading | disposition | kind | functions |\n| --- | --- | --- | --- | --- | --- |\n" + "\n".join(rows) + "\n"
cov += "\n## Catalogue entries (`OFFENCES`, reference/charge-generator-catalogue.ts)\n\nOne per punishing provision, generated from the encoding by `notes/state-public-gen/notes_gen.py`.\nProposed new `family` slugs: `state`, `piracy`, `genocide`, `armed-forces`, `unlawful-assembly`, `public-servant`, `contempt`.\n\n```ts\n"
for e in entries:
    cov += "  " + json.dumps(e, ensure_ascii=True).replace('"section"', "section").replace('"title"', "title").replace('"defines"', "defines").replace('"family"', "family").replace('"offenceFn"', "offenceFn").replace('"chargeFn"', "chargeFn").replace('"definitionFns"', "definitionFns").replace('"factsType"', "factsType").replace('"factsParam"', "factsParam") + ",\n"
cov += "```\n"
open("/Users/mengwong/src/legalese/pc-encode/notes/state-public-coverage.md", "w").write(cov)
print(sum(1 for r in rows if "| encoded |" in r), "encoded;", sum(1 for r in rows if "| deferred |" in r), "deferred;", sum(1 for r in rows if "| repealed |" in r), "repealed;", len(rows), "rows")
