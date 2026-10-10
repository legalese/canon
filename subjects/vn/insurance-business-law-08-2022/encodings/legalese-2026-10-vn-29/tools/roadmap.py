#!/usr/bin/env python3
"""Move units of a roadmap (registers/roadmap-*.json) from `deferred`, and count them.

  python3 -I tools/roadmap.py set  registers/roadmap-law08-2022-qh15.json "Điều 15" encoded --modules law08-contract-formation.l4 [--anchor NAME] [--note TEXT]
  python3 -I tools/roadmap.py set  registers/roadmap-law08-2022-qh15.json 62-70 out-of-scope --reason "a sentence of real length"
  python3 -I tools/roadmap.py status registers/roadmap-*.json

UNIT is a unit id as the roadmap writes it ("Điều 15", "Điều 1(14)"), a comma-separated list of them, or, for the plain-article roadmaps, a range "62-70" (articles with a letter suffix, such as "Điều 20a", are named singly).
DISPOSITION is encoded | inert | out-of-scope | deferred.
`encoded` and `inert` need --modules (module file names in this directory; they are written repo-root-relative, which is what the pipeline's validator resolves);
`out-of-scope` and `deferred` need --reason (12 characters or more).
A reason or module list already on a unit is replaced, not appended to.
"""
import argparse, json, re, sys

PREFIX = "subjects/vn/insurance-business-law-08-2022/encodings/legalese-2026-10-vn-29/"


def load(p):
    return json.load(open(p, encoding="utf-8"))


def save(p, r):
    json.dump(r, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a").write("\n")


def pick(r, spec):
    ids = [u["id"] for u in r["units"]]
    out = []
    for part in [s.strip() for s in spec.split(",") if s.strip()]:
        m = re.fullmatch(r"(\d+)-(\d+)", part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            got = [i for i in ids if re.fullmatch(r"Điều (\d+)", i) and a <= int(i.split()[1]) <= b]
            if not got:
                sys.exit(f"range {part}: no unit of this roadmap falls in it")
            out += got
        else:
            if part not in ids:
                sys.exit(f"no unit '{part}' in this roadmap (ids look like '{ids[0]}')")
            out.append(part)
    return out


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("set")
    s.add_argument("roadmap"); s.add_argument("unit"); s.add_argument("disposition", choices=["encoded", "inert", "out-of-scope", "deferred"])
    s.add_argument("--modules"); s.add_argument("--reason"); s.add_argument("--anchor"); s.add_argument("--note")
    t = sub.add_parser("status"); t.add_argument("roadmaps", nargs="+")
    a = ap.parse_args()
    if a.cmd == "status":
        for p in a.roadmaps:
            r = load(p); c = {}
            for u in r["units"]:
                c[u["disposition"]] = c.get(u["disposition"], 0) + 1
            print(f"{p}: {len(r['units'])} units  " + "  ".join(f"{k} {v}" for k, v in sorted(c.items())))
        return
    r = load(a.roadmap)
    ids = pick(r, a.unit)
    if a.disposition in ("encoded", "inert") and not a.modules:
        sys.exit("encoded and inert need --modules")
    if a.disposition in ("out-of-scope", "deferred") and not (a.reason and len(a.reason) >= 12):
        sys.exit("out-of-scope and deferred need --reason of at least 12 characters")
    for u in r["units"]:
        if u["id"] in ids:
            u["disposition"] = a.disposition
            u.pop("reason", None); u.pop("modules", None)
            if a.disposition in ("out-of-scope", "deferred"):
                u["reason"] = a.reason
            else:
                u["modules"] = [PREFIX + m.strip() for m in a.modules.split(",")]
            if a.anchor: u["anchor"] = a.anchor
            if a.note: u["note"] = (u.get("note", "") + "; " if u.get("note") else "") + a.note
    save(a.roadmap, r)
    print(f"{len(ids)} unit(s) -> {a.disposition}")


main()
