# Public Transport Council Act 1987 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/PTCA1987.txt`. The edition says it incorporates
amendments up to 1 December 2021. Later amendments shown in it run to Act 17 of 2025
(in force 23 September 2026) and S 669/2025 (in force 9 October 2025).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the parts a
passenger, driver, transport operator or payment-service provider meets: fare evasion
and the penalty fee (ss 2, 52-55, 57, 58), not paying a taxi or ride-hail fare (s 56),
repeat offenders and maximum punishments, the rules on charging fares (s 41), the
ticket payment service licence (ss 28, 64), the Fuel Equalisation Fund penalty and
appeals (ss 33, 40), composition (s 67) and the fare adjustment formula (s 49, Third
Schedule). Not encoded: the Council itself and its finances (Parts 2-4), licence
conditions, codes and suspension, street-hail and ride-hail pricing policy orders, the
procedure for approving and reviewing fares, contributions from fare increases,
investigations, and offences by bodies corporate.

## What the Act turns out to say

### 1. A bus or train fare below the published fare is still an offence; a taxi fare below it is not

s 41(1)(c) and (2)(c) forbid a bus or train fare that "is different from" the fare
last published. s 41(3)(b) and (4)(b), for street-hail and ride-hail fares, forbid
only a fare that "is more than" the published one. s 41(8) makes the offence strict
liability, and s 41(10) says it binds the LTA, public bus operators and their
employees. Undercharging a bus passenger therefore contravenes s 41 on the text, while
undercharging a taxi passenger does not. Asserted.

### 2. Paying the penalty fee ends the matter, and the Council's appeal decision is final

s 53(1) lets a public transport official offer a penalty fee "of the prescribed
amount" (the amount is in regulations, not deposited). An appeal lies to the Council,
which may cancel an offer that is "not equitable", and "every decision on appeal is
final" (s 53(4)). Under s 53(8) a person who pays "cannot be prosecuted for an offence
under section 54 or offered composition under section 67". If it is not paid in time,
the offer is withdrawn (s 53(6)). Asserted.

### 3. Not tapping out is evasion only after the journey; and failing to show a ticket is presumed evasion

s 54(4)(a)(ii), for someone attempting to travel, makes failing to "tap in" evasion.
(b)(ii), for a journey travelled, adds "or tap out". s 54(5) presumes evasion,
"until the contrary is proved", where the passenger produces no ticket, a concession
ticket without evidence of entitlement, or an invalid ticket followed by no valid one.
Over-travel makes a ticket invalid only "without reasonable excuse" (s 2). Asserted.

### 4. Repeat-offender status counts only the same kind of offence

A repeat fare evader is one with an earlier s 54(1) conviction or one under s 24C(5)
as in force before 29 February 2016 (s 54(2)-(3)). For street-hail non-payment the
earlier conviction must be under s 56(1) or the old s 24D; for ride-hail, under s 56(2)
or the old s 24D (s 56(4)-(5)). An earlier ride-hail conviction does not make a later
street-hail non-payer a repeat offender. The maximum goes from a $1,000 fine to $2,000
or 6 months or both. Asserted.

### 5. You may refuse to give your name if the official will not show a card

s 57(2) makes refusing to give name and address to an official requiring a penalty fee
an offence ($1,000). But s 52(2): "It is not an offence for any person to refuse to
comply" if the official refuses, on demand, to declare office and show an
identification card. Arrest without warrant (s 58) needs both an unknown name and
address and either a refusal to give them or reason to doubt them. Asserted.

### 6. The fare formula carries a net +1.0%, and unused headroom carries forward

The Third Schedule formula as amended by S 669/2025 is "0.5 cCPI + 0.4 WI + 0.1 EI −
0.1% + 1.1%". The two constants net to +1.0%, so with no change in prices, wages or
energy the formula still allows a 1% increase. Under s 49(2) the shortfall below the
formula maximum may be claimed in a later year, though the Council may refuse it if
no claim is made (s 49(3)). Asserted, with every term treated as a percentage (an
encoding choice). The 2025 "first" and "second" 18-month periods in para 2 overlap
(1 January 2024 to 30 June 2025, and 1 January 2023 to 30 June 2024). Noted, not
asserted.

### 7. The penalty and composition caps

s 64: an unlicensed ticket payment service carries up to $50,000 or 6 months or both,
plus up to $5,000 for every day or part of a day it continues after conviction. s 41(5):
a street-hail or ride-hail licensee offering fares inconsistent with the pricing
policy faces up to $100,000. s 33 (Act 17 of 2025): a Fuel Equalisation Fund penalty
of up to $100,000, appealable to the Minister within 14 days (s 40). s 67: composition
is capped at the lower of half the maximum fine and $10,000. A smartcard certificate
served at least 56 days before the hearing is conclusive proof unless the accused gives
notice under s 55(10). Asserted.

## What would need doing before this is worth anything

- The prescribed penalty fee amount, the prescribed period for appealing it, and the
  list of compoundable offences are in regulations that were not retrieved.
- s 54(4)(c) (prescribed acts or omissions) is not encoded.
- The fare formula is encoded as a bare number; how the Council applies it to
  individual fares, and the s 47/48 procedures, are not.
- No decided cases or Council decisions were searched.
