# Encoding brief: the Carbon Pricing Act 2018 (Singapore), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Carbon Pricing Act 2018** — Singapore, 2020 Revised Edition, as printed by Singapore Statutes Online, "Current version as at 06 Oct 2026".

The Act requires the person in operational control of a business facility whose greenhouse gas emissions reach 2,000 tCO2e a year to register and report its emissions, and, at 25,000 tCO2e, to register the facility as a taxable facility, have its reports verified, and pay a carbon tax on its reckonable emissions — by surrendering fixed-price carbon credits (and, within limits, eligible international carbon credits). It provides for allowances for export-oriented facilities, assessments, objections and appeals, records and registers, enforcement powers and offences.

The source is `../source/CPA2018.txt`, extracted mechanically from SSO's PDF; `../source/PROVENANCE.md` says where it came from and transcribes the one formula the PDF prints as an image (s 31A: R × S / T). It is SSO's unofficial consolidation (SSO Terms of Use cl.8), not the authoritative text. The PDF is not in the repository.

### Vintages

The Carbon Pricing (Amendment) Act 2022 (Act 37 of 2022), in force **1 January 2024**, rewrote registration, reporting periods, payment, credits and the Third Schedule. The text before it was not supplied, so the law is stated for **emissions years and events from 2024**; earlier ones **refuse**. The Third Schedule itself carries the rates and prices for every year (including 2023 and earlier), and those tables are encoded as printed.

## The top-level goal, and the goals under it

Top level: *for this business facility and this emissions year, what does the Act require of the person in operational control, and what does it owe?* Under it, combine provisions into goal-level conclusions rather than one function per subsection:

1. Must the person register (or may it deregister)? — ss 3-10, 79
2. What must it report, and by when? — ss 11-15
3. How much carbon tax is charged? — ss 16, 20A-20G, First to Third Schedules
4. How, and by when, is it paid, and what if it is late? — ss 17-20, 24, 26-33D
5. Can the assessment be made, revised, objected to or appealed? — ss 21-25, 34-39
6. What records and register updates are owed? — ss 40-44, 67, 75
7. Is an offence committed, and what is the most it can cost? — ss 5(3), 47-62, 68-71, 76(4)

Keep an `@ref` on every rule. A provision with nothing to compute — a power, a procedure, a definition the caller applies — is **inert**: carry it in the coverage table and say so. Facts a witness or a record could give, and the outcome of a discretion (the Agency's, the Minister's or a court's), are inputs. Subsidiary legislation (prescribed industry sectors, ICC criteria and the ICC limit, record periods, compoundable offences, the end date of Division 1A) is not in the source: where a rule needs one, take it as an input or refuse.

## Deliverables, all in this `encodings/` directory (no row subfolder)

1. `.l4` modules: `cpa-types.l4` (nouns only), `cpa-schedules.l4`, the goal modules, `cpa-goal.l4` (the top level), and tests whose expected values come from the source.
2. `NOTES.md`: scope, the goals, a coverage table (every section and Schedule), a fork register.
3. `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's own words beside each limb.
- Where the source does not answer, `REFUSE "…"` — never `FALSE` or `0`.
- "Attains" a threshold means at least the threshold.
- Day counting: "within N days after" is the date N days later, inclusive; "N years after" the same date N years later. "Working day" is not defined in the Act; record the reading taken.
- Amounts are Singapore dollars, as a NUMBER; emissions in tCO2e.
- A failing assertion is a finding: never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Toolchain

`~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa`. Leave `JL4_LIBRARY_PATH` unset.
