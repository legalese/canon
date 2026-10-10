# Maintenance of Parents Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, "version in force from
5/12/2025", as deposited at `../../registers/source-bundle/MPA1995.txt`. The cover
says the revised edition incorporates amendments up to 1 December 2021; the latest
amendment annotated in the text is Act 19 of 2025 (wef 5 December 2025). Most of the
provisions encoded here carry the annotation Act 22 of 2023 (wef 1 July 2024).

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it is the Act under which an elderly
parent in Singapore can make an adult child pay for his or her upkeep, and under
which a child can resist on the ground of having been abandoned, abused or
neglected. This row takes who may claim (s 3), the child under 21 (s 3AA), the
parent's record of abandonment, abuse or neglect (ss 3B, 12A), when an order may be
made and the abandonment defence (s 5), how long an order lasts (s 7), proxies
(s 11), representation (ss 12C, 14), contempt (s 15) and the routes of challenge
(ss 3(8), 8(6), 17, 18(2)).

Not encoded: the Commissioner's conciliation machinery beyond s 12A, destitute
persons (s 12B), security and directions (s 6), variation grounds (s 8(1)–(3)),
enforcement (s 10), the Tribunal's constitution (s 13), information-gathering
(s 14A), special cases (s 16), privacy (s 19) and costs (s 20). The s 5(2) factors
are not encoded: they shape the amount, which the Act leaves to the Tribunal. What
counts as a "record or purported record of abandonment, abuse or neglect" is
"prescribed" (s 2) by regulations that were not retrieved, so here it is a yes/no
fact.

## What the Act turns out to say

### 1. A child under 21 cannot even be named

s 3AA (added by Act 19 of 2025): a child below 21 "is not liable to maintain the
child's parent", a claim must not be referred to the Commissioner against the child,
and the child "must not be named or joined as a respondent". The encoding therefore
refuses an order against a 19-year-old even where every s 5(1) condition is met.
Asserted.

### 2. A parent with a record of abandonment, abuse or neglect needs permission, decided without the child

s 3B(1): permission must first be obtained if the parent's own declaration, the
Commissioner, or a discontinued conciliation shows a record of abandonment, abuse or
neglect of the child. Permission may be granted on a "good arguable case" that the
parent did not abandon, abuse or neglect the child, or that the child should pay "on
just and equitable grounds" (s 3B(7)). The application is dealt with "without
informing or involving the child" unless the child was in the discontinued
conciliation **and** wishes to take part (s 3B(2)); s 18(3A) carries the same
silence into an appeal against a refusal. The Commissioner must not send such a
matter to conciliation without that permission (s 12A(1)). Asserted.

### 3. At the hearing, the burden is on the child

At the hearing of the application itself, abandonment is for the respondent to prove:
"The onus of proving abandonment, abuse or neglect is on the respondent alleging it"
(s 5(5)). Proved, the Tribunal "may" dismiss or reduce (s 5(4)) — a discretion, not
a bar. Asserted (as the opening of that discretion only).

### 4. An unsecured order dies with the child; a secured one does not

s 7(1): unsecured maintenance ends on the death of the parent or the respondent,
whichever is earlier; secured maintenance ends only on the parent's death. Where
there are several children, one child's death does not release the others (s 7(2)).
Asserted (s 7(1) only).

### 5. No lawyers, except the Commissioner

s 14(4) bars representation by an advocate and solicitor before the Tribunal, and
s 12C(2) in conciliation and mediation, except that the Commissioner may represent
the parent though a lawyer. An unpaid agent may appear with the Tribunal's
permission; a paid one may not (s 14(3)(a)). Asserted.

### 6. The age of 60 is a starting point, not a bar

s 3(1) requires 60 or above, domicile **and** residence in Singapore, and inability
to meet basic needs (defined in s 3(5)); s 3(6) lets a younger parent in if the
Tribunal is satisfied of infirmity "or that there is any other special reason". A
parent who is domiciled here but lives abroad cannot apply. Asserted.

### 7. Mediation is compulsory before a first hearing, optional on variation

s 5(7) says the Tribunal "must" refer the parties to a mediator before hearing an
application; s 8(4) says it "may" on a variation application. Asserted.

### 8. The amount is beyond the High Court's revision, and consent orders are hard to appeal

s 17(2): revision "do[es] not extend to" the quantum of maintenance. s 18(2): an
appeal lies on law or mixed law and fact, but not from a consent order unless the
consent is alleged to have been obtained by fraud, duress, threat or
misrepresentation. Challenges under ss 3(8), 8(6) and 17(1) must be brought within
14 days; this encoding counts the decision day as day 0, which is an inference.
Asserted.

### 9. Contempt is a fine or jail, not both

s 15(1): up to $5,000 "or" up to 6 months. Asserted as two maxima.

## What would need doing before this is worth anything

- The regulations prescribing what a "record or purported record of abandonment,
  abuse or neglect" is (s 2), and the transitional regulation saved by s 3AA(3),
  were not retrieved.
- Nothing models how the Tribunal sets or apportions the amount (ss 5(2), 5(6)).
- No Tribunal or High Court decisions were searched.
