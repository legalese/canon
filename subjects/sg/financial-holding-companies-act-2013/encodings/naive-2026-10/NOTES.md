# Financial Holding Companies Act 2013 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 13 of 2013, informal consolidation, "version in force from
9/3/2025", with amendments to Act 5 of 2025 annotated. The deposit carries the
2013 numbering ("No. 13 of 2013"); it is not marked as a 2020 Revised Edition text.

**Checks:** one case file, 122 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes what a
group, an investor or a practitioner meets first: whether a company is a financial
holding company and can be designated (ss 2(1), 4), holding out and use of the name
(ss 6, 7), permitted activities (s 8), the controller thresholds and who must clear
a change of shareholding or control (ss 11 to 15, 19 to 22, 25), the penalties and
defences (s 26), and the major-stake and immovable-property limits (ss 31, 32).
Information powers, the levy, objection and direction powers, exposures and equity
limits, capital and liquidity, audit and inspection, control and winding up,
foreign assistance and Part X are not encoded.

## What the Act turns out to say

### 1. Without a bank subsidiary, there is no 12% controller tier at all

s 14(1) (company with a Singapore bank subsidiary) requires the Minister's approval
to become a 12%, 20% or indirect controller. s 21(1) (company without one) lists only
a 20% controller and an indirect controller. Nothing in ss 12 to 21 needs clearing
to become a 12% controller of an insurer-led group. (A 12% holder may still be a
"substantial shareholder" under s 20, a Companies Act term not read here.) Asserted.

### 2. The Minister clears bank groups; the Authority clears the rest

Every Part IV step for a company with a bank subsidiary is the Minister's (ss 12(1),
13(1), (3), 14(1)), and s 15(1)(b) adds a "national interest" test on top of the
Authority's fit-and-proper finding. Without a bank subsidiary the Authority approves
(ss 19 to 22) and there is no national-interest test. A 5% acting-together pact over
disposal needs only "first notifying the Authority" (s 20(4)), where for a bank group
the same pact needs the Minister's approval (s 13(3)). Asserted.

### 3. Prison only for 20% and indirect controllers

s 26(1) punishes an unapproved merger, substantial shareholding, pact, or 12%
controllership by fine only (an individual up to $125,000, others $250,000). s 26(2)
adds up to 3 years' imprisonment for an individual who becomes a 20% or indirect
controller without approval. Asserted.

### 4. Two narrow defences, and no "I didn't mean to"

s 26(3): for ss 13, 14, 20 and 21, a person who was unaware, notified within 14 days
of becoming aware, and took the directed action has a defence. s 26(4): for ss 14 and
21 only, a person pushed over a threshold by a family associate's increase, with no
pact with that associate, who notified within 14 days of the contravention, has one
too. s 26(5): otherwise lack of intent or knowledge is no defence. A merger without
approval (ss 12, 19) gets neither defence. Asserted.

### 5. "Not less than" 12% and 20%, but "exceeding" 10%

s 11(2) controllers are caught at exactly 12% or 20%. A s 31(10) major stake must
exceed 10% of shares or votes, so a designated company may hold exactly 10% of
another company without approval. Asserted.

### 6. A designated company may own no investment property at all

s 32(1) bars a designated company from acquiring or holding "interests in or rights
over immovable property, wherever situated", subject to a 6-month grace after
designation (longer if the Authority allows) and to the s 32(5) exclusions: premises
used for the group's business, staff housing or amenities, security and enforcement,
and property held for others. Asserted. The encoding treats every holding within the
grace period as lawful; whether a NEW acquisition inside that period is protected by
s 32(2)(a) ("may ... hold") is an inference, not tested against anything.

### 7. Smaller points

- s 2(1): a holding company is a financial holding company when its financial
  subsidiaries account for 50% or more of ANY ONE of assets, capital, liabilities or
  revenue of the group (encoded as the largest of the four). Asserted.
- s 4(1): only Singapore-incorporated companies can be designated; an intermediate
  one only if the Authority considers its bank or insurer subsidiary significant to
  the group or to financial stability. Asserted.
- s 7(5): a business lawfully using a name suggesting association before designation
  may go on for 3 years. Asserted.
- s 8(1): anything beyond holding, permitted shareholdings, group support services and
  Authority-specified activities needs approval. Asserted.

## What would need doing before this is worth anything

- "Substantial shareholder" (Companies Act s 81) and the s 11(3) associate rules are
  inputs, not computed.
- The transitional cease-or-apply duties (ss 13(2), (4), 14(2), 20(2), (5), 21(2)) and
  their "excepted persons" under the Banking and Insurance Acts are not encoded.
- Regulations under ss 30, 31(8), 32(3) and the Authority's notices under Part VI
  (capital, liquidity, leverage) were not retrieved.
- No MAS guidance or case law was searched.
