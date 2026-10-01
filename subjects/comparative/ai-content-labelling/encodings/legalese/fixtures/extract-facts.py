#!/usr/bin/env python3
"""Read each fixture's C2PA manifest with c2patool and write down what it states.

For every files/*.jpg this writes facts/<stem>.json, whose keys are the field names of
`C2PA manifest` in labelling-domain.l4, and then generates ../fixture-manifests.l4,
which defines each fixture's manifest as an L4 value AND asserts that JSONDECODE of the
JSON file produces exactly that value. The second half is the REST/MCP path: a caller
sends JSON, and the assertion proves the JSON this script writes decodes to the record
the census uses.

Mechanical only: every value is copied from c2patool's JSON report. Nothing here
decides anything the statutes ask; see the scenario modules for those facts.

Usage: C2PATOOL=/path/to/c2patool python3 extract-facts.py
"""
import json, os, subprocess, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
C2PATOOL = os.environ.get("C2PATOOL", "c2patool")
DST = "http://cv.iptc.org/newscodes/digitalsourcetype/"
SOURCE_TYPE = {
    "digitalCapture": "digital capture",
    "trainedAlgorithmicMedia": "trained algorithmic media",
    "compositeWithTrainedAlgorithmicMedia": "composite with trained algorithmic media",
    "algorithmicallyEnhanced": "algorithmically enhanced",
}

def report(path):
    r = subprocess.run([C2PATOOL, str(path)], capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None  # c2patool prints "Error: No claim found" for a file without a manifest

def facts(rep):
    m = rep["manifests"][rep["active_manifest"]]
    sig = m.get("signature_info") or {}
    cgi = (m.get("claim_generator_info") or [{}])[0]
    gen = cgi.get("name") or (m.get("claim_generator") or "").split("/")[0]
    actions, sources, watermark, ai_disclosure = [], [], False, False
    for a in m.get("assertions", []):
        label = a.get("label", "")
        if label.startswith("c2pa.actions"):
            for act in (a.get("data") or {}).get("actions", []):
                actions.append(act.get("action", ""))
                dst = (act.get("digitalSourceType") or "").strip()
                if dst:
                    sources.append(dst)
                if act.get("action", "").startswith("c2pa.watermarked"):
                    watermark = True
        if label.startswith("c2pa.soft-binding"):
            watermark = True
        if label.startswith("c2pa.ai-disclosure"):
            ai_disclosure = True
    state = rep.get("validation_state", "")
    return {
        "its signature validates": state in ("Valid", "Trusted"),
        "its signer is on the C2PA trust list": state == "Trusted",
        "the signer it names": sig.get("issuer", ""),
        "the generator it names": gen,
        "the generator version it names": cgi.get("version", ""),
        "the time it records": sig.get("time", ""),
        "the identifier it carries": m.get("instance_id", ""),
        "the source types it declares": sources,
        "the actions it records": actions,
        "it declares a watermark": watermark,
        "it carries an AI disclosure assertion": ai_disclosure,
    }

def l4_source_type(uri):
    short = uri[len(DST):] if uri.startswith(DST) else None
    if short in SOURCE_TYPE:
        return "`%s`" % SOURCE_TYPE[short]
    return '(`another source type` "%s")' % uri

def l4_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')

def l4_list(items):
    return ("LIST " + ", ".join(items)) if items else "EMPTY"

def l4_record(f):
    b = lambda x: "TRUE" if x else "FALSE"
    return "\n".join([
        "    `C2PA manifest` WITH",
        "        `its signature validates`               IS %s" % b(f["its signature validates"]),
        "        `its signer is on the C2PA trust list`  IS %s" % b(f["its signer is on the C2PA trust list"]),
        "        `the signer it names`                   IS %s" % l4_str(f["the signer it names"]),
        "        `the generator it names`                IS %s" % l4_str(f["the generator it names"]),
        "        `the generator version it names`        IS %s" % l4_str(f["the generator version it names"]),
        "        `the time it records`                   IS %s" % l4_str(f["the time it records"]),
        "        `the identifier it carries`             IS %s" % l4_str(f["the identifier it carries"]),
        "        `the source types it declares`          IS %s" % l4_list([l4_source_type(u) for u in f["the source types it declares"]]),
        "        `the actions it records`                IS %s" % l4_list([l4_str(a) for a in f["the actions it records"]]),
        "        `it declares a watermark`               IS %s" % b(f["it declares a watermark"]),
        "        `it carries an AI disclosure assertion` IS %s" % b(f["it carries an AI disclosure assertion"]),
    ])

def json_for_l4(f):
    g = dict(f)
    g["the source types it declares"] = [
        SOURCE_TYPE[u[len(DST):]] if u.startswith(DST) and u[len(DST):] in SOURCE_TYPE else u
        for u in f["the source types it declares"]]
    return g

def main():
    files = sorted((HERE / "files").glob("*.jpg"))
    (HERE / "facts").mkdir(exist_ok=True)
    out = [
        "-- GENERATED by fixtures/extract-facts.py from c2patool's report on each file in",
        "-- fixtures/files/. Do not edit by hand; rebuild the files and rerun the script.",
        "--",
        "-- Each fixture's C2PA manifest, as c2patool reads it, and an assertion that the JSON",
        "-- in fixtures/facts/ decodes to the same value (the path a REST or MCP caller takes).",
        "",
        "IMPORT prelude",
        "IMPORT `labelling-domain`",
        "",
    ]
    for p in files:
        stem = p.stem
        rep = report(p)
        name = "`the manifest of %s`" % stem
        if rep is None:
            (HERE / "facts" / (stem + ".json")).write_text("null\n")
            out += ["-- %s: c2patool finds no manifest." % p.name,
                    "GIVETH A MAYBE `C2PA manifest`", "%s MEANS NOTHING" % name, ""]
            continue
        f = facts(rep)
        j = json_for_l4(f)
        (HERE / "facts" / (stem + ".json")).write_text(json.dumps(j, indent=2, ensure_ascii=False) + "\n")
        out += ["-- %s: validation_state %s" % (p.name, rep.get("validation_state")),
                "GIVETH A MAYBE `C2PA manifest`",
                "%s MEANS JUST (" % name, l4_record(f), "    )", ""]
        if all(u[len(DST):] in SOURCE_TYPE for u in f["the source types it declares"] if u.startswith(DST)):
            # The decode MUST sit in a definition with a GIVETH. An inline JSONDECODE whose
            # type is fixed only by the comparison returns RIGHT OF NOTHING, silently
            # (measured 2026-10-01; NOTES.md section 7).
            dec = "`the JSON facts of %s, decoded`" % stem
            out += ["GIVETH AN EITHER STRING `C2PA manifest`",
                    "%s MEANS JSONDECODE %s" % (dec, l4_str(json.dumps(j, ensure_ascii=False))),
                    "#ASSERT %s EQUALS (RIGHT (fromMaybe (REFUSE \"no manifest\") %s))" % (dec, name), ""]
    (HERE.parent / "fixture-manifests.l4").write_text("\n".join(out))
    print("wrote %d fixtures" % len(files))

if __name__ == "__main__":
    main()
