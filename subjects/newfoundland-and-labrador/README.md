# newfoundland-and-labrador/

Newfoundland and Labrador (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the House of Assembly of Newfoundland and Labrador - Statutes and Subordinate Legislation (consolidations prepared by the Office of the Legislative Counsel, Department of Justice); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fully accessible. Fetched over plain HTTPS with an honestly identified client (User-Agent 'canon-legislation-indexer/1.0 (michael.fairweather@gmail.com)'), requests spaced about 1.8s apart; roughly 20 requests in total (the directory index of /Legislation/sr/statutes/, ten statute pages, the statutes Important Information page, the update-notice page and the House of Assembly Copyright and Privacy Statement). No 403s, no rate limiting, no bot challenge. Directory listing is enabled at /Legislation/sr/statutes/, which yielded the exact file/citation codes (for example l02.htm = RSNL1990 cL-2), so nothing had to be guessed. Statute pages are Word-generated HTML in which the title, chapter citation, the 'This is an official version.' banner and the 'Amended:' chain all appear in the header. CanLII was not used: it refuses this network.

## Topics with no legislation here

- **Passenger compensation**: No provincial passenger-compensation statute. Air, rail and marine passenger rights are federal: Canada Transportation Act, SC 1996 c 10, with the Air Passenger Protection Regulations, SOR/2019-150, made under it. The province's Motor Carrier Act, RSNL1990 cM-19 - verified as an official version at https://www.assembly.nl.ca/legislation/sr/statutes/m19.htm, amended to 2001 c19, long title 'An Act to Provide for the Regulation of Motor Vehicles Used in the Transportation of Persons for Compensation' - licenses intra-provincial passenger carriers but creates no compensation entitlement for passengers.
- **Customs/duties**: Federal matter: Customs Act, RSC 1985 c 1 (2nd Supp), and Customs Tariff, SC 1997 c 36. Provinces have no customs power (Constitution Act, 1867, s 91(2) and (3)).
- **Work permits/immigration**: Federal matter: Immigration and Refugee Protection Act, SC 2001 c 27, and its regulations. Work permits are issued federally; the provincial nominee and priority-skills streams operate administratively under a federal-provincial agreement, not under a provincial statute.
