# Retirement and Re-employment Act 1993 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/7/2022"), as deposited at `../../registers/source-bundle/RRA1993.txt`. The latest
amendment annotated is Act 38 of 2021, with effect from 1 July 2022.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen for its **everyday-life relevance**, not for how often other Acts cite
it. It decides when an employee in Singapore may be retired and whether the employer
must then offer re-employment, which every older worker meets. This row takes:
- the specified age and what counts as a dismissal (s 2)
- the permitted ranges for the two ages (ss 4(1), 7A(11))
- the bar on age dismissal and void retirement terms (ss 4(2), 4(3), 6)
- eligibility for re-employment (s 7)
- the duty to re-employ and the employment assistance payment (ss 7A(1), 7C(1), (3))
- the minimum length of a re-employment contract (s 7A(6), (7))
- where disputes go, the time limits, and the bars between routes (ss 8, 8A, 8B, 8C)
- penalties and composition (ss 4(3), 8(7), 8B(13), 9(2), 9A(2), 9B, 9C, 10)

Not encoded: the officers (s 3), continuing to work past the specified age without
re-employment (s 7A(2), (3)), reckoning of service (ss 7B, 7C(6)), the transfer to
another employer in detail (s 7C(2), (7), (8)), how the Minister or the Tribunal fixes
amounts (ss 8(3), (4), 8B(6), (10), 8C(3)), investigation powers, exemptions,
tripartite guidelines and regulations (ss 9(1), 9A(1), (3), 11, 11B, 12).

## What the Act turns out to say

### 1. The Act does not say what the retirement or re-employment age is

s 4(1) lets the Minister specify the prescribed minimum retirement age by Gazette
notification, "at least 62 years but not more than 65 years". s 7A(11) does the same
for the prescribed re-employment age, 67 to 70. The ages actually in force are in
notifications that were not retrieved, so every age in this encoding is a parameter
and the cases use hypothetical values. Only the ranges are asserted. Asserted.

### 2. The protected age and the remedy age are different ages

The "specified age" is the higher of the prescribed minimum retirement age and the
retirement age in the contract (s 2(1)). The offence in s 4(2) covers dismissal on the
ground of age only before the **prescribed minimum retirement age** ($5,000 or 6
months, s 4(3)). But the remedy in s 8(1) is open to an employee "below the
**specified** age" who considers he or she was dismissed on the ground of age. So an
employee whose contract sets a higher retirement age can ask the Minister for
reinstatement after a dismissal that is not an offence. (That this gap exists is an
inference from the two provisions read together.) Asserted.

### 3. The duty to re-employ gives way only to no vacancy plus a payment or a new employer

s 7A(1) is "Subject to section 7C". Under s 7C(1) the duty falls away only if the
employer cannot find a suitable vacancy "despite making reasonable attempts" **and**
either offers an employment assistance payment or another employer's offer is accepted.
No vacancy alone is not enough. No payment is needed if the employee says he or she
will not continue (s 7C(3)). Eligibility needs birth on or after 1 July 1952, at least
satisfactory performance, and medical fitness, which is presumed unless the employer
proves otherwise on a balance of probabilities (s 7(1), (2)). Asserted.

### 4. Short deadlines, and choosing one route closes the others

The employee has one month: from the dismissal to make representations against an age
dismissal (s 8(1)), and from the last day of employment to notify the Commissioner of a
denial of re-employment or a dismissal without just cause (s 8A(1), (2)). Disputes over
the terms offered or the amount of the payment go to mediation within 6 months, then
the Employment Claims Tribunal (ss 8A(3), 8C(1)). For a dismissed employee,
representations under s 8B, representations under s 35(3) of the Industrial Relations
Act 1960, and a Tribunal claim over the payment each bar the other two (ss 8B(3), (4),
8C(2)). The just-cause route is only for those who reached the specified age on or
after 1 January 2012. "Month" is counted as a whole number here. Asserted.

### 5. s 8B says both "at any time" and "no later than one month"

s 8B(1) lets the employee make representations "at any time after any conciliation";
s 8B(2) requires them "no later than one month after the conclusion of any
conciliation". The encoding follows s 8B(2). Asserted (the one-month limit).

### 6. A re-employment contract is at least a year, unless less is left or agreed

s 7A(6): not less than one year at any one time "unless otherwise agreed". s 7A(7):
shorter if less than a year remains before the re-employment age. Asserted.

### 7. Compounding is capped at $1,000

s 10(1): the lower of half the maximum fine and $1,000. Which offences are
compoundable is left to regulations (s 10(3)), not retrieved. Ignoring a summons and
obstructing an inquiry carry no stated penalty, so s 9C applies: $5,000 or 6 months,
$10,000 or 12 months for a subsequent offence under the same section. Asserted.

## What would need doing before this is worth anything

- Retrieve the Gazette notifications fixing the prescribed minimum retirement age and
  the prescribed re-employment age, and the tripartite guidelines on the payment.
- Retrieve the compounding regulations and any regulations under s 12(2)(d).
- Model months and dates properly instead of whole numbers of months and years.
- No case law, Ministry decisions or Tribunal awards were searched.
