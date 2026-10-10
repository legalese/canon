# Singapore Convention on Mediation Act 2020 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/4/2022), deposited at `../../registers/source-bundle/SCMA2020.txt`. The revised
edition "incorporates all amendments up to and including 1 December 2021"; the
latest amendment annotated is Act 25 of 2021, in force 1 April 2022, which
rewrote s 5 to "grant permission to record". The deposit's Arrangement of
Sections is one number out of step with the body. This row follows the body's
numbering.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **requirement REQ-0049**: Tier 2 of the remaining Singapore Acts, ordered
by everyday-life relevance. The requirement asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet.
The row covers what a business holding a mediated settlement runs into: which
settlements the Act reaches (ss 2, 3 and articles 1 and 2 of the Convention in
the Schedule), who may apply (s 4), what must be filed (s 6), the grounds for
refusal (s 7), the effect of recording and setting aside (ss 5, 8), and parallel
claims (s 9). Not encoded: Rules of Court and regulations (ss 10, 11), the
Convention's treaty machinery (articles 8 to 16, apart from the fact that a
reservation excludes an agreement), and articles 12 and 13 (regional
organisations, non-unified States).

## What the Act turns out to say

### 1. Two Singapore firms can have an "international" settlement

Article 1(1)(b), applied by s 3(1), makes a settlement international when the
State where the parties have their places of business differs from the State
where "a substantial part of the obligations" is performed, or from the State
"most closely connected" with the subject matter. So two Singapore companies
settling a dispute over work in Indonesia, or over goods bound for China, fall
within the Act. Two Singapore companies settling over Singapore work do not.
Where a party has no place of business, article 2(1)(b) uses its habitual
residence instead. Asserted.

### 2. Singapore requires a translation that the Convention leaves optional

Under article 4(3) the competent authority "may request a translation". Under
s 6(4), an agreement not in English "must be accompanied by a certified
translation of it in the English language". A filing in another language with no
certified translation does not meet s 6. Asserted.

### 3. Consumer, family, inheritance and employment settlements are out, and so are court and arbitral ones

s 3(2)(a) imports article 1(2) and (3). The exclusions cover a consumer's dispute
"for personal, family or household purposes", anything "relating to family,
inheritance or employment law", court-approved settlements that are enforceable
as a judgment, and settlements "recorded and enforceable as an arbitral award".
A settlement approved by a court but **not** enforceable as a judgment there is
not excluded, because both limbs of article 1(3)(a) must hold. An unwithdrawn
Singapore reservation under article 8 also excludes an agreement. The deposit
does not say whether Singapore has made one, so the encoding takes it as an
input. Asserted.

### 4. Mediator misconduct counts only if it made the difference, and the court has two grounds of its own

Under s 7(2)(e) and (f), a mediator's serious breach, or failure to disclose a
conflict, is a ground only where the party "would not have entered into" the
agreement without it. Every s 7(2) ground also needs the respondent (A) to ask
for refusal and to prove it. Under s 7(3) the court "may also refuse" on Singapore
public policy, or where the subject matter "is not capable of settlement by
mediation", and neither needs a request. Every ground is "may", not "must". One
difference from the Convention: article 5(1) allows refusal "only if" a ground is
proved, and s 7(1) leaves out "only". That this makes the list non-exhaustive is
an inference, and it is not encoded. Asserted, apart from that inference.

### 5. Only the absent party can have a recorded order set aside

s 8 lets the High Court set aside an order recorded "in the absence of the party"
against whom it is enforced, on application by that party and on any ground for
refusal. A party who was present has no route under s 8. Once recorded, an
agreement is enforced "in the same manner as a judgment" and can be relied on
"by way of defence, set-off or otherwise" (s 5(2)). Asserted (s 8).

### 6. The mediator is not a party and cannot apply

s 4(1) gives the right to apply to "a party to an international settlement
agreement", and s 2(1) says "parties" "does not include any mediator". Under
s 4(2), other rights and remedies "apart from this Act" are untouched. Under s 9,
when a parallel claim is pending the court may adjourn and, on request, order
security. Asserted.

### 7. Article 9's cut-off date is not in s 3

Article 9 limits the Convention to settlement agreements concluded after it
enters into force for the Party. Section 3, which decides when the Act applies,
refers to articles 1, 2, 8, 12 and 13 but **not** article 9. Whether a settlement
concluded before entry into force is within the Act is therefore an open
question on the face of the text. That is an inference: the deposit does not
give the date of entry into force for Singapore, and this point is not encoded.

## What would need doing before this is worth anything

- The Rules of Court (s 10), including filing procedure and fees, were not
  retrieved.
- Whether Singapore has made any article 8 reservation, and the date the
  Convention entered into force for Singapore, are not in the deposit.
- "Commercial dispute" and "consumer" are undefined. The encoding takes them as
  inputs.
- No case law on recording or refusal was searched.
- The parties are modelled as two. Article 1(1)(a) speaks of "at least two
  parties".
