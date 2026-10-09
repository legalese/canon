# Encoding brief: the Housing and Development Act 1959 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Housing and Development Act 1959**: Singapore, 2020 Revised Edition, the informal consolidation printed by Singapore Statutes Online, version in force from 15 July 2026.

What the Act covers:
- Parts 2 and 3 constitute the Housing and Development Board and set out its functions, powers, entry powers, rules, composition and parking offences.
- Part 4 covers the sale of flats: eligibility, dealings, minimum occupation, security and trusts, death of an owner, management corporations, re-entry, compulsory acquisition, vesting, possession, false information and directions.
- Part 4A covers upgrading works in precincts: polls, contributions, charges and sale, and entry.
- Part 4B covers the Design-Build-and-Sell Scheme.
- Part 5 covers finance.
- Part 6 covers obstruction, identity, prosecutions and service.
- The First and Second Schedules list the lands vested in the Board on 1 May 1982.

The source is `../source/HDA1959.txt`, a copy of the text deposited in this repository; `../source/PROVENANCE.md` gives its origin. It is SSO's unofficial consolidation. In the deposited text, the two Schedules' lot tables have their columns interleaved.

## The top-level goal, and the goals under it

Top level: *for this HDB flat and its owner (or would-be owner), may the person buy it; is this dealing lawful; is the flat safe from creditors; and may the Board re-enter, compulsorily acquire it, or impose a financial penalty instead?*

1. **Buying a flat**: ss 50, 57, 92.
2. **Dealings with a sold flat**: ss 52, 55, 56, 58, 59.
3. **The Board's remedies and their periods**: ss 50(3)-(9), 59, 62-69, 74, 15, 28, 29.
4. **Upgrading works**: ss 77-84.
5. **The Board**: ss 6-11, 44, 45, 98.
6. **Offences, penalties, composition, parking liability, service and entry**: ss 13, 14, 28-33, 70, 72, 84, 107, 108, 111.

The Board's and the Minister's discretions and opinions are inputs, as are prescribed matters (minimum occupation periods, rules) and facts.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never use `FALSE` or `0`.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`hda-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
