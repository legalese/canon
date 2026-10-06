# What encoding Vietnamese insurance documents found: policy defects and counterintuitive scenarios

Status: draft, written 2026-10-07 by the lead of the `vn-insurance` session (Claude Sonnet 5.5) from the 24 deposited encodings (VN-01 to VN-26 except VN-12 and VN-16, which were still being finished).
Every encoding it draws on is itself a draft: no Vietnamese-qualified lawyer has read any of them against its source, and no independent second encoding has been run.
The findings are the encoders' own, reported in each row's `NOTES.md` section 4 and demonstrated, where they are, by an `#ASSERT` or `#TRACE` in the row's tests.
The 594 records behind this report were extracted from those notes by four Opus agents (`analysis/vn-insurance-findings/records-*.md`); the lead did not re-read all 594 against the sources.

## 1. What was done

26 documents were chosen, encoded in L4 by independent single-agent encoders working in parallel, and each encoder was asked to record, in a findings section, every place where the wording does something a reasonable reader would not expect.
The documents are 22 policy wordings from twelve insurers (motor damage, health, personal accident, travel, life, unit-linked and group-linked life, critical illness, home, property, fire, engineering, construction, liability), three Tasco Insurance wordings, and Decree 67/2023/NĐ-CP on compulsory motor third-party liability insurance.
Encoders did not see each other's work, so a defect that turns up in several rows was found several times independently.
The exceptions to that blindness are listed in section 8.

## 2. The numbers

594 findings in 24 rows, between 16 and 49 per row (median 24).
By line of business: motor and the motor decree 139 (6 rows), health, accident and travel 157 (5 rows), life 146 (6 rows), property, liability and engineering 152 (7 rows).

How firm the encoder says the finding is (its own label, copied by the extraction):

| standing | records | meaning |
| --- | --- | --- |
| LITERAL | 399 (67%) | follows the words as written; the encoder lists no reasonable alternative |
| CONTESTED | 141 (24%) | the encoder names a reasonable alternative reading and says which it took |
| LAW | 48 (8%) | the wording conflicts with a statute (mostly the Law on Insurance Business 08/2022/QH15) |
| unlabelled | 6 (1%) | English-and-Vietnamese differences in one policy that change no answer |

Whose money the defect moves, on the literal reading: against the claimant 367 (62%); unclear 165 (28%); against the insurer 34 (6%); no money 28 (5%).
Treat the 62% with care: the encoders read insurer-drafted text literally, and a literal reading of text drafted by one party tends to find the other party's losses.
The 34 against the insurer are real and of a different kind: they are the places where the insurer pays more than it can have meant (the "leakage" class, section 5.4).

The class of defect, as assigned by the extraction agents (primary class; a record can carry a second):

| class | records | what it is |
| --- | --- | --- |
| T7 internal inconsistency | 107 | two clauses, two products or two parts of one document answer the same case differently |
| T5 undefined or ambiguous term that decides outcomes | 87 | the word that carries the outcome is not defined |
| T6 illusory or self-defeating cover | 68 | cover granted, then taken back; an add-on that cannot pay |
| T1 clocks and deadlines | 61 | two clocks for one act; a bar that runs before the right arises; a clock with no start |
| T13 other | 58 | mostly "silent consequence" (a duty with no stated sanction, 24) and "no rule for the case" (7) |
| T11 insurer discretion or control | 42 | a range or a valuation with no criteria; the insurer controls when its own clock starts |
| T2 exclusion with no causal link, or overbroad | 40 | |
| T4 payout arithmetic | 39 | double deduction, no floor, order of operations, an excluded event paying more than a covered one |
| T12 forfeiture by notice or condition precedent | 23 | |
| T9 English and Vietnamese texts disagree | 21 (+6 unlabelled) | all in the one bilingual policy, Pacific Cross travel |
| T3 contract worse than the statute | 20 | |
| T8 published document is incomplete | 16 | an annex or table that the published file does not contain |
| T10 waiting period against term | 6 | |

