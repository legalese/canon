#!/usr/bin/env python3
"""Harvest the current consolidated Acts of Singapore from Singapore Statutes Online.

Scales the per-subject fetcher (sg/succession's fetch-sso.py) to the whole
corpus: 524 current Acts, laid out to mirror subjects/western-australia/.

THE PDF IS THE SOURCE, NOT THE HTML. The /Act/<id> landing page returns the
table of contents plus a first fragment only; the body arrives through 115-odd
lazy /Details/GetLazyLoadContent calls, and ?WholeDoc=1 / ?ViewType=Print are
stubbed or WAF-blocked. ?ViewType=Pdf returns the whole Act, Schedules included,
in one request. The landing page is still fetched, but only for the in-force
banner and the historical-version list.

SSO SOFT-404s WITH HTTP 200. A wrong Act id returns 200 with an HTML "Page Not
Found" body, and ?ViewType=Pdf on it returns 200 with ~24KB of HTML. curl --fail
sees neither. Every fetch therefore proves it got a PDF before writing it.

THE 3-7 A.M. WINDOW IS A LICENCE CONDITION, NOT A COURTESY. SSO's Terms of Use
cl.13(d)(i) permit automated extraction "only ... during the hours of 3 a.m. to
7 a.m. (Singapore Time)", and cl.15 lets AGC deny access if that is breached.
This script refuses to run outside the window unless --i-have-permission is
passed (use that only if AGC has granted you different terms in writing).
robots.txt independently asks for crawl-delay: 6, which is what --delay defaults
to; 524 Acts x 2 requests x 6s is about 105 minutes, inside a 4-hour window.

Resumable: an Act whose .pdf and .txt already exist is skipped, so an
interrupted run continues where it stopped and a second run is nearly free.

Usage:
  ./fetch-sso-corpus.py --manifest tools/sso-acts-manifest.json
                        [--out subjects/singapore] [--delay 6] [--limit N]
                        [--i-have-permission]
Requires: curl, pdftotext (poppler).
"""
import argparse, datetime, hashlib, html, json, re, shutil, subprocess, sys, time, pathlib

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
SGT = datetime.timezone(datetime.timedelta(hours=8))
WINDOW = (3, 7)  # [03:00, 07:00) Singapore Time, per SSO Terms of Use cl.13(d)(i)

COST = {"requests": 0, "elapsed_ms": 0, "bytes": 0}


def sgt_now():
    return datetime.datetime.now(datetime.timezone.utc).astimezone(SGT)


def in_window(now=None):
    return WINDOW[0] <= (now or sgt_now()).hour < WINDOW[1]


def require_window(override):
    now = sgt_now()
    if in_window(now):
        return
    if override:
        print(f"fetch-sso-corpus: WARNING - {now:%H:%M} SGT is outside the "
              f"{WINDOW[0]:02d}:00-{WINDOW[1]:02d}:00 extraction window, "
              f"proceeding on --i-have-permission.", file=sys.stderr)
        return
    nxt = now.replace(hour=WINDOW[0], minute=0, second=0, microsecond=0)
    if now.hour >= WINDOW[0]:
        nxt += datetime.timedelta(days=1)
    sys.exit(
        f"fetch-sso-corpus: refusing to run. It is {now:%Y-%m-%d %H:%M} SGT, and SSO's\n"
        f"  Terms of Use cl.13(d)(i) permit automated extraction only between "
        f"{WINDOW[0]:02d}:00 and {WINDOW[1]:02d}:00 SGT.\n"
        f"  Next window opens {nxt:%Y-%m-%d %H:%M} SGT "
        f"(in {str(nxt - now).split('.')[0]}).")


def curl(url, referer=None):
    cmd = ["curl", "-sS", "--fail", "--max-time", "120", "-H", f"User-Agent: {UA}"]
    if referer:
        cmd += ["-H", f"Referer: {referer}"]
    t0 = time.monotonic()
    out = subprocess.run(cmd + [url], capture_output=True, check=True).stdout
    # monotonic, not wall clock: the figure is an interval and a clock step
    # mid-fetch must not turn it into a negative one.
    COST["requests"] += 1
    COST["elapsed_ms"] += int((time.monotonic() - t0) * 1000)
    COST["bytes"] += len(out)
    return out


def must_be_pdf(act, url, blob):
    """Refuse a soft-404. See the module docstring."""
    if not blob.startswith(b"%PDF-"):
        head = blob[:200].decode("utf-8", "replace").replace("\n", " ")
        raise ValueError(
            f"{url} did not return a PDF ({len(blob)}B, starts {head!r}); "
            f"most likely a wrong Act id for {act!r}")
    return blob


