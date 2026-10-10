# Small Motorised Vehicles (Safety) Act 2020 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, "version in force from 1/6/2026", as deposited at
`../../registers/source-bundle/SMVSA2020.txt`. The latest amendment annotated is
Act 5 of 2026 wef 01/06/2026, which added Part 2A (keeping unsafe devices).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**, not for how often other Acts cite it:
e-scooters and power-assisted bicycles are bought, ridden and kept at home by
ordinary people in Singapore. This row takes what an owner, rider or occupier meets:
the definitions (s 2), importing without approval (s 5), keeping an unsafe device and
who is presumed to keep it (ss 8A, 8B), entry into homes (s 10(2)), seizure (s 11),
refusing to answer (s 12(6)), false information (s 13), composition (s 14),
forfeiture by the Authority (s 15(2), (3)) and obstruction (s 19).

Not encoded: s 8 (breach of the purpose of an import approval), s 7 (cancellation and
appeal), the detail of the s 10 entry powers, administration (ss 16-18), secrecy
(s 20), corporate and partnership liability (ss 22, 23), service (s 25). The
regulations, which hold the safety requirements, the import approval rules, the
prescribed circumstances and the list of compoundable offences, were not retrieved.

## What the Act turns out to say

### 1. Since 1 June 2026, keeping an unsafe device is itself an offence

Part 2A, added by Act 5 of 2026, makes it an offence to keep "an unsafe device at any
place" without reasonable excuse, "knowing that, or reckless as to whether" it is
unsafe (s 8A(1)). An unsafe device is a small motorised vehicle that does not meet the
prescribed safety requirements (s 2(1)). The Act was previously about imports; this
reaches the device in the flat. (That the Act was previously import-only is read from
the Act 5 of 2026 annotations on ss 3, 8A, 8B and 10(8).) Maximum for an individual: $2,000 or 3 months; repeat
offender $5,000 or 6 months; any other person $4,000, repeat $10,000. Asserted.

### 2. The registered owner is presumed to be the keeper, even when someone else has it

s 8B(1) presumes, "unless the contrary is proved", that the keeper is (a) the
registered owner if there is one; only if not, (b) the person in immediate possession;
only if neither, (c) the occupier of the premises where it is found. Common property
under the Town Councils Act 1988, public places and prescribed premises are excluded
from (c), so a device with no registered owner and no one holding it, found on
common property (a void deck is, by inference, such property), is presumed kept by no one. The "registered owner"
of a deregistered device is the person last recorded. Asserted (the order, not the
deregistration rule).

### 3. A device can be seized without warrant, and forfeited at once if it is a fire risk

s 11(1): an officer who has reason to believe a vehicle is connected with an offence
under s 5, 8 or 8A may seize it without warrant, whether or not the owner is present;
notice is owed to a known owner unless seized in the owner's or agent's presence
(s 11(3)). Entering and searching a home, though, needs the occupier's consent or a
court warrant (s 10(2)(a)). Ordinary forfeiture by the Authority needs four things
together: the vehicle is non-compliant or unsafe, it was the subject of an offence, 30
days have passed with no claim by a third party (the owner's own claim does not count),
and a conviction or composition (s 15(2)). But s 15(3) lets the Authority forfeit "at
once" a non-compliant or unsafe vehicle that is dangerous to keep or whose detention
"materially increases the likelihood of an outbreak of fire at the holding yard".
Asserted.

### 4. A motor is part of the definition, and an e-bike is never a PMD

A personal mobility device must be propelled by an electric motor, or by human power
and such a motor; a kick scooter is not one. A power-assisted bicycle, a trolley,
inline skates and wheeled toys are carved out of the PMD definition, and a PAB is its
own category (s 2(1)). Both definitions reach partly assembled vehicles; the third
limb, unassembled kits, comes into operation only on a date the Minister appoints by
Gazette notification (s 1(2)), and the deposit does not say whether that has
happened, so it is an input here. Asserted.

### 5. Obstruction: refusing an officer is excused only if both failures occur

s 19(2) excuses refusal to comply only where the officer "(a) fails to declare his or
her office; **and** (b) refuses to produce his or her identification card on demand".
Read as written, refusing an officer who declares the office but withholds the card is
still an offence ($5,000 or 6 months), though s 18(3) separately
requires the card to be produced before exercising a power. Asserted.

### 6. Smaller points

- Importing without approval: $5,000 or 6 months for an individual, $10,000 for others,
  doubled for a repeat offender convicted of the same offence within 5 years (s 5(3),
  (4)). Treating a conviction exactly 5 years earlier as within the period is an
  inference. Asserted.
- Self-incrimination is expressly a reasonable excuse for refusing to answer (s 12(6)).
  Asserted.
- Composition is capped at the lower of half the maximum fine and $5,000 (s 14(2)), and
  only for offences prescribed as compoundable. Asserted (the cap only).
- False information is an offence only if false or misleading in a material particular
  (s 13(2)). Asserted.

## What would need doing before this is worth anything

- The safety requirements (the content of "unsafe device") and the list of compoundable
  offences live in regulations that were not retrieved.
- Whether s 2(1) paragraph (c) of each definition has been brought into operation was
  not checked.
- The Active Mobility Act 2017 definitions incorporated by s 2(2), and the registration
  schemes s 8B relies on, were not read.
- No case law or LTA guidance was searched.
