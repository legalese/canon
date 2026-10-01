# Criminal Procedure Code 2010 — First Schedule — encoding notes

Row `legalese-aswathy`. Status `draft`. **No domain expert has read this against the source, and no independent test pass has been run** (section 6).

## 1. What is encoded and what is not

**Scope, by the requester's instructions of 2026-10-01: the First Schedule, then the Second Schedule**, with the provisions that read them. The Schedule is "Tabular statement of offences under the Penal Code 1871", as printed in Singapore Statutes Online's PDF, current version as at 01 Oct 2026. It is a procedural cross-reference for Penal Code offences: for each Penal Code section it says whether the police may ordinarily arrest without warrant, whether a warrant or a summons ordinarily issues, whether the offence is bailable of right, the maximum punishment, and which court tries it besides the General Division of the High Court. It is **not** a list of all Singapore criminal offences, and it is **not** a statement of the elements of the offences (Explanatory Note 1 says so); the elements are in the Penal Code (`sg/penal-code-1871`).

| module | covers |
| --- | --- |
| `cpc-types.l4` | the nouns: the four rule enumerations, the `First Schedule Row`, `Procedural Treatment`, `Jurisdiction Facts` |
| `ea-cpc-interface.l4` | the interface to the Evidence Act subject, **identical in both rows**; nothing in this row's rules reads it yet (section 4) |
| `cpc-first-schedule.l4` | the data: 478 printed rows and the 4 "other written law" rows. **Generated**; do not edit |
| `cpc-offence-procedure.l4` | reading a row; derived rows; the four "other written law" bands; ss 7 to 9 (trial courts) |
| `cpc-second-schedule.l4` | the Second Schedule (32 items, written laws) and the two sections that read it: s 159 (State Courts) and s 211A (High Court) |
| `written-law-interface.l4` | the interface to the Acts that create their own offences, **identical in this row, `sg/prevention-of-corruption-act-1960` and `sg/misuse-of-drugs-act-1973`**: one record, `Written Law Procedure Statement` (section 4) |
| `cpc-other-laws.l4` | an offence under an Act that has made its statement: arrestable, warrant or summons, bailable, the trial courts, and the Second Schedule, read together; the Prevention of Corruption Act 1960 and the Misuse of Drugs Act 1973 are the two Acts that have made one |
| `cpc-tests-offence-procedure.l4` | 135 assertions. **Generated** by `generators/cpc_tests_1.py` |
| `cpc-tests-second-schedule.l4` | 103 assertions. **Generated** by `generators/cpc_tests_2.py` |
| `cpc-tests-other-laws.l4` | 126 assertions: worked examples for an offence under each of the two Acts, with and without the Act's statement. **Generated** by `generators/cpc_tests_3.py` |

**Two questions.** *Do the criminal case disclosure procedures apply to this offence?* (Second Schedule, ss 159, 211A). The Schedule lists written laws, not offences: an offence is within it when its Act is listed (item 9 excludes ss 6 and 15 of the Immigration Act 1959; item 2A is the Banishment Act 1959 only as in force before the 2023 amendment). Section 159 then asks whether the case is to be tried in a District Court, and s 211A whether it must be, or has been designated to be, tried in the High Court; the parties' consent extends both. *And: what is the procedural treatment of this offence?* Given a Penal Code section (and subsection), `the First Schedule rows for the Penal Code section` returns its rows; `the procedural treatment of a row` returns arrestable, warrant, bailable and which courts may try it. For an offence under another written law, the four printed bands give the answer by the severity of the punishment, **and the other law may say otherwise** ("unless specifically empowered ... by the law offended against"; s 2(1) "or under any other written law"; "shown to be triable ... under that law"): `cpc-other-laws.l4` reads those three answers from an Act's own statement, for the two Acts that have made one.

**Not encoded, and why** (section 2 has the account):

- every other section of the Code (Parts 1 to 22), and the Third, Fourth, Fifth, Sixth and Seventh Schedules: out of scope by instruction. The procedures of Part 9 and Part 10 Division 5 themselves (the Case for the Prosecution and the Case for the Defence) are not encoded; only whether they apply is. The Code's Part 14 (evidence and witnesses), which connects to the Evidence Act subject, is among them.
- the elements of the offences: the Penal Code, `sg/penal-code-1871`.
- the other written laws whose offences the four bands cover, except the Prevention of Corruption Act 1960 and the Misuse of Drugs Act 1973 (which make their statements in their own rows), and the Criminal Procedure Rules.