Counting any mention of a class, not only the primary one: T1 or T4 (clock or arithmetic) appears in 168 records (28%); T6 or T7 (illusory cover or inconsistency) in 261 (44%).

Roughly 70% of the records cite an `#ASSERT` or `#TRACE` that demonstrates the scenario; the other 30% (about 175 by a crude text match on the evidence line) are marked by the encoder as reading-only, or rest on a table or a side-by-side comparison.

## 3. Eight lessons

### 3.1 Most defects are interactions, not typos

The defects that matter appear only when two clauses meet on one concrete set of facts.
T7 (inconsistency) is the largest class, T5 and T6 follow, and the typical record has the form "clause A grants X, clause B takes X back, so the customer gets Y".
A reader of any one clause sees nothing wrong.
What found them was writing a test scenario with real numbers and running it through both clauses, which is what an encoding forces.

### 3.2 The commonest structural failure is cover granted and then removed

A product line sells the cover and an exclusion, a definition or a condition empties it.
Examples (all on the literal reading): a home policy whose definition of the Home is a house or apartment and whose exclusion (c) removes houses and apartments (VN-05); a personal-liability cover that excludes "intentional or negligent" acts, which is most of what liability cover is for (VN-05); a travel policy that excludes 22 named diseases "whether occurring prior to or during" the trip, so a heart attack first striking abroad is excluded from every section, evacuation included (VN-06); a "riot" cover that one clause gives back and another excludes (VN-07, VN-20); an "all risks" policy that excludes damage of unknown cause (VN-08); a parts-theft add-on that allows zero claims on a contract under twelve months (VN-17); a battery add-on that replaces a 0.5m deductible with a 21m one for a battery the base cover already pays (VN-18).

### 3.3 The insured's clocks are short and forfeiting; the insurer's are unbounded; and bars can expire before the right exists

Across 12 rows from 9 insurers or sources, nothing binds the insurer to pay or decide by any date, or its clock starts only on a "complete and valid file" that the document does not define.
The insured's side is the opposite: strict notice, short bars, forfeiture on a miss, often stricter than the statute.
Worse, the two sets of clocks meet.
Notice is due within 120 days of discharge or death, but documents are barred one year after the event, so a death after day 245 cannot be claimed if the whole notice period is used (VN-19 X18).
A claim file is due 180 days after the last treatment, but permanent disablement qualifies only after 104 weeks (VN-03 X19: due 6 September 2026 for a disablement that qualifies on 2 March 2028).
A 12-month claim bar runs from the first symptoms of a cancer, so the claim can be barred before the diagnosis (VN-25 FD7); the same shape recurs in VN-24 X18, VN-26 F-08, VN-21 F1, VN-07 F3, VN-06 F-PA-NOTICE and VN-05 X-claim-time.
A grace period that restarts at every monthly deduction never ends (VN-13 finding 3).

### 3.4 Payout arithmetic breaks at the edges, and the breaks are not rare

- A formula with no floor can go negative: sum insured 1bn, advances 900m, debts 250m gives -100m, and the document does not say what is paid (VN-24 X3; the same shape in VN-11, VN-14, VN-25).
- A deduction is taken twice, so a premium debt of 2m is subtracted from a death benefit twice and 757.3m becomes the figure (VN-13, VN-14, VN-25).
- An excluded event pays more than a covered one: a death in war pays 600m, a covered death 475m (VN-25 FD5); an excluded suicide refunds 148m while a covered accidental death pays 100m (VN-14 X2); itemised fingers pay 350m, the whole hand 250m (VN-26 F-04).
- Thresholds are cliffs: overloading by 49.99% halves a payout, by exactly 50% costs nothing, by 50.01% loses everything (VN-02 V5); a first premium of 99m buys a 100m benefit and 100.5m buys a refund of 98.5m (VN-25 FD9).
- Two proportional cuts compound: two 250m policies on a 500m car that the Law treats as exactly insured pay 6m of a 14m loss (VN-02 V27, VN-01 X4, VN-15 X22).
- A statutory table can be internally non-monotone: Decree 67/2023 Annex I prices a 16-seat business vehicle at 3,054,000 and a 17-seat one at 2,718,000 (VN-10 R5; the lead checked this against the gazette text, source lines 2081-2082 of `nd67-congbao-1017-1018.txt`).

