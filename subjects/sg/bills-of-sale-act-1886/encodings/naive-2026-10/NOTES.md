# Bills of Sale Act 1886 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 1/4/2022, deposited
at `../../registers/source-bundle/BSA1886.txt`. The latest amendment annotated in the
body is Act 25 of 2021 wef 01/04/2022 (s 8(1)(e), enforcement orders). The arrangement
of sections at the top of the deposit is one number out of step with the body; the
body's numbering is followed.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0035**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. This row takes
what a borrower who gives a bill of sale over his goods, or a lender who takes one,
meets: what counts as a bill of sale (ss 2, 3), attestation (s 10(2)), when a bill is
void (ss 4, 5, 6), rent and property tax (s 7), seizure and sale (ss 8, 9), priority
(s 11), transfers (s 12) and renewal (s 13). Not encoded: the bankruptcy
"possession, order or disposition" rule (s 4(3), (4)), defeasances outside the bill
(s 10(4)), the register (ss 14, 15), satisfaction (s 16), search and copy fees
(s 17), declarations, registrars, fees and rules (ss 18 to 21), and the Schedules'
contents.

## What the Act turns out to say

### 1. A bill given as security is void if it secures less than $100 or an existing debt

s 6: a security bill is void "(a) if the amount ... secured is less than $100; (b) if
it is not made in the form set out in the First Schedule; (c) if it is made or given
wholly or in part in consideration of a pre-existing debt". So a lender cannot take a
bill of sale to shore up a loan already made. Exactly $100 is not "less than $100".
Asserted.

### 2. Lapse of 3 clear days or a wrong consideration voids a security bill outright

s 4(1)(a): a security bill not duly attested, not registered "within 3 clear days after
the execution", or that does not "truly set out the consideration" is void as to the
chattels, against everyone. An absolute (non-security) bill that fails the same tests
is void only against a trustee in bankruptcy, an assignee for creditors, a sheriff's
officer or the creditor behind the process, and only as to chattels still in the
grantor's apparent possession (s 4(1)(b), (2)). How the 3 clear days are counted
(registration up to the third day after execution) is an inference. Asserted.

### 3. The grantee's own lawyer cannot attest, and the effect must be explained

s 10(2): the attesting advocate and solicitor must not be "the advocate and solicitor
of the grantee", and the witness "shall personally explain to the grantor the effect
thereof", the attestation saying so. Asserted.

### 4. Seizure only for listed causes, then 5 clear days on the premises, then auction only

s 8(1) lists the only causes (default, bankruptcy or distress, fraudulent removal, no
rent and tax receipts on written demand, an enforcement order). Seized goods stay on
the premises and may not be removed or sold until 5 clear days have passed (s 8(2));
the grantor may apply to the High Court within 5 days (s 8(3)). Sale must be by public
auction by a licensed auctioneer, otherwise "absolutely void" with a fine up to $200
for anyone aiding it (s 9(1), (2)). The day arithmetic (first removal on the sixth day
after seizure) is an inference. Asserted.

### 5. Only one year's interest arrears, and no protection against the landlord

s 9(3): "Not more than one year's arrears of interest shall be recoverable under any
bill of sale." s 7: a security bill "shall be no protection against a distress for the
recovery of rent or property tax". Asserted.

### 6. Registration lapses after 12 months unless renewed; priority goes by registration

s 13(1): registration must be renewed "once at least every 12 calendar months" or it
"shall become void". s 11: competing bills rank "in the order of the date of their
registration", not execution. s 5: the bill catches only chattels specifically
scheduled and owned by the grantor at execution, so after-acquired goods are outside it
(subject to growing crops and substituted fixtures, plant or trade machinery). Asserted.

## What would need doing before this is worth anything

- The prescribed fees and any rules under s 21 were not retrieved; s 17's 25-cent
  figures may be superseded by "such other rate as is prescribed".
- The counting of "clear days" (Sundays, public holidays, the last day) and of the
  12-month renewal period needs the Interpretation Act and case law.
- No case law on what is a "bill of sale" (for example hire-purchase disguises) was
  searched; the instrument list is a handful of illustrations.
