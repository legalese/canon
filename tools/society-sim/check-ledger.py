#!/usr/bin/env python3
"""Validate subjects/<jurisdiction>/requirements.jsonl against ledger.schema.json and print the open queue.

Checks, per line: well-formed JSON; the schema (type, required, additionalProperties, enum,
pattern, minLength, minimum, items, nested properties — the subset the schema uses, so no
dependency on a jsonschema package); unique ids; every named subject directory exists; a
superseded entry names an existing id; a satisfied entry has a resolution.

Usage:  python tools/society-sim/check-ledger.py [subjects/sg/requirements.jsonl]
Exit code 1 if any line fails.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SCHEMA = json.load(open(os.path.join(HERE, "ledger.schema.json"), encoding="utf-8"))
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

TYPES = {
    "object": dict, "array": list, "string": str, "integer": int,
    "number": (int, float), "boolean": bool, "null": type(None),
}


def check(value, schema, path, errors):
    t = schema.get("type")
    if t is not None:
        allowed = t if isinstance(t, list) else [t]
        ok = False
        for name in allowed:
            py = TYPES[name]
            if isinstance(value, py) and not (name in ("integer", "number") and isinstance(value, bool)):
                ok = True
        if not ok:
            errors.append(f"{path}: expected {allowed}, got {type(value).__name__}")
            return
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in {schema['enum']}")
    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: shorter than {schema['minLength']}")
        if schema.get("format") == "date" and not DATE.match(value):
            errors.append(f"{path}: {value!r} is not YYYY-MM-DD")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: below minimum {schema['minimum']}")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path}: missing required {req!r}")
        if schema.get("additionalProperties") is False:
            for k in value:
                if k not in props:
                    errors.append(f"{path}: unexpected field {k!r}")
        for k, v in value.items():
            if k in props:
                check(v, props[k], f"{path}.{k}", errors)
    if isinstance(value, list) and "items" in schema:
        for i, v in enumerate(value):
            check(v, schema["items"], f"{path}[{i}]", errors)


def main():
    ledger = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "subjects", "sg", "requirements.jsonl")
    jurisdiction_dir = os.path.dirname(os.path.abspath(ledger))
    entries, failures, ids = [], 0, {}
    with open(ledger, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"line {n}: not JSON: {exc}")
                failures += 1
                continue
            errors = []
            check(e, SCHEMA, "$", errors)
            eid = e.get("id")
            if eid in ids:
                errors.append(f"$.id: duplicate of line {ids[eid]}")
            ids[eid] = n
            for slug in (e.get("instrument", {}).get("subject"), e.get("instrument", {}).get("parent_subject"),
                         e.get("attach_to", {}).get("subject")):
                if slug and not os.path.isdir(os.path.join(jurisdiction_dir, slug)):
                    errors.append(f"subject directory not found: {slug}")
            if e.get("status") == "satisfied" and not e.get("resolution", {}).get("commit"):
                errors.append("satisfied without resolution.commit")
            if e.get("status") == "declined" and not e.get("resolution", {}).get("reason"):
                errors.append("declined without resolution.reason")
            if e.get("status") == "superseded" and not e.get("resolution", {}).get("merged_into"):
                errors.append("superseded without resolution.merged_into")
            if errors:
                failures += 1
                print(f"line {n} ({eid}):")
                for err in errors:
                    print(f"    {err}")
            entries.append(e)
    for e in entries:
        m = e.get("resolution", {}).get("merged_into")
        if m and m not in ids:
            print(f"{e['id']}: merged_into {m} does not exist")
            failures += 1

    print(f"{len(entries)} entries, {failures} failing")
    open_q = [e for e in entries if e.get("status") in ("open", "claimed")]
    open_q.sort(key=lambda e: (-(e.get("priority") or 0), -e.get("count", 1), e["id"]))
    if open_q:
        print(f"\nopen queue ({len(open_q)}):")
        for e in open_q:
            inst = e["instrument"]
            print(f"  {e['id']}  {e['status']:8} {e['kind']:14} x{e['count']:<3} {inst['title']}"
                  f"{' ' + inst['provision'] if inst.get('provision') else ''}  -> {e['attach_to']['how']}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
