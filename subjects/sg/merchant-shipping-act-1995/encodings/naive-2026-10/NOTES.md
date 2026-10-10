# Merchant Shipping Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the other `naive-2026-10` rows (the `writing-l4-rules` skill was not loadable in
this session). No pipeline, no coverage table, no independent test pass, no human
gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 9
of 2026 (in force 1 May 2026) shown. Section numbers follow the body of the deposit;
the arrangement of sections at its top has its numbers shifted against the titles.

**Checks:** one case file, 97 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**17 of the 527 Singapore Acts** deposited here cite it. It is a large Act (eleven
Parts and two Conventions in Schedules). This row takes the parts with decision
content that an owner, master, insurer, claimant or member of the public meets:

- **Part 8**, limitation of liability: who may limit, which claims, the general
  limits by tonnage, the passenger limit, the overflow rule of Article 6(2), and the
  s 135 exclusion for fire and undeclared valuables.
- **Part 5**, four duties: which ships Part 5 covers (s 98), excess passengers
  (s 102), assistance after a collision (s 106), accident reports within 24 hours
  (s 107).
- **Part 9**, wreck: what a finder must do (s 153), immediate sale (s 157), and
  delivery to the owner or sale for the Consolidated Fund (ss 156, 159).

Registration, mortgages, manning, crew wages and discipline, surveys and load lines,
inquiries, delivery of goods, the limitation fund and its distribution, salvage
awards and the Salvage Convention are not encoded.

## What the Act turns out to say

### 1. A 299-ton ship and a 300-ton ship are worlds apart

Article 6(1)(a)(i) of the Convention sets the personal-injury limit at 3.02 million
Units of Account for a ship "not exceeding 2,000 tons". s 137(1)(b) replaces that
with **166,667** Units for a ship (other than a licensed harbour craft) "with a
tonnage less than 300 tons", and the property limit of 1.51 million with 83,333.
There is no taper: one ton of gross tonnage multiplies the personal-injury limit by
about eighteen. Asserted (299 and 300 tons, both limits).

### 2. Wreck-raising and cargo-removal claims cannot be limited in Singapore

Article 2(1)(d) and (e) list claims for raising or removing a sunk or wrecked ship
and for removing its cargo as subject to limitation. s 136(1) gives the Convention
the force of law "other than paragraph 1(d) and (e) of Article 2", so those claims
fall outside limitation. Salvage, general average, oil pollution (CLC) and nuclear
damage are excepted by Article 3 itself. Asserted.

### 3. Fire and undeclared jewels: not a limit but a complete exclusion

s 135(1) says the owner of a **Singapore** ship "is not liable" for property lost
by fire on board, or for "gold, silver, watches, jewels or precious stones" stolen
when their nature and value were not declared in writing at shipment. It reaches
charterers, managers and operators (s 135(4)) and the master and crew (s 135(2)),
and gives way only to intentional or reckless personal conduct (s 135(3), Art 4).
Ordinary goods stolen, or declared valuables stolen, are not excluded. Asserted.

### 4. Injured people get a second bite at the property fund

Article 6(2): if the personal-injury fund is not enough, the unpaid balance ranks
rateably with property claims against the 1(b) fund. On a 2,000-ton ship, $5.02m of
injury claims and $1.02m of property claims (in Units): injury claimants take
3.02m plus half of 1.51m (4.02m), property claimants 510,000. Asserted. The s 136(3)
priority for harbour-works damage within the 1(b) fund is not modelled.

### 5. The passenger limit turns on the certificate, not the head count

Article 7(1): 175,000 Units "multiplied by the number of passengers that the ship is
authorised to carry according to the ship's certificate"; s 138 makes that the
passenger ship's certificate. An overloaded ferry (500 aboard, 400 authorised) has
the same 70 million limit as one carrying 250. Carrying the excess is itself an
offence under s 102 (up to $10,000, 2 years, or both). Asserted.

### 6. A finder who keeps wreck pays double

s 153: a finder who owns the wreck must notify the receiver; anyone else must
deliver it "as soon as possible". A non-owner who fails without reasonable cause is
fined up to $2,000, forfeits any salvage claim, and must pay "double the value" to
the owner (or the person entitled). Unclaimed wreck is sold after one month and the
proceeds go to the Consolidated Fund (s 159). Asserted.

### 7. Smaller points

- s 106: each master in a collision must assist and stand by "if and so far as he or
  she can do so without danger" to his or her own ship. Asserted.
- s 107: accidents causing death or serious injury, damage affecting seaworthiness
  or safety equipment, great peril, stranding or wreck must be reported to the
  Director within 24 hours, unless reportable under the Wreck Removal Act 2017.
  Asserted.
- s 137(1)(a): for a licensed harbour craft, the (i) amounts are read as the
  third-party sum insured required by the Port Master. Asserted.

## Readings and assumptions (inference, not text)

- **s 98** ("applies to all Singapore ships wherever they may be and to all ships in
  Singapore except harbour craft"): encoded with the harbour-craft exception
  attaching only to non-Singapore ships in Singapore. It could also be read as
  excepting every harbour craft.
- **s 137(1)(a)**: only the (i) amounts are replaced by the sum insured; the
  per-ton additions above 2,000 tons are kept. The text does not say how the sum is
  split between personal and property claims, so only the aggregate is encoded.
- **ss 156, 159** "one month" is taken as 30 days. The Act does not define it here.
- Figures are in Units of Account (SDR, Art 8); no conversion to dollars (s 142).

## What would need doing before this is worth anything

- The limitation fund (Arts 11-13, ss 139, 140), harbour-works priority (s 136(3))
  and the crew-claims exception (Art 3(e)) are unencoded.
- The saving provision s 144 (occurrences before 29 December 2019 or 24 July 2021
  stay under the earlier text) is not modelled; the encoding uses the current limits
  for every occurrence.
- The Salvage Convention (Second Schedule) and salvage awards are untouched.
- No case law, MPA circulars or tonnage orders were read.
