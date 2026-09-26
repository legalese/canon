# virginia/

Virginia (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Virginia Law Portal - Code of Virginia (Virginia General Assembly, Division of Legislative Automated Systems, for the Virginia Code Commission); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over plain HTTPS with curl and an honest self-identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon corpus; metadata only)'). About 22 requests, spaced ~2 seconds apart: the /vacode/ root, title index pages for Titles 38.2, 51.1, 56, 60.2 and 63.2, chapter pages for tit. 2.2 ch. 39, tit. 38.2 ch. 5, tit. 40.1 ch. 3, tit. 51.1 ch. 1, tit. 55.1 ch. 12, tit. 56 ch. 10, tit. 58.1 ch. 3, tit. 60.2 ch. 6 and ch. 8, tit. 63.2 ch. 6, two individual section pages (ss 40.1-33.3 and 60.2-801), the 2026 Updates page and the /developers page. All returned HTTP 200 as server-rendered HTML - no bot challenge, no 403, no rate limiting and no JavaScript shell (by contrast the separate lis.virginia.gov/privacy page IS a JS app and returned only 'You need to enable JavaScript to run this app'). Article-level URLs return 200 but with an empty content pane, so chapter pages were used as the citable register pages. The register also offers bulk PDF and CSV downloads through its Virginia Law Library and JSON/XML web services via https://law.lis.virginia.gov/developers.

## Topics with no legislation here

- **Passenger compensation**: Federal matter, and largely regulation rather than statute. Air passenger rights are pre-empted by the Airline Deregulation Act, 49 U.S.C. s 41713, and administered by the US Department of Transportation under 14 C.F.R. parts 250 and 259; rail passenger rights arise under 49 U.S.C. subtit. V. There is no state-level passenger compensation statute.
- **Customs/duties**: Federal matter. Customs duties and import procedure are exclusively federal (U.S. Const. art. I, s 8, cl. 1; Tariff Act of 1930, 19 U.S.C. ch. 4; Harmonized Tariff Schedule). No US state legislates on customs.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and 8 C.F.R. part 274a. States may not issue work permits.
