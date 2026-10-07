# Encoding brief: the Child Development Co-Savings Act 2001 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Child Development Co-Savings Act 2001** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online, "Current version as at 07 Oct 2026" (148 pages).

Part 2 sets up the Child Development Co-Savings Scheme. Under it, Government co-savings match a parent's contributions to a child's account (s 3). Part 2 also covers trustees (s 4), protection of the moneys (s 5), a member's death (s 6) and recovery of wrong payments (s 8).

Part 3 sets out leave and payments for parents:
- maternity leave and benefits (ss 9-12);
- adoption leave and benefits (ss 12A-12AD);
- childcare, extended childcare and unpaid infant care leave (ss 12B-12D);
- shared parental leave for an April 2025 Scheme child (ss 12DA-12DD, Second Schedule);
- shared parental leave for an earlier child, by the mother's election (ss 12E-12G);
- paternity leave and benefits (ss 12H-12JA);
- general rules and recovery (ss 12L-13).

Part 4 covers disputes, verification, offences, composition, regulations and exemptions. The First Schedule fixes the weekly index.

The source is `../source/CDCSA2001.txt`, extracted mechanically from SSO's PDF. `../source/PROVENANCE.md` says where it came from and transcribes the four formulas the PDF prints as images: M/2 in s 12DD(1)(b), P/W in s 12JA(2)(d), and T/W and T/3 in First Schedule items 2 and 3. The source is SSO's unofficial consolidation (SSO Terms of Use cl.8). The PDF is not in the repository.

### Dates and cohorts

The Act states its own cohorts by date:
- April 2025 Scheme child and January 2024 Scheme child (s 2);
- confinement and estimated delivery date gates in ss 9A, 12F, 12I and 12JA;
- the maximum units in the Second Schedule, para 5.

Encode each date as printed. A case outside the Act's dates answers as the Act does: not eligible.

## The top-level goal, and the goals under it

Top level: *for this parent and this child, what paid leave or Government payment does the Act give, how much may be paid, and how much may the employer claim back?* Under it:

1. The common measures: the Scheme cohorts, the eligibility date, the specified event number, age, the weekly index, and the "k times the weekly index or 6k days" durations. (s 2, First Schedule)
2. The Co-Savings Scheme. (Part 2)
3. Maternity. (ss 9, 9A, 10, 12)
4. Adoption. (ss 12A-12AD)
5. Fathers. (ss 12H-12JA)
6. Shared parental leave. (ss 12DA-12DD, 12E-12G, Second Schedule)
7. Childcare and infant care leave. (ss 12B-12D)
8. General rules, recovery, disputes and offences. (ss 12L-13, Part 4)

Pay is given as the gross pay (or lost income) per week of work days. Income for the Government-paid benefits is given as total income per day in the prescribed period. Both are inputs, because regulations prescribe the period.

Discretions, regulations and the Employment Act 1968 periods are inputs.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, use `REFUSE "…"`, never `FALSE` or `0`.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables, all in this `encodings/` directory

1. `.l4` modules: `cdcsa-types.l4`, one module per goal group, `cdcsa-goal.l4`, and tests.
2. `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
