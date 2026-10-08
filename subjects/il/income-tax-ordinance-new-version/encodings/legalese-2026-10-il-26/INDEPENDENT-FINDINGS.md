# Independent findings, row IL-26 (BACKLOG IL-56), by fid-il-26

DECIDED-ANSWERS.md (sha256 `cbaad463574eb9ca9b9d526b0b61d76f67af77e3c64c46ed71550acd55aff314`) was written from the Hebrew sources before any file of this directory was opened, then copied here and not edited.
It decides 131 cases (A01-A30, B01-B10, C01-C04, D01-D08, E01-E14, F01-F02, G01-G17, H01-H03, I01-I08, J01-J08, K01-K13, L01-L11, M01-M03).
`tests-independent.l4` asserts the 68 cases (counting each assertion) that fall inside the scope this encoding pins; the rest are SCOPE (below).
`check.sh` run: 12 modules, 0 errors, 183 assertions satisfied, 0 failed, 7 refused, exit 0 (the 7 refusals are declared in `check.sh` by line, id and class).
`l4` sha256 before and after: `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (the same, `jl4-0.1-6df1397b`).

## Result in one sentence

Every value I decided for a case inside the pinned scope agrees with the encoding (68 satisfied assertions), apart from the seven refusals below, none of which is a wrong number; there is no OURS-WRONG finding.

## Disagreements

| Id | Class | Cases | What | Hebrew and arithmetic |
| --- | --- | --- | --- | --- |
| 1 | AMBIGUITY | C01, C02 (assertions at lines 178, 179) | The Director's table is not held. I decide the employer computes by items 1-5 (575 for a 10,000 salary, 156 for 7,000); the encoding's `the employer deducts, given the Director's table` refuses without the table's figure. | Reg 3(a) says the employer deducts "מס כמפורט בתוספת א׳"; item 6 says "המנהל יפרסם לוח ... ומשעשה כן ינכה המעביד את המס של עובדיו לפי אותו לוח". Whether the table is an aid to items 1-5 (my reading, M) or displaces them (the encoding's) the text does not say. The encoding's `Schedule A — the tax on a month's salary of ...` returns 575, so the number is available; only the "the employer deducts" entry point refuses. I tested both: that function gives 575, and the table-held case C03 (a supplied 600 is deducted) passes. |
| 2 | AMBIGUITY | F02 (line 235) | A part payment of 5,000 of a 10,000 month: 287.50 exact or 288. I flagged it as ambiguous (L); the encoding refuses by fork F3, as it should. | Reg 3(b): "חלק יחסי מהמס שיש לנכות ממשכורת החודש"; 575 x 5,000/10,000 = 287.50. No rounding rule outside Schedule A item 5. |
| 3 | SCOPE | A25, A26, A27, A28 (lines 155-158) | Tax years 2025 and 2023. I decided values from the ITO's editorial table rows "2024-2025" and "2023" (A25 575, A26 2,995, A27 4,647, A28 616). The encoding refuses: "section 121 as it stood before tax year 2026 is not in the deposited text". | The operative s 121 text in the deposit is the 2026-2027 text (amendment תשפ״ו־6); the earlier brackets appear only in the unofficial table note, and the 2023 rows have typos ("116,711", "187,481"). The encoding is right to decline to treat a table note as the section, so I class this SCOPE, not OURS-WRONG. 2025: 20,000 x 12 = 240,000: 8,412 + 5,124 + 20% x 73,080 (=14,616) + 31% x 46,200 (=14,322) = 42,474 less 6,534 = 35,940; /12 = 2,995. |
| 4 | TESTER-WRONG (fixture, fixed before the final run) | D04, E08 | The first run of my declared-additional-position cases gave 575, not 4,700. My payment fixture left `the employee works elsewhere, or receives a taxable pension from another payer` FALSE. | Reg 1 "משכורת בעד משרה נוספת": more than five hours a day, "המועסק במקום עבודה אחר או המקבל ממעביד אחר קצבה חייבת במס". An additional-position payment is one where the employee works elsewhere, so the encoding is right to need both the declaration and that fact. I corrected the fixture (`independent: additional-position payment`), not the expected value. |

## SCOPE (decided by me, not encoded, no assertion)

The encoding pins out of scope: regs 3(c)-(d) with Schedules B and C, 4(b), 6, 7, 8, 11-15 (NOTES section 2).
My cases that rest on them, with their decided answers, are in DECIDED-ANSWERS.md and remain untested:

- B09, B10 (s 35 and s 39B points are not in the item 3 list, so the employer does not credit them without a direction): the encoding takes the points as one input number and lists the s 35 ground only in reg 9(a)(4); it cannot test whether the points are credited automatically.
- E13 and the day-worker cases J01-J08 (Schedule B, 300 a day, the 35% lump sum): refused by name.
- G10 to G17 (reg 4(b), reg 7 retirement grants).
- H01-H03 (reg 8, payment in kind).
- I01-I08 (Schedule C, foreign workers): refused by name.
- K01-K13 (reg 6: provident fund 25%, sabbatical 35%, disabled escort 25%, shift credit 15% and the 0105 notice, survivors' 40%, non-residents, annuity capitalisation).
- L01-L11 (regs 2, 11, 12, 13 deadlines).
- M02, M03 (definitions of employer and registered spouse).
- A29 (2028) and A30 (2022) are asserted as refusals ("no annual figures ... have been sourced") and pass.

## What agreed (so the reader knows what was tested)

- Schedule A at 24 salaries from 3,000 to 100,000, both sides of every band top (7,010/7,011; 10,060/10,061; 19,000/19,001; 25,100/25,101; 46,690/46,691) and of the s 121B line (60,130; 60,200; 61,000), rounding at .50 (7,000 gives 156), credit points 2.25, 2.75, 3.25, 4.25 and 7.25, and the floor at nil.
- The maximal rate: no card, a card without the other-income section, a declared additional position, with and without a form 0130, a partial salary (including the 5-hours-a-day edge and the 18-day edge), a pension, a pension with an exempt part, the withdrawal of form 0130, an assessing-officer rate of 30%.
- Part payments 6,000 and 4,000 of 10,000.
- Reg 4(a) bonuses: nine cases including the 25% floor for a bankrupt's employees and a bonus that crosses the s 121B line.
- A payment made in 2027 for 2026 (M01): 575.
- The 47% flat rate is exact (D06: 3,333 gives 1,566.51), and 100,000 with no card gives 47,000, not 50,000 (R4).

## Anything the encoder read wrongly in the source

None found.

- All 24 `src:N` comments quote the Hebrew of line N of the deposited file verbatim, checked mechanically; the one string that differs is a heading (reg 10 is printed with the template `{{ח:סעיף|10|...}}` and quoted as plain text).
- The figures (credit point 2,904; s 121B amount 721,560; 60,130 a month; credit point 242 a month; maximal rate 47%; band tops) match the ITO text (lines 1563, 4349-4363, 4440-4450, 4455).
- The ten kinds in s 164 match the list at line 5323.
- The 18-day test ("למעט עבודה של פחות מ־18 ימים") is read as at least 18 days, as I read it.
- Reg 5's order (partial salary, then declared additional position, then no card or no other-income section) gives the same answers as mine on every combination I tested.

## Open points the text does not decide (both of us flagged)

- Whether the Director's table displaces items 1-5 (finding 1).
- Part-payment rounding (finding 2).
- The overlap of "partial salary" and "day worker" (E14: 12 days of 4 hours); both of us take partial salary first; I rate that L.
- Rounding of a flat-rate deduction (D06) and the ceiling reading of reg 6(h); the latter is out of scope.
