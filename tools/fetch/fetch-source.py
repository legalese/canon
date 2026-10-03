#!/usr/bin/env python3
"""Deposit current statute text into indexed subjects, from registers that are openly licensed
and allow scripted access.

    python tools/fetch/fetch-source.py au-cth                 # every Cth subject still without text
    python tools/fetch/fetch-source.py uk --only communications-act-2003
    python tools/fetch/fetch-source.py au-qld au-tas --dry-run

For each subject it writes, in registers/source-bundle/:
    <id>.txt        plain text, one paragraph per line, headings as "\tPart 4 — Title" (the WA shape)
and updates <id>.meta.json with text_deposited, retrieved_date, the exact source URL, the
version fetched and the sha256 of both the original download and the text. The original
download is not kept (UK XML runs to 13 MB an Act); its URL and hash are.

Never touches a subject whose jurisdiction licence in tools/worker/config.json is not open,
and never retries past a refusal (403/429 -> back off once, then stop that jurisdiction).
"""
import argparse, datetime, glob, hashlib, html, io, json, os, re, sys, time, urllib.parse
import urllib.request, urllib.error, zipfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CFG = json.load(open(os.path.join(ROOT, "tools", "worker", "config.json"), encoding="utf-8"))
UA = "Mozilla/5.0 (compatible; canon-source-fetcher/1.0; +https://github.com/legalese/canon)"
TODAY = datetime.date.today().isoformat()
DASH = " — "


class Refused(Exception):
    pass


def get(url, tries=2):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read(), r.headers
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and i + 1 < tries:
                time.sleep(45); continue
            if e.code in (403, 429):
                raise Refused("%s %s" % (e.code, url))
            raise


def tidy(lines):
    out = []
    for l in lines:
        l = re.sub(r"[ \t\xa0]+$", "", re.sub(r"(?<=\S)[ \xa0]{2,}", " ", l))
        if l.strip():
            out.append(l)
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- Commonwealth (docx)
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_text(blob):
    doc = ET.fromstring(zipfile.ZipFile(io.BytesIO(blob)).read("word/document.xml"))
    lines = []
    for p in doc.iter(W + "p"):
        style = p.find("%spPr/%spStyle" % (W, W))
        style = style.get(W + "val") if style is not None else ""
        buf = []
        for n in p.iter():
            if n.tag == W + "t":
                buf.append(n.text or "")
            elif n.tag == W + "tab":
                buf.append("\t")
            elif n.tag in (W + "br", W + "cr"):
                buf.append(" ")
            elif n.tag == W + "noBreakHyphen":
                buf.append("-")           # "Part 1-1", "s 12-5" use a non-breaking hyphen
        t = "".join(buf).strip()
        if not t or style.lower().startswith("toc"):
            continue          # the table of contents repeats every heading with a page number
        m = re.match(r"^(Chapter|Part|Division|Subdivision|Schedule)\s+([0-9]+[A-Z]*(?:[.-][0-9]+[A-Z]*)*)\s*[—–-]\s*(.+)$", t)
        if m and style.lower().startswith(("acthead", "heading", "head")):
            t = "\t%s %s%s%s" % (m.group(1), m.group(2), DASH, m.group(3))
        lines.append(t)
    return tidy(lines)


def fetch_cth(meta):
    """The current compilation as Word. Large Acts are published in volumes numbered from 1
    (a single-volume Act is volume 0); the volumes are fetched in order and joined.

    If the law in force today has not been compiled yet (amendments have commenced but no
    compilation is registered), 'Current' has no document; fall back to the latest registered
    compilation and record that it may be behind."""
    tid = meta["source_id"]
    api = "https://api.prod.legislation.gov.au/v1/"
    try:
        return _fetch_cth(tid, "Current")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
    blob, text, url, ver = _fetch_cth(tid, "Latest")
    cur = json.loads(get(api + "Versions/Find(titleId='%s',asAtSpecification='Current')" % tid)[0])
    lat = json.loads(get(api + "Versions/Find(titleId='%s',asAtSpecification='Latest')" % tid)[0])
    ver["caveat"] = ("The version in force from %s has no registered compilation yet; this text is the "
                     "latest compilation (No. %s, in force from %s), so amendments commencing on or after "
                     "that date may be missing." % (cur.get("start", "?")[:10], lat.get("compilationNumber"),
                                                    lat.get("start", "?")[:10]))
    return blob, text, url, ver


