# maine/

Maine (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Maine Revised Statutes, Office of the Revisor of Statutes (official); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with the standard WebFetch client, requests spaced roughly 2 seconds apart; 10 requests in total (the Titles index twice, then Title 26 index, Title 26 ch.7, Title 5 index, Title 5 ch.421, Title 24-A index, Title 24-A ch.27, Title 35-A index, Title 36 index, Title 22 ch.1053-B, Title 14 ch.709 and Title 14 ch.710). All returned 200 and no block, challenge or rate limit was encountered. One caveat on URL form: the Titles index advertises links under http://legislature.maine.gov/ros/LawsOfMaine/..., and http://legislature.maine.gov/ros/LawsOfMaine/26/title26ch0sec0.html returned HTTP 404; the working canonical form is https://legislature.maine.gov/statutes/<title>/title<NN>ch<C>sec0.html, which is what is recorded here.

## Topics with no legislation here

- **Passenger compensation**: No Maine statute. Air passenger rights are federal (49 U.S.C. 41712; 14 C.F.R. Part 250 oversold flights, Part 259 tarmac delays, US Department of Transportation) and are expressly pre-empted against state regulation by 49 U.S.C. 41713; intercity rail is Amtrak under 49 U.S.C. Subtitle V Part C. Maine's Title 35-A regulates transportation utilities but creates no passenger compensation entitlement.
- **Customs/duties**: Federal matter. US states are constitutionally barred from laying imposts or duties on imports or exports (U.S. Const. art. I, s.10, cl.2); customs law is 19 U.S.C. and the Harmonized Tariff Schedule.
- **Work permits/immigration**: Federal matter. Immigration and employment authorisation are governed by the Immigration and Nationality Act (8 U.S.C. 1101 et seq.), including employment verification at 8 U.S.C. 1324a; states have no power to issue work permits.
