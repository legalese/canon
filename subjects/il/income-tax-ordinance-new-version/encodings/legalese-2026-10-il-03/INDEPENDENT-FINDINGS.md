# IL-03 independent findings (fid-il-03)

Independent test pass over `legalese-2026-10-il-03` (ss 120B, 121, 121B), run 2026-10-06 by one session with no sub-agents.
Files: `DECIDED-ANSWERS.md` (91 scenarios, decided from the Hebrew source and stamped 14:02:44 UTC before any `.l4` file or `NOTES.md` was opened), `tests-independent.l4` (126 assertions), and this file.

## What `check.sh` printed

Run in a scratch copy of the directory with `L4=/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset; no file of the encoding was edited.

```
module                                    errors satisfied  failed  refused  expected
ito-120b-indexation.l4                         0         0       0        0         0
ito-121-individual-rates.l4                    0         0       0        0         0
ito-121b-additional-tax.l4                     0         0       0        0         0
ito-il03-nouns.l4                              0         0       0        0         0
ito-il03-tests.l4                              0        86       0        0         0
tests-independent.l4                           6       118       6        2         0
TOTAL (6 modules)                              6       204       6        2
```

`tests-independent.l4`: 126 `#ASSERT` = 118 satisfied + 6 failed + 2 refused.
The 6 errors are exactly the 6 failed assertions; there is no parse or check error.
`check.sh` exits 1, as it must with failures and refusals present; `expected_failed` was not changed, so the encoder's `check.sh` is untouched.

## Failing and refused assertions (8)

Line numbers are lines of `tests-independent.l4`; `L<n>` are lines of the source file.

| # | line | id | scenario | provision and Hebrew | I expected | encoding answered | classification |
|---|---|---|---|---|---|---|---|
| 1 | 267 | D03 | tax year 2026, born 1966-01-02 (60 on 2 Jan 2026), rent 100,000 on the scale | s 121(b)(1), L4354: `ולגבי הכנסה חייבת בשנת המס של יחיד שמלאו לו 60 שנים` (no date for the age test) | REFUSE | `RIGHT 10635.2` (reduced scale for the whole year) | genuine ambiguity, **recorded** (fork F2; NOTES §8 Q2) |
| 2 | 268 | D04 | as D03, born 1966-06-15 | same | REFUSE | `RIGHT 10635.2` | genuine ambiguity, recorded (F2) |
| 3 | 269 | D05 | as D03, born 1966-12-31 (60 on the last day of the year) | same | REFUSE | `RIGHT 10635.2` | genuine ambiguity, recorded (F2) |
| 4 | 284 | F01 | tax year 2026, under 60, wages 60,000 + rent on the scale 60,000 | s 121(b)(1), L4354: `לגבי הכנסה חייבת בשנת המס מיגיעה אישית` with (b)(1)(a) `84,120 השקלים החדשים הראשונים` — which shekels of the scale the personal-exertion income occupies is not said | REFUSE | `RIGHT 24600` (wages at the bottom) | genuine ambiguity, **recorded** (fork F1; NOTES §8 Q1) |
| 5 | 285 | F02 | tax year 2026, under 60, wages 30,000 + business income lacking required books 30,000 | s 121(b)(1)-(2), L4354, L4359 | REFUSE | `RIGHT 12300` | **my own error on reflection**: every placement gives 12,300 (below) |
| 6 | 286 | F03 | tax year 2026, wages −1,000 | s 121(a), L4350 (prices taxable income; s 1 L117 defines it after set-offs) | REFUSE | `LEFT an amount of income is negative` | **my own error on reflection, of mechanism**: the encoding declines by a typed rejection, which is the substance I meant |
| 7 | 371 | S13 | tax year 2025, s 121B amount supplied as 721,560, dividend 900,000 | s 121B(a), (a1), L4456-L4457; amendment tag `תשפ״ה־2` at L4455; note `(נקוב לשנת 2025; ...)` at L4462 | `RIGHT 8922` | refused: `section 121B for tax years before 2026 is not encoded in this model` | genuine ambiguity, **recorded** (assumption A1; NOTES §8 Q4) |
| 8 | 384 | S25 | tax year 2025, wages 600,000 + residential sale, betterment 200,000, sale value 5,385,286, not exempt | s 121B(e), L4462: `רק אם שווי מכירתה עולה על 5,385,285 שקלים חדשים {{ח:הערה|(נקוב לשנת 2025; ...)}}` | `RIGHT 2353.2` | refused, same message | genuine ambiguity, recorded (A1, Q4); see observation O1 for an inconsistency it exposes |

Rows 7 and 8 are counted by `check.sh` as **refused**, not failed: the expression refused where I asserted a value.

### Notes on each

**1-3, the age-60 date (F2).**
The text attaches "has reached 60" to the individual and "in the tax year" to the income, and names no date for the age.
The encoder took "60 on or before 31 December of the tax year" (`aged 60 or more by the end of the tax year`, `ito-121-individual-rates.l4:203`), which is the most favourable of the three readings it lists.
The stake is large and lands on one day: in D05 one day at 60 moves 100,000 of rent from 31,000 to 10,635.20, a difference of 20,364.80.
I would have declined (as the brief asks where the sources do not answer); the encoder answered and recorded the fork.
D01, D02 (60 on 1 January 2026) and D06 (60 on 1 January 2027) agree with the encoding under every reading and pass.

