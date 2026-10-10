# Radiation Protection Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
"incorporates all amendments up to and including 1 December 2021"; the latest
amending Act annotated in the body is 15/2019, and most annotations are 20/2014.

**Checks:** one case file, 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**8 of the 527 Singapore Acts** deposited here cite it. This row takes what a
business, clinic or laboratory meets: the licence requirements for radioactive
material and irradiating apparatus (ss 6, 7), the approvals for radioactive waste
(ss 12, 13, 15) and the s 13(3) presumption, records (s 16), confidentiality (s 18),
refusing entry (s 45(2)), appeals (s 46), officers' liability (s 50), the residual
penalty (s 52) and the composition cap (s 53). Administration, licence procedure,
the inspection and warrant machinery, the nuclear material offences of Part 8A and
the Second Schedule, arrest, search and forfeiture are not encoded.

## What the Act turns out to say

### 1. There is no appeal from a refusal to approve waste disposal

s 46(1) gives an appeal to the Minister, within 30 days, only from decisions "under
section 8, 14 or 15" — licences, the Director-General's own disposal of waste, and
waste transport. Decisions on disposing of radioactive waste (s 12), accumulating it
(s 13) and disposing of an irradiating apparatus (s 7(4)) are not listed. The
Minister's decision is final (s 46(4)). Reading "within 30 days" to include day 30
is an inference. Asserted.

### 2. Reasonable excuse saves disposal of waste, but not storing or moving it

s 12(2) makes unapproved disposal of radioactive waste an offence only "without
reasonable excuse". ss 13(4) (accumulation) and 15(2) (transport) carry no such
words. Asserted.

### 3. Waste stored for three months is presumed to be waste awaiting disposal

s 13(3): a substance arising from radioactive material produced, kept or used on
premises, accumulated in a part "appropriated for the purpose" and retained "for a
period of 3 or more months", is presumed, "unless the contrary is proved", to be
radioactive waste accumulated with a view to disposal — which needs approval under
s 13(1) unless a s 12 disposal approval already covers it (s 13(2)). Asserted.

### 4. A licence and an approval are different things, and the penalties halve

Possessing, using, importing, selling, manufacturing (apparatus) or transporting
(material) without a licence: up to $100,000 or 5 years (ss 6(2), 7(5)). Disposing of
an irradiating apparatus "whether in a working condition or otherwise" needs the
Director-General's prior written approval, not a licence (s 7(4)): $50,000 or 12
months (s 7(6)), the same as the waste offences. The encoding treats a licence as
not satisfying s 7(4). Note that s 7(1) does not list transport of irradiating
apparatus. Asserted.

### 5. Both seller and buyer of an irradiating apparatus must notify

s 7(2) and (3): the seller "must immediately give notice of the sale", and the buyer
"must immediately give notice of the purchase", each naming the other party.
$50,000 or 12 months. Asserted.

### 6. Without a warrant, an occupier may refuse entry

s 45(2): the obstruction offence does not apply to refusing consent to entry by an
inspector or officer "not acting pursuant to a warrant" under s 25, 26 or 41.
Asserted.

### 7. Composition is capped at the lower of half the fine and $15,000

s 53(1). For the $100,000 licence offences the cap is $15,000; for the $10,000
records offence it is $5,000; for the $6,000 confidentiality offence, $3,000. Which
offences are compoundable is left to regulations (s 53(3)), not retrieved. Asserted.

### 8. The licensee's safety duties have no penalty of their own

ss 10 and 11 (safe working environment, protection, training, monitoring, medical
examinations, protecting third parties) state no penalty. s 52 supplies one for
contraventions "for which no penalty is expressly provided": $50,000 or 12 months
where human life is endangered, otherwise $10,000 or 3 months. That s 52 reaches
ss 10 and 11 is an inference; ss 10 and 11 themselves are not encoded. The s 52
amounts are asserted.

## What would need doing before this is worth anything

- The Radiation Protection regulations — the "prescribed level" that makes an
  article radioactive material, the compoundable offences, exemptions under s 55 —
  were not retrieved; the definition of radioactive material turns on them.
- ss 8, 10, 11, 14, 17 and the whole of Parts 8 and 8A are unencoded.
- s 3(2) (the Government is not liable to prosecution) and s 50(2)–(6) are not
  modelled.
- No case law was searched.
