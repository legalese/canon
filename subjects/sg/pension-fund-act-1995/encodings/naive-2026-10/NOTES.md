# Pension Fund Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit
(`PFA1995.txt`) says it "incorporates all amendments up to and including
1 December 2021"; the latest amendment annotated is 4/2021, on Schedule item 13.

**Checks:** one case file, 50 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**8 of the 527 Singapore Acts** deposited here cite it. It is a short institutional
Act: it creates the Pension Fund as a Government fund and says what goes in, what
may come out, who covers a shortfall and how the Fund is examined. This row
encodes ss 4, 6-10, 12(2), 13 and the Schedule. Not encoded: establishment (s 3),
investment (s 5, which points to s 7 of the Financial Procedure Act 1966, not read),
accounts and audit (ss 11, 12(1)), the Financial Procedure Act's general
application (s 14) and regulations (s 15).

## What the Act turns out to say

### 1. The Consolidated Fund guarantee has a gap for some pre-1995 benefits

s 8(1) charges any shortfall in the Fund on the Consolidated Fund, but s 8(2) says
this "applies only to" public-service benefits that (a) were charged on the
Consolidated Fund before 1 April 1995 or (b) are provided under a law enacted on or
after 1 April 1995. A benefit under a pre-1995 law that was not charged on the
Consolidated Fund before that date falls outside the guarantee on the text. Whether
any such benefit exists was not checked. Asserted.

### 2. The diplomatic local-staff gratuity stands outside the public-service frame

Every other s 6(1) purpose is tied either to persons who have been in the public
service and a law in the Schedule ((a), (b)) or to a prescribed superannuation
scheme ((c)). Paragraph (d) — a gratuity on the death or retirement of "members of
the local staff of any diplomatic mission of Singapore" — needs neither. But the
s 8 deficiency guarantee is limited to persons who have been in the public service,
so on the text it does not obviously cover that gratuity (an inference: the Act does
not say whether local staff are in the "public service"). Asserted as encoded.

### 3. Two locks on every payment

s 6 says moneys "may only be withdrawn and applied" to the listed purposes; s 7
adds the Fund's own administration and investment expenses; s 10(2) adds that no
payment may be made "unless the payment is authorised by the Minister". A
scheduled pension without Ministerial authority fails; so does an authorised grant
to a purpose outside the list. Asserted.

### 4. Injury benefits need the injury to be attributable to the service

s 6(1)(b) covers injury benefits only "in respect of injuries received in and which
are attributable to that service". Asserted.

### 5. The Schedule names one subsection of the Singapore Armed Forces Act

Item 10 is "Section 206(1) of the Singapore Armed Forces Act 1972", not the Act as a
whole. The Home Affairs Uniformed Services Superannuation Act 2001 appears in s 9(3)
as the home of the INVEST Fund but is not in the Schedule. The Minister can amend the
Schedule by Gazette order (s 6(2)), so the list is only as current as the deposit.
Asserted.

### 6. Surplus can leave only three ways, each by warrant

s 9: to the Consolidated Fund (moneys "not required to meet the liabilities" in the
Minister's opinion), to the SAVER-Premium Fund, or to the INVEST Fund (the value the
Minister determines for members who opted into those plans). Asserted.

### 7. Examinations at most every five years, and on any costly amendment

s 13(1): periods "not exceeding 5 years". s 13(2): an amendment to the Schedule, a
scheduled law or a prescribed scheme that "affects the cost of benefits" or "creates
an initial unfunded liability" forces a fresh examination; every report goes to
Parliament "forthwith" (s 13(4)). The financial year runs 1 April to 31 March
(s 12(2)). Asserted.

### 8. Net income nets realised gains and losses

s 4(2): investment income plus profit, or minus loss, on realisation. Asserted.

## What would need doing before this is worth anything

- The prescribed superannuation schemes (s 6(1)(c)) are left to regulations, none
  retrieved.
- "Public service" (s 2) is collapsed into one flag; its four inclusions are not
  modelled.
- None of the 13 scheduled laws, nor the Financial Procedure Act 1966, was read.
- No Gazette orders amending the Schedule after 1 December 2021 were searched.
