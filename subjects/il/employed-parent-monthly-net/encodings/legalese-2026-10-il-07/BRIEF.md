# Encoding brief: the monthly net income of an employed parent in Israel, composed from six rows (IL-07)

Row IL-07, run id `IL-07-20261006`, encoder `enc-il-07` (one session, no sub-agents).
This brief restates the lead's task in the shape of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, so that a reviewer, or an independent test author, can work from it and the sources alone.

**Version 0.2.0 (2026-10-07, backlog row IL-10, encoder `enc-il-10`).** Meng ruled on 2026-10-07 to integrate row IL-08 (its Income Tax Ordinance half, ITO ss 35, 37-39, 40(b), 45A, 47, 64B, 65, and its National Insurance Law half, NII s 72, s 335, Schedule A1 Part D) into this capstone, rather than repair rows IL-01 to IL-06.
The brief below is version 0.1.0's and is kept as written; the statements 0.2.0 supersedes are marked "(0.2.0: …)". `NOTES.md` section 11 has the integration.

## The subject

This is a **composed subject**, not a statute.
It answers one question by composing six encodings already deposited in commons:

> What is the monthly net income, in a month of 2026, of an employed parent with children?

| row | instrument | provisions | directory |
| --- | --- | --- | --- |
| IL-01 | Income Tax Ordinance [New Version] | ss 33A, 34, 36, 36A (credit points) | `../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-01/` |
| IL-02 | Income Tax Ordinance [New Version] | s 66 (separate calculation for spouses) | `../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-02/` |
| IL-03 | Income Tax Ordinance [New Version] | ss 120B, 121, 121B (indexation, rates, additional tax) | `../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/` |
| IL-04 | National Insurance Law [Consolidated Version] 5755-1995 | s 1 (as needed), ss 334, 337, Schedule J (v0.2.0, repaired 2026-10-07) | `../../../national-insurance-law-consolidated-version-5755-1995/encodings/legalese-2026-10-il-04/` |
| IL-05 | National Insurance Law | Schedule K, ss 342, 348 (income bounds, the employer's deduction) | `../../../national-insurance-law-consolidated-version-5755-1995/encodings/legalese-2026-10-il-05/` |
| IL-06 | National Insurance Law | ss 65-68 (the child allowance) | `../../../national-insurance-law-consolidated-version-5755-1995/encodings/legalese-2026-10-il-06/` |
| IL-08 (0.2.0) | Income Tax Ordinance | ss 35, 37-39, 40(b), 45A, 47, 64B, 65 | `../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-08/` |
| IL-08 (0.2.0) | National Insurance Law | s 72, s 335, Schedule A1 Part D | `../../../national-insurance-law-consolidated-version-5755-1995/encodings/legalese-2026-10-il-08/` |

The two instruments' Hebrew texts are deposited in their subjects' `registers/source-bundle/`; Hebrew is authoritative and both files are unofficial consolidations.
This row cites them for checking and quotes them by copying; it encodes no provision of either itself.

## The household (pinned)

One employed parent, resident in Israel, paid the same monthly gross salary by one employer in every month of tax year 2026; possibly a spouse, who has no income; zero or more children, who are the earner's own children and, where there is a spouse, the spouse's too, unmarried, living with the parent or parents, and in Israel.
The household receives no Income Support benefit and no maintenance payment, nobody in it is absent from Israel or formerly insured, and the earner has no income other than the salary.
Where the earner has a credit or deduction under a provision no row encodes (s 35, s 45A, s 47 and the rest), that is an input and the capstone declines the tax; most real employees, who make pension contributions, are in that case.
(0.2.0: ss 35, 45A and 47 are composed from row IL-08, on further facts the caller gives: the pension contributions, the insured part of the salary, insurance premiums, an immigration. A credit no row encodes, ss 39A-40D, 44-46 and the like, is still an input that declines the tax.)

The answer for a month: the income tax for tax year 2026 and one twelfth of it, the national insurance contributions deducted from the salary, the health insurance contribution (an input), the child allowance for the month, and the net.

## Scope

- **Compose only what the six rows encode.**
  Where the household needs something no row encodes, take it as a named input or decline by name; never invent a rule.
- **The period.** 2026 is the one period all six rows answer, so the capstone answers months of 2026 and tax year 2026 and refuses every other by name.
- **The gaps** (ITO ss 35, 37-40, 45A, 65, 121A, 164; NII ss 67A, 72, 335, Schedule A1; the National Health Insurance Law) belong to backlog row IL-08; each one the capstone meets is listed in `GAPS.md` with what was done instead, in the order the capstone needs them.
  (0.2.0: row IL-08 encoded them except s 164 and the National Health Insurance Law; `GAPS.md` begins with each gap's status after the integration.)
- **Annual tax and a month.** The Ordinance computes tax for a tax year; withholding from a month's salary is s 164 and its regulations, which are not in the source bundle.
  Decide from the text, record the reading as a fork, and refuse where the text does not decide.
- **Figures.** Use no figure that cannot be cited: the rows' own sourced 2026 figures (credit point, threshold, average wage, basic amounts), cited to the row's NOTES.md, and any further official figure with URL, capture, retrieval time and sha256.

## Deliverables, all in this directory

1. `.l4` modules: a nouns module; one thin adapter per row, each importing only that row's modules; the composed pipeline; a tests module of worked households; a module of assertions expected to fail where a row disagrees with another row or with the regulator.
2. `vendor.sh`, `VENDORED.sha256`, `.gitignore`: the rows' modules copied flat beside this row's, pinned by hash, because the l4 CLI cannot import across directories.
3. `check.sh`: runs `vendor.sh --check` first, then every module of this row.
4. `NOTES.md` (coverage, forks, the answer table with hand arithmetic, what check.sh prints, open questions), `RECONCILE.md` (noun clashes and proposed row changes), `GAPS.md`, `SOURCE-LICENSE.md`, `encoding.json`, and `../../subject.json`.

## Rules that matter

- Tests take expected values from the source and the rows' sourced figures, worked by hand; never from running this code.
- A failing assertion is a finding; an expected value is never edited to make it pass.
- Read the diagnostics, not the exit code.
- The rows are read-only: a change a row should make is written in `RECONCILE.md` as a proposal.
- Semi-cleanroom with respect to the Axiom Foundation (ruled 2026-10-06): nothing of theirs is read, and no row's "Comparison with Axiom's RuleSpec" section is read.

## Toolchain

`/Users/mengwong/.local/bin/l4` (no `--version`), `JL4_LIBRARY_PATH` unset.
`L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
