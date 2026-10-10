# MediShield Life Scheme Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit's cover says it
incorporates amendments up to 1 December 2021, but the body carries annotations to Act
40 of 2024 (in force 1 April 2025), the latest amendment seen.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes what an insured
person, a paying parent, a defaulter's agent, a medical institution or a person under
investigation actually meets: who is covered (s 3(3)), the premium deadline and who
may be made to pay (s 4), the late-payment penalty cap (s 17), objections and joint
moneys (ss 12(4), 13), the notice rule for revoking an institution's approval (s 3B(3),
(4)), the offences (ss 16(6), 19, 21(4), 22, 29), composition (s 24) and a minor's
opt-out (ss 27(4), 28(6)). Refunds, shortfalls, the Fund and Council, recovery through
Government payments and suits, corporate officers' liability, the disclosure gateways
and service of documents are not encoded. Premium amounts and the interest and
penalty rates are prescribed elsewhere and were not retrieved.

## What the Act turns out to say

### 1. A false declaration without intent carries a penalty, not a fine — and companies pay five times

s 19(2): a person who knowingly makes a false or misleading health declaration, means
declaration or claim application is liable to "a penalty equal to the relevant amount"
if an individual, or "5 times the relevant amount" otherwise. There is no fine and no
imprisonment under s 19(2). Only if it is done with intent to underpay or be overpaid
(s 19(3)) does a fine arrive ($5,000 or 12 months for an individual; $10,000 and no
imprisonment for anyone else), plus a further penalty of 2 or 4 times the relevant
amount. Oddly, the non-individual multiplier is *lower* with intent (4x) than without
(5x), though with intent a fine is added. The "relevant amount" counts what *would*
have been undercharged or overpaid had the statement been accepted (s 19(4)), so a
caught attempt still costs. Asserted.

### 2. The late-payment penalty is capped at 17%

s 17(3): penalties on a period's premium and interest must not exceed 17% of the
premium plus s 11 interest for that period. Interest and penalty can only begin after a
Board-permitted period of at least one month (ss 11(1), 17(1)). The rates themselves
are left to regulations. Asserted.

### 3. Parents — including step-parents and anyone with custody — can be billed until the child turns 21

s 4(1)(c)(ii) lets the Board require "a parent or both parents" to pay if the insured
person has not attained 21 at the beginning of the insurance period; s 4(3) widens
"parent" to adoptive parents, step-parents, guardians and anyone with actual custody.
The premium is due within 30 days of the period's start or any later date the Board
permits, and the Board may take it from medisave "Despite anything in the CPF Act"
(s 4(2)). Asserted.

### 4. Composition is always capped at $1,000 for the offences in this Act

s 24(1) caps composition at the lower of half the maximum fine and $1,000. Every fine
in the encoded offences is at least $5,000, so the half-fine limb never bites: the cap
is $1,000 throughout. Which offences are compoundable is prescribed elsewhere. Asserted.

### 5. A defaulter can be stopped at the border, and leaving knowingly is a crime

s 16 lets a recovery body direct the Police or Immigration to prevent a defaulter from
leaving Singapore, with force and passport detention if needed. A defaulter who knows
of the direction and leaves or tries to leave without paying or giving security
commits an offence ($5,000 or 12 months) and may be arrested without warrant
(s 16(6)). Asserted.

### 6. Joint accounts are presumed split equally, but minors' accounts are out

s 13(3) presumes equal shares; s 13(9) excludes partnership accounts, trust accounts
and any account with a minor as a holder. The defaulter's agent must give owners
notice within 14 days and allow at least 42 days before paying; owners have 28 days to
object. A defaulter's agent has 14 days to object to the declaration itself (s 12(4)).
Asserted.

### 7. A minor may refuse health and means checks only from 16, and only if the paying parent does not object

ss 27(4), 28(6): a person under 21 may opt out of information-gathering for premium
loading or means testing only if 16 or over and no person liable to pay the premium
under s 4(1)(c)(ii) objects. Asserted.

### 8. No hearing is owed to an institution that no longer exists

s 3B(3) requires written notice and a chance to make representations before revoking
or suspending a medical institution's approval, but s 3B(4) drops it where a natural
person has died or been adjudged bankrupt, or another entity has been dissolved,
wound up or ceased to exist. Asserted.

## What would need doing before this is worth anything

- The premium tables, interest rates, penalty rates and the compoundable-offences list
  are in regulations, which were not retrieved.
- s 19(1)(b) and (c) (omissions, and information given to others) are folded into one
  "false or misleading and known" test; the knowledge limbs of (c) are not separated.
- The s 29(2) protections are reduced to one flag ("acted in good faith in accordance
  with Part 5"); their four heads are not encoded separately.
- Minor's opt-out: the encoding treats "a paying parent objects" as a single flag; the
  case where no one else is liable to pay is treated as no objection (an inference).
- No case law was searched.
