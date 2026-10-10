# Optometrists and Opticians Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments to 1 December 2021),
informal consolidation, version in force from 5/12/2025, as deposited at
`../../registers/source-bundle/OOA2007.txt`. The latest amendment annotated is Act 19
of 2025 wef 05/12/2025 (s 34); Act 11 of 2023 wef 01/05/2023 and S 249/2009 (the
Schedule) are also shown.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0021**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. This row takes
what an optician, optometrist, eye-care shop or customer meets: which acts are
reserved and to whom (s 2, the Schedule, ss 3, 25(6), 35(2), 39), unlawful practice
and employment (s 25), fees for unlawful work (s 26), the registered person's
deadlines (ss 13(3)-(5), 16(3), 17(2), 18(4)-(6), 22, 24(3)), the Board's disciplinary
measures (s 20(3), (4)), the maximum penalties and the composition cap (s 29). The
Board and its procedure, the registers, the regulations and everything they
prescribe (classes of registration, qualifications, fees), refusal grounds, costs,
committees, inspectors' powers, service of documents and exemption orders are not
encoded.

## What the Act turns out to say

### 1. An optician may test your eyes but may not prescribe

Part 1 of the Schedule (opticianry) gives the optician refraction, "an eye
examination to measure the power of vision" (s 2), for persons 8 or older, plus
interpreting prescriptions and dispensing and fitting optical appliances. It has no
prescribing item. Prescribing spectacles or contact lenses is only in Part 2
(optometry). Asserted.

### 2. Children under 8 and contact lenses are for optometrists only

Opticianry refraction stops at "persons of 8 years of age or older", and items 3 and
4 of Part 1 exclude contact lenses. An optician who refracts a 6-year-old or fits
contact lenses is carrying out optometry without being qualified for it, an offence
under s 25 (up to $25,000 or 6 months; $50,000 or 12 months on a repeat conviction).
Asserted.

### 3. The old contact lens practitioners became opticians, who may not fit contact lenses

s 39(1) deems every contact lens practitioner licensed under the repealed Contact
Lens Practitioners Act to be registered as an **optician** with a practising
certificate for "any practice of opticianry". As the Schedule now reads (after
S 249/2009), opticianry excludes contact lenses. On the Act's text alone, the deemed
optician may dispense spectacles but not fit contact lenses. The Minister may
prescribe conditions under s 39(1); none was retrieved, and whether the Schedule read
differently before S 249/2009 was not checked. Asserted, on the text alone.

### 4. Only ophthalmologists are outside the Act, not doctors generally

s 3 disapplies the Act only to "any ophthalmologist", meaning a specialist registered
in ophthalmology (s 2). A general practitioner is given no carve-out, so on the text a
GP who performs refraction needs registration as an optometrist or optician. An
exemption order under s 35(1) could say otherwise; none was retrieved. Students on a
Board-accredited course are covered by s 35(2). Asserted.

### 5. Selling ready-made reading glasses is, on its words, opticianry

"Optical appliances" covers "spectacles, eyeglasses ... for the aid or correction of
visual ... anomalies", and opticianry includes "supplying ... all optical appliances".
The text draws no line at off-the-shelf readers. Treating them as optical appliances
is this encoding's literal reading. A s 35(1) exemption order or the regulations may
take them out; neither was retrieved. Asserted, as a literal reading.

### 6. Some grounds leave the Board only the choice to cancel

Censure, a penalty of up to $10,000, or conditions or suspension of up to 3 years are
available "instead of cancelling" only on grounds (e) to (l) of s 20(3). Registration
obtained by an incorrect statement, a qualification withdrawn, a foreign registration
cancelled, or ceasing to practise (grounds (a) to (d)) leave cancellation or nothing
(apart from dismissing a complaint without merit, s 20(5)). Asserted.

### 7. A fee for unlawful work cannot even be kept

s 26: no one may "demand, claim, accept, receive, retain or sue for or recover" a fee
for an act done in contravention of s 25, so a fee already paid may not be retained.
An employer of an unqualified person has a defence only if it proves both that it did
not know and that it exercised due diligence (s 25(5)). Asserted.

### 8. The deadlines

A change of name or address within 28 days (s 13(3)), though an NRA change-of-address
report counts only for the residential address (s 13(5)); an appeal against refusal
to the Minister within 30 days, final (s 16(3)); a disciplinary appeal to the General
Division within 14 days unless the court allows more, with no further appeal (s 22);
practising certificate renewal at least 30 days before expiry, or a late fee (s 18(4),
(5)); surrender of certificates within 14 days of notice (ss 17(2), 18(6)); and no
re-registration until 3 years after cancellation, then at most once in 12 months
(s 24(3)). Composition is capped at the lower of half the maximum fine and $2,000
(s 29). Asserted.

## What would need doing before this is worth anything

- The regulations under ss 15(3) and 37 (classes of registration, qualifications,
  fees, the late application fee, compoundable offences, practice conditions) were not
  retrieved; s 25(1) also requires practice "in accordance with the prescribed
  conditions", which is not modelled.
- No exemption order under s 35(1) was retrieved; findings 4 and 5 may be displaced by
  one.
- The pre-2009 Schedule was not read, so finding 3 is about the current text only.
- Month and day counts are whole numbers; how "within 28 days" or "before the expiry
  of 3 years" is counted at the boundary is the encoding's choice.
- No Board decisions or case law were searched.
