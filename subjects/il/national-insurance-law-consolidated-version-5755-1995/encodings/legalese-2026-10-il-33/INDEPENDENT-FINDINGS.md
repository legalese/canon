# Independent findings for IL-33 (fid-il-33, BACKLOG IL-56)

Author: fid-il-33, independent test author.
`DECIDED-ANSWERS.md` was written from the Hebrew sources alone and frozen before any `.l4` module, `NOTES.md` or test of this encoding was opened.
Its sha256 is `61c59b6556091edcf35e17b42d15007b03c2904faf6ed9af5071e476c2d050e4`, recorded at 2026-10-09 07:47 (+08), and it has not been edited since.
It holds 383 decided cases (28 rounding, 22 basic amounts, 28 s 68 amounts, 68 retirement ages, 20 residence, 81 statuses, 26 housewife/widow/widower, 44 child/payee/count, 12 s 335, 8 Family Allowance Regulations, 26 Income Support gates, 20 Maintenance gates).
`tests-independent.l4` holds 321 assertions through the encoding's public entry points, each group tagged with the decided-answer ids it asserts; the decided cases it does not reach are listed under SCOPE (below).

## Run

`env -u JL4_LIBRARY_PATH L4=/Users/mengwong/.local/bin/l4 ./check.sh` exits 0.
l4 sha256 before and after the run: `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (the same).
`tests-independent.l4` row of the check table: errors 2, satisfied 318, failed 2, refused 1, expected 2/1.
The two failures and the one refusal are declared in `check.sh` by line and id and explained below.
Every other module is unchanged: 0 errors, and its own satisfied counts as before (the total of the table is 929 satisfied, 2 failed, 1 refused, 2 errors that are the 2 failures).
(A running `l4` with `JL4_LIBRARY_PATH` set to the empty string, as opposed to unset, makes every import fail; use `env -u`.)

## Disagreements

| id | decided answer | encoding | class |
| --- | --- | --- | --- |
| ST-37 (test line 388) | a 17-year-old resident who came under the Law of Return is insured for long-term care (s 223 "מבוטח" (4)), without an absorption basket | not insured unless the basket was given (`nii-statuses-chapters.l4` s 223: `(immigrated OR visa) AND basket`) | AMBIGUITY, with an unregistered fork |
| ST-38 (line 389) | an immigrant who first became resident at 70 (so excluded from Chapter 11 by Part C) is insured for long-term care through (4) | same, not insured without the basket | AMBIGUITY, same cause |
| ML-18 (line 837) | a creditor exempt under ML s 9A(c)(1) is not barred by the exit rules, so the month is paid | refuses by name: s 9A(c)(2) pays such a creditor by rules the Minister of Justice fixes and they are not deposited | TESTER-WRONG |
| ST-78 (first draft, corrected before the final run) | 5 months of service, not insured | the first draft passed the flag "six months and married within 30 days" as TRUE with 5 months, a contradiction; the encoding answered insured from the flag | TESTER-WRONG on the input; see the note on the flag below |

### ST-37 and ST-38: where the absorption-basket clause attaches (AMBIGUITY)

The Hebrew of s 223 "מבוטח" (4) (source line 2178) reads: "תושב ישראל שעלה לפי חוק השבות, או תושב ישראל שבידו אשרה ורישיון לישיבת קבע או אשרה ורישיון לישיבת ארעי מסוג א/5, לפי חוק הכניסה לישראל, שניתן לו סל קליטה מהמשרד לקליטת העליה, והכל אם אינם מבוטחים בביטוח אזרחים ותיקים וביטוח שאירים".
I read "שניתן לו סל קליטה" as qualifying the second limb (the holder of a permanent or A/5 visa), since a person who came under the Law of Return is an immigrant by that fact and the basket is the proof the Law asks of a visa holder.
The encoder reads it as qualifying both limbs.
Both readings are grammatical: the clause is masculine singular, which fits either "תושב ישראל".
The SHRUG policy of the encoding says one named switch with a default decline where readings differ; this clause has no row in the fork register (`NOTES.md` section 3) and no switch, so the encoder took one reading silently.
Arithmetic: none.
Effect: a Law-of-Return immigrant without a recorded basket, not insured under Chapter 11 (under 18, or first resident after the Part C age), is insured for care on my reading and not insured on the encoder's.
For an immigrant who is insured under Chapter 11 (the common case) both readings agree, because (1) already insures him; I asserted that case (ST-33) and it passes.
Recommendation: register it as a fork with the default declining where the two readings differ.

### ML-18: Maintenance Law s 9A(c)(2) (TESTER-WRONG)

Re-reading the Hebrew: s 9A(c)(1) disapplies (b) for a creditor entitled for the previous month who left Israel at the employer's request and cost, or for medical treatment; s 9A(c)(2) says "תשלום לפי סעיף קטן זה ישולם לפי כללים, תנאים ולתקופה שקבע שר המשפטים".
My decided answer stopped at (c)(1).
The encoding's refusal by name ("needs a source") is right.
The assertion stays as decided (it records my error), declared in `check.sh` as an expected refusal.

### The flag in `A completed service` (observation, not a disagreement)

`a woman who served at least six months and married within 30 days of the day she stopped` is an input flag; the encoding does not check it against `the months served`.
A caller who passes 5 months with the flag TRUE gets "insured".
That is an input convention, stated in the nouns module, and the Hebrew proviso ("ותקופת שירותה בפועל לא פחתה משישה חודשים, והיא נישאה בתוך 30 הימים") would be easy to check from the months and a marriage date.
I do not count it as a disagreement.

## Cases where my reading was chosen and the encoding agrees with a named reading

These pass when the reading is named, and the default declines as the SHRUG policy requires.

- BA-02 to BA-22: a fall in the index leaves the amount as it was; each year's figure is rounded to whole shekels before the next update; the encoder's arithmetic and mine agree to the shekel for all three slots in all twelve years (the ratios I got from the CBS file agree to five places with the encoder's).
- HW-08: "married means married only" for a woman known in public as the wife (the default declines).
- HW-18 parse 1: the maintenance limbs are alternatives inside the condition of separation (the default declines where the parses differ: not separated, no actual maintenance).
- RS-09: exactly 183 days (the default declines; the reading "neither limb applies" makes him a resident).
- RA-36: the day an age is reached when the later month lacks the day of birth (the default declines).
- ST-09 to ST-12: for a woman, s 240(a) tests the retirement age, not the Part C age.
  The encoder does the same without a fork; my reading was M, so I flag that the other reading (Part C also for women) would change the answer for a woman first resident between her Part C age and her retirement age.

## Cases decided where the encoder made a different choice that my tests cannot reach

- CH-31 (s 69, child with both parents, the mother not insured, the father insured): I decided the father is paid (L).
  The encoder's fork P3 pays the mother whether or not she is entitled.
  The facts record has no field for the mother's entitlement, so the case cannot be asserted.
  Class: AMBIGUITY.
- RR-16: where reg 2 and reg 3 both fit a daily benefit based on income, I took reg 2; the encoder's `reg 2 to 7 — the amount rounded ... a kind` makes the caller choose the kind, so the question does not arise in the code.

## SCOPE: decided cases not asserted, and why

- Not in this row (IL-06's s 65-68 and 72, kept apart by the BRIEF): CH-01 to CH-24 (who is an insured parent, who is a child, whose count, s 67), CH-35 and CH-36 (s 70), CH-42 to CH-44 (s 72(b)), CA-23 to CA-28 (s 66 additional tax, s 72, s 73).
  The s 68 amounts CA-01 to CA-22 are asserted only as far as this row reaches them: the basic amounts of the updating clause and the child-by-child rounding of reg 3 (with my multiplications as inputs), not the choice of ordinal.
- Not encoded (the coverage table of `NOTES.md` says out-of-scope): HW-21 to HW-26 (the widower, the Schedule 9 threshold, "עובד מבוטח"); ST-28 to ST-34 (the Chapter 9 housewife exceptions, "נכה"); ST-54 (s 77 registration); RR-26 and RR-27 (regs 9 and 10).
- Not expressible in the facts records: ST-80 and ST-81 beyond the refusals asserted; IS-11 to IS-14 (the s 2(a)(5), (9) grounds are given as listed flags, with no age-of-child or day-count test); IS-16 and IS-20 to IS-24 (s 3A, 14(c), 2(e), the basic amount); ML-06, ML-07, ML-11, ML-13, ML-17, ML-19, ML-20 (the adult-child definition, the 30-day reply, execution before applying, the 183-day notice exception, the supplement, foreign judgments); RS-12 (a citizen holding a visa); RS-16.
- RR-12: reg 3 excludes the benefit "לפי פרק ו3" (today's Chapter 8, shown in the consolidated text as "[פרק ו׳3]"); the encoding has no Chapter 8 kind and rounds whatever the caller labels a cash benefit.
  That is a small gap; the Chapter 8 benefit has no rounding rule at all in the Regulations, so a caller should be refused, not rounded.
  RR-28 (nothing rounds an amount outside regs 2 to 7) is likewise the caller's choice in this code.
- Inputs by design: ST-15 (the s 243 classes), ST-47 (the s 75(a)(2) excluded class), ST-79 (Security Service Law s 16(1), asserted as a refusal), IS-23 and ML-08 (regulation figures, asserted as refusals).

## What I checked in the encoder's reading of the source

- `tools/hebcheck.py` run against the source of each module: no Hebrew run in any module's own code or comments fails to occur in its source.
- Schedule A1 Parts A, B, C and E: every band edge I asserted matches (RA-01 to RA-68), including the open bands and the women's 1956 hand-off to the Retirement Age Law's Part B.
- The determining year of s 2A: grant minus 183 days, as I computed it (RS-07, RS-14).
- The updating clause: the November index as "published last before 1 January" (the CBS publishes on the 15th of the next month), the 2025 freeze, the 2026 ratio taken against November 2024 with no catch-up: all as I decided, and the printed 169/214/158 and 173/219/162 are reproduced.
- Nothing in the encoder's quoted Hebrew or its figures was found wrong against the source.
