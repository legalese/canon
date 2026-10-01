# Prevention of Corruption Act 1960 — encoding notes

Source: Singapore Statutes Online, 2020 Revised Edition, current version as at 01 Oct 2026 (`../source/PCA1960.pdf`; `PCA1960.txt` is the reading copy whose line numbers the modules cite). An unofficial consolidation (SSO Terms of Use cl.8). One vintage.

## 1. What is encoded and what is not

The Act's Parts 1 and 3 to 6 in full, and ss 3 and 4 of Part 2, organised by the question a prosecutor asks:

| question | module |
| --- | --- |
| Is this an offence under the Act (ss 5 to 12, 18(2), 21(2), 26, 28, 32(2); abetment, attempt, conspiracy 29 to 31), and what is the most it can cost (ss 5, 6, 7, 10 to 12, 13, 18(2), 21(2), 26, 28, 32(2))? | `pca-offences.l4` |
| What may the court hear, and what may it make of it (ss 23, 24, 25, 36)? | `pca-evidence.l4` |
| Who may do what to whom (ss 3, 4, 15 to 22), and how is the case brought (ss 32 to 35, 37)? | `pca-procedure.l4` |

**Not encoded:** ss 4A to 4F, the Occupational Superannuation Scheme for CPIB officers appointed on or after 1 November 2001 (pension, gratuity, bankruptcy and conviction effects on benefits, the INVEST Fund). It is pension administration with no bearing on a prosecution. s 15A (arms for CPIB officers) is inert.

**The Act has no minimum penalty for any offence.** Every figure in `the punishment for the offence` is a maximum.

## 2. Coverage table

| provision | heading | disposition | module |
| --- | --- | --- | --- |
| 1 | Short title | inert | — |
| 2 | Interpretation: "gratification", "agent" | encoded (`the thing is a gratification`, `the person is an agent`, `… for the purposes of section 8`) | offences |
| 2 | "CPIB officer", "Director", "INVEST Fund", "member", "Scheme", "service" | inert (Part 2 administration) | — |
| 2 | "principal", "public body", "special investigator" | used as facts, not rules (the witness can say whether the body is a public body; fork F10) | types |
| 3(3), (4) | deputy and assistant directors | encoded | procedure |
| 3(1), (2), (5) | appointment and grades by the President | inert | — |
| 4(1) | officers deemed public servants (Penal Code 1871) | encoded | procedure |
| 4(2) | warrant card is evidence of appointment | inert | — |
| 4A to 4F | the Scheme | out-of-scope (above) | — |
| 5(a), (b) | corruption | encoded | offences |
| 6(a), (b), (c) | corrupt transactions with agents | encoded | offences |
| 7 | increase of maximum penalty | encoded | offences |
| 8 | presumption of corruption | encoded | offences |
| 9(1), (2) | guilty notwithstanding that purpose not carried out | encoded | offences |
| 10, 11, 12 | tenders; Member of Parliament; member of a public body | encoded | offences |
| 13(1), (2) | penalty in addition | encoded | offences |
| 14 | principal may recover | encoded | offences |
| 15(1), (2), (3) | arrest; search of the arrested; where taken | encoded | procedure |
| 15A | arms | inert | — |
| 16 | bail or bond | encoded (16(2) states the Code's Division 5 applies; the Code's bail rules are not encoded here) | procedure |
| 17(1), (2) | powers of investigation without the Public Prosecutor's order; deemed rank | encoded | procedure |
| 18(1), (2) | special powers of investigation; failure to disclose | encoded | procedure; offences |
| 19 | investigation authorised by the Public Prosecutor | encoded | procedure |
| 20 | bankers' books | encoded as the order's conditions (the inspection itself is inert) | procedure |
| 21(1), (2) | Public Prosecutor's powers to obtain information; failure to comply | encoded at the threshold; the six kinds of notice are not enumerated (fork F9) | procedure; offences |
| 22(1), (2) | search and seizure | encoded | procedure |
| 23 | evidence of custom inadmissible | encoded | evidence |
| 24(1), (2) | disproportionate pecuniary resources | encoded | evidence |
| 25 | evidence of accomplice | encoded | evidence |
| 26 | obstruction of search | encoded | offences |
| 27 | legal obligation to give information | encoded | offences |
| 28 | false statements | encoded | offences |
| 29, 30, 31 | abetment, attempts, conspiracy | encoded | offences |
| 32(1) | every offence deemed arrestable | encoded, and handed to the Code | procedure |
| 32(2) | public officer failing to arrest | encoded | offences |
| 33 | consent of the Public Prosecutor | encoded | procedure |
| 34 | District Court has full jurisdiction | encoded, and handed to the Code | procedure |
| 35(1), (3) | examination of offenders; certificate of indemnity | encoded; 35(2) (refusal to be sworn dealt with as for other witnesses) inert | procedure |
| 36(1), (3) | protection of informers | encoded; 36(2) (the court conceals entries "but no further") inert | evidence |
| 37(1) | citizens abroad | encoded; 37(2) (bar to extradition) inert | procedure |

