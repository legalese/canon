# nova-scotia/

Nova Scotia (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Nova Scotia Office of the Legislative Counsel - Consolidated Statutes (nslegislature.ca/legc/statutes), UNREACHABLE; title and citation verification fell back to the Government of Nova Scotia Office of the Registrar of Regulations (novascotia.ca/just/regulations); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

BLOCKED at the network level. Every attempt to reach nslegislature.ca - the only official source of Nova Scotia's consolidated statutes - failed with 'connect ECONNREFUSED 64.15.49.119:443'. Attempts on 2026-09-23: four fetches (https://nslegislature.ca/legislative-business/legislation, https://nslegislature.ca/legc/statutes/, https://nslegislature.ca/legc/statutes/index.htm and https://www.nslegislature.ca/sites/default/files/legc/statutes/labour%20standards%20code.pdf) plus two loads in a real browser, which both reported 'navigation to https://nslegislature.ca was denied or failed'. That is a refused connection rather than a 403 or a bot challenge, and no workaround was attempted. The separate Government of Nova Scotia domain novascotia.ca IS reachable, so the Office of the Registrar of Regulations was used to verify Act titles and chapter citations: about 12 requests, spaced about 1.8s apart, with the honest User-Agent 'canon-legislation-indexer/1.0 (michael.fairweather@gmail.com)' - the 'Regulations by Act' index plus one regulation page per target Act, each of which recites its enabling Act and citation. That site is official but it is the register of REGULATIONS, and it labels its own consolidations 'unofficial and ... for reference only', so every Act below is recorded with in_force 'unclear'. A human on a network that can reach nslegislature.ca must confirm in-force status and as-at dates, and read the Legislative Counsel site's own terms. CanLII was not used: it refuses this network.

## Topics with no legislation here

- **Passenger compensation**: No provincial passenger-compensation statute identified. Air, rail and marine passenger rights are federal: Canada Transportation Act, SC 1996 c 10, and the Air Passenger Protection Regulations, SOR/2019-150. Nova Scotia's Motor Carrier Act licenses intra-provincial passenger carriers but is not a compensation statute, and it could not be checked on the register in any event.
- **Customs/duties**: Federal matter: Customs Act, RSC 1985 c 1 (2nd Supp), and Customs Tariff, SC 1997 c 36.
- **Work permits/immigration**: Federal matter: Immigration and Refugee Protection Act, SC 2001 c 27. The Nova Scotia Nominee Program and the Atlantic Immigration Program operate under federal-provincial agreements, not under a provincial statute.
