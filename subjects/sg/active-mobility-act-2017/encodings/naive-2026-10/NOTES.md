# Active Mobility Act 2017 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 5
of 2026 shown (provisions in force 27 February, 4 May and 1 June 2026).

**Checks:** one case file, 135 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
rider meets on a public path: which vehicle may go on which kind of path (ss 15, 16,
17), the maximum penalties for the Part 3 Division 2 offences and who is a repeat
offender (s 2), using a phone while riding (s 22A), the duties after an accident
(s 23), and riding a motorised PMD under the minimum age and facilitating it
(ss 23A, 23B). Declaring paths, access agreements, banned and non-compliant
vehicles beyond their penalties, registration (Parts 3A, 3B), competency tests and
certificates of medical need, dealing in devices (Part 4), enforcement (Part 5) and
rider insurance (s 58A) are not encoded. Speed limits, minimum riding and
supervising ages, and banned descriptions are all left to regulations, none of
which was retrieved: the ages are inputs here.

## What the Act turns out to say

### 1. A property-only accident carries no offence for riding off

s 23(1) gives the driver duties after any accident in which someone is injured
**or** property (including an animal) is damaged. But the offence in s 23(3)
needs an individual "killed or suffers injury", knowledge (actual or
constructive), and a failure under "subsection (1)(a), (b), (c), (d) or (e)".
Paragraph (f), the duty to report property damage at a police station, is not in
that list. So in the encoding, riding off after damaging only property, or missing
only the property report after an injury accident, is not a s 23(3) offence. No
other penalty for it was found in the sections read. Asserted.

### 2. Which vehicle is barred from which path is set by three sections, not a table

s 15 bars bicycles, PABs, PMDs and non-mobility motor vehicles from pedestrian-only
paths. s 16 bars only PABs, **motorised** PMDs and non-mobility motor vehicles from
footpaths, so a bicycle or a kick-scooter may use a footpath. s 17 bars from shared
paths every motor vehicle except a PAB, PMD or mobility vehicle. A mobility vehicle
is barred from none of them; s 2(1) counts its rider as a "pedestrian". Asserted.

### 3. The crossing and obstruction exceptions are for riders, not drivers

Crossing "by the shortest safe route", or travelling "no more than reasonably
necessary" to avoid an obstruction on an adjacent area, excuses a bicycle, PAB or
PMD on a pedestrian-only path (s 15(2)), and a PAB or motorised PMD on a footpath
(s 16(2)). It never excuses a car or motorcycle. The only motor-vehicle exception is
a mechanised sweeper cleaning paths in the course of employment (ss 15(3), 16(3),
17(2)). Asserted.

### 4. Dangerous riding has no repeat-offender tier; speeding outranks the path offences

Almost every offence doubles or more for a repeat offender (an earlier conviction
for the same offence within 5 years, s 2(1)). s 22(2), dangerous riding, does not:
$10,000 or 12 months either way. Speeding (s 21(3)) carries up to 6 months for a
first offence, twice the 3 months for riding on the wrong path. A non-compliant
vehicle (s 19(3)) carries the highest fine: $10,000, or $20,000 for a repeat
offender. Asserted.

### 5. Renting an e-scooter to a child can be facilitation; selling one cannot

s 23B(4): "facilitate" "excludes mere advertising and selling (but not letting for
hire)". The person must also know of, or be negligent as to, both the age and the
absence of an escort, and the child must actually ride. A defence lies in reasonable
inquiries on reasonable grounds, or in reasonably accepting evidence of age from the
rider. The encoding applies the intent-or-recklessness element of "facilitate" only
to lending and hiring, not to inviting or allowing (an inference from the definition's
placement). Asserted.

### 6. A phone in the hand is not enough, and a smart watch is outside

s 22A needs the device held in the hand **and** a function operated, while the
vehicle is moving on a public path. "To avoid doubt" the section does not reach a
self-driving vehicle or a wearable worn as the manufacturer intended. Asserted.

### 7. An escort must be in sight, not merely present

s 23A(4): "riding under escort" needs an arranged supervisor of the prescribed
minimum supervising age, on or near the shared path, with "a clear and unobstructed
line of sight" of the rider. A parent who has lost sight of the child is not an
escort. 23A applies only on a shared path; a motorised PMD on a footpath is already
an offence under s 16. Asserted.

## What would need doing before this is worth anything

- The regulations: speed limits (s 21), minimum riding and supervising ages
  (s 23A(5)), banned vehicle descriptions (s 18) and grace periods (s 19(4), (5)).
- The 5-year repeat-offender window is taken as inclusive; the text does not
  settle a conviction exactly 5 years earlier. The widened repeat-offender
  definitions in ss 16(5), 19(6) and 19A(5) are not modelled.
- s 23(1)(f) duplicates its paragraph letter "(f)" in the deposit; read as one
  paragraph.
- No cases on "reckless" or "dangerous to the public" (s 22) were searched.
