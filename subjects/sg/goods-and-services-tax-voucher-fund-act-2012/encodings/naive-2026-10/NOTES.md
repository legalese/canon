# Goods and Services Tax Voucher Fund Act 2012 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
9/3/2025), as deposited at `../../registers/source-bundle/GSTVFA2012.txt`. The revised
edition incorporates amendments to 1 December 2021; the one later amendment annotated is
Act 5 of 2025 wef 09/03/2025 (s 8(2), (2A)).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0076**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet.

The Act is short (19 sections) and mostly about a government fund's housekeeping. This
row takes the parts a recipient or applicant meets: ss 3(4), 4(1)(a), 6, 8A, 9 to 12,
16 to 18 and 19(2)(c). Not encoded: moneys paid in (s 3(2)), expenses (s 5),
dissolution (s 7), the Minister's appointments (s 8, including the Gazette requirement
of s 8(2A)), and accounts, audit and Parliament (ss 13 to 15).

## What the Act turns out to say

### 1. The Act does not say who gets a GST Voucher, or how much

s 4(1)(a) lets the Fund pay assistance "under a public scheme to such natural persons as
may be prescribed", to mitigate the impact of GST on their living expenses. Eligibility
and amounts are left to regulations (s 19(2)(a)) and to the scheme, neither of which is
in the deposit. So the encoding can say only that the recipient must be a natural person
of a prescribed class: a company or other business cannot receive this assistance (it
may be paid only as an appointed disburser's expenses, s 5(b)). Asserted.

### 2. Being eligible gives no absolute right

s 8A (inserted by Act 19 of 2020): "No person has an absolute right to any financial
assistance" from the Fund. The encoding returns FALSE whether or not the person is
eligible under the scheme. What remedy, if any, an eligible person who is refused has is
not in the Act. Asserted.

### 3. A careless statement is an offence; a careless document is not

s 16 catches anyone who, in or for an application (their own or someone else's),
"knowingly or recklessly" makes a false statement, but a document only if the person
"knows" it to be false "in a material particular". Recklessness is enough for words, not
for papers; a known falsity in a trivial detail of a document is not caught. An honest
mistake is neither. Maximum $5,000 or 12 months or both. Asserted.

### 4. Every overpayment comes back as a debt

s 11(a): money paid to someone not eligible, or eligible for less, is recoverable "as a
debt due to the Government": the whole sum, or the excess. No fault or fraud is
required and no time limit is stated in the Act. Asserted.

### 5. Your data can be shared without your consent, but not onward

s 9 lets the Minister certify that an appointed body needs another authority's
confidential information to pay assistance; the responsible Minister may then direct
disclosure, and the authority must comply despite any duty of secrecy, with immunity
from liability. Income-tax information under s 6 of the Income Tax Act 1947 is carved
out (s 9(3)). Once received, the information may not be passed on except with the
person's written consent or to administer or enforce the Act (s 10); breach is an
offence with the same $5,000 / 12-month maximum. Asserted.

### 6. Composition is capped at $1,000

s 18 allows a prescribed offence to be compounded for no more than the lower of half the
maximum fine and $1,000. For the Act's own offences ($5,000 maximum) the cap is $1,000.
Which offences are compoundable is for regulations; none were retrieved. Asserted.

### 7. Smaller points

Officers and partners share liability on consent, connivance or neglect (s 17). A
payment out of the Fund needs the Minister's approval or that of a person authorised in
writing (s 6(2)). The Fund's year runs 1 April to 31 March (s 12). Asserted.

## What would need doing before this is worth anything

- The regulations made under s 19 and the GST Voucher scheme itself (eligibility,
  amounts, compoundable offences) were not retrieved; without them the row cannot answer
  "do I get a voucher, and how much".
- No case law or administrative guidance was searched.
- The modelling of an ineligible person as eligible for 0 under s 11(a) is the
  encoder's, not the text's.
