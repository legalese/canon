# Chemical Weapons (Prohibition) Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CWPA2000.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amending Act annotated in the text is 2/2012, at s 26(2).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0088** in `subjects/sg/requirements.jsonl`. It sits in Tier 2 of the
remaining Singapore Acts, which are ordered by how often they touch everyday life. The
requirement asks what the Act decides for a person or business it applies to. No
scenario has asked a sharper question yet.

The row covers what a chemicals business or an individual actually meets:

- the definitions of "permitted purpose" and "chemical weapon" (s 2(1))
- the chemical-weapons offences and their defences (s 8)
- when a licence is needed (s 9(1) to (8))
- the maximum penalty for every offence in the Act
- obstruction of inspectors (s 25), confidentiality (s 26), reach outside Singapore
  (s 5(1)) and composition (s 30(1))

Not encoded:

- administration and forfeiture (ss 6, 10)
- the reporting and record-keeping duties themselves (s 12(1)). They turn on Parts VI
  to IX of the Convention's Verification Annex and on regulations that were not deposited.
- the Director-General's notices and directions (ss 13, 19(1))
- inspection powers and warrant procedure (ss 15 to 24, 27(1) to (3))
- liability of a company's officers (s 28) and court jurisdiction (s 29)
- the power to make regulations (ss 9(9), (10), (14), 32, 33)
- the Schedule's chemical lists. Which Schedule a chemical is in is taken as given.

## What the Act turns out to say

### 1. The same chemical, for the same industrial use, is lawful or a chemical weapon depending on its Schedule

Under s 2(1), the permitted purposes for a Schedule 1 chemical are only "research,
medical, pharmaceutical or protective". Every other toxic chemical is also permitted
for industrial, agricultural, military (not as a method of warfare) and law-enforcement
uses, riot control included. A toxic chemical is a "chemical weapon" unless it is
intended for a permitted purpose and its type and quantity fit that purpose. So a
Schedule 1 chemical held for an industrial process is, by definition, a chemical
weapon. The encoding infers that this puts it under s 8, with a maximum of life
imprisonment, rather than under the licensing offence in s 9(1), which covers only
dealings for a permitted purpose. A Schedule 3 chemical in the same plant is not. A Schedule 3
chemical held in a quantity that does not fit its industrial purpose is a chemical
weapon too. Asserted.

### 2. The innocent-holder defence covers using and holding, not developing or producing

Under s 8(3), the accused can prove that they did not know, suspect or have reason to
suspect, or that they reported promptly to an authorised officer. The defence is given
only for (1)(a) using, (c) acquiring, stockpiling or retaining, (d) transferring, (e)
military preparations and (g) using riot control agents in warfare. It is not given for
(b) developing or producing, or for (f) knowingly assisting. Section 8(4) keeps any
other defence open. The exemption in s 8(2) for officers and inspectors acting under
authority displaces the offence entirely. Asserted.

### 3. Licences follow the Schedule, and holding a Schedule 2 or 3 chemical needs none

Under s 9(1), every dealing in a Schedule 1 chemical needs a licence: use, development,
production, acquisition, stockpiling, retention and transfer. "Transfer" includes
import and export.

For a Schedule 2 chemical, s 9(2) requires a licence only to produce, process or
consume it. For a Schedule 3 chemical, a licence is required only to produce it. Under
s 9(4), importing or exporting either needs a licence. Acquiring, holding or using a
Schedule 2 or 3 chemical needs no s 9 licence. Asserted.

Processing and consuming are not words in s 9(1). The encoding infers that both are a
"use" of a Schedule 1 chemical.

### 4. A low-concentration mixture is free to import, but free to export only to a Convention party

Section 9(8)(a) lifts the import licence for a mixture within the "prescribed
concentration" of a prescribed Schedule 2 or 3 chemical. Section 9(8)(b) lifts the
export licence only for export "to a country that is a party to the Convention".
Mixtures are also exempt from s 9(1) and (2) (ss 9(5), (6)). The concentrations are in
regulations that were not retrieved. Asserted.

### 5. Unscheduled organic chemicals need a licence above 200 tonnes, or 30 tonnes with P, S or F

Section 9(3) requires a production licence above 200 tonnes a year in total of
unscheduled discrete organic chemicals. For any one such chemical containing
phosphorus, sulphur or fluorine, the threshold is 30 tonnes. The Act spells these
"phosphorous" and "sulfur". Exactly 200 or 30 tonnes needs no licence. Mixtures within
the prescribed concentration are left out of the count (s 9(7)). Asserted.

### 6. Refusing an inspector entry is not obstruction, unless the inspector has a warrant

Section 25(1) punishes wilfully obstructing, hindering, resisting or deceiving an
inspector, with a maximum of $15,000 or 12 months. Sections 25(2) and (3) say this does
not apply to a refusal to consent to entry by an inspector who is not acting under a
warrant. Asserted.

### 7. The penalty ladder, and a composition cap that the Act's own offences never fall below

- s 8: life imprisonment "and" a fine of up to $1 million. Every other offence says "or
  to both", so the encoding infers that both are imposed for s 8.
- unlicensed Schedule 1 dealing: $100,000 or 10 years
- other unlicensed dealing: $10,000 or 2 years (s 9(13))
- a false or misleading document: $10,000 or 2 years (s 14)
- obstructing an inspector, or obstructing a search: $15,000 or 12 months
  (ss 25(1), 27(4))
- failing a written direction, or breaching confidentiality: $6,000 or 12 months
  (ss 19(2), 26(3))
- failing to report or keep records, or failing to comply with a notice: $6,000 or
  6 months (ss 12(2), 13(4))

Section 30(1) caps composition at $1,000 where the offence's maximum fine is under
$5,000, and at $5,000 otherwise. No offence in the Act has a maximum fine under $6,000.
The encoding infers that the $1,000 tier can apply only to offences created by
regulations, which s 33(2)(e) allows with fines of up to $10,000. Asserted.

### 8. Only ss 8 and 26 reach outside Singapore

Under s 5(1), ss 8 and 26 extend to acts outside Singapore by a citizen, or by anyone
on board a ship or aircraft registered in Singapore. Under s 5(3), prosecution needs
the Public Prosecutor's consent. The encoding infers that the Act's other offences
reach only acts done in Singapore, because s 5 does not extend them. Under s 26(2),
confidential information may be disclosed only with consent, for the Convention, for
enforcement, or for a public-safety emergency or Singapore's security. Asserted.

## What would need doing before this is worth anything

- The regulations made under ss 9(9), (14), 12, 30(2) and 33 were not retrieved. They
  set the mixture concentrations, the licence terms and appeals, the reporting duties,
  which offences are compoundable, and any offences created by regulation.
- The Schedule's chemical lists are not encoded, so the encoding cannot tell which
  Schedule a named chemical is in.
- The munition and equipment limbs of "chemical weapon" (s 2(1)(b), (c)) and the
  reporting duties under s 12(1) are not modelled.
- No case law or Director-General practice was searched.
