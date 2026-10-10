# Commodity Trading Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 25
of 2021 (in force 1 April 2022) shown.

**Checks:** one case file, 98 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**8 of the 527 Singapore Acts** deposited here cite it. This row takes the parts a
broker, adviser, pool operator or spot trader actually meets. They are who needs a
licence (ss 12, 13, 13A, 14A and the Schedule, with the 8 October 2018 cessation),
"accredited investor", approval of markets and clearing houses (ss 4, 8), risk
disclosure (s 32), and the penalties and prosecution rules (ss 33, 49, 57, 58, 60).
Not encoded: the Board's approval criteria and business rules, grounds for refusing
or revoking a licence, accounts and audit, segregation of funds, the Board's powers,
secrecy, and Schedule item 1(a). The "Board" is the Enterprise Singapore Board (s 2).

## What the Act turns out to say

### 1. Since 8 October 2018 the licensing gate is closed to new forward-market business, but not to spot trading

s 12(2): s 12(1) "ceases to apply to any person who commences business as a commodity
broker on or after" 8 October 2018. s 13(2) does the same for trading advisers and pool
operators, and for their representatives and broker's representatives. s 4(2) and
s 8(2) do it for new commodity markets and clearing houses. s 13A, which licenses spot
commodity brokers, spot pool operators and their representatives, has **no such
subsection**. So a broker that started in 2019 needs no licence. A spot broker that
started in 2019 does. Asserted.

### 2. A representative of a new principal escapes only if it holds no transitional licence

s 13(2)(a), (c), (e) lift the requirement for a representative of a post-2018 principal
"who does not hold a transitional licence". A representative who does hold one stays
inside s 13(1). "Transitional licence" is defined by "section 66" (s 13(5)), and **no
s 66 appears in the deposited text**: the arrangement ends at s 65 and the body ends
at s 65 and the Schedule. The encoding takes the transitional licence as a bare fact.
Asserted.

### 3. The exemptions for banks and accredited-investor business do not reach spot trading

Schedule items 1(c) (dealing "only with accredited investors"), (d) (licensed banks
and merchant banks) and (e) (Finance and Treasury Centres and approved oil or
international commodity trading companies) are "in respect of sections 12(1) and
13(1)". s 13A has only items (f) (own-account spot trading that solicits no public
funds) and (g) (a pure order-taker). A bank acting as a spot commodity broker
therefore has no Schedule exemption. Section 61 lets the Board, with the Minister's approval, exempt any person, but
that power is not modelled. Asserted.

### 4. The order-taker exemption needs physical delivery for brokers but not for spot

Item 1(b), for s 12(1), requires that the person is not a party, does not carry the
customer's position and takes no customer money, **and** "there is physical delivery".
Item 1(g), for s 13A, has the first three conditions and not the fourth. Item 1(b) does
not mention s 13(1), so a broker's representative who meets it is still caught.
Asserted.

### 5. "Accredited investor" uses "exceed" for assets and "not less than" for income

Schedule para 2: an individual whose net personal assets "exceed $2 million" or whose
income in the preceding 12 months "is not less than $300,000". A corporation needs net
assets "exceeding $10 million". Exactly $2 million of assets does not qualify; exactly
$300,000 of income does. The Board may prescribe other amounts. Asserted.

### 6. Market abuse costs a company more but cannot send it to prison, and only the Public Prosecutor can start it

s 49: a Part 7 offence (false trading, bucketing, spreading false-trading information,
manipulation and cornering, fraudulent devices, fraudulently inducing trading) carries
up to $250,000 or 7 years for an individual, and up to $500,000 for a body corporate.
s 58(1)(a): proceedings "may be taken only with the consent of the Public Prosecutor".
The Board may prosecute any other offence itself. Asserted.

### 7. Risk disclosure must come first, and for advisers before the earlier of two moments

s 32(1): no account opens without a separate written risk disclosure document and a
signed and dated acknowledgment. s 32(2): a pool operator must deliver "on or before
the date" it solicits. s 32(3): an adviser must deliver "at or before" the solicitation
or the agreement, "whichever is the earlier". Breach is a Part 5 offence, $30,000 or 3
years (s 33). Asserted.

### 8. A fine-only offence can be compounded, but only on a written admission and payment within 14 days

s 58(2), (3). The title offence of s 57 ($20,000 plus $2,000 a day after conviction)
and the s 60 general penalty ($20,000) are fine-only. Asserted.

## What would need doing before this is worth anything

- Section 66 ("transitional licence") is missing from the deposit. The Act needs
  checking against SSO to see whether it exists, was omitted from the PDF, or is a
  cross-reference error.
- The arrangement of sections in the deposit lists Part 7 out of step with the body.
  The body's numbering (43 false trading to 49 penalties) was followed.
- The regulations under ss 13A(2), 16, 30 and 63 were not retrieved. They may exempt
  further classes (s 63(4)) or change the accredited-investor amounts.
- Whether an activity is a "commodity contract" at all, and so outside the futures
  regime of the Securities and Futures Act 2001, is taken as given. The definitions in
  s 2 and the s 3 carve-outs are not modelled.