No row is `deferred`.

## 3. Files

| file | what it is |
| --- | --- |
| `pca-types.l4` | the nouns: one record of facts per provision |
| `pca-offences.l4`, `pca-evidence.l4`, `pca-procedure.l4` | the rules |
| `written-law-interface.l4` | DECLARE-only; **identical in this row, `sg/criminal-procedure-code-2010` and `sg/misuse-of-drugs-act-1973`** (section 4) |
| `pca-tests-offences.l4` (361), `pca-tests-evidence.l4` (24), `pca-tests-procedure.l4` (181) | tests **generated** by `generators/pca_tests_1.py` and `pca_tests_2.py` from the Act's text, using `generators/fixtures.py` |
| `check.sh` | runs every module and compares the interface module with the copies in the sibling subjects |

## 4. Cross-subject references: what the Act points at, and how each is represented

`l4` resolves an `IMPORT` only to a module in the importing file's directory (or the project root, or the embedded library), so **no module in this row can import a rule from another subject**. Each reference is therefore represented in one of three ways: a fact the caller supplies; the interface record `Written Law Procedure Statement`; or a list of section numbers. Nothing was invented beyond the one interface record the Code row already uses for the Evidence Act.

| the Act says | in | how it is represented here | where the other side is |
| --- | --- | --- | --- |
| every offence is "an arrestable offence for the purposes of the Criminal Procedure Code 2010" (s 32(1)); a District Court may try it and award the full punishment (s 34) | PCA | `the Prevention of Corruption Act 1960's statement about its offences` (a `Written Law Procedure Statement`) | `sg/criminal-procedure-code-2010`, `cpc-other-laws.l4`, which reads it |
| the Act is listed at item 16A of the Second Schedule | CPC | not restated here | `cpc-second-schedule.l4`; `cpc-tests-other-laws.l4` tests it with the Act's statement |
| "powers in relation to police investigations given by the Criminal Procedure Code 2010" (ss 17, 19); ss 20(1), 23, 148, 258 of the Code named (ss 13(2), 17(1) proviso, 17(2)) | PCA | facts and comments: the Code's rules are not encoded for those sections | CPC row: Part 3 and Part 14 not encoded |
| Division 5 of Part 6 of the Code (bail) applies (s 16(2)) | PCA | stated in a comment; the bail rules are the Code's | CPC row: not encoded |
| Penal Code ss 161 to 165, 213 to 215 (ss 17(1)(a), 20, 21, 22, 24, 28, 35) | PCA | **three differently drawn lists**: `the Penal Code sections named in sections 17(1)(a) and 28(a)` (165, 213, 214, 215) and `… in sections 20, 21, 22, 24 and 35` (161 to 165, 213 to 215); a reader who takes them as one list will think s 28(a) reaches ss 161 to 164, which it does not | `sg/penal-code-1871` (ss 161 to 165 in its public-servants module) |
| "abets" and "criminal conspiracy" "within the meaning of the Penal Code 1871" (ss 29, 31) | PCA | facts (`the accused abetted, within the meaning of the Penal Code 1871, …`) | `sg/penal-code-1871` Chapters 5 and 5A |
| officers "deemed to be public servants within the meaning of the Penal Code 1871" (s 4(1)) | PCA | `the officer is deemed a public servant within the meaning of the Penal Code 1871` | `sg/penal-code-1871` s 21 |
| the Penal Code's Schedule item 15 (s 4B) excludes offences "under the Prevention of Corruption Act 1960" | Penal Code | the whole-code row's flag `is an offence under the Prevention of Corruption Act 1960 or the Securities and Futures Act 2001` is an input; a comment there now points here | `sg/penal-code-1871/encodings/legalese-whole-code/pc-general-part.l4` |
| "proved" (s 8: "unless the contrary is proved") | PCA | the accused's rebuttal is a fact (`the contrary is proved`); the standard is not encoded | Evidence Act s 3 ("proved"), `sg/evidence-act-1893` |
| a witness who paid is not presumed unworthy of credit "by reason only" (s 25) | PCA | `the witness may not be presumed unworthy of credit by reason only of the payment` | Evidence Act s 116 illustration (b): the court "may" presume an accomplice unworthy of credit unless corroborated; s 25 is the Act's exception in a corruption trial |
| complaints and informers (s 36) | PCA | `the court may require disclosure concerning the informer under section 36(3)` | Evidence Act s 126 (public officer not compelled to disclose communications made to him) and s 127 (a Magistrate or police officer not compelled to say whence he got information as to the commission of an offence); the Misuse of Drugs Act s 23 is the counterpart in that Act |
| s 24: disproportionate resources "may be taken into consideration … as corroborating the testimony of any witness" | PCA | a conclusion, not a presumption (it does not shift a burden) | Evidence Act s 116 illustration (b) (corroboration of an accomplice) |

