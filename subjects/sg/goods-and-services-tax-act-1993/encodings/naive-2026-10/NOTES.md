# Goods and Services Tax Act 1993 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 35
of 2022 and S 109/2023 shown in force.

**Checks:** one case file, 40 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**20 of the 527 Singapore Acts** deposited here cite it. This row takes the charge
(s 8), the rate (s 16), tax-inclusive pricing (s 17(2)), contracts that span a rate
change (s 40), liability to register (First Schedule) and exempt supplies (Fourth
Schedule Part 1). Not encoded: time and place of supply, the reverse charge, input
tax, zero-rating, special cases, assessment, appeals and offences.

## What the Act turns out to say

### 1. Prices include GST, but a later rate rise can be added on top

s 17(2): the value of a supply is the amount which, "with the addition of the tax
chargeable, is equal to the consideration". The tax is inside the agreed price: $109
at 9% is $100 plus $9 GST. But under s 40(1), if the rate changes between contract and
supply, the supplier **may add** the increase unless the contract expressly excludes
it or the change was taken into account. A $1,070 price agreed at 7% became $1,080
when supplied at 8%. Asserted.

### 2. Registration turns on "exceeded" $1 million, and happens whether or not you notify

First Schedule para 1(1): liability arises when taxable supplies in a calendar year
"has exceeded $1 million", so exactly $1 million does not trigger it. The forward test
is reasonable grounds to expect more than $1 million in the next 12 months. Para 4(2):
the Comptroller registers the person "whether or not the person so notifies", from 1
March of the following year. Asserted.

### 3. Overseas digital suppliers have a two-part test

Para 1A: worldwide supplies over $1 million **and** Seventh Schedule supplies to
Singapore over $100,000. Asserted.

### 4. Life insurance is exempt; motor insurance is not. A flat is exempt; a shop is not

Fourth Schedule Part 1 para 1(l) exempts only "a life insurance contract". General
insurance is not listed, so it is taxable. Para 2 exempts land with a building "used or
to be used principally for residential purposes"; commercial property is not listed.
A collector's coin is carved out of the currency-exchange exemption, and investment
gold and digital-token exchanges are exempt. Asserted.

### 5. Smaller things worth recording

- **s 8(1):** only a supply by a registered (or registrable) person in the course of
  business is charged. A director selling their own car privately is outside it.
- **s 10(2)(a):** a free gift is not a "supply".
- **s 16:** the section now lists rates only from 2003; the 3% rate of 1994 is no longer
  in the text.

## What would need doing before this is worth anything

- Time of supply (ss 11 to 12A) and the Part 6A transitional rules for supplies that
  span a rate change are needed to apply s 16 to a real invoice.
- The zero-rating provisions (s 21) and input tax (Part 4) are what a registered
  business actually needs.
- The Comptroller's e-Tax Guides and any case law were not retrieved.
