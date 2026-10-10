# Nurses and Midwives Act 1999 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
incorporates "all amendments up to and including 1 December 2021", and it also
shows annotations for Act 11 of 2023 (wef 1 May 2023) and Act 19 of 2025 (wef
5 December 2025, which inserted s 43A and s 42(2A)).

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
nurse, midwife, employer, nursing agency or member of the public actually meets:
who may practise and use the titles (ss 26, 27, 35), employing and placing
unqualified people (ss 28, 29), renewing and surrendering certificates (ss 18,
19(6)), discipline, costs, appeal and re-registration (ss 19, 20, 21, 23), the
smaller time limits (ss 13(3), 16(3), 17(8)) and composition (s 43A). The Board's
constitution, the registration criteria and Board discretions in ss 14, 15 and 17,
Advanced Practice Nurse certification (s 32), inspectors, Complaints Committees,
service, funds, regulations and the transitional Part 7 are not encoded.

## What the Act turns out to say

### 1. Being registered is not enough: a lapsed practising certificate makes you unqualified

s 26(2) defines "qualified nurse" as a registered or enrolled nurse "who holds a
valid practising certificate". So a registered nurse whose certificate has lapsed
commits an offence by calling themselves a nurse (s 26(1)(a), up to $10,000) and by
nursing for reward (s 27). Under s 19(10) a suspended nurse "is not to be regarded
as being registered", so holding a certificate does not save them either. A doctor
is not a "qualified nurse" either, so the title offence reaches a doctor who uses
it. That last point is a literal reading; the encoder did not find any exception
for it. Asserted.

### 2. Unpaid nursing is outside s 27; employing for it is not outside s 28

s 27 bans unqualified nursing and attending childbirth only "for a fee or reward",
and excepts doctors, people helping in an emergency, and supervised students in an
approved organisation. A student midwife's exception covers childbirth only, not
nursing. s 28 has no fee element: it bans employing or engaging an unqualified
person "to carry out any act of nursing", but excepts hiring someone to care for the
employer or "a family member, relative or friend". Asserted.

### 3. The employer's and agent's defence needs both ignorance and due diligence

ss 28(5) and 29(3): the defendant must prove both that they "did not know" the
person was not qualified and that they "had exercised due diligence". A nurse's
agent (a business "arranging the supply of the services of a nurse or a midwife"
for reward) gets no private-carer exception. Asserted.

### 4. The 3-year wait for re-registration does not apply to fraud

s 23(3) bars re-application for 3 years, and more than once in 12 months, only
where the cancellation was on grounds "19(1)(b) to (e)". Read literally, a nurse
struck off for obtaining registration fraudulently (ground (a)) or for disability
(f) may re-apply at once. Whether that is intended is not something the text says.
Asserted.

### 5. Ground (c) carries no costs order; grounds (g) and (h) carry no surrender duty

s 20(1) allows a costs order only on grounds (a), (b), (d), (e) or (f), so not where
the nurse was struck off abroad. The 14-day surrender duty (ss 18(7), 19(6)),
enforced by a $1,000 fine, applies only to grounds (a) to (f), not to non-renewal or
death. Asserted.

### 6. Repeat offenders face prison; first offenders do not

ss 27 to 30: a fine up to $10,000; for "a second or subsequent conviction", up to
$20,000 or 6 months' imprisonment or both. The title offences (ss 26, 35) have only
the $10,000 fine. Asserted for ss 27 to 30.

### 7. Discipline is capped; appeals are short and final

The Board may suspend for at most 2 years and fine at most $2,000 (s 19(2)). An
appeal to the High Court lies within 3 months unless the court allows more (s 21),
and there is no further appeal. A refused applicant has one month to appeal to the
Minister, "whose decision is final" (s 17(8)). Asserted.

### 8. Composition is capped at the lower of half the fine and $1,000

s 43A, inserted by Act 19 of 2025, so for a $10,000 offence the most the Board may
collect is $1,000, and for the $1,000 surrender offence $500. Which offences are
compoundable is left to regulations, which were not retrieved. Asserted.

## What would need doing before this is worth anything

- The model uses one practising-certificate flag for both nursing and midwifery;
  the Act speaks of a certificate "authorising" each.
- The "act of nursing" definition (s 26(2)) is taken as given, not modelled.
- Prescribed exceptions (ss 27(6)(c), 28(4)(c)), the late application fee, the
  "prescribed period" in s 19(1)(g) and the compoundable offences all live in
  regulations, none of which were retrieved.
- "One month" and "3 months" are modelled as whole-month counts; how a month is
  computed is not addressed.
- No case law or Board decisions were searched.
