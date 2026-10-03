#!/usr/bin/env python3
"""Build a current index of in-force principal Acts for each jurisdiction canon covers.

Writes one manifest per jurisdiction to tools/indexes/<jurisdiction>.json, as a list of
records with a stable shape:

    {"id": ..., "title": ..., "year": ..., "number": ..., "url": ..., "source_id": ...}

The manifest is the input to scaffold-subjects.py, which lays out one subject directory per
Act. Nothing here fetches the text of an Act; that is the per-jurisdiction harvest, which has
its own terms to respect (see fetch-sso-corpus.py for Singapore's 03:00-07:00 SGT window).

Scope, the same everywhere: principal Acts currently in force. Repealed Acts, pure amending
Acts, Bills and subordinate legislation are excluded, so the manifest describes the statute
book as a reader would meet it today.

Each fetcher uses the jurisdiction's own published interface and nothing else:

    au-cth   Federal Register of Legislation OData API        api.prod.legislation.gov.au
    au-qld   OQPC browse data source                          legislation.qld.gov.au/projectdata
    au-tas   EnAct browse data source                         legislation.tas.gov.au/projectdata
    nz       NZ Legislation search listing                    legislation.govt.nz/items
    uk       legislation.gov.uk Atom data feeds               legislation.gov.uk/ukpga/data.feed
    au-vic   Victorian Legislation in-force listing           legislation.vic.gov.au
    au-sa    SA Legislation browse listing                    legislation.sa.gov.au

NSW is deliberately absent. Its data source sits behind a bot challenge for scripted clients,
and this tool does not route around bot protection. The NSW index is built from the public
"Public Acts in force" table, read in a browser; see tools/indexes/README.md.

Usage:
    python tools/build-act-index.py au-cth au-qld au-tas
    python tools/build-act-index.py --all
"""
import argparse, datetime, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "indexes")
UA = "Mozilla/5.0 (compatible; canon-index-builder/1.0; +https://github.com/legalese/canon)"
DELAY = 1.0


def get(url, params=None, accept=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA, **({"Accept": accept} if accept else {})})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                body = r.read()
            time.sleep(DELAY)
            return body
        except urllib.error.HTTPError as e:
            # 403 and 429 from these sites are rate-limiting, not refusal: the same request
            # succeeds after a pause. Back off hard rather than retrying quickly.
            if attempt == 5:
                raise
            time.sleep((30 if e.code in (403, 429) else 5) * (attempt + 1))
        except Exception:  # noqa: BLE001 -- network flakiness, retried with backoff
            if attempt == 5:
                raise
            time.sleep(5 * (attempt + 1))


def now16():
    return datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")


def v(field):
    """Unwrap the {"__type__": ..., "__value__": ...} envelope the EnAct platform uses."""
    if isinstance(field, dict):
        return field.get("__value__")
    return field


# ------------------------------------------------------------------ Commonwealth
def au_cth():
    # The API throws a server-side exception when isPrincipal appears in $filter (checked
    # 2026-09-22), so principal status is filtered here rather than in the query.
    base = "https://api.prod.legislation.gov.au/v1/titles"
    flt = "collection eq 'Act' and isInForce eq true"
    rows, skip, page = [], 0, 500
    while True:
        # $orderby is required: without a stable sort the API pages non-deterministically, and
        # $skip paging then returns overlapping pages and silently drops records.
        data = json.loads(get(base, {"$filter": flt, "$top": page, "$skip": skip, "$count": "true",
                                     "$orderby": "id"}))
        batch = data.get("value", [])
        for t in batch:
            if not t.get("isPrincipal"):
                continue
            rows.append({"id": t["id"], "title": t["name"].strip(), "year": t.get("year"),
                         "number": t.get("number"), "source_id": t["id"],
                         "url": "https://www.legislation.gov.au/%s/latest/text" % t["id"]})
        skip += len(batch)
        total = data.get("@odata.count", 0)
        print("  au-cth %d / %d" % (skip, total), flush=True)
        if not batch or skip >= total:
            break
    return rows


# ------------------------------------------------------------------ EnAct platform
def enact(host, ds, sort_field, expression, view_prefix):
    rows, start, page = [], 1, 200
    while True:
        data = json.loads(get(host + "/projectdata", {
            "ds": ds, "start": start, "count": page, "sortField": sort_field,
            "sortDirection": "asc", "expression": expression, "subset": "browse", "collection": ""}))
        batch = data.get("data", [])
        for r in batch:
            aid = v(r.get("id"))
            rows.append({"id": aid, "title": (v(r.get("title")) or "").strip(),
                         "year": v(r.get("year")), "number": v(r.get("no")), "source_id": aid,
                         "url": "%s/view/html/inforce/current/%s" % (view_prefix, aid)})
        total = int(data.get("totalResults") or data.get("total") or data.get("count") or 0)
        start += len(batch)
        print("  %s %d%s" % (ds, start - 1, (" / %d" % total) if total else ""), flush=True)
        if not batch or (total and start > total) or len(batch) < page:
            break
    return rows


