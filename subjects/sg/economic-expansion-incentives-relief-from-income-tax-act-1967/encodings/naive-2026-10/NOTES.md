# Economic Expansion Incentives (Relief from Income Tax) Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to and including
1 December 2021), informal consolidation, version in force from 25/12/2024, as
deposited at `../../registers/source-bundle/EEIRITA1967.txt`. The latest amendment
annotated is Act 41 of 2024 (wef 25/12/2024). The arrangement of sections at the head
of the deposit is one row out of step with the body; the body's numbering is followed.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is **REQ-0078** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. Every incentive in the Act is applied for by "a company", so an
individual meets it only through a company.

The Act is long (about 3,000 lines of text). This row takes the decisions a company
meets most often: when a new approval can still be given; how long a pioneer or a
development and expansion relief period may run; the concessionary rate and its
rising floor; expansion income; approved foreign loans and approved royalties; the
investment allowance, its clawback and its use; confidentiality; and show-cause before
revocation. Not encoded: ascertaining income and the old/new trade rules (ss 7-12,
25-28), the loss carry-forward order (s 15), intellectual property income (s 19),
transfer of awards (Part 5), approved activities (ss 40A-40G), corporate partnerships
and the account-transfer mechanics (ss 42, 45), the recovery assessments (ss 14, 24,
61A), the saving of repealed Parts (s 65), and every regulation and "such earlier
date as may be prescribed".

## What the Act turns out to say

### 1. Nearly every door closes on 1 January 2029, and one has already closed

No new pioneer enterprise, pioneer service company, development and expansion company
or approved foreign loan "on or after 1 January 2029" (ss 5(4), 17(4), 21(4), 33(6)),
and no investment allowance for projects under s 43(1)(a) to (h) from then either
(s 43(8)). Approved royalties, fees and contributions closed on **1 April 2023**
(s 37(4)). The energy-efficiency and greenhouse-gas allowances close after
31 December 2026 (s 43(7), (10)); submarine cables after 31 December 2028 (s 43(9)).
All the investment allowance dates are "or such earlier date as may be prescribed".
Asserted.

### 2. The development and expansion rate rises half a point at each milestone

For a "specified" company (approved, or extended, on or after 29 February 2012) the
rate in a later part of the relief period "must not be less than [(0.5 × B) + A]%"
(s 21(13)), where the parts start at years 11, 16, 21 and 31 (s 21(17)) and B counts
the milestones passed. With A at 5% the floor is 5.5% in years 11-15 and 7% in years
31-40. With A at 15% only the parts from year 21 count, so the floor stays at 15%
until year 21, then 15.5%. The encoding assumes the company was specified on every
milestone date. Asserted.

### 3. The 15% rate is fenced off, but not for companies approved before 19 April 2016

s 21(10)(b) allows 5%, 10% or 15% for later approvals, and s 21(17A) lets the Minister
choose 15% only "on or after 17 February 2024" and only for income derived on or after
1 January 2024. (17A) names (10)(b), not (10)(a), so a company approved before
19 April 2016 may be given any rate "not less than 5%", 15% included, with no date
fence. That reading is the text's, not a checked policy. Asserted.

### 4. Relief periods: 15 years for pioneers, 20 or 40 for development and expansion

A pioneer relief period, with all extensions, "must not in total exceed 15 years",
extended at most 5 years at a time (s 6). A development and expansion period starts at
up to 10 years, is extended 5 years at a time, and caps at 20 (s 22(1)-(3)), except
that a "relevant" company (one that oversees, manages or controls the activity on a
regional or global basis, or does a services activity under s 20) may be extended 10 years
at a time up to 40, but only by an extension granted between 18 February 2008 and
31 December 2028 (s 22(4)-(7)). Whether a s 22(4) extension may start below the
20-year cap is not said; the encoding allows it (an inference). International legal
services approved between 1 April 2010 and 30 June 2017 got a flat, non-extendable
5 years at 10% (s 23). Asserted.

### 5. Assets bought with an allowance are locked in for two years after the period

A company must not "sell, lease out or otherwise dispose of" an asset that earned an
investment allowance during its qualifying period "or within 2 years after the end",
without the Minister's written approval (s 46(1)); the allowance is then deducted from
the account and any shortfall assessed (s 46(2)). Disposal exactly two years after is
treated as within the period (an inference: "within 2 years" read inclusively). The
qualifying period is up to 5 years, 8 for hire-purchase from 15 February 2007, 10 for a
tourism project (s 44(1)). Asserted.

### 6. The debt after a revocation can be waived only when the Act's own power was used

When an approved loan or royalty approval is revoked, the withholding tax that was not
deducted becomes a debt (ss 35(3), 39(4)). The finance Minister may waive it if the
contravention was not knowing or intentional, but only for a revocation "under
subsection (2)" (ss 35(4), 39(5)), not one under s 61. Revocation dates may be set
before the notice and even before the contravention (s 61A(1)). Asserted for the waiver.

### 7. Expansion income is only the excess over a three-year average

The concessionary rate applies to "expansion income": qualifying income that exceeds
one-third of the qualifying income of the three years before the commencement day
(s 21(18), (19)), unless the Minister specifies another figure (s 21(22), not modelled).
Asserted.

### 8. Smaller points

A foreign loan of $20 million or more may be put forward as of right; a smaller one is
at the Minister's discretion (s 33(1), (2)). Equipment it finances cannot be disposed of
without permission unless the loan is repaid (s 34). A royalty agreement may be varied
without sanction only to reduce the amount for the same consideration, with notice
within 30 days (s 38(2)). Royalties reinvested in the payer's ordinary shares are exempt
to that extent (s 40). Applications and certificates are confidential except at the
company's instance, but the Minister may gazette the name, industry and product (s 60).
A company has 30 days to show cause before revocation (s 61(1)). Asserted.

## What would need doing before this is worth anything

- No regulations were retrieved: the prescribed qualifying activities, the earlier
  closing dates for investment allowances, and the forms.
- Ascertaining income (ss 10, 25, 26), the loss order (s 15) and the account mechanics
  between the normal and concessionary allowance accounts (s 45) are where the money
  is decided, and none is encoded.
- B in s 21(13A) and (16) depends on the dates on which the company was "specified";
  the encoding assumes every milestone counts.
- Rates are percentages the Minister writes in a certificate; nothing here checks a
  real certificate or an EDB practice note.