### 3.5 The statute catches a pattern: the same eight clauses conflict with Law 08/2022/QH15 in many rows

The 48 LAW records fall into a few families that recur: the insurer may cancel without cause on a few days' notice; no deadline for the insurer to pay; innocent misstatement voiding the contract or the property; notice bars stricter than the statute; double insurance applied where the sums do not exceed the value; a discovery rule given to the (possibly dead) policyholder only; refund rules on avoidance; a subrogation clause where the Law forbids it.
These are the clauses an insurer's compliance team would most want listed, because they are the ones a regulator or a court is likely to override.
The mechanism that surfaces them is a fork register in each encoding that records where the Law and the wording part, and which the encoder followed.

### 3.6 The same words are read two ways

Two Bảo Minh forms carry the identical phrase "thời hạn thanh toán phí bảo hiểm dưới 30 ngày"; the VN-08 encoder read it as a drafting slip and the VN-20 encoder read it literally (VN-08 F4, VN-20 X17).
The Pacific Cross travel policy has an English text and a Vietnamese text: 27 differences between them, about 17 of which change an answer, and a further 22 defects present in both (VN-06).
Examples: a non-paying passenger in a private plane is excluded in English and covered in Vietnamese; a street riot is covered in English and excluded in Vietnamese; neither text says which prevails.
Any reasoning system over such wording has to carry its reading choices explicitly and show them to the reader.

### 3.7 Published documents are often incomplete

The injury and surgery tables are not in the published 19-page Tasco health file (VN-19 X2), three appendices are missing from the PTI file (VN-03), and the benefits annex is not in the PVI mirror copy (VN-04).
In each case the encoder had to make the missing table an input, and the encoding refuses (`REFUSE`) when the caller supplies none.
A customer reading the same published document cannot work out what is payable either.

### 3.8 Independent replication is the strongest signal in the set

Four of the five motor physical-damage wordings (Bảo Việt, UIC, OPES, Tasco voluntary) independently report that some exclusions ask for no causal link between the circumstance and the loss: hail damage to a parked car excluded because its inspection certificate lapsed (VN-01 X2), a car parked where prohibited that burns from an electrical fault excluded (VN-17 X-07).
The Bảo Minh siblings (installation and construction all risks, VN-21 and VN-22) share most of their defects one-to-one, which says they share a template.
Whether the market shares a template is a hypothesis these records support and do not prove.

## 4. Recurring clusters, by how many insurers show them

Row numbers are the rows whose findings contain the pattern, assembled by the extraction agents from their cross-matching and, where noted, confirmed by a keyword search over the records.