def au_qld():
    h = "https://www.legislation.qld.gov.au"
    return enact(h, "OQPC-BrowseDataSource", "sort.title",
                 'PrintType="act.reprint" AND PitValid=@pointInTime("%s") AND Repealed="N"' % now16(), h)


def au_tas():
    h = "https://www.legislation.tas.gov.au"
    return enact(h, "EnAct-BrowseDataSource", "new.sort.title",
                 'PrintType="act.reprint" AND Repealed<>Y AND Amending<>"pure" '
                 'AND PitValid=@pointInTime("%s")' % now16(), h)


# ------------------------------------------------------------------ United Kingdom
def _uk_feed(path):
    """Every entry in a legislation.gov.uk Atom feed, following its pagination."""
    out, page = [], 1
    while True:
        x = get("https://www.legislation.gov.uk/%s/data.feed" % path,
                {"results-count": 500, "page": page}).decode("utf-8", "replace")
        entries = re.findall(r"<entry>(.*?)</entry>", x, re.S)
        for e in entries:
            m = re.search(r"<id>https?://www\.legislation\.gov\.uk/id/([a-z]+)/([^<]+)</id>", e)
            t = re.search(r"<title>([^<]+)</title>", e)
            if m and t:
                out.append((m.group(1), m.group(2), t.group(1).strip()))
        more = re.search(r"<leg:morePages>(\d+)</leg:morePages>", x)
        if not entries or not more or int(more.group(1)) == 0:
            break
        page += 1
    return out


def uk():
    """Westminster Public General Acts in force.

    ukpga from 1801, apgb (Parliament of Great Britain, 1707-1800) and aep (the English
    Parliament, before 1707). legislation.gov.uk marks a wholly repealed Act by suffixing its
    title with "(repealed)", and those are dropped. Local and personal Acts, and the devolved
    legislatures, are out of scope.
    """
    this_year = datetime.date.today().year
    raw = []
    for y in range(1801, this_year + 1):
        got = _uk_feed("ukpga/%d" % y)
        raw += got
        print("  ukpga %d: %d" % (y, len(got)), flush=True)
    for series in ("apgb", "aep"):
        got = _uk_feed(series)
        raw += got
        print("  %s: %d" % (series, len(got)), flush=True)
    rows = []
    for series, rest, title in raw:
        if re.search(r"\(repealed\)\s*$", title, re.I):
            continue
        parts = rest.split("/")
        rows.append({"id": "%s/%s" % (series, rest), "title": title,
                     "year": parts[0] if parts else None,
                     "number": parts[-1] if len(parts) > 1 else None,
                     "source_id": "%s/%s" % (series, rest),
                     "url": "https://www.legislation.gov.uk/%s/%s" % (series, rest)})
    return rows


# ------------------------------------------------------------------ Victoria
def au_vic():
    """The public search proxy the Victorian Legislation site itself queries.

    The act_in_force content type also carries repealed Acts (their url moves to
    /repealed-revoked/ and field_act_sr_status flips to true), so both are checked. The
    site's own "Acts in force" listing reported 826 on 2026-09-22.
    """
    url = ("https://www.legislation.vic.gov.au/api/tide/elasticsearch/"
           "content-legislation-vic-gov-au__production__sapi_node/_search")
    body = json.dumps({"size": 5000, "track_total_hits": True,
                       "query": {"bool": {"filter": [{"term": {"type": "act_in_force"}}]}},
                       "_source": ["title", "field_act_sr_year", "field_act_sr_number", "url",
                                   "field_act_sr_status"],
                       "sort": [{"title_az": "asc"}]}).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"User-Agent": UA, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read())
    rows = []
    for h in data["hits"]["hits"]:
        s = h["_source"]
        path = (s.get("url") or [""])[0]
        if "/in-force/acts/" not in path or (s.get("field_act_sr_status") or [False])[0]:
            continue
        slug = path.rsplit("/", 1)[-1]
        rows.append({"id": slug, "title": (s.get("title") or [""])[0].strip(),
                     "year": (s.get("field_act_sr_year") or [None])[0],
                     "number": (s.get("field_act_sr_number") or [None])[0], "source_id": slug,
                     "url": "https://www.legislation.vic.gov.au/in-force/acts/" + slug})
    print("  au-vic %d hits, %d in force" % (len(data["hits"]["hits"]), len(rows)), flush=True)
    return rows


