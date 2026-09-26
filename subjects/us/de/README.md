# delaware/

Delaware (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the The Delaware Code Online (Delaware General Assembly, Division of Research); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Plain HTTPS GETs with an honest UA, about 20 requests spaced ~1.8 s apart. No block, challenge or rate limit; no robots obstruction encountered. Each title and chapter page offers an 'Authenticated PDF', which is the official electronic record under Delaware's Uniform Electronic Legal Material Act (1 Del. C. ch. 4, fetched and confirmed). The site publishes no explicit 'current through' banner; currency is shown per section by the session-law credits (e.g. '84 Del. Laws, c. 365').

## Topics with no legislation here

- **Passenger compensation**: No state statute. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250). The Title 26 railway and public-conveyance chapters (3, 5, 7) are all marked repealed on the register.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Delaware's Title 19 ch. 5 (Child Labor) covers minors' work permits, which is a different subject.
