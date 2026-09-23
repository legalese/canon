# manitoba/

Manitoba (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Manitoba Laws (King's Printer for Manitoba / Legislative Counsel); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with curl and python-urllib identifying themselves as 'canon-legislation-indexer/1.0 (metadata indexing)'; requests spaced about 2 seconds apart; roughly 14 requests, all HTTP 200. No block, no rate limit, no bot challenge. The C.C.S.M. index (statutes/index_ccsm.php?lang=en, 440 KB, 843 table rows) lists every consolidated Act by chapter code, title and originating S.M./R.S.M. chapter with a 'Current version (HTML)' link; repealed Acts are held on separate indexes, so presence on this index is itself evidence of currency. Per-Act legislative-history pages (statutes/ccsm/_info1act.php?c=E110) give the consolidation date without opening statute text - all nine checked read 'updated to: September 18, 2026'. Note that https://web2.gov.mb.ca/laws/copyright.php returns 404: the copyright terms are on manitoba.ca, linked from the Manitoba Laws footer. Manitoba Laws is the official register - under Part 5 (Proof of Legislation) of The Statutes and Regulations Act the bilingual version of an Act on this site is an official copy. No commercial publisher is involved.

## Topics with no legislation here

- **Passenger compensation**: Federal matter: compensation for denied boarding, delay, cancellation and lost baggage is set by the Air Passenger Protection Regulations, SOR/2019-150, made under the Canada Transportation Act, S.C. 1996, c. 10; interprovincial rail and bus carriage is federal too. No provincial statute provides a passenger-compensation scheme.
- **Customs/duties**: Federal matter: customs and tariffs are exclusively federal under s. 91(2)-(3) of the Constitution Act, 1867 - the Customs Act, R.S.C. 1985, c. 1 (2nd Supp.) and the Customs Tariff, S.C. 1997, c. 36. No provincial statute governs it.