## 2. Coverage table

Disposition: `encoded` (a rule or the data in the module named); `inert` (read, adds no condition or answer; the reason is given); `out-of-scope` (by instruction of 2026-10-01 — **not** a defect nothing detects: the encoding says so out loud).

| provision | heading | disposition | where |
| --- | --- | --- | --- |
| First Schedule, rows for Penal Code sections (chapters 3 to 23) | Tabular statement of offences under the Penal Code 1871 | encoded: 478 printed rows, seven columns each | first-schedule |
| First Schedule, "Offences against laws other than the Penal Code 1871" | | encoded: 4 rows (section "Other written law") | first-schedule; offence-procedure |
| First Schedule, Explanatory Notes (1) and (2) | | inert: they say the table is not a definition of the offences or punishments and does not restrict police powers of arrest; quoted in the data module header | first-schedule |
| First Schedule heading (the sections that refer to it: 2(1), 9(2) and (3), 153(1) and (3), 226(5), 427(1)) | | 2(1) and 9 encoded; 153, 226, 427 out-of-scope | offence-procedure |
| 1 | Short title | inert | — |
| 2(1) "arrestable offence", "arrestable case", "non-arrestable offence", "non-arrestable case" | | encoded as the meaning of column 3 | offence-procedure |
| 2(1) "bailable offence", "non-bailable offence" | | encoded as the meaning of column 5 | offence-procedure |
| 2(1) "fine-only offence" | | encoded (a field of `Jurisdiction Facts`) | offence-procedure |
| 2(1) other definitions; 2(1A), 2(2) | | inert: not read by the Schedule | — |
| 3 | Service of notices | out-of-scope | — |
| 4(1), (2) | Trial of offences under Penal Code 1871 or other laws | inert: says both kinds of offence are tried under the Code, subject to other laws regulating manner or place; the four bands carry the other-law case | offence-procedure (comment) |
| 5, 6 | Saving of powers; where no procedure is provided | out-of-scope | — |
| 7(1)(a) | Magistrates' Courts: offences up to 5 years or fine-only | encoded (fork F1) | offence-procedure |
| 7(1)(b) | deleted | inert | — |
| 7(1)(c) to (g), 7(2), 7(3) | other powers; where exercised | out-of-scope | — |
| 8(1) | District Courts: offences up to 10 years or fine-only | encoded (fork F1) | offence-procedure |
| 8(2) | a District Court has the powers of a Magistrate's Court | out-of-scope | — |
| 9(1) | Public Prosecutor may authorise a Magistrate's Court | encoded | offence-procedure |
| 9(2), 9(3)(a), (b), (c) | enlargement by the First Schedule's seventh column, by another law, by consent | encoded | offence-procedure |
| 9(4) | no enlargement of s 303 powers | inert: s 303 is not encoded | — |
| 10 to 13 | consent; the Public Prosecutor | out-of-scope (written and tested, then removed when the scope was narrowed to the First Schedule) | — |
| 14 to 429 | Parts 4 to 22, including Part 14 (evidence and witnesses) | out-of-scope | — |
| Second Schedule, items 1 to 23 (32 items with the lettered ones) | Laws to which criminal case disclosure procedures apply | encoded: data, and `the offence is under a law specified in the Second Schedule` | second-schedule |
| 159(1), (3) | When criminal case disclosure procedures apply (State Courts) | encoded (fork F7); 159(2) deleted | second-schedule |
| 211A(1), (2) | When they apply (High Court) | encoded (fork F9) | second-schedule |
| First Schedule bands for other written laws, read with an Act's own statement | | encoded for the Prevention of Corruption Act 1960 (item 16A of the Second Schedule) and the Misuse of Drugs Act 1973 (item 12) | other-laws |
| 158, 160 to 171, 172 to 221 (the procedures themselves), 427(1) (power to amend the Schedules) | | out-of-scope | — |
| Third, Fourth, Fifth, Sixth, Seventh Schedules | | out-of-scope | — |

## 3. The data: how a printed row becomes a record

