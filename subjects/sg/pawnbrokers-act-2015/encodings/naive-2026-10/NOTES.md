# Pawnbrokers Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, deposited at `../../registers/source-bundle/PA2015.txt`, with
later amendments annotated to Act 32 of 2024 (wef 25 November 2024). S 986/2022 (wef
1 January 2023) is annotated in the Second Schedule.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. This row takes what happens
across the counter: the licensing offence (s 6), deemed pawning by sale and
repurchase (First Schedule), valuation and pawn ticket (ss 48, 49), the profit cap and
fees (s 50, Second Schedule), extensions (s 51), redemption (ss 54, 56, 57), lost or
damaged pledges (s 60), forfeiture (ss 61, 63), realisation other than by forfeiture
(s 65), the rightful owner's notice (s 67), offences by pawnbrokers (s 72), cash
transaction reports (s 74A, Third Schedule) and the general penalty (s 79). Licence
grant and renewal, shareholder and director approvals, licence conditions,
investigative and regulatory powers, waivers and most of the anti-money-laundering
measures are not encoded.

## What the Act turns out to say

### 1. Forfeiture is the pawnbroker's only remedy, and a wrong sale costs it the loan

s 64: a pawnbroker "cannot sue, in debt or otherwise" for the loan or profit and
cannot realise its security other than by forfeiture. If it does (s 65), it owes the
person entitled to redeem any surplus of the pledge's value over loan and profit, and
if the value is equal or less, "the loan and profit are extinguished". Value is the
valuation it gave at the start (s 65(2)). Asserted (s 65; s 64 is stated, not asserted).

### 2. A sale-and-buy-back is a pawn

First Schedule para 1: where X sells goods and "is required to re-purchase the goods
... at a higher price", the goods are deemed pawned, the sale price is the loan and
the difference is the profit. s 3(3) tells the reader to look at "the substance of the
transaction and not to its form". Asserted.

### 3. The profit cap is 1.5% a month, a part month counts in full, and it stops

Second Schedule para 1: no more than 1.5% of the loan for each whole month, and 1.5%
for any balance that is part of a month. Para 2: no profit "2 months after the expiry
of the redemption period". Reading para 1(b) as charging the part month at a full 1.5%
is this encoding's reading of "1.5% of the total amount of the loan for the balance of
the term". Excess is void (s 50(2)) and an offence (s 50(3)). Asserted.

### 4. The pawnbroker's own valuation fixes what it pays if it loses the pledge

s 60: if the pledge cannot be produced, compensation is its value; if it comes back
damaged, the person chooses full value (and the pawnbroker keeps the pledge) or return
plus the decrease in value. Value is the s 48(1) valuation at the start. A low
valuation at intake therefore caps the pawnbroker's own exposure (an inference, not
stated). Asserted.

### 5. Missing paperwork makes the loan voidable, not void; on extension it costs the profit instead

ss 48(2), 49(5): without a prior valuation or a properly issued and signed ticket the
loan agreement is "voidable at the instance of the pawner". On an extension, the same
failures leave the extension valid but the pawnbroker "is not entitled to take any
profit" for the extended period (s 51(5)). Asserted.

### 6. Redemption runs until forfeiture, not until the period ends

s 54(1): a pledge can be redeemed during the redemption period (6 months, or longer if
agreed) and afterwards "before the pledge is forfeited". Forfeiture needs a notice
served within 2 months after the period ends (s 63) and comes one month after service
(s 61). Asserted.

### 7. Small things

The pawn ticket fee is capped at $2 and is chargeable only if the pawnbroker offers an
electronic mode of payment, "even if the mode of payment is not used" (Second Schedule
para 4). Taking a pawn from someone under 18 or who appears intoxicated, or advancing
other than in Singapore legal tender, is an offence (s 72), punished under the general
penalty of $20,000 or 12 months (s 79). Unlicensed pawnbroking is $50,000, with up to
12 months only on a repeat (s 6(3)). Cash sales of precious stones, metals or products
over $20,000 in a day to one customer must be reported within 15 business days (s 74A,
Third Schedule paras 1, 15). Asserted.

## What would need doing before this is worth anything

- Days are not modelled: forfeiture, notice timing and the s 67 window are counted in
  whole months, and s 54(3) (period ending on a closed day) is not encoded.
- The cash-transaction rule merges paras (a) and (b) of "relevant transaction" into a
  single daily total from one customer; customers known to act for the same person are
  not modelled separately.
- The prescribed particulars, manner of service and deemed-service rules are in
  subsidiary legislation, which was not retrieved.
- No case law or Registrar guidance was searched.
