#!/usr/bin/env python3
"""What should a human review next?

Works out each subject's pipeline stage from the repository itself, so there is no status
column to keep up to date by hand, and lists the subjects waiting on a person, oldest first.

Stages, and what makes each one count as done:

  Indexed         subject.json exists
  AI pass #1      the subject has L4 modules (corpus_modules, or *.l4 files in the directory)
  Human pass #1   reviews/human-1.md exists; its first line says "Verdict: approve" or
                  "Verdict: changes requested"
  AI pass #2      reviews/ai-2.md exists (the AI's response to the human review)
  Human pass #2   gates/HG1.payload.sig exists (HG1 signed, see gates/README.md)

A subject is WAITING ON A HUMAN when its latest completed stage is an AI pass. The queue
orders those by how long they have waited: the date of the last commit that touched the stage
the human is due to review. Uncommitted work is shown but flagged, since nobody else can see it.

Usage:
    python tools/review-queue.py            # the queue
    python tools/review-queue.py --all      # every subject past Indexed, with its stage
"""
import argparse, datetime, glob, json, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGES = ["Indexed", "AI pass #1", "Human pass #1", "AI pass #2", "Human pass #2"]


def git(*args):
    r = subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True)
    return r.stdout.strip()


def last_commit_date(paths):
    out = git("log", "-1", "--format=%cs", "--", *paths) if paths else ""
    return out or None


def stage_of(d):
    s = json.load(open(os.path.join(d, "subject.json"), encoding="utf-8"))
    l4 = sorted(glob.glob(os.path.join(d, "*.l4")) + glob.glob(os.path.join(d, "**", "*.l4"), recursive=True))
    l4 = sorted(set(l4))
    done = {"Indexed": True,
            "AI pass #1": bool(s.get("corpus_modules")) or bool(l4),
            "Human pass #1": os.path.exists(os.path.join(d, "reviews", "human-1.md")),
            "AI pass #2": os.path.exists(os.path.join(d, "reviews", "ai-2.md")),
            "Human pass #2": os.path.exists(os.path.join(d, "gates", "HG1.payload.sig"))}
    latest = max(i for i, st in enumerate(STAGES) if done[st])
    rel = os.path.relpath(d, ROOT).replace(os.sep, "/")
    if latest == 0:                       # never encoded: skip the git calls, which are slow
        return {"subject": rel, "stage": STAGES[0]}
    tracked = bool(git("ls-files", "--", rel + "/subject.json"))
    dirty = bool(git("status", "--porcelain", "--", rel))
    asserts = 0
    for f in l4:
        asserts += sum(1 for ln in open(f, encoding="utf-8", errors="replace") if ln.startswith("#ASSERT"))
    since_paths = {1: l4, 3: [os.path.join(d, "reviews", "ai-2.md")]}.get(latest, [])
    waited_from = last_commit_date([os.path.relpath(p, ROOT) for p in since_paths]) if tracked else None
    reg = os.path.join(d, "registers", "incident-register.xlsx")
    return {"subject": rel.replace("subjects/", ""), "name": s.get("display_name") or s.get("id"),
            "stage": STAGES[latest], "done": done, "modules": len(l4), "asserts": asserts,
            "status": s.get("status"), "version": s.get("encoding_version"),
            "hg1_prepared": os.path.exists(os.path.join(d, "gates", "HG1.payload.txt")),
            "incidents": os.path.exists(reg), "tracked": tracked, "uncommitted": dirty or not tracked,
            "waiting_since": waited_from}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    rows = []
    for sj in glob.glob(os.path.join(ROOT, "subjects", "**", "subject.json"), recursive=True):
        d = os.path.dirname(sj)
        try:
            r = stage_of(d)
        except Exception as e:  # noqa: BLE001 -- a malformed subject is reported, not fatal
            print("skipped %s: %s" % (d, e)); continue
        if r["stage"] != "Indexed":
            rows.append(r)
    today = datetime.date.today()
    waiting = [r for r in rows if r["stage"] in ("AI pass #1", "AI pass #2")]
    waiting.sort(key=lambda r: (r["waiting_since"] or "9999", r["subject"]))
    print("WAITING ON A HUMAN -- oldest first\n")
    for i, r in enumerate(waiting, 1):
        nxt = STAGES[STAGES.index(r["stage"]) + 1]
        days = (today - datetime.date.fromisoformat(r["waiting_since"])).days if r["waiting_since"] else None
        flags = []
        if r["uncommitted"]: flags.append("UNCOMMITTED -- only on this machine")
        if r["hg1_prepared"]: flags.append("HG1 payload prepared")
        if r["incidents"]: flags.append("has incident register")
        print("%2d. %-52s next: %s" % (i, r["subject"], nxt))
        print("    %s -- %s, v%s, %d modules, %d assertions" % (r["name"], r["status"], r["version"],
                                                                r["modules"], r["asserts"]))
        print("    waiting since %s%s%s" % (r["waiting_since"] or "(not committed)",
                                         " (%d days)" % days if days is not None else "",
                                         ("  |  " + "; ".join(flags)) if flags else ""))
    if a.all:
        print("\nALL SUBJECTS PAST INDEXED\n")
        for r in sorted(rows, key=lambda r: r["subject"]):
            print("  %-58s %s" % (r["subject"], r["stage"]))


if __name__ == "__main__":
    main()
