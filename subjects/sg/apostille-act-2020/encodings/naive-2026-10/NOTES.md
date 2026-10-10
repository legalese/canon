# Apostille Act 2020 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/AA2020.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. Its legislative history lists only Act 38 of 2020; s 21 is
"Omitted as having had effect". No later amendment is annotated.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0048**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. Anyone who
brings a foreign certificate, degree or power of attorney into Singapore, or needs a
Singapore document accepted abroad, meets it.

This row takes ss 2, 6, 8-12 (foreign public documents, the bar on legalisation, the
effect of an apostille, and when one may be demanded) and ss 14-17 with the Second
Schedule (Singapore public documents, the competent authority, issuing and refusing).
Not encoded: s 5 (application), the register and verification (s 18), the Minister's
powers (ss 19, 20), and every "prescribed" matter, which needs regulations that were
not retrieved; each is an input flag.

## What the Act turns out to say

### 1. An apostille is usually optional, and sometimes may not even be demanded

s 12(1): a person proving the origin of a foreign public document "is not required to
do so by means of a Convention certificate" and is not required to comply with "any
more rigorous formality". Only for a "specified foreign public document" (a class for
which legalisation "is or may be required" before Singapore's accession, or a class that
did not exist before then) may an apostille be required, and even then nothing more
rigorous. This applies "despite any written law or rule of law to the contrary".
Asserted.

### 2. Consular legalisation of a foreign public document is not merely unnecessary but forbidden

s 9(1): legalisation "is not required, and may not be performed". The Act says nothing
about legalisation of documents from a non-Convention State, from a State in an
objection relationship with Singapore, or from a consul; for those the encoding returns
"whatever other law requires". Asserted.

### 3. The Act's definitions omit the Convention's commercial and customs exclusion

Article 1 of the Convention (First Schedule) says it does not apply to "administrative
documents dealing directly with commercial or customs operations". Neither s 6 (foreign)
nor s 14 (Singapore) repeats that exclusion. Read literally, a foreign customs
declaration from a Convention State is a foreign public document under s 6 and escapes
legalisation. That is a reading of the text, not a decided point; a court might read
the Convention back in through s 3(1). Asserted (as the literal reading).

### 4. The Convention State definition cuts both ways

s 2: a State Party is not a "Convention State" if it objected to Singapore's accession,
or if Singapore objected to its accession. Documents from either kind of State get no
benefit from Part 2. Asserted.

### 5. The apostille's presumption survives harmless defects

s 11: an attached purported apostille makes the document's origin "presumed to be
sufficiently proven". A defect (wrong form, omitted information, damage, detachment)
defeats it only "if, and to the extent that" it is proven AND it "affects the
authenticity or reliability" of the certificate. The encoding reduces "to the extent
that" to yes or no. Asserted.

### 6. Any bearer may ask, but the Academy must refuse on five fixed grounds

s 16(1): a competent authority "must issue" on request of the signer or "any bearer".
s 17(1) makes refusal mandatory if the document is not a Singapore public document,
forgery is reasonably believed, the authority is not competent, required information
is missing, or the fee is unpaid (plus prescribed grounds). Refusal is discretionary
only where the signature, seal or stamp cannot be verified (s 17(2)). The Second
Schedule names one competent authority, the Singapore Academy of Law, for "Any Singapore
public document"; that no other body is competent is an inference from the single
entry. Asserted.

## What would need doing before this is worth anything

- The Apostille Regulations (prescribed documents, private documents, fees, grounds,
  electronic apostilles) were not retrieved; every prescribed matter is a bare flag.
- Whether s 6 and s 14 really admit commercial and customs documents should be checked
  against the Parliamentary debates and any case law.
- Which States are Convention States, and which objections exist, is a matter of fact
  outside the deposit.
- The partial "to the extent that" effect in s 11(3)(d) is not modelled.
