# Factors Act 1889 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FA1889.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. No later amendment is annotated.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0036** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to. No scenario has asked a sharper
question yet.

The Act is short (14 sections), so this row takes all the operative provisions,
ss 1 to 12. It leaves out s 13 (the Act adds to an agent's common-law powers and
takes nothing away), s 14 (short title), and what "ordinary course of business",
"good faith" and "notice" mean. Those three are given facts here.

## What the Act turns out to say

### 1. An owner can lose goods to a stranger without ever agreeing to the sale

Under s 2(1), a sale, pledge or other disposition by a mercantile agent who holds the
goods or their documents with the owner's consent is "as valid as if he were expressly
authorised by the owner". It has to be made in the ordinary course of business, to a
taker who acts in good faith and has no notice that the agent lacks authority. The
owner's own instructions to the agent do not count. Asserted.

### 2. Consent is presumed, and withdrawing it does not protect the owner

s 2(4): "the consent of the owner shall be presumed in the absence of evidence to the
contrary". s 2(2): if the owner revokes consent, a disposition is still valid unless
the taker knew about the revocation. Under s 2(3), documents the agent got because it
held the goods with consent are deemed held with consent. The encoding lets that
deeming override evidence that the owner never consented to the agent holding the
documents. **That is a reading of "deemed"**, not something the text spells out.
Asserted.

### 3. A buyer let into possession can pass title over the unpaid seller's head

Under s 9, a buyer who got the goods or documents with the seller's consent can
deliver them to a good-faith taker who has no notice of the seller's lien or rights,
"with the same effect as if" the buyer were a mercantile agent in possession with the
owner's consent. Under s 8, a seller who stays in possession after a sale can likewise
pass title to a second buyer who takes delivery in good faith without notice of the
first sale. The encoding also requires a s 9 resale to be in the ordinary course of
business, because s 2(1)'s effect depends on that. **This is an inference** from the
words "same effect as if". s 9 does not say it. Asserted, under that inference.

### 4. What a pledgee gets is capped by what it gave or what the agent could claim

s 5: a pledgee who gave goods, documents or a negotiable security in exchange gets no
interest "in excess of the value" of what it gave. s 4: a pledgee taking the goods for
a debt the agent already owed gets "no further right ... than could have been enforced
by the pledgor". A fresh cash advance has no cap in the Act. The encoding returns the
amount advanced, which **is an inference**. Asserted.

### 5. The owner keeps several routes back, but only until the goods are sold or pledged

Under s 12(2), the owner can take the goods back from the agent (or the agent's trustee
in bankruptcy) before they are sold or pledged. Pledged goods can be redeemed before
sale by paying off the pledge, plus the agent's lien if the agent requires it. The
owner can also recover from the pledgee whatever is left of the sale proceeds after
its lien. Under s 12(3), the owner can sue the buyer for the unpaid price, subject to
the buyer's set-off against the agent. Under s 12(1), the agent stays liable to the
owner, civilly and criminally, for exceeding authority. The Act protects the buyer, not
the agent. Treating the balance and the price as never less than zero is an
inference. Asserted.

### 6. Endorsement always transfers a document; delivery only sometimes

s 11: a document may be transferred by endorsement. Delivery alone works only where
custom or the document's terms make it transferable by delivery, or it makes the goods
deliverable to bearer. s 10: passing on a lawfully transferred document to a taker in
good faith for value defeats a vendor's lien or right of stoppage in transit, in the
same way a bill of lading does. Asserted.

## What would need doing before this is worth anything

- The Sale of Goods Act provisions on the same ground (buyer and seller in possession,
  nemo dat) were not read. How the two Acts fit together is not encoded.
- No case law was searched. That includes the meaning of "ordinary course of business"
  and whether it applies under s 9.
- s 7(1) says the consignee "may transfer any such lien to another person". That power
  is not encoded.
- Possession through another person (s 1(2)) is encoded for mercantile agents only.
