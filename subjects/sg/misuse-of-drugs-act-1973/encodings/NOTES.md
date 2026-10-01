# Misuse of Drugs Act 1973 — encoding notes

Source: Singapore Statutes Online, 2020 Revised Edition, current version as at 01 Oct 2026 (`../source/MDA1973.pdf`; `MDA1973.txt` is the reading copy whose line numbers the modules cite). An unofficial consolidation (SSO Terms of Use cl.8). One vintage. The text carries marginal amendments after the 2021 edition; those that are in force at 01 Oct 2026 are in the text, and the amendments commencing on 1 June 2024 (Misuse of Drugs (Amendment) Act 2023: psychoactive substances) are read as in force.

## 1. What is encoded and what is not

By the question a prosecutor asks:

| question | module |
| --- | --- |
| Is this an offence under the Act? Parts 2 (controlled drugs), 2A (psychoactive substances) and 2B (abetment, attempt, offences abroad, body corporate); the definitions they turn on (s 2) and proof of a psychoactive substance (ss 22A, 22B) | `mda-offences.l4` |
| What does the court presume, and what may it admit? ss 15 to 22, 23, certificates (ss 16, 31(6), 33(4AC) to (4AE), 33A(3), (4)) | `mda-presumptions.l4` |
| What is the punishment on conviction? The Second Schedule (86 rows as printed), ss 33, 33A, 33B, and the punishments the other sections state (49 rows) | `mda-punishment.l4`, with the generated data `mda-second-schedule.l4` and `mda-section-punishments.l4` |
| Who may search, arrest, take a specimen and seize, what is forfeited, and which court hears the case? ss 24 to 28, 30 to 32, 53 | `mda-enforcement.l4` |

