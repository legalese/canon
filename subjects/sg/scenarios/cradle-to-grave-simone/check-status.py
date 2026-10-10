#!/usr/bin/env python3
"""Compare the status claims in facts.json with the encoding rows that actually exist.

A subject "has a row" when some directory under subjects/sg/<slug>/encodings/ (or that
directory itself, for the older flat layout) holds an encoding.json or a .l4 file. An
empty row directory does not count.

For every Act an event touches:
  ENC or PART claimed, no row       -> reported (the row has gone, or never existed)
  NONE claimed, row exists          -> reported (a row has landed; promote to ENC or PART
                                       after reading its scope)
  slug not under subjects/sg/       -> reported
REGS, POLICY and CASE entries carry no subject check beyond the slug existing.

Run from anywhere:  python subjects/sg/scenarios/cradle-to-grave-simone/check-status.py
Exit code 1 if anything is reported.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SG = os.path.abspath(os.path.join(HERE, "..", ".."))
FACTS = os.path.join(HERE, "facts.json")


def has_row(slug):
    enc = os.path.join(SG, slug, "encodings")
    if not os.path.isdir(enc):
        return False
    for root, _dirs, files in os.walk(enc):
        if "encoding.json" in files or any(f.endswith(".l4") for f in files):
            return True
    return False


def row_scope(slug):
    enc = os.path.join(SG, slug, "encodings")
    out = []
    for root, _dirs, files in os.walk(enc):
        if "encoding.json" in files:
            try:
                d = json.load(open(os.path.join(root, "encoding.json"), encoding="utf-8"))
                out.append((os.path.relpath(root, enc) or ".", (d.get("scope") or "")[:160]))
            except Exception as e:  # noqa: BLE001
                out.append((os.path.relpath(root, enc) or ".", f"unreadable encoding.json: {e}"))
    return out


def main():
    facts = json.load(open(FACTS, encoding="utf-8"))
    problems = []
    touched = {}
    for ev in facts["events"]:
        for law in ev["law"]:
            slug, status = law["subject"], law["status"]
            if slug is None:
                continue
            touched.setdefault(slug, set()).add(status)
            if not os.path.isdir(os.path.join(SG, slug)):
                problems.append((ev["id"], slug, status, "no such subject directory"))
                continue
            row = has_row(slug)
            if status in ("ENC", "PART") and not row:
                problems.append((ev["id"], slug, status, "claims a row; none found"))
            if status == "NONE" and row:
                problems.append((ev["id"], slug, status, "claims no row; a row exists"))

    print(f"{len(facts['events'])} events, {len(touched)} subjects touched")
    if not problems:
        print("statuses agree with the tree")
        return 0
    print(f"{len(problems)} status claims disagree with the tree:")
    seen = set()
    for eid, slug, status, why in problems:
        print(f"  {eid:5} {status:5} {slug}: {why}")
        if why.startswith("claims no row") and slug not in seen:
            seen.add(slug)
            for row, scope in row_scope(slug):
                print(f"        row {row}: {scope}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
