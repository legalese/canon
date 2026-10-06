# Encoding brief: the Work Injury Compensation Act 2019 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Work Injury Compensation Act 2019** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online, "Current version as at 06 Oct 2026".

The Act makes an employer (and, from 1 January 2025, a platform operator) liable to pay no-fault compensation for a personal injury by an accident arising out of and in the course of the work, and for listed occupational diseases; fixes the amounts by Schedule (death, permanent or current incapacity, temporary incapacity, medical expenses); says whom the money is paid to and when; sets out the claim process (notice, assessment, objection, review, appeal); bars double recovery with an action for damages; requires the employer or operator to insure; and creates offences.

The source is `../source/WICA2019.txt`, extracted mechanically from SSO's PDF; `../source/PROVENANCE.md` says where it came from and transcribes the three formulas the PDF prints as images. It is SSO's unofficial consolidation (SSO Terms of Use cl.8), not the authoritative text. The PDF itself is not in the repository.

### Vintages

- An accident **before 1 September 2020** is under the repealed Act (s 83(1)), which is not in the source: **refuse**.
- An accident **from 1 September 2020 to 31 December 2024** is under this Act, but in the text before the Platform Workers Act 2024 amendments (Act 30 of 2024, in force 1 January 2025), which was not supplied: **refuse**.
- From **1 January 2025** the text applies. Inside it, the First and Fifth Schedules carry two sets of floors and caps, for accidents before and on or after **1 November 2025** (S 694/2025). Both are encoded, and the accident date picks one.

## Scope — pinned

The whole Act: ss 1-83 (with ss 34A-34P, 35A, 35B, 47A-47I, 11A), and the First to Sixth Schedules. Combine provisions into **goal-level** conclusions (who is covered; is there liability; how much; who is paid; the claim process; damages; insurance; offences) rather than one function per subsection, while keeping an `@ref` on every rule.

A provision with nothing to compute — a power, a procedure, a definition the caller applies — is **inert**: carry it in the coverage table and say so. Facts a witness could give, and the outcome of a discretion (the Commissioner's, the Minister's or a court's), are inputs. Subsidiary legislation (the prescribed time limits, interest rate, minimum insurance, compulsory terms, compoundable offences, funeral cap, apportionment manner) is not in the source: where a rule needs one, take it as an input or refuse.

## Deliverables, all in this `encodings/` directory (no row subfolder)

1. `.l4` modules: `wica-types.l4` (nouns only), one module per goal group, and tests whose expected values come from the source.
2. `NOTES.md`: scope, the goals, a coverage table (every section and Schedule), a fork register, and anything a reviewer must know.
3. `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, `REFUSE "…"` — never `FALSE` or `0`.
- Employees and platform workers: where Part 3A applies a Part 2 rule "with the necessary modifications", write the rule once for both and say so.
- Day counting: "within N days after" and "before the expiry of N days after" are read as the date N days later, inclusive; "one year after" as the same date the next year. Record any other reading as a fork.
- Amounts are Singapore dollars, as a NUMBER. Ages are "the age on the next birthday ... at the time of the accident".
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
