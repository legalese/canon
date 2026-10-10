# Traditional Chinese Medicine Practitioners Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, version in force from 5 December 2025, as deposited at
`../../registers/source-bundle/TCMPA2000.txt`. The latest amendment annotated is Act
19 of 2025 (Statutes (Miscellaneous Amendments) Act 2025, in force 5 December 2025),
whose annotation appears at s 34 on service of documents. The Schedule (substances whose
preparation or supply is a practice of TCM under s 2(e)) is empty in the `.txt`
deposit: only its heading survived extraction.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0022** in `subjects/sg/requirements.jsonl`: Tier 2 of
the remaining Singapore Acts, ordered by everyday-life relevance. The requirement
asks what the Act decides for a person or business it applies to; no scenario has
asked a sharper question yet.

This row takes the provisions a practitioner, a clinic or a patient meets: what the
practice of TCM is (s 2), who may practise and the offences of unlawful practice and
employment (ss 24, 25), the duties to notify, renew and surrender (ss 12, 16, 17),
discipline and when it bites (ss 19, 21, 23), voluntary cancellation (s 26A),
complaints (ss 26B, 26C), the duty to answer an investigator (ss 29(8), 30(5), (6))
and composition (s 34A). Not encoded: the Board and its committees, the Register's
contents, the regulation-making powers, the timetable and procedure of inquiries,
interim-order procedure, investigators' search and seizure, funds, costs, service and
exemptions. Which practices are "prescribed" depends on a Ministerial order under
s 14(1) that is not in the deposit, so it is an input.

## What the Act turns out to say

### 1. Registration is not enough; a practising certificate is what makes practice lawful

s 24(6) defines a "qualified person" as one both registered **and** holding a
practising certificate in force. A registered practitioner whose certificate has
lapsed commits the s 24(1) offence, as does one practising outside the conditions of
registration. A suspended practitioner is not "a registered person" while the
suspension lasts (s 19(9)). The maximum is $25,000 or 6 months, rising to $50,000 or
12 months on a second conviction. Asserted.

### 2. An unlawful practitioner cannot keep or sue for the fee

s 25: no one may "demand, claim, accept, receive, retain or sue for or recover" a
fee for an act done in contravention of s 24. The patient's payment is not merely
unenforceable; the practitioner is not entitled to retain it. Asserted.

### 3. A clinic employing an unqualified practitioner needs ignorance AND due diligence

s 24(2) makes employing a person who is not a qualified person an offence; the
defence in s 24(5) requires the accused to prove both that they did not know and
that they had exercised due diligence. Not knowing alone is no defence. Asserted.

### 4. Board decisions wait 31 days, or the end of an appeal, unless a cancellation is certified

s 19(6): a decision under s 19(1)-(3) takes effect on the 31st day. s 19(7): a
**cancellation** takes immediate effect when the Board certifies a serious and
imminent risk to the public; the power is not given for a suspension or other
measure. s 21(3): an appeal to the General Division of the High Court holds an
uncertified decision back until it is confirmed or the appeal is dismissed or
withdrawn, and there is no further appeal (s 21(2)). Asserted.

### 5. What the Board may do short of cancellation depends on the ground

Grounds (e) to (k) of s 19(1) (breach of conditions or conduct rules, convictions,
misconduct or negligence, breach of a Board order, improper conduct) open the full
menu in s 19(2), including a penalty of up to $10,000, or $50,000 for conduct on or
after 1 April 2020, and suspension of up to 3 years. Ill-health (s 19(1)(l)) opens
only suspension of up to 12 months, altering the class, or modifying conditions.
Grounds (a) to (d) (fraudulent registration, withdrawn qualification, foreign
deregistration, ceasing to practise) have no alternative to cancellation in the
text. Asserted.

### 6. An unconfirmed interim order does not cancel the practising certificate

s 17(7) deems the practising certificate cancelled on cancellation or suspension
under s 19 or s 26A, or when an interim order is **confirmed** (s 26H(8)(a)). An
interim order that is made but not yet confirmed already requires the practitioner
to stop (s 26H(2)(a)), but does not by itself cancel the certificate. Asserted.

### 7. Smaller rules a practitioner meets

- Changes of name or address must be notified within 28 days (s 12(3), $1,000);
  an NRA report of a residential move counts as notification on the day it is made
  (s 12(5)). Treating an NRA report within 28 days as timely is an inference.
- Renewal later than 30 days before expiry attracts a late fee (s 17(5)).
- Certificates must be surrendered within 14 days (ss 16(2), 17(8)).
- Re-registration after cancellation cannot be sought within 3 years, nor more
  than once in 12 months (s 23(3)).
- Voluntary cancellation is barred where the Board believes there is evidence of a
  conviction, misconduct or improper conduct, or an inquiry is pending (s 26A(3)).
- A complaint about conditions, conduct rules, misconduct, improper conduct or
  ill-health needs a statutory declaration unless made by an official (s 26B(2));
  the Board may dismiss only if **unanimously** of the view it is frivolous,
  vexatious, misconceived or lacking in substance, and must otherwise refer it to
  an Inquiry Committee (s 26C(3), (4)).
- Self-incrimination is a reasonable excuse for not answering an investigator
  (s 30(6)).
- Composition is capped at the lower of half the maximum fine and $2,000
  (s 34A(1)).

All asserted.

## What would need doing before this is worth anything

- The Ministerial orders under s 14(1) declaring which practices are prescribed,
  and the registration regulations under s 14(4) (classes, conditions, transitional
  savings under s 24(3)), were not retrieved; without them the s 24 offence cannot
  be applied to a real activity.
- The Schedule's list of substances is missing from the `.txt` deposit and should
  be read from the PDF.
- Which offences are compoundable is prescribed by regulations not in the deposit.
- No Board decisions or case law were searched.
