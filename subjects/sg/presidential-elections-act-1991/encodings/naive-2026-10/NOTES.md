# Presidential Elections Act 1991 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, with amendments to Act 34 of 2024 (in force 22 January 2025)
and S 612/2023 shown. The deposit's metadata calls it "Current version as at 01 Oct
2026".

**Checks:** one case file, 53 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
candidate, voter, employer or publisher meets: what happens after a reserved election
fails (s 5B), the certificate of eligibility (ss 8(3), 8A, 8B), notice of nomination
(s 7), the deposit (s 10), compulsory voting (s 26), the expenses cap (ss 50, 61), the
employer's duty (s 58), and the polling-period publication offences (ss 42C, 59, 60B,
60C, 60D, 62). The community and service requirements themselves are in Articles 19
and 19B of the Constitution, which is not deposited here and was not read; the
encoding names the s 5B stages by their order only. Nomination and polling procedure,
overseas voting, corrupt practices, most of the advertising regime, election agents
and returns, and election petitions are not encoded.

## What the Act turns out to say

### 1. A failed reserved election steps down, one writ at a time, to an open one

s 5B: an election reserved for one community that wholly fails is followed by open
elections "until a person is elected as President". Reserved for two communities, a
failure moves to the second limb of Article 19B(2)(b), and a second failure opens the
election. Reserved for three, there are three stages before it opens. In an open
election under s 5B "a person does not need to belong to any community" (s 5B(4)).
Asserted.

### 2. "Wholly failed" means two different things in the same Act

For s 5B an election has wholly failed "only if no person stands or will stand
nominated as a candidate on nomination day" (s 5B(5)). For the Act generally, s 7A(4)
says it has wholly failed "if no candidate is nominated or returned as elected". A
nominated candidate who is not returned therefore fails the s 7A test but not the
s 5B one. How the two interact was not explored. Asserted.

### 3. Under 45 on the last nomination day, the application simply lapses

s 8(3) (Act 9 of 2023): an applicant below 45 on the latest nomination day need not be
considered, and the application "is deemed to be withdrawn". Otherwise the Committee
**must** issue a certificate if satisfied of integrity and the service requirements
(s 8A(1)), **must** reject one with no community declaration, including in a reserved
election one that does not claim the reserved community (s 8A(2)(b), (3)), and may
reject one not made according to the Act. The certificate is "not subject to appeal or
review in any court" (s 8C). Asserted (except s 8C).

### 4. Not voting takes you off the register; getting back on costs $50

s 26: every elector "must record his or her vote". Non-voters' names are "expunged"
from the register. A good and sufficient reason restores the name "without penalty";
otherwise it costs $50. Once a writ is issued, no name is restored until after
nomination day, or polling day if there is a poll. Asserted.

### 5. One-eighth of the vote, exactly, still loses the deposit

The deposit is three times the Parliamentary Elections Act deposit (s 10(1); that
figure was not read and is a parameter). It is forfeited if the candidate is not elected
and polls a share that "does not exceed one-eighth" of the votes (s 10(5)), so exactly
one-eighth forfeits. Asserted.

### 6. The spending cap is $600,000 or 30 cents an elector, whichever is greater

s 50(1). Personal expenses and "any fee paid to any election agent not exceeding $500"
are left out. The encoding reads that literally: a fee of $500 or less is excluded, a
larger fee counts in full. The alternative reading, that the first $500 of any fee is
excluded, is not encoded. Knowing overspending is an illegal practice: up to $2,000 and
three years' incapacity to vote or stand (s 61). Asserted.

### 7. The publication calendar

Survey results are blacked out from the day of the writ to the close of polls (s 60B).
Exit polls are banned on polling day before the polls close (s 60C). The cooling-off
period for election advertising runs from the eve of polling day to the close of polls
(s 42C(4)). Canvassing (s 62) and party badges (s 59) are banned "on polling day and the
eve of polling day", and the text has no close-of-polls limit, so read literally they
run all day. A candidate may wear a replica of his or her own symbol (s 59(4)). The
s 60D defence needs both limbs. Asserted.

## What would need doing before this is worth anything

- Articles 19 and 19B of the Constitution, which set the eligibility and community
  rules this Act carries out, need to be deposited and read.
- The Parliamentary Elections Act s 28(1) deposit was not looked up.
- "Clear days" in s 7 is read as excluding both end days. That is an inference: the
  Act does not define the term.
- The Schedule of counted presidential terms (s 5A) is not encoded. In the .txt
  deposit its term numbers are separated from the names, so they can be matched only
  by order.
- No regulations, Election Judge decisions or case law were searched.
