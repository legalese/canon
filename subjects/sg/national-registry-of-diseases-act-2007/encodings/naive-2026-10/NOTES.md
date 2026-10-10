# National Registry of Diseases Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text, one pass. The `writing-l4-rules`
skill could not be loaded in this session, so the conventions of the finished naive
rows (coroners-act-2010, stamp-duties-act-1929) were followed instead. No pipeline, no
coverage table, no independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/NRDA2007.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021"; later amendments are annotated in the
text, the latest Act 19 of 2025 (in force 5 December 2025), which rewrote the s 2
definition of "healthcare institution" around the Healthcare Services Act 2020. The
deposit's metadata says "Current version as at 03 Oct 2026".

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0027** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. A patient meets this Act on a diagnosis of cancer, kidney failure or a
heart attack; a clinic, hospital or laboratory meets it through its manager's duty to
notify.

This row takes the Schedule of reportable diseases, the s 2 definition of healthcare
institution, the manager's duties (ss 6, 7), confidentiality (ss 5(2), 8), the four
routes out of the Registry (ss 9-12), the protection of notifiers (s 17(2)), the
offence maxima and composition (s 20). Not encoded: appointments (s 3), functions
(s 4), investigation powers (ss 13-15) beyond the obstruction offence, officers of
bodies corporate (s 16), protection of officials (s 17(1), (3)), jurisdiction (s 19),
exemptions (s 21), amendment of the Schedule (s 22), the regulation-making list (s 23)
and the saving provision (s 24). The form and time limit for notification are
"prescribed" and the regulations were not retrieved, so no deadline is encoded.

## What the Act turns out to say

### 1. A patient's consent is never asked for notification, and not always for disclosure

s 6(1) puts the duty on the manager of the healthcare institution: where a person is
diagnosed with or treated for a reportable disease there, the manager "must ... notify
the Registrar". Nothing in the Act asks the patient, and there is no opt-out in the
text. Disclosure of identifiable information to a treating doctor (s 11) or a
researcher (s 12) needs the "requisite consent"; disclosure to a national public
health programme (s 10) does not — it needs only the Director-General's approval, and
the Director-General must be satisfied the programme "cannot be carried out with
anonymised information" (s 10(3)). Asserted.

### 2. A living organ donor is on a disease register

The Schedule lists "Single Kidney — Post Nephrectomy (Donor)" and "Liver — Post
Hepatic Resection (Donor)" alongside cancer, chronic kidney failure and acute
myocardial infarction. A donor's hospital must notify as it would for a cancer
patient. Benign tumours are reportable only "of the brain and other parts of the
central nervous system" (including the pituitary); a benign skin tumour is not. Stroke
and diabetes are not in the Schedule. Asserted.

### 3. The registers are closed, and Registry staff cannot be made to testify

s 5(2): the registers "must not be open for inspection by the public". s 8(1): Registry
staff are "not compellable in any proceedings" to give identifiable evidence "Except in
the case of a prosecution for an offence under this Act" — so not in a murder trial,
a negligence claim or a divorce. Unauthorised disclosure by staff carries $10,000 or
12 months (s 8(3)). The Act gives a patient no right of access to their own entry;
s 23(2)(d) only lets regulations provide for "certified extracts". Asserted (the
compellability rule; the access point is not encoded).

### 4. Anyone may buy anonymised data; the Director-General simply gets it

s 9(1): the Registrar "may", on a request by any person, on payment of the prescribed
fee and subject to conditions, disclose anonymised information, and "must" on a
request by the Director-General. Breach of a condition is an offence ($5,000 or
6 months). Asserted.

### 5. A clinic's failure to notify is a $2,000 fine; the notifier is shielded from confidence claims

s 6(2), s 7(3): failure without reasonable excuse, or knowingly false information, is
a fine not exceeding $2,000, with no imprisonment; the Registrar's certificate that a
notification was not made is prima facie evidence (ss 6(3), 7(4)). s 17(2): whoever
notifies or supplies information to comply with the Act is not liable "for breach of
confidence" and is not in breach of professional ethics — and unlike s 17(1) and (3),
this subsection says nothing about good faith. Asserted.

### 6. The composition cap never bites below half the fine

s 20(1): the Director-General may compound a prescribed offence for "the lower of"
half the maximum fine and $5,000. The highest fine in the Act (and the ceiling for
regulation offences under s 23(3)) is $10,000, so half of it is exactly $5,000; for
every offence in the Act the half-fine figure governs (inference from the figures
read; no compoundable offences regulations were retrieved). Asserted for four
offences.

### 7. A deletion annotation sits awkwardly in s 2

The definition of "authorised Registry officer" is printed followed by "[Deleted by
Act 11 of 2023 wef 01/05/2023]", yet s 7 still uses the term. Whether the annotation
belongs to that definition or to a removed one beside it cannot be told from the
deposit. Not asserted.

## What would need doing before this is worth anything

- The notification regulations (form, time limit, and the case definitions of chronic
  kidney failure and acute myocardial infarction) were not retrieved.
- The Healthcare Services Act 2020 was not read; that nursing homes and home
  healthcare are licensable services outside the s 2 list is an inference.
- No Gazette orders under s 2(b), s 21 or s 24 were searched, and no case law.
- The investigation powers (ss 13-15), including inspection of medical records
  "even if the prior consent of the person has not been obtained" (s 14(1)(b)(ii)), are
  not encoded.
