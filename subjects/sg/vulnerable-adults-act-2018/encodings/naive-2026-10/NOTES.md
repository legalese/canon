# Vulnerable Adults Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/VAA2018.txt`. The edition says it incorporates all
amendments up to and including 1 December 2021. Later amendments are annotated in the
text. The latest is Act 21 of 2023 (wef 2 January 2025).

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row covers the points a
family member, caregiver, doctor, publisher or social worker would meet:

- who is a vulnerable adult, and what counts as a working day (s 2)
- removal, and the 14-working-day duty that follows it (ss 10, 11)
- who may apply for which court order (s 12), and when the judge sits with advisers (s 13(6))
- committal periods and the residence clean-up order (s 14(1)–(3))
- penalties for breaching an order (s 14(10)) and for an identifying publication (s 22(6))
- how long an expedited order lasts (s 15), and offence versus contempt (s 16)
- treatment without consent (s 18)
- protection for people who give information (ss 9(4), 23(2))

Assessment and entry powers, the Review Board, designation of places, information
sharing between agencies, enforcement powers, arrest, service and the rule-making
powers are not encoded.

## What the Act turns out to say

### 1. A capable adult's refusal binds the State, until a court says otherwise

Under s 10(1) the Director-General or a protector may remove a vulnerable adult on
reasonable grounds of abuse, neglect or self-neglect. That needs one of three things:
the adult consents while someone else is preventing removal, a mental capacity
assessor finds that the adult lacks capacity to consent, or there is a court order
under s 10(4). A capable adult who refuses cannot be removed without that order. A
donee's or deputy's consent is not needed (s 10(2)). Asserted.

### 2. Being old and frail is not enough. The test is incapacity to protect oneself

To be a "vulnerable adult" under s 2, a person must be 18 or older and, "by reason of
mental or physical infirmity, disability or incapacity", be incapable of protecting
himself or herself from abuse, neglect or self-neglect. Age alone does not qualify
anyone. Asserted.

### 3. Who may apply depends on the adult's capacity, and the lists do not overlap neatly

Under s 12(2) the Director-General or a protector may apply for any order. Everyone
else may apply only for the personal protection orders: s 14(1)(e)–(h) and the s 15
expedited order. Who counts as "everyone else" depends on capacity:

- **Adult assessed to lack capacity to consent to the application:** an approved
  welfare officer, a donee or deputy, or a family member may apply. No consent is
  needed.
- **Any other case:** a welfare officer or family member needs the adult's consent,
  and the adult may apply on his or her own. The donee or deputy is not listed.

So a donee cannot apply for a capable adult, and an adult assessed as incapable
cannot apply alone. Family members can never seek committal. Asserted.

### 4. The State has 14 working days, and Saturdays count

Under s 11(1)(b), after a removal the Director-General or protector must apply to
court within 14 working days, unless the adult has already been allowed to return.
If a s 12 application cannot be made in time, s 11(2) requires an interim custody
application within the same period. s 2 says a "working day" excludes any Sunday and
public holiday. Saturdays are therefore working days. That conclusion is an inference
from what the definition leaves out. Asserted.

### 5. "Necessary for protection and safety" opens the residence clean-up order

Under s 14(2), an order to make a residence safe (s 14(1)(j)) needs the consent of
the adult and of every owner. Where the owners cannot be located, it needs the
adult's consent and a lapsed advertisement period instead. s 14(3) lets the court
dispense with either consent if the person lacks capacity, or if the court thinks
the order "necessary for the protection and safety of the vulnerable adult". Every
order already requires necessity under s 12(1)(b) and s 14(1). Whether the s 14(3)
exception therefore swallows the consent rule is an inference this row flags and
does not resolve. Asserted as encoded.

### 6. An expedited order lasts at most 28 days, unless extended

Under s 15(3) an expedited order runs from service. Under s 15(4) it ends on the
earlier of 28 days after it was made and the decision on the s 12 application. The
court may extend it (s 15(5)). This row reads an extension as displacing both limbs
of (4), which is an inference. Asserted.

### 7. Breaching a protection order: up to 18 months on a repeat

Under s 14(10), as amended by Act 21 of 2023, the maximum on a first conviction is
$10,000 or 12 months, and on a second or subsequent conviction $10,000 or 18 months.
s 16 prevents punishing the same breach both as an offence and as a contempt. An
identifying publication under s 22(6) carries a fine only: $5,000, or $10,000 on a
repeat conviction. Asserted.

### 8. A doctor may treat without consent in only two cases

Under s 18(2), treatment needs the adult's consent unless one of two conditions holds:

- a mental capacity assessor has found that the adult lacks capacity to consent, and
  the practitioner reasonably believes the treatment is in the adult's best
  interests; or
- consent is impracticable to obtain, the practitioner reasonably believes there is
  an emergency, and the practitioner considers the treatment to be in the adult's
  best interests.

Best interests alone never override a capable refusal. Asserted.

### 9. Reporting voluntarily needs more care than answering a direction

A person who notifies voluntarily under s 23 is free of civil and criminal liability
only if they acted "with reasonable care and in good faith" (s 23(2)(b)). A person
who gives information because a direction under s 9 required it needs good faith
alone (s 9(4)(b)). Asserted.

## What would need doing before this is worth anything

- The definitions of abuse, neglect, self-neglect and wellbeing are taken as a single
  yes/no input, not encoded.
- The text before the Act 21 of 2023 amendments was not retrieved, so the earlier
  s 14(10) penalties are unknown.
- Family Justice Rules and regulations (the "prescribed period" in s 14(2)(b)) were
  not retrieved.
- No case law was searched.
- How s 14(2) and (3) combine, and how far a s 15(5) extension reaches, are
  inferences.
