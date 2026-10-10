# Co-operative Societies Act 1979 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
9/3/2025"), with amendments annotated to Act 5 of 2025 (wef 9 March 2025).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**4 of the 527 Singapore Acts** deposited here cite it. This row takes the rules with
numbers in them that members and officers of a society meet: founding numbers (s 5),
membership qualifications (s 39), votes (s 42), the shareholding cap and share
transfers (ss 43, 44), leaving (ss 47-49), calling meetings (ss 53, 55), quorum and
voting (ss 56, 57), committee eligibility (s 60), the levy on surplus (s 71), bonus
certificates and shares (s 73), and the word "co-operative" (s 99). Registration
procedure, by-laws, credit-society control, audit and returns, loans and investment,
dividends, amalgamation, inquiry, dissolution, liquidation, disputes and the general
offences of ss 100-100F are not encoded.

## What the Act turns out to say

### 1. The fixed numbers cap the percentages for large societies

s 55(2): an extraordinary general meeting must be convened on a requisition signed by
"at least 20% or 60 of the members or delegates ..., whichever is the less". s 56(1):
the quorum is "20% or 30 ..., whichever is the less". So a society of 5,000 members
needs only 60 signatures, and 30 members make a quorum. Asserted.

### 2. An inquorate meeting can still decide, but not everything

s 56(2): if no quorum is present within 30 minutes, those present form a quorum, but
that meeting cannot amend the by-laws and a resolution needs two-thirds of the members
present. Otherwise s 57: simple majority, a tie loses, and the chair has no casting
vote. Asserted. Reading "within 30 minutes" as "more than 30 minutes waited" is an
inference.

### 3. The surplus levy is stepped, and some gains are left out

s 71(2): 5% of the first $500,000 of surplus to the Central Co-operative Fund, and 20%
of the excess to that Fund or the Singapore Labour Foundation. s 71(2A), added by Act
17 of 2024: gains on disposing of own-use immovable property or of shares are excluded
from the surplus. A $800,000 surplus pays $85,000; with $300,000 of excluded gains it
pays $25,000. Prescribed substitute rates, Government grants excluded by order (2B) and
remission (6) are not encoded. Asserted.

### 4. The Registrar's approval cures some committee bars, not others

s 60(1): the Registrar's written approval cures lack of citizenship or residence (b)
and prior removal or suspension (f), and s 60(3), (4) let it cure the fraud-or-dishonesty
bar. It does not reach bankruptcy (c), a conviction under this Act (d) or dismissal by a
society (e). For a non-credit society the fraud bar lasts 5 years (from release, or from
conviction if not imprisoned); for a credit society it has no time limit. Asserted.
Collapsing "release" and "conviction" into one count of years is a simplification.

### 5. Membership is personal and capped

s 42(1): one vote per individual member, in person, whatever the shareholding. s 43: no
member may hold more than 20% of the share capital without the Registrar's approval,
but the cap does not apply to a society, trade union or platform work association.
s 44(2): shares may be transferred only after a year, and only to the society, a member
or an accepted applicant. s 47: a past member's liability ends 2 years after leaving.
Asserted.

## What would need doing before this is worth anything

- The Co-operative Societies Rules (substitute levy rates, dividend caps, prescribed
  matters) were not retrieved.
- The credit-society common bond (s 39(4)-(6)), by-law expulsion procedures (s 49(2))
  and the early bonus payouts of s 73(7), (7A) are not encoded.
- No case law was searched.
