# Enterprise Singapore Board Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (revised edition to
1 December 2021), with later annotations shown to Act 17 of 2026 (wef 1 July 2026);
the deposit's metadata says "Current version as at 03 Oct 2026".

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. It is an institutional Act,
so this row takes the rules with decision content: who may sit on the Board and when
office is vacated (ss 11(2), 18, 20), meetings, quorum and voting (ss 22(3), 23, 25),
secrecy and immunity (ss 34, 35), the offences and their maximum penalties
(ss 8(2), 34(2), 46 to 48, 50, 51), the bar on registering names that use the Board's
protected words (s 49), and the composition ceiling (s 52). The Board's functions and
powers, Ministerial directions, finance (including the export levy of s 38), the
inspection powers of s 45, corporate liability, and the transfer and transitional
Parts are not encoded.

The arrangement of sections at the top of the deposit is out of step with the body
from Division 2 of Part 3 and again in Part 7 (for example, the arrangement lists
"Composition of offences" at 51; the body has it at s 52). This row follows the body.

## What the Act turns out to say

### 1. A registering authority must refuse any name containing "ESG", unless the Board consents

s 49(1) applies "despite anything in any written law": except with the Board's
consent, a registering authority must not register a company, firm or other body, or
a trade mark or design, bearing a name or mark in s 49(2). That list includes
"Singapore Standard", "Technical Reference", "IE Singapore", "SPRING Singapore",
"Enterprise Singapore Board" and "ESG", "in any form", and names so nearly resembling
them as to be likely to deceive. Read literally, a firm called "ESG Advisory" needs
the Board's consent (whether that literal reading is how the provision is applied was
not checked; the text gives no exception for other meanings of the letters). Asserted.

### 2. Misusing an accreditation or certification mark is the heaviest offence by far

s 47(4): up to $50,000 or 3 years, and s 47(5) lets a District Court impose the full
penalty despite the Criminal Procedure Code 2010; s 47(6) allows forfeiture. Use is
lawful only with a valid accreditation or certification for that use, or the Board's
authorisation. Every other offence encoded tops out at $10,000 (s 46) or less;
failing to answer a notice for returns (s 51) is a fine of up to $1,000 with no
imprisonment. Asserted.

### 3. Lying in a grant application is an offence even if no grant is obtained

s 46(1)(a) catches a statement known to be false or misleading in a material
particular, made in or in support of an application for any incentive, grant, loan or
other financial benefit from the Board; s 46(3) says expressly that not obtaining the
benefit is no defence. $10,000 or 12 months. Asserted.

### 4. Composition is capped at the lower of half the maximum fine and $5,000

s 52(1): so $5,000 for the mark offence (half of $50,000 would be $25,000), $2,500 for
a false Singapore Standard claim, $1,000 for breach of secrecy. Only offences
"prescribed as a compoundable offence" can be compounded; the regulations were not
read, so the encoding computes the ceiling only. Asserted.

### 5. Quorum is at least 5 and at least a third, and silence counts as a yes

s 23(1): the quorum is the higher of one-third of the members and 5. With 16 members,
5 present is not enough (5 x 3 < 16). s 25(4): a member present is presumed to have
voted for a decision unless he or she expressly dissents or votes against; the
presiding member has a casting vote on an equality (s 25(2)). The encoding counts
every non-dissenting member present as a vote in favour. Asserted.

### 6. The Minister can remove a member at any time, without reasons or compensation

s 15(1) "at any time and without giving any reason"; s 20(2) no compensation on
ceasing to hold office "for any reason". A failure to disclose an interest vacates
the office only once a notice about the default is given to the Minister (s 20(1)(f));
missing 3 consecutive meetings does so unless the Board approved (s 20(1)(g)). The
term is 3 years or a shorter period in the instrument (s 18(1)). Asserted.

### 7. Disqualification follows the usual list, with a 6-month imprisonment threshold

s 11(2): undischarged bankrupts, those in a composition with creditors, judges and
judicial officers, those sentenced to 6 months' imprisonment or more without a free
pardon, disqualified directors (Companies Act and VCC Act), and those lacking
capacity. Asserted.

### 8. Secrecy has five exceptions, and the Board's authorisation must come first

s 34(1)(b) requires "prior authorisation from the Board"; the encoding treats
authorisation given afterwards as no exception (an inference from "prior"). $2,000 or
12 months (s 34(2)). Officers acting in good faith and with reasonable care are
protected from liability (s 35(1)). Asserted.

## What would need doing before this is worth anything

- The regulations prescribing compoundable offences and any further protected names
  under s 49(2)(b) ("other prescribed words or names") were not read.
- s 18(1) does not say what happens if an instrument states a period longer than
  3 years; the encoding caps it at 3, which is an inference.
- Voting ignores members prevented from voting under s 26 of the Public Sector
  (Governance) Act 2018, and s 49(2)(c) (names that "so nearly resemble") is not
  modelled beyond the fixed examples.
- No case law or Board practice was searched.
