# minnesota/

Minnesota (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Minnesota Office of the Revisor of Statutes - Minnesota Statutes (official publisher); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched cleanly over HTTPS with an honest identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon metadata research; michael.fairweather@gmail.com)'), requests spaced ~2 seconds apart; about 20 requests in total. No robots block, no challenge, no 403/429. Working URL patterns: chapter page /statutes/cite/<chapter> (e.g. /statutes/cite/177), full chapter text /statutes/<year>/cite/<chapter>/full, section page /statutes/cite/<section>. Note: /statutes/chapter/<n>, /statutes/part/<n> and /copyright/ do not exist (404). Two transient connection failures (curl exit 28 / empty response) on /statutes/info and /statutes/cite/181.13/pdf were worked around simply by retrying the same page through a different fetcher, not by changing identity. The site carries no copyright notice and no terms-of-use page that I could find.

## Topics with no legislation here

- **Passenger compensation**: No state statute. Air passenger rights are federal (49 U.S.C. 41712 and the DOT oversales/denied-boarding rules at 14 C.F.R. pt. 250); intercity rail is Amtrak under 49 U.S.C. subtit. V pt. C. Minnesota regulates carriers (ch. 221) but does not confer passenger compensation.
- **Customs/duties**: Federal matter, not state: Tariff Act of 1930 and the Harmonized Tariff Schedule, 19 U.S.C.
- **Work permits/immigration**: Federal matter, not state: Immigration and Nationality Act, 8 U.S.C. ch. 12; employment authorisation and verification at 8 U.S.C. 1324a. Minn. Stat. ch. 181A (child labour) issues employment certificates for minors, which is a different subject.
