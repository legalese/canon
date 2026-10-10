# Transboundary Haze Pollution Act 2014 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/THPA2014.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021"; the only later amendment annotated
in the body is Act 31 of 2022 (wef 1 November 2022) on s 17, which is not encoded.

**Checks:** one module (`thpa-haze.l4`), one case file (`thpa-cases-haze.l4`), 57
assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0080**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. The Act is
short, and the row takes what a business (and its officers) actually meets: the
meaning of haze pollution in Singapore (s 2), participation in management (s 3),
the offences and maximum fines (s 5), civil liability (s 6), the defences (s 7),
the presumptions (s 8), when a preventive measures notice may be given (s 9), the
information-notice, falsification and obstruction offences (ss 10(6), 10(7), 14),
deemed service by registered post (s 15(2)(b)), officers' liability (s 16) and the
composition ceiling (s 19). Not encoded: the investigation powers themselves
(ss 10(1) to (5), (8) to (11), 11), ss 12, 13, other modes of service, and ss 17,
18, 20 to 24.

The prescribed air quality index number (s 2(2)(a)) and the list of compoundable
offences (s 19(1)) are in regulations that were not retrieved. The index number is
a parameter; the cases use 100 purely as an illustration.

## What the Act turns out to say

### 1. The offences and the civil duty bind entities, not individuals as such

s 5(1), (3) and s 6(1), (2) are framed against "an entity", defined as "any sole
proprietorship, partnership, corporation or other body of persons". A smallholder
acting alone is outside them; a sole proprietorship is inside. Individuals come in
through s 16: an officer or partner of a body corporate, unincorporated
association or partnership that commits the offence is guilty of it unless he or
she proves BOTH no consent, connivance or privity AND all due diligence. Asserted.

### 2. Up to $100,000 a day, plus $50,000 a day for ignoring a notice, capped at $2 million

s 5(2), (4): a fine not exceeding $100,000 "for every day or part of a day" of
haze, plus, if a preventive measures notice was not complied with, $50,000 for
every day of non-compliance; s 5(5) caps the aggregate at $2 million. Twenty days
of haze alone reach the cap. There is no imprisonment under s 5. Asserted.

### 3. A parent or manager can be liable for its subsidiary's land

s 5(3) and s 6(2) reach an entity that "participates in the management" of the
landowner. s 3 says when, "if, and only if": actual participation, decision-making
control over the haze-causing decision, or manager-level responsibility for
day-to-day decisions or a substantial part of operational (not financial or
administrative) functions. Asserted.

### 4. The burden is reversed, link by link

s 8(4): ownership is presumed from a map supplied under a s 10 notice, by a foreign
government or its agencies, or by a prescribed person. s 8(1): haze is presumed to
involve smoke from a fire abroad if the meteorological data show the smoke moving
toward Singapore, "even though" other fires are burning. s 8(2): the owner is then
presumed to have caused or condoned it; s 8(3): a managing entity too, though its
participation must itself be proved. A map from a campaign group or a newspaper is
not in the list. Asserted.

### 5. The "someone else did it" defence excludes most of the people who would do it

s 7(2), (4): conduct by another person without the entity's knowledge or consent is
a defence to the causing limb, but not if that person is an employee, an agent, a
contractor engaged to work on the land or the contractor's employee, or a holder of
a customary right with whom the entity has a farming or forestry agreement. A
trespasser or a customary-right holder with no agreement can found it. To the
condoning limb (s 7(3)) the defence is reasonable measures to prevent and, once the
conduct has occurred, to stop or reduce it. A grave natural disaster or act of war
as the sole cause (s 7(1)) answers every limb. Asserted.

### 6. Civil claims need harm in Singapore, and foreign law is irrelevant

s 6(3): a person in Singapore may sue for personal injury, disease, incapacity or
death in Singapore, physical damage to property in Singapore, or economic loss
including lost profits in Singapore. s 6(4): actionable "whether or not that conduct
is also actionable in the foreign jurisdiction". That damage to property abroad, or
annoyance with no injury, damage or loss, falls outside is an inference from the
closed list. Asserted.

### 7. A preventive measures notice needs no haze in Singapore yet

s 9(1): air pollution in Singapore OR in any part of a country outside Singapore
from a fire abroad, with the smoke likely to move toward Singapore, is enough for
the Director-General to give a notice to an involved entity. Asserted.

### 8. Composition is capped at $5,000 whatever the offence

s 19(1): the lower of half the maximum fine and $5,000. For a $2 million s 5
offence that is $5,000; for the s 10(6) offence ($5,000 or one month) it is $2,500.
Which offences are compoundable is prescribed elsewhere. Asserted as a ceiling.

## What would need doing before this is worth anything

- The regulations prescribing the air quality index number and the compoundable
  offences were not retrieved.
- Whether "every day or part of a day" counts a day of haze anywhere in Singapore,
  or only days linked to the entity's conduct, is not settled by the text; the
  encoding takes a count of days as given.
- The evidential presumptions are modelled as booleans; nothing models how
  "until the contrary is proved" is discharged.
- No case law or prosecutions under the Act were searched.
