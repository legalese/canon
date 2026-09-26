# `source/` — the sources, and the twin check

| file | what | from |
| --- | --- | --- |
| `traffic-ordinance.wiki` | פקודת התעבורה [נוסח חדש], Wikisource wikitext, revision **3081544** (OpenLawBot, 2026-09-09) | he.wikisource.org, `action=raw&oldid=3081544` |
| `traffic-regulations.wiki` | תקנות התעבורה, Wikisource wikitext, revision **3081414** (OpenLawBot, 2026-09-09) | he.wikisource.org, `action=raw&oldid=3081414` |
| `sefer-hachukim-2265-p91-amendment-97.pdf` | ספר החוקים 2265, ב׳ בטבת התשע״א (9 December 2010), p. 91: חוק לתיקון פקודת התעבורה (מס׳ 97), התשע״א–2010 | fs.knesset.gov.il/18/law/18_lsr_301018.pdf, the link the Wikisource page itself carries for this amendment |
| `kovetz-hatakanot-6825-p114.pdf` | קובץ התקנות 6825, כ״ג בחשוון התש״ע (10 November 2009), p. 114: תקנות התעבורה (תיקון מס׳ 2) ו(תיקון מס׳ 3), התש״ע–2009 | olaw.org.il/takanot/takanot-6825.pdf, the link the Wikisource page carries |
| `revisions.json` | the two revision records as the Wikisource API returned them | |
| `SHA256SUMS` | digests of the four deposits | |
| `fetch.sh` | re-fetches the two wikitexts at the pinned revisions and the two PDFs, and re-checks the digests | |
| `twin-check.py` | holds the Hebrew row to the English one; see its docstring | |

**Wikisource is not an official source.** It is a volunteer consolidation; what makes it usable is that OpenLawBot lands every amendment with a link to the Knesset's PDF of the gazette issue, and the two gazette issues that matter here are deposited beside it and were read.

**What was read against what.** Paragraph (3A) of the definition of "שיכור" in `traffic-ordinance.wiki` was read against the Amendment 97 gazette PDF (text layer extracted with PyMuPDF; Hebrew comes out of the PDF in visual order, so it was compared phrase by phrase, not diffed): the figures (50, 10, 24, 3,500), the four classes and their lettering are the same. Reg. 169A's definition of "ריכוז אלכוהול בגוף" was read against K.T. 6825 the same way: 240 and 50, the deletion of "המידה הקבועה", and the absence of a commencement clause in Amendment No. 3.

**What was not read.** K.T. 4335 (5742, p. 830), the 1982 amendment that first inserted reg. 169A, is served by olaw.org.il as a 17-page image-only scan with no text layer; it was fetched, could not be read, and is not deposited. That is why the encoding covers no rules-effective date before 10 November 2009.

**Rate limits.** Wikimedia throttles aggressively. `fetch.sh` sends a descriptive User-Agent, fetches serially, and sleeps between requests.

**RTL in a terminal.** Never eyeball `grep` output to check a Hebrew section number; the terminal renders in visual order. Work in Python and print `repr()`, as the checks in the encoding session did.
