# Pharmacists Registration Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021, in operation
from 31 December 2021), informal consolidation, version in force from 5/12/2025,
as deposited at `../../registers/source-bundle/PRA2007.txt`. The latest amendment
annotated is Act 19 of 2025 w.e.f. 05/12/2025, which rewrote s 69 (composition).
The body's section numbers are followed: the arrangement at the head of the deposit
runs one behind from s 21.

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers requirement **REQ-0019**: tier 2 of the remaining Singapore Acts,
ordered by everyday-life relevance. It asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet.

The row takes what a pharmacist, a would-be pharmacist, a pharmacy-owning employer
or a member of the public meets: who counts as an unauthorised person (s 2, s 70,
the Schedule), the offences and their defences (ss 28-31), the penalty (s 35) and
composition (s 69), eligibility for registration (ss 16, 17, 19), the pharmacist's
own deadlines (ss 15(4)-(6), 23, 24(c)(iii)), the Disciplinary Committee's
sanctions, when its orders bite and the appeal (ss 45(2), 46, 47), and restoration
(ss 26(2), 48(2)). Not encoded: the Council and the Specialists Accreditation Board
(Parts 2, 5), specialist registration, the complaints procedure, the Health
Committee and interim orders (ss 38-44, 50-60), inspectors, and the Council's
discretions to refuse registration (s 21(5)) or remove names (s 25(1)).

## What the Act turns out to say

### 1. A registered pharmacist without a current practising certificate is an "unauthorised person"

s 2 defines "unauthorised person" to include "a registered pharmacist who does not
have a valid practising certificate". So a pharmacist who lets the certificate lapse
and keeps dispensing commits the same s 28 offence as an unregistered shop
assistant, with the same $25,000 maximum. Registration alone is not enough.
Asserted.

### 2. The "I never claimed to be a pharmacist" defence only covers practising

s 28(2): it is a defence to a prosecution under s 28(1)(a) (practising pharmacy) if
the defendant proves he or she "did not in any way represent himself or herself as
a duly qualified or registered pharmacist". The defence is not extended to the
title and holding-out limbs (b) to (f) (inference: those limbs are themselves
representations, so the defence could not fit them). An
unregistered person who calls himself a druggist is guilty whatever else he proves.
Asserted.

### 3. An employer's ignorance is not a defence on its own

s 29(1) makes an employer, principal or partner guilty of the employee's s 28
offence. The s 29(2) defence needs both that the offence was committed "without the
defendant's knowledge" AND that the defendant "has taken all reasonable precautions
and exercised due diligence". Lack of knowledge alone fails. For a registered
pharmacist, s 30(3)'s defence covers allowing (s 30(1)) and enabling (s 30(2)) but
not knowingly practising alongside an unauthorised person (s 30(4)). Asserted.

### 4. On its words, an appeal holds off even an "immediate" disciplinary order

s 46(7): a removal or suspension order does not take effect until 30 days after it
is made, but s 46(8) lets the Committee order it to take effect immediately to
protect the public. s 47(4) then says "Despite section 45 or 46", where a person has
appealed against an order under s 45(2) or 46, "the order does not take effect
unless" it is confirmed or the appeal is dismissed or withdrawn. The words are not
limited to non-immediate orders. Read literally, an appeal suspends an immediate
order made to protect the public. The encoding follows the literal words. Whether a
court would read s 47(4) that way is not known here (no case law was searched).
Asserted.

### 5. A first offence carries no prison term, a second can carry 6 months

s 35: a $25,000 fine for a first conviction under ss 28-33. A second or subsequent
conviction "under any of those sections" (so not necessarily the same one) carries
$50,000 or 6 months or both. Composition (s 69, rewritten by Act 19 of 2025) is
capped at the lower of half the maximum fine and $2,000, so a compounded s 28
offence costs at most $2,000. The s 15(5) fine for late notice of a change of
address ($1,000) composes at $500. Which offences are compoundable is left to
regulations not retrieved. Asserted.

### 6. Getting back on the register: 3 years after a disciplinary removal, no wait after an administrative one

s 48(2): no application to restore a name removed by a Disciplinary Committee
"before the expiry of 3 years from the date of the removal", nor more than once in 12
months, and only after complying with the order. But a name removed for not renewing
the practising certificate for 5 continuous years (s 24(c)(iii)), or under
s 25(1)(a) or (b) (breach of registration conditions, or the specialist grounds), may be restored on application with only
a once-in-6-months limit (s 26(2)). Asserted.

### 7. Deadlines that fall on the pharmacist

Change of name or address: tell the Registrar within 28 days (s 15(4)(a); $1,000
fine), though a change of residential address reported under the National
Registration Act 1965 counts (s 15(6)). Practising certificates last no more than 2
years; renewal applications later than one month before expiry attract a late fee
(s 23(3), (4)), whose amount is not in the Act. On suspension or cancellation the
certificate must be surrendered within 14 days of notice (s 23(6); $1,000). Appeal
against a Disciplinary Committee order lies to the General Division of the High
Court within 30 days of service, with no further appeal (s 47(1), (2)). Asserted.

### 8. Eligibility turns on months of supervised experience in Singapore

Full registration: a Singapore degree and at least 12 months' approved practical
experience, of which at least 9 were under a fully registered pharmacist in
Singapore (s 16(1)(b)). Conditional registration for a foreign qualification: 12
months, of which only 3 need be supervised in Singapore, plus selection for a
Singapore job and the Council's examination (s 17(3)). Temporary registration: up
to 2 years, renewable for periods each of no more than 12 months (s 19(3)).
Asserted.

### 9. Disciplinary sanctions

A suspension must be between 3 months and 3 years; conditions may last up to 3
years; the financial penalty is capped at $50,000 (s 45(2)(b)-(d)). Asserted.

## What would need doing before this is worth anything

- The Pharmacists Registration regulations (fees, compoundable offences, prescribed
  qualifications and examinations) were not retrieved.
- The s 47(4) reading in finding 4 needs checking against case law and the
  parliamentary debates.
- Day-counting for "within 28 days" and "30 days after the order" is an inference
  (the last day counts as in time); the Interpretation Act was not consulted.
- The Council's discretions (ss 16(2), (3), 21(5), 25), specialist registration and
  the complaints, health and interim-order procedures are unencoded.
