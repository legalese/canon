# Road Traffic Act 1961 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating the Road
Traffic (Miscellaneous Amendments) Act 2025, which restructured ss 64 and 65.

**Checks:** two case files, 164 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**34 of the 527 Singapore Acts** deposited here cite it. Its 447,000 characters
cover vehicles, licensing, schools, charges and parking; this row takes the
offences a driver can commit and what follows them.

## What the Act turns out to say

### 1. s 65AA(2) forfeits a vehicle for an offence under a subsection that is not an offence

s 65AA(2): forfeiture follows a conviction for dangerous driving causing death "or
section 26(2) of the Police Force Act 2004 (which offence is committed on or after
1 November 2019)". In the Police Force Act as deposited here (see the
`police-force-act-2004` row), s 26(2) is the police officer's **power to order** a
driver to stop at a barrier; the offence of failing to stop is s 26(5), punished
under s 26(8). Act 21 of 2021 rearranged s 26 with effect from 1 January 2022; s 65AA
was not updated. Read literally, no one can be convicted "under section 26(2)".
Asserted as that pair.

### 2. The 2025 restructuring dropped the base offences from the enhanced-penalty list

s 67A lets a court triple the punishment on a third "specified offence". Since the
2025 amendments, dangerous and careless driving with no harm are s 64(5) and s 65(5).
s 67A(3) lists s 64(1) and s 65(1) only "as in force immediately before" the
amendments, and the new harm offences (ss 64(2) to (4), 65(2) to (4)). **Neither
s 64(5) nor s 65(5) is on the list**, and the deposited text cites "64(5)" nowhere.
The same dangerous driving counts towards enhancement if committed before the
amendment and not if committed after, unless it hurt someone. Asserted.

### 3. Driving without a licence outranks dangerous driving

s 35(3): driving without a licence carries up to **3 years** (6 for a repeat
offender). Dangerous driving that harms no one carries up to 12 months (s 64(5)(a));
careless driving 6 months (s 65(5)(a)). Asserted.

### 4. No minimum disqualification for a sober first offender who kills

s 64(9) and s 65(9) prescribe minimum disqualifications for repeat, serious
(drink-driving) and serious repeat offenders -- up to 15 years, and life on a third
drink-related conviction (s 64(10)). They prescribe **none** for a sober first
offender, whatever the harm: dangerous driving causing death by a first offender
attracts up to 8 years' imprisonment and no minimum disqualification under s 64(9).
(The general disqualification power in s 42 is not encoded.) Where a driver is both
a repeat and a serious offender, (9) does not say which period applies; the encoding
takes the longer. Asserted across twenty driver profiles.

### 5. Lending your car to a drunk friend can cost you the car

s 65AA(1): where a drunk (serious or serious repeat) driver causes death or grievous
hurt, the court "is to" forfeit the vehicle unless the offender is not the owner
**and** used it without the owner's consent. A lent car is used with consent, so it
goes, and there is no residual discretion. Under s 65AA(2), for a sober driver who
kills by dangerous driving, the court may decline for "other good reasons". Asserted.

### 6. The phone offence needs hand, operation and motion

s 65B(1): a driver who "holds in his or her hand" a device and "operates" a function
"while the vehicle is in motion". A cradled phone, a phone used at a red light, and
a smartwatch worn as intended (s 65B(1A)) are all outside it. Asserted.

### 7. After a minor accident, a note may not be enough

s 84(1), (2): after damage with no one at the scene, the driver must take reasonable
steps to tell the owner, and must report to the police within 24 hours **unless** the
owner then contacts the driver. A note left on a windscreen that brings no call does
not discharge the duty to report. Asserted.

### 8. Smaller things worth recording

- **s 67:** drink-driving carries a **minimum** fine of $2,000 ($5,000 and mandatory
  imprisonment on a second conviction), and disqualification of at least 2 years,
  5 on a repeat, life on a third.
- **s 64(11)(b):** two earlier convictions for speeding by more than 40 km/h within
  five years make a driver a "repeat offender" for dangerous and careless driving.
- **s 64(6)(b), (7)(b):** a repeat dangerous driver who kills faces at least 2 years;
  one who causes grievous hurt at least 1 year.

## What would need doing before this is worth anything

- **The prescribed alcohol limit and the rules** were not retrieved.
- **No case law was searched.** Sentencing frameworks for ss 64 and 65 are extensive.
- The general disqualification power (s 42), speeding (s 63) and the remaining Parts
  are not encoded.
