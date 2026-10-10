# Bus Services Industry Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 17
of 2025 (in force 23 September 2026) shown. Deposit: `../../registers/source-bundle/BSIA2015.txt`.

**Checks:** one case file, 116 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes the rules an
operator, an investor in an operator, or a bus passenger actually meets: what a "bus
service" and a "regular route service" are and the licence classes (s 2), unauthorised
operation of a bus service, depot or interchange (ss 11, 22), the 5% controller notice
and 25% / 50% / 75% controller approvals for designated entities (ss 28B, 28F, 28G,
28R), and the new Part 7A conduct rules on buses and at interchanges (ss 42AA to 42AE,
42AG(2), (3)), with the penalty for each. The procurement framework, the licensing
discretion, step-in, special administration, enforcement, appeals and everything left
to regulations are not encoded.

## What the Act turns out to say

### 1. Selling down needs approval as much as buying up

s 28G(1)(b): without the LTA's prior written approval a person must not, "as a result
of a decrease", **cease** to be a 25%, 50% or 75% controller of a designated entity.
Going from 30% to 10% needs approval just as going from 10% to 30% does; moving within
a band (30% to 49%, 60% to 55%) does not. Transactions entered into before the
effective designation date are outside it (s 28G(2)). Asserted.

### 2. Jumping straight past 5% skips the 5% notice

s 28B defines a 5% controller as holding "5% or more, but less than 25%". A person
who goes from 3% to 30% in one step never "becomes a 5% controller", so on a literal
reading the 7-day notice in s 28F(1) is not engaged — though s 28G approval is. A
decrease into the 5% band does not trigger s 28F either, which is limited to "an
increase". The single-number banding (the larger of equity and voting power) is an
inference; the definitions are framed "or". Asserted.

### 3. Wilful damage carries twenty times the fine for endangering lives, but under a fifth of the prison term

s 42AD (wilfully damaging a bus, depot or interchange): up to $200,000 or 12 months.
s 42AC (wilfully endangering the safety of anyone travelling): up to $10,000 or 5
years. Compensation for damage under s 42AE is payable "whether wilfully or
otherwise", on top of any penalty. Part 7A was inserted by Act 17 of 2025 and came
into force on 23 September 2026. Asserted.

### 4. A bus captain can ask to look in your bag, but not frisk you

s 42AA(2) lets any "approved person" — including an employee of a Class 1 operator
authorised by the LTA in writing — ask a passenger to walk through a detector, X-ray
or open a bag. Only a police officer or a "senior approved person" (auxiliary police,
a security officer engaged by the operator, or an outsourced enforcement officer) may
ask for a frisk search or a hand-held scan of the person (s 42AA(3)). Refusing without
reasonable excuse is an offence ($1,000), except where a plain-clothes police officer,
or an approved person, has not declared his or her office (s 42AA(7)). For an
outsourced enforcement officer the carve-out needs **both** a failure to declare
office and a refusal to produce the identification card. The encoding assumes each
person holds the LTA's written authorisation. Asserted.

### 5. A small unlicensed operator faces no prison; an unlicensed depot does

s 11(2): operating 10 or more regular route services without authority — $50,000 or 6
months, $5,000 a day continuing; "in any other case" — $10,000 and $500 a day, with
**no** imprisonment. Operating a bus depot or interchange without authority (s 22(2))
carries $10,000 **or 6 months**. "Operate" excludes merely driving, registering or
maintaining a bus, and for depots merely repairing, refuelling or (since Act 17 of
2025) charging one. Asserted.

### 6. Tourist, community and courtesy buses are still "bus services"

They are excluded from "regular route service" only. A community or courtesy service
is defined as provided "for a fare, or for consideration which is limited to the
costs", so if it runs to a timetable on a fixed route with two or more stops it is a
bus service that s 11 requires to be licensed or exempt. A free shuttle has no
"fare" and is not a bus service at all. Asserted.

### 7. The licence classes leave a gap (inference)

Class 1 authorises "10 or more regular route services"; Class 2 "a single bus
service". The s 2 definitions name no class for a licence covering 2 to 9 services;
the encoding returns `no class defined in s 2`. Whether such a licence is issued in
practice was not checked. Asserted.

### 8. Dangerous items: buses and interchanges, not depots

s 42AB bars taking a dangerous item (weapons, petroleum, hazardous or corrosive
substances, prescribed items) on board a bus or into a bus interchange without the
express permission of a police officer or approved person ($5,000). The section does
not name bus depots. Subsection (4) — no offence if the item is disposed of before
boarding — adds little on its face, since an item disposed of was not taken on board.
Asserted.

## What would need doing before this is worth anything

- "Associate", "indirect controller" and "equity interest" (ss 28B to 28D) and the
  designation process (s 28E) were not encoded; the controller bands are applied to a
  single percentage supplied by the user.
- Ministerial exemptions under s 46 and orders excluding services from "regular route
  service" were not retrieved; the "prescribed" dangerous items and Part 7A
  regulations were not retrieved.
- The s 28G defences in (9) and (10) and the s 28H, 28I approvals were read but not
  encoded.
- No case law, LTA guidance or subsidiary legislation was searched.