def _fetch_cth(tid, asat):
    url = ("https://api.prod.legislation.gov.au/v1/Documents/Find(titleid='%s',asatspecification='%s',"
           "type='Primary',format='Word',uniquetypenumber=0,volumenumber={vol},rectificationspecification='Latest')" % (tid, asat))
    blobs, texts, names = [], [], []
    for vol in range(0, 20):
        try:
            blob, h = get(url.replace("{vol}", str(vol)))
        except urllib.error.HTTPError as e:
            if e.code == 404 and (vol == 0 or blobs):
                if blobs:
                    break
                continue
            raise
        fn = re.search(r"filename=([^;]+)", h.get("Content-Disposition", "") or "")
        names.append(re.sub(r"(?i)\.docx$", "", fn.group(1)) if fn else "?")
        t = docx_text(blob)
        if texts:
            # later volumes repeat the compilation front matter, then "Contents", then the
            # heading of the Chapter they continue; keep only the body
            c = t.find("\nContents\n")
            if c >= 0:
                t = t[c + len("\nContents\n"):]
            chapters = re.findall(r"^\tChapter [^\n]*$", "".join(texts), re.M)
            first = t.split("\n", 1)
            if chapters and first[0] == chapters[-1]:
                t = first[1] if len(first) > 1 else ""
        blobs.append(blob); texts.append(t)
        if vol == 0:
            break
        time.sleep(1)
    ver = {"version": names[0].split("VOL")[0] if names else None, "version_kind": "compilation register id"}
    if len(blobs) > 1:
        ver["volumes"] = names
    return b"".join(blobs), "".join(texts), url.replace("{vol}", "0" if len(blobs) == 1 else "1.." + str(len(blobs))), ver


# ---------------------------------------------------------------- UK (CLML)
L = "{http://www.legislation.gov.uk/namespaces/legislation}"
SKIP = {L + "CommentaryRef", L + "Commentaries", L + "Contents", L + "Resources"}


def clml_text(blob):
    root = ET.fromstring(blob)
    body = root.find(".//%sPrimary" % L)
    lines, pending = [], []

    def text_of(el):
        out = []
        def walk(e):
            if e.tag in SKIP:
                if e.tail: out.append(e.tail)
                return
            if e.text: out.append(e.text)
            for c in e: walk(c)
            if e.tail: out.append(e.tail)
        if el.text: out.append(el.text)
        for c in el: walk(c)
        return re.sub(r"\s+", " ", "".join(out)).strip()

    def walk(e):
        tag = e.tag.replace(L, "")
        if e.tag in SKIP:
            return
        if tag in ("Part", "Chapter", "Pblock", "PsubBlock", "Schedule") :
            num = e.find(L + "Number"); title = e.find(L + "Title")
            n = text_of(num) if num is not None else ""
            t = text_of(title) if title is not None else ""
            if tag == "Schedule" and e.find(L + "TitleBlock") is not None:
                tb = e.find(L + "TitleBlock")
                num = tb.find(L + "Number"); title = tb.find(L + "Title")
                n = text_of(num) if num is not None else n
                t = text_of(title) if title is not None else t
            if n or t:
                lines.append("\t" + (n + DASH + t if n and t else n or t))
            for c in e:
                if c.tag not in (L + "Number", L + "Title", L + "TitleBlock"):
                    walk(c)
            return
        if tag == "P1group":
            title = e.find(L + "Title")
            p1 = e.find(L + "P1")
            num = p1.find(L + "Pnumber") if p1 is not None else None
            head = text_of(title) if title is not None else ""
            lines.append((text_of(num) + "\t" if num is not None else "") + head)
            for c in e:
                if c.tag != L + "Title":
                    walk(c)
            return
        if tag == "Pnumber":
            return
        if tag in ("P1", "P2", "P3", "P4", "P5", "P6"):
            num = e.find(L + "Pnumber")
            if tag != "P1" and num is not None:
                pending.append("(%s) " % text_of(num))
            for c in e:
                if c.tag != L + "Pnumber":
                    walk(c)
            return
        if tag == "Text":
            t = text_of(e)
            if t:
                lines.append("".join(pending) + t)
                del pending[:]
            return
        for c in e:
            walk(c)

    for c in (body if body is not None else root):
        walk(c)
    return tidy(lines)


def fetch_uk(meta):
    url = "https://www.legislation.gov.uk/%s/data.xml" % meta["source_id"]
    blob, _ = get(url)
    root = ET.fromstring(blob)
    dc = "{http://purl.org/dc/terms/}"
    valid = root.find(".//%svalid" % dc)
    mod = root.find(".//%smodified" % dc)
    return blob, clml_text(blob), url, {
        "version": valid.text if valid is not None else (mod.text if mod is not None else None),
        "version_kind": "point in time (dct:valid) of the latest revised version",
        "caveat": "revised text; may carry more than one extent version of a provision, and prospective "
                  "provisions, which CLML marks but this text does not distinguish"}


