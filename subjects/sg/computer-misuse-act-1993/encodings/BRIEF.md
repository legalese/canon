# Encoding brief: the Computer Misuse Act 1993 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Computer Misuse Act 1993**: Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online as the "Current version as at 07 Oct 2026" (26 pages).

The Act does the following:
- It defines a computer, securing access, modification, authority and damage (s 2).
- It creates offences of computer misuse (ss 3-10). These include the national digital identity (Singpass) offences in ss 8A and 8B, and the dealing offences in ss 9 and 10.
- It enhances punishment where a protected computer is involved (s 11), and makes abetment, attempts and preparatory acts the offence itself (s 12).
- It reaches conduct outside Singapore on stated links (s 13).
- It provides for amalgamated charges, the courts, composition, compensation and arrest (ss 14-19).
- The First Schedule defines the national digital identity service and a credential. The Second Schedule lists the scam offences.

The source is `../source/CMA1993.txt`, extracted mechanically from SSO's PDF; `../source/PROVENANCE.md` says where it came from. It is SSO's unofficial consolidation (SSO Terms of Use cl.8). The PDF is not in the repository.

### Vintage

The text is as amended by Act 21 of 2025, in force on 30 December 2025. That Act added scam offences and caning, and recast s 8A(1) and s 8B(5). The source does not carry the earlier text, so **conduct before 30 December 2025 refuses**.

## The top-level goal, and the goals under it

Top level: *for this conduct involving a computer, does the Act reach it, is the alleged offence made out, and what is the most it can cost?* Under it are four goals:

1. **The definitions.** Is it a computer; did the person secure access to, or modify, a program or data; was it without authority; was there damage? (s 2; Schedules)
2. **The offences.** Are the elements of the alleged offence present, and is no exception in the section met? (ss 3-10, 12)
3. **Punishment.** What are the maximum fine, imprisonment and caning: for a first or a repeat conviction, with damage, with a protected computer? (ss 3-12)
4. **Reach and procedure.** Territorial scope, amalgamation of charges, courts, composition, compensation, investigation and arrest. (ss 13-20)

Findings of the court are inputs: knowledge, purpose, intent, reasonable steps, and whether a presumption was rebutted. So are which offences are prescribed as compoundable, and a prescribed loss threshold for "damage".

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, use `REFUSE "…"`, never `FALSE` or `0`.
- Amounts are Singapore dollars and imprisonment is in years.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables, all in this `encodings/` directory

1. `.l4` modules: `cma-types.l4` (nouns), one module per goal, `cma-goal.l4`, and tests.
2. `NOTES.md`: scope, the goals, a coverage table and a fork register.
3. `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