def detag(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = html.unescape(re.sub(r"(?s)<[^>]+>", " ", t))
    return re.sub(r"[ \t\xa0]+", " ", t)


def slug(title):
    s = title.lower().replace("’", "").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


LICENSE = """# Source license

The quoted text of **{title}** is sourced from
[Singapore Statutes Online](https://sso.agc.gov.sg/) at {url}, provided by the
Legislation Division of the Attorney-General's Chambers of Singapore ("AGC").

- **Copyright owner**: Government of Singapore.
- **License**: not an open license. Reproduction is permitted under the standing
  grant in [SSO's Terms of Use](https://sso.agc.gov.sg/Terms-of-Use) cl.13,
  subject to the conditions reproduced below. AGC may modify or revoke that
  permission at any time without notice (cl.14).
- **Retrieved**: {retrieved}, from {url}
- **Excluded from the grant**: graphics and images on SSO, which may not be
  reproduced without AGC's prior written permission (cl.6).

## Required attribution (cl.13(a))

> This Singapore legislation is subject to the copyright of the Singapore
> Government and is reproduced here with the permission of the
> Attorney-General's Chambers of Singapore. Readers may check Singapore Statutes
> Online (https://sso.agc.gov.sg/) for the latest version of this legislation.

## Other conditions of the grant

- **Accuracy is the reproducer's responsibility** (cl.13(b)): AGC does not
  warrant the accuracy of what is reproduced here.
- **No suggestion of endorsement** (cl.13(c)(i)): nothing in this repository
  conveys that AGC or SSO is associated or affiliated with, or endorses, this
  work or its producers.
{provenance}

## Status of the text (cl.8)

SSO reproduces an **unofficial** consolidation. It is not the authoritative text
of Singapore legislation, and s 48 of the Interpretation Act 1965 does not apply
to anything copied from it.
"""

# cl.13(d) governs extraction "through automated means" only, so the two
# provenances make different — and differently true — statements. Never let a
# hand-downloaded Act inherit the automated wording: the licence file would then
# assert compliance with a window condition that was never engaged.
PROVENANCE_AUTOMATED = """- **Extraction window** (cl.13(d)(i)): the automated extraction that produced
  this file was carried out between 3 a.m. and 7 a.m. Singapore Time, and was
  rate-limited to SSO's published crawl-delay."""

PROVENANCE_MANUAL = """- **Extraction window** (cl.13(d)(i)): not engaged. This file was downloaded
  by hand from SSO through an ordinary browser session, not extracted through
  automated means, so the 3 a.m. to 7 a.m. condition does not apply to it."""


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", default="subjects/singapore")
    ap.add_argument("--delay", type=float, default=6.0)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--i-have-permission", action="store_true")
    a = ap.parse_args(argv)

    if not shutil.which("pdftotext"):
        sys.exit("fetch-sso-corpus: pdftotext not found (poppler)")
    require_window(a.i_have_permission)

    acts = json.load(open(a.manifest, encoding="utf-8"))
    out_root = pathlib.Path(a.out)
    retrieved = sgt_now().strftime("%Y-%m-%d")
    done, skipped, failed = [], [], []

    for i, (act_id, title) in enumerate(list(acts.items())[:a.limit]):
        if not in_window() and not a.i_have_permission:
            print(f"\nfetch-sso-corpus: window closed at 07:00 SGT, stopping "
                  f"after {len(done)} Act(s). Re-run tomorrow to resume.")
            break
        d = out_root / slug(title)
        bundle = d / "registers" / "source-bundle"
        pdf_p, txt_p = bundle / f"{act_id}.pdf", bundle / f"{act_id}.txt"
        meta_p = bundle / f"{act_id}.meta.json"
        page = f"https://sso.agc.gov.sg/Act/{act_id}"
        before = dict(COST)

        if pdf_p.exists() and txt_p.exists():
            # An Act put here by hand has the PDF and the text but no
            # landing-page metadata, and re-downloading the PDF to get it would
            # be waste. Backfill from the landing page alone — one request — and
            # leave the hand-fetched bytes untouched. A plain skip here would
            # strand in_force/historical_versions at null for good.
            existing = {}
            if meta_p.exists():
                try:
                    existing = json.loads(meta_p.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    existing = {}
            if existing.get("in_force"):
                skipped.append(act_id)
                continue
            try:
                landing = curl(page).decode("utf-8", "replace")
            except subprocess.CalledProcessError as e:
                failed.append({"act_id": act_id, "title": title,
                               "error": f"metadata backfill: {str(e)[:250]}"})
                time.sleep(a.delay)
                continue
            fl = detag(landing)
            mm = re.search(r"Current version as at\s+(\d{1,2} \w+ \d{4})", fl)
            existing.update({
                "in_force": f"Current version as at {mm.group(1)}" if mm else None,
                "historical_versions": sorted(set(re.findall(
                    rf"/Act/{act_id}/Historical/(\d{{8}})", landing))),
                "metadata_backfilled": retrieved,
                "retrieval_cost": {k: COST[k] - before[k] for k in COST},
            })
            meta_p.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")
            done.append(act_id)
            print(f"[{i+1}/{len(acts)}] {act_id} {title}: metadata backfilled "
                  f"({len(existing['historical_versions'])} version(s)), "
                  f"existing PDF kept")
            time.sleep(a.delay)
            continue

        bundle.mkdir(parents=True, exist_ok=True)
        try:
            pdf = must_be_pdf(act_id, f"{page}?ViewType=Pdf",
                              curl(f"{page}?ViewType=Pdf", referer=page))
            pdf_p.write_bytes(pdf)
            subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout",
                            str(pdf_p), str(txt_p)], check=True)
            time.sleep(a.delay)
            landing = curl(page).decode("utf-8", "replace")
        except (subprocess.CalledProcessError, ValueError) as e:
            failed.append({"act_id": act_id, "title": title, "error": str(e)[:300]})
            print(f"  !! {act_id}: {str(e)[:120]}", file=sys.stderr)
            time.sleep(a.delay)
            continue

        flat = detag(landing)
        m = re.search(r"Current version as at\s+(\d{1,2} \w+ \d{4})", flat)
        versions = sorted(set(re.findall(rf"/Act/{act_id}/Historical/(\d{{8}})", landing)))
        text = txt_p.read_text(encoding="utf-8", errors="replace")
        meta = {
            "title": title,
            "act_id": act_id,
            "url": page,
            "pdf_url": f"{page}?ViewType=Pdf",
            "retrieved_date": retrieved,
            "in_force": f"Current version as at {m.group(1)}" if m else None,
            "historical_versions": versions,
            "sha256": hashlib.sha256(pdf).hexdigest(),
            "bytes": len(pdf),
            "text_sha256": hashlib.sha256(txt_p.read_bytes()).hexdigest(),
            "char_count": len(text),
            # Per document, so the bundle's total can be checked against the
            # sum of its parts.
            "retrieval_cost": {k: COST[k] - before[k] for k in COST},
        }
        (bundle / f"{act_id}.meta.json").write_text(
            json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        (d / "subject.json").write_text(json.dumps({
            "id": slug(title),
            "display_name": title,
            "jurisdiction": "SG",
            "citation": title,
            "act_id": act_id,
            "source": {
                "provider": "Singapore Statutes Online (AGC)",
                "source_id": act_id,
                "url": page,
                "retrieved_date": retrieved,
            },
            "corpus_modules": [],
            "projections": [],
            "encoding_version": "0.0.0",
            "status": "draft",
        }, indent=2) + "\n", encoding="utf-8")
        (d / "SOURCE-LICENSE.md").write_text(
            LICENSE.format(title=title, url=page, retrieved=retrieved,
                           provenance=PROVENANCE_AUTOMATED),
            encoding="utf-8")
        done.append(act_id)
        print(f"[{i+1}/{len(acts)}] {act_id} {title}: {len(pdf)}B pdf, "
              f"{len(text)} chars, {len(versions)} version(s)")
        time.sleep(a.delay)

    report = {
        "retrieved_from": "sso.agc.gov.sg",
        "retrieved_date": retrieved,
        "note": "PDF is the source; the HTML landing page is TOC-only for long Acts",
        "terms": "SSO Terms of Use cl.13; extraction confined to 03:00-07:00 SGT",
        "counts": {"fetched": len(done), "skipped": len(skipped),
                   "failed": len(failed), "total": len(acts)},
        "failed": failed,
        "retrieval_cost": {**COST, "tool": "tools/fetch-sso-corpus.py"},
    }
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "fetch-manifest.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"\nfetched {len(done)}, skipped {len(skipped)}, failed {len(failed)} "
          f"of {len(acts)} | {COST['requests']} requests, "
          f"{COST['elapsed_ms']/1000:.0f}s, {COST['bytes']/1e6:.1f} MB")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
