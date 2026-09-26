# montana/

Montana (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Montana Code Annotated, published by the Legislative Services Division of the Montana Legislature; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched cleanly over HTTPS with an honest identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon metadata research)'), requests spaced ~2 seconds apart; about 16 requests. Legacy hosts leg.mt.gov and archive.legmt.gov both 301 to mca.legmt.gov, which serves static HTML. No 403, 429 or challenge was encountered, although the pages do carry an obfuscated client-side bot-detection script; every request returned HTTP 200 with full content. URL patterns used: /bills/mca/index.html (table of contents), /bills/mca/title_0XXX/chapter_0YYY/parts_index.html, /bills/mca/title_0XXX/chapter_0YYY/part_0ZZZ/sections_index.html, /bills/mca/title_.../section_.../<file>.html. No copyright or terms-of-use page exists on the MCA site (mca.legmt.gov/bills/mca/help.html has none; www.legmt.gov/terms-of-use/, www.mt.gov/copyright and mt.gov/terms-of-use all 404); only the disclaimer quoted below.

## Topics with no legislation here

- **Passenger compensation**: No state statute. Air passenger rights are federal (49 U.S.C. 41712; DOT denied-boarding rules, 14 C.F.R. pt. 250); intercity rail is Amtrak under federal law. Title 69 regulates carriers but confers no passenger compensation entitlement.
- **Customs/duties**: Federal matter, not state: Tariff Act of 1930 and the Harmonized Tariff Schedule, 19 U.S.C.
- **Work permits/immigration**: Federal matter, not state: Immigration and Nationality Act, 8 U.S.C. ch. 12; employment authorisation and verification at 8 U.S.C. 1324a.
