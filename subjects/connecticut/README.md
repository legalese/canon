# connecticut/

Connecticut (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Connecticut General Assembly — General Statutes of Connecticut (prepared under the direction of the Legislative Commissioners' Office); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Plain HTTPS GETs with an honest UA ('canon-legislation-indexer/1.0 (legalese/canon L4 corpus; metadata only)'), about 18 requests spaced ~1.8 s apart. No block, challenge or rate limit. One caveat: the WebFetch tool failed on this host with 'unable to verify the first certificate' (the server serves an incomplete TLS chain); curl with default verification succeeded, so the chain resolves for normal clients. Titles index states 'Revised to January 1, 2025', and every chapter page carries the note that the 2026 Supplement, revised to January 1, 2026, holds updates from the 2025 sessions — so the free site is the 2025 revision plus a separately published 2026 supplement, and an as-at-2026 reading requires checking the supplement as well.

## Topics with no legislation here

- **Termination/severance**: No state statute. Connecticut is an at-will state with no severance entitlement and no mini-WARN Act; the Title 31 index carries no plant-closing notice chapter. The statutory consequences of dismissal are limited to payment of final wages (§ 31-71c, Chapter 558), continuation of group health coverage on a plant closing (§ 31-51o) and unemployment compensation (Chapter 567). Mass-layoff notice is federal: WARN Act, 29 U.S.C. § 2101 et seq.
- **Passenger compensation**: No state statute. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250). Connecticut's Title 16 chapters on motor buses (286) and taxicabs (287) are licensing and rate regulation, not passenger compensation.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Connecticut regulates only minors' employment certificates (Chapter 557, §§ 31-23 et seq.), which is a different subject.
