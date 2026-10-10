# Weights and Measures Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill as shown in the finished example rows (the skill itself
could not be loaded in this session) and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021), informal
consolidation "version in force from 28/11/2025", deposited as
`../../registers/source-bundle/WMA1975.txt`. The latest amendment annotated is Act 7
of 2025 wef 28/11/2025 (the definition of "food"). Act 13 of 2025 wef 01/07/2025
moved administration to the Competition and Consumer Commission of Singapore.
Section numbers follow the body. The arrangement at the top of the deposit is one
number out of step from s 16 to s 28: for example, it lists "Short weight" as s 18,
but the body numbers it s 19, and s 35 cites it as s 19.

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen for **everyday-life relevance**, not citation count. Every market
stall scale, petrol pump and supermarket package in Singapore is weighed or measured
under it, and a shopper's protection against short weight is in it. This row covers
what a shopper or small trader meets:
- use for trade (s 5)
- lawful units (ss 6, 18, 40)
- when a trade instrument is lawful (s 7(2), s 40(3))
- false instruments and their defences (ss 14, 15)
- short weight and short packages (ss 2, 19)
- the food evaporation defence (s 21(3))
- the default exemptions (s 16(4))
- weighing in the buyer's presence (s 28A)
- inspectors' entry (s 30(1)(c))
- composition and penalties (ss 29A(5), 33, 35)

Not encoded:
- standards and the Second Schedule tables
- pattern approval
- regulations and orders
- the s 17 quantity-order offences
- the warranty, third-party and overseas defences (ss 20, 22, 23)
- most of s 21
- documents and road-vehicle check-weighing
- Authorised Verifiers beyond their penalty
- arrest, recall and corporate liability

No subsidiary legislation was read. So prescribed errors, prescribed instruments and
s 40 transactions are flags in the encoding, not values.

## What the Act turns out to say

### 1. A short package costs a trader less than a short scoop

s 35(1) puts short delivery (s 19(1)) and misrepresenting quantity (s 19(2)) at up to
$5,000 or 3 months or both. A prepacked package holding less than its label says is a
separate offence (s 19(3)), and s 35(1) does not list it. It falls under s 35(2): a
fine of up to $2,000 and no imprisonment. Failing to weigh loose goods in front of the
buyer (s 28A) also gets only s 35(2). Asserted.

### 2. Any shortfall in a package is an offence unless regulations say otherwise

s 19(3) is breached "if the weight, measure or number of the goods in the package is
less than that stated", with no tolerance in the Act itself. The tolerance comes only
from s 19(5): a package is deemed full if it, or its lot, meets conditions prescribed
by regulations under s 37. That saving does not apply to catch weight goods (packaged
goods sold in varying quantities). Asserted. The s 2 definitions of "non-standard"
(short by more than the prescribed error, up to twice it) and "inadequate" (short by
more than twice it) packages are encoded as a classifier. Asserted.

### 3. The 12-month defence starts the month after the label

s 14(1) makes using a false or unjust trade instrument an offence on its face. One
defence (s 14(2)(b)) covers use "during a period of 12 months immediately following
the month in which an Accuracy Label for the instrument was issued", where the trader
neither knew nor had reason to suspect the fault. Read literally, use in the month of
issue itself falls outside the window. That is the encoder's literal reading, not a
ruling. Asserted. An employee who neither knew nor suspected has a separate defence
(s 14(2)(a)). Asserted.

### 4. A restaurant meal is exempt from quantity orders but not from short weight

By default, s 16(4) exempts from the Minister's quantity orders:
- goods sold for consumption at the seller's premises
- ready-to-eat prepacked meals
- armed-forces goods
- export sales made on written notice

But s 19(8)(a) carries only the armed-forces and export exemptions over to the
short-weight offences. So a hawker's plate is still within s 19. Asserted.

### 5. The kati survives only by regulation

Under s 6(1) the only units lawful for trade are the First Schedule's metric units.
Under s 6(2) the metric carat is lawful only for precious stones or pearls. The
customary hoon, chee, tahil and kati (Third Schedule; 1 kati = 0.6048 kg) are lawful
only in transactions the Minister prescribes under s 40(1), which applies "despite
anything in this Act". Retail goods may show a non-metric unit only in addition to the
metric one, and no larger (s 18(2)). Asserted.

### 6. Scales the public may use are trade scales

s 5(3): any instrument "made available in Singapore for use by the public, whether on
payment or otherwise" is treated as in use for trade for Part 3. That brings it under
the stamping and Accuracy Label regime of s 7. Asserted.

### 7. The buyer can ask to see prepackaged goods weighed

Under s 28A(1), loose goods sold by retail by weight must be weighed at the time of
sale, in the buyer's presence, on a suitable instrument the buyer can easily see.
Under s 28A(2), goods prepackaged and weighed beforehand must be weighed in front of
the buyer on request. The encoder reads (2) as limited to goods weighed at the selling
premises. The words allow that reading but do not compel it. Asserted on that reading.

### 8. Two smaller points

- The Controller may compound any offence for up to $2,000 (s 33). Asserted.
- Inspectors may not enter, under s 30(1)(c), premises "used only as a private
  dwelling house". Asserted.

## What would need doing before this is worth anything

- The regulations need reading: the prescribed errors, the s 19(5) package and lot
  conditions, which instruments s 7 applies to, and which transactions allow customary
  units.
- The text of s 18(1)(c) is worded oddly. It makes it an offence to use an instrument
  "other than" one that measures "only by reference to" non-metric units. That reads
  inverted and was not encoded.
- s 29A(5)'s own penalty of $10,000 or 2 years is encoded as displacing s 35(2). That
  is an inference.
- The quantity orders under s 16 were not retrieved.
- No case law was searched.
