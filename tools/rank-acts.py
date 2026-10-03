#!/usr/bin/env python3
"""Rank a jurisdiction's in-force Acts by how much attention they get on the open web.

Measure: English Wikipedia pageviews for the Act's article over the last 12 complete months,
from the Wikimedia REST API. An Act with no article scores zero.

This is a proxy, and a biased one, chosen because it is public, reproducible and cheap:
  - it over-weights constitutional, historical and politically notorious Acts;
  - it under-weights workhorse Acts that practitioners use daily but nobody writes about;
  - title matching is exact after redirect resolution, so an article filed under a variant
    title ("Residential Tenancies Act 1987 (Western Australia)") is tried explicitly.
Treat the output as a shortlist to review, not a verdict.

Usage:
    python tools/rank-acts.py au-wa --top 40
Reads tools/indexes/<jurisdiction>.json (or subjects/<dir>/*/subject.json for au-wa and sg),
writes tools/rankings/<jurisdiction>.json.
"""
import argparse, datetime, glob, json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
UA = "canon-act-ranker/1.0 (https://github.com/legalese/canon)"

# Parenthetical disambiguators Wikipedia uses for sub-national or foreign Acts.
SUFFIXES = {
    "au-wa": ["(Western Australia)", "(WA)"],
    "au-sa": ["(South Australia)", "(SA)"],
    "au-nsw": ["(New South Wales)", "(NSW)"],
    "au-vic": ["(Victoria)", "(Vic)"],
    "au-qld": ["(Queensland)", "(Qld)"],
    "au-tas": ["(Tasmania)", "(Tas)"],
    "au-cth": ["(Australia)", "(Cth)"],
    "nz": ["(New Zealand)"],
    "sg": ["(Singapore)"],
    "uk": ["(United Kingdom)", "(UK)"],
}


def get_json(url, params=None):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(5 * (attempt + 1))
        except Exception:
            time.sleep(5 * (attempt + 1))
    return None


def load_titles(jur):
    p = os.path.join(HERE, "indexes", jur + ".json")
    if os.path.exists(p):
        d = json.load(open(p, encoding="utf-8"))
        return [(a["id"], a["title"]) for a in d["acts"]]
    folder = {"au-wa": "western-australia", "sg": "singapore"}.get(jur)
    if folder:
        out = []
        for f in glob.glob(os.path.join(ROOT, "subjects", folder, "*", "subject.json")):
            s = json.load(open(f, encoding="utf-8"))
            out.append((s["id"], s.get("display_name") or s.get("citation")))
        if jur == "sg":
            man = json.load(open(os.path.join(HERE, "sso-acts-manifest.json"), encoding="utf-8"))
            have = {t for _, t in out}
            out += [(k, v) for k, v in man.items() if v not in have]
        return out
    sys.exit("no index for %s" % jur)


def resolve(titles):
    """Map each candidate title to the article it resolves to, following redirects."""
    found = {}
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]
        d = get_json("https://en.wikipedia.org/w/api.php", {
            "action": "query", "titles": "|".join(batch), "redirects": 1,
            "format": "json", "formatversion": 2})
        if not d:
            continue
        q = d.get("query", {})
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        redir = {r["from"]: r["to"] for r in q.get("redirects", [])}
        pages = {p["title"]: p for p in q.get("pages", [])}
        for t in batch:
            t2 = norm.get(t, t)
            t3 = redir.get(t2, t2)
            p = pages.get(t3)
            if p and not p.get("missing") and not p.get("invalid"):
                found[t] = t3
        time.sleep(0.5)
    return found


def pageviews(article, start, end):
    a = urllib.parse.quote(article.replace(" ", "_"), safe="")
    d = get_json("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
                 "en.wikipedia/all-access/user/%s/monthly/%s/%s" % (a, start, end))
    time.sleep(0.2)
    return sum(i["views"] for i in d["items"]) if d and "items" in d else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jurisdiction")
    ap.add_argument("--top", type=int, default=40)
    a = ap.parse_args()
    jur = a.jurisdiction
    acts = load_titles(jur)
    # Candidate titles: the plain title, then each disambiguated variant.
    cands = {}
    for aid, t in acts:
        cands.setdefault(t, (aid, t))
        for s in SUFFIXES.get(jur, []):
            cands.setdefault("%s %s" % (t, s), (aid, t))
    found = resolve(list(cands))
    today = datetime.date.today().replace(day=1)
    end = (today - datetime.timedelta(days=1)).replace(day=1)
    start = end.replace(year=end.year - 1)
    s, e = start.strftime("%Y%m0100"), end.strftime("%Y%m0100")
    best = {}
    for cand, article in found.items():
        aid, title = cands[cand]
        best.setdefault(aid, {"id": aid, "title": title, "articles": set()})["articles"].add(article)
    rows = []
    for aid, r in best.items():
        views = sum(pageviews(art, s, e) for art in r["articles"])
        rows.append({"id": aid, "title": r["title"], "articles": sorted(r["articles"]), "views": views})
    rows.sort(key=lambda r: -r["views"])
    os.makedirs(os.path.join(HERE, "rankings"), exist_ok=True)
    out = {"jurisdiction": jur, "measure": "en.wikipedia pageviews, user agents",
           "window": [start.isoformat(), end.isoformat()], "acts_in_index": len(acts),
           "acts_with_article": len(rows), "ranking": rows}
    json.dump(out, open(os.path.join(HERE, "rankings", jur + ".json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("%s: %d Acts, %d with a Wikipedia article (window %s to %s)" %
          (jur, len(acts), len(rows), start, end))
    for i, r in enumerate(rows[:a.top], 1):
        print("%3d %9d  %s" % (i, r["views"], r["title"]))


if __name__ == "__main__":
    main()
