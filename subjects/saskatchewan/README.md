# saskatchewan/

Saskatchewan (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Office of the King's Printer for Saskatchewan - Publications Centre (Freelaw); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with curl and python-urllib identifying themselves as 'canon-legislation-indexer/1.0 (metadata indexing)'; requests spaced about 2 seconds apart; roughly 20 requests, all HTTP 200 apart from deliberate endpoint probes that returned 404. No block, no rate limit, no bot challenge. The Publications Centre is a single-page application, so '#/freelaw' and '#/products/NNNNN' return only a 1.2 KB JavaScript shell to a scripted client; the register's own public JSON API was used instead. /api/v1/categories/1505/products returned the full list of 509 consolidated Acts (category 1505, 'Acts (Consolidated Statutes)') and /api/v1/products/{id} returned each Act's record, carrying the official name and chapter, the enacting chapter and effective date, the whole amendment chain and a 'Last update posted' date - so verification needed no statute text. There is no separate terms page on the Publications Centre itself: the copyright terms live on saskatchewan.ca/copyright. The Office of the King's Printer (renamed from Publications Saskatchewan in 2022) is the official publisher; no commercial publisher is involved. The public-facing product URLs are hash-routed, so the 'url' values below need JavaScript in a browser to render.

## Topics with no legislation here

- **Passenger compensation**: Federal matter: compensation for denied boarding, delay, cancellation and lost baggage is set by the Air Passenger Protection Regulations, SOR/2019-150, made under the Canada Transportation Act, S.C. 1996, c. 10; interprovincial rail and bus carriage is federal too. No provincial statute provides a passenger-compensation scheme.
- **Customs/duties**: Federal matter: customs and tariffs are exclusively federal under s. 91(2)-(3) of the Constitution Act, 1867 - the Customs Act, R.S.C. 1985, c. 1 (2nd Supp.) and the Customs Tariff, S.C. 1997, c. 36. No provincial statute governs it.