Seven printed columns land in one `First Schedule Row`: `printed section` and `base section` (column 1), `offence description` (2), `arrest rule` (3), `process rule` (4), `bail rule` (5), `maximum punishment` as printed (6), `court rule` (7); plus `chapter heading` (with the sub-heading), `derivation note` and `page of the SSO PDF`. The first table lists the controlled values.

| column | value | rows |
| --- | --- | --- |
| 3 arrest | May arrest without warrant | 386 |
| | May not arrest without warrant | 58 |
| | May not arrest ... unless specifically empowered by the law offended against | 2 |
| | As for the underlying offence | 36 |
| 4 process | A warrant ordinarily issues | 353 |
| | A summons ordinarily issues | 109 |
| | As for the underlying offence | 19 |
| | As for the offence committed by the person hired, engaged or employed | 1 |
| 5 bail | Not bailable | 302 |
| | Bailable | 162 |
| | As for the underlying offence | 18 |
| 7 court | Magistrate's Court or District Court | 263 |
| | District Court | 130 |
| | General Division of the High Court only (blank cell; fork F3) | 57 |
| | As for the underlying offence | 28 |
| | According to sections 7, 8 and 9 (the four other-law rows) | 4 |

(482 rows: 478 printed, 4 other-law bands. 46 printed rows have at least one derived cell.)

A **derived cell** is one that is not a fixed answer: "According as to whether a warrant or summons may issue for the offence abetted", "The court by which the offence attempted is triable", "May arrest without warrant, if arrest for the offence abetted may be made without warrant but not otherwise". They occur in the rows for enhanced penalties (ss 73, 74A, 74B), abetment (ss 109 to 120), conspiracy (s 120B), unlawful assembly (ss 149, 150), the false-evidence family (ss 193 to 201), omission to apprehend (ss 213, 214, 221, 222), forgery (s 471) and attempts (s 512(2)). Such a row answers a column only when the underlying offence's treatment is supplied (`the procedural treatment of a derived row`); otherwise the rule is a named `REFUSE` that says why. The printed words are kept in `derivation note`.

Rows are not unique by section: a section can have several rows (s 193 two, s 222 three, s 130B two), and the section is printed with its subsection (`375(2)`, `376EB(3)(a)`). `base section` is the section without its subsection (`375`, `376EB`); the lookup is by `base section`, and the printed section is kept.

## 4. The Evidence Act relationship

