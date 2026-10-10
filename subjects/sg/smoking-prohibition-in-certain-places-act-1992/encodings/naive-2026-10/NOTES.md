# Smoking (Prohibition in Certain Places) Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021, in operation
31 December 2021), informal consolidation "version in force from 1/5/2026", as
deposited at `../../registers/source-bundle/SPCPA1992.txt`. The latest amendment
annotated is Act 9 of 2026, in force 1 May 2026, which takes vaporisers out of the
definition of "smoking". The arrangement of sections at the top of the deposit is
one row out of step with the body; this row follows the body's numbering.

**Checks:** one case file, 57 assertions satisfied, 0 errors.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it decides where a person in Singapore
may light a cigarette, what a coffee-shop, mall or condominium manager must do about
someone who does, and what the fines are. An automated count found 1 of the 527
deposited Singapore Acts citing it by title; that count undercounts and is not a
measure of importance.

This row takes the definition of smoking (s 2), the prohibition and its exceptions
(ss 3, 3A, 3B, 10), smoking facilities and the Director-General's designation of
them (ss 3C, 3D), the notice to attend court (s 4(2)), entry without a warrant
(s 4A(2), (3)), obstruction (s 4B), the duties of managers and operators (ss 5, 6)
and composition (s 7). Not encoded: which places and vehicles have actually been
prescribed, the prescribed circumstances under s 3B, the prescribed facility
requirements, the prescribed appeal period, the list of compoundable offences — all
of which live in regulations that were not retrieved — and the rest of s 4A, s 8
and ss 9-12.

## What the Act turns out to say

### 1. Vaping is not "smoking" under this Act

Since Act 9 of 2026 (wef 1 May 2026), "smoking" in s 2 "does not include inhaling
and expelling the smoke emitted by a vaporiser ... or the holding of any vaporiser
that is emitting smoke". Whatever other law says about vaporisers, vaping at a
bus-stop is not the s 3 offence. Holding a lit cigarette without puffing it, on the
other hand, *is* smoking, and so is inhaling the smoke of "any other substance",
such as shisha. Asserted.

### 2. A private flat cannot be made a no-smoking place under this Act

s 3A(1) lists what may be prescribed: publicly accessible places; and, if not
publicly accessible, Government or statutory-body places, "common property of any
residential premises or building", commercial or industrial places, recreational
facilities; and passenger vessels. A flat that is none of those falls outside every
head, and a no-smoking zone (s 3A(3)) catches only publicly accessible places
within it, so a staff-only office in a zone is not caught by the zone alone. A
private car is neither a "place" (s 2 excludes vehicles) nor a "specified vehicle"
(which must be a public service vehicle). Asserted, except the car point, which is
in comments only.

### 3. Condominium common areas get more privacy from inspectors than shops do

s 4A(2): officers may enter a specified place that is residential common property
and not publicly accessible "only if" they reasonably believe an offence has been
committed there or evidence can be found there. Everywhere else they may enter
without a warrant "at all reasonable times". Asserted.

### 4. A manager is fixed with what the cashier knows, and must call the police

s 6(1), (2): the manager must tell the smoker to stop "indicating the penalty", ask
the smoker to leave if they do not, and if they still refuse, seek the help of a
police or authorised officer. Asking the smoker to leave and then giving up is an
offence under s 6(4). s 6(5) presumes the manager knows whatever an employee under
the manager's supervision knows, until the contrary is proved. Anyone may complain
to the manager, who must investigate (s 6(3)). The manager need not refund an
admission fee or fare to someone told to leave (s 6(7)). Asserted, except the
refund point, which is in comments only.

### 5. The heaviest penalty falls on whoever abuses a manager, not on the smoker

The smoker faces a fine of up to $1,000 (s 3(2)) and composition of up to $500 if
the offence is prescribed as compoundable (s 7). A person who "hinders, obstructs,
threatens, abuses, molests or assaults" a manager carrying out these duties faces up
to 6 months' imprisonment (s 6(6)) — the longest term in the Act. A manager whose
smoking facility does not meet the prescribed requirements faces $5,000 plus $500 a
day after conviction, rising to $10,000 or 3 months on a repeat (s 3C(6)), with a
"not reasonably practicable" defence (s 3C(7)). Asserted.

### 6. An appeal freezes a designation, and self-incrimination excuses only some refusals

A smoking facility designated by the Director-General (as opposed to by the manager)
"does not take effect until the appeal is determined or earlier withdrawn"
(s 3D(7)), and the Minister's decision is final (s 3D(5)). Under s 4B(2),
self-incrimination is a reasonable excuse "for the purposes of subsection (1)(a) or
(b)" — obstructing and refusing to produce — but the text does not extend it to
giving false information. The encoding confines it as the text does; whether a court
would go further is an inference left open. Note too that s 4B escalates on a
"second or subsequent offence" while s 6(4) escalates on a "second or subsequent
conviction". Asserted.

## What would need doing before this is worth anything

- The regulations that prescribe specified places, specified vehicles, no-smoking
  zones, permitted circumstances, facility requirements, the appeal period and the
  compoundable offences were not retrieved; without them the encoding cannot say
  whether any real place is a no-smoking place.
- The Tobacco and Vaporisers Control Act 1993 (which the vaporiser carve-out points
  to) was not read.
- No case law or enforcement practice was searched.
- The s 6 duty sequence is modelled as one path (tell, then ask to leave, then call
  for help); the text's "render any assistance that is reasonable" (s 6(2)(b)) is
  not modelled.