**What the existing mechanism does not support, and what is therefore not done.** The Code's own rules of arrest, bail, investigation and warrants for an offence "under this Act" cannot be called from this row; the Act's statement hands the Code the two answers it needs (arrestable; District Court), and the Code row then applies its own rules to the punishment this row computes. The exact cross-reference that would need a real cross-subject import to be represented as a rule and not as an input: **the Code's `the procedural treatment of an offence under the Act` reading `the punishment for the offence` from this row** (today the caller passes the maximum term as a fact).

## 5. Fork register

| id | where the text is ambiguous or silent | reading taken | text |
| --- | --- | --- | --- |
| F1 | "corruptly" (ss 5, 6, 9) is not defined | a fact about the accused, not decided by the encoding | s 5 "corruptly solicit"; the Act has no definition |
| F2 | s 8 "deemed … corruptly as an inducement or reward as hereinbefore mentioned" | supplies the corrupt element and the purpose limb of ss 5 and 6; does not supply that the thing is a gratification or was in fact paid; computed once (`the presumption of section 8 operates`) and entered as a BOOLEAN input to each offence rule | s 8, "it is proved that any gratification has been paid or given to or received by" |
| F3 | s 9: the four "notwithstanding" facts | fields, so a test shows they are not read | s 9(1), (2) |
| F4 | s 3(3), (4): deputy and assistant directors | may exercise the powers conferred on the Director or a special investigator; the Act's sections name "the Director or any special investigator" | s 3(3), (4) |
| F5 | three lists of Penal Code sections | kept as three | ss 17(1)(a), 28(a) against ss 20, 21, 22, 24, 35 |
| F6 | s 7: the enhanced penalty | raises only the imprisonment ceiling (5 to 7 years); the fine ceiling is $100,000 in both | s 7 |
| F7 | s 13(1): "an offence committed by the acceptance of any gratification" | 5(a), 6(a), 10(b), 11(b), 12(b); not 6(c) (a false document), not the giving offences | s 13(1) |
| F8 | s 32(1) and the Code | the statement says `deems … arrestable` TRUE and `empowers the police` FALSE (s 15(1) empowers the Director and special investigators, not the police) | ss 15(1), 32(1) |
| F9 | s 21(1)(a) to (f): six kinds of notice | the threshold (service of the person, kind of offence) is encoded; the kinds are not enumerated because no rule depends on which was asked for | s 21(1) |
| F10 | "public body", "principal", "special investigator" | facts: whether a body is a public body is something a witness says | s 2 |
| F11 | s 36(1) "no witness shall be obliged or permitted to disclose" | the rule asks only when the court may require disclosure (s 36(3)); it does not model the prohibition separately | s 36 |
| F12 | s 35(3) "in the opinion of the court" | a fact about the court's opinion | s 35(3) |

