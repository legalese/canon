# Building and Construction Industry Security of Payment Act 2004 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 1 April 2022, as
deposited at `../../registers/source-bundle/BCISPA2004.txt`. The latest amendment
annotated in the text is Act 25 of 2021 (wef 1 April 2022), which recast enforcement
as needing "permission of the court" (ss 21(1)(a), 27(1)-(3), 28A(4)). Most other
post-2005 changes are annotated [47/2018].

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0030** in `subjects/sg/requirements.jsonl`: Tier 2 of
the remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. This row follows a progress payment from claim to enforcement:
which contracts are covered (s 4), due dates and interest (s 8), pay-when-paid and
contracting-out clauses (ss 9, 36), the 30-month long-stop (s 10(2)(b)), the payment
response and the window to apply for adjudication (ss 11(1), 12, 13(3)(a)), which
objections survive (ss 15(3), (4), 17(6), 27(7)), review (s 18(1), (3)), when the
adjudicated amount must be paid (s 22(1), (2)(a)), lien and suspension (ss 24(3), 25,
26), and the security for setting aside (s 27(4), (5)).

Not encoded: the definitions of construction work, goods and services beyond their
effect, valuation (s 7), the form of claims and responses, appointment of adjudicators,
adjudication and review procedure, withdrawal, direct payment by a principal beyond its
21-day bar, the nominating bodies, adjudicators' eligibility, costs and fees,
confidentiality, other proceedings, service and the Minister's powers. No regulations
were retrieved, so the prescribed claim date (s 10(2)(a)(ii)), the prescribed review
amount (s 18(1)) and the judgment-debt interest rate (s 8(5)(b)) are parameters; the
figures used for them in the cases (10000 and 5.33) are placeholders.

Every day number is a count on the Act's calendar: s 2 says a "day" is "any day other
than a public holiday". The encoding does not know the public holidays.

## What the Act turns out to say

### 1. A contract can speed payment up but cannot slow it down

s 8(1): where a construction contract fixes a due date, payment is due on "the earlier
of" that date and 35 days after the payment response deadline (or after a GST-registered
claimant's tax invoice). A 60-day or 90-day contract term is overridden by the 35-day
cap; a 30-day term stands. With no contract date the payment is due 14 days after the
same trigger (s 8(2)). Supply contracts: the earlier of the contract date and 60 days
after the claim, or 30 days with no date (s 8(3), (4)). Asserted.

### 2. Saying nothing is disputing

s 12(3): a claimant "is considered to dispute a payment response if the claimant does
not in writing accept" it. A claimant who simply stays silent therefore gains the right
to adjudicate once the 7-day dispute settlement period ends unsettled (s 12(2), (6)),
and must then apply within 7 days (s 13(3)(a)): for a construction claim, the window is
days 7 to 14 after the payment response deadline. Asserted.

### 3. A respondent who wants a review must first pay

s 18(3): a respondent ordered to pay "must not lodge any application for the review ...
unless the respondent has paid the adjudicated amount to the authorised nominating
body", and only if the adjudicated amount exceeds its own response amount by the
prescribed amount (s 18(1)). Asserted, with a placeholder for the prescribed amount.

### 4. Pay-when-paid clauses and deterrents are dead letters

s 9 makes unenforceable any provision "by whatever name called" that ties liability or
the due date to payment by a further party or to "the operation of any other contract".
s 36(2) voids any provision that excludes or prejudices the Act or "may reasonably be
construed as an attempt to deter a person from taking action under this Act". A waiver
of adjudication or a forfeiture triggered by adjudicating is void; a liquidated-damages
clause is untouched. The example clauses are the encoder's, classified by the encoder.
Asserted.

### 5. A patent error rescues an objection before the adjudicator, but not in court

s 17(6)(c) lets the adjudicator consider an objection left out of the adjudication
response if it "relates to a patent error". s 27(7), on applications to set aside,
keeps the "arose afterwards" and "could not reasonably have known" exceptions but has
no patent-error exception. Asserted.

### 6. When the claimant can seek review, the respondent pays in a 3-day window

s 22(1): pay within 7 days of service or by the adjudicator's payable date, "whichever
is the later". But where the claimant may seek review, s 22(2) says pay "not earlier
than 7 days but within 10 days" after service (or later, after a review). Read
literally, the adjudicator's own payable date is not in the s 22(2) list; the encoding
follows the literal reading, which is an inference that a court might not share.
Asserted.

### 7. Suspension and lien need notice, copies, and 7 days, and a housing developer can buy 21 more

ss 25(2) and 26(1): the claimant may exercise the lien or suspend "if, and only if" it
served notice on the respondent, served copies on the principal and owner, 7 days have
elapsed since the last service, and it is still unpaid. The lien covers only goods
"unfixed and which have not been paid for" and not goods owned by a third party
(s 25(1), (4)(a)). s 24(3): a licensed housing developer principal with a Project
Account that serves a notice of direct payment bars both for 21 days unless it has
defaulted before on that contract. Work must resume within 3 days of payment
(s 26(4), (5)). The day-7 and day-21 boundaries are encoding choices; the cases avoid
them. Asserted.

### 8. "In writing" is read generously

s 4(1) applies the Act only to contracts "made in writing on or after 1 April 2005",
but s 4(4) counts an oral contract recorded with the parties' authority, or agreed by
reference to written terms, as written. Small residential work that needs no building
approval is excluded (s 4(2)(a)), as is work outside Singapore (s 4(2)(b)(ii)).
Asserted.

## What would need doing before this is worth anything

- The Building and Construction Industry Security of Payment Regulations were not
  retrieved: the prescribed claim date, the review threshold, the forms, and any
  prescribed exclusions (s 4(2)(e)) are all missing.
- The s 22(2) reading in finding 6 and the day-boundary choices in finding 7 need a
  lawyer and the case law.
- Calendar arithmetic with public holidays removed is left to the caller.
- No adjudication determinations or court decisions were searched.
