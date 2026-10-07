# Encoding brief: the Insurance Act 1966 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Insurance Act 1966** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online as the "Current version as at 07 Oct 2026" (233 pages). The latest amendments printed are Act 12 of 2024, Act 37 of 2024 and Act 5 of 2025.

What the Act does:
- Restricts insurance business to licensed insurers, authorised reinsurers and foreign insurers under a scheme (Part 2).
- Regulates their names, solicitation, ownership and control, funds and solvency, premiums, officers and loans (Part 2, Division 2).
- Regulates intermediaries and brokers (Part 2B).
- Provides for returns, inspections, investigations, the Authority's control of failing insurers, transfers of business and winding up (Parts 3 and 3AA).
- Covers appeals (Part 3B) and nomination of beneficiaries (Part 3C).
- Sets general offence provisions, insurable interest, capacity, and policy owners' rights in life policies (Part 4).
- Defines the insurance terms in the First Schedule, including "Singapore policy" and ordinary residence.

The source is `../source/IA1966.txt`, extracted mechanically from SSO's PDF. `../source/PROVENANCE.md` says where it came from. It also transcribes the two formulas the PDF prints as images; both are A/B × C, in s 133(5)(c) and s 150(11). The source is SSO's unofficial consolidation (SSO Terms of Use cl.8). The PDF is not in the repository.

## The top-level goals, and the goals under them

The Act speaks to two audiences, so there are two top-level goals.

**A. A regulated person.** *For this person and what it does, does the Act reach it, does it permit it, and if not, what offence is it and what is the most it can cost?*
1. Authorisation and conduct: ss 3-10 and 64-92.
2. Ownership and control: ss 26-37 and 87-89.
3. Funds and premiums: ss 16 and 22.
4. Penalties: every penalty in the Act, and ss 142-145.

**B. A policy.** *For this policy and its owner, what kind of policy is it, is it valid and for how much, what rights does the owner have, and who receives the death benefits?*
- Goal 6, the policy: the First Schedule, and ss 3, 66, 68 and 146-152.
- Goal 7, nominations and payout: ss 131-136 and 150.

**Goal 5 answers its own dated questions:** supervision, appeals, transfers and winding up (ss 11-14, 42-45, 59, 80, 94-130), including the s 123 priority of claims.

The following are inputs:
- the Authority's and the Minister's approvals, consents, opinions and discretions;
- prescribed amounts and prescribed exemptions;
- figures defined in other Acts (the Companies Act 1967's "substantial shareholder", the Income Tax Act 1947's "resident").

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, `REFUSE "…"`, never `FALSE` or `0`.
- Amounts are Singapore dollars; imprisonment is in years.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables, all in this `encodings/` directory

1. `.l4` modules: `ia-types.l4`, the goal modules, `ia-goal.l4`, and tests.
2. `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
