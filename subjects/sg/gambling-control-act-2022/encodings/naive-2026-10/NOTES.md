# Gambling Control Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the other naive rows (the `writing-l4-rules` skill was not loadable in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** Gambling Control Act 2022 (No. 15 of 2022), informal consolidation
"current version as at 01 Oct 2026", with amendments to Act 29 of 2024 (in force
21 September 2026) shown. The Act is not part of the 2020 Revised Edition.

**Checks:** one case file, 114 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes what an
ordinary punter, parent, young person, excluded person or small operator meets:
what counts as social gambling (s 12), the minimum ages (s 13), the offences of
gambling with or as an underaged individual (ss 30-33, 35), the punter and
found-in offences (ss 20, 26), and the maximum penalties across ss 18-37.
Licensing, approvals, advertising, entry bans, presumptions, forfeiture and
regulatory sanctions are not encoded.

## What the Act turns out to say

### 1. Running unlawful gambling carries mandatory imprisonment

ss 18, 19, 21-25, 27(1)-(3), 36 and 37 all say the offender "shall be liable on
conviction to a fine not exceeding $500,000 **and shall also be punished with
imprisonment**" for up to 7 years (10 and $700,000 for a repeat offender; s 37 is
$200,000 and 4 years). The punter offences (ss 20, 26) read "a fine ... or to
imprisonment ... or to both". Asserted.

### 2. Acting for someone else earns a lower tier, but not for every offence

Where the contravention is "by engaging in conduct described in section 6(2),
8(3) or 10(2)" (conduct on behalf of or under arrangements made by another), ss
18, 19, 22, 24, 25 and 27 drop to $200,000 and 5 years. ss 21 (financial
interest), 23 (owner or occupier) and 36 (possessing instruments) have no lower
tier. Asserted.

### 3. The minimum age depends on whether the screen is on

s 13: a lottery ticket or a sports bet at an outlet without a live broadcast needs
18; the same sports bet at premises "where ... a live broadcast of the sporting
event" is provided needs 21. s 32(7) carries the same split into the entry
offence: a lottery outlet or a no-broadcast betting outlet is not an "approved
gambling venue" for an underaged individual's entry. Asserted.

### 4. A 20-year-old gambling in a casino is underaged, but commits no s 31 offence; the person gambling with them might

Item 5 of the s 13 table applies "even if carried on within a casino", so a
20-year-old is underaged there. s 31(7) says s 31 "does not apply to gambling
within any casino". s 30 (gambling with an underaged individual) has no such
carve-out in the text read; s 17(6) disapplies Parts 4-8, not Part 2, to casinos.
Reading s 30 as reaching casino operators is an inference from the text and the
Casino Control Act 2006 was not read. Asserted as the encoding's reading.

### 5. Class-licensed and social gambling have no minimum age

Item 5 of the s 13 table excludes gambling "authorised by a class licence" and
"social gambling", and items 1-4 do not cover them. On this reading nobody taking
part in them is an underaged individual. An inference from the table's
structure. Asserted.

### 6. Social gambling must be at home, among people who know each other, and nobody else may profit

s 12(1): non-remote, at an individual's home in Singapore, participants only family
or personal acquaintances, "substantially spontaneous" (even if regular or
arranged), not for a non-participant's gain or in the course of business, and
profit only by winning. Online play among friends is never social gambling.
Asserted.

### 7. Underaged offenders are fined, never jailed, and lying about age costs more than gambling

An underaged gambler faces $1,500 (ss 31(2), 32(3)) but $10,000 for using false
evidence of age (s 33(1)); none may be imprisoned or detained for failing to pay
(ss 31(5), 32(8), 33(2)). An employer of anyone under 21 to conduct gambling
commits an offence (s 35), except a licensee employing them for office work
"wholly performed within enclosed premises". Asserted.

## What would need doing before this is worth anything

- No Regulations were retrieved: the s 12(1)(f) conditions, any s 13(2) order
  raising an age, and prescribed countable offences for "repeat offender".
- Whether remote betting on a horse race is "off-course betting" (18) or item 5
  (21) was not resolved; the encoding only models an online game of chance.
- Gaming machine rooms, restricted periods and "excluded person" status are flags
  here; the Casino Control Act 2006 provisions they depend on were not read.
- No case law or Authority guidance was searched.
