# Mental Health (Care and Treatment) Act 2008 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (it labels itself as
incorporating amendments up to 1 December 2021), with later amendments shown to
Act 16 of 2024 (in force 1 January 2025, s 7).

**Checks:** one case file, 59 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes what a police
officer, doctor, carer or institution actually meets: police apprehension (s 7),
producing a person for police inspection (s 8(3), (4)), the ladder of detention
orders (ss 10, 13), who must not sign (s 11), discharge (ss 12, 14), leave and
retaking (s 15), offences against patients (s 22), protection of those acting under
the Act (s 25), improper detention (s 26), the penalty caps and composition (s 30).
Designation and management of institutions, visitors' inspections, transfers and
removal from Singapore, and maintenance orders are not encoded.

## What the Act turns out to say

### 1. Involuntary detention is a four-rung ladder: 72 hours, 1 month, 6 months, 12 months

A designated medical practitioner's Form 1 order allows 72 hours (s 10(1)). A
**different** designated medical practitioner, examining before the 72 hours end,
can extend by one month (Form 2, s 10(2)). Before that month ends, two designated
medical practitioners, **one a psychiatrist**, examining **separately**, can
authorise up to 6 months (Form 3, s 10(3)-(5)). Beyond that, the visitors must apply
to a Magistrate, whose order lasts up to 12 months and may be sought again
(s 13(1)-(3), (6)). Asserted.

### 2. A police officer must apprehend; danger to oneself is enough, and nothing need be imminent

s 7(1) makes apprehension a duty, not a power. Since Act 16 of 2024, a reasonable
belief that a person is endangering their **own** life or safety is by itself a
sufficient basis for suspecting a mental disorder (s 7(2)(a)), and the danger need
only be "reasonably likely", "need not be imminent", and "actual harm is not
required" (s 7(2)(aa)). Asserted.

### 3. The treating doctor may not sign any order, and the family bar is narrower than "relative"

s 11 bars a practitioner who is treating the patient, who stands in a fiduciary
relationship, or who is the spouse, parent, child, sibling or one of their in-laws.
Grandparents, grandchildren, uncles, aunts, nephews and nieces, all "relatives" under
s 2, are not barred. Asserted.

### 4. Sex with a patient in the institution is an offence for anyone, and consent rarely helps

s 22(5) is not limited to staff: "any person". Consent is no defence if the accused
knew or had reason to suspect the person was a patient (s 22(6)). Maximum $20,000 or
10 years. Ill-treatment by staff (abuse, wilful harm, or wilful neglect including
failing to provide food, clothing, medical aid or care) carries $5,000 or 4 years,
rising to $20,000 or 7 years where death is caused (s 22(7)). Reading consent as a
defence where the accused had no reason to suspect is an inference from s 22(6).
Asserted.

### 5. Visitors' leave has a 28-day grace; the principal officer's does not

A patient on leave from two visitors may be retaken only if not back within 28 days
of the end of the absence and no discharge certificate has arrived (s 15(3)). Leave
from the principal officer (at most 6 months) ends with no grace: a patient not back
"upon the end of the period" may be retaken (s 15(4)). Applying the s 15(2)
certificate only to visitors' leave is an inference. Asserted.

### 6. Acting under the Act is protected unless in bad faith or without reasonable care

s 25 shields anyone acting under the Act from civil or criminal liability unless they
acted in bad faith or without reasonable care, and no proceedings may be brought
without the court's permission, given only on "substantial ground", with notice to
the person. Asserted.

### 7. Smaller rules

Refusing to produce a person for inspection by a police officer of sergeant rank or
above: fine up to $4,000, no imprisonment (s 8(4)); the restriction to the
subsection (3) officer is an inference. Detaining 2 or more mentally disordered
persons for gain outside a psychiatric institution is an offence (s 26(1)(b)), with
prosecution needing the Public Prosecutor's consent (s 26(2)). Prescribed offences
may be compounded for up to $2,000 (s 30). Rules may carry up to $5,000 or 6 months
(s 32(3)). Asserted, except the consent requirement.

## What would need doing before this is worth anything

- Which offences are "prescribed as compoundable" (s 30) and the rules on restraint
  and seclusion (s 32(2)(a)) are in subsidiary legislation, which was not retrieved.
- The months-and-hours periods are returned as labels; computing actual expiry from
  a signing time (and "one month" from the end of 72 hours) is not encoded.
- The voluntary route (s 6(2)), the interaction with the Criminal Procedure Code
  admissions (s 28) and the Mental Capacity Act 2008 (s 29) are untouched.
- No case law was searched.
