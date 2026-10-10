# Education Act 1957 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 5
of 2025 (in force 9 March 2025) shown.

**Checks:** one case file, 131 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes the decisions
a school operator, a teacher, or someone naming an education business actually meets:
what is a school and whether it must be registered (ss 2, 3, 4, 21), the restriction
on "school", "academy", "college" and "university" in a name (s 4A), refusing and
cancelling a school (ss 24, 25), the committee-size cap (s 26(2)), who may teach and
the grounds for refusing or cancelling a teacher's registration or authority (ss 35,
38-44), appeals and where they go (ss 15, 47, 48), the effect of cancellation (ss
49(1), 50) and penalties (ss 4A(3), 17, 62, 64). The Education Finance Board, the
Educational Advisory Council, the Appeals Board's constitution, supervisor and
manager registration (except the appeal route), inspection powers, appeal hearing
procedure, regulations and the Schedule forms are not encoded.

The arrangement of sections at the top of the deposit is numbered out of step with
the body (it puts "Exemption" against 1 and "Appeal to be argued on grounds stated"
against 59). The body's numbers are used throughout.

## What the Act turns out to say

### 1. The same ground goes to a different forum depending on whether it refuses or cancels

s 48(2)(a) sends appeals against decisions under "25(1)(a)" and "39(a)" to the
Minister, and everything else to the Appeals Board. But s 25(1)(a) is cancellation
of a school on *any* s 24 ground, and s 39(a) is cancellation of a teacher on *any*
s 38 ground. So a school refused for inadequate fire precautions appeals to the
Appeals Board, while a school cancelled for the same reason appeals to the Minister;
a teacher refused for lacking minimum qualifications goes to the Board, but one
cancelled for it goes to the Minister. The Minister may redirect any appeal to the
Board. Asserted.

### 2. Lacking qualifications cannot stop an unregistered teacher being authorised, but can end the authority

s 42(a) lets the Director-General refuse to authorise an unregistered teacher on the
grounds in "section 38(a) to (g)", leaving out (h), the prescribed minimum
qualifications. s 43(1)(a) allows cancellation of the authority on any s 39 ground,
and s 39(a) brings in every s 38 ground, (h) included. Read literally, a lack of
qualifications is not a ground to refuse the authority but is a ground to cancel it
the day after. Asserted.

### 3. Anyone teaching 10 or more people runs a "school", and naming yourself one is an offence

s 2 defines a school as education for "10 or more persons". s 21 forbids carrying
one on unregistered (subject to Ministerial exemption under s 3, and s 4 takes out
ITE, private education institutions and licensed early childhood centres). s 4A
forbids "academy", "college", "school", "university" or derivatives "in any
language" in the name under which a person provides education, without the
Director-General's written consent: $2,000 or 12 months. A capacity of more than
1,200 pupils in any one session is itself a ground for refusing registration
(s 24(j)). Asserted. That a private education institution is outside s 4A is an
**inference** from s 4; s 4A(2) does not list it.

### 4. Two penalty tiers, and an overlap between them

s 62(1) offences (acting as manager or teacher of an unregistered school, false
statements, obstructing inspection, teaching unregistered, continuing after
cancellation) carry $2,000 or one year. Everything else falls to s 62(2): $500,
or $1,000 for a second offence, with no imprisonment, plus $100 a day for a manager
or teacher whose offence under "section 20 or 23(3)" continues after conviction.
s 20(a) and (c) describe much the same conduct as s 62(1)(a) and (e), but refer to
"the penalties hereinafter provided", and only s 20 attracts the daily fine. The
encoding gives the daily fine to s 20(b) (a manager employing an unregistered
teacher), which s 62(1) does not cover. s 23(3) (exhibiting the certificate and
staff list) does not itself create an offence; treating it as one is an
**inference** from s 62(2)'s wording. Asserted.

### 5. The Appeals Board is closed to Government teachers except on cancellation

s 15: the Board "shall not hear an appeal from any Government teacher other than an
appeal against the cancellation of his registration as a teacher". The appellant
bears the onus of showing the Director-General's grounds wrong (s 58), and the
decision on appeal "shall not be questioned in any court" (s 60(3)). Appeals must be
lodged within 14 days of service (s 48(2)); conditions of registration likewise
within 14 days (s 47). Asserted, except ss 58 and 60(3).

### 6. Cancellation bites at once, and so does being on the premises

A cancelled school ceases from service of the notice unless the Director-General
permits it to continue pending appeal (s 49(1)). If not permitted, any pupil or other
person on the premises without written authority commits an offence, and police may
enter by force (s 50). If every manager's registration is cancelled, the school's
must be (s 25(2)). Only the Director-General can set a prosecution going (s 64).
Asserted.

## What would need doing before this is worth anything

- The Education (Schools) Regulations and any prescribed exemptions under s 4A(2)(e)
  and Gazetted terms under s 4A(1)(a) were not retrieved.
- The overlap between s 20 and s 62(1) is reported, not resolved; which penalty a
  court applies to s 20(a) and (c) conduct was not researched.
- Only selected grounds from s 24 (8 of 18) and s 38 are enumerated; the rest
  behave the same way in the encoding but are not listed.
- Supervisor and manager registration (ss 28-34) is touched only through the appeal
  route.
- No case law was searched.
