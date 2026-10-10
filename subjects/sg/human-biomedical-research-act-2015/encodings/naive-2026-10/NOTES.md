# Human Biomedical Research Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021,
in operation 31 December 2021), informal consolidation, version in force from
5/12/2025, deposited at `../../registers/source-bundle/HBRA2015.txt`. The latest
amendment in its legislative history is Act 19 of 2025 (Statutes (Miscellaneous
Amendments) Act 2025), commencement 5 December 2025.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0025** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The row takes what a research subject, tissue donor, family member, researcher or
tissue dealer meets: what counts as human biomedical research and as human tissue
(ss 2, 3, First and Second Schedules), who consents for a minor, an adult lacking
capacity or a dead person (ss 7(1)(b), 8, 11(1), 13(2)), withdrawal (s 14), the
deception defence (s 26(2)), paying for tissue (ss 32, 33), removal and reuse of
tissue (s 37(2), (3), (9)) and the maximum penalties (ss 22(6), 26 to 33, 37 to 39,
50). Not encoded: administration, institutional review boards beyond s 13(2),
research institutions' and tissue banks' duties (ss 23, 24, 34 to 36), codes of
practice, enforcement, appeals, the Fifth Schedule waivers, minors lacking capacity
(s 8(1)(d)), tissue from minors (s 10), the consent formalities (s 6) and the
information list (s 12).

## What the Act turns out to say

### 1. Drug trials are not "human biomedical research" under this Act

The Second Schedule (items 6 and 7, the latter added by S 334/2019) excludes
"Clinical trials of health products conducted in accordance with the Health Products
Act 2007" and of medicinal products under the Medicines Act 1975. So does item 4, the
National Registry of Diseases. A hospital study of diabetes using patient records is
caught (s 3(2)(a) with (f)); a drug trial on the same patients is not. Asserted.

### 2. Research needs a link to the body, not just a health topic

s 3(2) catches research on disease, aesthetics or performance only "where the
research involves" an intervention, identifiable biological material or identifiable
health information. An anonymous prevalence survey with none of these is outside the
definition (this follows from the words; no example in the text says so). Any research
on human gametes or embryos is caught regardless (s 3(3)(a)). Asserted.

### 3. Spit, urine, cut hair and nail clippings are not "human tissue"

The First Schedule removes them from "human tissue", along with non-identifiable
material "substantially manipulated" — but freezing, cutting, centrifugation and the
other methods in paragraph 4(2) do not count as manipulation. Blood and a plucked hair
with its follicle remain tissue. Asserted.

### 4. Selling tissue is a $100,000 offence, but a donor may be made whole

s 32(1) makes a contract for the sale of human tissue void, and (2), (3) make entering
into, paying, receiving or offering an offence: $100,000 or 10 years. s 33 does the
same for advertising tissue for sale in Singapore. Not caught (s 32(4)): reimbursing a
living donor's travel, accommodation, domestic help, child care and loss of earnings;
storage and quality-control costs; and Government medical-benefit schemes for donors.
Asserted.

### 5. The family ladders differ between the incapacitated and the dead

For an adult lacking capacity with no authorised donee or deputy (s 7(1)(b)): spouse,
adult child, parent or guardian, adult sibling, then "any other person named by the
adult". For the dead (s 11(1)): the same four, then the executor or administrator,
then whoever must dispose of the body — and the person the adult named is not on that
list. In both, actual notice of the person's contrary indication or of opposition by
the same or a prior class blocks consent. Asserted.

### 6. A minor's consent needs a parent too, unless the board waives it

s 2: anyone under 21 who has never married is a minor; a married 19-year-old is an
adult. A minor who understands must consent together with one adult parent or guardian
(s 8(1)(a)), unless an IRB waives the parent under s 13(2) — the text's examples are
"neglected or abused minors" and adolescents in studies of sexually transmitted disease
treatment. A minor who does not understand may be enrolled on a parent's consent only
where the research cannot be done without that class of minors. Asserted.

### 7. Tissue consent can be withdrawn only while it still means something

A research subject may withdraw "at any time" (s 14(1)). A tissue donor may withdraw
only if the tissue is identifiable and either unused or practicably withdrawable
(s 14(2)); data already obtained may be kept (s 14(3)); any penalty for withdrawing is
void (s 14(4)). Asserted.

### 8. Companies face double fines; deceivers need all three defences

s 50 doubles the maximum fine for a body corporate ($200,000 for tissue trading).
Deceiving someone into research (s 26(1)(c)) is defended only if the deception was
necessary, its possibility disclosed, and the approved proposal followed (s 26(2)).
Leftover clinical tissue cannot go to research until the treating doctor no longer
needs it (s 37(9)). Asserted.

## What would need doing before this is worth anything

- The Human Biomedical Research Regulations (prescribed witnesses, matters for
  substitute consent, further waiver circumstances) were not retrieved; several
  provisions turn on "as may be prescribed".
- The Fifth Schedule waivers and the Third and Fourth Schedule research categories are
  quoted only through their penalties, not modelled.
- s 32(6) carves out organs, blood, eggs, sperm and embryos to other Acts; not modelled.
- No case law or MOH guidance was searched.