**Not encoded:** the lists of substances in the First Schedule (well over 140 named Class A substances plus the chemical families defined by structure, about 20 Class B, about 20 Class C, and Part 4's definitions), the Third Schedule (controlled equipment, materials and substances), the Fourth Schedule (specified drugs) and the Fifth Schedule (excluded substances). They are chemical names. **The class of a drug (`Class A drug`, `Class B drug`, `Class C drug`), whether a thing is a controlled drug, a Third Schedule substance, or within another Fifth Schedule paragraph, and whether a controlled drug is a specified drug, are inputs.** Also not encoded: treatment and rehabilitation (ss 34 to 39) beyond the antecedent facts a previous admission supplies; photographs and body samples (ss 40A to 40D); committees of inquiry (ss 41 to 52); s 26A (disposal of seized items) and s 29 (disposal of forfeited things); ss 54 to 57; and the regulation-making powers (ss 10B, 58, 59).

## 2. Coverage table

| provision | heading | disposition | module |
| --- | --- | --- | --- |
| 1 | short title | inert | — |
| 2 | Interpretation: "controlled drug", "psychoactive substance", "excluded substance", "controlled equipment, material or substance", "traffic", "manufacture", "specified drug", "young person", "vulnerable person" | encoded (the first four as rules; "traffic" and "manufacture" in the offence rules; "young person" as 21; "specified drug" as a fact) | offences |
| 2 | "approved institution", "Director", "drug addict", "officer of the Bureau", "corresponding law" and the other defined terms | used as facts, inert, or in the officers rules | enforcement |
| 3, 4 | Director and officers of the Bureau; advisory committees | inert (appointment) | — |
| 5(1), (2) | trafficking | encoded | offences |
| 6, 7 | manufacture; import and export | encoded | offences |
| 8(a), (b) | possession; consumption | encoded | offences |
| 8A | consumption abroad by a citizen or permanent resident | encoded | offences |
| 9, 10, 10A | paraphernalia; cultivation; equipment for manufacture | encoded (10A(2): a licence is no defence to import or export: a field read for nothing) | offences |
| 10B | regulations on controlled equipment | out-of-scope | — |
| 11 | owners, tenants, occupiers | encoded | offences |
| 11A | arranging or planning gatherings | encoded | offences |
| 11B, 11C, 11D, 11E | exposing a child; introducing a trafficker; instruction and dissemination; procuring a young person | encoded | offences |
| 11F to 11Q | the Part 2A mirror: psychoactive substances (trafficking, manufacture, import and export, possession and consumption, 11J abroad, paraphernalia, premises, gatherings, children, introductions, instruction, young persons) | encoded | offences |
| 12, 12A | abetment, attempts, preparatory acts; (12A repealed) | encoded | offences |
| 13 | abetting or procuring offences within or outside Singapore | encoded | offences |
| 14 | body corporate | encoded | offences |
| 15 | certificate of corresponding law | encoded | presumptions |
| 16 | certificate of analyst | encoded | presumptions |
| 17 | presumption concerning trafficking | encoded | presumptions |
| 18, 18A | possession and knowledge of controlled drugs; of psychoactive substances | encoded | presumptions |
| 19, 20, 21, 22 | premises; ship or aircraft; vehicle; urine test | encoded | presumptions |
| 22A, 22B | proof of, and knowledge of, a psychoactive substance | encoded | offences |
| 23 | protection of informers | encoded | presumptions |
| 24, 25, 25A, 26 | search and seizure; arrest; bail and bond; ships, vehicles, persons arriving or departing | encoded at the threshold: who may act and on what suspicion; the conduct (break open, taken to the Bureau, directions to operators) is inert | enforcement |
| 26A, 29 | disposal of seized items and forfeited things | out-of-scope | — |
| 27, 28 | forfeiture | encoded | enforcement |
| 30 | obstruction | encoded | enforcement |
| 31, 31A, 31B | urine, hair and oral fluid tests | encoded; 31(3) (non-citizens arriving) inert | enforcement |
| 32 | investigation by officers of the Bureau | encoded; 32A (arms) inert | enforcement |
| 33 | punishment for offences | encoded | punishment |
| 33A | repeat consumption of specified drugs | encoded | punishment |
| 33B | discretion not to impose death | encoded | punishment |
| 34, 34A to 40 | supervision, treatment and rehabilitation; approved institutions; review committees; inmates | out-of-scope (administration of orders and institutions), except 34A(2) (a punishment row) and 38A(5), 40B(4) (punishment rows); a previous admission under s 34(2) is an input | section-punishments |
| 40A to 40D | photographs, finger impressions, particulars, body samples | out-of-scope | — |
| 41 to 52 | committee of inquiry | out-of-scope (inquiries into approved institutions). Their punishments (ss 44(3), 45(2), 46, 52) are not rows | — |
| 53 | jurisdiction of courts | encoded, and handed to the Code | enforcement |
| 54, 55, 56, 57 | indemnity; protection; weapons; auxiliary police | out-of-scope (the deeming of an auxiliary police officer as a public servant, s 57(4), is noted in the Penal Code cross-reference) | — |
| 58, 58A, 59 | regulations; Minister's power to amend Schedules | out-of-scope | — |
| First, Third, Fourth, Fifth Schedules | substances | out-of-scope (inputs, above) | — |
| Second Schedule | offences punishable on conviction | encoded: the table in full, 86 rows | second-schedule |

No row is `deferred`.

## 3. Files

| file | what it is |
| --- | --- |
| `mda-types.l4` | the nouns: one record of facts per provision |
| `mda-second-schedule.l4`, `mda-section-punishments.l4` | **generated** by `generators/mda_schedule.py`: the Second Schedule's printed table and the punishments the sections state. Do not edit |
| `mda-offences.l4`, `mda-presumptions.l4`, `mda-punishment.l4`, `mda-enforcement.l4` | the rules |
| `written-law-interface.l4` | DECLARE-only; **identical in this row, `sg/criminal-procedure-code-2010` and `sg/prevention-of-corruption-act-1960`** (section 4) |
| `mda-tests-offences.l4` (198), `mda-tests-presumptions.l4` (89), `mda-tests-punishment.l4` (328), `mda-tests-enforcement.l4` (324) | tests **generated** by `generators/mda_tests_1.py` and `mda_tests_2.py` |
| `check.sh` | runs every module and compares the interface module with the copies in the sibling subjects |

## 4. Cross-subject references

`l4` resolves an `IMPORT` only to a module in the importing file's directory, so **no module in this row can import a rule from another subject**. Each reference is a fact the caller supplies, the interface record `Written Law Procedure Statement`, or a comment.

| the Act says | in | how it is represented here | where the other side is |
| --- | --- | --- | --- |
| the police may arrest without a warrant any person who has committed or is reasonably suspected of an offence under the Act (s 25(1)); a District Court has power to impose the full penalty except death (s 53) | MDA | `the Misuse of Drugs Act 1973's statement about its offences` | `sg/criminal-procedure-code-2010`, `cpc-other-laws.l4` |
| the Act is item 12 of the Code's Second Schedule | CPC | not restated | `cpc-second-schedule.l4`; `cpc-tests-other-laws.l4` |
| the Code's powers of a police officer in an investigation into an arrestable offence; "arrestable offence" (s 32); Division 5 of Part 6 (bail, s 25A); ss 325(1), 330(1) of the Code (caning, s 33(3)); s 92 | MDA | comments and the officers rules; the Code's rules are the Code's | CPC row: only the First and Second Schedules and the sections that read them are encoded |
| "a public servant within the meaning of the Penal Code 1871" for committee members and auxiliary police officers (ss 42(4), 57(4)) | MDA | out-of-scope Parts; noted here | `sg/penal-code-1871` s 21 |
| abetment, attempt and conspiracy: s 12 makes the abettor, attempter or preparer guilty of the offence and punished as for it | MDA | `the accused is guilty of the offence by section 12`; the punishment is the offence's own row | `sg/penal-code-1871` Chapters 5, 5A, 23 |
| Singapore Armed Forces Act 1972 ss 3, 26, 34, 82(5) (military courts, consumption offences) (ss 31(9), 33, 33A) | MDA | facts: previous convictions and the counts of them | not encoded in this corpus |
| Customs Act, Immigration Act, Police Force Act, Prisons Act, Medicines Act, Health Products Act, Tobacco and Vaporisers Control Act, Air Navigation Act: definitions | MDA | facts and the Officer Role enumeration | not encoded in this corpus |
| "proved" in the presumptions ("until the contrary is proved"; s 17 "unless it is proved that ... was not for that purpose") | MDA | the accused's rebuttal is a fact; the standard is not encoded | Evidence Act s 3, `sg/evidence-act-1893` |
| informers (s 23: no witness is "obliged" to disclose; the court may require disclosure in two cases) | MDA | `the court may permit inquiry and require full disclosure concerning the informer` | Evidence Act ss 126, 127; compare Prevention of Corruption Act s 36, which says "obliged or permitted" |
| certificates "admissible ... without proof of signature" and "proof of all matters contained therein" (ss 16, 33(4AC) to (4AE)) | MDA | `the analyst's certificate is admitted without proof of signature`, `… is proof of all matters contained in it` | Evidence Act Part 3 (documents) and s 80 |

What is NOT done: the Code's rules cannot call the Act's punishments. The caller passes the maximum term, death and life to the Code's `Jurisdiction Facts`. The cross-reference that would need a real cross-subject import is that one.

## 5. How the punishment is found

`the punishment on conviction ...` returns a `Punishment`: death; imprisonment for life possible; maximum and minimum imprisonment in months; maximum and minimum fine; minimum and maximum strokes; and whether imprisonment, fine or both may be imposed in the alternative ("or ... or both"). A `0` means none printed. It is the printed range, not a sentence.

**Order of precedence** (s 33(1): "Except as provided in subsection (3B), (4A), (4B) or (4C) or under section 33A"; s 33(4D)):

| offence | the order | rule |
| --- | --- | --- |
| trafficking, import, export (5(1), 7) | 1 the sixth column (a specified quantity or a specified drug) if engaged; 2 s 33(4A) (a previous conviction under 5(1), 7, 11F(1), 11H(1)); 3 s 33(4B) (21 or older and a young or vulnerable intended recipient); 4 the class column | `the punishment on conviction of an offence under section 5(1) or 7` |
| possession (8(a)) | the sixth column; s 33(3B) where the row says so and there is a previous conviction under 8(a) or 11I(1)(a) | `the punishment on conviction of an offence under section 8(a)` |
| consumption, failing to provide a specimen (8(b), 31(2), 31A(2)) | 1 s 33A(2); 2 s 33A(1), (1A), (1B); 3 ss 33(4), (4AA), (4AB); 4 s 33(3A) | `the punishment on conviction of consumption or of failing to provide a specimen` |
| consumption of a psychoactive substance (11I(1)(b)) | s 33(3D) if a previous conviction or admission; else s 33(3C) | `the punishment on conviction of an offence under section 11I(1)(b)` |
| gathering (11A) | s 33(4C) where 21 or older and the gathering has a young or vulnerable person | `the punishment on conviction of an offence under section 11A` |
| any other offence in the Schedule | the row | `the Second Schedule punishment` |
| any other offence with its punishment in its section | the enhanced band, then the repeat band, then the base band | `the punishment the section states for the offence` |
| death | s 33B: the court may (1)(a) or must (1)(b) impose life imprisonment instead | `the sentence where the sixth column punishment is death` |

## 6. Fork register

| id | where the text is ambiguous or silent | reading taken | text |
| --- | --- | --- | --- |
| F1 | the substance lists | not carried; class and "is a controlled drug" are inputs | First, Third, Fifth Schedules |
| F2 | psychoactive substance and controlled drug | mutually exclusive, because Fifth Schedule para 4 excludes "any controlled drug or controlled substance" from "psychoactive substance" | s 2; Fifth Schedule |
| F3 | the rebuttal of a presumption | a fact; the standard is not encoded | ss 17 to 22 |
| F4 | Second Schedule, sixth column: one drug can engage two rows (a drug containing diamorphine and cocaine); and an opium band asks for the weight and the morphine | where two rows engage and print different punishments, REFUSE; opium in the weight band without the morphine content engages no sixth-column row, so the class column answers (opium 1,500 g containing 25 g of morphine is neither within 5(2)(a) nor 5(2)(b)) | the Schedule prints no rule for either |
| F5 | "except as otherwise provided in this Schedule" | the class-column rows of ss 5, 6, 7 and the possession row 8(a)(9) apply only when no specific sixth-column row is engaged | Second Schedule, 5(1), 6(1), 7(1), 8(a)(9) |
| F6 | an offence under 8(b), 31(2) or 31A(2) committed before 1 April 2019 | REFUSE: s 33(3A) says "committed on or after 1 April 2019" and the earlier text (the Schedule's deleted rows) is not in this text. s 33(4) prints no maximum; the row's maximum is 0, "none printed" | s 33(3A); Second Schedule 8(b), 31(2), 31A(2) "[Deleted by Act 1 of 2019]" |
| F7 | s 53, Magistrate's Court | the statement to the Code says FALSE: "jurisdiction to hear and determine all proceedings" read literally with the Code's s 9(2)(b) would let a Magistrate's Court try an offence punishable with death; the Code's s 7(1)(a) decides | s 53; CPC s 9(2)(b) |
| F8 | the repeat and enhanced bands of ss 11B to 11Q, 33(3B), 33(3D), 33(4A) to (4C) | engaged by facts the caller supplies; the section's condition is printed in each row's `what engages the band`. Only the antecedent counts of s 33A and ss 33(4), (4AA), (4AB) are computed | the sections |
| F9 | s 11P(9)(b), (c): the belief defence applies to manufacture, and to trafficking, import and export | applied to every activity except consuming alone | s 11P(9) |
| F10 | s 5(2) and s 17 | possession for the purpose of trafficking is trafficking; the section 17 outcome stands for that element and is an input | ss 5(2), 17 |
| F11 | s 20 | the presumption is of the drug's import with the master's or captain's knowledge, whoever is accused | s 20 |
| F12 | s 24 "senior officer of customs"; ss 25, 26 "officer of customs" | kept as printed | ss 24(1), 25(1), 26(1) |
| F13 | 33(3A) "shall also be liable to a fine not exceeding $20,000" | the maximum fine is $20,000 and the fine is in addition to imprisonment (not in the alternative) | s 33(3A) |
| F14 | s 17(ha) "113 grammes of ketamine" and (i) the three amphetamines "10 grammes of any or any combination" | the thresholds are strict ("more than"); the three are summed | s 17 |

## 7. The Second Schedule data: how it was made and checked

The table is printed in a layout the text extraction scrambles (item numbers, lettered paragraphs and the sixth column are laid out in columns). It was read from `MDA1973.txt` lines 5869 to 6770 and transcribed into `generators/mda_schedule.py`, which writes the 86 rows. Checks run:

1. **The printed cells are transcribed a second time, as the printed words**, in `generators/mda_tests_2.py` ("Maximum 20 years and 15 strokes; Minimum 5 years and 5 strokes"), parsed there into a `Punishment`, and the encoding is tested against that at, below and above every band edge for every specified substance in ss 5, 7 and 8(a). The two transcriptions agree (328 assertions in `mda-tests-punishment.l4`).
2. **Every threshold figure** (800, 1,200, 330, 500, 660, 1,000, 130, 200, 167, 250, 20, 30, 10, 15 grammes; $200,000, $40,000, $20,000, $10,000, $5,000, $4,000, $2,000, $1,000) occurs in the printed Schedule's text; the counts of 4 for each of 330, 660, 130, 167 and 800 are consistent with each appearing once in each of ss 5 and 7 (the "not less than" band and the "not more than" band) and in 8(a)'s (a) and (b) bands.
3. **Row count**: 15 class rows (5 sections by 3 classes), 32 sixth-column rows for trafficking, import and export (2 sections, 8 items, 2 bands), 4 for manufacture, 25 for possession (8 items by 3 bands and the residual 8(a)(9)), 10 in the seventh column. 86 in all; the four rows the Schedule itself prints as "[Deleted by Act 1 of 2019]" (8(b), 13, 31(2), 31A(2)) are not rows and are asserted absent.

What was **not** done: the table was not read against the printed page by a second person, and the printed page's layout (which paragraph a cell belongs to) was read from the text, not the image.

## 8. What `check.sh` prints

```
module                                    errors satisfied  failed
mda-enforcement.l4                             0         0       0
mda-offences.l4                                0         0       0
mda-presumptions.l4                            0         0       0
mda-punishment.l4                              0         0       0
mda-second-schedule.l4                         0         0       0
mda-section-punishments.l4                     0         0       0
mda-tests-enforcement.l4                       0       324       0
mda-tests-offences.l4                          0       198       0
mda-tests-presumptions.l4                      0        89       0
mda-tests-punishment.l4                        0       328       0
mda-types.l4                                   0         0       0
written-law-interface.l4                       0         0       0
TOTAL (12 modules)                             0       939       0
```

No assertion is expected to fail. The tests were written from the Act's text by the same session that wrote the rules; **no independent test pass has been run** (the encoding-a-subject skill's step 8) and no domain expert has read the modules against the Act (gate HG1).

## 9. Open questions for a domain expert

- s 33(4): "punished with imprisonment for a term of not less than 3 years" prints no maximum. Is the maximum that of s 33(3A) (10 years) or none? The row records none printed.
- s 33(3B) applies to "an offence under section 8(a) that the sixth column of the Second Schedule specifies is subject to this subsection": the rows marked "(subject to section 33(3B))" are the (a) bands and 8(a)(9). Are the (b) and (c) bands intentionally outside it?
- Two sixth-column rows for one drug (F4): is the intended answer the heavier?
- s 8(b)(i) and (ii): the distinction matters only through s 33A, which speaks of "specified drug"; the first-offence punishment is the same. Intended?
- s 11E and s 11Q: whether the young person must in fact have committed the offence (encoded as an input).
- s 53 and the Magistrate's Court (F7).
- Whether a person with a previous conviction under s 8(a) for a Class A drug, now convicted of 8(a) for a quantity within the (b) band, is outside s 33(3B) (the encoding says yes, as the row says).
