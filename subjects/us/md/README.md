# maryland/

Maryland (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Maryland General Assembly - Statute Text (Annotated Code of Maryland), official legislative site; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with the standard WebFetch client, requests spaced roughly 2 seconds apart; 12 requests in total (the Statutes landing page, the Home page for the footer, the Privacy Notice, and section pages for Labor and Employment 3-501, 3-505, 3-1301, 8.3-101 and 11-301, State Personnel and Pensions 21-101, Human Services 5-101, Tax-General 10-101, Insurance 27-303, Public Utilities 7-307 and Real Property 8-203). All returned 200; no block, challenge or rate limit. Two quirks worth recording: https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText with no query string renders 'File Not Found', and the article/section pages carry no printed as-at date, effective-date note or version label - the only currency control is the site's 'include enactments of the last session' toggle (the URLs recorded here use enactments=false, i.e. the text in force rather than the text as it will read after the last session's enactments commence).

## Topics with no legislation here

- **Passenger compensation**: No Maryland statute. Air passenger rights are federal (49 U.S.C. 41712; 14 C.F.R. Part 250 oversold flights, Part 259 tarmac delays) and state regulation of air carrier prices, routes and services is pre-empted by 49 U.S.C. 41713; intercity rail is Amtrak under 49 U.S.C. Subtitle V Part C. Maryland's MARC and MTA services set passenger rights by tariff and regulation, not by statutory compensation entitlement.
- **Customs/duties**: Federal matter. US states are constitutionally barred from laying imposts or duties on imports or exports (U.S. Const. art. I, s.10, cl.2); customs law is 19 U.S.C. and the Harmonized Tariff Schedule.
- **Work permits/immigration**: Federal matter. Immigration and employment authorisation are governed by the Immigration and Nationality Act (8 U.S.C. 1101 et seq.), including employment verification at 8 U.S.C. 1324a; states have no power to issue work permits.
