# Liquor Control (Supply and Consumption) Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited as `LCSCA2015.txt`. The deposit says it
"incorporates all amendments up to and including 1 December 2021" and came into
operation on 31 December 2021. The latest amendment annotated in the text is Act 28 of
2017 (at s 2). The retrieval record calls it the current version as at 1 October 2026.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen for its **everyday-life relevance**: it decides where and when a person
in Singapore may drink in public, what happens to someone drunk in the street, and who
may sell liquor. This row takes the provisions an individual meets: the definitions of
liquor and supply and the repeat-offender rule (s 2), unlicensed supply (s 4), public
drinking (s 12), drunkenness (s 14), the Liquor Control Zone uplift (s 16), banning
notices and zone directions (ss 18 to 20), police requests (ss 21, 22), false
information (s 28) and composition (s 33). Licensing (ss 5 to 9), enforcement powers
over premises (ss 10, 11, 23), the declaration of zones (s 15), business cessation
orders (s 17), appeals (ss 25 to 27) and the miscellaneous provisions are not encoded.

## What the Act turns out to say

### 1. The Act never says when you may not drink in public

s 12(1) forbids drinking at a public place "during any prescribed no-public drinking
period applicable to that place", and s 12(2) lets the Minister prescribe different
periods for different places. The hours are not in the Act at all; they live in
subsidiary legislation, which was not retrieved. The encoding takes "within the
no-public drinking period" as an input. Asserted.

### 2. A bar is no shelter after closing time

The licensed-premises exception in s 12(3)(a) needs both that the licence allows
drinking there and that it is during trading hours. Drinking at a bar after its
trading hours, or at licensed premises whose licence does not allow on-site
drinking, during a no-public drinking period is an offence by the customer, not only
by the licensee (s 6 separately binds the licensee). Asserted.

### 3. A repeat drunken nuisance faces no longer prison term than a first one

s 14(2) (drunken annoyance) and s 14(4) (ignoring a direction to leave) carry $1,000
or 6 months for a first offence and $2,000 or 6 months for a repeat offender: only the
fine doubles. By contrast s 14(1) (drunk and incapable) rises from one month to three.
A repeat offender is one with a conviction under the same provision "not earlier than
5 years before" (s 2(2)). Asserted.

### 4. Liquor Control Zones raise penalties by half, but only for ss 4, 12 and 14

s 16 makes an offence under s 4, 12 or 14 committed in a Liquor Control Zone liable to
"not more than one and a half times the respective penalties": $20,000 becomes
$30,000, and a repeat drunk-and-incapable term of 3 months becomes 4.5. The encoding
applies the uplift to both fine and imprisonment, reading "penalties" without
distinction (an inference). Breaching a banning notice (s 19) or refusing a police
request (ss 21, 22), though they arise in the same setting, carry no uplift. Asserted.

### 5. A banning notice cannot keep you from home or work

A banning notice may be given without a hearing (s 18(3)) on reasonable suspicion of an
offence under s 12 or 14 in a zone, for no more than 30 days (s 18(4)). But s 19(2)
says it does not prevent entering or remaining to reside or to attend "the
individual's usual place of residence or work" there. A police direction to leave a
zone is capped at 24 hours, and cannot be given to someone arrested (s 20(2)).
Asserted.

### 6. Giving liquor away is not "supply"

"supply" in s 2(1) is built on selling, bartering or exchanging, including drinks
bundled into paid goods or services; nothing covers a free gift. So the licensing
requirement in s 4(1) does not reach giving a bottle away. This is an inference from
the definition. Delivery of liquor the recipient owns or ordered, emergencies and
religious rites are expressly exempt (s 4(2)). Asserted.

### 7. Liquor starts above 0.5% ethanol; composition is capped at $5,000

Liquor means a beverage or mixture with "more than 0.5% ethanol by mass or volume", or
a prescribed substance; 0.5% exactly is not liquor. An offence may be compounded for
no more than the lower of half the maximum fine and $5,000 (s 33(1)). Asserted.

## What would need doing before this is worth anything

- The regulations that prescribe the no-public drinking periods, the prescribed public
  places of s 12(3)(c), the compoundable offences and the application deadline for
  consumption permits were not retrieved.
- Whether the s 16 uplift extends to imprisonment, and whether the composition cap uses
  the uplifted fine, would need checking against practice or case law; none was
  searched.
- Licensing, trading hours and the zone declaration powers are not encoded.
