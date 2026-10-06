# Independent test report — Carbon Pricing Act 2018 (SG)

Expected values were decided from `../source/CPA2018.txt`, `../source/PROVENANCE.md` and `BRIEF.md` alone and written to `independent-expectations.md` (about 190 scenarios, ids A1-L4) before any `.l4` file, `NOTES.md` or the encoder's tests were opened.
The modules were then read only for their exported names and record types; `cpa-tests.l4` was glanced at for record-building syntax.
The assertions are in `tests-independent.l4`.

## Numbers

`~/.local/bin/l4 run tests-independent.l4` (JL4_LIBRARY_PATH unset), 266 `#ASSERT` lines:

| | count |
|---|---|
| assertions satisfied | **262** |
| assertions failed | **4** |
| other errors (DiagnosticSeverity_Error that are not failed assertions) | **0** |

`l4 check` succeeds. All 4 failures are `#ASSERT REFUSED` assertions, which `l4 run` reports as "assertion failed: expected a refusal, but the expression produced a value" (the message text is on the line after "Message:").

## Failing assertions

All four are about the same thing: the brief's vintage rule. BRIEF.md, "Vintages": *"the law is stated for **emissions years and events from 2024**; earlier ones **refuse**."*
The encoding has the guard (`the law is encoded for the year`), but uses it only in the registration rules (`the applications required…`, `the applications Y must make…`), the tax (`the carbon tax charged for`) and the top-level goal. The other rules that take an emissions year or an event date have no guard, so they apply the post-2024 text to earlier years and dates.

| line | scenario | expected | the encoding gave (`#EVAL` in scratchpad/indep-cpa/evals.l4) | source |
|---|---|---|---|---|
| 262 | s 9(2) advance notice, control to cease on 2023-06-01 | REFUSE (an event before 2024) | `2023-04-17` | s 9(2) "at least 45 days before that date"; BRIEF "Vintages" |
| 307 | s 17(1) last day to pay, **emissions year 2023**, s 21(1) notice served 2024-08-01 | REFUSE (s 17(1) was rewritten by Act 37 of 2022, and the pre-2024 text was not supplied) | `2024-09-30` | s 17(1)(a) "[Act 37 of 2022 wef 01/01/2024]"; BRIEF "Vintages" |
| 335 | s 24 waiver, tax $20 for **emissions year 2023** | REFUSE (s 24 is marked as amended by Act 37 of 2022; its "carbon price … of fixed-price carbon credits" did not exist before 2024) | `TRUE` (limit 5 × $5 = $25) | s 24 "[Act 37 of 2022 wef 01/01/2024]"; BRIEF "Vintages" |
| 378 | s 37(2) High Court threshold, change of $6,249 in the tax for **emissions year 2023** | REFUSE (s 37(2) is marked as amended by Act 37 of 2022) | `TRUE` (250 × $5 = $1,250) | s 37(2) "[Act 37 of 2022 wef 01/01/2024]"; BRIEF "Vintages" |

How much this matters: the s 9(2) case is borderline, because s 9(2) itself is not marked as amended. Even so, the brief's rule refuses every event before 2024, and the encoding's own top-level goal and tax rule follow that rule. The other three are clearer. Sections 17(1), 24 and 37(2) all carry the "[Act 37 of 2022 wef 01/01/2024]" marker, so the encoding is answering for 2023 from text that did not apply in 2023. The Third Schedule rate for 2023 ($5) is printed and is correctly *not* refused (G1 passes). What should refuse is the use of the current s 24 and s 37(2) wording for a 2023 emissions year.

Other rules with the same missing guard, not asserted separately: s 15(1), s 19(3)/(4), s 21(2), s 23(2)-(3), s 31A, s 33, s 34(2), s 44, s 67, s 75, and the s 17(4) late-payment penalty. Each takes dates but never calls `the law is encoded for the year`.

## Everything else passed