# ---------------------------------------------------------------- Qld / Tas (EnAct whole HTML)
def enact_text(page):
    s = page.decode("utf-8", errors="replace")
    a = s.find('<div id="fragview">')
    if a >= 0:
        s = s[a:]
    for end in ('<div id="push">', '<div id="footer">'):
        b = s.find(end)
        if b >= 0:
            s = s[:b]; break
    # "<B>1</B><span>Short title</span>" and "(a)the ..." -> keep a gap after the number
    s = re.sub(r'(?i)(<B class="HeadingStyle">[^<]*</B>)', lambda m: m.group(1) + "\t", s)
    s = re.sub(r'(?i)(<span class="ListNumber">[^<]*</span>)', lambda m: m.group(1) + " ", s)
    s = re.sub(r"(?is)<(script|style|nav|button|header|footer)\b.*?</\1>", "", s)
    s = re.sub(r"(?is)<(blockquote|p|div)[^>]*class=\"[^\"]*history-note[^\"]*\"[^>]*>.*?</\1>", "", s)
    # "Part 1" + "Introduction" -> "\tPart 1 — Introduction"
    s = re.sub(r'(?is)<p[^>]*class="(Chapter|Part|Division|Subdivision|Schedule)HeadingParagraph"[^>]*>(.*?)</p>',
               lambda m: "\n\t" + re.sub(r"(?s)<span class=\"HeadingNumber\">(.*?)</span>\s*", r"\1" + DASH, m.group(2)) + "\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</?(p|div|blockquote|h\d|li|tr|table)\b[^>]*>", "\n", s)
    s = re.sub(r"(?i)<td\b[^>]*>", "\t", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return tidy(l for l in s.split("\n"))


def fetch_enact(host):
    def f(meta):
        url = "https://%s/view/whole/html/inforce/current/%s" % (host, meta["source_id"])
        blob, _ = get(url)
        return blob, enact_text(blob), url, {"version": TODAY,
                                             "version_kind": "current in-force version on the retrieval date"}
    return f


FETCHERS = {
    "au-cth": ("commonwealth-of-australia", fetch_cth),
    "uk":     ("united-kingdom", fetch_uk),
    "au-qld": ("queensland", fetch_enact("www.legislation.qld.gov.au")),
    "au-tas": ("tasmania", fetch_enact("www.legislation.tas.gov.au")),
}

LIC_DONE = """## Status of this deposit

Statute text deposited {today}: `registers/source-bundle/{txt}`, converted to plain text from
{url}
({vk}: {ver}). sha256 of the download: `{sha}`.
"""


def deposit(d, key, fetch, dry):
    metas = [m for m in glob.glob(os.path.join(d, "registers", "source-bundle", "*.meta.json"))]
    if len(metas) != 1:
        return "skip: %d meta files" % len(metas)
    mp = metas[0]
    meta = json.load(open(mp, encoding="utf-8"))
    if meta.get("text_deposited"):
        return "skip: already deposited"
    if not meta.get("source_id"):
        return "skip: no source_id"
    if dry:
        return "would fetch %s" % meta["source_id"]
    blob, text, url, ver = fetch(meta)
    if len(text) < 500:
        return "FAIL: only %d chars of text from %s" % (len(text), url)
    base = mp[:-len(".meta.json")]
    open(base + ".txt", "w", encoding="utf-8", newline="\n").write(text)
    meta.update({"text_deposited": True, "retrieved_date": TODAY, "text_url": url,
                 "version": ver.get("version"), "version_kind": ver.get("version_kind"),
                 "download_sha256": hashlib.sha256(blob).hexdigest(),
                 "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                 "text_chars": len(text), "converter": "tools/fetch/fetch-source.py"})
    if ver.get("caveat"):
        meta["text_caveat"] = ver["caveat"]
    if ver.get("volumes"):
        meta["volumes"] = ver["volumes"]
    json.dump(meta, open(mp, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(mp, "a", encoding="utf-8").write("\n")
    lp = os.path.join(d, "SOURCE-LICENSE.md")
    if os.path.exists(lp):
        lic = open(lp, encoding="utf-8").read()
        new = LIC_DONE.format(today=TODAY, txt=os.path.basename(base) + ".txt", url=url,
                              vk=ver.get("version_kind"), ver=ver.get("version"), sha=meta["download_sha256"])
        lic = re.sub(r"(?s)## Status of this deposit\n.*?(?=\n## |\Z)", new.rstrip("\n") + "\n", lic) \
            if "## Status of this deposit" in lic else lic.rstrip("\n") + "\n\n" + new
        open(lp, "w", encoding="utf-8", newline="\n").write(lic)
    return "ok %6dk chars  %s" % (len(text) // 1000, ver.get("version"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jurisdictions", nargs="+", choices=sorted(FETCHERS))
    ap.add_argument("--only", help="subject slug")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--pause", type=float, default=3.0, help="seconds between requests")
    a = ap.parse_args()
    for key in a.jurisdictions:
        jd, fetch = FETCHERS[key]
        lic = CFG["jurisdictions"].get(jd, {}).get("licence")
        if lic not in ("open", "permission"):
            print("%s: licence is %r -- not fetching" % (jd, lic)); continue
        subs = sorted(glob.glob(os.path.join(ROOT, "subjects", jd, "*", "subject.json")))
        print("== %s (%d subjects)" % (jd, len(subs)))
        for sj in subs:
            d = os.path.dirname(sj)
            if a.only and os.path.basename(d) != a.only:
                continue
            try:
                r = deposit(d, key, fetch, a.dry_run)
            except Refused as e:
                print("  REFUSED %s -- stopping %s" % (e, jd)); break
            except Exception as e:
                r = "FAIL: %s: %s" % (type(e).__name__, str(e)[:120])
            print("  %-64s %s" % (os.path.basename(d)[:64], r)); sys.stdout.flush()
            if not r.startswith("skip") and not a.dry_run:
                time.sleep(a.pause)


if __name__ == "__main__":
    main()
