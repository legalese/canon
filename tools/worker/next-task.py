#!/usr/bin/env python3
"""Dry run of a canon worker: survey the corpus and say what a runner WOULD claim now.

Nothing is claimed, fetched, written or pushed. The only network call is a read of the
claim branches on origin (git ls-remote / fetch of refs/heads/claim/*), so the answer
reflects what other runners hold right now.

    python tools/worker/next-task.py
    python tools/worker/next-task.py --weekly-used 12 --five-hour-used 30
    python tools/worker/next-task.py --no-remote        # skip reading claims from origin

The usage figures come from the runner's own session (the routine reads them with its
usage tool and passes them in); this script applies the policy in config.json to them.
See WORKER.md for the full procedure a real run follows.
"""
import argparse, datetime, glob, json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SUBJECTS = os.path.join(ROOT, "subjects")
CFG = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))

KEY_TO_DIR = {
    "sg": "singapore", "au-cth": "commonwealth-of-australia", "nz": "new-zealand",
    "au-wa": "western-australia", "au-sa": "south-australia", "au-nsw": "new-south-wales",
    "au-vic": "victoria", "au-qld": "queensland", "au-tas": "tasmania", "uk": "united-kingdom",
    "au-act": "australian-capital-territory", "au-nt": "northern-territory",
    "us-federal": "united-states", "us-ca": "california", "us-ny": "new-york", "us-tx": "texas",
    "ca-federal": "canada", "ca-on": "ontario", "ca-bc": "british-columbia",
    "in-central": "india", "ie": "ireland", "za": "south-africa", "hk": "hong-kong",
}
# "Part 4 — Title", "Part IIB — Title", "Part 6B — Title"; the dash is sometimes mis-decoded (U+FFFD)
PART_RE = re.compile(r"^[ \t\xa0]*Part[ \xa0]+([0-9]+[A-Z]*(?:[.-][0-9]+[A-Z]*)*|[IVXL]+[A-Z]*)[ \xa0]*[—–�-][ \xa0]*(.+?)\s*$", re.M)
SCHED_RE = re.compile(r"^[ \t\xa0]*Schedule[ \xa0]+\d+[A-Z]*[ \xa0]*[—–�-]", re.M)


def git(*args):
    r = subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True)
    return r.stdout.strip()


def targets():
    """Topic Acts in tracker order, plus every subject that already has L4 modules."""
    out, seen = [], set()
    by_name = {}
    for sj in glob.glob(os.path.join(SUBJECTS, "*", "*", "subject.json")):
        try:
            s = json.load(open(sj, encoding="utf-8"))
        except Exception:
            continue
        jd = os.path.basename(os.path.dirname(os.path.dirname(sj)))
        by_name[(jd, s.get("display_name"))] = os.path.dirname(sj)
    for f in ("verification.json", os.path.join("round2", "verification.json")):
        p = os.path.join(ROOT, "tools", "topics", f)
        if os.path.exists(p):
            for r in json.load(open(p, encoding="utf-8")):
                d = by_name.get((KEY_TO_DIR[r["jurisdiction"]], r["act"]))
                if d and d not in seen:
                    seen.add(d); out.append(d)
    for sj in glob.glob(os.path.join(SUBJECTS, "*", "*", "subject.json")):
        d = os.path.dirname(sj)
        if d not in seen and glob.glob(os.path.join(d, "*.l4")):
            seen.add(d); out.append(d)
    return out


def parts_of(text):
    """Parts in the body of an Act, up to the first Schedule. Headings appear once in the
    contents and again in the body; the body starts where the first heading recurs. Part
    numbers can repeat (Parts inside Chapters), so a unit is identified by its position."""
    hits = [(m.start(), m.group(1), m.group(2).strip()) for m in PART_RE.finditer(text)]
    if not hits:
        return []
    key = (hits[0][1], hits[0][2])
    again = [h for h in hits[1:] if (h[1], h[2]) == key]
    start = again[0][0] if again else hits[0][0]
    sched = [m.start() for m in SCHED_RE.finditer(text) if m.start() > start]
    stop = sched[0] if sched else len(text)
    body = [h for h in hits if start <= h[0] < stop]
    parts = []
    for i, (pos, num, title) in enumerate(body):
        end = body[i + 1][0] if i + 1 < len(body) else stop
        parts.append({"part": "%d:%s" % (i + 1, num), "title": title[:70], "chars": end - pos})
    return parts


