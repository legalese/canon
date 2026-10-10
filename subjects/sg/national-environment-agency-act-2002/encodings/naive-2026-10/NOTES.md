# National Environment Agency Act 2002 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments up to
1 December 2021; the latest amendment annotated in the body is Act 7 of 2020, on s 23).

**Checks:** one case file, 91 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. It is an institutional Act:
it sets up a statutory board and lends its officers powers under other laws. This row
takes only the provisions that decide something: membership and term (ss 5, 7),
quorum and voting (s 9), approvals for joint ventures and loans (ss 12(h), 23), the
financial year (s 19), immunity and information errors (s 17), where money goes
(ss 21, 46(4)), the offences and penalties (ss 40, 42, 47, 48(2)), compensation for a
meteorological station (s 41), auxiliary officers (s 42A), officers' liability (s 43),
certificate evidence (s 45) and composition (s 46). Functions (s 11), general powers,
the seal, committees, staff, estimates, Part 6 transfers of 2002 and 2007, and the
Schedule are not encoded.

## What the Act turns out to say

### 1. Composition money goes to the Consolidated Fund, everything else to the Agency

s 21: "All moneys recovered or charges collected under this Act must be paid into and
form part of the moneys of the Agency." s 46(4): "All composition sums collected under
this section must be paid into the Consolidated Fund." Both carry the same amendment
note [11/2019]. So the Agency keeps fees but not the composition sums its own officers
collect. Asserted.

### 2. Leaking Agency information carries a smaller fine but a longer prison term than obstructing an officer

Secrecy breach (s 47(2)): up to $2,000 or 12 months. Using the Agency's symbol (s 40(2))
or obstructing, misinforming or defying an officer (s 42(2)): up to $10,000 or 6 months.
Regulations may go to $10,000 or 12 months, plus $1,000 a day for a continuing offence
after conviction (s 48(2)). The secrecy duty binds anyone who "is or has been" a member,
officer, employee, auxiliary officer, agent or committee member. Asserted.

### 3. The quorum can never be fewer than 4, whatever the board size

s 9(1) (as amended by 2/2012) takes "the higher of" one-third of members in office and
4 members. With between 7 and 14 members under s 5 (Chairperson, Deputy and 5 to 12
others) one-third is at most 5, so 4 governs any board up to 12 members. A tie is
broken by the Chairperson's or Deputy's casting vote; the encoding INFERS that a member
elected to preside when both are absent has no casting vote, since s 9(5) names only
those two. Asserted.

### 4. Weather forecasts that turn out wrong give no claim, if made in good faith

s 17(3): where the Agency supplies information to the public, neither it nor its
employees are liable for "any error or omission of whatever nature" made in good faith
in the ordinary course of duties. s 11(1)(q) makes meteorological services for the
general public a function, so that is the obvious case (an inference about application,
not a statement in the Act). s 17(1) separately protects members, officers, employees and
"other person acting under the direction of the Agency" personally for good-faith acts.
Asserted.

### 5. Loans need the Government as lender or the Finance Minister's approval

s 23(1) (substituted by 7/2020): the Agency "cannot raise loans ... except in accordance
with this section". It may borrow from the Government, or from any other source "with
the approval of the Minister for Finance"; bonds and debentures must be instruments the
Minister for Finance approves. A joint venture needs the (portfolio) Minister's approval
(s 12(h)). Asserted.

### 6. A landowner gets compensation for permanent damage only

s 41: in an emergency, on reasonable notice, officers may enter land to set up a
meteorological observation station. The Agency "must pay compensation ... for any
permanent damage", and "Except as provided in subsection (2), no action may be brought".
Disputes about the amount go to a District or Magistrate's Court. Asserted.

### 7. An auxiliary officer acts only on a written authorisation and an officer's direction

s 42A(1), (2): the chief executive's written authorisation specifies the powers "and no
other powers", and they may be exercised only as authorised "and directed by an officer
or employee of the Agency". The directing officer need not be "present at all times"
(s 42A(7)). An auxiliary officer is not an Agency officer or employee (s 16A(4)) but is
deemed a public servant under the Penal Code 1871 while exercising the power (s 42A(5)(b)).
Asserted (the authorisation test only).

### 8. A chief executive's certificate needs 10 clear days' notice

s 45(3): the accused must get a copy and notice "at least 10 clear days before the
commencement of the proceedings". The encoding counts clear days as excluding both the
day of service and the day proceedings begin; that reading of "clear days" is an
inference, the Act does not define it. Asserted.

## What would need doing before this is worth anything

- Which offences are prescribed as compoundable (s 46(3)) is left to regulations, which
  were not retrieved.
- s 42 borrows the offences of every "environmental written law" (EPMA 1999, EPHA 1987
  and laws the Agency administers); none of those was read.
- Whether the chief executive appointed a member under s 5(2) counts within the 5 to 12
  "other members" is not settled by the text; the encoding takes the count as given.
- Part 6 (transfers of 2002 and 2007) and the Schedule were read but not encoded.
- No case law was searched.
