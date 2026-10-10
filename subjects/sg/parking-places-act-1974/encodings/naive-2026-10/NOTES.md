# Parking Places Act 1974 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/PPA1974.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021"; the latest amendment annotated is
Act 12 of 2021 (s 13(3)).

**Checks:** one case file, 52 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes what a driver,
vehicle owner, car-park operator or developer meets: the heavy-vehicle definition and
licence (ss 2, 5), limits on road parking places (s 4(2)), the post-2018 layout duty and
deficiency charge (ss 6A, 6B), when a parking charge takes effect (s 9(5)), composition
(s 12), naming the driver (s 13), the owner's liability (s 14), removal, clamping,
release and sale (s 15), entry into private parking places (s 15B), the penalties
(ss 5A, 6A, 13, 15C, 16, 19) and personal immunity (s 20). Administration, the
Authority's powers to provide parking, charge-setting procedure, shared-mobility removal
and forfeiture (s 15(2), (8)-(13)), service, corporate liability and the rule-making
power are not encoded. The parking offences themselves, which offences are
compoundable, and the deficiency-charge amount are all in rules, which were not
retrieved.

## What the Act turns out to say

### 1. The owner is guilty of the driver's parking offence unless they name the driver in 14 days

s 14(1) makes the owner at the time guilty "as if the person were the actual offender".
The ways out are: the vehicle was stolen or illegally taken; a statutory declaration
naming the person in charge within 14 days after service of the notice (s 14(3)(a)); or
showing the owner could not with reasonable diligence have found out. A single
declaration covering more than one parking offence does not count (s 14(5)). Once a
penalty is imposed on one person, no further penalty may be imposed on anyone else
(s 14(2)). Asserted.

### 2. A car-rental hirer and the registered owner may both be "owners"

s 14(6)(d) makes the hirer under "a hiring agreement or hire-purchase agreement" an
owner, while s 14(7)(a) says the registered owner is not taken to have ceased possession
by "any hiring (not being a hiring under a hire-purchase agreement) or lending". Read
together (an inference, not stated in terms), a rental hirer is an owner and the
registered owner who hired the car out remains one; a borrower and a workshop are not.
Asserted.

### 3. The layout-notice offence is fifteen times the general fine, with a fixed daily fine

Contravening a s 6A(4) infringement notice carries a fine up to $30,000 and, for a
continuing offence, "a further fine of $500" a day — not "not exceeding", unlike every
other continuing fine in the Act (ss 5A(4), 16). There is no imprisonment. The duty in
s 6A(1) binds only parking places provided, or developments permitted, on or after
8 May 2018, or with a parking plan application pending on that date. Asserted (the
fixed-versus-maximum wording is noted, not modelled).

### 4. Composition is capped at the lower of half the maximum fine and $5,000

s 12(1)(a). So the cap is $5,000 for the $30,000 and $10,000 offences and $1,000 for
the $2,000 ones. Only offences "prescribed" as compoundable can be compounded; the
prescription was not read. Asserted for the cap only.

### 5. Several offences have no penalty of their own

Operating an unlicensed heavy-vehicle parking place (s 5(1)), plying for hire in a
parking place (s 10), failing to name the driver within 14 days (s 13(2)), and removing a
clamped or detained vehicle (s 15(7)) state no penalty, so s 16's general $2,000 or
3 months (plus up to $500 a day for continuing offences) applies. Lying about the driver
(s 13(3)) or in an application (s 15C) is $10,000 or 12 months. Obstruction (s 19) is
$2,000 or 3 months with no continuing fine. Asserted.

### 6. A clamped vehicle stays at the owner's risk until everything is paid

s 15(4): release only by an officer's direction and after all expenses and charges are
paid (waivable under s 15(16)); where it was taken because the owner has an outstanding
warrant, release may be refused until the owner is arrested or surrenders or the warrant
is cancelled (s 15(5)). Unclaimed after one month, it may be sold after one month's
Gazette notice (s 15(14)). Asserted.

### 7. Heavy vehicle thresholds use different weights

Goods vehicles, concrete mixers and trailers count by maximum laden weight over
5,000 kg; mobile cranes and recovery vehicles by unladen weight over 2,500 kg; buses by
more than 15 seats excluding the driver (s 2). Asserted.

### 8. Officers may enter private parking places 8 a.m. to 6 p.m. on 6 hours' notice

s 15B(1)-(3): consent dispenses with notice inside those hours; outside them, entry needs
necessity and at least 6 hours' notice. Asserted. The text of (3) does not mention
consent; the encoding does not let consent alone justify entry outside hours.

## What would need doing before this is worth anything

- The Parking Places Rules (the actual parking offences, the deficiency-charge
  calculation and the compoundable offences) were not retrieved.
- "Within one month" in s 15(14) is modelled in whole months; day-level timing and the
  boundary at exactly 6 p.m. are not tested.
- Dates in s 6A are encoded as YYYYMMDD numbers.
- Shared-mobility removal and forfeiture (s 15(2), (8)-(13)) and corporate officer
  liability (ss 17, 17A) are unencoded and matter in practice.
- No case law was searched.
