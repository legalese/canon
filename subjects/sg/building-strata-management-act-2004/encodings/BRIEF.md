# Encoding brief: the Building (Strata Management) Act 2004 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Building (Strata Management) Act 2004**: Singapore, 2020 Revised Edition, the informal consolidation printed by Singapore Statutes Online, version in force from 1 October 2026. It was enacted as the Building Maintenance and Strata Management Act and has since been renamed.

What the Act covers:
- **Part 1**: definitions and the six kinds of resolution (s 2).
- **Part 2**: the Commissioner of Buildings. Part 3 is repealed.
- **Part 4**: selling strata lots, and the schedule of strata units.
- **Part 5**: management.
  - Division 1: the developer's maintenance funds before a management corporation exists.
  - Division 2: the management corporation and the common property, covering:
    - by-laws;
    - funds;
    - contributions;
    - charges;
    - records;
    - the initial period.
  - Division 3: the council.
  - Division 4: proprietors.
  - Division 5: managing agents.
  - Division 6: insurance.
  - Division 7: subsidiary management corporations.
  - Division 8: termination.
  - Division 9: proceedings.
- **Part 6**: Strata Titles Boards and their orders. Part 7 is repealed.
- **Part 8**: general provisions, covering offences, composition, service and savings.
- **First Schedule**: general meetings.
- **Second Schedule**: council meetings.
- **Fourth Schedule**: transitional provisions. (The Third Schedule is omitted as having had effect.)

The source is `../source/BSMA2004.txt`, a copy of the text deposited in this repository; `../source/PROVENANCE.md` gives its origin. It is SSO's unofficial consolidation.

## The top-level goal, and the goals under it

Top level: *for this strata development, is this matter validly decided by the management corporation; may this person sit on its council; and what does a proprietor in arrears now face?*

1. **Resolutions and general meetings**: s 2(2)-(8), ss 26, 27, the resolution each matter needs, and the First Schedule.
2. **The owner developer**: Parts 4 and 5 Division 1, s 23, s 26(4), and ss 49-52.
3. **The management corporation**: contributions, interest, the s 40(10) offence, charges and sale (ss 40-43), funds, records and information, by-laws, the lot and the common property, and insurance.
4. **The council**: ss 53-61 and the Second Schedule.
5. **Strata Titles Boards**: Part 6.
6. **Offences, penalties, composition and service**.

Inputs: the Commissioner's, the Minister's, a Board's and a court's discretions and findings; prescribed matters; public holidays; and facts.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`bsma-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
