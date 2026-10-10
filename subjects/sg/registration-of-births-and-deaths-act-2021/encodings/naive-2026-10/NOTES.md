# Registration of Births and Deaths Act 2021 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 17 of 2021, informal consolidation ("version in force from
30/9/2026"), with amendments by Act 2 of 2024 (16 April 2024), Act 20 of 2022
(15 October 2024) and Act 16 of 2026 (30 September 2026) shown. This Act has no
2020 Revised Edition; it post-dates it.

**Checks:** one case file, 108 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes what an
ordinary person, doctor, hospital or ship's or aircraft's master meets: who must
report a birth, death or stillbirth, to whom, the 42-day duty to give birth
particulars, the rules on a child's name, the definition of a stillborn child,
registering a citizen's or PR's death abroad, the false-statement offence, and the
maximum penalties (ss 2(1), 7, 8, 10, 19-23, 26, 28, 32, 33, 35, 42, 48, 51).
Administration, the Registrar-General's own registration duties, adoption,
legitimation and assisted-reproduction re-registration, corrections and
cancellation, investigation powers and register and certificate offences are not
encoded.

## What the Act turns out to say

### 1. Parents of a child born in hospital have no duty to report the birth — but do have a duty to give the particulars

s 7(2)(a): for a birth in a hospital, the people responsible for reporting are
"every medical practitioner who attends to the birth, and the hospital". Parents are
listed only for births in other premises, in conveyances and elsewhere. But s 8
puts the separate duty to give the birth particulars within 42 days on "every parent"
or a legal guardian, not on the doctor or hospital. A home birth is reported by the
parents and the occupier who knows of it; if the baby is brought to hospital within
24 hours, the hospital and its doctors become responsible as well, without releasing
the parents (s 7(3)). Asserted.

### 2. Who you report to depends on where it happened

A birth goes to the Registrar-General (ss 7(4), 10(4)). A death or stillbirth in
Singapore that is not a reportable death goes to "a medical practitioner" (ss 22(3),
32(3)), who must examine the body and send the particulars to the Registrar-General
within 24 hours (ss 23(2), 33(1)(b)). A death or stillbirth on an aircraft, vessel or
train bound for Singapore goes "to the police" (ss 26(3), 35(3)). Section 22 applies
only where the death "is not, or does not appear to be, a reportable death"; s 31
leaves the Coroners Act duties untouched. Asserted.

### 3. In a hospital, the hospital alone reports a death; outside, the circle widens

s 22(2): a hospital death is reported by the hospital. In other premises, by a
relative present at the death and an occupier who knows of it. In "any other place",
by every relative who knows, every person present, and every person who takes charge
of the body — so a bystander at a street death is responsible, but a bystander in a
house is not. s 32(2) repeats the list word for word for stillbirths. Asserted.

### 4. A child's name can be changed once, in the first year, while the child lives

s 21: a name entered at registration may be altered on an application made "within
one year after the child's birth", only if it "has not been altered before" under s 21
and "the child is not deceased". A birth registered without a name can have one added
for 7 years (s 20), and the duty to supply it runs for the same 7 years (s 8(1A)(a),
added by Act 2 of 2024). The Registrar-General may refuse a name resembling a title,
rank or award, an obscene or offensive name, one contrary to the public interest, or a
patronymic or matronymic marker that does not match the child's sex (s 19(2)). The
name must be in the modern English alphabet, plus any "permitted character" gazetted by
the Registrar-General (s 19(1), s 2(1)); the length limit is that of the electronic
register and is not stated in the Act. Asserted.

### 5. No duty to give particulars for a child who dies within 42 days

s 8(2): "Subsection (1) does not apply in the case of a child who dies within 42 days
after the child's birth." The 42-day offence carries $1,500 or one month, and $50 a day
for continuing after conviction (s 8(4)). Asserted (the daily fine is not).

### 6. A stillbirth is 24 weeks, no sign of life, and not a termination

s 2(1): a stillborn child "issues from the child's mother after the twenty-fourth week
of pregnancy" and shows no sign of life after delivery, and the definition excludes "a
foetus that is aborted by or through treatment carried out for termination of
pregnancy" (the definition carries an Act 2 of 2024 annotation; which words that
amendment added is not shown in the deposit). READING: "after the twenty-fourth week" is
taken as 24 or more completed weeks; the text could also be read as more than 24.
Asserted on that reading.

### 7. The penalties are light for reporting, heavy for lying

Failing to report: $1,500 or one month. A doctor late with death or stillbirth
particulars: a fine up to $1,000 and no imprisonment (ss 23(3), 33(2)). A false or
misleading statement made knowingly or recklessly: $10,000 or 10 years (s 48).
Obstruction: $2,500 or 3 months (s 51). The reporting offences carry a "without
reasonable excuse" defence, but, unlike s 5 of the Coroners Act 2010, the Act does not
say who must prove it. Asserted.

### 8. A consequential amendment points at a provision that no longer exists

s 68(b) inserted into the National Registration Act 1965 a definition of "permitted
character" by reference to "section 19(3) of the Registration of Births and Deaths Act
2021". s 19(3) is marked "[Deleted by Act 2 of 2024 wef 16/04/2024]", and the
definition now sits in s 2(1). Whether the National Registration Act was itself updated
was not checked. Not asserted.

## What would need doing before this is worth anything

- The Registrar-General's discretions (refusing a name, registering on incomplete
  particulars, s 9(2)) are modelled as plain conditions; nothing on how they are used.
- Registration in conveyance cases (ss 11-13) and the adoption and legitimation
  routes (ss 14-18) were read only in passing and are not encoded.
- "Within one year" and "within 3 months" are tested on whole months away from the
  boundary; exact day-counting is not modelled.
- No regulations, prescribed websites or Registrar-General notifications were read.