| pattern | rows | insurers or sources |
| --- | --- | --- |
| exclusion or condition with no causal link; any breach defeats the claim | 01, 02, 15, 17 (motor); 05, 08, 09, 20, 21, 22 (conditions precedent) | 7 |
| no outside date for the insurer's own payment or decision, or its clock starts on an undefined "complete file" | 12 rows by keyword (03, 23, 11, 13, 24, 17, 10, 05, 07, 08, 09, 20); 16 rows by the agents' cross-match | 9 |
| insurer may cancel without cause on a few days' notice | 05, 07, 08, 09, 20 (and 03: guaranteed renewal undone by a cancel-for-any-reason clause) | 5 |
| innocent misstatement or omission voids cover or takes property out of it (against Law art 22(2)) | 07, 08, 20, 21, 22, 13, 14, 25 | 4 |
| a time bar that runs out before the right arises | 03, 05, 06, 07, 19, 21, 23, 24, 25, 26 | 7 |
| a formula with no floor | 11, 14, 24, 25 | 2 |
| a deduction taken twice | 13, 14, 25 | 2 |
| double insurance applied where sums do not exceed the value (Law art 49(1)) | 01, 02, 15 (and 21's other-insurance clause) | 4 |
| an excluded or worse event pays more than a covered or better one | 01, 02, 14, 15, 18, 24, 25, 26 | 6 |
| threshold cliffs (a payout that jumps at a boundary) | 02, 10, 13, 15, 17, 18, 19, 24, 25 | 7 |
| an add-on that cannot pay, or pays less than the base cover | 15, 17, 18 | 3 |
| riot, war or terrorism wording gaps | 05, 06, 07, 08, 20, 21, 22, 26 | 5 |
| discretion with no criteria (a reduction band, a valuation, a part-or-all refund) | present in all 24 rows (41 records mention it by keyword) | 14 |

## 5. A gallery of counterintuitive scenarios

Each is a record in `analysis/vn-insurance-findings/`; the numbers are the encoders' fixtures, reported as they are.
"Literal reading" means the encoder says the wording reads that way; where a row marks it CONTESTED, the alternative reading is in the record.

### 5.1 Motor

- **A drunk joyrider is paid, the drunk friend is not.** The exclusions speak of the "driver", which requires the owner's consent, so a thief crashing at 80 mg alcohol per 100 ml has the 16,000,000 loss paid while a consenting friend's is excluded (VN-01 X1; CONTESTED).
- **Meeting the 24-hour theft duty still loses 10%.** A theft reported in 20 hours satisfies the 24-hour duty, but a six-hour rule in the payout clause cuts 580,000,000 to 522,000,000 (VN-01 X3; CONTESTED).
- **Adding a child passenger removes the overload cut.** Seven adults in a five-seat car: 40% over, so 5,700,000 on a 10,000,000 repair; add a child under 7 and the two rules count differently, so 9,500,000 (VN-15 X4).
- **One dong decides who pays the independent assessment.** An assessment of 10,000,000 leaves the policyholder paying; 10,000,001 "differs", so the insurer pays (VN-15 X23).
- **A passenger's death is unpaid because of the driver's paperwork.** An expired inspection certificate or a red-light offence by the driver removes the passenger accident cover, and a third party's claim fails the same way (VN-17 X-19).
- **The excess-liability formula promises 60m and the layer rule pays 0** (VN-18 X19; CONTESTED).
- **A flooded electric motor is excluded and the flood add-on does not buy it back** (VN-18 X21; the lead checked it against source lines 784-785 and 1190-1192, and the same insurer's other product, VN-17, covers all engine types in a flood, source lines 1307-1314).
- **Compulsory insurance (Decree 67/2023):** a cyclist who causes an accident halves a pedestrian's compensation (75m instead of 150m) while a passenger in the same crash gets 150m (VN-10 R4); a parked car that rolls into a pedestrian is outside the cover (R2); a pillion rider who is not a "hành khách" is neither third party nor passenger (R1, CONTESTED).

### 5.2 Health, accident and travel

- **A claim file due before the disablement exists** (VN-03 X19, above), and **a living claimant must supply a death certificate** because benefit 6 has one document list for death and disablement (VN-03 X17).
- **Day-case surgery is paid by neither the surgery benefit (24-hour stay) nor the outpatient benefit** (VN-03 X25).
- **The eligibility clause, read at claim time, refuses every claimant**, because anyone under treatment is ineligible (VN-04 X4; CONTESTED).
- **Two families, one accident, one day**: the family already paid 30m gets 70m more on a later death, the family not yet paid gets nothing (VN-04 X1; CONTESTED).
- **365-day waiting periods sit inside a one-year term**, so chronic disease and childbirth cover on a first certificate is nothing, or one day in a leap year (VN-04 X14).
- **A roped climber is excluded and a free-solo climber is covered**, because the exclusion names climbing "with" safety gear (VN-19 X6).
- **Tuberculosis is covered from year two by one clause and excluded outright by another** (VN-19 X22).
- **A permanent-injury claim costs 600m on the same death**: claiming 40% for a lost eye leaves a death a year later with nothing more, while no earlier claim pays 1,000,000,000 (VN-23 D4).
- **Read literally, a business group accident policy excludes injury "while performing work"** (VN-23 D1; CONTESTED).
- **Travel**: a heart attack first striking on the trip is excluded from every section; a covered death six months after the accident pays 1,000,000,000 but the notice deadline closed 138 days earlier; liability cover pays 0 if the traveller is sued abroad (VN-06 F-HEART, F-PA-NOTICE, F-PL-FORUM).

### 5.3 Life

- **A murdered insured is excluded on the literal reading** of "phạm tội" (committing a crime), which names no offender: 207,000,000 against 757,300,000 (VN-13 finding 2; VN-11 finding 1; CONTESTED).
- **Only a dead policyholder can extend the claim year**, so a beneficiary who learns of the death 19 months later is out of time (VN-11 finding 3; LAW).
- **A covered accidental death pays 100m; an excluded suicide refunds 148m** (VN-14 X2).
- **An employer's crime defeats the employee's death benefit**, leaving an account value payable to nobody named (VN-14 X9).
- **A fatal motor race is paid on the death benefit while disability from the same race is excluded** (VN-24 X21).
- **Bigger first premium, smaller temporary cover**: above 100m the benefit is replaced by a refund (VN-24 X15, VN-25 FD9).
- **Claiming the permanent-injury maximum ends the contract and forfeits a 1,000,000,000 death benefit for the same accident** (VN-26 F-02; CONTESTED).
- **An accidental death on day 181 is paid nothing**, while the same death drunk or from illness pays 30,000,000 (VN-26 F-01).
- **The insurer's own slow letter defeats a timely reinstatement** (VN-26 F-16).

### 5.4 Property, liability and engineering

- **Winning at arbitration forfeits the win after a year** unless the insured challenges the final award (VN-05 X-award).
- **A year-end product injury falls between two consecutive claims-made policies** and the retroactive date never operates (VN-09 X1; CONTESTED).
- **Defence costs paid from the limit leave damages unpaid** that are below the limit (VN-09 X14).
- **Neglected gutters forfeit a storm claim** on the roof, because every condition is a condition precedent (VN-20 X14).
- **Insured at new price, paid at depreciated value**: 2,000,000,000 premium base, 1,200,000,000 paid (VN-22 X15).
- **A total loss pays nothing until the insured has paid to replace it** (VN-21 finding 9).
- **Hidden damage is time-barred before it is found**: a 14-day notice bar runs from the occurrence, not discovery (VN-21 finding 1; LAW).
- **A suit window of three months is already closed by a twelve-month liability bar** (VN-07 finding 3).

The leakage class, where the insurer pays more than it can have meant, includes: the thief who is paid because "driver" requires consent (VN-01 X1); the added child passenger (VN-15 X4); the drunk driver's own death paid in full because the drink-driving exclusion is worded for property only (VN-18 X1); early-stage advances that can exceed the sum insured (VN-24 X2); an excluded death paying more than a covered one (VN-25 FD5); fingers itemised paying more than the hand (VN-26 F-04); a loyalty bonus that counts one year's interest five times (VN-25 FD27); total-loss add-on paying above market value (VN-01 X20).
These are the same kind of defect as the payout-formula ambiguity that Legalese found in a major insurer's policy in an earlier engagement, and they are the ones a pricing or claims-leakage team would care about.

## 6. What found them, and what did not

Every finding came from encoding: reading the source line by line, writing tests from it, and seeing a test come out wrong or a clause have no answer.
None came from `l4 verify`.
On five Tasco rule modules (VN-17, VN-18, VN-19) `l4 verify` analysed 63 boolean decisions and reported "no propositional findings" for all 63, and it declined 101 others ("Can only visualize, as a ladder diagram, a DECIDE that returns a boolean").
That is expected from its stated design: it works on the boolean skeleton and treats every comparison as an opaque atom.
The classification above suggests where a stronger checker would have found things: clock and arithmetic classes (T1 and T4) appear in 168 records (28%), and cliffs, non-monotone tables, overlapping bands (VN-08 finding 8: short-period refund rows overlap at 3 and 6 months) and negative formulas are properties of numbers and dates, not of the boolean skeleton.
Classes T5, T6 and T7 (undefined terms, illusory cover, inconsistency) mostly need the clause text and a scenario; a solver over the encoded rules would find some by reachability ("is there any claim this exclusion does not defeat?") and not others.
The lead has not measured how many of the 594 any solver would find; that is untested.

## 7. What the set could serve as, and what it lacks

Each record already has the shape of a test item: a document and clause span (`src:N` lines into a pinned source), a scenario with numbers, the outcome on the literal reading, a class, a standing label, and, for about 70%, an executable assertion that demonstrates it.
What it lacks:

- **Adjudication.** The standing labels are the encoders' own.
  No Vietnamese insurance lawyer has said which findings are real, which are artefacts of the encoder's reading, and which an insurer would simply pay.
- **A false-positive rate.** The records list what encoders reported, not what they considered and dropped (VN-18 withdrew one, X12, as resting on assumptions outside the sources).
- **Independence beyond the model.** All encoders are the same model family working from the same instructions, so shared blind spots are possible and invisible.
- **Coverage.** 24 documents of the 1,130 catalogued; the sample is wordings that were easy to fetch.
- **Ground truth for what is not a defect.** There is no set of clauses confirmed clean.

## 8. Limits and disclosures

- VN-12 (Manulife endowment and critical illness) and VN-16 (PTI via Gras Savoye) are not in the 594; their encoders were interrupted by a usage limit and were being resumed when this was written.
- The extraction agents classified and cross-matched; the lead verified a sample against sources: VN-10 R5 against the gazette text, VN-18 X21 against source lines 784-785 and 1190-1192 and VN-17's flood clause at lines 1307-1314, the headline numbers of VN-01 X3, VN-13 finding 2, VN-25 FD5 and VN-26 F-02 against the findings assertions, and the five motor causal-link records against the encoders' notes.
  The rest are as reported.
- Blind-rule exceptions: VN-01's expander read VN-08's template header before the encoder noticed and stopped; VN-11 read part of VN-13's material (the file was deleted, and Meng ruled the contamination acceptable); an encoder ran a `pkill` on a pattern that may have killed a sibling's run.
- The quotation volume in the encodings is high (by character, about 30% to 100% of the source by row) and is accepted by Meng's ruling of 2026-10-07: "accept it as is. Unavoidable."
  Nothing here is pushed.
- Counts of classes depend on the extraction agents' judgment on borderline cases; the primary-class counts are not an independent classification.

## 9. Where things are

- Row encodings: `subjects/contracts/insurance/vn-*/encodings/legalese-2026-10-vn-NN/` and `subjects/vn/decree-67-2023/encodings/legalese-2026-10-vn-10/` (each with `NOTES.md` section 4, the findings or tests modules, `GLOSSARY.md`, `COMPARABLES.md`).
- The 594 records, one block per finding: `analysis/vn-insurance-findings/records-motor.md`, `records-health.md`, `records-life.md`, `records-property.md`; the parsed table `records.json` and the counting script `stats.py` are beside them.
- Source documents are fetched, not held: each row's `source/fetch.sh` pins the URL and sha256, and the downloaded PDFs sit in each row's gitignored `source/raw/`.
  For human reading there is one copy of all 30 on Meng's machine at `~/VN/sources/` (open `INDEX.html` there: each row, its publisher URL, its local file, its sha256).
