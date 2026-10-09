# Encoding brief: the Sale of Food Act 1973 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Sale of Food Act 1973**: Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online. This is the informal consolidation of the version in force from 1 May 2026.

The Act does the following:
- Part 1 defines food, food business, unsafe and unsuitable food, "sell", and non-retail food business.
- Part 2 sets up administration and enforcement: entry, seizure, information and samples.
- Part 2A covers food safety directions, compensation and appeals.
- Part 3 creates the selling offences.
- Part 4 requires non-retail food businesses to be licensed.
- Part 5 sets out presumptions, including adulteration and liability.
- Part 6 covers legal proceedings and defences.
- Part 7 covers prohibited food contact articles, obstruction, licences, appeals, penalties and composition.

The Act has no Schedule.

The source is `../source/SFA1973.txt`, a copy of the text deposited in this repository by the bulk ingestion; `../source/PROVENANCE.md` gives its origin. It is SSO's unofficial consolidation (SSO Terms of Use cl.8).

## The top-level goal, and the goals under it

Top level: *for this article and what this person did with it, does the Act reach it, is an offence committed, does a defence answer it, and what is the most it can cost?*

1. **What the Act reaches** (ss 2A-2F, 25): food, unsafe, unsuitable, adulterated, food business, non-retail food business, sale.
2. **Offences and penalties** (Parts 3, 4, 7; ss 5-10, 10K, 33(5), 46(6), 48-50, 56(1)(r)).
3. **Defences and who else is liable** (ss 16A(6)-(7), 26, 27, 31-33, 40(4)-(5)).
4. **Enforcement and procedure**: seizure, directions, compensation, licences, appeals, summons and notice periods.

The following are inputs: the Director-General's and the Minister's discretions; prescribed standards and substances; regulations; the court's findings (knowledge, prejudice, insanitary conditions).

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`sfa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
