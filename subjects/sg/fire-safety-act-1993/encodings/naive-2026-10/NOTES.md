# Fire Safety Act 1993 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit
(`FSA1993.txt`) labels itself "version in force from 18/12/2023"; the latest
amending Act annotated in the body is 40/2019. Section numbers here follow the
body: the arrangement of sections at the top of the deposit is out of step with
it (for example, the arrangement lists "False alarm" against 23; the body
section is 25).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes the
offences that an occupier, building owner, contractor or member of the public
actually meets: specified fire hazards (s 2, ss 26, 27), abatement notices
(s 28(5)), hydrants and false alarms (ss 24, 25), fire certificates (s 35),
at-risk premises and who counts as owner or occupier in Part 3 (ss 38(5), 40),
alarm monitoring cancellations (s 53), fire safety works, supervision, revoking
a fire safety certificate and change of use (ss 56, 58, 60, 61), and the
penalty machinery (ss 101, 107). Registered inspectors and fire safety
engineers, powers of entry, emergency abatement and closure, Emergency
Response Plans, regulated fire safety products and the petroleum licensing
scheme are not encoded.

## What the Act turns out to say

### 1. The owner's offence is strict; everyone else's needs knowledge

s 26(1) makes an owner or occupier guilty if he "causes, or does or omits to do
anything that is likely to cause" a specified fire hazard, and (4) declares it
"a strict liability offence": intent need not be proved. s 27, the offence for
**any** person who disables a fire safety measure or obstructs an escape route,
requires that the person "knows or ought to know" of the effect. Asserted.

### 2. An obstruction someone fleeing can easily move is not an s 27 offence

s 27(b) requires the obstruction to be one that might make escape more difficult
**and** that "cannot be easily removed by an individual escaping from a fire".
The definition of specified fire hazard in s 2 has no such limb, so the same
obstruction may still be a hazard for which the owner answers under s 26.
Asserted (s 27 limb; the overlap with s 26 is an inference).

### 3. Most of the everyday offences carry only the general penalty

ss 26, 27, 28(5), 35(4), 37(6), 38(6) and 85(1) state no penalty, so s 107
applies: $10,000 or 6 months or both, and $1,000 a day for a continuing offence.
The stated penalties are much heavier for building works: $200,000 or 2 years
for unapproved fire safety works (s 56) or an unapproved change of use (s 61),
and the same for unsupervised works (s 58) but with a **$2,000** daily rate,
twice the others. A false alarm, including "a false call for the ambulance",
is $5,000 or 3 months (s 25). Asserted.

### 4. Composition is capped at the lower of half the fine and $5,000

s 101(1): only offences prescribed as compoundable, for "a sum not exceeding
the lower of" half the maximum fine and $5,000. A false alarm compounds for at
most $2,500; anything with a fine of $10,000 or more for at most $5,000. Which
offences are prescribed was not retrieved. Asserted.

### 5. The strata exclusion is confined to Part 3

s 40 says that "In this Part" (Part 3: fire certificates, Emergency Response
Plans, fire safety managers) the owner or occupier of a strata-subdivided
building does not include subsidiary proprietors or tenants. Part 2, which
holds the s 26 owner-or-occupier offence, has no such provision. Asserted on
the text; whether a court would read Part 2 the same way is not known.

### 6. No knowledge needed to commit the fire certificate offence

s 35(5)-(6): occupying, using, or permitting the use of a designated building
without a fire certificate is strict liability; the prosecution need not prove
the defendant "knew that there was no fire certificate". Which buildings are
designated is left to Gazette notification. Asserted.

### 7. Revocation needs a notice and a failure first

s 60(9): the Commissioner "must not revoke" a fire safety certificate unless a
written notice to comply was given and the person failed or refused, and (12)
the revocation takes effect on a date "not less than 14 days" from written
notification. Asserted.

## What would need doing before this is worth anything

- The Fire Safety regulations (which offences are compoundable, which buildings
  need a fire certificate, which premises need fire safety managers) were not
  retrieved.
- The offence enumeration in the penalty table is a selection; the petroleum,
  product and registration offences are mostly not in it.
- Day arithmetic for s 60(12) treats dates as day numbers; no calendar rules.
- No case law was searched.
