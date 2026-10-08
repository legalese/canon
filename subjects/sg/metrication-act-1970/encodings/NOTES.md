# Metrication Act 1970 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act, ss 1–7 and the First to Fourth Schedules**, as printed by SSO, current version as at 07 Oct 2026, text identical to 05 Oct 2026 (2020 Revised Edition; the 1985 edition's Schedules A–D renumbered).
The only change since 1971 is G.N. No. S 22/1989, a rectification of the Fourth Schedule operating from 30 March 1987. No date is gated beyond s 3(1)'s own date, 15 February 1971, which the encoding states as the Act's answer: before that day, s 3(1) gives SI no legal force.
s 6 lets the Minister vary the Schedules by Gazette notification. The Schedules here are as printed; a later notification would be a new version this encoding does not have.

### The goals

Top level, `the metrication position for` a `Measurement` (`ma-goal.l4`): *for a measurement used in Singapore, what does the Act say about it?* It returns one record, a field per goal:

| goal | question | function | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Is the unit part of SI, and in which role, with what symbol and quantity? | `the SI status of` u `, the context excluding the Fourth Schedule:` x | ss 2, 3(2); First, Second, Fourth Schedules | `ma-units.l4` |
| 2 | Does its use have legal force under s 3(1), keep another lawful system's force under s 7(2), or neither? | `the legal force of using` … | ss 3(1), 7(2) | `ma-units.l4` |
| 3 | What is the amount in SI units, and is the conversion exact, and under which limb of s 5? | `the conversion of` n u | s 5; Third Schedule | `ma-conversion.l4` |
| 4 | What must a s 4 order do; can an act done in a non-SI unit be challenged on that ground alone? | `an order within s 4` o; `the outcome of a challenge to an act done on` … | ss 4, 7(1) | `ma-orders-saving.l4` |

The Schedules themselves, as data, are in `ma-schedules.l4`; the nouns in `ma-types.l4`. The long title, s 1 and s 6 are carried as text (`provisions carried as text`, `ma-orders-saving.l4`).
The finer rules the goals compose (`a unit of the International System of Units:`, `the SI value of`, `s 7(1) bars a challenge to an act done on` and the rest) remain callable, and are what `ma-tests.l4` and `tests-independent.l4` test.

## 2. Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| long title | | inert |
| 1 | Short title | inert |
| 2 | Interpretation | Goal 1, `ma-units.l4`: (1)(a)–(b) membership of the International System of Units, with the "unless … context" exception as an input; (2) "SI" |
| 3 | International System of Units | Goals 1–2, `ma-units.l4`: (1) the 15 February 1971 date; (2) the three Schedules |
| 4 | Power to adapt, etc. | Goal 4, `ma-orders-saving.l4`: what an order under s 4 must do, (1)(a)–(b) and (2) |
| 5 | Conversion | Goal 3, `ma-conversion.l4`: every Third Schedule row, and which system ((a) or (b)) each unit is from |
| 6 | Power to vary Schedules | inert — a power |
| 7 | Saving | (1) Goal 4, `ma-orders-saving.l4`; (2) Goal 2, `ma-units.l4` |
| First Schedule | 6 basic units | `ma-schedules.l4`, Goal 1: every row (unit, symbol, quantity) |
| Second Schedule | 15 supplementary and derived units | `ma-schedules.l4`, Goal 1: every row |
| Third Schedule | 3 imperial and 4 local customary conversions | `ma-schedules.l4`, Goal 3: every row, with "exactly" or "approximately" |
| Fourth Schedule | 4 units used with SI | `ma-schedules.l4`, Goal 1: every row |

## 3. Fork register

| id | provision | the question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 7(1) "before the making of any order under section 4" | before which order? | before the s 4 order that touches the act in question; the order's date is an input, NOTHING if none has been made | Read as "before the first order of any kind", a single date would cut off the saving for every written law at once, including laws no order had yet converted. The text supports either. |

Smaller readings:
- **The gallon** is printed twice, as litres and as cubic decimetres. One row carries both, and the encoding says so in the unit name.
- **s 2(1)(b)'s exception** ("unless there is something in the subject or context … inconsistent") is a reading of the other written law, so it is an input, not computed here.

## 4. Tests

`ma-tests.l4`, 40 assertions: every Schedule's row count (6, 15 and 4), sample rows from each Schedule including the symbol "Ω", SI membership with and without the Fourth Schedule exception, both sides of 15 February 1971, s 4's three conditions, every Third Schedule conversion with the arithmetic shown, and the internal consistency the Schedule implies (16 tahil = 604.789824 g ≈ 1 kati; 10 chhun = 1 chhek exactly), s 7(1) on each side, and s 7(2).
`tests-independent.l4` (97 assertions) and `INDEPENDENT-TEST-REPORT.md` are the independent pass. A separate session wrote its expectations from the source before reading the encoding (`independent-expectations.md`). All 97 passed on the first run, and still pass unchanged after the 2026-10-07 restructure into goal modules (only their `IMPORT` lines changed, `ma-act` having been split).
`ma-tests-goals.l4`, 41 assertions, tests the goal functions and the top-level goal, values worked by hand from the source: SI status for a basic, a derived and a Fourth Schedule unit with and without the s 2(1)(b) exception; legal force on each side of 15 February 1971 and under s 7(2); conversions with their s 5 limb and exactness, and a refusal for an SI unit; challenge outcomes before, on and after the order's date; and four whole measurements through `the metrication position for`.

## 5. Checks

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-07: 9 modules, 0 errors, 178 assertions satisfied, 0 failed (`ma-tests` 40, `ma-tests-goals` 41, `tests-independent` 97). No assertion is expected to fail. See also `encoding.json` → `checks`.
