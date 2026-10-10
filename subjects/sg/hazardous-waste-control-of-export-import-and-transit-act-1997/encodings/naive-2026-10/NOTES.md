# Hazardous Waste (Control of Export, Import and Transit) Act 1997 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 January 2025), as deposited at `../../registers/source-bundle/HWCEITA1997.txt`.
The revised edition incorporates amendments up to 1 December 2021; the latest
amendment annotated is S 871/2024 wef 01/01/2025, which amends the Basel Convention
annexes in the Schedule (Annex II now ends with Y49, electrical and electronic waste).

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**REQ-0082** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining Singapore
Acts, ordered by everyday-life relevance. The requirement asks what the Act decides
for a person or business it applies to; no scenario has asked a sharper question yet.

This row takes what a trader, carrier or company officer meets: what counts as
hazardous or other waste (ss 4, 5, 9, 10 and the Annex II headings), what a transit
proposal is (s 6), the military exemption (s 12), the bars on granting a permit
(ss 22, 23), the three prohibitions and their penalties (ss 25 to 27), the
enforcement offences and their penalties (ss 29, 30, 32 to 37), entry into a home
(s 31(2)), company officers (s 42) and the appeal against a refusal (s 45).

Not encoded: the regulation-making provisions (ss 17 to 20, 48, except the s 48(2)(e)
ceiling, which is noted), s 21 on corresponding requirements between sets of
Article 11 regulations, fees (s 24), the time limit for permit conditions (s 11),
injunctions (s 28), the content of the movement-control and search powers, the
evidentiary certificates (ss 39 to 41), service (s 46), Convention countries (s 47),
and the Basel Convention text itself. No regulations under the Act were retrieved,
so "prescribed" waste and all permit conditions are inputs, and which Annex category
a real substance falls in is an input too.

## What the Act turns out to say

### 1. The three prohibitions have three different escape routes

An import is lawful with an import permit, **or** if it is authorised by an order
under Part 3 regulations, **or** if it has been ordered under them (s 25(1)). An
export has only two: a permit, or an export that "has been ordered" (s 26(1)); an
export merely *authorised* by an order is still an offence. Bringing waste in on a
transit needs a transit permit and nothing else will do, not even an order (s 27(1)).
Asserted.

### 2. A company pays three times the fine but cannot be imprisoned; its officers can

The shipment offences carry up to $300,000 for a body corporate, against $100,000 or
2 years or both for an individual (ss 25(4), 26(3), 27(3)). Under s 42 a director,
manager, secretary or similar officer is also guilty unless he or she proves **both**
no knowledge, consent or connivance **and** all due diligence; s 42(2) lists what
diligence looks like (compliance assessments, an environmentally sound management
system, contingency procedures, trained staff). Asserted.

### 3. Whether something is "waste" can depend on the country it is going to

For an export or a transit only, a substance becomes hazardous or other waste if the
destination is a Basel party and the Secretariat's prescribed website says that
country classifies it so (s 5(2)), or if the Minister has gazetted a declaration
(s 5(3), (4)). The same substance coming *in* is not caught by s 5. Under an
Article 11 arrangement the arrangement can pull a substance in (s 9) or expressly
push it out (s 10), for imports as well. The Act does not rank these against s 4;
this row applies s 10 last, overriding everything, and that ranking is an
inference. Asserted.

### 4. Regulations alone cannot make a waste hazardous

Both limbs of s 4(a) need an Annex III hazardous characteristic: a waste "prescribed
by any regulations ... where the waste has any of the characteristics mentioned in
Annex III", or an Annex I waste unless it has none of them. Household waste and the
Annex II plastic and e-waste categories are "other waste" with no characteristic
needed. Ship-operations waste and radioactive waste are outside the Act. Asserted.

### 5. Self-incrimination is a named excuse during a search, but not for an information notice

s 32(4) says it is a reasonable excuse to refuse to answer or produce a document
during a search if it "might tend to incriminate the person"; s 30(7) excuses
disobeying a movement order that would endanger someone. s 29, the written
information notice, names no excuse at all, though it too is committed only
"without reasonable excuse". The row says only whether the Act *names* the excuse.
Asserted.

### 6. Officers may enter a home on 6 hours' notice, without consent or a warrant

s 31(2) bars entry to an occupied dwelling house "unless with the consent of the
occupier ... or with 6 hours' previous notice". That a court warrant under s 31(3)
also permits entry is an inference. Asserted.

### 7. Smaller points

Failing to produce a permit is only a $3,000 fine with no imprisonment (ss 33, 34);
the other enforcement offences are $10,000 or 12 months. A false document is excused
only if the giver both flags where it is false and supplies the correct information
(s 37). Only a refusal to grant a permit is appealable under s 45, within 30 days,
and the Minister's decision is final. The Director-General must not grant any permit
that could result in waste reaching Antarctica (s 23). Asserted.

## What would need doing before this is worth anything

- No regulations made under the Act were retrieved (the deposit names none). Under
  ss 17 to 20 and 48 they would hold the permit scheme, the prescribed wastes and any
  regulation offences.
- The Annexes were read only for their headings; no substance-level classification
  is encoded.
- The ranking of ss 4, 5, 9 and 10 is an inference and needs checking against the
  Basel Convention and practice.
- No case law or official guidance was searched.
