# vermont/

Vermont (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Vermont Statutes Online - Vermont General Assembly (Office of Legislative Counsel); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over plain HTTPS with curl and an honest self-identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon corpus; metadata only)'). About 17 requests, spaced ~2 seconds apart: the statutes index, title pages for Titles 3, 8, 9, 21, 30, 32 and 33, chapter pages for 3 V.S.A. ch. 15 and ch. 16, 8 V.S.A. ch. 129, 9 V.S.A. ch. 137, 21 V.S.A. ch. 5, 30 V.S.A. ch. 5, 32 V.S.A. ch. 151 and 33 V.S.A. ch. 11, plus the site-wide disclaimers page. All returned HTTP 200 as server-rendered HTML - no JavaScript shell, no bot challenge, no 403, no rate limiting. Title URLs are zero-padded (/statutes/title/03, /08, /09); unpadded forms return HTTP 404, which is how three first attempts failed. Subchapter-level URLs do not exist, so the citable register page for a subchapter is its chapter page, which prints the subchapter heading and its section list. IMPORTANT CURRENCY CAVEAT: the site states it is current only through the 2025 session, so 2026-session acts are not yet merged - 21 V.S.A. s 346 still shows the forward-looking marker '[Repealed effective July 1, 2026]' even though that date has passed.

## Topics with no legislation here

- **Passenger compensation**: Federal matter, and largely regulation rather than statute. Air passenger rights are pre-empted by the Airline Deregulation Act, 49 U.S.C. s 41713, and administered by the US Department of Transportation under 14 C.F.R. parts 250 and 259; rail passenger rights arise under 49 U.S.C. subtit. V. There is no state-level passenger compensation statute.
- **Customs/duties**: Federal matter. Customs duties and import procedure are exclusively federal (U.S. Const. art. I, s 8, cl. 1; Tariff Act of 1930, 19 U.S.C. ch. 4; Harmonized Tariff Schedule). No US state legislates on customs.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and 8 C.F.R. part 274a. States may not issue work permits.
