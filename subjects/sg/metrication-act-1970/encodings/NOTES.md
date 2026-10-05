# Metrication Act 1970 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act, ss 1–7 and the First to Fourth Schedules**, as printed by SSO, current version as at 05 Oct 2026 (2020 Revised Edition; the 1985 edition's Schedules A–D renumbered).
The only change since 1971 is G.N. No. S 22/1989, a rectification of the Fourth Schedule operating from 30 March 1987. No date is gated beyond s 3(1)'s own date, 15 February 1971, which the encoding states as the Act's answer: before that day, s 3(1) gives SI no legal force.
s 6 lets the Minister vary the Schedules by Gazette notification. The Schedules here are as printed; a later notification would be a new version this encoding does not have.

## 2. Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| long title | | inert |
| 1 | Short title | inert |
| 2 | Interpretation | encoded: (1)(a)–(b) membership of the International System of Units, with the "unless … context" exception as an input; (2) "SI" |
| 3 | International System of Units | encoded: (1) the 15 February 1971 date; (2) the three Schedules |
| 4 | Power to adapt, etc. | encoded: what an order under s 4 must do, (1)(a)–(b) and (2) |
| 5 | Conversion | encoded: every Third Schedule row, and which system ((a) or (b)) each unit is from |
| 6 | Power to vary Schedules | inert — a power |
| 7 | Saving | encoded, (1) and (2) |
| First Schedule | 6 basic units | encoded, every row (unit, symbol, quantity) |
| Second Schedule | 15 supplementary and derived units | encoded, every row |
| Third Schedule | 3 imperial and 4 local customary conversions | encoded, every row, with "exactly" or "approximately" |
| Fourth Schedule | 4 units used with SI | encoded, every row |

## 3. Fork register

| id | provision | the question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 7(1) "before the making of any order under section 4" | before which order? | before the s 4 order that touches the act in question; the order's date is an input, NOTHING if none has been made | Read as "before the first order of any kind", a single date would cut off the saving for every written law at once, including laws no order had yet converted. The text supports either. |

Smaller readings:
- **The gallon** is printed twice, as litres and as cubic decimetres. One row carries both, and the encoding says so in the unit name.
- **s 2(1)(b)'s exception** ("unless there is something in the subject or context … inconsistent") is a reading of the other written law, so it is an input, not computed here.

## 4. Tests

`ma-tests.l4`, 40 assertions: every Schedule's row count (6, 15 and 4), sample rows from each Schedule including the symbol "Ω", SI membership with and without the Fourth Schedule exception, both sides of 15 February 1971, s 4's three conditions, every Third Schedule conversion with the arithmetic shown, and the internal consistency the Schedule implies (16 tahil = 604.789824 g ≈ 1 kati; 10 chhun = 1 chhek exactly), s 7(1) on each side, and s 7(2).
`tests-independent.l4` (97 assertions) and `INDEPENDENT-TEST-REPORT.md` are the independent pass. A separate session wrote its expectations from the source before reading the encoding (`independent-expectations.md`). All 97 passed on the first run.

## 5. Checks

See `encoding.json` → `checks`.