def survey(d):
    rel = os.path.relpath(d, SUBJECTS).replace(os.sep, "/")
    jd = rel.split("/")[0]
    pol = CFG["jurisdictions"].get(jd, {"licence": "unclear", "fetch": "not-built"})
    s = json.load(open(os.path.join(d, "subject.json"), encoding="utf-8"))
    texts = [p for p in glob.glob(os.path.join(d, "registers", "source-bundle", "*"))
             if p.endswith((".txt", ".xml", ".html"))]
    l4 = glob.glob(os.path.join(d, "*.l4"))
    plan_p = os.path.join(d, "registers", "encoding-plan.json")
    plan = json.load(open(plan_p, encoding="utf-8")) if os.path.exists(plan_p) else None
    review = os.path.join(d, "reviews", "human-1.md")
    wants_response = (os.path.exists(review)
                      and "changes requested" in open(review, encoding="utf-8").readline().lower()
                      and not os.path.exists(os.path.join(d, "reviews", "ai-2.md")))
    return {"rel": rel, "jd": jd, "name": s.get("display_name"), "policy": pol, "texts": texts,
            "l4": l4, "plan": plan, "wants_response": wants_response}


def remote_claims(read_remote):
    if not read_remote:
        return {}
    prefix = CFG["claims"]["branch_prefix"]
    git("fetch", "-q", "origin", "+refs/heads/%s*:refs/remotes/origin/%s*" % (prefix, prefix))
    out = {}
    for line in git("for-each-ref", "--format=%(refname:short) %(committerdate:unix) %(authorname)",
                    "refs/remotes/origin/" + prefix).splitlines():
        ref, ts, who = line.split(" ", 2)
        out[ref.split(prefix, 1)[1]] = {"ts": int(ts), "who": who}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weekly-used", type=float)
    ap.add_argument("--five-hour-used", type=float)
    ap.add_argument("--no-remote", action="store_true")
    ap.add_argument("--show", type=int, default=12)
    a = ap.parse_args()
    now = datetime.datetime.now(datetime.timezone.utc).timestamp()
    ttl = CFG["claims"]["ttl_hours"] * 3600

    # 1. gate
    g = CFG["gate"]
    if a.weekly_used is None or a.five_hour_used is None:
        gate, headroom = "NOT EVALUATED (no usage figures passed; a real run must pass them)", None
    elif a.weekly_used >= g["max_weekly_pct"] or a.five_hour_used >= g["max_five_hour_pct"]:
        gate, headroom = "CLOSED -- weekly %s%% / 5-hour %s%% against ceilings %s%% / %s%%. A real run exits here." % (
            a.weekly_used, a.five_hour_used, g["max_weekly_pct"], g["max_five_hour_pct"]), 0
    else:
        headroom = min(g["max_weekly_pct"] - a.weekly_used, g["max_five_hour_pct"] - a.five_hour_used)
        gate = "OPEN -- %.0f points of headroom" % headroom

    # 2-4. survey, claims, filter
    claims = remote_claims(not a.no_remote)
    subs = [survey(d) for d in targets()]
    tally = {"total": len(subs), "has_text": 0, "encoded": 0, "claimed": 0,
             "blocked_licence": 0, "needs_source": {}}
    cands = []
    U = CFG["units"]
    for s in subs:
        lic, fetch = s["policy"]["licence"], s["policy"]["fetch"]
        c = claims.get(s["rel"])
        claimed = c and (now - c["ts"]) < ttl
        if claimed:
            tally["claimed"] += 1
        if s["texts"]:
            tally["has_text"] += 1
        if s["l4"]:
            tally["encoded"] += 1
        branch = CFG["claims"]["branch_prefix"] + s["rel"]
        if s["wants_response"] and not claimed:
            cands.append(("respond_to_review", s, "respond to the human review", U["respond_to_review"], branch))
            continue
        if lic not in ("open", "permission"):
            tally["blocked_licence"] += 1
            continue
        if not s["texts"]:
            why = fetch
            tally["needs_source"][why] = tally["needs_source"].get(why, 0) + 1
            if fetch == "ready" and not claimed:
                cands.append(("fetch_source", s, "fetch the source text", U["fetch_source"], branch))
            continue
        if s["l4"] and s["plan"] is None:
            continue          # encoded before plans existed: treated as through AI pass #1
        done = {p["part"] for p in (s["plan"] or {}).get("parts", []) if p.get("status") == "done"}
        text = open(s["texts"][0], encoding="utf-8", errors="replace").read()
        parts = [p for p in parts_of(text) if p["part"] not in done]
        if not parts or claimed:
            continue
        # a unit is the next Part, plus following Parts while it is still small
        unit = [parts[0]]
        while (len(unit) < len(parts) and sum(u["chars"] for u in unit) < U["encode_part_min_chars"]
               and sum(u["chars"] for u in unit) + parts[len(unit)]["chars"] <= U["encode_part_max_chars"]):
            unit.append(parts[len(unit)])
        chars = sum(u["chars"] for u in unit)
        size = min(chars, U["encode_part_max_chars"])
        nums = [u["part"].split(":")[1] for u in unit]
        label = "encode Part%s %s (%s), %dk chars%s" % (
            "s" if len(unit) > 1 else "", " to ".join([nums[0], nums[-1]] if len(nums) > 1 else nums),
            unit[0]["title"] + (" ..." if len(unit) > 1 else ""), chars // 1000,
            "" if s["plan"] else "; first unit also writes the encoding plan (%d Parts)" % len(parts))
        cands.append(("encode_part", s, label, size * U["encode_per_1000_chars"] // 1000, branch))

    order = {k: i for i, k in enumerate(CFG["priority"])}
    cands.sort(key=lambda c: order.get(c[0], 99))
    fits = [c for c in cands if headroom is None or headroom >= 10 or c[3] <= 20000]

    # report
    print("CANON WORKER -- DRY RUN (nothing claimed, fetched or pushed)\n")
    print("1. Gate:   %s" % gate)
    print("2. Claims: %s" % (("%d live claim branch(es) on origin" % sum(1 for c in claims.values() if now - c["ts"] < ttl))
                             if not a.no_remote else "not read (--no-remote)"))
    print("3. Survey: %d target subjects -- %d have source text, %d already encoded, %d blocked by licence, %d claimed"
          % (tally["total"], tally["has_text"], tally["encoded"], tally["blocked_licence"], tally["claimed"]))
    if tally["needs_source"]:
        print("           needing source text, by why it is not fetched yet:")
        for k, v in sorted(tally["needs_source"].items(), key=lambda kv: -kv[1]):
            print("             %-40s %d" % (k, v))
    print("\n4. Candidate work, in priority order (top %d of %d):" % (min(a.show, len(fits)), len(fits)))
    for i, (kind, s, label, cost, branch) in enumerate(fits[:a.show], 1):
        print("   %2d. %-17s %-58s ~%dk tokens" % (i, kind, s["rel"][:58], cost // 1000))
        print("       %s" % label)
    if fits:
        kind, s, label, cost, branch = fits[0]
        print("\n5. WOULD CLAIM:  %s\n                 unit: %s" % (branch, label))
        print("                 (a real run pushes an empty claim commit to that branch with "
              "--force-with-lease=refs/heads/%s: so it fails if anyone else holds it)" % branch)
    else:
        print("\n5. WOULD CLAIM:  nothing -- no unblocked, unclaimed work fits. A real run exits.")


if __name__ == "__main__":
    main()
