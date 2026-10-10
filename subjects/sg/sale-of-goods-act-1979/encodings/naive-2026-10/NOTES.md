# Sale of Goods Act 1979 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SGA1979.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31
December 2021; the page furniture reads "Informal Consolidation – version in force
from 1/4/2022". The latest amendment annotated is Act 25 of 2021, wef 1 April 2022
(ss 52 and 61, "claimant").

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: every purchase of goods in Singapore is a
contract of sale under it, and it is where a buyer's right to goods of satisfactory
quality comes from. (An automated count found 4 of the 527 deposited Singapore Acts
citing it by its slug title; that undercounts Acts cited by short or older titles and
is not a measure of importance.)

This row takes what an individual buyer most often meets: perished goods (s 6),
satisfactory quality and fitness for purpose (s 14) and the slight-breach rule
(s 15A), losing the right to reject on acceptance (ss 11(3), 35), wrong quantities
(s 30), title from a non-owner (ss 21, 23), goods on approval and risk (ss 18 Rule 4,
20), damages (ss 50, 51, 53) and auctions (s 57). Not encoded: formation and price,
sale by description and sample (ss 13, 15) on their own, bulk and unascertained goods,
sellers and buyers in possession (ss 24–26), delivery rules, partial rejection
(s 35A), the unpaid seller's rights (Part 5), specific performance (s 52), exclusion of
implied terms (s 55), and the Schedule's modifications for older contracts.

## What the Act turns out to say

### 1. Only a business seller owes satisfactory quality — but a consignment shop can make a private sale a business one

s 14(1): apart from s 14 and s 15 "there is no implied condition or warranty about the
quality or fitness" of goods. The quality and fitness conditions in s 14(2) and (3)
arise only "where the seller sells goods in the course of a business". A purely
private sale carries neither. But s 14(5) applies them to a business agent selling for
a private owner, unless the buyer knows the owner is private or reasonable steps are
taken to tell them. Asserted.

### 2. A consumer may reject for even a slight defect; a business buyer may not

s 15A(1): where a breach of the implied terms in ss 13–15 "is so slight that it would
be unreasonable for the buyer to reject", a buyer who "does not deal as consumer" may
treat it only as a breach of warranty (damages, not rejection). The seller must prove
both the slightness (s 15A(3)) and that the buyer is not a consumer (s 61(4B)). The
same rule governs short and excess deliveries (s 30(2A), (2B); s 30(2A) is annotated
"[4/2014]"). Asserted.

### 3. Pointing out a defect, or an inspection that should have found it, removes the quality condition for that defect

s 14(2C): the condition "does not extend to any matter" specifically drawn to the
buyer's attention before the contract, or, where the buyer examines the goods first,
which "that examination ought to reveal". A buyer who inspects and misses a hidden
defect keeps the condition. Asserted.

### 4. Acceptance ends rejection, not damages — and asking for a repair is not acceptance

Once the buyer has accepted the goods, s 11(3) lets a breach of condition be treated
"only as a breach of warranty", and s 53 still gives damages or a price reduction.
Under s 35 a buyer is deemed to accept by intimating acceptance or acting inconsistently
with the seller's ownership only after a reasonable opportunity to examine (s 35(2)), or
by keeping the goods beyond a reasonable time without rejecting (s 35(4)). s 35(6)(a): a
buyer does not accept "merely because" he asks for or agrees to a repair. Asserted.

### 5. An honest buyer from a thief gets nothing; an honest buyer from a fraudster may

s 21(1): a buyer from a non-owner without authority acquires "no better title ... than
the seller had", unless the owner's conduct precludes denial. s 23: where the seller's
title is voidable and not yet avoided, a buyer in good faith without notice gets good
title. Good faith means "in fact done honestly, whether it is done negligently or not"
(s 61(2)). Asserted. (Whether a given seller's title is void or voidable is general law
the Act does not decide.)

### 6. Keeping goods on approval past the return time buys them

s 18 Rule 4: property in goods "on approval or on sale or return" passes when the buyer
signifies approval, or keeps the goods without notice of rejection beyond the fixed
time or, if none, a reasonable time. Risk follows property (s 20(1)), except that a
party whose fault delays delivery bears the loss that delay causes (s 20(2)). Asserted.

### 7. An auction bid can be withdrawn until the hammer falls; an undisclosed seller's bid lets the buyer treat the sale as fraudulent

s 57(2), (4), (5). Asserted.

### 8. The market measures of damages do not say which way round

ss 50(3) and 51(3) give "the difference between the contract price and the market or
current price". The direction and the floor at zero in the encoding are inferences from
"the estimated loss directly and naturally resulting" (ss 50(2), 51(2)), and are
labelled as such in the source. s 53(3) is explicit: value as warranted less value on
delivery. Asserted (with the inference).

## What would need doing before this is worth anything

- "Deals as consumer" is defined by Part 1 of the Unfair Contract Terms Act 1977
  (s 61(4A)), and exclusions are subject to it (s 55); neither was read.
- Other consumer legislation that may give a buyer remedies alongside this Act (for
  example the Consumer Protection (Fair Trading) Act) was not read or considered.
- s 35A (partial rejection), severable contracts under s 11(3), the s 35(3) bar on a
  consumer waiving the examination right, and agreement otherwise under s 20 are not
  modelled.
- No case law was searched; "reasonable time", "satisfactory quality" and "slight" are
  left as facts supplied by the user.