## 6. The punishments, by provision

All maxima; none of the Act's provisions prints a minimum. "Fine and/or imprisonment" is "or … or both".

| offence | provision | fine not exceeding | imprisonment not exceeding |
| --- | --- | --- | --- |
| corruption: 5(a), 5(b) | s 5 | $100,000 | 5 years |
| corrupt transactions with agents: 6(a), (b), (c) | s 6 | $100,000 | 5 years |
| 5 or 6 where the matter was a contract or proposal for a contract with the Government, a department or a public body, or a subcontract | s 7 | $100,000 | 7 years |
| withdrawal of tenders 10(a), (b); Member of Parliament 11(a), (b); member of a public body 12(a), (b) | ss 10, 11, 12 | $100,000 | 7 years |
| failure to disclose or produce under a Public Prosecutor's order | s 18(2) | $2,000 | 1 year |
| failure to comply with the Public Prosecutor's notice | s 21(2) | $10,000 | 1 year |
| obstruction of search | s 26 | $10,000 | 1 year |
| false or misleading information | s 28 | $10,000 | 1 year |
| public officer failing to arrest the giver | s 32(2) | $5,000 | 6 months |
| abetment, attempt, conspiracy | ss 29, 30, 31 | as for the offence | as for the offence |
| the penalty on acceptance of a gratification | s 13(1) | a sum equal to the gratification or its assessed value, recoverable as a fine, **in addition**; s 13(2): increased by up to the gratification in offences taken into consideration | — |

## 7. What `check.sh` prints

```
module                                    errors satisfied  failed
pca-evidence.l4                                0         0       0
pca-offences.l4                                0         0       0
pca-procedure.l4                               0         0       0
pca-tests-evidence.l4                          0        24       0
pca-tests-offences.l4                          0       361       0
pca-tests-procedure.l4                         0       181       0
pca-types.l4                                   0         0       0
written-law-interface.l4                       0         0       0
TOTAL (8 modules)                              0       566       0
```

No assertion is expected to fail. The tests' expected values were written from the Act's text by the same session that wrote the rules; **no independent test pass has been run** (the encoding-a-subject skill's step 8), and no domain expert has read the modules against the Act (gate HG1). Both are the next steps.

## 8. Open questions for a domain expert

- Does the s 8 presumption reach an offence under s 5 where the recipient is in the Government's employment but the giver has no "dealing" with it yet (the giver "seeks to have" one)? The encoding follows the words: "has or seeks to have".
- Is the s 24 corroboration rule available for the Penal Code offences in the list of ss 161 to 165, 213 to 215 only when the trial is of one of those, or also in a trial under the Act that merely involves one? The encoding follows the words (a trial "into" one of them).
- s 17(1): "may, without the order of the Public Prosecutor, exercise all or any of the powers … given by the Criminal Procedure Code 2010" for an arrestable offence "disclosed in the course of an investigation under this Act": does "disclosed" require that the offence be unforeseen? Not encoded: a fact.
- Whether s 14's civil debt is available against both agent and giver at once. The encoding allows either as defendant.
