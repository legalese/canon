# Evidence (Civil Proceedings in Other Jurisdictions) Act 1979 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/ECPOJA1979.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021; the latest amendment annotated in the body is Act 40 of 2019.

**Checks:** one module (`ecpoja-assistance.l4`), one case file
(`ecpoja-cases-assistance.l4`), 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0047**: tier 2 of the remaining Singapore Acts, ordered by everyday-life
relevance. The requirement asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. For a person in Singapore,
the answer is: when they can be ordered to give evidence for a foreign lawsuit, what
the order can make them do, and when they can refuse.

The Act has six sections, so ss 2 to 5 are encoded whole. Not encoded: s 1 (short
title), s 6 (Rules of Court on the manner of applications and references), the
court's discretion under s 4(1) as to what is "appropriate", and the amount of the
witness allowance under s 4(5), which the Act takes from High Court practice and does
not state.

## What the Act turns out to say

### 1. A foreign privilege counts only if the foreign side backs it

s 5(1)(b) lets a person refuse evidence they could not be compelled to give in the
requesting country, but s 5(2) switches that off unless the claim is supported by a
statement in the request (with any conditions fulfilled) or conceded by the
applicant. Otherwise the person can be made to give the evidence, and it is held
back only if the foreign court, on a reference, upholds the claim. A Singapore
privilege (s 5(1)(a)) needs no such backing. Asserted.

### 2. No fishing: the order cannot ask what documents you have

s 4(4): an order cannot require a person to state what relevant documents are or
have been in their possession, custody or power, or to produce any documents except
particular documents named in the order that appear to the court to be, or likely to
be, in their possession. Asserted.

### 3. Tax, monetary and revenue cases are outside the Act

s 2 defines "civil proceedings" as civil or commercial matters, but not proceedings
"arising out of any fiscal, monetary or revenue law or measure". A request in such a
case, like one in a criminal case, gives the High Court no powers under s 3. Asserted.

### 4. The foreign court gets nothing a Singapore court could not order, with one exception

s 4(3): an order may require only steps that could be required to obtain evidence in
Singapore High Court civil proceedings, even for the items listed in s 4(2) (medical
examination, blood samples, inspection of property). The one exception is testimony
not on oath, which may be ordered when the requesting court asks for it. Asserted.

### 5. The Minister's word on security is final

s 5(3): no one is compelled to give evidence that would prejudice Singapore's
security, and a Minister's certificate to that effect is "conclusive evidence".
Asserted.

### 6. Proceedings need only be contemplated, and a tribunal will do

s 3 covers requests from "a court or tribunal" outside Singapore, for proceedings
already begun or whose institution "is contemplated". A witness required to attend
is paid as a High Court civil witness would be (s 4(5)). Asserted.

## What would need doing before this is worth anything

- The Rules of Court made under s 6 (how applications and references are made) were
  not retrieved; they decide much of the practice.
- What counts as "tribunal" (for example, an arbitral tribunal) is not settled by the
  text and was not researched; the cases use an employment tribunal.
- No case law on s 4(4) or on the s 5 privileges was searched.
