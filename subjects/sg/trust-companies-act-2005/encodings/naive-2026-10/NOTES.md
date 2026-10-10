# Trust Companies Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/TCA2005.txt`, with amendments to Act 42 of 2024 (in
force 20 June 2025) shown. The changes that matter here are to ss 9, 11 and 14, made
by Act 12 of 2024 (in force 24 January 2025).

**Checks:** one case file, 111 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**14 of the 527 Singapore Acts** deposited here cite it. This row covers the rules a
trust company, its officers and its shareholders deal with directly:

- who needs a licence (s 3, the First and Second Schedules, s 15)
- the maximum fines, and the doubling for corporations (ss 66, 67)
- approval of directors and resident managers (s 13), and individuals who are disqualified (s 14(1))
- controllers (ss 16, 20) and holdings in other corporations (s 21)
- the probate and appointment work a licensed company may and may not take (ss 22, 23, 26, 56)
- trust orders before own-account trades (s 27)
- annual accounts (s 30) and unclaimed money (s 60)

Not encoded:

- winding up
- MAS control and transfers of business (Parts 3A, 3B)
- audit beyond s 30
- inspection and investigation (Part 7)
- confidentiality (Part 8)
- appeals (Part 9)
- composition of offences (s 69)
- anything left to regulations

## What the Act turns out to say

### 1. A bank may help create a trust but may not be the trustee

Section 15(1)(a) and (b) exempt licensed banks and merchant banks only for three
things:

- helping create an express trust
- arranging a trustee
- trust administration "which [is] procedural and non-discretionary"

Acting as trustee and discretionary administration are not on the list. A bank doing
either needs a trust business licence like anyone else. By contrast, a bare trustee,
anyone preparing a will, and an executor are outside s 3 altogether (Second Schedule).
Asserted.

### 2. The fine for unlicensed business doubles for a company. The fines for a licensed company's own breaches do not.

Under s 67(1), the maximum fine for a corporation is "2 times" the stated maximum. So
the s 3(4) maximum for unlicensed trust business, $75,000 plus $7,500 a day, becomes
$150,000 plus $15,000 a day for a company. Section 67(2) excludes a list of offences,
and these are exactly the ones only a licensed company can commit:

- breaching a licence condition (s 7(3))
- ceasing business while a trust is unadministered (s 11(2))
- unapproved appointments (s 13(6))
- holdings over 20% in another corporation (s 21(2))
- late accounts (s 30(4))

A licensee's breach of its licence conditions therefore caps at $100,000. An unlicensed
company's first-day maximum is $150,000. Mixing trust assets with the company's own
(s 59) and dealing ahead of trust orders (s 27) are not on the s 67(2) list, so those
fines do double. The encoding doubles the daily further fine too. That is an inference
from "the maximum amount that the court could ... impose". Asserted.

### 3. Two offences have no penalty of their own since 2024, so the general penalty applies

Act 12 of 2024 rewrote s 9(2), the duty to notify changes within 14 days. It now says
only "shall be guilty of an offence" and deleted the old s 9(3). Section 26(2),
accepting guardianship of an infant's person or a personal-welfare power, states no
penalty either. Both fall to s 66's "$12,500". Neither is on the s 67(2) list, so a
corporation faces $25,000. Asserted.

### 4. The Singapore-only limb for directors in s 14(1)(b) appears to do nothing

Under s 14(1)(b), the Authority must consent before a disqualified individual acts as a
director, but only for a company "incorporated in Singapore". Section 14(1)(a), though,
covers any "officer". Section 2 adopts the Companies Act definition of officer, and the
deposited Companies Act 1967 says officer "includes ... any director". Read literally,
a disqualified director of a foreign-incorporated trust company needs consent anyway.
The encoding follows that reading, which depends on the encoder reading the Companies
Act definition into s 14. Asserted.

### 5. Different control thresholds: "20% or more" in s 16, "more than 20%" in s 21

A person holding exactly 20% of a Singapore-incorporated licensee is a 20% controller
and needed prior approval (s 16). A licensee holding exactly 20% of another
corporation needs no approval (s 21(1) says "more than ... 20%"). Holdings as trustee
are exempt. Asserted.

### 6. Two different defences under s 20, each with a 14-day clock

Under s 20(2), a person who did not know they had crossed a control threshold has a
defence if they notify the Authority within 14 days of becoming aware. Under s 20(3), a
person who did know has a defence only if:

- the crossing came from a family associate's increase
- there is no agreement to act together
- they notified within 14 days of the contravention

Section 20(4) excludes any other "did not intend" defence. One "days to notify" input
serves both limbs. It is measured from different starting points in each. Asserted.

### 7. Other duties with numbers

Each of these is asserted:

- **Accounts (s 30):** lodged within 5 months of the year end. The Authority may extend
  this by no more than 4 months, for a "special reason". Lateness costs up to $500 a
  day, capped at $50,000, and the fine is not doubled.
- **Unclaimed trust money (s 60):** money unclaimed for 6 years goes into court, unless
  a court order restrains payment.
- **Approval refusals without a hearing (s 13(4)):** the Authority may refuse approval
  of an appointee without hearing the company only where the appointee is an
  undischarged bankrupt, or has a fraud conviction punishable with 3 months or more.
  Section 14(1)(c) applies to any fraud conviction, with no such threshold.

## What would need doing before this is worth anything

- The regulations were not retrieved, so these are open:
  - the minimum financial requirements (s 5(2))
  - fees
  - the prescribed exempt persons (s 15(1)(d))
  - which offences are compoundable (s 69)
- The s 15(1)(c) exemption for capital markets services licensees is not modelled.
  "Fund management or custodial services" is not a First Schedule item, so how it
  meets trust business is unclear.
- Associate aggregation (s 16(4)(c)) is taken as an input, not computed.
- The Registration of Criminals Act Third Schedule ground in s 14(1)(c)(iii) is not
  modelled.
- Whether s 67's doubling reaches the daily further fine, and the s 14(1)(a)/(b)
  reading in finding 4, both need a practitioner's view. No MAS guidance or case law
  was searched.
