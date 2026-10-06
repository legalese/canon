# IL-02 — independent test pass: findings

Independent test author fid-il-02, 2026-10-06, following `l4-ide/skills/encoding-a-subject/references/second-pass.md`.
Order of work: decided 101 scenarios from the Hebrew source and froze them in `DECIDED-ANSWERS.md` (finished 14:03:09 UTC); only then opened the `.l4` modules to learn their names; wrote and ran `tests-independent.l4` in a scratch copy; only then read `NOTES.md`.
Before finishing `DECIDED-ANSWERS.md` I had read `BRIEF.md` from the encoding directory and nothing else in it.

## The numbers `check.sh` printed

Run in a scratch copy of the encoding directory with `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset:

```
module                                    errors satisfied  failed  refused  expected
...
ito66-tax-years.l4                             0         3       0        0         0
ito66-tests-ita.l4                             0        23       0        0         0
ito66-tests.l4                                 0       139       0        0         0
tests-independent.l4                           2       101       2        0         0
TOTAL (11 modules)                             2       266       2        0
```

`tests-independent.l4` holds 103 `#ASSERT` directives: **101 satisfied, 2 failed, 0 refused, 2 errors** (the two errors are the two failed assertions; there is no other diagnostic).
The two failures are left failing, so `check.sh` on the encoding directory will now exit 1; that is intended by the second-pass procedure.

