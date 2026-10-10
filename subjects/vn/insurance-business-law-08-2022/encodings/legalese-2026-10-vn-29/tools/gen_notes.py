#!/usr/bin/env python3
"""Write NOTES.md, encoding.json and SOURCE-LICENSE.md.

NOTES.md comes from templates/NOTES.md.in. The template carries the prose. These placeholders are filled by this script from the
tools' own output and from the data files, so no number in NOTES.md is typed by hand:

  @@COVERAGE@@   the coverage table, from the three roadmaps, the raw sources (headings) and templates/coverage.tsv (glosses)
  @@ROADMAP@@    the lines `tools/roadmap.py status registers/roadmap-*.json` prints
  @@CHECK@@      the table `check.sh` prints
  @@VNSRC@@      the last line `tools/vnsrc.py check ...` prints
  @@SRCREFS@@    the output of `tools/srcrefs.py check --strict ...` and `--refs ...`, and what the modules contain (NOTES.md 7.1)
  @@FORKS@@, @@FINDINGS@@   the fork register and the findings, from tools/notes_data.py

  python3 -I tools/gen_notes.py
"""
import glob, hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEP = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import notes_data  # noqa: E402

RAW = os.path.normpath(os.path.join(DEP, "..", "..", "source", "raw"))
ROADMAPS = [
    ("registers/roadmap-law08-2022-qh15.json", "law08-2022-qh15.txt", "Law 08/2022/QH15, Điều 1 to 130 (Công báo 575 + 576)"),
    ("registers/roadmap-law08-2022-qh15-577-578.json", "law08-2022-qh15-577-578.txt", "Law 08/2022/QH15, Điều 131 to 157 (Công báo 577 + 578)"),
    ("registers/roadmap-law139-2025-qh15.json", None, "Law 139/2025/QH15, the 25 numbered clauses (Công báo 39)"),
]
CONT = {"tại", "của", "và", "về", "trong", "hoặc", "cho", "theo", "với", "các", "đối", "có", "để", "do"}
L4SHA = "db2c66fda1d2e30a5182fd3d60add141bd0e40cf09b14f6eb68772ce947797d7"


def raw_lines(name):
    return open(os.path.join(RAW, name), encoding="utf-8").read().split("\n")


def heading(lines, n):
    first = lines[n - 1]
    text = re.sub(r"^\s*(?:\d+\s+)?Điều\s+\d+\.\s*", "", first).strip()
    k = n
    while k < len(lines):
        nxt = lines[k].strip()
        k += 1
        if not nxt:
            break
        if "CÔNG BÁO" in nxt:
            continue
        if re.match(r"^\d+\.\s", nxt) or re.match(r"^[a-zđ]\)\s", nxt):
            break
        prev_last = text.split()[-1].lower().rstrip(",") if text.split() else ""
        if nxt[0].islower() or prev_last in CONT:
            text += " " + nxt
        else:
            break
    return re.sub(r"\s+", " ", text).strip()


def load_tsv():
    d = {}
    for ln in open(os.path.join(DEP, "templates", "coverage.tsv"), encoding="utf-8"):
        ln = ln.rstrip("\n")
        if ln:
            parts = ln.split("\t")
            d[parts[0]] = (parts[1], parts[2] if len(parts) > 2 else "")
    return d


def run(cmd):
    return subprocess.run(cmd, cwd=DEP, capture_output=True, text=True).stdout


def forks_md():
    out = []
    for fid, short, where, readings, taken, licence in notes_data.FORKS:
        out.append(f"- **{fid}**. {short}\n  - Where: {where}\n  - Readings: {readings}\n  - Taken: {taken}\n  - Licence: {licence}")
    return "\n".join(out)


def findings_md():
    out = []
    for fid, short, lines, scenario, evidence in notes_data.FINDINGS:
        out.append(f"- **{fid}**. {short}\n  - Source lines: {lines}\n  - Minimal scenario: {scenario}\n  - Evidence: {evidence}")
    return "\n".join(out)


