# Round 4: index Israeli legislation

You are indexing legislation for the `legalese/canon` L4 corpus. **Metadata only: never copy or
quote statute text into your output.** Identify the principal Israeli statutes for the topics you
are given, and record exactly how you verified each one.

## Sources, in order of authority

1. **Reshumot / Sefer HaChukim** (רשומות, ספר החוקים) is the official publication. Knesset PDFs live
   under `https://fs.knesset.gov.il/...`. Cite the Sefer HaChukim issue and date where you can find it.
2. **The Knesset legislation database** (`main.knesset.gov.il/Activity/Legislation/Laws/`) and the
   Ministry of Justice sites are official secondary references for status and amendments.
3. **"The Open Book of Laws"** (ספר החוקים הפתוח) on Hebrew Wikisource,
   `https://he.wikisource.org/wiki/ספר_החוקים_הפתוח`, is a maintained *consolidated* text of Israeli
   legislation, kept current with amendments. It is **not official**, but it is the practical route
   to a consolidated Hebrew text, and it is the source the existing Israeli subject in this repo
   uses. Each law has a page such as `https://he.wikisource.org/wiki/חוק_הגנת_השכר`.

Israel has no free official consolidated register: the official texts are the original publication
plus every amending Act. Say so where it matters, and never present the Wikisource text as official.

## What to return per Act

- `title` — the accepted English title, e.g. "Wage Protection Law, 5718-1958". Use the English name
  the Knesset or Ministry of Justice uses where one exists.
- `title_he` — the Hebrew title exactly as the register prints it, including the Hebrew year, e.g.
  "חוק הגנת השכר, התשי\"ח-1958".
- `identifier` — the official citation you found (Sefer HaChukim issue and page, or the year), plus
  the Wikisource page name if that is the consolidated source.
- `url` — the consolidated Wikisource page (or an official page if you found a better one).
- `official_url` — the Knesset or Reshumot page or PDF, if you found one. Omit if not.
- `in_force` — `"yes"`, `"not yet in force"` or `"unclear"`, with `notes` explaining anything but yes.
- `verified_how` — what you actually saw: the page title, the Hebrew year, the last amendment noted,
  the date the consolidation claims, or the Knesset status line. Be specific.
- `topic` — one of the twelve topics you were given.
- `notes` — anything a human needs: partial commencement, a replacement Act pending, a law that is
  Mandate-era (פקודה, Ordinance) rather than a Knesset Law, or one that sits in a Code.

**Verify, do not assume.** Fetch the page for every Act and say what you saw. Do not rely on your
own memory of Israeli law, and do not rely on a search snippet.

## Choosing Acts

Two or three Acts per topic is right where Israel splits a subject across statutes (employment law
especially). Prefer the operative statute a person would actually be governed by. Include an
Ordinance (פקודה) where that is still the governing instrument, such as the Income Tax Ordinance or
the Customs Ordinance. If a topic is genuinely governed by a Code chapter or by regulation rather
than by statute, record it in `topic_gaps` with the reason.

## Access rules, which are absolute

- Identify yourself honestly; never pretend to be a browser you are not.
- If a site blocks scripted access, returns 403/429 or shows a bot challenge or CAPTCHA, stop and
  record it. Never work around a block.
- Space requests about 1.5-2 seconds apart.

## Output

Write one JSON file, `tools/topics/round4/<group>.json`, keyed by group name, in this shape:

```json
{
  "Israel": {
    "jurisdiction": "Israel",
    "register": {"name": "...", "url": "https://...",
                 "access_notes": "what you fetched, what worked, how many requests"},
    "licence": {"summary": "No copyright subsists in Israeli statutes: Copyright Act, 5768-2007, s 6 ...",
                "open_licence": true, "terms_url": "https://...", "attribution": "...",
                "quote": "a short verbatim quote of s 6 or of the site's terms"},
    "language_authenticity": "Hebrew is authoritative; English translations are unofficial.",
    "acts": [ { ...as described above... } ],
    "topic_gaps": [{"topic": "...", "reason": "..."}]
  }
}
```

Return, as your final message, a short summary only: each Act's English and Hebrew title, its topic,
its in-force verdict, and anything a human must check. Do not paste the JSON.
