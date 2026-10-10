# Singapore Food Agency Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, which "incorporates all
amendments up to and including 1 December 2021". The latest amendment annotated in
the body is S 26/2022 (wef 13 January 2022, to s 11(2)(d)). The deposit's metadata
calls it the current version as at 1 October 2026.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. It is an institutional Act.
It sets up the Agency, and it leaves the food-safety rules themselves to the Acts the
Agency administers. This row takes the provisions with decision content: the symbol
offence (s 8), membership and disqualification (ss 9, 11(2), 12), term, resignation
and vacation of office (ss 16, 18, 20), quorum and voting (ss 23, 25), secrecy
(s 34), protection from personal liability (s 35), borrowing (s 42), the
accreditation-mark offence (s 43), composition (s 44) and officers' liability for a
corporation's offence (s 45(2)). Not encoded: functions and powers (ss 5, 6),
Ministerial directions, committees and delegation, personnel, finance other than
borrowing, offences by unincorporated associations (s 46, which mirrors s 45),
service, and the transfer and transitional Parts 8 and 9.

## What the Act turns out to say

### 1. A unanimous meeting can pass what a divided one cannot

s 25(3): a resolution passes "if it is agreed by all members present without dissent,
or if a majority of the members who are entitled to vote on the matter cast votes in
favour of it". Under s 25(4), a member who is present and does not expressly dissent
is presumed to vote in favour. So 4 members out of 12 (a quorum under s 23) can pass a
resolution if nobody dissents. But in a meeting of 10 members where 4 attend, one
dissent sinks it: 3 votes in favour are not a majority of the 10. Asserted.

### 2. The casting vote does not always break a tie

s 25(2) gives the presiding member a casting vote "in the case of an equality of
votes". The encoding counts the casting vote as one extra vote in favour and then
applies the majority test in s 25(3). On that reading, a 4–4 tie among 8 voters on a
board of 12 entitled members does not pass even with the casting vote, because 5 is
not a majority of 12. A 6–6 tie among 12 does pass. How (2) and (3) combine is an
**inference**: the text does not say. Asserted.

### 3. Permission is no defence to a look-alike symbol

s 8(2)(a) makes it an offence to use a symbol identical to the Agency's "without the
prior written permission of the Agency". Limb (b), using a symbol that "so resembles"
the Agency's "as to deceive or cause confusion", says nothing about permission. Read
literally, permission excuses identical use but not confusingly similar use. The
penalty is a fine up to $10,000, imprisonment up to 6 months, or both. Asserted.

### 4. Composition is capped at $2,000 for every offence

s 44(1): the sum may not exceed "the lower of" half the maximum fine and $2,000. That
is $1,000 for unlawful disclosure (s 34, maximum $2,000) and $2,000 for misusing an
accreditation mark (s 43, maximum $50,000). Only offences "prescribed as a
compoundable offence" qualify, and the regulations that prescribe them were not
deposited. The encoding stands in a flag for that. Asserted.

### 5. Three missed meetings end a membership, and leaving office pays nothing

s 20(1)(g): a member ceases to hold office if he or she "fails to attend 3 consecutive
meetings of the Agency without the approval of the Agency". A failure to disclose an
interest ends office only once a notice of the default has been given to the Minister
(s 20(1)(f)). s 20(2): no compensation for ceasing to hold office "for any reason".
Asserted (the compensation rule is quoted, not asserted).

### 6. A free pardon removes the prison disqualification

s 11(2)(c) disqualifies an individual sentenced to 6 months' imprisonment or more "and
has not received a free pardon". A bankrupt or a Judge is disqualified outright. The
Chairperson must be a member other than the Chief Executive (ss 9(2), 12(1)(a)).
Asserted.

### 7. The mark offence carries a heavy penalty

s 43: using an accreditation, certification or inspection mark (or a colourable
imitation) without holding a valid accreditation or the Agency's authorisation, and
without reasonable excuse, is punishable by a fine up to $50,000, imprisonment up to
3 years, or both. A District Court may impose the full penalty, and the property may be
forfeited. The Agency may borrow from the Government freely, but from any other
source only with the Minister's approval (s 42(3)). Asserted.

## What would need doing before this is worth anything

- The regulations under s 48 (including any list of compoundable offences) were not
  retrieved.
- The quorum rounding (one-third of a membership not divisible by 3) and the
  casting-vote reading are inferences that need checking.
- Nothing in the Public Sector (Governance) Act 2018, which ss 7, 20(1)(f), 21, 24 and
  25(4) rely on, was read.
- The six citing Acts were not read, so it is not known which provisions they rely on.
