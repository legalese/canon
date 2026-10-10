# Supply of Goods Act 1982 — naive encoding

**Method: naive.** Straight from the deposited text with the conventions of the
`writing-l4-rules` skill and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SGA1982.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31 December
2021. The latest amendment in its Legislative History is Act 44 of 1996 (commencement
1 January 1997). The Act is the UK Supply of Goods and Services Act 1982, applied in
Singapore from 12 November 1993 by the Application of English Law Act 1993.

**Checks:** one module, one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen because it matters in everyday life, not because other Acts cite it
often. Renting a car or a party tent, trading in an old phone, or a renovation
contractor supplying tiles and a water heater with the work: none of these is a sale
of goods for money, and this Act is where the person receiving the goods gets the
quality and fitness terms a buyer would have.

Part 1 is short, so nearly all of it is encoded: ss 1 to 11, the definition of
"goods" and the burden rule in s 18, and the start date in s 19(2). Part 2 (services)
is marked "not applicable" in the deposit. **Not encoded:** the credit-broker limbs
of ss 4(4)(b) and 9(4)(b), terms annexed by usage (ss 4(7), 9(7)), the bailor's right
to repossess (s 7(3)), other enactments preserved by s 11(3), and the Unfair Contract
Terms Act 1977. s 11(1) makes exclusion "subject to" that Act; it is deposited
separately but was not read for this row, so what it allows is an input here.

## What the Act turns out to say

### 1. A private person can be liable on description and sample, though not on quality

s 4(2) and s 9(2) imply satisfactory quality only where the supplier acts "in the
course of a business"; s 4(1) says there is otherwise "no implied condition or
warranty about the quality or fitness". But the description condition (ss 3, 8) and
the sample conditions (ss 5, 10) contain no business requirement. So a neighbour who
swaps goods that do not match their description, or barters by sample goods with a
defect the sample did not show (s 5(2)(c)), breaches an implied condition, while the
same neighbour handing over plainly poor goods breaches none. Asserted.

### 2. The slight-breach downgrade does not reach title or the chance to compare

ss 5A and 10A let a supplier turn a breach of condition into a breach of warranty when
the recipient does not deal as consumer and the breach is so slight that rejection
would be unreasonable. They list only ss 3, 4 and 5(2)(a) and (c) (8, 9, 10(2)(a) and
(c)). The title condition (ss 2(1), 7(1)) and the condition that the recipient have "a
reasonable opportunity of comparing the bulk with the sample" (ss 5(2)(b), 10(2)(b))
are not listed, so even a business customer keeps the right to treat the contract as
repudiated for them. Asserted.

### 3. Both halves of the downgrade are for the supplier to prove

s 5A(3) puts on the supplier the burden of showing the breach is slight, and s 18(5)
the burden of showing the recipient "does not deal as consumer". A contrary intention
in the contract switches the rule off (s 5A(2)). A consumer's slight breach therefore
stays a breach of condition. Asserted.

### 4. Barter, contractors' materials and hire are in; sales, hire-purchase, deeds of gift and pledges are out

s 1(2) excepts a contract of sale of goods, a hire-purchase agreement, a gratuitous
transfer by deed and a security; s 1(3) keeps a contract in "whether or not services
are also provided" and "whatever is the nature of the consideration". s 6(1) covers
hire other than hire-purchase. That a barter or a contractor's materials falls here
rather than under the Sale of Goods Act is an inference from s 1(2)(a) and (3); the
Act does not define a contract of sale. Asserted.

### 5. A limited-title transfer carries no title condition, and a narrower encumbrance warranty

Where the contract shows the transferor is to pass "only such title as he or a third
person may have" (s 2(3)), the s 2(1) condition falls away, and the encumbrance
warranty covers only charges "known to the transferor and not known to the transferee"
(s 2(4)), not every undisclosed charge (s 2(2)(a)). Hire has no limited-title variant
(s 7). Asserted.

### 6. The usual exceptions to the quality condition, and an agent's private principal

The quality condition does not extend to defects drawn to the recipient's attention,
defects an examination the recipient made ought to have revealed, or defects a
reasonable look at the sample would have shown (ss 4(3), 9(3)). Fitness fails where
the recipient did not, or could not reasonably, rely on the supplier (ss 4(6), 9(6)). A
business agent for a private owner is treated as a business unless the recipient knew
or reasonable steps were taken to tell them (ss 4(8), 9(8)); the encoding collapses
those two into one input. Asserted.

### 7. The Act does not say what a breach of warranty gets you

Nothing in Part 1 states a remedy for breach of warranty, or states outright that
breach of condition allows rejection; s 5A(1)(a) assumes the latter. No remedy beyond
"treat the contract as repudiated" is encoded. That the general law of contract
supplies the rest is an inference.

## What would need doing before this is worth anything

- Read the Unfair Contract Terms Act 1977 (deposited separately) for "deals as
  consumer" (s 18(4)) and the limits on exclusion that s 11(1) defers to.
- Encode the credit-broker limbs and the agent's "reasonable steps" limb separately.
- Whether a given trade-in or contractor's job is a sale of goods (Sale of Goods Act)
  or a transfer under this Act is a question of characterisation the text leaves to
  case law; none was searched.
- s 19(2)'s saving for s 5 of the Civil Law Act 1909 is not encoded.
