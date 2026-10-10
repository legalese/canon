# Official Secrets Act 1935 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/OSA1935.txt`. The cover says it incorporates all
amendments up to and including 1 December 2021; the Schedule annotates later
changes, the latest being Act 17 of 2026 with effect from 1 July 2026. Section
numbers follow the body: the arrangement at the top of the deposit is one step out
of line with it (it lists "1." with no heading, then "2. Short title").

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0057**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. This row takes what such a
person meets: photographs and cameras at prohibited places (ss 3(2), (3), (5), 4),
wrongful communication and receipt (s 5), the specified organisations of the
Schedule, the presumptions (ss 3(6), 7), the duty to give information on demand
(s 10), harbouring (s 11), prosecution consent (s 14), directors and partners
(s 16(3)) and the maximum penalties (s 17). Not encoded: the spying offence of
s 3(1) beyond its penalty, what is a prohibited place (a given fact here), the
Minister's orders on seized photographs, the s 6 uniform and forgery offences and
s 8 obstruction beyond their penalties, the s 9 message warrant, attempts (s 12),
arrest and search (ss 13, 15), place of trial and closed hearings, and ss 17A-19.

## What the Act turns out to say

### 1. A photograph inside a prohibited place carries the spying penalty, and the burden is on the photographer

s 3(2) needs no prejudicial purpose: anyone who takes a photograph "of or within a
prohibited place" is guilty "unless he proves" it is not prejudicial and not
intended to be useful to a foreign Power. It is an offence "by reason of section 3",
so s 17(1) sets the maximum: $20,000 and 14 years, the same as spying under s 3(1).
A permit from the competent authority (s 3(3)) is the only other way out. Asserted.

### 2. Outside the fence the burden flips, unless you are in an aircraft

The proviso to s 3(2): a photograph taken outside a prohibited place that happens to
include it is an offence only if an intent to prejudice "is proved". "This proviso
does not apply to any photograph taken from an aircraft", so an aerial photograph is
back under the reverse burden. Asserted.

### 3. Merely having a camera inside is a $200 matter, and residents are exempt

s 4(1): possessing photographic apparatus within a prohibited place without a signed
written permit is an offence with a maximum fine of $200 and no imprisonment, but not
for a person residing within that place. The gap between s 4 ($200) and s 3(2)
(14 years) is the gap between holding the camera and pressing the shutter. Asserted.

### 4. The Act reaches contractors of statutory boards, and their employees

s 5(1)(e) covers information obtained as a holder of "a contract made on behalf of
the Government or any specified organisation", or as an employee of such a
contractor. The Schedule names, among others, HDB, the CPF Board, IRAS, MAS, GIC and
its subsidiaries, and (added in 2025-2026) the Communicable Diseases Agency, the
National Council of Social Service, the Public Transport Council and the Skills and
Workforce Development Agency. Communicating such information to an unauthorised
person, or merely failing to take reasonable care of it (s 5(1)(i)), is an offence.
Asserted for a selection, with two bodies the Schedule does not name.

### 5. Receiving is an offence unless it was against your wishes

s 5(2): a person who receives protected information knowing or having reasonable
ground to believe it was communicated in breach is guilty unless he proves "that the
communication to him ... was contrary to his desire". Asserted.

### 6. Every person must answer a sergeant, and must turn up if expenses are paid

s 10 makes it the duty of "every person" to give on demand any information in his
power about an offence or suspected offence under the Act to a police officer not
below sergeant (or a person given those powers by the Minister under s 18), an armed
forces officer on duty, or a soldier on guard, sentry or patrol, and to attend when
required "upon tender of his reasonable expenses". Failure is punishable with up to
$2,000 and 2 years (s 17(3)). That a constable is below the rank of sergeant is an
inference; the Act does not define the ranks. Asserted.

### 7. Directors and partners share the company's guilt unless they prove ignorance

s 16(3): where a company or a partnership is guilty, every director, officer or
partner is guilty of the like offence "unless he proves" it happened without his
knowledge or consent. Asserted.

### 8. Two penalty provisions reach a false permit application

s 3(5) gives its own penalty for a false declaration to obtain a permit ($2,000 before
a District Court, $1,000 before a Magistrate's Court, no imprisonment), but s 17(1)
applies $20,000 and 14 years to every offence "by reason of section 3". This encoding
applies s 3(5)'s own figures; that the specific provision governs is an inference.
Asserted (on the inference).

### 9. Consent gates the trial, not the arrest

s 14: no prosecution without the Public Prosecutor's consent, but the person may be
arrested and remanded before it; until consent "he shall not be called upon to
plead". s 17(2) also needs the Public Prosecutor's consent for a Magistrate's Court
trial of a s 5, 6, 8 or 11 offence; s 17(3) gives Magistrate's Court figures for
ss 9 and 10 without mentioning consent. Asserted.

## What would need doing before this is worth anything

- No gazetted prohibited-place orders or competent-authority notifications were
  retrieved, so whether any real place is "prohibited" cannot be answered.
- The deleted Schedule items 2 and 7 were not identified.
- The interaction of s 17(1) with s 3(5), and of s 17 with the Criminal Procedure Code
  2010 on which court may try s 3 offences, was not researched.
- "Fine ... and to imprisonment" is encoded as two maxima; whether both must be
  imposed was not considered.
- No case law was searched.
