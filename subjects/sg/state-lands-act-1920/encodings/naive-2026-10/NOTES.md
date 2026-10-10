# State Lands Act 1920 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating amendments up
to and including 1 December 2021 (the latest amending Act annotated in the body is
11/2015).

**Checks:** one case file, 81 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. This row takes what runs with
a State title and binds whoever holds it: how deep the land goes (s 9), the
conditions implied by date of issue (s 11(2) to (5)), the grantee's covenants and
re-entry (ss 13, 14(1)(e), 14(2)), the State's royalty and right to take materials
(s 14(1)(a), (b)), successors bound without notice (s 15), the cap on rent revision
(s 16(2), (3)), forfeiture of religious or charitable land (s 17(1)) and the
boundary duty (s 29). Not encoded: the Chief Valuer and Commissioner of Lands,
rule-making, modes of alienation (s 8), the subjacent-support easement (s 10), the
deceased grantee (s 12), Collector's Certificates, surrender and regrant, the HDB and
road-reserve grants, treaty vesting (s 17(2)) and fees (s 28).

Dates are encoded as YYYYMMDD numbers.

## What the Act turns out to say

### 1. Ignore a boundary notice and you pay twice the cost

s 29(1): every owner or occupier of land abutting State land must define and keep
defined the boundary by a wall, bank, drain, fence, road, path or other sufficient
means. If, after written notice, the work is not commenced within 30 days and
diligently proceeded with, the Collector may do it and "recover twice the amount of
the cost necessarily incurred", as if it were an arrear of rent. The encoding reads
the trigger as either not begun by day 30 or begun but not diligently pursued; that
reading is an inference. Asserted.

### 2. Not all breaches lead to forfeiture, and rent arrears are not one that does

s 14(1)(e) lets the Collector re-enter "on any portion of the land in the name of the
whole" and forfeit the land for breach of the s 13 covenants **other than** rent and
maintenance of landmarks. So burying a body without the Minister's written permission,
or dealing with part of the land (other than a lease of 7 years or less, s 13(1)(d)),
forfeits the whole; non-payment of rent does not, under this section. Digging for
minerals without the President's consent carries the same forfeiture, but only for
grants and leases issued after 1 January 1936 (s 14(2)), and not for road materials
used on the land. Asserted.

### 3. Land goes down 30 metres below the Datum, unless the title says otherwise

s 9(1): land includes only the subterranean space "specified in the State title", or,
if none is specified, "to -30.000 metres from the Singapore Height Datum". s 9(3)
reads the same default into every other written law. Whether a stratum exactly at
the limit is included is an inference from "to". Asserted.

### 4. A successor is bound whether or not they knew

s 15: an assignee or proprietor is bound by the exceptions, reservations and
covenants in the State grant or lease "irrespective of whether the assignee or
proprietor has notice (actual or constructive)", for grants issued before, on or after
15 January 1981. Asserted.

### 5. The implied conditions depend on the date of issue

A mineral-oil reservation is implied in grants and leases made after 3 May 1907
(s 11(2)); a right-of-way condition for adjacent landholders after 1 December 1915
(s 11(4)); a grant issued before 1 March 1961 is deemed an estate in perpetuity
(s 11(5)). The first two yield to an express contrary provision. Sending in a claim
after the Collector's written offer of compensation is treated as a submission to
arbitration (s 11(3)). Asserted.

### 6. Rent revisions are capped at 50%, and improvements do not count

s 16(2): at each 30-year revision the new rent may not exceed the previous term's by
more than 50%; s 16(3): the landholder's improvements "must not be taken into
account". Asserted.

### 7. Religious land forfeits on change of use, whenever granted

s 17(1): land granted free or at nominal rent for religious or charitable purposes is
forfeited if applied to other purposes without the President's written consent;
s 17(3) applies it to grants "whenever made". Asserted.

### 8. The State takes materials free, except near a house

s 14(1)(a): a 10% royalty on the gross produce of all mines and minerals except
laterite. s 14(1)(b): the State may take earth, clay, gravel, sand and stone for
public purposes without compensation, except for actual damage to growing crops,
roads, paths, fruit trees or buildings, and never from a dwelling house's site,
adjoining buildings, curtilage, garden, orchard or pleasure grounds. Asserted.

## What would need doing before this is worth anything

- The rules under ss 7, 16(5) and 27 (forms, fees, rent, applications) were not
  retrieved.
- Whether s 14(1)(e)'s exclusion of rent breaches is filled by another remedy
  elsewhere (for example under the rules or the Land Revenue Collection Act 1940) was
  not checked.
- The s 29(3) trigger reading and the s 9 boundary case are inferences.
- No case law was searched.
