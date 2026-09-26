# kentucky/

Kentucky (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Kentucky Revised Statutes, Legislative Research Commission (official); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with the standard WebFetch client, requests spaced roughly 2 seconds apart; 8 requests in total (the KRS title/chapter index three times for verbatim chapter titles, footer links and the Chapter 304 subtitle list, plus chapter pages for 337, 278, 383, 61 and 304.12). All returned 200. IMPORTANT: two hosts serve this register. apps.legislature.ky.gov/law/statutes/ serves the statute text and worked every time. The SharePoint host legislature.ky.gov returned HTTP 403 Forbidden for the policy pages (https://legislature.ky.gov/policies-security/Pages/Disclaimers.aspx and https://legislature.ky.gov/Pages/disclaimer.aspx), so the formal disclaimer/terms page could not be read; I stopped rather than retrying or changing client identity. Note also that the index page's own hrefs point at the 403-ing legislature.ky.gov host, so the working apps.legislature.ky.gov URLs are recorded here instead.

## Topics with no legislation here

- **Passenger compensation**: No Kentucky statute. Air passenger rights are federal (49 U.S.C. 41712 and 14 C.F.R. Part 250, oversold flights / Part 259, tarmac delays, administered by the US Department of Transportation), and intercity rail is Amtrak under 49 U.S.C. Subtitle V Part C. Kentucky regulates intrastate motor carriers under KRS Chapter 281 but sets no passenger compensation entitlement.
- **Customs/duties**: Federal matter. US states are constitutionally barred from laying imposts or duties on imports or exports (U.S. Const. art. I, s.10, cl.2); customs law is 19 U.S.C. and the Harmonized Tariff Schedule.
- **Work permits/immigration**: Federal matter. Immigration and employment authorisation are governed by the Immigration and Nationality Act (8 U.S.C. 1101 et seq.), including employment verification at 8 U.S.C. 1324a; states have no power to issue work permits.
