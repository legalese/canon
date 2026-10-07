# Independent findings, row IL-08 (income tax half)

Independent test pass on `legalese-2026-10-il-08`, the Income Tax Ordinance encoding of ss 1, 2, 35, 37-40, 45A, 47, 64B and 65.
Test author `fid-il-08a`, working in two sessions on 2026-10-07.
The first session wrote `DECIDED-ANSWERS.md` from the Hebrew source and stopped at a usage limit.
The second session wrote this file and `tests-independent.l4`.
`DECIDED-ANSWERS.md` was finished at 00:45:44 UTC, before any `.l4` file, `NOTES.md`, `encoding.json`, `check.sh` or `tools/` of this encoding was opened.
Its main body was frozen and has not been edited.
The only addition is a section headed "Revised after seeing the encoding", appended at the foot.

## The run

The command was `/Users/mengwong/.local/bin/l4 run tests-independent.l4`, run in a scratch copy of this directory with `JL4_LIBRARY_PATH` unset.
It ran from 2026-10-07T01:45:29Z to 01:45:44Z.
The binary resolves to cabal store `jl4-0.1-ff13a0ea`, sha256 `f6501568…dfa8bc`, the same build `NOTES.md` section 0 records.
`tests-independent.l4` has sha256 `88a0bf25…ce926451`.
Only this one module was run; `check.sh` was not run over the encoding.

| module | errors | satisfied | failed | refused |
| --- | ---: | ---: | ---: | ---: |
| `tests-independent.l4` | 7 | 190 | 7 | 8 |

There are 205 assertions, 10 of them `#ASSERT REFUSED`.
All 7 errors are the 7 failed assertions; there are no other errors.
Counts were taken the way `check.sh` takes them, by reading the line after each `Message:` rather than the exit code.

**Classification of the 15 that did not pass:**

- **Encoding errors (2).** D187 fails: the s 45A floor is lost, so the credit falls when the payment rises. D183 refuses on a case that has only one kind of sum.
- **Genuine ambiguities the encoder did not record (5 assertions, 3 questions).** D019 is the second limb of "תושב חוץ". D055 is a second aliyah. D190 and D236 (two assertions) are the order between s 47(b) and s 45A.
- **My own error (1).** D244: the facts contradict each other.
- **Not errors (7).** These are refusals of tax years before 2024, the encoding's recorded scope (assumption A1). For each one the per-month helper agrees with my figure.

## Failing assertions

### 1. D187: survivors' pension insurance above the floor gives *less* credit. Encoding error.

**Scenario.**
An employee, not a beneficiary member, earns 100,000 of insured income in 2026.
He pays only survivors' pension insurance, 5,000.

**Provision.**
s 45A(d) chapeau, line 1725: `לא יעלה על הגבוה מבין הסכומים המפורטים להלן`.
The (d)(1) floor (2,268 for 2026) is set against (d)(2)(b)(2), line 1730: `7% מהכנסתו המזכה, ובלבד שהסכום הכולל שבשלו יינתן זיכוי בעד סכומים ששולמו לביטוח קצבת שאירים כאמור בסעיף קטן (ב) לא יעלה על 1.5% מהכנסתו המזכה של היחיד`.

**Expected.**
Limb (2) after its proviso is 1,500.
The higher of 2,268 and 1,500 is 2,268, so the base is 2,268 and the credit is 35% × 2,268 = 793.80.

**Encoding answered.**
525, which is 35% × 1,500.

**Why it is an encoding error.**
The encoding's own fork F5 says the provisos "bind where limb (2) is the higher amount, and not where the fixed amount of limb (1) is".
The code decides whether limb (1) governs by comparing it with limb (2) *before* the proviso (5,000).
It then applies the proviso inside the 35% branch and never compares the result with the floor again.
That branch is `s 45A(d)-(e) — the sums credited, where every creditable sum is at 35%, for` in `ito-s45a-insurance-and-pension-credit.l4`.
None of its `min `the most` (…)` arms takes `max` with the fixed amount.
As a result the answer matches neither reading:

