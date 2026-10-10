# Medicines Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 31
of 2022 (in force 1 November 2022) and S 759/2022 shown.

**Checks:** one case file, 75 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
trader, pharmacist, practitioner or advertiser meets: which licences a dealing needs
and the exemptions from licensing (ss 5 to 8), retail sale only by or under a
pharmacist (ss 24 to 27), prescription-only products (s 29), medical advertisements
(ss 49 to 51 and the First Schedule), the due-diligence and warranty defences
(ss 64, 65), and the maximum penalties and composition (ss 20, 35, 50, 51, 53, 66,
72). The meaning of "medicinal product" (s 3), licensing procedure (ss 10 to 19),
adulteration and purchaser protection (ss 31 to 33) beyond which defences apply,
labelling (ss 44 to 48), enforcement powers (ss 56 to 61) and s 77 are not encoded.
No order or regulation under the Act was read, so whether a product is on the
general sale list or is prescription-only is a fact the user supplies.

## What the Act turns out to say

### 1. Advertising any treatment service to the public is prohibited outright

s 51(1)(b) forbids publishing "any advertisement referring to any skill or service
relating to the treatment of any disease or condition affecting the human body". It
is not limited to the First Schedule conditions or to medicinal products. The only
carve-out in s 51(2) is for advertisements going only to practitioners, pharmacists,
nurses and midwives or their trainees; the Minister may exempt by order (s 51(4)(b)),
and no order was read. On the text, a television advertisement for a clinic's back
pain service contravenes it. Literal reading. Asserted.

### 2. The First Schedule list is narrower and odder than "serious disease"

A medical advertisement may not claim to prevent, alleviate or cure any of 19
conditions, including diabetes, hypertension, cancer, menstrual disorders, "sexual
function" and "conception and pregnancy". Heart disease, asthma and the common cold
are not on the list. Asserted.

### 3. The pharmacist's licensing exemption now reaches only hospitals

s 7(1) and (2), as amended by Act 4 of 2021, exempt from ss 5 and 6 only what is
done "in a hospital by or under the supervision of a pharmacist". On the text, a
community pharmacist who compounds a product is manufacturing without the s 7
exemption. "Hospital" includes institutions designated by the Minister (s 2), and no
designation was read. Literal reading. Asserted.

### 4. An import licence lets you import, but the text does not say it lets you sell

s 5(2) allows import under "a product licence or an import licence", and s 10(3)
grants an import licence "to import any medicinal product for sale or supply". But
s 5(1) and (3) still forbid a person who imported a product from selling it "except
in accordance with a licence granted for the purposes of this section (called in this
Act a product licence)". Whether an import licence counts is not stated. The encoding
reads it literally: a parallel importer holding only an import licence contravenes
s 5 by selling. Inference from the text; may well be wrong in practice. Asserted.

### 5. The two herbal exemptions use different tests

From licensing (s 8): either a remedy made on premises the business can close to the
public and supplied to a particular person in that person's presence, or a remedy
whose plants are only dried, crushed or comminuted and that is sold "without any
written recommendation" as to its use; the second has no premises condition. From the
pharmacist requirement (s 27(3)): sale at closable premises of a remedy processed by
drying, crushing or comminuting "with or without diluting with water". A label saying
what dried herbs are for loses the s 8(2) exemption. Asserted.

### 6. The defences cover different offences

The act-or-default-of-another provision and its due-diligence defence (s 64) apply to
ss 31 to 33, 44 to 47 and 50 to 52. The warranty defence (s 65) applies only to
s 31(b), ss 32, 33 and 44 to 47: not to adulterating a product (s 31(a)) and not to
advertising. Neither applies to selling without a pharmacist (s 24). The warranty
defence needs notice to the prosecution "not later than 7 clear days before the date
of the hearing" and to the warrantor; a name or description on an invoice is deemed a
written warranty. Asserted.

### 7. Smaller points

- Spoken words are not an "advertisement" unless recorded or broadcast (s 49(2)); a
  label and a product-specific leaflet are not either (s 49(3)). Spoken claims are
  reached instead by s 50(3) (false or misleading representations), which is not
  encoded. Asserted.
- Prescription-only products may not be administered by anyone but an appropriate
  practitioner or someone on that practitioner's directions, "otherwise than to
  himself or herself": self-administration is outside s 29(2)(b). Asserted.
- The ceiling for most offences is $5,000 or 2 years or both; failing to answer an
  information notice, breaching general sale list conditions and failing to furnish
  copies of advertisements are fine-only at $2,000. Any offence may be compounded for
  up to $2,000 (s 72). Asserted.

## What would need doing before this is worth anything

- The orders making the general sale list (s 23) and prescription-only list (s 29),
  any exemption orders under ss 9, 28, 29(3) and 51(4), and any s 77 orders moving
  products to the Health Products Act 2007 were not read. Which products the Act
  still covers depends on them.
- Findings 1, 3 and 4 are literal readings; regulator practice and case law were not
  searched.
- s 3 (what is a medicinal product) and s 21 (special defences for licence holders)
  are not encoded.
