# Adoption of Children Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 20 of 2022, informal consolidation, version in force from
15/10/2024, as deposited at `../../registers/source-bundle/ACA2022.txt` (retrieved
2026-10-01). It is not a 2020 Revised Edition Act. The only amendment annotation in
the body is "[Act 31 of 2022 wef 15/10/2024]", at s 66. The arrangement of sections
at the top of the deposit runs two numbers behind the body; the encoding follows the
body.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
prospective adopter, birth parent, adoption agency or publisher actually meets: who
may apply and the exceptions (ss 4, 5), which child (s 6), briefings and the ASA
(ss 11, 14, 20), service and consent (ss 25, 26), dispensing with consent (s 37),
what the court must be satisfied of (s 42), confidentiality (s 48), payments
(ss 53, 55), placement before an ASA (s 57), and the maximum penalties. Not encoded:
the Guardian-in-Adoption's role and affidavit, ASA variation and appeals, interim
and ancillary court powers, the detail of ss 38 to 41, the effects of an order
(ss 44, 46, 47), s 51, enforcement powers, Part 8 and the transitional provisions.

## What the Act turns out to say

### 1. Being the child's relative does not cure the bar on a man adopting a girl alone

s 5(1)(c) makes a sole applicant ineligible where he "is a male and the child before
the court is a female". The consanguinity exception in s 5(2)(a) applies only "in a
case where subsection (1)(a) or (b) applies" (the age bars). Read literally, a male
relative applying alone for a girl can only rely on special circumstances under
s 5(2)(c), even though s 23(2) contemplates a father adopting his own child.
Asserted (a 40-year-old male relative with a baby girl fails without special
circumstances).

### 2. Special circumstances do not let a married person apply alone

s 4(2)(b) allows a sole application only by someone "who is not an individual
mentioned in subsection (1)(a)", that is, not married. The special-circumstances
exception in s 5(2)(c) reaches s 5(1) and the residence requirements of
s 4(1)(a)(iii), (iv) and (b), but not s 4(2). Only s 5(2)(b) helps a married sole
applicant: the spouse consents, or that consent is dispensed with because the spouse
cannot be found or is incapable, or the couple are permanently separated. Asserted.

### 3. Every payment by an applicant is void unless a court sanctions it

s 53(2): every payment or reward "in consideration of the adoption of a child or for
any adoption-related service" made or received by the applicants, and every
agreement for one, "is void and unenforceable" unless the court sanctions it or the
application is withdrawn or struck out. The section draws no line between payments
that s 55 permits (such as an authorised agency's briefing fee) and those it
forbids. Sanction must be sought "at the time that the adoption application is
made" (s 53(3)). Asserted.

### 4. The identification ban lasts for life, and the adoptive parent's say ends at 21

s 48(1) forbids identifying a person as the subject of an adoption application
"even after the protected person attains 21 years of age", whether or not an order
was made. Under 21, the adoptive parent (if the application succeeded) or a relevant
person (if it failed) can consent; from 21, only the person concerned or the
Guardian-in-Adoption. The fine is up to $5,000, or $10,000 for a repeat conviction,
with no imprisonment. Asserted.

### 5. Living with a child before holding an ASA is a 3-year offence, and "potential adopter" is wide

s 57(1) bars a potential adopter from residing with, or spending time with, a child
for whom an adoptive parent is being sought unless he or she holds a valid and
favourable ASA (plus, for a child who is not a citizen or PR, a dependant's pass for
adoption or its in-principle approval). "Potential adopter" (s 57(11)) includes
anyone who has merely told a relevant person that they want to adopt the child.
Relatives within the prohibited degrees, step-parents, CYPA care-givers and cases the
Guardian-in-Adoption permits are exempt. The maximum is $10,000 or 3 years, then
$20,000 or 6 years. Asserted.

### 6. The bars on who may adopt

s 5(1): an applicant must be at least 25 and at least 21 years older than the child,
and must not have a conviction for an offence prescribed by regulations. s 4: a
couple must both be habitually resident, with at least one citizen or both permanent
residents; a valid and favourable HSR from before s 11 commenced lifts those
residence requirements (s 4(3)). The child must be under 21, resident (a visit,
student or special pass does not count, however often renewed) and never married
(s 6). Asserted.

### 7. Consent has five formal conditions, and can be dispensed with on nine grounds

s 26(2): consent must follow the prescribed information, be in writing in the
prescribed form, be witnessed by two witnesses present together who are each at
least 21, follow prescribed procedures, and be attested. s 37 lists the grounds for
dispensing with it; the ill-treatment and failure-of-care grounds look back to before
a "specified period" of 12 months (child under 3) or 24 months (3 or older). Asserted.

## What would need doing before this is worth anything

- The regulations under s 75 (prescribed offences in s 5(1)(d), suitability factors
  in s 7, consent forms and information in s 26, payments prescribed under
  s 55(2)(c), exemptions under s 57(4)(d)) were not retrieved.
- "Within the last 3 years" (s 11) is read as at most 36 whole months, and the ASA's
  2-year validity as fewer than 24 months since issue; both are inferences about the
  boundary.
- The validity of the marriage (s 4(1)(a)(i), (ii)) is assumed for joint applicants.
- Findings 1 and 2 are literal readings; no case law on s 5(2) was searched.
- Sections 38 to 41 (meaning of ill-treatment, care or protection, emotional abuse)
  were read only in part.
