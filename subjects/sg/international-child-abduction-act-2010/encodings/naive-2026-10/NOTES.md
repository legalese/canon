# International Child Abduction Act 2010 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, "version in force from 1/4/2022", deposited
as `../../registers/source-bundle/ICAA2010.txt`. The latest amendment annotated is
s 8(4), "[Act 25 of 2021 wef 01/04/2022]".

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: a parent who takes a child across a
border without the other parent's consent, or the parent left behind, meets this Act.
(An automated count found 3 of the 527 deposited Singapore Acts citing it by its slug
title; that count undercounts, and is not a measure of importance.)

This row takes what such a parent meets: whether the Convention applies (s 4, Arts 3,
4), when return must be ordered and when it may be refused (Arts 12, 13, 17, 18, 20),
the Central Authority route (ss 6, 7, 21, Art 27), the court route (ss 8, 11, 13, 14),
legal aid and advice (ss 17, 18) and costs (s 23, Art 26). Not encoded: the Gazette
list of Contracting States (not in the deposit), territorial declarations (s 4(3)),
intervention (s 9), interim orders (s 10) beyond their effect on s 13, welfare advice
(s 12), the Legal Aid and Advice Act 1995 machinery imported by s 19, proof of
documents (s 22) and regulations (ss 20, 24).

## What the Act turns out to say

### 1. The one-year line decides whether settlement counts

Art 12: if proceedings start when "less than one year has elapsed" since the wrongful
removal, the court "shall order the return of the child forthwith"; the child being
settled in the new environment is no answer. After a year, return is still ordered
"unless it is demonstrated that the child is now settled". The encoding counts whole
months: a settled child at 11 months must be returned, while at 12 months the court
may refuse. Asserted.

### 2. A refusal ground makes return discretionary, never forbidden

Art 13 says the court "is not bound to order the return" (consent or acquiescence,
grave risk, the child's objection) and Art 20 that return "may be refused" on human
rights grounds; Art 18 keeps the power "to order the return of the child at any time".
So the encoding has two outcomes, "must order return" and "may refuse return", and no
outcome in which return is barred. Asserted.

### 3. The Convention stops at 16, and only covers abductions after the in-force date

Art 4: the Convention "shall cease to apply when the child attains the age of 16
years". s 4(2): unless the Minister's order says otherwise, it applies between
Singapore and another State only to removals, retentions and access breaches
"occurring on or after" the date the order specifies. A 16-year-old, or a child
taken before that date, is outside the return mechanism. Asserted.

### 4. Starting a return case freezes every custody decision, Syariah Court included

s 13(1): once a s 8 application is made, "no decision may be made by any court" on
custody, care and control or access until it is determined, and s 13(4) extends
"court" to the Syariah Court and the Appeal Board under the Administration of Muslim
Law Act 1966. Only the Court's interim orders under s 10 survive (s 13(3)). Separately,
Art 17: a Singapore custody order in the abductor's favour is not by itself a ground
to refuse return. Asserted. (s 13(2) explains "deciding on the merits", words s 13(1)
does not use; the encoding reads (1) as written.)

### 5. Legal aid reaches the parent resisting return, not the respondent to a declaration

s 17 lets the Director grant legal aid to a citizen or habitual resident of Singapore
or a Contracting State who is "a party to the proceedings under section 8" (either
side) or "the applicant in the proceedings under section 14". A respondent to a s 14
declaration application is not listed. s 23: the Government bears no Art 26 costs
except through that legal aid or advice. Asserted. Whether the Legal Aid and Advice
Act 1995 means test applies through s 19 is an inference, not encoded.

### 6. The injunction is available before a return order and after a dismissal

s 11(1): while a s 8 application "is pending or has been dismissed", the Court may
restrain "any person from taking the child out of Singapore". Once return is ordered,
s 8(4) instead lets the Court permit the child to be taken out. Asserted.

### 7. The Schedule is a partial Convention

The deposited Schedule reproduces only some Articles; Arts 2, 6, 11, 16, 23, 25 and
33 onward appear only as "... ... ...". What the omitted Articles say cannot be read
from the deposit. s 3 gives force of law to "the provisions of the Convention as set
out in the Schedule", so (an inference) the omitted Articles do not have force of law
in Singapore through s 3. Not asserted.

## What would need doing before this is worth anything

- The Gazette order listing Contracting States and their in-force dates was not read.
- "Less than one year" is modelled in whole months; a day count is needed at the
  boundary.
- Art 13(a)'s "not actually exercising" is folded into the Art 3(b) wrongfulness test;
  the two carry different burdens and should be separated.
- No case law on habitual residence, grave risk, settlement or the child's objections
  was searched; each is a judgment the encoding takes as an input.
- The Legal Aid and Advice Act 1995 and its Regulations, imported by s 19, were not read.
