# Third Parties (Rights Against Insurers) Act 1930 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/TPRAIA1930.txt`. The deposit says it "incorporates
all amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amendment annotated in the body is Act 27 of 2019
(Work Injury Compensation Act 2019, at s 1(6)(b)). The arrangement of sections at
the top of the deposit is out of step with the headings; the body's numbering
(1, 2, 3, 3A, 4) is followed.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0038**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet.

The Act is four pages, so the whole operative text is encoded: ss 1, 2, 3 and 3A.
Not encoded: s 4 (short title); the meaning of bankruptcy, composition, winding up
and "commencement", which come from the Insolvency, Restructuring and Dissolution
Act 2018 (not read); the content of s 28 of the Work Injury Compensation Act 2019
(taken as a flag); and the policy's own terms, which the insurer can still raise.

## What the Act turns out to say

### 1. If the person who hurt you goes bust, you step into their insurance claim

s 1(1): when an insured who is covered against liabilities to third parties becomes
bankrupt, makes a composition with creditors or (for a company) is wound up, put
into receivership or has floating-charge holders take possession, the insured's
rights against the insurer "shall ... be transferred to and vest in the third
party". The effect (an inference; the Act does not say it in these words) is that
the insurance money goes to the injured person rather than into the insolvent
estate for all creditors to share. It does not matter whether the liability arose
"before or after that event". Asserted.

### 2. You get the lesser of the two amounts, and keep a claim for the rest

s 1(4): the insurer is under "the same liability to the third party as he would
have been under to the insured". If the policy is worth more than the claim, the
insured keeps the excess against the insurer; if it is worth less, the third party
still has the balance against the (insolvent) insured. A policy worth $50,000
against an $80,000 claim gives $50,000 from the insurer and $30,000 left against
the insured. Asserted.

### 3. A late settlement with the insured is disregarded, but only for bankruptcy and winding up

s 3 stops an insurer and an insolvent insured from settling the claim between
themselves, and makes a waiver, assignment, disposition or payment to the insured
ineffective against the third party, **only where the insured has become bankrupt
or a company has a winding-up order or voluntary winding-up resolution**. A
composition, a receivership, possession under a floating charge and a s 419 order
on a deceased debtor's estate are not named, although all of them trigger the
transfer in s 1. Read literally, "after liability has been incurred" qualifies only
the agreement; a payment to the insured after the commencement is caught even if
made before the liability arose. Asserted (literal reading).

### 4. Policy terms that cancel cover on insolvency are void; ordinary terms are not touched

s 1(3) makes a policy "of no effect" in so far as it avoids the contract or alters
the parties' rights on the insolvency events. s 2(1) does the same for a term
triggered by giving information to a claimant, or prohibiting it. Nothing in the
Act strikes down an ordinary exclusion or a claims-notice condition; that they
survive is an inference from that silence and from s 1(4). Asserted.

### 5. The claimant is entitled to be told about the insurance, but the duty has no penalty

s 2(1): the bankrupt, debtor, company, personal representative, trustee, liquidator,
receiver or person in possession must, on the request of anyone claiming the
insured is liable to them, give the information reasonably required to find out
whether rights have passed and to enforce them. s 2(2): the **insurer** comes under
the same duty only once information already given points to it. s 2(3): the duty
includes letting the claimant inspect and copy contracts of insurance, premium
receipts and other documents in the person's possession or power. The Act sets no
penalty and no deadline. A broker is not named (encoded as not under the duty).
Asserted.

### 6. Exclusions: reconstruction, reinsurance and workplace injury

s 1(6)(a): no transfer where a company is wound up voluntarily "merely for the
purposes of reconstruction or of amalgamation". s 1(5): a liability "in the capacity
of insurer under some other contract of insurance" is not a liability to third
parties, so a reinsurance claim does not pass. s 1(6)(b): cases under s 28(1) to (3)
of the Work Injury Compensation Act 2019 are excluded. s 3A extends everything said
of companies to limited liability partnerships. Asserted.

### 7. It is an English Act of 1930, applied here since 1993

The Legislative History records the Act as 20 & 21 Geo. V, c. 25, commenced
10 July 1930, applied in Singapore from 12 November 1993 by the Application of
English Law Act 1993 (without the amendments made by the English Insolvency Acts
1985 and 1986). The date under the long title is 12 November 1993. Not asserted.

## What would need doing before this is worth anything

- Para (a) of s 1(1) ("becoming bankrupt or making a composition") is encoded
  literally for every kind of insured; whether a company can meet it, and which
  Singapore procedures count as a "composition or arrangement", needs the
  Insolvency, Restructuring and Dissolution Act 2018.
- Restricting the s 419 order to individuals is an inference from "deceased debtor".
- No case law was read; in particular, how far the insurer may raise the policy's
  conditions against the third party, and the literal reading of s 3, are untested.
- The interaction with motor insurance legislation was not looked at.
