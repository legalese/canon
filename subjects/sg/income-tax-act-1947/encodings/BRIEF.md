# Encoding brief: the Income Tax Act 1947 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Income Tax Act 1947** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online, "Current version as at 06 Oct 2026" (1,118 pages).

The Act charges income tax on income accruing in or derived from Singapore or received in Singapore from outside it (s 2A, s 10), exempts listed income (Part 4), allows deductions and capital allowances (Parts 5, 6), sets special rules for ascertaining some income (Part 7), builds statutory, assessable and chargeable income (Parts 8 to 10, with personal reliefs for resident individuals), sets the rates (Part 11, Second Schedule, and concessionary rates), provides for withholding at source and double-tax relief (Parts 12 to 14), and governs returns, assessments, objections, appeals, collection, refunds and offences (Parts 16 to 20).

The source is `../source/ITA1947.txt`, extracted mechanically from SSO's PDF; `../source/PROVENANCE.md` says where it came from and transcribes the formulas the PDF prints as images that the encoding relies on. It is SSO's unofficial consolidation (SSO Terms of Use cl.8). The PDF is not in the repository. The Multinational Enterprise (Minimum Tax) Act 2024 (DTT and MTT, s 2A(2)-(6)) is a separate Act and out of scope.

### Vintages

Most provisions are stated by **year of assessment (YA)**; the YA is the calendar year after the basis period. Many provisions were rewritten without their old text being kept. The computation of tax is stated for **YA 2024 onwards**; an earlier YA **refuses**. Where the Act itself keeps YA-specific figures (the Second Schedule tables for YA 2012-2016, 2017-2023 and 2024 on; the relief thresholds of $4,000 for YA 2024 and before and $8,000 from YA 2025; reliefs that cease from YA 2026; remissions for YA 2024 and YA 2025), encode them as printed.

## The top-level goal, and the goals under it

Top level: *how much income tax does this person owe for this year of assessment, and by when?* Under it, combine provisions into goal-level conclusions rather than one function per subsection:

1. Is the person resident, and who is chargeable? — s 2, Part 15
2. What income is charged, and from where? — Part 3 (ss 2A, 10-12)
3. Is the income exempt? — Part 4, First Schedule
4. What may be deducted, and what capital allowances are made? — Parts 5, 6, Sixth Schedule
5. What are the statutory, assessable and chargeable income? — Parts 7-10, Fifth Schedule
6. At what rate, and what rebates, remissions and credits apply? — Part 11, Second and Twelfth Schedules, ss 42A, 46, 50-50C, 92J, 92L
7. What must be withheld at source? — Part 12
8. What must be filed, when may the Comptroller assess, and how are disputes resolved? — Parts 16-18
9. When is tax due, what is added if it is late, and when is it refunded? — Part 19
10. Is an offence committed, and what is the most it can cost? — Part 20 and the offences elsewhere

Keep an `@ref` on every rule. A provision with nothing to compute — a power, a procedure, a definition the caller applies — is **inert**. Facts a witness or document could give, and the outcome of a discretion or an approval (the Comptroller's, the Minister's, an authorised body's), are inputs. The many incentive regimes that turn on a Minister's approval (exemptions in ss 13A-13X, concessionary rates in ss 43A-43X) take the approval and the awarded rate as inputs. Subsidiary legislation (rules and regulations under ss 7, 10G, 37, 45 etc.) is not in the source: where a rule needs a prescribed figure, take it as an input or refuse.

## Deliverables, all in this `encodings/` directory (no row subfolder)

1. `.l4` modules: `ita-types.l4`, one module per goal group, `ita-goal.l4` (the top level), and tests whose expected values come from the source.
2. `NOTES.md`: scope, the goals, a coverage table (every section and Schedule), a fork register.
3. `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, `REFUSE "…"` — never `FALSE` or `0`.
- Day counting: "within N days after" is the date N days later, inclusive; "within one month after" the same day of the next month; "within 4 years after the expiry of [a YA]" is 31 December of the fourth following year.
- Amounts are Singapore dollars, as a NUMBER; rates as percentages.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
