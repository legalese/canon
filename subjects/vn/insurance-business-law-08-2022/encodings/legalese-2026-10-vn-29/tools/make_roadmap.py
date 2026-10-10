#!/usr/bin/env python3
"""Write the P3.0 roadmaps: one unit per article (Điều) of each Law 08/2022/QH15 gazette file, and one per numbered clause of Law 139/2025/QH15, every unit `deferred`.

Usage: python3 -I make_roadmap.py RAW_DIR OUT_DIR      (RAW_DIR is source/raw/, written by source/fetch.sh)
The unit list is the output of the regular expressions below over the pdftotext -layout rendering, so it can be re-derived;
dispositions are then moved by hand as each unit lands (this script is for the initial state only and refuses to overwrite).
"""
import json, os, re, sys

ENC = "legalese-2026-10-vn-29"
SUBJ = "insurance-business-law-08-2022"
ART = re.compile(r"^\s*Điều\s+(\d+[a-z]?)\.\s*(.*)$")
CH = re.compile(r"^\s*Chương\s+([IVXL]+)\s*$")
MUC = re.compile(r"^\s*Mục\s+(\d+)\.?\s*(.*)$")
STOP = re.compile(r"^\s*(\d+[a-z]?\.\s|[a-zđ]\)\s|Điều\s|Chương\s|Mục\s)")


def law08(path, doc, basis):
    lines = open(path, encoding="utf-8").read().split("\n")
    units, chapter, chtitle, muc = [], "", "", ""
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = CH.match(ln)
        if m:
            chapter = "Chương " + m.group(1)
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            chtitle = lines[j].strip() if j < len(lines) else ""
            muc = ""
        m = MUC.match(ln)
        if m and not ART.match(ln):
            muc = "Mục " + m.group(1)
        m = ART.match(ln)
        if m:
            title = m.group(2).strip()
            j = i + 1
            while j < len(lines) and lines[j].strip() and not STOP.match(lines[j]) and not title.endswith("."):
                title += " " + lines[j].strip()
                j += 1
                if j - i > 3:
                    break
            title = re.sub(r"\s+", " ", title).strip().rstrip(".")
            note = f"{chapter} ({chtitle}){', ' + muc if muc else ''}; {doc}.txt line {i + 1}"
            units.append({"id": "Điều " + m.group(1), "title": title,
                          "disposition": "deferred", "reason": "Not started: every unit begins deferred (runbook P3.0) and is moved when it lands.",
                          "note": note})
        i += 1
    return units


def law139(path):
    """Top-level clauses only: a numbered line that continues the article's own 1, 2, 3 ... sequence and opens with an amending verb.
    The quoted replacement text inside a clause has its own numbered paragraphs; those are not units of this Law."""
    verbs = ("Sửa đổi", "Bổ sung", "Thay thế", "Bỏ ", "Bãi bỏ", "Luật này", "Khoản")
    lines = open(path, encoding="utf-8").read().split("\n")
    units, art, last = [], None, 0
    for i, ln in enumerate(lines):
        m = re.match(r"^\s*Điều\s+(\d)\.\s", ln)
        if m and not ln.strip().startswith("“"):
            art, last = m.group(1), 0
            continue
        m = re.match(r"^\s*(\d{1,2})\.\s+(\S.*)$", ln)
        if m and art in ("1", "2", "3") and int(m.group(1)) == last + 1 and m.group(2).startswith(verbs):
            last = int(m.group(1))
            title = m.group(2).strip()
            j = i + 1
            while j < len(lines) and lines[j].strip() and not title.endswith((":", ".")) and j - i < 3:
                title += " " + lines[j].strip()
                j += 1
            units.append({"id": f"Điều {art}({last})", "title": re.sub(r"\s+", " ", title),
                          "disposition": "deferred", "reason": "Not started: every unit begins deferred (runbook P3.0) and is moved when it lands.",
                          "note": f"law139-2025-qh15.txt line {i + 1}"})
    return units


def put(out, doc, units, basis, gran):
    p = os.path.join(out, f"roadmap-{doc}.json")
    if os.path.exists(p):
        sys.exit(f"refusing to overwrite {p}")
    r = {"kind": "encoding-roadmap", "roadmap_version": "1.0.0", "subject": SUBJ, "encoding": ENC, "granularity": gran,
         "source": {"document_id": doc, "enumeration_basis": basis, "enumeration_complete": True}, "units": units}
    json.dump(r, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a").write("\n")
    print(p, len(units), "units")


if __name__ == "__main__":
    raw, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for doc in ("law08-2022-qh15", "law08-2022-qh15-577-578"):
        put(out, doc, law08(os.path.join(raw, doc + ".txt"), doc, ""),
            f"every line of source/raw/{doc}.txt that begins (after spaces) with 'Điều N.' (tools/make_roadmap.py), heading joined across wrapped lines", "section")
    put(out, "law139-2025-qh15", law139(os.path.join(raw, "law139-2025-qh15.txt")),
        "every numbered clause (N.) of articles 1, 2 and 3 of source/raw/law139-2025-qh15.txt (tools/make_roadmap.py)", "subsection")