A control that the record comparisons are not vacuous: a scratch probe asserting three wrong values (a children's count of 3 for 2½, a 36A half of 0 for ½, a taxable income of 200,001 for 200,000) reported all three as `assertion failed`.

## Failing assertions

### 1. V-4 — the (a)(1) claim is answered for tax year 2023

- **Assertion:** `tests-independent.l4:204`, `#ASSERT REFUSED (s 66(a)(1) — the spouse who is not the registered spouse may claim a separate calculation, for <a couple in tax year 2023>)`.
- **Scenario:** a salaried registered man and a salaried woman who is not the registered spouse and claims under (a)(1), tax year 2023.
- **Provision and words:** the brief, "The text answers tax years from 2024 … For an earlier tax year the encoding does not hold the text, and refuses"; the source shows only s 66 as amended at retrieval, whose amendment list (line 2454) ends at "תשפ״ג־6, תשפ״ד־3".
- **Expected:** a refusal.
- **Encoding answered:** `TRUE`.
- **Classification: encoding error** (the scope of the year gate), not recorded as a fork.
  `NOTES.md` §3 A1 says "For a tax year before 2024 every top-level rule refuses", and §1 lists "whether the spouse who is not the registered spouse may claim, and has made, a separate calculation" among the things the modules answer "for a married couple in a tax year from 2024".
  The gate `in tax year … , the answer is` (`ito66-tax-years.l4:55`) is applied in only three rules: `s 66(a)-(b) — the calculations, for`, `s 66(c) — the credit points it gives the`, and `s 66(c) — in a separate calculation, the … has the entitlement under`.
  My companion assertion through the assembled rule, `tests-independent.l4:205`, refuses as expected.
  A follow-up probe (not a decided assertion) on the same 2023 couple shows **seven of the eleven couple-level rules answer 2023 instead of refusing**:

  | rule | 2023 answer |
  | --- | --- |
  | `s 66(a)(1) — the spouse who is not the registered spouse may claim a separate calculation, for` | `TRUE` |
  | `s 66(a)(1) — a separate calculation is made, for` | `TRUE` |
  | `s 66(d) — subsection (a) applies to` | `TRUE` |
  | `s 66(a)(2) — the spouse to whose taxable income the income not from personal exertion is added, for` | `registered spouse` |
  | `s 66(a)(3) — the children's income deemed the registered spouse's, for` | `0` |
  | `s 66(b) — for … , the property income goes:` | `it is not calculated separately` |
  | `s 66(c) — governs the calculation of the` | `TRUE` |
  | `s 66(c)(4)-(6) — the credit points of the … for` (one child, born 2015) | `2` |
  | `s 66(c) — in a separate calculation, the … has the entitlement under` `section 40(a)` | refuses |
  | `s 66(a)-(b) — the calculations, for` | refuses |
  | `s 66(c) — the credit points it gives the` | refuses |

  Whether the seven are "top-level" is the encoder's call, but each takes a whole `Spouses in a tax year`, carries the year, and answers a question §1 says the row answers; no rule in the row is `@export`ed (`grep -c @export` is 0 in every module), so nothing marks the seven as internal.
  The repair the skill suggests is one line per rule: wrap each couple-level rule in `in tax year (couple's tax year) , the answer is`, or move the gate into a single entry point and say in `NOTES.md` that the others are helpers.

### 2. E-4 — a birth-year point deferred out of 2023 into 2024

- **Assertion:** `tests-independent.l4:385`, `#ASSERT REFUSED (the woman's s 66(c) points, tax year 2024, child born 2023, mother defers TRUE)`.
- **Scenario:** a child of both spouses born in 2023; the mother elected under (c)(4)(a1) to count one birth-year point in the following year; the question is her children's points for 2024.
- **Provision and words:** (c)(4)(a1) "אמו של ילד תהיה זכאית לבחור אם נקודת זיכוי אחת מתוך נקודות הזיכוי שלהן היא זכאית כאמור באותה פסקה, בשנת הלידה, תובא בחשבון בשנת המס שבה נולד הילד או בשנת המס שלאחריה"; the brief, "what it does not show, you do not know".
- **Expected:** a refusal, because the point moved is one of the points the mother was entitled to "under that paragraph, in the year of birth", and the year of birth is 2023, whose text the source does not show.
- **Encoding answered:** `in a separate calculation` with ½ (s 36A), 0 (s 37), **5½** children's points (4½ for a child turning 1, plus the deferred point).
- **Classification: genuine ambiguity, not recorded by the encoder.** My own confidence in this expectation was **L** in `DECIDED-ANSWERS.md`, and on reflection I would not call the encoding wrong.
  For the encoding: the 2024 calculation is governed by the 2024 text, and moving exactly one point needs only that the mother had at least one birth-year point in 2023 and was allowed to elect; the 2024 text then says where it lands.
  Against: whether a 2023 mother could make the election at all, and had a point to move, is 2023 law, and the brief and `NOTES.md` §3 A1 both say the earlier text is not held.
  The fork is at the vintage boundary, between F11 (which only asks whether the election reaches a step-mother) and A1; `NOTES.md` does not mention it.
  The input `the mother elects to count one birth-year credit point in the following tax year` also carries no year, so the encoding cannot tell an election of 2023 from one of 2024.
  Recommended: record it as a fork; either refuse for a 2024 calculation of a child born in 2023 with the election set, or keep 5½ and say that it assumes the 2023 law allowed the election.

## Expectations the interface could not express (12)

Recorded in `DECIDED-ANSWERS.md` ("Revised after seeing the encoding") and as comments in `tests-independent.l4`.

| scenario | why it cannot be expressed | effect |
| --- | --- | --- |
| A1-10, A1-11 (the (a)(1) five-year window at 5 and 6 years) | limb 2 of the pension proviso is a BOOLEAN input, `the spouse was entitled to a separate calculation, in the five years before the pension began, …` | **the edge "בחמש השנים האחרונות" is the caller's, not computed** |
| B-3, B-4, B-5 (acquired 6 months, exactly 1 year, 1 year less a day before marriage) | (b) income arrives pre-sorted into `taxable income from property owned one year before the marriage` | **the edge "שנה לפני נישואיו" is the caller's, not computed** |
| B-6, B-7, B-8 (gift during marriage; bought during marriage; inherited before marriage) | same: no mode or date of acquisition is an input | the (b) qualification is the caller's |
| A3-9 (a child's linkage differentials counted as "interest") | `A child` has one interest field; s 65's "ריבית, דמי ניכיון או הפרשי הצמדה" must be folded into it by the caller | depends on the caller; `NOTES.md` §2 says "interest classified by the caller" |
| A3-7, A3-8 (a child's dividends, a child's employment income) | no field | the encoding agrees by construction (never counted) |
| A3-11 (a child's interest on inherited assets) | no field records an inherited asset | the encoding agrees by construction (F6: no exception) |

**One finding from this table, not an assertion failure.**
The two conditions of (b) ("מרכוש שהיה בבעלותו שנה לפני נישואיו או מרכוש שקיבל בירושה בתקופת נישואיו") and the five-year window of the (a)(1) proviso are s 66's own conditions, not answers of another section, yet the encoding takes their conclusions as inputs.
`NOTES.md` §2 marks 66(b) and 66(a)(1) "encoded", and §1's list of what is not encoded names the classification of income by kind but not these two tests.
I classify it as **an unrecorded scope choice**: defensible, but `NOTES.md` should say that the date edges s 66 itself carries are supplied by the caller, so a reader does not take "encoded" to mean they are computed.

## Where my reading and the encoder's agreed on a recorded fork

Every one of these I decided before reading the encoding; the encoding took the same branch.

| my scenario | my confidence | encoder's fork | branch both took |
| --- | --- | --- | --- |
| D-8 | L | F1 | the (d) gate is on the couple (asserted, but the interface cannot distinguish the readings: see `DECIDED-ANSWERS.md`) |
| A2-5 | M | F3 | equal personal-exertion incomes: refuse |
| A3-2 | M | F15 | a child turning 18 in the year is excluded from (a)(3) |
| A3-10 | H | F14 | the child's (a)(3) income stays on the registered spouse when the pool moves |
| A3-11 | L | F6 | no s 65 inheritance exception (by construction) |
| B-9, B-11 | H | none (the text of (b)) | either spouse may claim (b) ("בן זוג"); without another separate calculation the (b) income stands alone. F7 (a *registered* spouse's (b) income always stands alone) was not among my scenarios |
| C-CAP | M | F13 | the children's credit is capped at the tax on personal-exertion income |
| C-NONE | M | (c) chapeau | with no separate calculation, (c) does not govern |
| R1A-2, R1A-4 | M, L | F18 | (c)(1A) is open to the registered spouse, and "אף אם" is not "only if" |
| S-2, S-4 | H | F12 | a divorced partner's children are not reached by (4A) or (6) |
| E-3 | H | (a1) | the election is the mother's alone |
| R-3 | L | F9 | a same-sex couple: refuse |

Agreement on the L-confidence rows is weak evidence: the encoder and I may share a reading for the same reason, which is the risk `second-pass.md` names.
The ones a domain expert should still settle are F1, F3, F6, F9 and F18, all already in `NOTES.md` §8.

## My own errors, on reflection

None of the 103 assertions turned out to be my error.
One scenario was written loosely: V-2 said "same facts, tax year 2023", which puts a child born in 2024 into 2023; the expected refusal does not depend on the child, and the test asserts it with a child born in 2023 as well.
E-4 is listed above as an ambiguity rather than an encoding error because my own confidence in it was low.

## What I read

`second-pass.md`, `writing-l4-rules/SKILL.md`, `source-patterns/11-when-the-encoding-cannot-answer.md`, the deposited Hebrew source (s 1, ss 33A-40A, 64B, 65, 66, 66A, 66B), and `BRIEF.md`; then the encoding's `.l4` modules except `ito66-tests-ita.l4` (only `ito66-tests.l4` lines 1-90, for the input-supply pattern); then `NOTES.md`.
The rule modules name fork ids F1-F13 in comments, with a one-line gloss of each reading; I read those after my answers were frozen.
Nothing from the Axiom Foundation, no `rulespec-*`, no `ENCODING-GAPS.md`, no `.axiom/`, no `tax-benefit-source-map.json` and no `specs/research/AXIOM-*` was read, searched or fetched. No web access was used.
