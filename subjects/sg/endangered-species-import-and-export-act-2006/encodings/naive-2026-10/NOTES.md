# Endangered Species (Import and Export) Act 2006 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/ESIEA2006.txt`. The cover says "version in force from
1/7/2026". The Revised Edition takes in amendments to 1 December 2021. The latest
amendment annotated in the body is Act 15 of 2026 (wef 1 July 2026: hybrid plants
and s 8A), and in the Schedule it is S 88/2026 (wef 5 March 2026).

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**Requirement REQ-0081** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked
a sharper question yet.

This row covers what a traveller, pet or plant owner, trader or carrier runs into:
what counts as a scheduled species (s 2), transit (s 2A), the offences and penalties
(ss 4, 5, 5A), the due-diligence defence (s 6), mandatory refusal and cancellation of
permits (ss 7(4), 8), which seized conveyances can be forfeited (s 15), the
repatriation window (s 15D), recovery of expenses (s 15E(2)), the general penalty
(s 18) and composition (s 25).

Not encoded:
- the Schedule itself. It holds the CITES Appendices, about 4,200 lines of the
  extracted text, so an item's Appendix is taken as a fact;
- s 2(2), which says which Appendix a hybrid counts as being in;
- certification (s 8A);
- the investigation, search, seizure and arrest powers (ss 9 to 14);
- forfeiture procedure (ss 15A to 15C);
- who bears the expenses (s 15E(1));
- corporate attribution (ss 20, 20A), beyond the s 5A(2) penalties;
- exemptions, service and rules (ss 26, 27, 29).

## What the Act turns out to say

### 1. Possessing a protected species is not an offence in itself. Selling a Gazette-notified one is, however it arrived

s 4(1)(b) makes possession an offence only for a scheduled species "imported, or
introduced from the sea, without a valid permit". s 4(1)(c) makes it an offence to
sell, advertise or display a species "specified by the Minister by notification in
the Gazette", with no condition about how it got here. So owning a lawfully imported
listed parrot is not an offence. Advertising a Gazette-notified species is an offence
even if it came in with a permit. Asserted.

### 2. Fines are counted per specimen, and the cap rises with market value

s 4(2): for an individual, the maximum fine is $100,000 for each Appendix I specimen,
or $50,000 for each Appendix II or III specimen. The total may not exceed "$500,000
... or the market value ... of all the specimens ..., whichever is higher". The
imprisonment maximums are 6 years (Appendix I) and 4 years (Appendix II or III). For a
corporation, association or partnership (s 5A(1)) the figures double to $200,000 and
$100,000, with a cap of "$1 million" or the market value, and there is no
imprisonment. Under s 5A(2), an officer or partner liable for the same offence faces
up to 8 years (Appendix I) or 6 years. Ten Appendix I specimens worth $800,000 give a
maximum of $800,000 for an individual, not $500,000. The encoding reads the
provision as per-specimen sum, capped at the higher of the fixed sum and the market
value. That reading is not tested against a sentencing case. Asserted.

### 3. Hybrids are caught, with different rules for animals and plants

As amended by Act 15 of 2026 (wef 1 July 2026), a hybrid animal is a scheduled species
if an Appendix I or II animal is in its "recent lineage", defined as the 4 preceding
generations. An Appendix III ancestor does not count, and neither does a listed
ancestor five generations back. A hybrid plant is caught if it "is derived from one or
more plants specified in the Schedule", with no generation limit stated. Naturally
excreted urine, faeces and ambergris are excluded from "readily recognisable part or
derivative". Asserted.

### 4. A late CITES document can never cover an Appendix I species

s 5(3)(a) and s 7(4)(a): an export document issued after the export is valid only
for an Appendix II or III species, and only where the exporter, re-exporter or
importer did not cause or contribute to the late issue. For an Appendix I species the
Director-General "must refuse" the permit. An altered document is valid only if the
alteration is both sealed or stamped AND authenticated by signature. Asserted.

### 5. Transit is narrow, and the clock is 14 days

s 2A: a species is in transit "only if" its document is issued no later than 14 days
after arrival and names a destination outside Singapore. In addition, the species must
stay on the conveyance, be transferred directly under official control, or be held
under control for no more than 14 days unless the Director-General approves longer.
Outside transit, bringing the species in is an "import" that needs a permit. In
transit, s 5 requires the exporting country's CITES document and, where the
destination requires one, its import document. Asserted.

### 6. The defence is the defendant's to prove, and blaming someone else needs 7 clear days' notice

s 6: the person charged must prove both a cause beyond their control and "all
reasonable precautions and ... all due diligence". If the defence blames another
person, notice identifying that person must be served on the prosecutor at least 7
clear days before the hearing. Otherwise the defence needs the court's permission.
Asserted.

### 7. Carriers' exposure: large ships and scheduled services keep their conveyances

s 15: a seized conveyance of more than 200 tons net, or an aircraft or train on a
regular passenger service, is not liable to forfeiture. Under s 15D, the owner of the
conveyance can be directed to repatriate a forfeited species at their own expense. The
direction binds only if made within 12 months after arrival or within 6 months after
proceedings conclude or the offence is compounded, "whichever is the later". Failing
to comply carries a fine of up to $10,000 or 12 months. Treating pending proceedings as
keeping the window open is an inference, and no case asserts it. Asserted otherwise.

### 8. Composition is capped at $5,000; expenses are collected like a fine

s 25: only a prescribed compoundable offence may be compounded, for at most $5,000.
Seized items other than a conveyance remain liable to forfeiture after composition.
s 15E(2): seizure and care expenses not paid within 14 days after demand are
recoverable "as if it were a fine". Asserted.

## What would need doing before this is worth anything

- The Schedule was not encoded, and neither was any Gazette notification under
  s 4(1)(c). So the encoding cannot say whether a given animal or plant is listed, or
  which Appendix it is in.
- The rules under s 29 (permit terms, fees, levies, prescribed transit documents,
  compoundable offences) were not retrieved.
- The reading of the per-specimen cap in s 4(2) and s 5A has not been checked against
  sentencing decisions.
- s 2(2) (which Appendix a hybrid falls in), s 8A and the corporate provisions are
  left out.
