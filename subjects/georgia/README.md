# georgia/

Georgia (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Official Code of Georgia Annotated, public access edition — published for the Georgia Code Revision Commission by LexisNexis (linked from the Georgia General Assembly site as 'Georgia Code'); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

legis.ga.gov is a JavaScript application that returns only a loading shell to scripted clients and to WebFetch, and its /laws/ path 404s, so the General Assembly home page was read in a browser; its single 'Georgia Code' link points to http://www.lexisnexis.com/hottopics/gacode, which redirects into an advance.lexis.com container. The table of contents was read in that browser: titles, chapters and article/section headings for Titles 33, 34, 44, 46, 47, 48 and 49 were expanded and recorded. Opening an individual section document then triggered a CAPTCHA ('Captcha Validation — We use CAPTCHA on this site to prevent automated software from overburdening the system'). I stopped there and did not attempt to solve or bypass it. Consequence: chapter and section headings are verified from the register's own TOC, but I could not read a 'current through' currency statement or an individual section's text, so no as-at date is recorded for Georgia.

## Topics with no legislation here

- **Termination/severance**: No state statute. Georgia is an at-will state (O.C.G.A. § 34-7-1) with no severance entitlement and no mini-WARN Act; the Title 34 table of contents shows no plant-closing or layoff-notice chapter (Chapters 11, 12, 13 and 15 are 'Reserved'). Mass-layoff notice is federal: WARN Act, 29 U.S.C. § 2101 et seq.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Georgia legislates around the edges of the federal scheme — the Georgia Security and Immigration Compliance Act requires public employers and their contractors to use E-Verify (O.C.G.A. § 13-10-91) and § 50-36-1 requires verification of lawful presence for public benefits — but no Georgia statute confers permission to work.
