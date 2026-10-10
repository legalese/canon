# Shared Mobility Enterprises (Control and Licensing) Act 2020 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, "version in force from 4/5/2026", as deposited at
`../../registers/source-bundle/SMECLA2020.txt`. The latest amendment annotated is
Act 5 of 2026 with effect from 4 May 2026, which deleted a definition from s 2(1)
and inserted "mobility vehicle".

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for **everyday-life relevance**: it governs the bike-share and scooter-share
services people hire from the kerb, and it lets operators and the LTA stop renting
to riders who park badly. An automated count found 2 of the 527 deposited Singapore
Acts citing it by its slug title. That count undercounts, so it is not a measure of
importance.

This row takes what a rider meets: what counts as a vehicle (s 2(1)), undocked and
docked (s 3(2), (3)), improper parking (s 2(2)), refusal of hire (ss 23(4) to (6),
25(3)), questioning riders (s 34(3)) and non-compliance with officers (s 36). It
adds the headline operator numbers: the unauthorised-service offence (s 8), the
financial-penalty cap (s 29(6)), composition (s 37) and appeal deadlines (ss 38, 39).
Not encoded: licence applications and grant criteria, licence conditions, class
licences, accounts and records, standards of performance, safety directives, the
grounds and procedure for regulatory action, entry powers, officers' liability,
service of documents and the transitional Schedule. The vehicle types that make a
service a "shared mobility service", the "prescribed period" of refusal, and the
compoundable offences are all left to Regulations, which were not retrieved.

## What the Act turns out to say

### 1. Three bad parkings in a year can cut a rider off from every operator

s 23(1) to (3) let licensees share information about hirers' improper parking.
Under s 23(5) a licensee may treat a rider as one who "persistently improperly
parks" if, through such an arrangement, it reasonably believes the rider improperly
parked "on at least 3 earlier occasions within the year", counting vehicles of the
same type or prescribed class, with any operator. Earlier years are disregarded.
Once a refusal is made, "all occasions which counted towards that refusal must be
disregarded" by any licensee afterwards (s 23(6)), so the count restarts.
Regulations may change the 3 (s 23(7)). Asserted.

### 2. The refusal power reaches undocked vehicles only

Both the licensee's entitlement to refuse and its duty to refuse on an LTA direction
(s 23(4)(a), (b)) are framed around "any undocked vehicle". Under s 3(2) a vehicle
counts as undocked unless it is indoors or in an enclosed shelter, or in a dock that
is both "attached permanently to the ground" and for the exclusive use of the
provider's customers. A permanent public rack open to anyone still leaves the bike
undocked. Asserted.

### 3. The rider has no appeal against an LTA-ordered refusal

s 38 makes a s 25 direction appealable "except a direction described in section
25(3)", which is the direction to refuse hire to a particular hirer. The defined
"appellant" is in any case only an applicant, licensee or class licensee (or a
former one), never a hirer. The LTA's power is fenced instead: it may only direct a
refusal against someone convicted of, or who accepted composition for, an offence
under s 21 or 22 of the Active Mobility Act 2017, s 5A of the Road Traffic Act 1961,
or the Parking Places Act 1974 "involving improper parking of vehicles hired from
any licensee or class licensee", committed on or after 22 July 2020. The direction
cannot outlast the prescribed period (s 25(3)(a)). Asserted.

### 4. "Improper parking" is a narrow, two-part test

s 2(2) makes parking improper only when the vehicle is left undocked outside an
area that is both demarcated for that type of vehicle and provided by a licensee,
class licensee, the Government or a public authority. A marked box provided by
anyone else does not count as a proper area. The example of a box painted by a
private condominium is an inference from that list, not a case the text names.
Asserted.

### 5. Operator penalties are large; the composition cap is small

Providing a service without a licence or class licence, or while suspended, is a
strict-liability offence, with a fine of up to $10,000 or 6 months, plus $500 "for
every day or part of a day" it continues after conviction (s 8). The LTA's financial
penalty is capped at the higher of $100,000 per instance and 10% of annual
shared-mobility turnover (s 29(6); the same in s 30(4) for former licensees).
Composition, by contrast, is capped at the lower of half the maximum fine and $5,000
(s 37). Asserted.

### 6. Protections for the person on the scooter

An authorised officer may question the rider of a shared vehicle, but "must not"
use that power on an under-aged rider. An escorting appropriate supervisor may be
questioned instead (s 34(3)). Refusing to answer is a reasonable excuse if the
answer "might tend to incriminate that person" (s 36(4)). There is also a defence
for someone who shows they do not have the document and took all reasonable steps
to get it (s 36(3)). Asserted.

### 7. Drafting loose ends in the deposit

The arrangement of sections at the top is column-shifted in places: in Part 1 the
number 1 sits beside the heading of s 3, and Divisions with three short headings
show the same shift. The encoding follows the body's numbering. The Schedule is headed
"Section 53", yet the saving provision that cites it is s 50. Paragraphs 3 and 4 of
the Schedule refer to "section 51(5)", which does not appear in this edition. The
Act 5 of 2026 annotation reads "wef 04/052026". Not asserted.

## What would need doing before this is worth anything

- The Shared Mobility Enterprises Regulations (the prescribed vehicle types,
  refusal period and compoundable offences) were not retrieved, so the encoding
  cannot say which services the Act actually covers.
- Active Mobility Act 2017 definitions (bicycle, personal mobility device, mobility
  vehicle, under-aged rider) were not read. The vehicle list is taken from s 2(1)
  alone.
- The definition deleted by Act 5 of 2026 is not identified in the deposit, and the
  amending Act was not read.
- No LTA directions, decisions or case law were searched.
