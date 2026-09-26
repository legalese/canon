# hawaii/

Hawaii (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Hawaii Revised Statutes, published by the Hawaii State Legislature (Legislative Reference Bureau, Revision of Statutes Division); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

BLOCKED — the register could not be read at all. Every request to www.capitol.hawaii.gov returned HTTP 403 behind a Cloudflare interstitial reading 'Sorry, you have been blocked / You are unable to access capitol.hawaii.gov', for the HRS index, the /hrscurrent/ directory and an individual chapter page alike. The same 403 was returned to the WebFetch tool and to a full browser, so this is a network-level block on the host, not a bot challenge I could have satisfied, and I made no attempt to work around it. The Legislature's alternate host data.capitol.hawaii.gov returned HTTP 522 (origin timeout) on two attempts, as did labor80.hawaii.gov. About 10 requests in total, spaced ~1.8 s apart. The block is consistent with the state's published terms of use, which forbid automated access outright (quoted below). The Legislative Reference Bureau site (https://lrb.hawaii.gov/statute-revision/), which is reachable, describes the HRS and its supplements but hosts no statutory text. Everything below was therefore corroborated only from Hawaii state agency pages that cite their own enabling chapters — an official government source, but not the register — so no HRS entry below has a verified in-force status or as-at date. THIS JURISDICTION NEEDS RE-VERIFICATION FROM capitol.hawaii.gov ON AN UNBLOCKED NETWORK.

## Topics with no legislation here

- **Passenger compensation**: No state statute identified, and the register was blocked so this could not be checked exhaustively. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250). Interisland carriers are regulated by the PUC under HRS ch. 271G as to certification and rates, not passenger compensation.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Hawaii's HRS ch. 390 (Child Labor Law) requires a 'work permit' — a child labor certificate for working minors until age 18, per the DLIR Wage Standards Division page — but that is a different subject and confers no immigration permission.
