# Currency Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited as `CA1967.txt`. The deposit says it
"incorporates all amendments up to and including 1 December 2021". The latest amending
Act annotated in the body is 6/2019. The deposit's metadata records it as the current
version as at 1 October 2026.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**REQ-0072** in `subjects/sg/requirements.jsonl`. It sits in Tier 2 of the remaining
Singapore Acts, which are ordered by how often they touch everyday life. The requirement
asks what the Act decides for a person or business it applies to. No scenario has asked
a sharper question yet. This row takes what a person paying, being paid, handling or
picturing money runs into: ss 11-14, 18-20, 23, 25 and 26. Not encoded: Part 2 (the
2002 transfer from the Board of Commissioners of Currency, ss 3-10), exchange
arrangements and fees (s 15, which depends on prescribed conditions that were not
deposited), form and design (s 17), the Currency Fund and asset backing (ss 21, 22),
seizure of counterfeits (s 24), the certificate of genuineness (s 13(8), (9)),
regulations (s 28) and the savings (s 29).

## What the Act turns out to say

### 1. The coin limit applies to the size of the payment, not the number of coins

s 13(3): coins are legal tender "for the payment of an amount not exceeding 20 times
the face value of a coin of that denomination". So $1 coins can settle a $20 debt but
not a $21 one, and 10-cent coins can settle $2.00 but not $2.10. Read literally, the
limit applies to the whole payment. On that reading a payer cannot force a few $1 coins
onto a large bill even when most of it is paid in notes. That reading is an inference
from the wording and is how the encoding works. Notes are legal tender "for the payment
of any amount" (s 13(2)). Asserted.

### 2. Writing on a note can stop it being legal tender

s 13(6)(b) treats a note as "illegally dealt with" if it has been "defaced by writing or
impressing on any note any mark, word, letter or figure". A note in that state is not
legal tender under s 13(2). Fair wear and tear does not count. Under s 13(7), a note
stained or damaged by an intelligent banknote neutralisation system (IBNS) is also
illegally dealt with, but this applies to notes only, not coins. Under s 19(1), nobody
is *entitled* to recover the value of such a note from the Authority. Any refund is "an
act of grace" at its "absolute discretion" (s 19(2)), and the note "must be
repossessed" when tendered (s 19(3)). Asserted.

### 3. A payee can refuse denominations in advance, but only in writing

s 13(4): if the payee has given the payer "written notice" that a denomination will not
be accepted, legal tender status does not apply to that payment to the extent of the
notice. Without a notice, a lawful tender "is deemed to have satisfied that debt"
(s 13(5)). The encoding treats a notice as covering the whole tender and does not model
partial notices. Asserted.

### 4. Defacing money is an offence, but cash-in-transit IBNS is excused

s 23(1) makes it an offence to mutilate or destroy any note or coin, or to print or
stamp marks on a note or names on a coin. The maximum is a fine of $2,000, with no
imprisonment. Two exceptions cover notes damaged when an IBNS goes off. One is for a
licensed security service provider that sells an IBNS or uses one for cash-in-transit
(s 23(2)). The other is for a licence applicant in a trial that a licensing officer
required (s 23(3)). Neither exception covers coins or the other limbs of s 23(1). s
23(1)(c) reaches marks made by printing, stamping "or by any similar means". Whether a
handwritten note falls under that phrase is not decided here. The enum leaves it out.
Asserted.

### 5. A coin-like token is banned outright, but a picture of a note only without permission

s 20(1) and (2) bar pictures of money in advertisements, and money designs on
merchandise, "except with the permission of the Authority". s 20(4) bars making any
piece "resembling or similar to any coin" and has no permission exception. The penalty
is up to $2,000, 3 months, or both (s 20(5)). A photograph outside an advertisement and
not on merchandise falls outside the words of s 20. That conclusion is an inference.
Asserted.

### 6. A private bearer note is fined at its own face value

s 14 forbids issuing a bill or note "payable to bearer on demand" without the Authority's
permission. Cheques drawn on a banker against funds held are carved out. The fine is
"equal to the amount of the bill, note or engagement", even beyond the Magistrate's
Court's usual jurisdiction. Arrest without warrant is available for ss 14, 20 and 23
(s 25), and every prosecution under the Act needs the Public Prosecutor's consent
(s 26). Asserted.

### 7. Demonetised money must be exchangeable for at least six months

s 18: withdrawn notes and coins stop being legal tender. The notification must allow
"a reasonable period, in any event at least 6 months" for exchange at face value. Only
the six-month floor is encoded, not reasonableness. Asserted.

## What would need doing before this is worth anything

- The regulations under ss 15 and 28 (exchange conditions and fees) and the Gazette
  notifications under ss 17(5) and 18 were not retrieved. The case file uses
  illustrative face values. The deposit does not list which denominations exist.
- The coin limit in finding 1 needs checking against any MAS guidance or case law. No
  case law was searched.
- s 12 ("validly agreed") and s 13(4) partial notices are reduced to booleans.
