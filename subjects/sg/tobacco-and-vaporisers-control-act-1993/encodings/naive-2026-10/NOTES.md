# Tobacco and Vaporisers Control Act 1993 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 9
of 2026 (in force 1 May 2026) shown. Act 9 of 2026 annotations run through the
definitions, Part 3 and all of Parts 3A and 3B.

**Checks:** one case file, 121 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**11 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
smoker, a vaper, a retailer, a parent or a venue operator meets: who is under-aged
(s 2), online sales (s 2(2)), free samples (s 9(2)), supply to and use by under-aged
persons (ss 10, 11), minimum pack size (s 12), the outright bans on chewing tobacco,
vaporisers and imitation tobacco products (ss 15, 16, 16A), products containing a
specified psychoactive substance (ss 19B-19E, 19G), and the duties of responsible
persons of specified premises (s 19W). Advertising (Part 2), loyalty programmes,
the display ban, warning notices, licences, the evidential presumptions, drug
testing, rehabilitation and enforcement are not encoded.

## What the Act turns out to say

### 1. Importing a vape now carries mandatory imprisonment, and transit is no excuse

s 16(4): a person who imports a vaporiser or any component "shall on conviction be
punished with imprisonment for a term not exceeding 9 years" and is in addition
liable to a fine of up to $300,000; selling carries mandatory imprisonment of up to
6 years (s 16(5)). Chewing tobacco is treated the same way (s 15(6), (7)), but
s 15(4) exempts import solely for taking the thing out of Singapore. **s 16 has no
such exemption**, and nor does s 16A. A vaporiser need not contain nicotine at all
(s 16(7)). Asserted.

### 2. Etomidate vapes carry minimum prison terms and the cane

Part 3A (inserted by Act 9 of 2026) reaches any tobacco product, imitation tobacco
product or vaporiser that "contains a specified psychoactive substance" (the
Schedule lists etomidate, metomidate and four related compounds). Import: 3 to 20
years and 5 to 15 strokes (s 19B). Sale: 2 to 10 years and 2 to 5 strokes (s 19C).
Possession or purchase: $20,000 or 10 years (s 19D). Consumption is an offence even
without a vaporiser (s 19E(3)), and a citizen or PR who consumes abroad and is
caught by a s 19J urine test may be dealt with as if in Singapore (s 19F). Asserted.

### 3. Leaving an etomidate vape where a child can reach it is a prison-only offence

s 19G(1): an adult who "knowingly or recklessly" leaves the product exposed or in an
unlocked container, knowing a child "has, or is likely to have, access", commits an
offence punishable only by imprisonment, up to 10 years, with a 2-year minimum on a
second conviction. "Child" here means below 16; the s 19G(2) offence of letting a
"young person" (below 21) use it was not encoded beyond the definitions. Asserted.

### 4. The smoking age is a 19-20-21 staircase from an unstated date

"Under-aged person" means below 19 for 12 months "after the date prescribed", below
20 for the next 12 months, and below 21 after that. The date itself is not in the
Act. The encoding counts months from that date and assumes it has passed
(inference). Asserted.

### 5. Under-aged possession is an offence only in public or on a road; buying always is

s 11(1) catches an under-aged person who uses or possesses a tobacco product "in a
public place or on a road", or who buys one — capped at $300. Possession elsewhere is
not within it. A seller has a defence only if he proves reasonable belief and inquiries,
or reasonable acceptance of evidence of age (s 10(2)); fines run from $500 (giving)
to $10,000 (repeat selling). Asserted.

### 6. Venues must eject vapers but need not search or refund

s 19W puts the responsible person of a specified premises under a duty to tell a
person with a vape to dispose of it and, failing that, ask them to leave; staff
knowledge is presumed to be the responsible person's "until the contrary is proved".
Fine $1,000, $2,000 on repeat. The responsible person need not refund admission or
fares (s 19W(9)) and need not search anyone (s 19W(10)). Which premises are
"specified" is left to regulations. Asserted.

## What would need doing before this is worth anything

- The "date prescribed" for the under-aged phase-in, the prescribed minimum pack
  size if gazetted, the prescribed tobacco products under s 15(1)(a)(ii)-(iv) and the
  specified premises under Part 3B were not retrieved.
- Ordinary cigarettes are modelled only as "not banned outright"; the s 18 licence
  regime and s 14 prescribed-substance products were not read.
- The evidential presumptions (ss 16B, 16C, 19M-19P) change who must prove what in
  every prohibited-product case and are not encoded.
- s 19G(2), s 19H (procuring a young or vulnerable person) and s 19I (gatherings)
  were read but not encoded.
- No case law or Health Sciences Authority guidance was searched.
