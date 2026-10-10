# Intoxicating Substances Act 1987 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 5
of 2025 (in force 9 March 2025) shown. The arrangement of sections at the head of
the deposit is out of step with the body from s 16 on; the body's numbers are used.

**Checks:** one case file, 109 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**11 of the 527 Singapore Acts** deposited here cite it. This row takes what an
intoxicating substance is, the misuse and supply offences, the blood test and the
presumption it raises, supervision and detention in an approved centre, consent to
body samples, deemed forfeiture, officer liability and protection, and the penalty
for each offence: ss 2 to 4, 10(4), 13, 14, 16, 17, 26A, 26B, 39, 41, 42 and the
Schedule. Informers, arrest, search, investigation, administration of approved
centres, Review Committees, magistrate's inquiries, custody and weapons, the DNA
database and committees of inquiry are not encoded beyond their penalties.

## What the Act turns out to say

### 1. Only toluene counts

An "intoxicating substance" (s 2) is one whose fumes contain "any chemical compound
specified in the Schedule", and the Schedule lists exactly one: toluene, at "1
microgramme per 1 millilitre of blood" (entry annotated Act 5 of 2025). A substance
that intoxicates when sniffed but contains no toluene is outside the Act, including
the supply offence in s 4. Asserted.

### 2. Refusing the blood test can cost less than the misuse it would prove

Misuse (s 3) carries no express penalty, so s 39 applies: $2,000 or 6 months **or
both**. Refusing a blood test without reasonable excuse (s 13(3)) is $2,000 or 3
months, and the text gives no "or to both". If the officer did not warn of the
penalty, the court "may dismiss the charge" (s 13(4)). Asserted. Whether a court
could impose both for s 13(3) under some general provision is not read here.

### 3. The presumption needs the level to be above, not at, 1 microgramme

s 14(1) presumes misuse "until the contrary is proved" if a certified specimen holds
the compound "in excess of" the Schedule amount. Read as strictly greater: 1
microgramme exactly raises no presumption. The certifier must be an HSA analyst or a
Gazetted ministerial appointee (added by Act 5 of 2025). Asserted.

### 4. Voluntary inmates escape the fingerprint and DNA powers; consent rules differ by age

s 26B(2) reaches people convicted under ss 3(2), 4(2) or 13(3), people under a
supervision order, and people in a centre under a s 17(1) order. A voluntary inmate
(s 17(2)) is not listed, nor is someone convicted only of obstruction (s 9). Blood and
prescribed invasive samples need "appropriate consent" (s 26B(5)): the person's own
at 16 or over, both the person's and a parent's at 14 or 15, a parent's alone under
14 (s 26A). Hair and mouth swabs need none, and reasonable force may be used
(s 26B(4)(b)). Separately, a s 13 blood test accepts the person's own consent from 16
(s 13(7)). Asserted.

### 5. Detention is capped three ways

A s 17(1) order detains for up to 6 months; the Review Committee may extend by up to
3 months "at any one time"; and no one is held more than 12 months after admission
(s 17(6)). Voluntary admission is capped at 6 months (s 17(3)); a parent or guardian
can apply only for someone under 21 (s 17(2)(b)). Supervision orders run up to 12
months and, after imprisonment, start when the sentence expires (s 16(3)). Asserted
(except the start date, which is not encoded).

### 6. Supplying is the heavy offence

s 4: selling, supplying or offering, with knowledge or "reasonable cause to believe"
of misuse by the buyer "or by another person", is $5,000 or 2 years or both; "supply"
includes possession for supply (s 2). The heaviest penalty in the Act, though, is
false evidence before a committee of inquiry: $10,000 or 7 years (s 32). Asserted.

## What would need doing before this is worth anything

- **Inference:** s 17(2)(a) does not say who applies; it is read as the person's own
  application at any age. Whether s 17(5) extensions reach a voluntary inmate, given
  the 6-month cap in s 17(3), is not resolved; the encoding applies the cap.
- Below 16 the Act says nothing on consent to a s 13 blood test; the encoding only
  says the person's own consent is enough from 16.
- The supervision-start rule (s 16(3)) and the s 10(1) notice of seizure are not
  encoded.
- No regulations under s 43, no Gazette appointments and no case law were read.
