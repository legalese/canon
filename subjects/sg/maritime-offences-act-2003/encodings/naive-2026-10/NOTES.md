# Maritime Offences Act 2003 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation; the deposit labels itself
"version in force from 1/7/2025". The latest amendment annotated is Act 3 of 2021
(wef 1 July 2025), in the s 2 definition of "act of violence"; Act 17 of 2022 is
annotated against s 15.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. The Act is short (15
sections), so this row takes most of it: the definitions of ship and fixed platform
(s 2), the exclusion for warships and other service vessels, hijacking (ss 3, 8),
destroying or damaging a ship (s 4), false information (s 5(3), (4)), threats (s 6(1)),
penalties (ss 7(5), 11(4), 12(7), 13), the master's power of delivery (s 12), the
Public Prosecutor's consent (s 14) and extradition with non-treaty countries (s 15).
Not encoded: damage to navigation facilities (s 5(1), (2)), threats to them (s 6(2)),
the fixed-platform damage and threat offences (ss 9, 10) beyond their penalties, the
deeming of connected violence into Singapore (ss 7(1), 11(1)) beyond its penalty, and
s 15(5).

## What the Act turns out to say

### 1. Attempt is capped at 15 years; abetment carries life

ss 7(5) and 11(4) expressly punish an attempt with imprisonment "not exceeding 15
years". The abetment offences in ss 7(3), (4) and 11(2), (3) carry no express penalty,
so s 13(1) applies: "imprisonment for life". On the text, abetting a hijacking is
punishable more severely than attempting one. The principal offences (ss 3 to 6, 8 to
10) likewise carry life by s 13(1). Asserted.

### 2. Reach is universal, except for foreign warships and service vessels

ss 3(1) and 4(4): the offences apply "whatever his or her nationality or citizenship,
whatever the state in which the ship is registered and whether the ship is in Singapore
or elsewhere". The only exclusion is an act against a warship, naval auxiliary, customs
or law enforcement vessel, and even that falls away if the offender is a Singapore
citizen, the act is in Singapore, or the vessel is in Singapore's service (ss 3(2),
4(5), 5(6), applied by 6(4); s 8(2) for platforms, with no warship limb). Asserted.

### 3. The master's safety defence covers notification only, not handing over evidence

s 12(7) makes it an offence (fine up to $5,000) to contravene s 12(4) (notify the
country before delivery) or s 12(6) (give statements and evidence after it), without
reasonable excuse. s 12(8)'s defence — belief on reasonable grounds that notifying
would endanger the ship — applies only to "a contravention of subsection (4)", and
for a country other than Singapore also requires notice to some other competent
authority in time or a reasonable belief that notifying any authority would also be
dangerous. Asserted.

### 4. Only a Singapore-registered ship may deliver to another Convention country

s 12(2): any master, wherever the ship is and whatever its flag, may deliver a
suspected offender to an appropriate officer in Singapore. s 12(3): delivery to "any
other Convention country" is open only to a ship registered in Singapore. Delivery
covers a "relevant maritime offence" against a ship other than a service vessel; the
text does not extend it to fixed platform offences. Asserted (the first two points).

### 5. Charging is allowed before the Public Prosecutor consents

s 14(1) forbids instituting a prosecution without the Public Prosecutor's written
consent, but s 14(2) lets a person be arrested, a warrant issued and executed, a
person charged and remanded or bailed before consent; "no further steps" after that.
Which later steps count is not listed; "taking a plea" and "proceeding to trial" are
this encoding's examples of further steps (an inference). Asserted.

### 6. False information must actually endanger navigation, and two defences exist

s 5(3) requires that the communication "endangers" safe navigation — not "is likely to
endanger", the wording of s 5(1) — and does not use "unlawfully". s 5(4) lets the
accused prove reasonable belief in the truth, or lawful employment to communicate
information and good faith. Asserted.

### 7. A ship that is laid up is not a ship

s 2 excludes from "ship" any vessel that permanently rests on or is attached to the
seabed, or "has been withdrawn from navigation or laid up". A fixed platform must be
permanently attached to the seabed for exploration, exploitation or another economic
purpose. Asserted.

### 8. Extradition with non-treaty countries depends on the Protocol

s 15(2), (3): where no treaty is in force, a Gazette notification may apply the
Extradition Act 1968 to a Protocol country for both maritime and fixed platform
offences, but to a Convention country that is not a Protocol country for maritime
offences only. Asserted.

## What would need doing before this is worth anything

- "Unlawfully" (s 2) and "act of violence" (s 2) are single input flags; neither is
  decided against the other written law they point to.
- ss 5(1), 6(2), 9, 10 and the deeming in ss 7(1), 11(1) and 15(5) are not encoded.
- No order appointing the "appropriate officer" under s 12(9), no prescribed form
  under s 12(4), and no case law were retrieved.