- Under F5(i), D187 should be 793.80.
- Under F5(ii), where the provisos always bind, D186 (survivors' insurance 2,000) should be 525. The encoding answers 700, and my D186 assertion passes.

The defect is a cliff.
I probed it after the run, outside the delivered tests:

| survivors' insurance paid | credit |
| ---: | ---: |
| 2,000 | 700 |
| 2,268 | 793.80 |
| 2,269 | 525 |
| 5,000 | 525 |

Paying one more shekel cuts the credit by 268.80.
The same omission is in the (d) work-income arm and the (e) arms of that rule.
So it can strike whenever the pension sums plus the capped survivors' sums come to less than the fixed amount, while the sums paid come to more.
It returns a wrong number with no diagnostic.

### 2. D019: the second limb of "תושב חוץ". Genuine ambiguity, not recorded by the encoder.

**Scenario.**
An individual is abroad at least 183 days in each of 2025 and 2026.
On the ties, his centre of life is in Israel in those years.
His centre of life is not in Israel in 2027 and 2028.
The question is whether he is an Israeli resident in 2026.

**Provision.**
s 1, lines 167-169: `”תושב חוץ“ – מי שאינו תושב ישראל, וכן יחיד שהתקיימו בו כל אלה: (א) הוא שהה מחוץ לישראל 183 ימים לפחות, בכל שנה, בשנת המס ובשנת המס שלאחריה; (ב) מרכז חייו לא היה בישראל ... בשתי שנות המס שלאחר שנות המס האמורות בפסקת משנה (א)`.

**Expected.**
REFUSE.
The second limb deems such an individual a foreign resident even though his centre of life was in Israel.
The text does not say which prevails, nor for which tax year the deeming operates.

**Encoding answered.**
TRUE: resident, on the centre-of-life finding.

**Classification.**
This is a genuine ambiguity the encoder did not record.
The coverage table (`NOTES.md` section 2) has no row for "תושב חוץ" at all.
It lists "תושב ישראל" (a)(1)-(4) and (b), "הכנסת עבודה", "בן זוג" and "גיל הפרישה".
The input record `An individual's year, for the definition of Israeli resident` carries no facts about later tax years, so the limb cannot even be put to the rule.
Other sections take this rule's TRUE as "resident" (ss 37-40, 45A(a)(1)), so the answer feeds into them.
At the least it needs a coverage row and a refusal, or an input, for an individual who meets limbs (a) and (b).

### 3. D055: a second aliyah. Genuine ambiguity, not recorded; I lean to an encoding error.

**Scenario.**
An individual has already received the credit on a first aliyah, and immigrates again.
The scenario says nothing about the 1977 rules.

**Provision.**
s 35(c), line 1580: `ולא יינתן אלא בפעם הראשונה שנעשה לעולה`.
s 35(e)(1), line 1586: `כללים למתן הזיכויים על פי סעיף קטן (א) למי שהיה בעבר בגדר ”עולה“`.
The rules were published, according to the note at line 1588, but they are not in the source bundle.

**Expected.**
REFUSE.
A flat 0 ignores the rules that (e)(1) authorises for exactly this person.

**Encoding answered.**
- With `rules under section 35(e) apply to the immigrant` set to FALSE: 0. The assertion fails.
- With it set to TRUE: the refusal. That assertion passes.

**Classification.**
The encoding moves the question to the caller as a boolean input.
My D055 expected a refusal and did not accept "or input", unlike several other scenarios.
For someone who is not a first-time immigrant, the (e)(1) rules are by their terms the instrument that governs.
A caller can answer FALSE only by knowing rules the row says it does not hold.
So the 0 is close to the "guessed 0" that `BRIEF.md` forbids.
The fork register does not record this; the coverage row for s 35(e) says only "out-of-scope, refused".
Suggested fix: refuse whenever `the first time the individual became an immigrant` is FALSE.

### 4-6. D190 and D236: the order between the s 47(b) deduction and the s 45A credit. Genuine ambiguity, not recorded as a fork.

**Scenario.**
A self-employed individual, not a beneficiary member, has no work income and taxable income of 100,000.
- D190: he pays 10,000 to a pension fund.
- D236: he pays 5,000; separately, he pays 7,000.

**Provision.**
s 47(b)(1), line 1779: `7% מהכנסתו המזכה שאיננה הכנסת עבודה`.
s 47(c), line 1787: `סכום שנוכה לפי סעיף קטן (ב) או (ב1) לא יובא בחשבון לצורך סעיף 45א`.
s 45A(b) and (d)(2)(b)(1) also bear on it.

**Expected.**
REFUSE, or a recorded fork.
The source does not say whether the deduction or the credit takes the payment first:

| paid | deduction first | credit first |
| ---: | --- | --- |
| 10,000 | deduction 7,000, credit 1,050 | credit 1,750, deduction 5,000 |
| 5,000 | deduction 5,000 | deduction 0 |
| 7,000 | deduction 7,000 | deduction 2,000 |

**Encoding answered.**
The deduction was 7,000 for D190, and 5,000 and 7,000 for D236.
These are the deduction-first answers.

**Classification.**
This is a genuine ambiguity, and the encoder half-recorded it.
The nouns module comment above `sums deducted under section 47(b) or (b1)` says "Which sums the individual deducts and which he takes as a credit is his return's".
In line with that, s 45A takes the deducted sum as an input.
But `the deduction under section 47 for` takes no such input: it always returns the largest deduction s 47(b) allows.
The fork register has nothing on the order; F10 is a different question.

On reflection, s 47(c) assumes the deduction is fixed before s 45A applies, and that supports deduction first.
I note this in "Revised after seeing the encoding" but have not changed the expected answer.
The encoding's answers are a defensible reading.
What is missing is the record of it, and an input or a refusal on the s 47 side for a taxpayer who claims the credit first.

### 7. D244: my own error.

**Scenario.**
An individual who is "not a beneficiary member", self-employed with taxable income of 200,000, pays 30,000.

**Provision.**
s 47(a)(7), line 1776: `בסכום שלא פחת מ־16% מסך כל השכר הממוצע במשק באותה שנת מס`.
For 2026 that is 16% × 165,228 = 26,436.48.

**Expected.**
18,084: 7% of 164,400, plus the further deduction of up to 4%.

**Encoding answered.**
0.
The 30,000 was entered as the sum paid for him in respect of his income, as the facts require.
That makes him a beneficiary member.
s 47(b) then gives nothing, and the (b1) field, which I left empty, gives nothing either.

**Classification.**
This is my own error.
The facts cannot both hold, because his own 30,000 deposit makes him a beneficiary member.
With the deposits for him set below the threshold, the encoding answers 18,084, my figure.
I probed that after the run, outside the delivered tests.
The assertion is left failing, as written.

## Refused assertions

### R1. D183: life insurance only, above the 5% proviso. Encoding error (it refuses where the answer is determined).

**Scenario.**
An employee, not a beneficiary member, earns 100,000 of insured income.
He is resident and pays only life insurance, 6,000.

**Provision.**
s 45A(a)(1) at 25%, with the proviso in (d)(2)(b)(2), line 1730: `ושהסכום הכולל שבשלו יינתן זיכוי בעד סך הסכומים ששולמו לביטוח חיים כאמור בסעיף קטן (א)(1), לביטוח קצבת שאירים כאמור בסעיף קטן (ב) ובשל הכנסה שאינה מעבודה, לא יעלה על 5% מהכנסתו המזכה של היחיד`.

**Expected.**
The base is 5,000 and the credit 25% × 5,000 = 1,250.

**Encoding answered.**
"section 45A does not say which sums are credited when its limits cut sums of different kinds".

**Why it is an encoding error.**
There is only one kind of sum here, so the refusal's own words are false of this case.
Fork F1 computes exactly "where every creditable sum is at 35% (the rate is one…)".
That reasoning covers a case where every creditable sum is at 25% just as well, but the rule's second branch tests only ``at 25%` EQUALS 0`.
The case is common: anyone whose only payment is life insurance above 5% of qualifying income.
My probe after the run gave 1,250 for 5,000 of life insurance and a refusal for 5,001.
It is not a wrong number, but it declines an answer the text gives.

### R2-R8. Tax years before 2024. Not errors: the encoding's recorded scope (assumption A1).

These seven are D040 (2023), D047 (2021), D048 (2022), D049 (2023), D052 (2022) and D053 (2021 and 2022).
Each refuses with "row IL-08 does not hold the text of these sections for a tax year before 2024".
`NOTES.md` section 3 (A1) records the gate.

The same scenarios are asserted a second time through `s 35 — the fraction of a point for month … of the tax year, for`, which has no year gate.
All seven helper assertions are satisfied, as is D046, the 8.5-point total over 2023-2028, through the helper.
So the month arithmetic, both regimes, and the regime boundary (aliyah on 2021-12-31 against 2022-01-01) agree with mine.

One remark, not a finding.
For s 35 the encoder read Amendment 262 and encoded both texts of (a)(1).
The uniform 2024 gate therefore leaves the old text reachable only in the last months of a pre-2022 immigrant's period (my D050).

## Expectations that could not be expressed through the interface: 49 of 224 scenarios

175 scenarios have at least one assertion; 49 have none.
They fall into three groups.

**(a) Consistent by design (11).**
The encoding takes the fact as an explicit input, or records the fork or inert status my answer accepted:

- D017: retirement age is an input.
- D036: the value of a car is in the item's amount.
- D037: the place of production is an input.
- D065: a class the Minister determined is an input ground.
- D092: the s 38(b) "registered spouse's income" anomaly is noted in F22 and read purposively.
- D122: a single-parent family is an input.
- D200: a designated body is in a field's name.
- D248: a provident fund that is not a pension fund has no field.
- D251: F28 and F29 are recorded.
- D276: s 66(d) income is the caller's.
- D304: s 121A is inert.

**(b) The conclusion the scenario tests is itself an input (24).**
An assertion would only restate the input:

- D001-D003: `has a spouse`.
- D024-D034: the s 2 source, and an expense the employee is allowed, are the caller's classification.
- D083-D085: `proved that the spouse's income was from personal exertion within paragraphs (1) to (6)`. Rent under para (7), or interest, is not classified by the rule.
- D102-D104: one boolean folds together 24 hours a week, 9 months, and a business rather than employment.
- D192 and D247: a child's age is folded into the field name "aged 18 or more".
- D234: insured income is an input number.
- D294: whose child it is goes in a constructor.

**(c) Not represented: no rule, no input and no refusal (14).**

- D004: a date's tax year.
- D014-D016: the definition of income from personal exertion.
- D035: gambling winnings under s 2A. A caller can file them under s 2(10) and get no refusal.
- D109: an election under s 39 that was never made. The boolean's FALSE silently means "chose s 38".
- D120-D121: s 40(a).
- D271: a couple who divorce within the five years. `s 64B(d)(1) — … still stands, unless they cease to be spouses or the Director decides, …` names the exception but takes no input for it, so it answers TRUE for a divorced couple.
- D273: one election displacing another within five years.
- D292: spouses living apart. The s 65 rule has no notion of whether the couple are spouses.
- D293: a separate computation under s 66. The s 65 rule says in its description that it applies where s 66 does not, but it cannot refuse.
- D300 and D303: the value of a credit point. It is an input to ss 35(b) and 38(b); no rule supplies it.

Of these, D109 and D271 are worth noting because they give a confident answer with no diagnostic.
D109 defaults to s 38.
D271 says the determination stands after a divorce.

## Observations made after seeing the encoding (not tests, and not in DECIDED-ANSWERS.md)

These come from reading the rules and probing them after the run.
No assertion in `tests-independent.l4` tests them.

1. **s 40(b)(1A1) moves two points, not one, for a child of one parent.**
   The text, line 1638: `נקודת זיכוי אחת מתוך נקודות הזיכוי שלהן היא זכאית כאמור באותן פסקאות … תובא בחשבון בשנת המס שבה נולד הילד או בשנת המס שלאחריה`.
   The encoding applies the election in both the paragraph (1) points and the (1A)-table points that (1B) adds.
   Take a resident single mother whose child of one parent was born in 2025 (the other parent died).
   Without the election she has 6 points in 2025 and 10 in 2026.
   With it she has 4 and 12, so two points move.
   F13 records that the election reaches (1B)'s (1A) points, but not that the move then doubles.
2. **The D187 cliff** (above) also appears for life insurance as a cliff into refusal.
   5,000 gives 1,250; 5,001 is refused.

## Where the encoding and I agree

190 assertions are satisfied.
Every scenario in these sections agrees:

- s 1: the day-count presumptions, rebuttal and findings (D005-D012, D018).
- s 2: the territorial charge, and s 2(2) as work income.
- s 35: every month count from 2024, the returning-resident window to the day, the absence bounds, and s 35(b) at its exact threshold.
- ss 37-39: all, including the s 38(b) thresholds of 25,410 and 29,040 and the s 39 election.
- s 40(b): all 39 assertions, across (1), (1A) with its proviso, (1A1), (1B) and (2).
- s 47(a): every definition (D220-D233).
- s 47(b) and (b1): the deductions apart from the order question (D235, D240-D243, D245, D246).
- s 45A: D180-D182, D184-D186, D188, D189, D191, D193-D199 and D249.
- ss 64B and 65: all.
- The published 2026 figures: they match the editorial-note figures I chose.

Several of the encoding's recorded forks are the readings I reached on my own before seeing them.
They are F5(i) as a reading, F12, F16 (one additional point; my D165), F22 (my D093), F24 (calendar months), F31 (1 October) and F32 (equal incomes).

## What I read, and in what order

1. `DECIDED-ANSWERS.md`, first and in full. It is the previous session's, and frozen.
2. `BRIEF.md`. The previous session had already read it, as its line 6 records.
3. The `.l4` modules of the encoding: nouns, tax years, published figures, and every rule module, in full.
4. The encoder's own tests modules, only for how inputs are built: the first 33 lines of the s 1-2 tests, lines 20-129 of the s 45A/47 tests, and `grep` output over the s 1-2, s 35 and s 45A/47 tests. That output showed some of the encoder's assertions, with expected values, in passing. None was used, and every expected value in my file comes from `DECIDED-ANSWERS.md`.
5. `check.sh`, for how it counts.
6. After writing and running `tests-independent.l4`, `NOTES.md` in full. It has no section headed "Comparison with Axiom", and I read no other row's `NOTES.md`.
7. Lines 167-169 of the deposited source, to quote the D019 limb exactly (sha256 checked: `b87f2cf4…94b81b6`).

I read nothing under `/Volumes/transcend/src/Axiom/`, any `rulespec-*` directory, any Axiom Foundation material, any `ENCODING-GAPS.md`, `.axiom/`, `data/coverage/tax-benefit-source-map.json`, or anything named `composed/`.
`readlink` showed that the `l4` binary lives under `/Volumes/transcend/caches/cabal/store/`.
That is a build cache, not the forbidden Axiom path, and nothing in it was opened.
