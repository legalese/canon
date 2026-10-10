# Policies of Assurance Act 1867 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive rows (the `writing-l4-rules` skill was not available to load in
this session). No pipeline, no coverage table, no independent test pass, no human
gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PAA1867.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". Its Legislative History lists the English Act (30 & 31 Vict.,
c. 144, commencement 20 August 1867), its application in Singapore from 12 November
1993 under the Application of English Law Act 1993 (except section 8), and the 1994
Revised Edition (Chapter 392). No amending Act is annotated.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is **REQ-0037** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Act is eight short sections, so the row takes all of it except the
short title: ss 1 to 7 and the Schedule. Not encoded: what the Stamp Duties Act does
to an assignment that is not "duly stamped", and the First Schedule exceptions and
amendments under the Application of English Law Act 1993, which the Legislative
History mentions but which were not retrieved.

## What the Act turns out to say

### 1. Priority goes to whoever notifies the insurer first, not whoever took the assignment first

s 3: "the date on which such notice was received shall regulate the priority of all
claims under any assignment". The date of the assignment plays no part. A later valid
notice beats an earlier notice that fails s 3 (for example, one left at a branch).
The Act does not say what happens when two notices arrive on the same day; the
encoding gives neither priority (an encoding choice). Asserted.

### 2. An assignee cannot sue until written notice reaches the insurer's principal place of business

s 3 bars an assignee from suing "until a written notice of the date and purport of
such assignment has been given to the assurance company liable under such policy at
its principal place of business for the time being". An oral notice, a notice left
at a branch, or one that omits the purport does not lift the bar. The bar is on an
"assignment"; a holder by "other derivative title" (s 1) is not mentioned in s 3 and
is not barred here. Asserted.

### 3. The insurer is safe if it paid in good faith before the notice arrived, but not on the day it arrives

s 3: a payment "bona fide made ... before the date on which such notice was received"
is valid against the assignee. A payment on the day of receipt is not "before the
date". The encoding treats a notice that fails s 3 as never received (an inference).
Asserted.

### 4. The insurer's duties carry no stated sanction or deadline

s 4 obliges every assurance company to print, on every policy, its principal place
of business for notices; s 6 obliges it, on a written request by the person who gave
or signed the notice or their executors or administrators, to deliver a written
acknowledgment. The Act states no penalty for either, and no time limit or fee for
the acknowledgment. An acknowledgment signed by a person who is de jure or de facto
the manager, secretary, treasurer or other principal officer is conclusive evidence
against the company that it received the notice. Asserted.

### 5. Stamping is part of the s 5 form but not a condition of the right to sue

s 5 says an assignment "may be made" by endorsement or separate instrument in the
Schedule words or to that effect, "duly stamped". Neither s 1 nor s 3 refers back to
s 5, so the encoding lets an assignee with an unstamped deed sue once notice is given.
Whether another statute stops that was not checked. The Schedule's "[within] policy"
suggests the Schedule words apply to an endorsement too, and the encoding reads them
so (an inference). Asserted.

### 6. "Assurance company" includes a body that does other things as well

s 7: any body carrying on the business of assuring lives or survivorships, "either
alone or in conjunction with any other object or objects". A "policy" is any
instrument paying out of an assurance company's funds on a contingency depending on
the duration of human life. Asserted.

## What would need doing before this is worth anything

- The First Schedule to the Application of English Law Act 1993 should be read for
  any exceptions or amendments to this Act.
- The Stamp Duties Act consequence of an unstamped assignment, and how this Act sits
  beside the Insurance Act 1966 and the Civil Law Act on assignment of choses in
  action, were not looked at.
- The same-day tie in s 3 priority and the treatment of a defective notice are
  encoding choices with no case law behind them.
