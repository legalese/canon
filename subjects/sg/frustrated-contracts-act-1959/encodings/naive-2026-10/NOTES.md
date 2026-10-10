# Frustrated Contracts Act 1959 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FCA1959.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021, in operation 31 December 2021. The
latest amending Act in its legislative history is Act 7 of 1997 (in force 1 October 1997).

**Checks:** one case file, 46 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen for its **everyday-life relevance**. When a wedding venue closes, a
tour is cancelled by a border closure or a renovation is stopped by a fire, this Act
decides who gets the deposit back. The Act is short: s 1 is the short title, and
ss 2 and 3 are all encoded. The court's discretion ("as the court considers just") is
not modelled as an outcome. The encoding models only the statutory ceilings the
court must stay within. The Act does not define frustration, and this row does not
model it either. Section 7 of the Sale of Goods Act 1979, which s 3(5)(c) refers to,
was not read.

## What the Act turns out to say

### 1. A deposit comes back by default; the payee keeps only what it spent, and only if the court allows

s 2(2): sums paid before discharge are "recoverable", and sums payable "cease to be so
payable". Under s 2(3) the payee keeps anything only if the court considers it just,
and never more than the expenses it incurred before discharge. A venue that took a
$10,000 deposit and spent $3,000 preparing must refund at least $7,000. The $5,000
balance stops being payable. Asserted.

### 2. Expenses can let the payee recover money that was never paid

s 2(3) lets the court allow the payee to "retain or, as the case may be, recover" sums
"paid or payable", up to its expenses. So where $1,000 was paid, $4,000 was payable
and $3,000 was spent, the payee may keep the $1,000 and still recover $2,000 of the
balance that s 2(2) said had ceased to be payable. Reading the ceiling as the lesser
of (paid plus payable) and expenses, with the paid money used first, is an
**inference**: the text does not say in what order. Asserted.

### 3. Insurance money is ignored unless someone was obliged to insure

s 2(6): in deciding what to recover or retain, the court "shall not take into account"
insurance money payable because of the frustration, unless an express term of the
contract or an enactment required the insurance. Asserted.

### 4. Shipping, insurance and perished specific goods are outside the Act

s 3(5): voyage charterparties and other contracts to carry goods by sea are excluded,
but time charterparties and charterparties by way of demise are not. Contracts of
insurance are excluded. So is a sale of specific goods frustrated because the goods
perished. A sale of specific goods frustrated for another reason is still covered.
Contracts with the Government are covered like any others (s 3(2)). Asserted.

### 5. The contract's own clause comes first; a finished severable part is paid in full

s 3(3): if the contract provides for frustration, the court gives effect to that
clause and applies s 2 only so far as consistent with it. s 3(4): a severable part
performed before discharge, or performed except for an ascertainable payment, is
treated as a separate contract that was not frustrated. Asserted.

### 6. The Act reached back six weeks

s 3(1): the Act applies to contracts "whether made before or after 13 February 1959"
(its commencement), where discharge was on or after 1 January 1959. Discharge in 1958
falls outside it. Asserted, by year only.

### 7. A non-money benefit is capped at its value to the recipient

s 2(4): for a valuable benefit other than money, the court may award a just sum "not
exceeding the value of that benefit to the party obtaining it". The court must have
regard to the recipient's own expenses and to how the frustrating event affected the
benefit. s 2(7) lets the court treat a benefit given to a third person as obtained by
the party who assumed obligations in return. Only the ceiling and the conditions are
asserted.

## What would need doing before this is worth anything

- The court's discretion is the substance of ss 2(3) and 2(4). Only the ceilings
  are encoded. No case law on how "just" sums are fixed was searched.
- What counts as frustration (the common law) is taken as an input.
- Sale of Goods Act 1979 s 7 was not read. The exclusion in s 3(5)(c) is modelled
  only through the "goods perished" wording.
- s 2(4)(a)'s cross-reference to sums retained under s 2(3) is not modelled.
