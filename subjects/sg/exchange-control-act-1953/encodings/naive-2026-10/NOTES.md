# Exchange Control Act 1953 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to and including
1 December 2021, in operation 31 December 2021), informal consolidation, version in
force from 1/4/2022, deposited as `ECA1953.txt`. The latest amendment annotated is
Act 25 of 2021 wef 01/04/2022 (Fourth Schedule para 3).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**REQ-0071**: Tier 2 of the remaining Singapore Acts, ordered by everyday-life
relevance. The requirement asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. This row takes what a person
or business meets when holding, buying, paying or carrying money and gold across the
border: the definitions and scheduled territories (s 2, First Schedule), dealing
(s 3(1)), surrender (s 4), payments (s 7), the personal representative's residence
(s 42(1)), import and export (ss 23, 24), payment for exports (s 25), exemptions
(s 33), contracts and insolvency (s 35, Fourth Schedule para 5), and the offence,
penalties, composition and consent to prosecute (Fifth Schedule Part 2). Not encoded:
travellers' cheques (s 6), compensation deals (s 9), securities (Part 4, ss 10 to 22),
debts, goods, settlements and companies (ss 26 to 32), blocked accounts (s 34, Third
Schedule), enforcement powers (Fifth Schedule Parts 1 and 3) and the Second Schedule.

**The deposit is the Act alone.** It contains no exemption order under s 33, no order
specifying currency under s 4(2), no order prescribing export territories under
s 25(1), and no notification extending the Act's life under s 1(3). Read on its own
text, the Act forbids a great deal of ordinary life; whether any of it is enforced
depends on those orders. That Singapore's controls were in practice lifted by
exemption is outside knowledge, not something the deposit says, and nothing here
relies on it.

## What the Act turns out to say

### 1. On its face, paying a US supplier from Singapore needs the Authority's permission

s 7(1)(a): "Except with the permission of the Authority, no person shall ... in
Singapore ... make any payment to or for the credit of a person resident outside the
scheduled territories". The prohibition is not limited to foreign currency, and the
First Schedule does not list the United States or Japan. Paying a Malaysian supplier is
not caught; paying a Singapore landlord on the order of a Japanese company is
(s 7(1)(b)). Only a s 33 exemption order, absent from the deposit, takes this away.
Asserted.

### 2. "Foreign currency" is not what it sounds like: sterling and ringgit are not foreign

s 2(1) excludes "any currency or notes issued under the law of any part of the
scheduled territories". The First Schedule has 65 entries, among them the United
Kingdom, Malaysia, Australia, Hong Kong SAR, India, Indonesia, Thailand and the
Philippines, and names that no longer exist, such as "Swaziland", "Western Samoa" and
the "Gilbert and Ellice Islands Colony". (That it reads like the old sterling area is
an observation, not something the text says.) So selling ringgit to a friend in Singapore is
outside s 3(1); selling US dollars or yen is inside it. Asserted.

### 3. Gold may be imported freely but not exported, and craftsmanship takes it out of the Act

s 24(c) forbids exporting "any gold" without permission; s 23 does not mention gold.
"Gold" excludes gold "materially increased in value by skilled craftsmanship", so a
crafted necklace is neither gold for s 3 nor for s 24. Postal orders, Treasury bills,
share certificates, life policies and a promissory note in a non-scheduled currency
payable outside the scheduled territories also need permission to leave. Asserted.

### 4. Holders of gold must offer it to an authorised dealer

s 4(1): a person in Singapore entitled to sell gold or specified currency "shall offer
it ... for sale to an authorised dealer" unless the Authority consents to retention.
Buying from an authorised dealer counts as consent (s 4(4)), but once the purpose stated
for it ends the consent is treated as revoked (s 4(3)), so leftover travel dollars fall
back under the duty if the currency is specified. On non-compliance the Authority may
vest the gold or currency in itself (s 4(6)). Gold needs no order; currency does.
Asserted.

### 5. The fine is $10,000 or three times the value; composition is capped at $1,000

Fifth Schedule Part 2 para 1(3): fine up to $10,000, up to 3 years' imprisonment, or
both, with discretionary forfeiture. Para 1(5): where the offence relates to property
and is not only a failure to give information, the maximum is "such fine as is
authorised by sub-paragraph (3) or a fine equal to 3 times the value". The encoding
reads this as the greater of the two, an inference: the text does not say "whichever
is greater". An offence may be compounded for not more than $1,000 (para 3), and
prosecution needs the consent of the Attorney-General or the Authority; against an
employer for an employee's act, the Attorney-General's alone (para 5). Only a person "in
or resident in Singapore" commits a Part 2 offence, though s 2(7) applies the Act's
obligations to all persons, citizens or not, in Singapore or not. Asserted.

### 6. Contracts carry an implied condition; insolvency proofs ignore missing permission

s 35(1) implies into every contract that a term needing permission "shall not be
performed except insofar as the permission or consent is given or is not required",
unless that is shown inconsistent with the parties' intention (s 35(2)). In a
Singapore bankruptcy, winding up or estate, such a claim is admitted to proof as if
permission had been given, but payment out remains subject to Part 3 (Fourth Schedule
para 5). Asserted.

### 7. The Act was enacted to last one year

s 1(2): "This Act shall continue in force for a period of one year from the date of the
coming into force thereof", extendable by Gazette notification (s 1(3)). The
consolidation presents it as current, which implies continuing extensions; none is in
the deposit. Not asserted.

### 8. Exports to prescribed territories must be paid for within 6 months

s 25(1): goods to a prescribed territory may go only if payment has been or will be
made to a Singapore resident "not later than 6 months after the date of exportation"
and the return accords with the objects of the Act; s 25(2) lets the Authority lengthen,
shorten or remove the deferred-payment period. No territory is prescribed in the
deposit. Asserted.

## What would need doing before this is worth anything

- Retrieve the exemption orders under s 33, the orders specifying currency (s 4(2)) and
  notes (s 23(1)(a)), any order prescribing export territories (s 25(1)), and the
  extension notifications under s 1(3). Without them every "breach" here is a breach of
  the bare text only.
- Whether the euro, issued for Cyprus and Malta (both in the First Schedule) as well as
  for unlisted states, is "foreign currency" was not decided; the encoding leaves the
  euro out.
- The joint-person rules in s 2(2), (3) were not modelled: under s 2(2) a prohibition
  applies if any one of several joint persons has the residence attribute.
- Securities (Part 4), blocked accounts and the enforcement powers were not read beyond
  their headings.
- No case law was searched.
