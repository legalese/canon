# Encoding brief: the Apportionment Act 1928 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Apportionment Act 1928** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online, "Current version as at 05 Oct 2026".

The Act makes rents, annuities (including salaries and pensions), dividends and other periodical payments in the nature of income accrue from day to day, so that when an interest ends part-way through a period (a death, a re-entry, a sale) the part accrued so far can be apportioned (s 3). It says when the apportioned part is payable (s 4), who can recover it and how (s 5), and two exclusions: annual sums under policies of assurance (s 6) and cases where apportionment is expressly excluded (s 7). s 2 defines the payments, and deems dividends to accrue by equal daily increment over the period they are declared for.

There is one vintage. The source is `../source/AA1928.pdf` and its text, `../source/AA1928.txt`; `../source/PROVENANCE.md` says where it came from. It is SSO's unofficial consolidation (SSO Terms of Use cl.8), not the authoritative text.

No date gate: the Legislative History lists no amending Act since 1928, only revised editions.

## Scope — pinned

ss 1-7, the whole Act. A provision with nothing to compute (a short title, a power with no condition) is **inert**: carry its words and say so in the coverage table. Out of scope: any subsidiary legislation, and the other Acts this one refers to — what they decide is an input.

## Deliverables, all in this `encodings/` directory (no row subfolder)

1. `.l4` modules: one module of nouns only, the rules, and tests whose expected values come from the source.
2. `NOTES.md`: scope, a coverage table (every section and Schedule), a fork register, and anything a reviewer must know.
3. `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, `REFUSE "…"` — never `FALSE` or `0`.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.
- Day counting is not stated in the Act; record the reading taken as a fork.
- Amounts are Singapore dollars, as a NUMBER.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
