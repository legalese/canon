# Control of Plants Act 1993 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/CPA1993.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021"; the latest amendment annotated in the
body is Act 25 of 2021 (s 8(5), wef 1 April 2022).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
produce importer, a commercial grower, a pesticide operator or a landowner meets: the
import and transhipment licence and per-consignment permit (ss 2, 7, 8), the
cultivation licence and pesticide rules (ss 9-11, 13), protection of innovative
pesticide data (ss 15, 16), the prohibited-plant presumption (s 18), pest and
clearance notices and compensation (ss 21, 25, 26), the appeal (s 33), the penalties,
protection from liability (s 45) and composition (s 47). Administration, quarantine,
export prohibitions, investigation powers, sampling, forfeiture, service, exemptions
and the rules are not encoded. No subsidiary legislation was read, so prescribed
residue levels, fees and the list of compoundable offences are unknown here.

## What the Act turns out to say

### 1. The pesticide rules bind only commercial growers

s 9 disapplies the whole of Part 3 to cultivation "for domestic and home gardening
purposes" and to cultivation "which is not for sale". Part 3 holds not only the
cultivation licence (s 10) but also the pesticide rules (s 11): registered pesticide,
certified or supervised operator, storage, disposal, residues. So a home gardener using
an unregistered pesticide breaches nothing in s 11. Asserted.

### 2. Ignoring a clearance notice is not qualified by "wilfully", and costs five times as much per day

s 21(7) punishes an owner or occupier who "wilfully fails" to comply with a pest
notice, with a continuing fine of up to $100 a day after conviction. s 25(3), for a
notice to fell and burn diseased cultivation (which needs the Minister's approval),
punishes one who simply "fails to comply", at up to $500 a day. Asserted
(30 continuing days: $13,000 against $25,000).

### 3. Every consignment needs its own permit, and the whole consignment must pass

s 8(1): a licensed importer also needs a permit "in respect of each consignment", and
"the whole consignment" must match the permit, be free of prohibited pesticide residue
and within prescribed levels, meet sanitary standards, be evidenced to the
Director-General, and have containers bearing "the producer's name and address".
Failing any one is the offence. The due-diligence defence in s 8(4) needs both a cause
outside the licensee's control and all reasonable precautions; blaming another person
requires written notice to the prosecutor 7 clear days before the hearing, unless the
court permits (s 8(5), added by Act 25 of 2021). Asserted.

### 4. A landowner is deemed to have permitted a prohibited plant

s 18: if a prohibited plant is found growing in breach of a s 17 order, owner and
occupier are "deemed to have permitted the plant to grow" unless they prove both that it
was planted without their knowledge and consent and that they "forthwith effectually
eradicated and destroyed it" on finding out. Asserted.

### 5. No compensation for diseased plants

s 26: compensation for cultivation destroyed under a s 25 notice is at the Minister's
discretion, valued at market value, and "no compensation is to be paid for any diseased
plant". It can be withheld or reduced for non-compliance or neglect. The encoding gives
only the ceiling (market value or nil). Asserted.

### 6. Uniform penalties, one exception

Every offence encoded carries a fine of up to $10,000; imprisonment is up to 3 years
for each except s 37(9) (false statements, destroyed documents, failing a lawful demand),
which is 12 months. Composition is capped at $1,000 and only for offences prescribed as
compoundable (s 47). Asserted.

### 7. Smaller points

- An appeal against refusal, suspension or revocation goes to the Minister in writing
  within 7 days of receipt of the notice, and the Minister's decision is final; the
  suspension or revocation bites meanwhile unless the Minister orders otherwise (s 33).
  Treating day 7 as in time is an inference. Asserted.
- Entry to look for pests needs written notice at least 6 hours ahead (s 21(2)). Asserted.
- Innovative pesticide data is protected for 5 years from receipt, subject to consent and
  public health or safety (ss 15, 16). Only the consent and health exceptions of s 16(1)(a)
  are encoded; disclosure to agencies and international bodies is not. Asserted.

## What would need doing before this is worth anything

- The two inferences in s 7 (produce for own consumption is outside s 7; produce that
  never leaves its conveyance is neither imported nor transhipped) need checking against
  the rules made under s 49(2)(k), which were not read.
- The subsidiary legislation (residue levels, sanitary standards, fees, compoundable
  offences, s 17 and s 28 orders) was not retrieved.
- The body-corporate and employer liability provisions (ss 35, 36) are not encoded.
- No case law was searched.