# ------------------------------------------------------------------ South Australia
def au_sa():
    """The Current Titles list the SA Attorney-General's Department publishes as a PDF.

    The newest PDF is discovered from the current-titles page, converted with pdftotext
    (ships with Git for Windows), and parsed: each entry is a title, possibly wrapped over
    two lines, with "Version: d.m.yyyy" on its first line.
    """
    import shutil, subprocess, tempfile
    page = get("https://www.legislation.sa.gov.au/lists-and-index-to-sa-legislation/current-titles"
               ).decode("utf-8", "replace")
    pdfs = re.findall(r'href="([^"]*?(\d{4}\.\d{2}\.\d{2})-Current-Titles\.pdf)"', page)
    if not pdfs:
        raise RuntimeError("no Current Titles PDF linked from the SA current-titles page")
    href, stamp = max(pdfs, key=lambda t: t[1])
    exe = shutil.which("pdftotext") or r"C:\Program Files\Git\mingw64\bin\pdftotext.exe"
    with tempfile.TemporaryDirectory() as d:
        pdf, txt = os.path.join(d, "t.pdf"), os.path.join(d, "t.txt")
        with open(pdf, "wb") as f:
            f.write(get(href))
        subprocess.run([exe, "-layout", pdf, txt], check=True)
        lines = open(txt, encoding="utf-8", errors="replace").read().splitlines()
    # The list continues past the Acts into "South Australian Subordinate Legislation";
    # everything from that header on is regulations and rules, and is out of scope.
    for i, ln in enumerate(lines):
        if ln.strip().startswith("South Australian Subordinate Legislation"):
            lines = lines[:i]
            break
    entries, cur = [], None
    for ln in lines:
        if "Version:" in ln:
            if cur:
                entries.append(cur)
            title, ver = ln.split("Version:", 1)
            cur = {"title": title.strip(), "version": ver.strip()}
        elif ln.strip() and cur and not re.match(r"^\s*(\d{1,2}/\d{2}/\d{4}|South Australian Acts|\d+)\s*$", ln):
            cur["title"] += " " + ln.strip()
        elif not ln.strip() and cur:
            entries.append(cur); cur = None
    if cur:
        entries.append(cur)
    rows = []
    for e in entries:
        t = re.sub(r"\s+", " ", e["title"]).strip()
        # A wrapped line can carry a second version stamp such as "27.2.2025-uncommenced".
        # It describes an uncommenced version of the Act, not the Act, so it is moved out of
        # the title and kept on the record.
        m2 = re.search(r"\s+(\d{1,2}\.\d{1,2}\.\d{4}-uncommenced)$", t)
        if m2:
            t = t[:m2.start()].strip()
            e["version"] = e["version"] + "; " + m2.group(1)
        if not t:
            continue
        m = re.search(r"\b(\d{4})$", t)
        slug = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
        rows.append({"id": slug, "title": t, "year": m.group(1) if m else None, "number": None,
                     "source_id": slug, "version": e["version"],
                     "url": "https://www.legislation.sa.gov.au/legislation/acts"})
    print("  au-sa: %d titles from the %s Current Titles list" % (len(rows), stamp), flush=True)
    return rows


FETCHERS = {"au-cth": au_cth, "au-qld": au_qld, "au-tas": au_tas, "uk": uk, "au-vic": au_vic,
            "au-sa": au_sa}


def write(jur, rows):
    os.makedirs(OUT, exist_ok=True)
    seen, out = set(), []
    for r in rows:
        if r["id"] in seen:
            continue
        seen.add(r["id"]); out.append(r)
    out.sort(key=lambda r: r["title"].lower())
    doc = {"jurisdiction": jur, "retrieved": datetime.date.today().isoformat(),
           "scope": "principal Acts in force", "count": len(out), "acts": out}
    p = os.path.join(OUT, jur + ".json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=1, ensure_ascii=False)
    print("%s: %d Acts -> %s" % (jur, len(out), os.path.relpath(p, os.path.dirname(HERE))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jurisdictions", nargs="*")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    todo = list(FETCHERS) if a.all else a.jurisdictions
    for j in todo:
        if j not in FETCHERS:
            sys.exit("unknown jurisdiction %r; have %s" % (j, ", ".join(FETCHERS)))
        print("== " + j, flush=True)
        write(j, FETCHERS[j]())


if __name__ == "__main__":
    main()
