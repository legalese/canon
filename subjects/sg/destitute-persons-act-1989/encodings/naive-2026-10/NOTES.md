# Destitute Persons Act 1989 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments to 1 December 2021),
informal consolidation marked "version in force from 1/7/2026", with amendments by
Act 5 of 2025 (wef 9 March 2025) and Act 14 of 2025 (wef 1 July 2026) annotated.
Deposit: `../../registers/source-bundle/DPA1989.txt`.

**Checks:** one module, one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its everyday-life relevance. The Act decides what happens to a person
found begging or idle and without means in a public place, and to the relative or
friend who takes that person home from a welfare home. It is short, so nearly all
of its operative sections are encoded: ss 2, 3, 4, 6, 7(2), 10, 11, 12, 13(2), 14
and 16 to 20. Not encoded: establishing homes and making rules (ss 7(1), 9), how the
Review Committee is appointed and gazetted (s 10(1A), (2)), transfers (s 15), the
work requirement in s 13(1), and everything delegated to the Social Residential
Homes Act 2025.

## What the Act turns out to say

### 1. A voluntary resident who walks out commits an offence carrying prison only

s 16(b) covers leaving without permission a home "to which the person has been
admitted on the person's own application under section 5", as well as a home where
the person is required to reside under s 3. The only penalty is "imprisonment for a
term not exceeding 6 months": there is no fine. On release, s 19 says the person
"must be returned to a welfare home". Asserted.

### 2. No time limit on a residence warrant

s 3(3) caps the inquiry at 30 days from admission, extendable by the Minister by
"not exceeding 30 days", so at most 60. But the s 3(4) warrant requiring residence
carries no maximum period. Release depends on s 11 (discharge on the Review
Committee's advice), s 12 (discharge to a carer) or s 20 (the Minister). The
12-month review duty in s 10(1) attaches only once the Minister "may appoint" a
Committee. Asserted (deadline arithmetic, review interval).

### 3. Who is "destitute" turns on a reading the text does not settle

s 2(1)(b) covers an idle person in a public place "who has no visible means of
subsistence or place of residence or is unable to give a satisfactory account". This
row reads "no means ... or place of residence" as lacking both, so an idle rough
sleeper with visible income is not destitute under (b). The other reading would
catch anyone idle in public who lacks either. Limb (a), nuisance begging, applies
even to a person with a home and income. Begging includes busking or selling where
the conduct is "calculated to induce the giving of alms" (s 2(2)). Asserted, on the
chosen reading.

### 4. Temporary admission uses a narrower test than the definition

s 3(2) lets the Director-General temporarily admit a delivered person only on
"reasonable cause to believe" the person "has no visible means of subsistence". A
nuisance beggar with visible means is destitute under s 2(1)(a) but cannot be
temporarily admitted on that ground. Since 1 July 2026, s 7(2) also bars any
admission or warrant unless the home is licensed under the Social Residential Homes
Act 2025. Whether a person temporarily admitted pending inquiry is "required to
reside in accordance with section 3" for s 16(b) is unclear; this row says no
(an inference), though s 16(c), failing to return after permitted leave, still
applies. Asserted.

### 5. The carer has 24 hours and no stated excuse

A relative or friend whom the Director-General thinks willing and able, who applies
and gives satisfactory security, must be given the discharge (s 12(1): "must ...
order"). If the care "for any reason" ceases, the carer must tell the
Director-General in writing within 24 hours (s 12(2)), on pain of a $500 fine or 2
months (s 12(3)). No reasonable-excuse defence is written in. Asserted.

### 6. Begging is an offence only on the third time

s 4 punishes only a "habitual beggar": someone found nuisance-begging on at least 2
previous occasions who "consequently, was required on those 2 occasions to reside in
a welfare home". Voluntary admissions do not count (an inference from the contrast
with s 5). Maximum $3,000 or 2 years. Asserted.

### 7. Fingerprint records: returned on request, otherwise destroyed, but photos kept

After 2 years from discharge the person may apply for the fingerprint sheet and
photographs; if no application arrives before 3 years, they "must be destroyed"
(s 6(2)). But s 6(3) lets the Director-General keep 3 copies of the photographs for
a register regardless. An application before the 2 years end is not provided for.
Asserted.

### 8. A deleted-definition annotation sits awkwardly in the deposit

In s 2(1) the line "[Deleted by Act 14 of 2025 wef 01/07/2026]" follows the
"public place" definition. It most likely marks a different definition removed at
that point (an inference), so "public place" is treated as still in force. Not
asserted.

## What would need doing before this is worth anything

- The Destitute Persons rules made under s 9, and the Social Residential Homes Act
  2025, were not read; conditions of admission, work, leave and discharge live
  there.
- The two interpretive choices (s 2(1)(b) "neither", s 16(b) and temporary
  admission) need checking against case law or the earlier text.
- The "public place" annotation (finding 8) should be checked against the SSO
  version history.
- No case law was searched.
