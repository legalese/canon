# iowa/

Iowa (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Iowa Legislature - Iowa Code (Legislative Services Agency); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Clean, scriptable HTML over HTTPS, no blocking of any kind: no CAPTCHA, no bot challenge, no 403 and no rate limiting. Fetched with an honest user agent (canon-index-builder/1.0, identifying an indexing client and a contact address). The chapter section-listing pages used for verification have the form https://www.legis.iowa.gov/law/iowaCode/sections?codeChapter=<chapter>&year=2026 and each one prints the Code year, the Title, the Chapter heading and every section number and catchline. Currency: the Iowa Code landing page shows 'Iowa Code - 2026, effective 1/1/2026 - 12/31/2026' as the current edition (a dropdown offers editions back to 2004), and every chapter page fetched carried the banner 'Iowa Code - 2026'. About 14 requests in total, issued sequentially and spaced 2 seconds apart.

## Topics with no legislation here

- **Passenger compensation**: Federal, and preempted. Air passenger rights come from US DOT rules (14 CFR Parts 250, 259, 260) and the Airline Deregulation Act (49 U.S.C. 41713) preempts state regulation of airline prices, routes and services. Iowa has no passenger-compensation statute.
- **Customs/duties**: Federal, and constitutionally exclusive. U.S. Const. art. I, sec. 10, cl. 2 bars a state from laying imposts or duties on imports or exports; customs law is 19 U.S.C., administered by CBP.
- **Work permits/immigration**: Federal. Work authorisation and immigration status are governed by the Immigration and Nationality Act, 8 U.S.C., and 8 C.F.R. Iowa's only related provisions are eligibility screens for state benefits (for example 239B.2B 'Eligibility of noncitizens.', seen in the ch. 239B listing), not any grant of work authorisation.