These all agree with my source-derived answers:
- **Schedules:** First Schedule GWPs at both ends of the HFC and PFC lists, carbon dioxide equivalence, both thresholds, every Part 2 item on both sides, Part 3 exclusions, and a mixed reckonable total.
- **Registration:** s 3 single-site tests and the s 4 tie refusal; s 7(1)-(6) at the exact thresholds, already-registered cases and control ceasing; s 8(1)(a)(ii) deadlines (A), (B) with both orders of the later-of, and (C), including across a year end; s 8(4).
- **Deregistration and reporting:** s 9 grounds both ways for taxable and reportable facilities; s 9(2) 45 days; s 9(4)-(5) and s 10(4); s 11 reporting periods and exclusions; s 12; s 15(1) working days with and without a holiday.
- **Tax and payment:**
  - s 16 tax: rounding up, the threshold on the unrounded figure, every rate and price band, s 20C allowances with (A−C) rounding, and the s 20B end date;
  - s 17(1) due dates for each kind of assessment; s 17(3)/(3B) credits and rounding; ICCs under s 33B/33C;
  - s 17(4) penalties: the 5% penalty, the 60-day point, completed months, the triple cap and 299 months under the cap;
  - s 19 refund time limits, crediting and rounding; s 24 at the boundary; s 29; s 31A at each price change (including no change in 2026); s 32; s 33 closure (notice, 30 days, objection, refund, (b)).
- **Process:** s 21(2), s 22, s 23 (4 years, 30 days, extension, allowance); s 34 deadline and decisions; s 37(2) at 250 × R; s 38; s 44; s 67(5)/(6); s 75(3).
- **Offences:** every maximum penalty, including the s 54(3) 10% + $10,000 + $50/day, the s 56(2)-(5) multiples and further fines, s 59, and the second-offence tiers in ss 55(2) and 62(1). Also s 71 composition, ss 68-69 officers, s 5(3), and s 79(1)-(2).
- **Top-level goal:** taxable year, unregistered year, late payment, an unprescribed sector, and the 2023 refusal.

## Scenarios I could not express (or only partly)

| id | scenario | why |
|---|---|---|
| D9 | s 7(1A): the person who must apply is whoever has control on 31 December | not computed; the caller supplies the person |
| D20 | s 7(7): a facility may be registered to more than one person | inert in the encoding |
| A/(C) overlap | X's facility taxable but the previous year < 25,000: both s 8(1)(a)(ii)(A) and (C) apply on their words | the Act does not order them. The encoding gives (C) priority, a reasonable reading. I did not assert it because I had not decided it before reading the code |
| F4 | s 11(3): the obligation arises at the end of the reporting period | inert |
| F7, F9 | s 12(2) and 12(3)(b): non-reckonable parts and the period after deregistration need not be verified | no partial-verification output, only a single "must be verified" flag; 12(3)(a) is covered only through the "plan approved" input |
| G18/G19 | Division 1A for 2023 | not separately testable; the tax for 2023 refuses as a whole |
| G21 | s 16(4): whose liability the tax is | carried as text |
| H11 | the ICC limit | taken as an input (as I expected) |
| H31 | s 29(1): whether the Agency *may* cancel when there are no credits | only "tax treated as paid by cancelling" is computed, with no permission predicate |
| I12 | refusing to deregister a *reportable* facility is not appealable | the `Agency decision` enum has no such value, so I could test it only as `some other decision` |
| J5 | email service takes effect "when retrievable" | the encoding uses the sending date, which is coarser than the Act's time-of-retrieval |
| K32 | s 70(3) over 10 days = $10,000 | only the per-day figure is exposed; I asserted $1,000/day |
| K38 | an offence that is not prescribed as compoundable cannot be compounded | `the composition limit…` has no "prescribed compoundable" input |
| C9 tie | covered (refuses) | — |
| L4 | s 79(3): the first reporting period is 2019 | carried as text |
| H19-H20 reading | the 1% months counted from the end of the 60 days, and the cap applied to the additional penalties alone | my reading and the encoding's (F5) coincide |

## Triage by the encoder (2026-10-06)

All four failures are **encoding errors**, and the report's wider point stands: the vintage gate (`the law is encoded for the year`) was applied only to registration, the tax and the top-level goal. It now wraps every rule that takes a year or a date: ss 9(2), 11(2A), 15(1), 17(1), 17(3), 17(4), 19(3), 19(2), 19(4), 21(2), 23(2), 23(3), 24, 31A, 32, 33(1)(c), 34(2), 37(2), 44(2), 67(5) and 75(3). All 266 independent assertions now pass, unchanged; six assertions of the same kind were added to `cpa-tests.l4`.

The scenarios the interface could not express (see above) are recorded in NOTES.md section 7 as known limits; none is a wrong answer.
