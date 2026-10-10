# Application of English Law Act 1993 — naive encoding

**Method: naive.** Written straight from the deposited text following the
`writing-l4-rules` conventions of the example rows, and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/AELA1993.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31 December 2021.
The latest amendment annotated in the text is [4/2021].

**Checks:** one case file (`aela-cases-english-law.l4`), 50 assertions satisfied, 0 errors,
0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0043**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or business it
applies to. No scenario has asked a sharper question yet. For this Act the answer is which
English contract and commercial statutes bind them, and to what extent.

The row encodes s 3 (common law and equity), s 4(1)–(4) with Parts 1 and 2 of the First
Schedule (which English statutes apply, and which sections of them), s 5(1) (no other English
statute applies), and s 6(2) (the old Civil Law Act s 5 survives for old claims). It also
encodes four rules the Second Schedule wrote into other Acts in 1993: Civil Law Act s 6A,
Conveyancing and Law of Property Act s 18A, and Insurance Act ss 61A and 61B.

Not encoded: s 5(2), ss 6(1), (3), 7, 8, 9, the textual amendments in First Schedule Part 3,
and the Second Schedule's other insertions (voluntary waste, trusts of land in writing, chain
of executorship, accumulations, the co-owner's account, conveyances to defraud creditors or
purchasers, the Extradition Act amendment, and piracy in the Penal Code).

## What the Act turns out to say

### 1. Singapore runs on the 1993 snapshot of the English commercial statutes

s 4(2): the Part 2 enactments are "as they are in force as at 12 November 1993". The Sale of
Goods Act 1979, the Unfair Contract Terms Act 1977, the Misrepresentation Act 1967 and the rest
apply in their 1993 form, so a later UK amendment does not reach Singapore. s 4(2) says nothing
about Part 1, so for a Part 1 statute the encoding's handling of later UK text is a default and
is not tested. Asserted (Part 2).

### 2. The extents leave out exact sections

The fourth column applies only ss 3 and 5 of the Mercantile Law Amendment Act 1856. It leaves out
Sale of Goods Act ss 22 and 25(2), Part II of the Supply of Goods and Services Act 1982, and
Minors' Contracts Act ss 1(b) and 4(1). For the Unfair Contract Terms Act it applies only Part I
(without s 1(1)(c), (3)(b) and the 1984 amendment to s 1) and Part III. It also leaves out named
earlier UK amendments: the Consumer Credit Act 1974 change to Factors Act s 9, and the Insolvency
Acts 1985 and 1986 changes to the Third Parties (Rights against Insurers) Act 1930. Asserted.

### 3. Every other English statute is out, unless a written law brings it in

s 5(1): "Except as provided in this Act, no English enactment is part of the law of Singapore."
The way back in is s 4(1)(b): an English enactment that applies "by virtue of any written law".
The Statute of Frauds 1677 is not listed, but the Second Schedule re-enacted its core as Civil
Law Act s 6A. Asserted.

### 4. Old contract law hides in other Acts: a literal reading catches short tenancies

s 6A (as inserted) bars an action on a guarantee, a contract about land "or any interest in such
property", or an agreement not to be performed within a year, unless there is a signed note in
writing. Read literally, a six-month tenancy is a disposition of an interest in immovable
property, so it is caught. The 1993 text has no short-lease exception. Whether the courts or a
later amendment read it that way was not checked. Asserted on the literal reading.

### 5. Relief against forfeiture has a floor of four weeks

CLPA s 18A (as inserted): a lessee sued for forfeiture for unpaid rent ends the action by paying
the arrears and costs into court within the time for acknowledging service. That route is closed
if the lessor also sues on another ground or claim (s 18A(6)). Otherwise the possession order must
give "not ... less than 4 weeks", and payment within that period, or the period as extended, saves
the lease. One oddity: s 18A(5) is "Subject to subsection (6)", but (6) disapplies only (2). The
encoding lets (5) operate in every case. Asserted.

### 6. Insurance needs an interest, and an accidental fire is no one's fault

Insurance Act s 61A (as inserted): insurance on an event in which the beneficiary has no interest,
or by way of wagering, is void. Recovery is capped at the value of the interest. None of this
"extend[s] to" insurance on ships or goods or to indemnity contracts. s 61B: no action lies against
the person on whose premises a fire "accidentally began", but landlord–tenant contracts are not
defeated. Asserted.

### 7. Old claims keep the old reception rule

s 6(2): for proceedings begun, or a cause of action accrued, before 12 November 1993, the repealed
Civil Law Act s 5 still applies. Asserted.

An observation about this repository, not about the Act: the Part 2 statutes appear here as
Singapore subjects of their own (for example `subjects/sg/sale-of-goods-act-1979`,
`unfair-contract-terms-act-1977`, `factors-act-1889`, `partnership-act-1890`). This row does not
check those deposits against the extents above.

## What would need doing before this is worth anything

- Read the present text of Civil Law Act s 6A, CLPA s 18A and Insurance Act ss 61A and 61B. This
  row encodes them as inserted in 1993, and they may have been renumbered or amended since.
- Look for any modification order under s 8. None was retrieved.
- Find out what s 3 means in practice: whether an English decision after 1993 is "part of the law
  of Singapore immediately before" that date is a question for case law, which was not searched.
- Check how s 6A deals with short tenancies (finding 4) against case law and the current Civil
  Law Act.
- Section-level questions about the listed statutes need their Part and section structure. The
  encoding takes the Part as an input and does not check it.
