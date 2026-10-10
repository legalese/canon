# Inland Revenue Authority of Singapore Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text, following the
`writing-l4-rules` conventions of the example rows (the skill itself was not
loadable in this session). No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (incorporating amendments
up to 1 December 2021), with later amendments annotated, the latest seen being
S 589/2026 (wef 11 September 2026). Part 5A was inserted by Act 11 of 2024 (wef
1 November 2024).

**Checks:** one case file, 57 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**8 of the 527 Singapore Acts** deposited here cite it. Most of the Act sets up a
statutory board — incorporation, functions, staff, finance, the 1992 transfer from the
Inland Revenue Department — with little decision content. The part an ordinary
business meets is Part 5A (Scheduled public schemes: wage credits, the Jobs Support
Scheme, rental support, the SME Cash Grant 2026 and others): recovery of grants
wrongly given, the false-information offences, investigation notices and arrest.
This row takes Part 5A's decision points plus ss 10, 25, 27, 28, 28A, s 5 and the
First Schedule's membership and quorum rules. Not encoded: functions and powers,
staff, finance, transfer provisions, entry and search in detail, restraint, informer
protection, service and electronic service, regulations.

## What the Act turns out to say

### 1. Three tiers of false-information offence, and the lowest has no fault element

s 17F(1) makes it an offence to give a public agency information "false or misleading
in any material particular", or to omit a material particular, to obtain a scheme
grant. No mental element is stated. The consequence is a penalty equal to the
amount not entitled to, with no fine or imprisonment (s 17F(2)). Negligence or no
reasonable excuse (s 17F(3)) doubles the penalty and adds up to $5,000 or 3 years;
wilful intent (s 17F(5)) trebles it and adds up to $10,000 or 3 years. The penalty
runs on the grant actually given or that "would have been given ... had the offence
not been detected". Reading s 17F(1) as strict liability is an inference from the
absence of a fault element. Asserted.

### 2. Only the wilful tier is arrestable without warrant

s 17I(1)(a) lets the chief executive officer or a specially authorised officer arrest
without warrant for "any offence under section 17F(5)" — not (1) or (3) — or anyone
destroying, deleting or resisting the taking of evidence. Detention must not exceed 48
hours, excluding the journey to the Magistrate's Court (s 17I(6)). Asserted.

### 3. Recovery reaches back before the 2024 amendment

s 17A applies to grants given "before, on or after" the commencement of the 2024
amendment, so wrongly given wage credits or Jobs Support payments from earlier years
can be recovered as a debt due to the Government (s 17B). Notice gives 30 days or any
later time allowed (s 17C); daily interest at the prescribed rate runs from the end of
that period until payment in full (s 17D); the Authority may remit or refund (s 17E).
The prescribed rate was not retrieved. Asserted (days only).

### 4. A Town Council is not a "public agency"

s 17F(7) defines public agency to include public authorities established under a public
Act "(other than a Town Council)", so false information given only to a Town Council
falls outside s 17F. Asserted.

### 5. Most duties of secrecy are displaced, but not statutory ones

Under s 17H a person may withhold information covered by legal privilege or by
another statutory secrecy obligation — but expressly not the Evidence Act ss 128,
128A, 129 and 131 obligations (s 17H(7)). Any other duty of secrecy is no defence
(s 17H(16)), and good-faith compliance is protected (s 17H(17), (18)). Treating a
contractual confidence as a displaced duty is an inference from "a duty of secrecy".
Asserted.

### 6. Composition is capped at the lower of half the exposure and $10,000

s 28A(1): a prescribed compoundable Part 5A offence may be compounded for not more than
the lower of half "the maximum fine prescribed and penalty payable" and $10,000.
Adding fine and penalty before halving is a reading of those words. Which offences are
prescribed compoundable was not retrieved. Asserted.

### 7. Ignoring a notice costs up to $10,000 plus $100 a day

s 17G(2) and s 17H(13): up to $10,000 or 12 months or both, plus up to $100 for every day
the offence continues after conviction. A s 17H(8) notice gives 21 days unless the
officer sets another period (s 17H(9)). Asserted.

### 8. Protection from suit, secrecy and the board

The Authority cannot be sued over any tax it collects as the Government's agent
(s 25); officers are protected for good-faith acts (s 10). Unauthorised disclosure by
staff is an offence ($2,000 or one year, s 27); so is using a confusingly similar
symbol ($2,000 or 6 months, s 28). The Authority has a Chairperson and 5 to 10 other
members (s 5); 5 members form a quorum (First Schedule para 11(2)); a bankrupt or a
person sentenced to 6 months or more without a free pardon is disqualified (para 9).
Asserted.

## What would need doing before this is worth anything

- The prescribed interest rate (s 17D) and the list of compoundable offences (s 28A)
  are in regulations not retrieved.
- The terms of each Scheduled public scheme, which decide entitlement, are outside the
  Act and were not read.
- Entry, search and restraint powers (s 17H(1)-(6), s 17J) and informer protection
  (s 27A) are not encoded.
- No case law or IRAS guidance was searched.