def srcrefs_md():
    """The generated part of NOTES.md 7.1: the gate's own output, the counts, and the quote runs that take no @ref."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("srcrefs", os.path.join(HERE, "srcrefs.py"))
    sr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sr)
    raw = os.path.join("..", "..", "source", "raw", "law08-2022-qh15.txt")
    mods = sorted(os.path.basename(p) for p in glob.glob(os.path.join(DEP, "*.l4")))
    res = []
    problems = []
    for flag in ("--strict", "--refs"):
        out = run([sys.executable, "-I", "tools/srcrefs.py", "check", flag, raw] + mods).strip().split("\n")
        problems += out[:-1]
        res += [f"    $ python3 -I tools/srcrefs.py check {flag} {raw} *.l4", "    " + out[-1], ""]
    refs, runs, exempt = 0, 0, {}
    for m in mods:
        lines = open(os.path.join(DEP, m), encoding="utf-8").read().split("\n")
        refs += sum(1 for ln in lines if ln.startswith("@ref "))
        scan = sr.Scan(lines)
        runs += len(scan.runs)
        for _, block, _ in scan.runs:
            if scan.exempt(block):
                end = scan.ends[block]
                kind = "end of file" if end is None else "`" + end.split()[0] + "`"
                exempt.setdefault(m, {})
                exempt[m][kind] = exempt[m].get(kind, 0) + 1
    res += [f"- `@ref` lines in the modules: {refs} (the gate counts their locators above).",
            f"- Quote runs: {runs}, of which {sum(sum(v.values()) for v in exempt.values())} are followed by a heading, a directive or the end of a file, so take no `@ref`."]
    if exempt:
        res += ["", "| Module | Runs that take no `@ref` | What follows the run |", "| --- | --- | --- |"]
        for mod in sorted(exempt):
            res.append(f"| `{mod}` | {sum(exempt[mod].values())} | " + ", ".join(k if len(exempt[mod]) == 1 else f"{k} x {n}" for k, n in sorted(exempt[mod].items())) + " |")
    res += ["", "Problems: " + ("none." if not problems else "")]
    res += ["- `" + x + "`" for x in problems]
    return "\n".join(res)


def main():
    tsv = load_tsv()
    sections, missing = [], []
    for rpath, rawname, title in ROADMAPS:
        r = json.load(open(os.path.join(DEP, rpath), encoding="utf-8"))
        lines = raw_lines(rawname) if rawname else None
        out = [f"### {title}", "", "| Unit | Heading as the document writes it | English gloss | Disposition | Where in the L4 | Note |", "| --- | --- | --- | --- | --- | --- |"]
        for u in r["units"]:
            uid = u["id"]
            head = u["title"]
            if lines:
                m = re.search(r"line (\d+)", u.get("note", ""))
                if m:
                    head = heading(lines, int(m.group(1)))
            gloss, note = tsv.get(uid, ("", ""))
            if not gloss:
                missing.append(uid)
            mods = [os.path.basename(x) for x in u.get("modules", [])]
            where = ", ".join(f"`{x}`" for x in mods) if mods else "—"
            if u["disposition"] in ("out-of-scope", "deferred"):
                note = (u.get("reason") or "") + " " + note
            out.append(f"| {uid} | {head.replace('|', '/')} | {gloss} | {u['disposition']} | {where} | {note.replace('|', '/')} |")
        sections.append("\n".join(out))
    if missing:
        sys.exit("no gloss for: " + ", ".join(missing))

    status = run([sys.executable, "-I", "tools/roadmap.py", "status"] + [os.path.relpath(p, DEP) for p in sorted(glob.glob(os.path.join(DEP, "registers", "roadmap-*.json")))])
    status_lines = [x for x in status.strip().split("\n")]
    status = "\n".join("    " + x for x in status_lines)
    chk = subprocess.run(["./check.sh"], cwd=DEP, capture_output=True, text=True).stdout
    chk_lines = chk.rstrip("\n").split("\n")
    total = [x for x in chk_lines if x.startswith("TOTAL")][0]
    nums = total.split(")")[1].split()
    errors, satisfied, failed, refused = (int(x) for x in nums[:4])
    nmod = int(re.search(r"\((\d+) modules\)", total).group(1))
    chk = "\n".join("    " + x for x in chk_lines)

    tpl = open(os.path.join(DEP, "templates", "NOTES.md.in"), encoding="utf-8").read()
    body = (tpl.replace("@@COVERAGE@@", "\n\n".join(sections)).replace("@@ROADMAP@@", status)
               .replace("@@CHECK@@", chk).replace("@@FORKS@@", forks_md()).replace("@@FINDINGS@@", findings_md())
               .replace("@@SRCREFS@@", srcrefs_md()))

    # SOURCE-LICENSE.md first (its text is part of the vnsrc run)
    nsrc = 0
    for f in glob.glob(os.path.join(DEP, "*.l4")):
        nsrc += sum(1 for ln in open(f, encoding="utf-8") if re.match(r"^\s*-- src:", ln))
    open(os.path.join(DEP, "SOURCE-LICENSE.md"), "w", encoding="utf-8").write(
        "# SOURCE-LICENSE\n\n"
        "The terms of the sources are not established by us: see the subject-level file `../../SOURCE-LICENSE.md`, which this file does not repeat or modify.\n\n"
        f"This encoding quotes the sources one `-- src:N |` line at a time: {nsrc} such lines in its `.l4` modules (generated by `tools/expand.py` from `tools/vnsrc.py`'s quote routine and checked by `tools/vnsrc.py check`), "
        "from `law08-2022-qh15.txt`, `law08-2022-qh15-577-578.txt` and `law139-2025-qh15.txt`. The gazette PDFs are not held in this deposit.\n\n"
        "The encoding itself is Apache-2.0 (`encoding.json`).\n")

    files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(DEP, "*.l4"))) + ["GLOSSARY.md", "NOTES.md", "PROGRESS.md", "SOURCE-LICENSE.md"]
    open(os.path.join(DEP, "NOTES.md"), "w", encoding="utf-8").write(body)
    vn = run([sys.executable, "-I", "tools/vnsrc.py", "check", "../../source/raw/law08-2022-qh15.txt"] + files)
    last = vn.strip().split("\n")[-1]
    open(os.path.join(DEP, "NOTES.md"), "w", encoding="utf-8").write(body.replace("@@VNSRC@@", last))
    vn2 = run([sys.executable, "-I", "tools/vnsrc.py", "check", "../../source/raw/law08-2022-qh15.txt"] + files)
    if vn2.strip().split("\n")[-1] != last:
        print("warning: vnsrc line changed after NOTES.md was written:", vn2.strip().split("\n")[-1])

    subj = json.load(open(os.path.join(DEP, "..", "..", "subject.json"), encoding="utf-8"))
    docs = [{"id": d["id"], "url": d["url"], "sha256": d["sha256"], "retrieved": d["retrieved"], "authority": "authoritative: the Government gazette (Công báo)"} for d in subj["source"]["documents"]]
    l4mods = sorted(os.path.basename(p) for p in glob.glob(os.path.join(DEP, "*.l4")))
    enc = {
        "id": "legalese-2026-10-vn-29",
        "encoder": "legalese",
        "display_name": "Law 08/2022/QH15 on Insurance Business (Luật Kinh doanh bảo hiểm), all 157 articles as made and as amended by Law 139/2025/QH15, in three vintages",
        "status": "draft",
        "version": "0.1.0",
        "license": "Apache-2.0",
        "maintainer": {"name": "Legalese Pte. Ltd.", "github": "legalese"},
        "run": {"id": "VN-29-20261010", "agent": "enc-vn-29", "date": "2026-10-10", "method": "one agent, one session, no sub-agents, from BRIEF.md"},
        "language": {"source_text": "vi", "module_body": "en", "note": "Identifiers and comments are English (@lang en). Vietnamese appears only in `-- src:N |` comment lines generated mechanically from line N of a deposited source (tools/expand.py), and in short runs in GLOSSARY.md and NOTES.md that tools/vnsrc.py checks occur verbatim in a source."},
        "source": docs,
        "modules": l4mods,
        "scope": ("The whole Act: all 157 articles of Law 08/2022/QH15 in V1, and the effect on them of all 25 numbered clauses of Law 139/2025/QH15 in V2 and V3. "
                  "Encoded: definitions (Điều 4) as predicates over witness facts; Chương II (Điều 15-61) article by article; Chương III-VII with dated arms where Law 139/2025/QH15 changed the text; "
                  "every delegation to the Government or the Minister of Finance as a named REFUSE with a test; the deferred commencements of Điều 156(2) and the transitional dates of Điều 156-157 in each vintage. "
                  "Inert (labelled stubs): statements of policy, lists of addressees and of State functions, duties of internal organisation judged by adequacy. Not encoded: any other law (Civil Code, Maritime Code, Law on Enterprises, Law on Investment, Bankruptcy Law and others), which are inputs or refusals. See NOTES.md sections 1-2."),
        "vintages": {
            "V1": {"in_force": "2023-01-01 to 2025-12-31", "what": "Law 08/2022/QH15 as made", "source": "law08-2022-qh15.txt, law08-2022-qh15-577-578.txt"},
            "V2": {"in_force": "from 2026-01-01", "what": "V1 with Law 139/2025/QH15 Điều 1 and Điều 2 applied except Điều 2(6) and 2(8); applied by this encoder to V1", "source": "law139-2025-qh15.txt"},
            "V3": {"in_force": "from 2026-07-01", "what": "V2 with Điều 2(6) and 2(8) of Law 139/2025/QH15 also applied (Điều 3(2) of that Law); applied by this encoder", "source": "law139-2025-qh15.txt"},
        },
        "forks": {fid: short for fid, short, *_ in notes_data.FORKS},
        "findings": {fid: short for fid, short, *_ in notes_data.FINDINGS},
        "self_check": {
            "command": "./check.sh",
            "date": "2026-10-10",
            "l4": f"the build ~/.local/bin/l4 pointed to on 2026-10-10 (symlink to ~/.cabal/bin/l4, cabal store jl4-0.1-a76e8866), sha256 {L4SHA}",
            "modules": nmod,
            "errors": errors,
            "satisfied": satisfied,
            "failed": failed,
            "refused": refused,
            "vnsrc": last,
            "roadmaps": status_lines,
        },
        "not_reviewed": {
            "gate": "HG1",
            "state": "not sought",
            "note": "No domain expert has read this encoding against the source. No independent test pass has been run. Every expected value in every tests module was written by the same session that wrote the rules, worked by hand from the cited source lines before it was asserted; three expected values were corrected after a first run because the value I had written was wrong against the text (NOTES.md section 6).",
        },
    }
    json.dump(enc, open(os.path.join(DEP, "encoding.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(os.path.join(DEP, "encoding.json"), "a").write("\n")
    print("NOTES.md, SOURCE-LICENSE.md, encoding.json written;", last, "|", total)


if __name__ == "__main__":
    main()