**4, the stacking of mixed income (F1).**
The three placements give three answers for F01: personal-exertion income at the bottom 24,600 (the encoding); other income at the bottom 26,035.20; pro rata 25,317.60.
The encoder's reason for (i) in the fork register overstates the case against (ii): it says that under (ii) "the reduced rates would never reach an individual with other income above 84,120, which empties (b)(1) for exactly the mixed case it names".
Under (ii) only the 10% band is lost once other income passes 84,120; the personal-exertion income still takes 14%, 20% and the reduced 31% in whatever bands it occupies, and (b)(1) is emptied only when other income reaches 301,200.
That does not make (i) wrong, and it may match practice, but the argument in F1 is weaker than written.

**5, F02 — my error.**
Wages of 30,000 sit inside the 10% band whether they occupy positions 0-30,000 (reading (i)) or 30,000-60,000 (reading (ii)), and pro rata gives the same; the unbooked trade income is at 31% in every reading.
So the source does answer, 12,300, and the encoding's answer is right. I applied R0.6 more widely than the facts required.

**6, F03 — my error, of mechanism.**
I wrote REFUSE meaning "s 121 does not price a negative amount"; the encoding returns `LEFT` with a named problem, which a caller can fix. Same substance, different route; the encoding's route is the better one for invalid input.

**7-8, s 121B in tax year 2025.**
My expectation rests on the residential note "(נקוב לשנת 2025)" and on 2025 being the first freeze year; neither is text stating from which tax year the 5785 amendment (which added (a1)) applies.
The encoder declines every year before 2026 and asks the question in NOTES §8 Q4.
I keep the expectation visible and do not claim the encoding is wrong.

## Expectations that could not be expressed through the interface (5)

| id | expectation | why it cannot be asserted | status |
|---|---|---|---|
| S11 | no s 121B(a) amount supplied → REFUSE | the amount is a required argument of `the additional tax under section 121B for … , with the amount in section 121B(a) at …`; the case cannot be posed | satisfied by the types |
| S12 | 640,000 must not be applied as the threshold in 2025-2027 | a negative claim about the code | checked by reading: `the amount printed in section 121B(a), as at 2017` (`ito-121b-additional-tax.l4:39`) is defined and no rule reads it; `640_000` and `721_560` occur nowhere else in the rule modules |
| I11 | 2028, caller holds only the ROUNDED 1 January 2024 figure → REFUSE | `An amount on 1 January of a tax year` requires both the before- and after-rounding 2024 figures for every year | see observation O2 |
| S31 | s 121B(c), "notwithstanding any enactment" | inert in the encoding (no other enactment to override) | agrees with my reading |
| S32 | s 121B(d), s 8(c) spreading applies | an input convention on `amount` (`ito-il03-nouns.l4:26`) | agrees with my reading |

## Observations from reading the encoding (not assertions)

**O1. The 2025 residential threshold is unreachable, and its helper disagrees with its section.**
`the text fixes the residential-apartment sale value for tax year` answers 2025 and 2026 (`ito-121b-additional-tax.l4:67-69`), and NOTES §5 tabulates 5,385,285 for 2025, so the encoder accepts the note "(נקוב לשנת 2025)" as showing the 5785 text applies in 2025 for s 121B(e).
But `the additional tax under section 121B for` refuses every year before 2026 at its first arm (`:217-218`), so the 2025 arm is reachable only by calling the helper directly.
Either the note is good enough to answer 2025 (and S13/S25 should compute) or it is not (and the helper should decline 2025 too). The current state reads the same note both ways.

**O2. A silent failure in the s 120B record.**
For 2028 the answer depends only on `amount on 1 January 2024, before rounding` (`ito-120b-indexation.l4:169`).
A caller who holds only the published, rounded 2024 figure must still fill that field, and if they put the rounded figure in it the encoding returns a plausible 2028 amount with exit 0 and no warning.
For 2029 onward both 2024 fields are required and unused.
A `MAYBE` on the before-rounding field, refusing 2028 when it is `NOTHING`, would turn this from silent to loud.

**O3. Where an independent reading agreed with a recorded fork.**
My pre-encoding readings matched the encoder's choice on F3 (C05: (b)(2) reaches the over-60 limb), F4 (I04: a falling index lowers the amount), F5 (I10: 2028 restart by the 2027 rise only, no catch-up), F9 (S24: the exemption condition sits in the residential limb), F13 (I09: 2027 is frozen), F14 (S02, S22: "exceeds" is strict), F15 (S27: betterment is capital-source income), F16 (A12: continuous brackets), F17 (I16: no s 120B(b) adjustment in a freeze year), and A1/A3 for s 121 (2026-2027 answered; 2023, 2024, 2025 and 2028 declined).
Two readers arriving at the same choice is evidence, not proof; F4 and F5 in particular remain readings of a term ("שיעור עליית המדד") and a clause ("המדד של שנת המס 2027") that a court could read otherwise.

## Candour

- I did not open `NOTES.md`, any `.l4` file, `encoding.json`, `check.sh` or `tools/` before `DECIDED-ANSWERS.md` was stamped. I did read `BRIEF.md` first, as permitted; its framing ("what they do not show, you do not know"; the tax year as vintage selector) shaped my year-scope expectations (E01-E05, I14, S14), so those agreements are less independent than the rest.
- After stamping, to learn how inputs are supplied, I read the first 90 lines of `ito-il03-tests.l4` (fixtures) and ran a grep over it that displayed about a dozen of the encoder's assertions with their expected values (s 121 boundaries and named refusals). None was reused; every value in `tests-independent.l4` is from `DECIDED-ANSWERS.md`.
- I read nothing under the Axiom or RuleSpec paths the brief excludes.
