# Interpretation Act 1965 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from 5
December 2025).

**Checks:** one case file, 28 assertions satisfied, 0 errors.

## Why this Act, and why scoped

Requirement **REQ-0013** in `subjects/sg/requirements.jsonl`, raised three times by
the `cradle-to-grave-simone` scenario, asked this Act when a person born on 14 March
2003 attains the age of 21 "for the purposes of written law". This row takes what the
Act says about time: ss 2 (month, year), 50 (computing periods of days) and 51
(standard time). It also records that the Act has no provision on attaining an age.

## What the Act turns out to say

### 1. The Interpretation Act does not say when a person attains an age

No provision deals with it. None of these words appears anywhere in the deposited
text: "age", "aged", "attain", "attains", "attained", "birth", "birthday",
"anniversary". s 50 governs periods of **days** only, and s 2 says only what a month and
a year are. REQ-0013's expected answer ("the anniversary of birth, at the start of the
day") cannot be taken from this Act. Asserted as a negative: `this Act fixes when a
person attains an age` is FALSE.

The rule is instead stated Act by Act. Seven deposited Acts each carry their own clause:
- Women's Charter
- Central Provident Fund
- CareShield Life
- MediShield Life
- Child Development Co-Savings
- Children and Young Persons
- Social Residential Homes

Each says a person attains an age on the anniversary of birth, and that someone born
on 29 February has a 1 March anniversary in non-leap years. The Acts this scenario
event engaged (Parliamentary Elections, Human Organ Transplant, the Wills Act, Mental
Capacity) are not among them. For those, the answer must come from case law, which this
row does not encode. A new ledger entry raises that.

### 2. Only Sundays and public holidays are excluded days, not Saturdays

s 50(b): "if the last day of the period is a Sunday or a public holiday (which days are
called in this section excluded days)". A period ending on a Saturday ends on the
Saturday. Asserted.

### 3. For six days or less, excluded days are not counted at all

s 50(d): for any time "not exceeding 6 days, excluded days must not be reckoned".
A 6-day period from Monday 1 January 2024 ends on Monday 8 January, the same day as a
7-day period. Asserted.

### 4. Smaller things worth recording

- **s 50(a):** the day of the event is not counted.
- **s 50(c):** an act due on an excluded day is in time on the next day that is not
  excluded.
- **s 51:** standard time is UTC + 8 hours, unless changed by Gazette notification.

## Encoding note: days are numbers

The installed `l4` binary has no date library (`IMPORT daydate` does not resolve), so a
day is a whole number from day 0 = Monday 1 January 2024, and Sunday is `n MODULO 7 =
6`. Public holidays are an input of up to three day numbers. Dates before 2024 are not
supported by this convention. With a current `l4` the row should be rewritten on
`DATE`.

## What would need doing before this is worth anything

- **Decide the general age rule** (new ledger entry): which decided case states when a
  person attains an age for Acts without their own clause, and whether it agrees with
  the anniversary rule the seven Acts state.
- The real Singapore public-holiday calendar (Holidays Act) is an input, not encoded.
- s 50 applies "unless the contrary intention appears"; that qualifier is not modelled.
