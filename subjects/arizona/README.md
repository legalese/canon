# arizona/

Arizona (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Arizona State Legislature - Arizona Revised Statutes; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Straightforward. Title indexes at https://www.azleg.gov/arsDetail/?title=<n> were fetched directly over HTTPS without a browser; six requests (titles 20, 23, 33, 38, 40, 43) plus the home page, spaced out. No block, no 403, no bot challenge, no rate limiting. Every title page carries the same currency and disclaimer statement, so the as-at position is uniform across the acts below.

## Topics with no legislation here

- **Passenger compensation**: Federal. Air passenger rights come from US DOT rules (14 C.F.R. Parts 250, 259) and state regulation of airline prices, routes and services is preempted by the Airline Deregulation Act, 49 U.S.C. s 41713. Arizona regulates motor carriers under Title 28 but has no passenger compensation scheme.
- **Customs/duties**: Federal and exclusive: U.S. Const. art. I, ss 8 and 10; Tariff Act of 1930, 19 U.S.C. States levy no customs duties.
