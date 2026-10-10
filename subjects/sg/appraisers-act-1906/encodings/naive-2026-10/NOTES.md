# Appraisers Act 1906 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
"incorporates all amendments up to and including 1 December 2021"; the latest
amending Act annotated in the body is Act 4 of 2021.

**Checks:** one case file, 50 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**4 of the 527 Singapore Acts** deposited here cite it. The Act has only ten live
sections, so nearly all of it is encoded: who is an appraiser (s 2), the duty to be
licensed (s 4), the fee bar (s 6(4), (5)), the contents, expiry and renewal of a
licence (s 7(1), (2)), the offence (s 7(3)), refusal and cancellation (ss 10, 11) and
trial (s 12). Not encoded: s 6(1) to (3) and (6) (who grants, Gazette notice, the
Minister's fee order), s 13 (regulations) and Form A beyond its expiry line. The Act
states no fee amount.

## What the Act turns out to say

### 1. Only valuers of immovable property need a licence

s 2 deems an appraiser anyone who values "any estate or immovable property, lands,
tenements or hereditaments", or interests in them, for reward. Goods, shares and
vehicles are not mentioned. Treating a paid valuer of those as outside the Act is an
inference from the words, not a stated exclusion. An unpaid valuation is outside s 2.
Asserted.

### 2. The two offences in s 7(3) are joined by "and"

s 7(3) reads "(a) having had such a licence continues ... and omits to renew it; and
(b) carries on a trade or business ... without taking out a licence, shall ... each be
guilty of an offence". Read literally, both limbs would have to hold together; "each"
suggests two offences. This encoding treats them as alternatives (an inference): a
lapsed licensee who keeps working, and someone who never took out a licence, each
commit an offence. The only penalty is a fine of up to $2,000; there is no
imprisonment. Asserted.

### 3. Renewing late is not, on its face, an offence

s 7(2): every licence "expires on 31 December and must be renewed annually at least
10 days before" expiry, so by 21 December. But s 7(3) punishes only continuing in the
next year without renewing. Renewing on 25 December breaches s 7(2) yet falls under
no penalty in the Act. Asserted (the deadline; the absence of a penalty is a reading).

### 4. Refusal needs no reason; cancellation does

s 10: the Comptroller of Property Tax "may refuse any application" with no stated
ground, but may cancel only for a conviction under the Act or a failure to account for
money or property held as a licensed person. s 11 adds court judgments finding a
breach of trust or duty, or return commission paid to an employer who is accountable
to someone else for the sale proceeds. Return commission to an employer selling on its
own account is not a ground. Asserted.

### 5. No fee, no licence

s 6(5): "No licence may be granted or renewed ... until the fee has first been paid."
The fee is set by Ministerial order by class of licence (s 6(4), (6)); no amount is in
the Act. Asserted.

## What would need doing before this is worth anything

- The Ministerial fee order and any regulations under s 13 were not retrieved.
- That a licence expires on 31 December of the year of grant is an inference from s
  7(2) and Form A.
- The relationship between this Act and any other valuation or estate-agency
  regime was not examined; the 4 citing Acts were not read.
- No case law was searched.