The Code's Part 14 (evidence and witnesses) is out of scope here, so nothing in this row's rules reads the Evidence Act. `l4` resolves an `IMPORT` only to a module in the importing file's own directory (the project root, `JL4_LIBRARY_PATH` or the embedded library), so a rule in one subject cannot import a module from another. The two subjects therefore meet at **`ea-cpc-interface.l4`**, a DECLARE-only file carried **byte-identically** in `sg/evidence-act-1893/encodings/` and here. Its two records are the conclusions each Act hands the other: `Evidence Act Conclusions` (computed by the Evidence Act row, to be consumed by the Code's Part 14) and `Code Conclusions` (computed by the Code, consumed by the Evidence Act's ss 32(4) and 122(5)). Identity is checked with `cmp` (section 5).

Limitation to report: the two Acts reference each other through a copied interface module, not through a cross-subject import. The exact references the interface stands for are listed in the Evidence Act row's NOTES.md section 4.

### 4A. The Acts that create their own offences

The same arrangement, for a second interface. The First Schedule's last four rows, and ss 2(1) and 9(2) and (3), leave three answers to "the law offended against" or "any other written law": that the police are specifically empowered to arrest without warrant, that the offence is arrestable, and that the law shows the offence as triable by a District Court or a Magistrate's Court under that law. **`written-law-interface.l4`** declares one record, `Written Law Procedure Statement`, carried byte-identically in this row, `sg/prevention-of-corruption-act-1960` and `sg/misuse-of-drugs-act-1973`. The Act's row computes it from the Act's own sections (the Prevention of Corruption Act ss 32(1), 34; the Misuse of Drugs Act ss 25(1), 53); `cpc-other-laws.l4` reads it. `check.sh` compares the copies with `cmp` in each of the four rows that carry an interface module.

| the Code needs | the Act says | the statement says |
| --- | --- | --- |
| arrestable whatever the punishment | PCA s 32(1): every offence "deemed to be an arrestable offence for the purposes of the Criminal Procedure Code 2010" | `the Act deems the offence to be an arrestable offence ...` TRUE |
| the law offended against specifically empowers the police | MDA s 25(1): an officer of the Bureau, police officer, special police officer or officer of customs "may arrest and search without a warrant" any person who has committed or is reasonably suspected of an offence under the Act; PCA s 15(1) gives the power to the Director and special investigators, not the police | MDA TRUE; PCA FALSE |
| District Court | PCA s 34 "jurisdiction to try any offence under this Act and to award the full punishment"; MDA s 53 "a District Court has power to impose the full penalty ... except the punishment of death" | TRUE for both (the Code's s 9(3) itself excepts an offence punishable with death) |
| Magistrate's Court | PCA: silent; MDA s 53 gives it jurisdiction over "all proceedings" | FALSE for both (fork F10; the Code's own s 7(1)(a) still lets a Magistrate's Court try an offence up to 5 years) |

The Second Schedule needs no statement: items 12 and 16A already list the Misuse of Drugs Act 1973 and the Prevention of Corruption Act 1960 as printed, and `cpc-tests-other-laws.l4` tests that an offence under either is within it and that `the criminal case disclosure procedures` then apply as ss 159 and 211A say.

What is NOT done, and why: the Code's rules cannot call the Act's `the punishment for the offence`; the caller passes the maximum term, death and life as `Jurisdiction Facts`. The cross-reference that would need a real cross-subject import is that one.

## 5. What `check.sh` prints

Run with `l4` build `unstable-20260926-c76e6b0` (win32-x64), 2026-10-01:

```
module                                    errors satisfied  failed
cpc-first-schedule.l4                          0         0       0
cpc-offence-procedure.l4                       0         0       0
cpc-other-laws.l4                              0         0       0
cpc-second-schedule.l4                         0         0       0
cpc-tests-offence-procedure.l4                 0       135       0
cpc-tests-other-laws.l4                        0       126       0
cpc-tests-second-schedule.l4                   0       103       0
cpc-types.l4                                   0         0       0
ea-cpc-interface.l4                            0         0       0
written-law-interface.l4                       0         0       0
TOTAL (10 modules)                             0       364       0
```

No assertion is expected to fail. `check.sh` compares each `*-interface.l4` with the copies of the same name in the sibling subjects with `cmp`: identical (the check was added on 2026-10-01 and is in the Evidence Act row's `check.sh` too).

## 6. Fork register

| fork | the readings | taken | why |
| --- | --- | --- | --- |
| F1 | ss 7(1)(a) and 8(1) test "the maximum term of imprisonment provided by law": is life imprisonment, or death, within 5 or 10 years? | no: outside both | life imprisonment is not a "term" of years (s 2(1) "life imprisonment" is for the duration of a person's natural life); s 9(3) itself excepts "an offence punishable with death" from District Court jurisdiction by enlargement |
| F2 | a derived cell could be left blank, copied from the printed words as a string, or made a rule | a constructor `As for the underlying offence`, printed words in `derivation note`, answer only when the underlying offence is supplied | the Schedule says the answer is that of the underlying offence; guessing it would be inventing a rule |
| F3 | a blank "by what court triable" cell | no court besides the General Division of the High Court | the column is headed "besides the General Division of High Court", so a blank cell means no court besides it. The 57 blank rows are the most serious offences (death, life, or 15 to 20 years, e.g. ss 121, 194, 375(2), 395, 512(1)), but not all: s 306 and s 399 are printed with 10 years and a blank court although s 8(1) would let a District Court try a 10-year offence. The Schedule does not state the reading in terms |
| F4 | the four "other written law" rows are printed after s 512(2) and the extraction first fused them into it | separate rows, section "Other written law", court "According to sections 7, 8 and 9" | they are headed "OFFENCES AGAINST LAWS OTHER THAN THE PENAL CODE 1871" and are not attempts |
| F5 | "May not arrest without warrant unless specifically empowered to do so by the law offended against" | not arrestable ordinarily; the other law's own power is a further input (`the law offended against specifically empowers ...`) | s 2(1) defines arrestable by "ordinarily arrest without warrant according to the third column ... or under any other written law" |
| F7 | s 159(1)(b) "is to be tried in a District Court" | a fact about the forum; a Magistrate's Court trial is outside (1) and needs consent under (3) | the text |
| F8 | item 9 "other than sections 6 and 15" | the section is tested without subsections, so every subsection of ss 6 and 15 is excluded | the item names sections, not subsections |
| F9 | s 211A(2) "any offence that is to be tried in the General Division of the High Court, but is not mentioned in subsection (1)" | consent extends the procedures to an offence designated for the High Court under a law the Schedule does not list | (1)(a) already covers every offence that must be tried there |
| F10 | an Act's statement (`cpc-other-laws.l4`) | it can only add to what the case already shows (it makes `a law other than the Penal Code shows the offence as triable by a ... Court under that law` true, never false); an Act that deems its offences arrestable (PCA s 32(1)) makes every offence under it arrestable whatever its punishment; an Act that empowers the police (MDA s 25(1)) engages "unless specifically empowered" and so matters only below 3 years' imprisonment; neither statement says a Magistrate's Court may try the offence, so s 7(1)(a) decides | ss 2(1), 9(2)(b), 9(3)(b) and the First Schedule's last four rows |
| F6 | the third column "ordinarily": Explanatory Note 2 says the column does not restrict the powers of arrest police officers may lawfully exercise | the column answers "ordinarily", and no rule says a non-arrestable offence cannot lead to an arrest | s 64 and s 65 give other powers; they are not encoded |

## 7. Extraction of the First Schedule: what was tried and what was checked

The table has no ruled lines and stacks several section numbers in the first column. Three readings were tried:

1. `pdftotext -layout` (the file `source/CPC2010.txt`): **rejected for the table**: stacked section numbers drift away from their rows (a row for "sale of obscene objects" appears under s 302).
2. PyMuPDF's table finder: **rejected**: it drops whole rows (ss 113 to 118) and merges adjacent ones.
3. `generators/first_schedule_extract.py`: **used**. It reads each character's position, splits spans into words, places each word in a column by its left edge, and starts a row at each section number in the first column. Body text is 10 pt but rows added by amendment are 11 pt, so size is not used to tell a heading from a row; chapter headings are found by their text and sub-headings by being centred italic lines.

Checks run on the result (478 rows):

- every one of its 478 section numbers matches a section number at the start of a line in the layout text; the layout text has 19 more such tokens, each a punishment figure ("20 years") or a section named in the text of another row ("121B or 121C");
- compared row by row with the table finder's output (464 rows), 460 agree on columns 3, 4, 5 and 7, and the other 4 differ only because the table finder had merged two rows (ss 193 and 222); the PDF's own word positions confirm this encoding's reading;
- every cell in columns 3, 4, 5 and 7 maps to a controlled phrase, and `first_schedule_l4.py` stops on a phrase it does not know;
- 135 assertions (section 5) read rows back through the L4 lookup for standard rows (ss 379, 500, 506, 489H, 193) and each derived-row kind, and the courts of the other-law bands.

**Not checked:** a human reading of the printed table against the 478 rows, column 2 and column 6 text (offence descriptions and punishments are carried as printed and are not tested), and the marginal amendment notes' effect on any row's date.

## 8. Open questions for a domain expert

- Second Schedule: it says "laws"; is an offence under subsidiary legislation made under a listed Act within it? The encoding takes the Act that creates the offence as given and does not decide this.
- s 211A(2) (fork F9): is the meaning taken the intended one?
- Misuse of Drugs Act s 53 gives a Magistrate's Court jurisdiction over "all proceedings under this Act". Read literally with Code s 9(2)(b), a Magistrate's Court could try an offence punishable with death. The statement says FALSE and leaves the Magistrate's Court to s 7(1)(a); is that the intended reading (fork F10)?
- Are blank "by what court triable" cells (57 rows) meant as "General Division of the High Court only" (F3)? In particular ss 306 and 399 (10 years) and ss 123 and 130C (15 years): s 8(1) alone would let a District Court try a 10-year offence, so the blank there either overrides s 8(1) or is a gap.
- For the false-evidence rows (ss 195 to 200) the printed arrest cell is "according as to whether arrest may be made without warrant for the offence or not" for s 195 but "May arrest without warrant" for ss 196 to 200; confirm that is as intended and not an extraction of one cell.
- s 376EB(3)(a) and the like are stored with their subsection; sections whose subsections the Penal Code renumbers will need the lookup by `base section`.
