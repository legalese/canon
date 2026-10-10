# Hire-Purchase Act 1969 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit's cover says "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. The last amending Act in the deposited legislative history is
Act 11 of 2013 (Insurance (Amendment) Act 2013).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it governs buying a car or household
goods on instalments, and what happens when a payment is missed and the goods are
taken back. This row takes the provisions a hirer or guarantor meets: which
agreements are regulated (s 2, First Schedule), enforceability (s 5), copies and
statements (s 8), assignment (s 11), returning the goods (s 14), repossession and its
aftermath (ss 15-17), guarantees (s 21), excessive terms charges (s 29), the time to
reopen a harsh transaction (s 32(5)), void clauses (s 33), secondhand goods (s 39)
and the offences (ss 27(2), 35-37, 44(3), 48). The implied terms (Part 3),
misrepresentation, early completion, regaining the goods (s 18), insurance and the
guarantor's other rights are not encoded, nor is anything prescribed by regulation.

## What the Act turns out to say

### 1. A car worth far more than $55,000 can still be regulated

First Schedule item 2(2): a motor vehicle is covered if its value does not exceed
$55,000 including GST and duty, "but shall exclude the cost of a certificate of
entitlement". A car priced at $95,000 of which $40,000 is the COE is inside the Act.
Item 2 does not require the vehicle to be for personal use, unlike the "consumer
goods" of item 1 (capped at $20,000 including GST); the encoding reads it that way,
which is an inference. Asserted.

### 2. After repossession the owner has 7 business days to send the Fifth Schedule notice, or loses everything

s 15(3) requires the notice to the hirer and every guarantor within 7 business days of
taking the goods; s 15(6): if it "is not served, the rights of the owner under the
regulated agreement shall thereupon cease and determine". The owner must also hold the
goods for 7 business days after that notice, longer if the hirer asks for them back
(s 16). Asserted.

### 3. The hirer gets the surplus, and the owner's claim is capped by the goods' value

s 17(1)(b) has two limbs, but both come to the same figure: the goods' value plus
what the hirer has paid, less the "net amount payable". s 17(2) is the mirror: the
owner may recover nothing that would take him above the net amount payable. "Value" is
the best price reasonably obtainable less the costs of repossession, storage, repair
and sale (s 17(3)), and the owner bears the burden of proving the price was the best
(s 17(4)). But the hirer must claim in writing within 7 business days of the notice
and sue within 3 months (s 17(5)) — unless the owner never served the notice.
"Net amount payable" is not defined in s 2 of this edition; it is an input here.
Asserted.

### 4. An unwritten agreement is beyond the court's rescue

s 5(3) lets the court dispense with defects in the particulars and notices of ss 3
and 4 where the hirer was not prejudiced, but it begins "Notwithstanding subsection
(2)" and does not reach s 5(1): "A regulated agreement that is not in writing shall
not be enforceable by the owner." Asserted.

### 5. Overcharging terms charges costs the owner all of them, not only the excess

s 29(2): if terms charges exceed the prescribed cap, the hirer may treat the
agreement as void and recover everything paid, or have his liability reduced "by the
amount included in the agreement for terms charges" — the whole amount. s 39 gives the
same reduction where secondhand goods are not described as secondhand, unless the
hirer knew or the owner did not. Asserted.

### 6. Asking to be paid for consent to an assignment counts as refusing it unreasonably

s 11(2): an owner who requires "any such payment or other consideration for his
consent" is deemed to withhold it unreasonably, and the hirer may then assign without
it (s 11(1)); only defaults and reasonable costs may be required (s 11(5)). Asserted.

### 7. Repossession needs 7 business days' notice, unless the owner proves a flight risk

s 15(1), (2); the Fourth Schedule form. The burden of proving reasonable grounds to
fear removal or concealment is on the owner. Where a notice fixes fewer than 7 days,
the encoding still requires 7 to pass (an inference; the text could also make such a
notice ineffective). Asserted.

### 8. Some clauses are void outright; a guarantee for more needs an independent solicitor

s 33 voids clauses excluding the hirer's right to return the goods, allowing
repossession on bankruptcy, or relieving the owner of liability for the dealer's
statements, among others. Clauses requiring insurance at the hirer's expense (s 25),
forbidding liens (s 40(2)) and fixing where the goods are kept (s 10) are contemplated
by the Act and not void. A guarantee for more than the balance originally payable, or
covering other goods, is void unless signed before an independent solicitor who
certifies it (s 21). Fraudulently disposing of the goods carries up to 3 years
(s 37); other offences carry 12 months, with fines of $5,000 (ss 35-37) or $3,000
(s 48). Asserted.

## What would need doing before this is worth anything

- The regulations prescribing the terms-charge cap (s 29), the overdue-interest cap
  (s 33(c)) and the fee for a repeat copy (s 8(2)) were not retrieved.
- "Net amount payable" and "net balance due" (ss 13, 17) are not defined in the
  deposited s 2; where they are defined, if anywhere, was not traced.
- Whether a document in type smaller than ten-point Times (s 47) is "not in writing"
  for s 5(1), given s 47(3), is not resolved.
- The 3- and 4-month boundaries of ss 8(2) and 32(5) are not tested.
- No case law was searched.
