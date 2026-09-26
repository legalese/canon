# Coverage — Chapter 17, Offences against property (ss 378-462)

Source: `inputs/PC1871.txt`, Chapter 17 at line 10213, Chapter 18 at line 11765.
Modules (all in `deposit/`):

| module | covers | facts records |
| --- | --- | --- |
| `pc-property-theft.l4` | ss 378-402 | `Theft Facts`, `Extortion Facts`, `Robbery Facts` (nests a theft and an extortion), `Gang Facts` |
| `pc-property-trust.l4` | ss 403-414 | `Misappropriation Facts`, `CBT Facts`, `Stolen Property Facts` |
| `pc-property-cheating.l4` | ss 415-424B | `Cheating Facts`, `Personal Information Facts`, `Services Facts`, `Fraudulent Disposition Facts`, `Fraud by False Representation Facts` |
| `pc-property-mischief.l4` | ss 425-462 | `Mischief Facts`, `Criminal Trespass Facts`, `Found Armed Facts`, `Receptacle Facts` |
| `pc-property-tests.l4` | tests for all four | 98 fixtures, 195 assertions |

The section text quoted above each rule is copied from the source by a script, not retyped.
The same script writes every `punishment prescribed by s N` record from one table.

**What `l4 run` prints** (toolchain `l4-unstable-20260926-c76e6b0`, `JL4_LIBRARY_PATH` unset, counted with `deposit/check.sh`'s anchored patterns):

| module | errors | warnings | assertions satisfied | failed |
| --- | --- | --- | --- | --- |
| `pc-property-theft.l4` | 0 | 0 | 0 | 0 |
| `pc-property-trust.l4` | 0 | 0 | 0 | 0 |
| `pc-property-cheating.l4` | 0 | 0 | 0 | 0 |
| `pc-property-mischief.l4` | 0 | 0 | 0 | 0 |
| `pc-property-tests.l4` | 0 | 0 | 195 | 0 |

The tests file carries 195 `#ASSERT` lines, and 195 are satisfied.
Positive control: two deliberately false assertions appended to a copy of the tests (`commits theft` on illustration (i); `offence under s 420(1)` on the fraudulently-only fixture) both came back `assertion failed`, so the harness can fail.
There are no expected failures.

Dispositions: `encoded` (a ladder and, for a punishing section, `offence under s N` + `charge under s N` + `punishment prescribed by s N`, all `@export`ed with `@desc`), `encoded (definition)` (a defining section: its predicate is exported; there is no charge under it, because a charge is laid under the punishing section), `repealed`, `none` (no such section).
No row is `deferred`.

## Theft (ss 378-382) — `pc-property-theft.l4`, `Theft Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 378 | Theft | encoded (definition) | `commits theft` | (a), (d), (e), (g), (h), (i), (j), (k), (m), (p), (q) — see note T-1 |
| 379 | Punishment for theft | encoded | `offence under s 379`, `charge under s 379`, `punishment prescribed by s 379` | illus (q) charge text byte-for-byte (reference row) |
| 379A | Punishment for theft of a motor vehicle | encoded | `offence under s 379A`, `charge under s 379A`, `punishment prescribed by s 379A` | — (no illustrations); car, tyre, neither |
| 380 | Theft in dwelling house, etc. | encoded | `offence under s 380`, `charge under s 380`, `punishment prescribed by s 380` | — ; shop, open air, building used for neither |
| 381 | Theft by clerk or servant of property in possession of master | encoded | `offence under s 381`, `charge under s 381`, `punishment prescribed by s 381` | s 378 illus (d) |
| 382 | Theft after preparation made for causing death or hurt in order to commit theft | encoded | `offence under s 382`, `charge under s 382`, `punishment prescribed by s 382` | (a), (b) |

T-1. Illustrations (b) (the dog and the bait), (f) (the ring in Z's house), (l) (ransom for a reward), (n) (alms from Z's wife) and (o) (the paramour) reduce to the same all-TRUE or one-leaf-FALSE patterns already asserted; they are covered in the `@desc` of the leaf they turn on rather than asserted separately. Illustration (c) is deleted by Act 51 of 2007.

## Extortion (ss 383-389) — `Extortion Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 383 | Extortion | encoded (definition) | `commits extortion` | (a), (b), (c), (d) |
| 384 | Punishment for extortion | encoded | `offence under s 384`, `charge under s 384`, `punishment prescribed by s 384` | charge text; refusal |
| 385 | Putting person in fear of harm in order to commit extortion | encoded | `offence under s 385`, `charge under s 385`, `punishment prescribed by s 385` | threat with no delivery |
| 386 | Extortion by putting a person in fear of death or grievous hurt | encoded | `offence under s 386`, `charge under s 386`, `punishment prescribed by s 386` | s 383 illus (d) |
| 387 | Putting person in fear of death or of grievous hurt in order to commit extortion | encoded | `offence under s 387`, `charge under s 387`, `punishment prescribed by s 387` | death threat, no delivery |
| 388 | Extortion by threat of accusation of an offence punishable with death, or imprisonment, etc. | encoded | `offence under s 388`, `charge under s 388`, `punishment prescribed by s 388` | — |
| 389 | Putting person in fear of accusation of offence, in order to commit extortion | encoded | `offence under s 389`, `charge under s 389`, `punishment prescribed by s 389` | s 389 lacks s 388's "attempted to induce" limb |

## Robbery and gang-robbery (ss 390-402) — `Robbery Facts`, `Gang Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 390 | Robbery (with "When theft is robbery", "When extortion is robbery") | encoded (definition) | `commits robbery`, `theft is robbery`, `extortion is robbery` | (a), (b), (c), (d) |
| 391 | Gang-robbery | encoded (definition) | `commits gang-robbery`, `5 or more persons` (threshold helper) | boundary 4 / 5 |
| 392 | Punishment for robbery | encoded | `offence under s 392`, `charge under s 392`, `punishment prescribed by s 392`, `punishment prescribed by s 392, after 7 p.m. and before 7 a.m.` | both punishments; refusal on illus (d); Chen Weixiong Jerriek charge text byte-for-byte (reference row) |
| 393 | Attempt to commit robbery | encoded | `offence under s 393`, `charge under s 393`, `punishment prescribed by s 393` | attempt with hurt (also s 394) |
| 394 | Voluntarily causing hurt in committing robbery | encoded | `offence under s 394`, `charge under s 394`, `punishment prescribed by s 394` | hurt by accused; by a joint robber |
| 395 | Punishment for gang-robbery | encoded | `offence under s 395`, `charge under s 395`, `punishment prescribed by s 395` | 5 or more conjointly; an aider |
| 396 | Gang-robbery with murder | encoded | `offence under s 396`, `charge under s 396`, `punishment prescribed by s 396` | with and without the murder |
| 397 | Robbery when armed or with attempt to cause death or grievous hurt | encoded | `offence under s 397`, `charge under s 397`, `punishment prescribed by s 397` | armed, and not; fork P-5 |
| 398 | [There is no section 398.] | none | — | — |
| 399 | Making preparation to commit gang-robbery | encoded | `offence under s 399`, `charge under s 399`, `punishment prescribed by s 399` | — |
| 400 | Punishment for belonging to gang-robbers | encoded | `offence under s 400`, `charge under s 400`, `punishment prescribed by s 400` | gang-robbers vs thieves |
| 401 | Punishment for belonging to gang of thieves | encoded | `offence under s 401`, `charge under s 401`, `punishment prescribed by s 401` | thieves vs gang-robbers |
| 402 | Assembling for purpose of committing gang-robbery | encoded | `offence under s 402`, `charge under s 402`, `punishment prescribed by s 402` | — |

## Criminal misappropriation (ss 403-404) — `pc-property-trust.l4`, `Misappropriation Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 403 | Dishonest misappropriation of property | encoded | `dishonestly misappropriates or converts to his own use` (defining predicate), `offence under s 403`, `charge under s 403`, `punishment prescribed by s 403` | (a), (c) both halves; Explanation 2 illus (a), (g) |
| 404 | Dishonest misappropriation of property possessed by a deceased person at the time of his death | encoded | `offence under s 404`, `charge under s 404`, `punishment prescribed by s 404`, `punishment prescribed by s 404, clerk or servant` | the Illustration (the servant) |

Explanation 1 (a misappropriation for a time only) and Explanation 2 (the finder) ride in the `dishonestly` leaf's `@desc`: they say when the act is dishonest, which is a fact the investigator answers.
Explanation 2's illustrations (b)-(f) are further instances of the all-TRUE pattern asserted by (g).

## Criminal breach of trust (ss 405-409) — `CBT Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 405 | Criminal breach of trust | encoded (definition) | `commits criminal breach of trust` | (a), (b), (c), (d), (e), (f) |
| 406 | Punishment of criminal breach of trust | encoded | `offence under s 406`, `charge under s 406`, `punishment prescribed by s 406` | charge text; refusal on (d) |
| 407 | Criminal breach of trust of property entrusted for purposes of transportation or storage | encoded | `offence under s 407`, `charge under s 407`, `punishment prescribed by s 407` | the Illustration; s 405 illus (b), (f) |
| 408 | Criminal breach of trust by employees | encoded | `offence under s 408`, `charge under s 408`, `punishment prescribed by s 408` | — |
| 409 | Criminal breach of trust by public servant, or by banker, merchant, agent, director, officer, partner, key executive or fiduciary | encoded | `entrusted in a capacity within section 409(1)`, `offence under s 409`, `charge under s 409`, `punishment prescribed by s 409` | s 405 illus (a) (executor = fiduciary), (c) (agent), (e) (public servant) |

s 408(2) and s 409(2)-(3) (who is an employee, director, officer, partner, key executive, fiduciary) ride in the `@desc` of the capacity leaves.

## Receiving stolen property (ss 410-414) — `Stolen Property Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 410 | Stolen property | encoded (definition) | `stolen property within section 410` | ceases on return to the person entitled |
| 411 | Receiving stolen property | encoded | `defence under s 411(3)`, `offence under s 411(1)`, `offence under s 411(2)`, `charge under s 411(1)`, `charge under s 411(2)`, `punishment prescribed by s 411(1)`, `punishment prescribed by s 411(2)` | the Illustration (reported fund transfer: defence); charge text |
| 412 | Receiving property stolen in the commission of a gang-robbery | encoded | `offence under s 412`, `charge under s 412`, `punishment prescribed by s 412` | the Illustration (jewels reported: defence) and its converse |
| 413 | Habitually dealing in stolen property | encoded | `offence under s 413`, `charge under s 413`, `punishment prescribed by s 413` | — |
| 414 | Assisting in concealment or disposal of stolen property | encoded | `offence under s 414(1)`, `offence under s 414(2)`, `charge under s 414(1)`, `charge under s 414(2)`, `punishment prescribed by s 414(1)`, `punishment prescribed by s 414(2)` | — |

## Cheating (ss 415-420A) — `pc-property-cheating.l4`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 415 | Cheating | encoded (definition) | `cheats` | (a)-(f), (h), (i) as one pattern; (g); (k); the second limb |
| 416 | Cheating by personation | encoded (definition) | `cheats by personation` | (a) |
| 416A | Illegally obtained personal information | encoded | `offence under s 416A`, `charge under s 416A`, `punishment prescribed by s 416A` (`Personal Information Facts`) | (1)(b) with knowledge; (1)(a) with no offence in view |
| 416B | Cheating by remote communication | encoded (definition) | `cheats by remote communication` | a scam call; a Minister-excluded system |
| 417 | Punishment for cheating | encoded | `offence under s 417`, `charge under s 417`, `punishment prescribed by s 417` | — |
| 418 | Cheating with knowledge that wrongful loss may be thereby caused to a person whose interest the offender is bound to protect | encoded | `offence under s 418`, `charge under s 418`, `punishment prescribed by s 418` | — |
| 419 | Punishment for cheating by personation | encoded | `offence under s 419`, `charge under s 419`, `punishment prescribed by s 419` | s 416 illus (a) |
| 420 | Cheating and dishonestly inducing a delivery of property | encoded | `offence under s 420(1)`, `offence under s 420(2)`, `charge under s 420(1)`, `charge under s 420(2)`, `punishment prescribed by s 420(1)`, `punishment prescribed by s 420(2)` | Lewis Christine charge text byte-for-byte (reference row) |
| 420A | Obtaining services dishonestly or fraudulently | encoded | `offence under s 420A`, `charge under s 420A`, `punishment prescribed by s 420A` (`Services Facts`) | the Illustration (the flight) |

s 416 illus (b) (pretending to be a deceased person) is the same leaf as (a).
s 415 illus (j) (false dice) is the all-TRUE first-limb pattern.

## Fraudulent deeds and dispositions of property (ss 421-424B)

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 421 | Dishonest or fraudulent removal or concealment of property to prevent distribution among creditors | encoded | `offence under s 421`, `charge under s 421`, `punishment prescribed by s 421` (`Fraudulent Disposition Facts`) | — |
| 422 | Dishonestly or fraudulently preventing a debt or demand due to the offender from being made available for his creditors | encoded | `offence under s 422`, `charge under s 422`, `punishment prescribed by s 422` | — (not tested) |
| 423 | Dishonest or fraudulent execution of deed of transfer containing a false statement of consideration | encoded | `offence under s 423`, `charge under s 423`, `punishment prescribed by s 423` | — |
| 424 | Dishonest or fraudulent removal or concealment of property or release of claim | encoded | `offence under s 424`, `charge under s 424`, `punishment prescribed by s 424` | release of claim needs dishonesty |
| 424A | Fraud by false representation, non-disclosure or abuse of position not connected with contracts for goods or services | encoded | `commits fraud by false representation, non-disclosure or abuse of position` (shared elements of 424A(1)/424B(1)), `offence under s 424A`, `charge under s 424A`, `punishment prescribed by s 424A` (`Fraud by False Representation Facts`) | — |
| 424B | Fraud by false representation, non-disclosure or abuse of position | encoded | `offence under s 424B`, `charge under s 424B`, `punishment prescribed by s 424B` | 424A vs 424B split on the goods-or-services contract |

## Mischief (ss 425-440) — `pc-property-mischief.l4`, `Mischief Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 425 | Mischief | encoded (definition) | `commits mischief` | (a), (c), (e), (g); a change that does not diminish value |
| 426 | Punishment for committing mischief | encoded | `offence under s 426`, `charge under s 426`, `punishment prescribed by s 426` | charge text |
| 427 | Punishment for committing mischief causing disruption to key service, etc. | encoded | `offence under s 427`, `charge under s 427`, `punishment prescribed by s 427` | (a), (c) |
| 428 | Mischief by killing or maiming any animal | encoded | `offence under s 428`, `charge under s 428`, `punishment prescribed by s 428` | — (not tested) |
| 429 | [Repealed by Act 51 of 2007] | repealed | — | — |
| 430 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 430A | [Repealed by Act 15 of 2019] | repealed | — | — |
| 431 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 431A | [Repealed by Act 15 of 2019] | repealed | — | — |
| 432 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 433 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 434 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 435 | Mischief by fire or explosive substance with intent to cause damage | encoded | `offence under s 435`, `charge under s 435`, `punishment prescribed by s 435` | — |
| 436 | Mischief by fire or explosive substance with intent to destroy a house, etc. | encoded | `offence under s 436`, `charge under s 436`, `punishment prescribed by s 436` | — (not tested) |
| 437 | Mischief with intent to destroy or make unsafe a decked vessel or a vessel of 20 tons burden | encoded | `20 tons or upwards` (threshold helper), `offence under s 437`, `charge under s 437`, `punishment prescribed by s 437` | boundary 19 / 20 |
| 438 | Punishment for the mischief described in section 437 when committed by fire or any explosive substance | encoded | `offence under s 438`, `charge under s 438`, `punishment prescribed by s 438` | committed; attempted |
| 439 | Punishment for intentionally running vessel aground or ashore with intent to commit theft, etc. | encoded | `offence under s 439`, `charge under s 439`, `punishment prescribed by s 439` | — (not tested) |
| 440 | Mischief committed after preparation made for causing death or hurt | encoded | `offence under s 440`, `charge under s 440`, `punishment prescribed by s 440` | — (not tested) |

s 425 illus (b) is deleted by Act 51 of 2007; (d) and (f) are the same pattern as (e) (damage to another through one's own or a shared property, Explanation 2).

## Criminal trespass (ss 441-462) — `Criminal Trespass Facts`, `Found Armed Facts`, `Receptacle Facts`

| s | heading | disposition | functions | illustrations tested |
| --- | --- | --- | --- | --- |
| 441 | Criminal trespass | encoded (definition) | `commits criminal trespass` | entry; remaining to annoy; entry with no intent (refusal) |
| 442 | House-breaking | encoded (definition) | `commits house-breaking` | — |
| 443 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 444 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 445 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 446 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 447 | Punishment for criminal trespass | encoded | `offence under s 447`, `charge under s 447`, `punishment prescribed by s 447` | 3 months / $1,500 |
| 448 | Punishment for house-breaking | encoded | `offence under s 448`, `charge under s 448`, `punishment prescribed by s 448` | — |
| 449 | House-breaking in order to commit an offence punishable with death | encoded | `offence under s 449`, `charge under s 449`, `punishment prescribed by s 449` | — (not tested) |
| 450 | House-breaking in order to commit an offence punishable with imprisonment for life | encoded | `offence under s 450`, `charge under s 450`, `punishment prescribed by s 450` | — (not tested) |
| 451 | House-breaking in order to commit an offence punishable with imprisonment | encoded | `offence under s 451`, `charge under s 451`, `punishment prescribed by s 451` | charge text |
| 452 | House-breaking after preparation made for causing hurt, etc. | encoded | `offence under s 452`, `charge under s 452`, `punishment prescribed by s 452` | — (not tested) |
| 453 | Possession of house-breaking implements or offensive weapons | encoded | `offence under s 453`, `charge under s 453`, `punishment prescribed by s 453` (`Found Armed Facts`) | armed; lawful purpose shown; s 453(3) presumption |
| 454 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 455 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 456 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 457 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 458 | [Repealed by Act 15 of 2019] | repealed | — | — |
| 458A | Punishment for subsequent offence under section 449, 450, 451 or 452 | encoded | `offence under s 458A`, `charge under s 458A` (framed "451 read with 458A" etc.), `punishment prescribed by s 458A` | section field |
| 459 | Grievous hurt caused while committing house-breaking | encoded | `offence under s 459`, `charge under s 459`, `punishment prescribed by s 459` | — |
| 460 | House-breaking when death or grievous hurt caused | encoded | `offence under s 460`, `charge under s 460`, `punishment prescribed by s 460` | — (not tested) |
| 461 | Dishonestly breaking open any closed receptacle containing or supposed to contain property | encoded | `offence under s 461`, `charge under s 461`, `punishment prescribed by s 461` (`Receptacle Facts`) | — |
| 462 | Punishment for same offence when committed by person entrusted with custody | encoded | `offence under s 462`, `charge under s 462`, `punishment prescribed by s 462` | — |

Rows marked "not tested" have no Illustration in the Code and got no scenario of mine in the time available; their ladders typecheck and their charges build, but no assertion exercises them.

## Cross-module joins owed

Each is a flat BOOLEAN leaf here whose `@desc` names the owning section and module.

| leaf (record) | reads | owner | sections here |
| --- | --- | --- | --- |
| `hurt` (Robbery) | s 319 hurt | body-a | 390(2) |
| `wrongful restraint`, `fear of instant wrongful restraint`, `instant wrongful restraint` (Robbery) | s 339 wrongful restraint | body-a | 390 |
| `voluntarily causes hurt` (Robbery) | s 321 | body-a | 394 |
| `causes grievous hurt to any person`, `attempts to cause death or grievous hurt to any person` (Robbery; Criminal Trespass) | s 320 grievous hurt | body-a | 397, 459 |
| `fear of grievous hurt` (Extortion) | s 320 | body-a | 386, 387 |
| `one of those persons commits murder in so committing gang-robbery` (Robbery) | s 300 murder | body-a | 396 |
| `having made preparation for causing death or hurt or restraint ...` (Theft), `... death or hurt or wrongful restraint ...` (Mischief), `... hurt ... assaulting ... wrongfully restraining ...` (Criminal Trespass) | ss 319, 339, 351 | body-a | 382, 440, 452 |
| `any person guilty of such house-breaking voluntarily causes or attempts to cause death or grievous hurt` (Criminal Trespass) | ss 320, 321/322 | body-a | 460 |
| `attempting to commit robbery` (Robbery), `attempts to commit such mischief` (Mischief) | s 511 attempt | general-part | 393, 394, 397, 438 |
| `in his capacity as a public servant` (CBT) | s 21 | pc-general (already shared) | 409(1)(a) |
| `in order to commit any offence punishable with death / imprisonment for life / imprisonment` (Criminal Trespass); `of having committed ... an offence punishable with death, or with imprisonment for life, or ... 10 years` (Extortion) | another offence's `Punishment`, via pc-general's `punishable with death or imprisonment for life`, `punishable with imprisonment`, `punishable with imprisonment for` n `months or upwards within section 41` | pc-general + the other offence's module | 388, 389, 449-451 |

The edge used is `property -> body-a`, which PLAN §1 allows; but PLAN lists only ss 382, 394, 397 and 459-460 as its readers, and this encoding also reads body-a at ss 386, 387, 390, 396, 440 and 452 (same direction, no new edge).
The edge `property -> general-part` (s 511) is allowed.

## Definition ladders for the charge generator (`DEFINITION_LADDERS`)

Flat leaves in this group's records that have a Chapter 2 drill-down: `dishonestly` → `dishonestly within section 24` (s 24); `fraudulently` → `fraudulently within section 25` (s 25); `movable property` → `movable property within section 22` (s 22); `voluntarily` (Robbery) → `voluntarily within section 26A` (s 26A); `valuable security` (Extortion) → `valuable security within section 30` (s 30); `having reason to believe` (Stolen Property) → `reason to believe within section 26` (s 26).
