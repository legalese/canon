# Coverage - documents-defamation (Chapters 18, 20, 21, 22; ss 463-510)

Every section in the four Chapters has a row: 45 sections plus the numbering gaps the Code itself records.
Source: `inputs/PC1871.txt` lines 11765-12526 (Chapter 18 to the end of Chapter 22).

**Modules** (all in `deposit/`; the group is split by the Code's own parts, notes/PLAN.md §1):

| module | covers |
| --- | --- |
| `pc-documents-defamation-common.l4` | two builders for the two punishment shapes the group uses; no section |
| `pc-documents-defamation-forgery.l4` | Chapter 18 "Forgery", ss 463-477A |
| `pc-documents-defamation-currency.l4` | Chapter 18 "Currency and bank notes", ss 489A-489I |
| `pc-documents-defamation-defamation.l4` | Chapter 20 (repealed), Chapter 21, ss 493-502 |
| `pc-documents-defamation-intimidation.l4` | Chapter 22, ss 503-510 |
| `pc-documents-defamation-tests.l4` | the tests for all of the above |

**Measured** on the toolchain in `BRIEF.md`, `JL4_LIBRARY_PATH` unset, 2026-09-26: every module 0 errors, 0 warnings; the tests module 172 assertions satisfied, 0 failed, out of 172 `#ASSERT` lines.
A positive control (two expectations flipped, in a scratch copy) reported 2 failed, so the harness can fail.

**Every offence row with a charge has all four contract items**: facts record, defining predicate, `offence under s N`, `charge under s N`, each `@export` with `@desc`.
Where the defining and the punishing section are one (s 471, s 504 and most of Chapter 18), the `offence under s N` ladder IS the defining predicate; there is no separate verb-named function.

| s | heading | disposition | functions |
| --- | --- | --- | --- |
| 463 | Forgery | encoded (definition) | `commits forgery` over `Forgery Facts` |
| 464 | Making a false document or false electronic record | encoded (definition, with Explanations 1-2 in the leaf @desc; (2) in @desc) | `makes a false document or false electronic record` |
| 465 | Punishment for forgery | encoded | `offence under s 465`, `charge under s 465`, `punishment prescribed by s 465` |
| 466 | Forgery of a record of a court of justice, or a public register of births, etc. | encoded | `the document is of a description mentioned in section 466`, `offence under s 466`, `charge under s 466`, `punishment prescribed by s 466` |
| 467 | Forgery of a valuable security or will | encoded | `the document is of a description mentioned in section 467`, `offence under s 467`, `charge under s 467`, `punishment prescribed by s 467` |
| 468 | Forgery for the purpose of cheating | encoded | `offence under s 468`, `charge under s 468`, `punishment prescribed by s 468` |
| 469 | Forgery for the purpose of harming the reputation of any person | encoded | `offence under s 469`, `charge under s 469`, `punishment prescribed by s 469` |
| 470 | "A forged document" or "a forged electronic record" | encoded (definition only; no charge) | `a forged document or forged electronic record within section 470` |
| 471 | Using as genuine a forged document or forged electronic record | encoded | `offence under s 471`, `charge under s 471`, `the punishment under s 471` (chooses s 465/466/467's) over `Forged Document Facts` |
| 472 | Making or possessing a counterfeit seal, plate, etc., with intent to commit a forgery punishable under s 467 | encoded | `offence under s 472`, `charge under s 472`, `punishment prescribed by s 472` over `Counterfeit Seal Facts` |
| 473 | ... with intent to commit a forgery punishable otherwise | encoded | `offence under s 473`, `charge under s 473`, `punishment prescribed by s 473` |
| 473A | Making or possessing equipment for making a false instrument | encoded | `offence under s 473A`, `charge under s 473A`, `punishment prescribed by s 473A` over `False Instrument Equipment Facts` |
| 473B | ... with intent to induce prejudice | encoded | `offence under s 473B`, `charge under s 473B`, `punishment prescribed by s 473B` |
| 473C | Meaning of "prejudice" and "induce" | encoded (definition only; no charge) - (1), (2), (4) on the ladder; (3) and (5) widen leaves (@desc) | `to a person's prejudice within section 473C` over `Prejudice Facts` |
| 474 | Having possession of certain document or electronic record known to be forged, with intent to use it as genuine | encoded; two punishments (s 466 / s 467 descriptions) | `offence under s 474`, `charge under s 474`, `the punishment under s 474`, `punishment prescribed by s 474, for a document of a description in section 466` / `... 467` |
| 475 | Counterfeiting a device or mark used for authenticating documents described in s 467, or possessing counterfeit marked material | encoded | `offence under s 475`, `charge under s 475`, `punishment prescribed by s 475` over `Counterfeit Mark Facts` |
| 476 | ... documents or electronic records other than those described in s 467 | encoded | `offence under s 476`, `charge under s 476`, `punishment prescribed by s 476` |
| 477 | Fraudulent cancellation, destruction, etc., of a will | encoded | `offence under s 477`, `charge under s 477`, `punishment prescribed by s 477` over `Will or Security Destruction Facts` |
| 477A | Falsification of accounts | encoded (Explanation 1 as a pleading rule in the recital; Explanation 2 in @desc) | `offence under s 477A`, `charge under s 477A`, `punishment prescribed by s 477A` over `Falsification of Accounts Facts` |
| 478-489 | [There are no sections 478 to 489] | none exist - a comment in the forgery module's header | - |
| 489A | Forging or counterfeiting currency or bank notes; (2) "bank note", "coin", "currency" | encoded | `offence under s 489A`, `charge under s 489A`, `punishment prescribed by s 489A`; (2): `bank note within section 489A(2)`, `coin within section 489A(2)`, `currency within section 489A(2)` over `Currency Description Facts` |
| 489B | Using as genuine forged or counterfeit currency or bank notes | encoded | `offence under s 489B`, `charge under s 489B`, `punishment prescribed by s 489B` over `Currency Facts` |
| 489C | Possession of forged or counterfeit currency or bank notes | encoded | `offence under s 489C`, `charge under s 489C`, `punishment prescribed by s 489C` |
| 489D | Making or possessing instruments or materials for forging or counterfeiting currency or bank notes | encoded | `offence under s 489D`, `charge under s 489D`, `punishment prescribed by s 489D` |
| 489E | Abetting in Singapore counterfeiting of currency out of Singapore | encoded; punishment by reference to abetment, carried as the section's words (no `Punishment` record - FORK DD-15) | `offence under s 489E`, `charge under s 489E` |
| 489F | Fraudulently or dishonestly diminishing weight or altering composition of any coin | encoded (Explanation in @desc) | `offence under s 489F`, `charge under s 489F`, `punishment prescribed by s 489F` |
| 489G | Altering appearance of currency with intent that it shall pass as currency of different description | encoded | `offence under s 489G`, `charge under s 489G`, `punishment prescribed by s 489G` |
| 489H | Delivery to another of altered currency | encoded | `offence under s 489H`, `charge under s 489H`, `punishment prescribed by s 489H` |
| 489I | Possession of altered currency | encoded | `offence under s 489I`, `charge under s 489I`, `punishment prescribed by s 489I` |
| Ch 19 | [There is no Chapter 19] | none exists | - |
| 493 | [Repealed by Act 15 of 2019] | repealed - comment in place | - |
| 494 | [Repealed by Act 15 of 2019] | repealed - comment in place | - |
| 495 | [Repealed by Act 15 of 2019] | repealed - comment in place | - |
| 496 | [Repealed by Act 15 of 2019] | repealed - comment in place | - |
| 497 | [There is no section 497] | none exists - comment in place | - |
| 498 | [Repealed by Act 51 of 2007] | repealed - comment in place | - |
| 499 | Defamation (Explanations 1-5, First to Tenth Exceptions, Explanation to Exceptions) | encoded (definition): the Exceptions are on the ladder as one call; Explanations 2, 3, 5 widen leaves; 4 is a leaf; 1 is an alternative limb | `defames`, `the imputation falls within an Exception to s 499` over `Defamation Facts` |
| 500 | Punishment for defamation | encoded | `offence under s 500`, `charge under s 500`, `punishment prescribed by s 500` |
| 501 | Printing or engraving matter known to be defamatory | encoded | `offence under s 501`, `charge under s 501`, `punishment prescribed by s 501` over `Defamatory Matter Facts` |
| 502 | Sale of printed or engraved substance containing defamatory matter | encoded | `offence under s 502`, `charge under s 502`, `punishment prescribed by s 502` |
| 503 | Criminal intimidation | encoded (definition; Explanation in @desc) - the reference row's ladder, unchanged | `commits criminal intimidation` over `Criminal Intimidation Facts` |
| 504 | Intentional insult with intent to provoke a breach of the peace | encoded | `offence under s 504`, `charge under s 504`, `punishment prescribed by s 504` over `Intentional Insult Facts` |
| 505 | Statements conducing to public mischief (with its Exception) | encoded | `offence under s 505`, `charge under s 505`, `punishment prescribed by s 505`, `the Exception to s 505 applies`, `with any intent mentioned in section 505` over `Public Mischief Statement Facts` |
| 506 | Punishment for criminal intimidation | encoded - one offence, two punishments (reference row) | `offence under s 506`, `charge under s 506`, `the threat falls within the aggravated limb of s 506`, `punishment prescribed by s 506`, `punishment prescribed by s 506, where the threat is to cause death, grievous hurt, destruction by fire or a serious offence`, threshold helper `punishable with death or with imprisonment for a term which may extend to 7 years or more` |
| 507 | Criminal intimidation by an anonymous communication | encoded | `offence under s 507`, `charge under s 507`, `punishment prescribed by s 507` (same facts record as s 506) |
| 508 | [Repealed by Act 15 of 2019] | repealed - comment in place | - |
| 509 | [Repealed by Act 15 of 2019] | repealed - comment in place | - |
| 510 | [Repealed by Act 5 of 2015] | repealed - comment in place | - |

Nothing is `deferred`.

## Illustrations: which are tests, and which are not

| Illustration | test? |
| --- | --- |
| s 464 illus (a)-(k) | all eleven asserted (`offence under s 465`; s 467 too where the document is a valuable security or will) |
| s 464 Explanation 1 illus (a)-(e) | all five asserted. Illus (b)'s second sentence (B, knowingly drawing the bill, "is also guilty of forgery") is the same ladder on B's facts and is not separately asserted |
| s 464 Explanation 2 illus | asserted |
| s 489F Explanation (scooping) | asserted |
| s 499 illus (a)-(c) | asserted |
| s 499 Third Exception illus; Fifth (a), (b); Sixth (d); Seventh; Eighth; Ninth (a) | asserted |
| s 499 Sixth Exception illus (a)-(c) (a book, a speech, a stage performance submit to public judgment) | not separately asserted: each widens the Sixth Exception's leaf (its @desc) rather than deciding a case; (d) and (e) exercise the leaf |
| s 499 Sixth Exception illus (e); Ninth illus (b) | (e) is the same shape as Fifth (b) (opinion not founded on the performance: leaf FALSE), covered by that test; Ninth (b) is the same leaf as Ninth (a) |
| s 503 illus | asserted, with its charge text |

## What the ladders read from other groups (cross-module joins owed)

| leaf | in record | section | owner | edge on PLAN §1's list? |
| --- | --- | --- | --- | --- |
| `grievous hurt` | `Criminal Intimidation Facts` | s 320 | body-a | **no** - `documents-defamation -> body-a` is needed for s 506 |
| `intending that the document forged shall be used for the purpose of cheating` | `Forgery Facts` | s 415 | property | yes (s 468 reads s 415). It is an intention, so it stays a leaf even at integration |
| `commits mischief in respect to such document` | `Will or Security Destruction Facts` | s 425 | property | **no** - s 477 reads s 425 too |
| `makes or abets ...`, `omits or alters or abets ...` | `Falsification of Accounts Facts` | s 107 | general-part | yes |
| `abets the counterfeiting of any currency out of Singapore` | `Currency Facts` | s 107, ss 109-117 | general-part | yes |
| the (a)-(b) intents and effects of s 505 | `Public Mischief Statement Facts` | s 140B; Chapter 6 (offences against the State); Chapter 8 (public tranquillity) | state-public | **no** - `documents-defamation -> state-public` needed for s 505 |

## DEFINITION_LADDERS entries (drill-downs for flat leaves)

`{ fn: 'dishonestly within section 24', leaf: 'dishonestly', section: '24' }`, `{ fn: 'fraudulently within section 25', leaf: 'fraudulently', section: '25' }` (ss 464, 471, 477, 489F);
`{ fn: 'counterfeits within section 28', leaf: 'forges or counterfeits', section: '28' }`;
`{ fn: 'valuable security within section 30', leaf: 'purports to be a valuable security', section: '30' }`; `{ fn: 'a will within section 31', leaf: 'purports to be a will', section: '31' }`;
`{ fn: 'public servant within section 21', leaf: 'purports to be a certificate or document made by a public servant in his official capacity', section: '21' }`;
`{ fn: 'to a person\'s prejudice within section 473C', leaf: 'intends that by reason of so accepting it, that person does or does not do some act to his or any other person\'s prejudice', section: '473C' }`;
`{ fn: 'currency within section 489A(2)', leaf: 'currency or a bank note', section: '489A(2)' }` and `bank note within section 489A(2)` beside it.
