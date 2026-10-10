# Parking Places (Surcharge) Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. The latest amendment annotated in the body is [24/2018] on s 8(1);
the Legislative History lists the Parking Places (Amendment) Act 2018 (Act 24 of 2018,
s 20), commenced 1 May 2018.

**Checks:** one case file, 47 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**, not by citation count. Anyone who owns or
runs a car park for five or more vehicles in a designated area may owe the surcharge,
and the cost of parking there may carry it. The Act is nine sections long, so it is
encoded whole except s 1 (short title), s 6 (payment into the Consolidated Fund) and
s 9 (rules). What the Act leaves out cannot be encoded from it: which areas are
designated, the rates, and when and how payment is made are all left to Ministerial
orders in the Gazette (ss 2, 3(1)-(3)). None was retrieved, and no s 7 exemption order
was retrieved either.

## What the Act turns out to say

### 1. The Act is a frame with no numbers in it

Every figure a payer would want is somewhere else. Designated areas are fixed by order
(s 2). Rates are fixed by order (s 3(1)), "on the basis of the number of parking lots
or otherwise" (s 3(2)). The time and manner of payment are fixed by order (s 3(3)). The
encoding can say whether a surcharge is levied but not how much it is. The per-lot
function takes the rate as an input and is only an illustration of the basis the Act
names. Asserted.

### 2. The surcharge is payable without demand, and refunds are barred by default

s 3(4): the surcharge is payable "without demand", so it falls due when the fixed time
comes whether or not anyone sends a bill. s 3(6): "despite the provisions of any other
written law" the Superintendent "must not refund any surcharge except in such special
circumstances as the Superintendent may approve". On the words, even an overpayment
cannot be refunded unless the Superintendent approves special circumstances. Asserted.

### 3. Failing to give information or to answer a question is not the s 4(3) offence

s 4(1) lets the Superintendent require "any form, return or information" and answers
to "any question". But s 4(3) punishes only failing "to submit any form or return" and
a statement false in a material particular in "any such form or return". The words do
not reach a failure to give information or to answer a question. The offence also has
no stated mental element: a material falsehood is enough on its face. That reading is
taken from the words alone; no case was searched. Asserted.

### 4. Five vehicles is the threshold, and it counts motor vehicles

s 2: a parking place is land "used for the parking of 5 or more motor vehicles",
whoever owns it, whether a person, a statutory board or an institution. A yard for
four cars is outside the Act; a yard for five is inside. That a bicycle rack does not
count is an inference from the definition of "motor vehicle". Asserted.

### 5. The private house exclusion needs all three limbs

s 8(1), as amended by Act 24 of 2018: the Act does not apply to "private parking places
used exclusively in connection with any private dwelling house" for vehicles "kept for
private use only". A house drive that also takes a business's vans is caught, and so
is a private-car park shared by a house and a shop. "Dwelling house" (s 8(2)) means
any building or part of one used or adapted for human habitation, which is not
limited to a detached house; whether a condominium car park qualifies is left to the
user as a fact. Asserted for the limbs; the condominium point is not asserted.

### 6. The penalty is a fine or prison, not both, and composition is capped at $500

s 4(3): a fine up to $5,000 "or" imprisonment up to 6 months. s 5: the Superintendent
may compound an offence for up to $500 from a person "reasonably suspected" of it.
Asserted.

## What would need doing before this is worth anything

- The orders under ss 2, 3 and 7 (designated areas, rates, payment, exemptions) and any
  rules under s 9 were not retrieved; without them the encoding cannot tell anyone
  what they owe.
- The text of s 8 before the 2018 amendment was not read, so what changed is unknown.
- The Parking Places Act 1974, under which the Superintendent is appointed, was not read.
- No case law was searched, including on whether s 4(3) needs a mental element.
