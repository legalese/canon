# Encoding brief: Business Names Registration Act 2014, in L4

You are producing an L4 encoding of the Business Names Registration Act 2014 (Singapore) from its source.
This brief is the whole specification.

## The subject

**Business Names Registration Act 2014** (2020 Revised Edition; Act 29 of 2014, in force 3 January 2016), as shown on Singapore Statutes Online "Current version as at 30 Sep 2026".

The Act requires persons carrying on business in Singapore to register the person and the business name with the Registrar of Business Names (Part 2), sets who is exempt (s 4), governs names, changes and cancellation, and closes with inspection, offences, service of documents and transitional provisions (Part 3). It is a primary Act with no Schedules. It delegates to regulations in several places (ss 2(3)(l), 4(1)(p), 6(1)(b)(ix), 7(1), 8, 24(3), 28, 37, 40(6), 43); no regulation is among the inputs.

| vintage | source | where |
| ------- | ------ | ----- |
| Current consolidation, 30 Sep 2026 | Singapore Statutes Online PDF, "PDF created date on: 30 Sep 2026"; marginal amendments to 2025 visible in the text | `source/BNRA2014.pdf` (text: `source/BNRA2014.txt`) |

One vintage, so no vintage axis. The text is SSO's point-in-time PDF, which SSO's terms (cl.8) call an **unofficial** consolidation. The PDF was downloaded by hand from the SSO website.

## Scope: the whole Act

Every provision: ss 1 to 45. The Legislative History, Abbreviations and Comparative Table are not part of the Act and are out of scope. Definitions the Act takes from other Acts are **inputs**, not encoded.

## Deliverables, all under `encodings/`

1. `.l4` modules, English identifiers, ASCII filenames, the shared nouns in `bnra-types.l4`.
2. Test modules asserting what the SOURCE says: both sides of every threshold (30 and 14 days; 42 days; 60 days; 12 months; 1, 2 and 6 years; 3 months; $1,000, $5,000, $10,000; the lower of half the maximum fine and $5,000).
3. `NOTES.md` with the coverage table, the fork register and the answer tables.
4. `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`.

## Rules that matter

- **Isomorphic.** One source provision, one recognisable place, section numbering in `§` headings, a citation on every rule.
- **Duties with a stated deadline are regulative rules.** Powers of the Registrar, a court or the Minister are encoded as availability, never as what will be done.
- **Where the Act delegates and no regulation is an input**: an input fact where a fact can stand in (a fee paid, a particular prescribed), a named `REFUSE` where nothing can.
- **A failing assertion is a finding.** Never edit an expected value to match the code.
- **Read diagnostics, not exit codes.** `check.sh` prints errors, satisfied and failed.

## Toolchain

`l4` from `legalese/prereleases` tag `unstable-20260926-c76e6b0`. `JL4_LIBRARY_PATH` unset.
