# Organised Crime Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to
Act 21 of 2025 (in force 30 December 2025, the scam-group offences) and, in the
Schedule, S 560/2026 (in force 17 August 2026) shown.

**Checks:** one case file, 111 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes what a
group is (s 2(1)), the membership and recruiting offences (ss 5, 6), the shared
penalties for supporting a group (ss 8 to 12), the sentence arithmetic for
instructing an offence and for committing one for a group (ss 7, 13), the hard
limits on organised crime prevention orders and financial reporting orders
(ss 17, 22, 26, 27), director disqualification (s 39), tipping-off (s 44), the
duty to give information (s 74) and composition (s 79). The grounds for making
the orders, investigation powers, informer protection, confiscation (Part 9),
examination orders and the list of serious offences in the Schedule are not
encoded; whether a group's purpose concerns a "serious offence" is a given fact.

## What the Act turns out to say

### 1. As deposited, "locally-linked" has no local link

The s 2(1) definition of "locally-linked organised criminal group" in the
deposit is a group seeking benefit from "any serious offence". It differs from
"organised criminal group" only by dropping limb (b), acts outside Singapore
that would be serious offences here. Nothing in the deposited words requires a
member, a meeting or an offence in Singapore. This matters because s 5
(membership) reaches only locally-linked groups, and ss 6(2), 7(2), 8 to 12(2)
and 13(2) reach people abroad only through them. A person abroad who knowingly
belongs to a local drug syndicate commits the s 5 offence; a person in Singapore
who knowingly belongs to a group profiting only from acts abroad does not. The
deposit may have lost words, or "serious offence" may itself be read as local
(an inference). The deposit was not checked against the gazetted text. Asserted.

### 2. Scam offences need knowledge, not reasonable grounds, and carry caning

The scam limbs added by Act 21 of 2025 (ss 5(1A), 6(5) to (8)) require that the
person act "knowing" what the group is. "Having reasonable grounds to believe"
is enough for every other Part 2 offence. In exchange, an individual convicted
under a scam limb "shall also be punished with caning with not less than 6
strokes": a mandatory minimum that the other Part 2 offences do not carry.
Asserted.

### 3. Recruiting someone under 21 is presumed to be knowing

s 6(4) and (8) raise the maxima (an individual $350,000 or 7 years; others
$700,000) where the recruiter knew or had grounds to believe the recruit was
"a vulnerable person or below 21 years of age". s 6(9) presumes that knowledge,
"unless otherwise proven", once the age or vulnerability is proved. Asserted.

### 4. An instruction not carried out halves the prison term but doubles the fine

s 7(4): if the instructed offence is not committed, the maximum fine is twice
the offence's but the maximum imprisonment is "half". Death or life becomes at
most 10 years, or 20 if hurt was caused. If it is committed (s 7(5)) the fine
is 4 times and the term grows by 4 years (under 4 years) or 10 years (4 or more).
Committing an offence for a group (s 13) doubles the fine and adds 2 or 5
years. Neither s 7(5) nor s 13 says what happens to death or life imprisonment.
Asserted.

### 5. Orders have hard limits

An OCPO may not be in force for more than 5 years (s 17(2)). An FRO is limited
to 5 years, or, if made on conviction, the prison sentence plus 5 years (s 22).
Neither may be made against an individual under 16 (s 27). Self-incrimination
does not excuse non-compliance (s 26(2)). Director disqualification runs 5 years
after release from prison, or 5 years or less if there is no prison sentence
(s 39(3), (4)). Asserted.

### 6. Everyone must report, and must prove their own excuse

s 74: any person aware of information about an offence under the Act must give
it "immediately" to a law enforcement officer. The burden of proving a
reasonable excuse is theirs. Having already given it under another law is a
reasonable excuse. Composition is capped at the lower of half the maximum fine
and $5,000 (s 79), so the $5,000 offence under s 74 compounds for at most
$2,500. Asserted.

## What would need doing before this is worth anything

- Check the s 2(1) "locally-linked" definitions against the gazetted text (finding 1).
- Encode Part 1 of the Schedule (199 items, several of them marked "as in force
  before 1 August 2022") so that "serious offence" is decided, not given.
- Where conduct falls under both a general and a scam limb of s 6, this row
  applies the scam limb's caning. That is an inference: the text does not say
  which charge is brought.
- The compoundable offences are left to regulations, which were not retrieved.
- No case law was searched.
