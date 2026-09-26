# Coverage - justice-order group (Penal Code 1871, Chapters 11-15, ss 191-298A)

Source: `inputs/PC1871.txt`, Chapter 11 at line 4839, Chapter 15 ending before Chapter 16 at line 6515.
Modules: `deposit/pc-justice-order.l4` (Chapters 11-12), `deposit/pc-justice-order-public.l4` (Chapters 13-15), `deposit/pc-justice-order-tests.l4` (tests for both).
Every section between those lines appears below: the list was generated from the section numbers found in the source text itself, and a script checked that each has a row (125 of 125).

Dispositions: `encoded` (ladder, and for a punishing section `offence under s N` + `charge under s N` + its punishment record(s)), `repealed`, `absent` (the Code says the number does not exist).
No section is `deferred` or `out-of-scope`. Where an encoding simplifies the section's structure, the row names the fork in `justice-order-forks.md`.

Checked with the toolchain in BRIEF.md, `JL4_LIBRARY_PATH` unset, via `deposit/check.sh` over copies of pc-domain, pc-general and these three modules:

```
pc-justice-order-public.l4    errors 0  satisfied  0  failed 0
pc-justice-order-tests.l4     errors 0  satisfied 92  failed 0
pc-justice-order.l4           errors 0  satisfied  0  failed 0
```

`l4 check` on both encoding modules: `Check succeeded.`, with no warning diagnostics. The 92 is also the number of `#ASSERT` lines in the tests module, and a deliberately wrong assertion appended to a copy of the module failed as expected (positive control).


## Chapter 11 - False evidence and offences against public justice (pc-justice-order.l4)

| s | heading | disposition | functions / note |
| --- | --- | --- | --- |
| 191 | Giving false evidence | encoded | `False Evidence Facts`; `gives false evidence` (definition; punished by ss 193-195) |
| 192 | Fabricating false evidence | encoded | `fabricates false evidence` (definition; punished by ss 193-195) |
| 193 | Punishment for false evidence | encoded | `offence under s 193`, `charge under s 193`, `the false evidence is in a stage of a judicial proceeding`; punishments `s 193 (judicial proceeding)`, `s 193 (any other case)` |
| 194 | Giving or fabricating false evidence with intent to procure conviction of a capital offence | encoded | `offence under s 194`, `charge under s 194`; punishments `s 194`, `s 194 (innocent person executed)` |
| 195 | Giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment | encoded | `offence under s 195(1)`, `charge under s 195(1)`, `offence under s 195(2)`, `charge under s 195(2)`; `punishment prescribed by s 195(1) for` (a function of the other offence's Punishment), `punishment prescribed by s 195(2)` |
| 196 | Using evidence known to be false | encoded | `Using False Evidence Facts`; `corruptly uses evidence known to be false`, `offence under s 196`, `charge under s 196` |
| 197 | Issuing or signing a false certificate | encoded | `issues or signs a false certificate`, `offence under s 197`, `charge under s 197` |
| 198 | Using as a true certificate one known to be false in a material point | encoded | `uses as true a certificate known to be false`, `offence under s 198`, `charge under s 198` |
| 199 | False statement made in any declaration which is by law receivable as evidence | encoded | `makes a false statement in a declaration receivable as evidence`, `offence under s 199`, `charge under s 199` |
| 200 | Using as true any such declaration known to be false | encoded | `uses as true a declaration known to be false`, `offence under s 200`, `charge under s 200`; the Explanation widens the s 199 leaf |
| 201 | Causing disappearance of evidence of an offence committed, or giving false information touching it, to screen the offender | encoded | `Offence Information Facts`; `causes disappearance of evidence of an offence to screen the offender`, `offence under s 201`, `charge under s 201`; punishments `s 201(a)`-`(c)` |
| 202 | Intentional omission to give information of an offence, by person bound to inform | encoded | `intentionally omits to give information of an offence`, `offence under s 202`, `charge under s 202` |
| 203 | Giving false information respecting an offence committed | encoded | `gives false information respecting an offence`, `offence under s 203`, `charge under s 203`; the Explanation widens the knowledge leaf |
| 204 | Destruction of document or electronic record to prevent its production as evidence | encoded | `Evidence Document Facts`; `destroys a document to prevent its production as evidence`, `offence under s 204`, `charge under s 204` |
| 204A | Obstructing, preventing, perverting or defeating course of justice | encoded | `Course of Justice Facts`; `does an act tending to obstruct, prevent, pervert or defeat the course of justice`, `offence under s 204A`, `charge under s 204A`; Explanation 1 is a NOT-limb, Explanation 2 widens the act leaf |
| 204B | Bribery of witnesses | encoded | `Witness Bribery Facts`; `bribes or suborns a witness`, `offence under s 204B`, `charge under s 204B`; (2) is the @desc of the witness leaf |
| 205 | False personation for the purpose of any act or proceeding in a suit | encoded | `Personation in Suit Facts`; `falsely personates another in a suit or prosecution`, `offence under s 205`, `charge under s 205` |
| 206 | Fraudulent removal or concealment of property to prevent its seizure as a forfeiture, in execution of a decree or under or pursuant to an enforcement order | encoded | `Decree Fraud Facts`; `fraudulently removes or conceals property to prevent its seizure`, `offence under s 206`, `charge under s 206` |
| 207 | Fraudulent claim to property to prevent its seizure as a forfeiture, in execution of a decree or under or pursuant to an enforcement order | encoded | `fraudulently claims property to prevent its seizure`, `offence under s 207`, `charge under s 207` |
| 208 | Fraudulently suffering a decree for a sum not due | encoded | `fraudulently suffers a decree for a sum not due`, `offence under s 208`, `charge under s 208` |
| 209 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 210 | Fraudulently obtaining a decree for a sum not due | encoded | `fraudulently obtains a decree for a sum not due`, `offence under s 210`, `charge under s 210` |
| 211 | False charge of offence made with intent to injure | encoded | `False Charge Facts`; `falsely charges an offence with intent to injure`, `offence under s 211`, `charge under s 211`; punishments `s 211`, `s 211 (grave offence)` |
| 212 | Harbouring an offender | encoded | `Harbouring Facts`; `harbours an offender`, `offence under s 212`, `charge under s 212`; punishments `s 212(a)`-`(c)`; (2) widens the offence leaf |
| 213 | Taking gifts, etc., to screen an offender from punishment | encoded | `Screening Gift Facts`; `takes a gift to screen an offender`, `offence under s 213`, `charge under s 213`; the Exception is a NOT-limb |
| 214 | Offering gift or restoration of property in consideration of screening offender | encoded | `offers a gift to screen an offender`, `offence under s 214`, `charge under s 214`; the Exceptions paragraph is a NOT-limb of both ss 213 and 214 |
| 215 | Taking gift to help to recover stolen property, etc. | encoded | `takes a gift to help recover stolen property`, `offence under s 215`, `charge under s 215`; "unless he uses all means" is a NOT-limb |
| 216 | Harbouring an offender who has escaped from custody, or whose apprehension has been ordered | encoded | `harbours an escaped offender`, `offence under s 216`, `charge under s 216`; punishments `s 216(a)`-`(c)`; (2) widens the escape leaf |
| 216A | Harbouring robbers or gang-robbers, etc. | encoded | `harbours robbers or gang-robbers`, `offence under s 216A`, `charge under s 216A`; the Explanation widens the knowledge leaf |
| 216B | "Harbour" | encoded | `harbours within section 216B` (definition; the drill-down for ss 212, 216, 216A) |
| 217 | Public servant disobeying a direction of law with intent to save person from punishment or property from forfeiture | encoded | `Public Servant Justice Facts`; `disobeys a direction of law to save a person from punishment`, `offence under s 217`, `charge under s 217` |
| 218 | Public servant framing an incorrect record or writing with intent to save person from punishment, or property from forfeiture | encoded | `frames an incorrect record to save a person from punishment`, `offence under s 218`, `charge under s 218` |
| 219 | Public servant in a judicial proceeding making an order, etc., which he knows to be contrary to law | encoded | `makes an order in a judicial proceeding known to be contrary to law`, `offence under s 219`, `charge under s 219` |
| 220 | Commitment for trial or confinement by person having authority who knows he is acting contrary to law | encoded | `commits a person for trial or confinement knowing it contrary to law`, `offence under s 220`, `charge under s 220`; punishment `s 220` (section field "220(2)") |
| 221 | Intentional omission to apprehend on the part of a public servant bound by law to apprehend | encoded | `Escape by Public Servant Facts`; `intentionally omits to apprehend a person charged with an offence`, `offence under s 221`, `charge under s 221`; punishments `s 221(a)`-`(c)` |
| 222 | Intentional omission to apprehend on the part of a public servant bound by law to apprehend person under sentence of a court of justice | encoded | `intentionally omits to apprehend a person under sentence`, `offence under s 222`, `charge under s 222`; punishments `s 222(a)`-`(c)` |
| 223 | Escape from confinement negligently suffered by a public servant | encoded | `negligently suffers a person to escape`, `offence under s 223`, `charge under s 223` |
| 224 | Resistance or obstruction by a person to his lawful apprehension | encoded | `Escape Facts`; `resists or escapes lawful apprehension for his own offence`, `offence under s 224`, `charge under s 224` |
| 225 | Resistance or obstruction to the lawful apprehension of another person | encoded | `resists the lawful apprehension of another person`, `offence under s 225`, `charge under s 225`; punishments `s 225(a)`-`(e)` |
| 225A | Public servant omitting to apprehend or suffering other persons to escape in cases not already provided for | encoded | `omits to apprehend in a case not otherwise provided for`, `offence under s 225A`, `charge under s 225A`; punishments `s 225A(a)`, `(b)` |
| 225B | Resistance or obstruction to lawful apprehension, or escape, or rescue, in cases not otherwise provided for | encoded | `resists apprehension or escapes in a case not otherwise provided for`, `offence under s 225B`, `charge under s 225B` |
| 225C | Offences against laws of Singapore where no special punishment is provided | encoded | `Disobedience of Law Facts`; `disobeys a law where no special punishment is provided`, `offence under s 225C`, `charge under s 225C` |
| 226 | (Repealed) | repealed | [Repealed by Act 31 of 2023 wef 30/05/2025] |
| 227 | (Repealed) | repealed | [Repealed by Act 1 of 2014] |
| 228 | Intentional insult or interruption to a public servant sitting in any stage of a judicial proceeding or mediation or other alternative dispute resolution process | encoded | `Court Proceedings Facts`; `insults or interrupts a public servant sitting in a judicial proceeding`, `offence under s 228`, `charge under s 228` |
| 229 | Personation of an assessor Chapter 12 - Offences relating to government stamps | encoded | `personates an assessor`, `offence under s 229`, `charge under s 229` |

## Chapter 12 - Offences relating to Government stamps (pc-justice-order.l4)

| s | heading | disposition | functions / note |
| --- | --- | --- | --- |
| 230 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 231 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 232 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 233 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 234 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 235 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 236 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 237 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 238 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 239 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 240 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 241 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 241A | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 242 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 243 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 243A | (Repealed) [There are no sections 244 and 245.] | repealed | [Repealed by Act 51 of 2007] |
| 244-245 |  | absent | The Code prints "[There are no sections 244 and 245.]" |
| 246 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 247 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 248 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 249 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 250 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 251 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 252 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 253 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 254 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 254A | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 255 | Counterfeiting a Government stamp | encoded | `Government Stamp Facts`; `counterfeits a Government stamp`, `offence under s 255`, `charge under s 255`; (2) and the Explanation widen the leaves |
| 256 | Having possession of an instrument or material for the purpose of counterfeiting a Government stamp | encoded | `possesses an instrument for counterfeiting a Government stamp`, `offence under s 256`, `charge under s 256` |
| 257 | Making or selling an instrument for the purpose of counterfeiting a Government stamp | encoded | `makes or sells an instrument for counterfeiting a Government stamp`, `offence under s 257`, `charge under s 257` |
| 258 | Sale of counterfeit Government stamp | encoded | `sells a counterfeit Government stamp`, `offence under s 258`, `charge under s 258` |
| 259 | Having possession of a counterfeit Government stamp | encoded | `possesses a counterfeit Government stamp`, `offence under s 259`, `charge under s 259` |
| 260 | Using as genuine a Government stamp known to be counterfeit | encoded | `uses as genuine a counterfeit Government stamp`, `offence under s 260`, `charge under s 260` |
| 261 | Effacing any writing from a substance bearing a Government stamp, or removing from a document a stamp used for it, with intent to cause loss to Government | encoded | `removes writing from a Government stamp to cause loss to the Government`, `offence under s 261`, `charge under s 261` |
| 262 | Using a Government stamp known to have been before used | encoded | `uses a Government stamp known to have been before used`, `offence under s 262`, `charge under s 262` |
| 263 | Erasure of mark denoting that stamp has been used Chapter 13 | encoded | `erases the used mark from a Government stamp`, `offence under s 263`, `charge under s 263` |

## Chapter 13 - (repealed) (pc-justice-order-public.l4)

| s | heading | disposition | functions / note |
| --- | --- | --- | --- |
| 264 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 265 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 266 | (Repealed) | repealed | [Repealed by Act 15 of 2019] |
| 267 | (Repealed) Chapter 14 - Offences affecting the public tranquility, public health, safety, convenience, decency and morals | repealed | [Repealed by Act 15 of 2019] |

## Chapter 14 - Offences affecting the public tranquility, public health, safety, convenience, decency and morals (pc-justice-order-public.l4)

| s | heading | disposition | functions / note |
| --- | --- | --- | --- |
| 267A | Affray | encoded | `Affray Facts`; `commits an affray` (definition; punished by s 267B) |
| 267B | Punishment for committing affray | encoded | `offence under s 267B`, `charge under s 267B` |
| 267C | Uttering words, making document, etc., containing incitement to violence, etc. | encoded | `Incitement Facts`; `utters words or makes a document containing incitement to violence`, `offence under s 267C`, `charge under s 267C`; (4) widens the content leaf |
| 268 | Public nuisance | encoded | `Public Nuisance Facts`; `is guilty of a public nuisance` (definition; punished by ss 290, 291); the Explanation is in the leaf's @desc |
| 268A | Communicating false information of harmful thing | encoded | `Harmful Thing Hoax Facts`; `communicates false information of a harmful thing`, `offence under s 268A`, `charge under s 268A` |
| 268B | Placing or sending thing with intent to cause fear of harm | encoded | `places or sends a thing with intent to cause fear of harm`, `offence under s 268B`, `charge under s 268B`; (2) is in the leaf's @desc |
| 268C | Placing or sending thing causing fear of harm | encoded | `places or sends a thing causing fear of harm`, `offence under s 268C`, `charge under s 268C`; (2) is in the leaf's @desc |
| 269 | Negligent act likely to spread infection of any disease dangerous to life | encoded | `Public Health Facts`; `negligently does an act likely to spread infection`, `offence under s 269`, `charge under s 269` |
| 270 | Intentional or rash act likely to spread infection of any disease dangerous to life | encoded | `intentionally does an act likely to spread infection`, `offence under s 270`, `charge under s 270` |
| 271 | Disobedience to a quarantine rule | encoded | `disobeys a quarantine rule`, `offence under s 271`, `charge under s 271` |
| 272 | Adulteration of food or drink which is intended for sale | encoded | `adulterates food or drink intended for sale`, `offence under s 272`, `charge under s 272` |
| 273 | Sale of noxious food or drink | encoded | `sells noxious food or drink`, `offence under s 273`, `charge under s 273` |
| 274 | Adulteration of drugs | encoded | `adulterates drugs`, `offence under s 274`, `charge under s 274` |
| 275 | Sale of adulterated drugs | encoded | `sells adulterated drugs`, `offence under s 275`, `charge under s 275` |
| 276 | Sale of any drug as a different drug or preparation | encoded | `sells a drug as a different drug`, `offence under s 276`, `charge under s 276` |
| 277 | Fouling the water of a public spring or reservoir | encoded | `fouls the water of a public spring or reservoir`, `offence under s 277`, `charge under s 277` |
| 278 | Making atmosphere noxious to health | encoded | `makes the atmosphere noxious to health`, `offence under s 278`, `charge under s 278` |
| 279 | Rash driving or riding on a public way | encoded | `Rash Conduct Facts`; `drives rashly on a public way`, `offence under s 279`, `charge under s 279` |
| 280 | Rash navigation of a vessel | encoded | `navigates a vessel rashly`, `offence under s 280`, `charge under s 280` |
| 281 | Exhibition of a false light, mark or buoy | encoded | `exhibits a false light, mark or buoy`, `offence under s 281`, `charge under s 281` |
| 282 | Conveying person by water for hire in a vessel overloaded or unsafe | encoded | `conveys a person by water in an unsafe vessel`, `offence under s 282`, `charge under s 282` |
| 283 | Danger or obstruction in a public way or navigation | encoded | `causes danger or obstruction in a public way`, `offence under s 283`, `charge under s 283` |
| 284 | Rash or negligent conduct with respect to dangerous or harmful substance | encoded | `Dangerous Conduct Facts`; `does a rash act with a dangerous substance`, `offence under s 284`, `charge under s 284`; punishments `s 284(3)(a)`-`(d)` picked by the gravest result (FORK JO-8) |
| 285 | Causing or contributing to risk of dangerous fire | encoded | `causes or contributes to the risk of a dangerous fire`, `offence under s 285`, `charge under s 285`; punishments `s 285(2)(a)`-`(e)` |
| 286 | Presumption of cause of fire | encoded | `is presumed to have substantially contributed to the risk of fire within section 286` (a presumption, wired into the s 285 ladder as an alternative limb), `within 60 minutes` |
| 287 | Rash or negligent conduct with respect to any machinery in possession or under charge of offender | encoded | `does a rash act with machinery`, `offence under s 287`, `charge under s 287`; punishments `s 287(3)(a)`-`(d)` |
| 288 | Negligence in pulling down or repairing buildings | encoded | `omits precautions in pulling down or repairing a building`, `offence under s 288`, `charge under s 288`; punishments `s 288(2)(a)`, `(b)` |
| 289 | Negligence with respect to any animal | encoded | `omits precautions with an animal`, `offence under s 289`, `charge under s 289`; punishments `s 289(2)(a)`-`(c)` |
| 290 | Punishment for public nuisance | encoded | `offence under s 290`, `charge under s 290`; punishments `s 290(a)`-`(c)` |
| 291 | Continuance of nuisance after injunction to discontinue | encoded | `continues a public nuisance after injunction`, `offence under s 291`, `charge under s 291` |
| 292 | Sale of obscene objects, etc. | encoded | `Obscenity Facts`; `the object is obscene within section 292`, `deals in an obscene object`, `offence under s 292`, `charge under s 292` (punishment from (1), (1A), (1B)(a)/(b)), `offence under s 292(1C)`, `charge under s 292(1C)`; helpers `10 or more individuals`, `below 18 years of age` |
| 292A | Possession, distribution, etc., of child sex-doll | encoded | `deals in a child sex-doll`, `offence under s 292A`, `charge under s 292A`; (2) is the leaf's @desc; helper `below 16 years of age` |
| 292B | Obscene object on online location | encoded | `runs an online location for obscene objects`, `offence under s 292B`, `charge under s 292B`; punishments `s 292B(1)`, `s 292B(2)`; (3) in @desc |
| 293 | Sale, etc., of obscene objects to young person | encoded | `deals in an obscene object with a young person`, `offence under s 293`, `charge under s 293`; helper `below 21 years of age` |
| 294 | Obscene acts Chapter 15 - Offences relating to race | encoded | `does an obscene act in a public place`, `offence under s 294`, `charge under s 294` |

## Chapter 15 - Offences relating to race (pc-justice-order-public.l4)

| s | heading | disposition | functions / note |
| --- | --- | --- | --- |
| 295 | (Repealed) | repealed | [Repealed by Act 31 of 2019 wef 01/11/2022] |
| 296 | (Repealed) | repealed | [Repealed by Act 31 of 2019 wef 01/11/2022] |
| 297 | (Repealed) | repealed | [Repealed by Act 31 of 2019 wef 01/11/2022] |
| 298 | Uttering words, etc., with deliberate intent to wound the racial feelings of any person | encoded | `Racial Feelings Facts`; `wounds the racial feelings of a person`, `offence under s 298`, `charge under s 298` |
| 298A | Promoting enmity between different groups on grounds of race and doing acts prejudicial to maintenance of harmony Chapter 16 - Offences affecting the human body Offences affecting life | encoded | `promotes enmity between racial groups`, `offence under s 298A`, `charge under s 298A` |

## Tests

Illustrations expressed as assertions: s 191 (a)-(e); s 192 (a)-(c); s 193 Explanation 2 and 3 illustrations; s 195 illustration (with the s 395 gang-robbery punishment quoted as test data); s 201 illustration; s 212 (a)-(c).
Explanations tested: s 200 Explanation (an informal declaration); s 204A Explanations 1 and 2; s 286 (presumption, with the 60-minute boundary on both sides); s 292 Exception (religious objects).
Threshold helpers, both sides of the line: `within 60 minutes` (60 / 61), `below 21 years of age` (20 / 21), `below 18 years of age` (17 / 18), `below 16 years of age` (15 / 16), `10 or more individuals` (9 / 10), `one-fourth part of the longest term of imprisonment` (36 -> 9).
Charges asserted as full text: ss 193 (two), 201, 204A, 224, 267B, 298. Refusals asserted as full text: ss 193, 201, 267B.
Illustrations not expressible on these atoms: none in Chapters 11-15; every Illustration printed is asserted.
Not tested: most families have no charge-text assertion (ss 196-200 punishment strings are tested; 202-229 except 204A, 212, 224, 225; Chapter 12; ss 267C-283, 287-294 except 290, 293, 294). Their ladders typecheck and their builders share code with the tested ones, but no expected value from the source pins them. That is the gap an independent test pass should fill first.

## Catalogue entries (reference/charge-generator-catalogue.ts `OFFENCES`)

New `family` slugs proposed (the app's union has none of them): course-of-justice, court-proceedings, decree-fraud, escape, false-charge, false-evidence, general-disobedience, government-stamps, harbouring, obscenity, public-health, public-order, public-safety, public-servant-justice, race, screening.

```json
[
 {
  "section": "193",
  "title": "giving or fabricating false evidence",
  "defines": "ss 191, 192, 193",
  "family": "false-evidence",
  "offenceFn": "offence under s 193",
  "chargeFn": "charge under s 193",
  "definitionFns": [
   "gives false evidence",
   "fabricates false evidence"
  ],
  "factsType": "False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "194",
  "title": "giving or fabricating false evidence with intent to procure conviction of a capital offence",
  "defines": "ss 191, 192, 194",
  "family": "false-evidence",
  "offenceFn": "offence under s 194",
  "chargeFn": "charge under s 194",
  "definitionFns": [
   "gives false evidence",
   "fabricates false evidence"
  ],
  "factsType": "False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "195(1)",
  "title": "giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for 7 years or upwards",
  "defines": "ss 191, 192, 195",
  "family": "false-evidence",
  "offenceFn": "offence under s 195(1)",
  "chargeFn": "charge under s 195(1)",
  "definitionFns": [
   "gives false evidence",
   "fabricates false evidence"
  ],
  "factsType": "False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "195(2)",
  "title": "giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for life",
  "defines": "ss 191, 192, 195",
  "family": "false-evidence",
  "offenceFn": "offence under s 195(2)",
  "chargeFn": "charge under s 195(2)",
  "definitionFns": [
   "gives false evidence",
   "fabricates false evidence"
  ],
  "factsType": "False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "196",
  "title": "using evidence known to be false",
  "defines": "s 196",
  "family": "false-evidence",
  "offenceFn": "offence under s 196",
  "chargeFn": "charge under s 196",
  "definitionFns": [
   "corruptly uses evidence known to be false"
  ],
  "factsType": "Using False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "197",
  "title": "issuing or signing a false certificate",
  "defines": "s 197",
  "family": "false-evidence",
  "offenceFn": "offence under s 197",
  "chargeFn": "charge under s 197",
  "definitionFns": [
   "issues or signs a false certificate"
  ],
  "factsType": "Using False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "198",
  "title": "using as a true certificate one known to be false in a material point",
  "defines": "s 198",
  "family": "false-evidence",
  "offenceFn": "offence under s 198",
  "chargeFn": "charge under s 198",
  "definitionFns": [
   "uses as true a certificate known to be false"
  ],
  "factsType": "Using False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "199",
  "title": "false statement made in a declaration which is by law receivable as evidence",
  "defines": "s 199",
  "family": "false-evidence",
  "offenceFn": "offence under s 199",
  "chargeFn": "charge under s 199",
  "definitionFns": [
   "makes a false statement in a declaration receivable as evidence"
  ],
  "factsType": "Using False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "200",
  "title": "using as true a declaration known to be false",
  "defines": "ss 199, 200",
  "family": "false-evidence",
  "offenceFn": "offence under s 200",
  "chargeFn": "charge under s 200",
  "definitionFns": [
   "uses as true a declaration known to be false"
  ],
  "factsType": "Using False Evidence Facts",
  "factsParam": "f"
 },
 {
  "section": "201",
  "title": "causing disappearance of evidence of an offence committed, or giving false information touching it, to screen the offender",
  "defines": "s 201",
  "family": "screening",
  "offenceFn": "offence under s 201",
  "chargeFn": "charge under s 201",
  "definitionFns": [
   "causes disappearance of evidence of an offence to screen the offender"
  ],
  "factsType": "Offence Information Facts",
  "factsParam": "f"
 },
 {
  "section": "202",
  "title": "intentional omission to give information of an offence by a person bound to inform",
  "defines": "s 202",
  "family": "screening",
  "offenceFn": "offence under s 202",
  "chargeFn": "charge under s 202",
  "definitionFns": [
   "intentionally omits to give information of an offence"
  ],
  "factsType": "Offence Information Facts",
  "factsParam": "f"
 },
 {
  "section": "203",
  "title": "giving false information respecting an offence committed",
  "defines": "s 203",
  "family": "screening",
  "offenceFn": "offence under s 203",
  "chargeFn": "charge under s 203",
  "definitionFns": [
   "gives false information respecting an offence"
  ],
  "factsType": "Offence Information Facts",
  "factsParam": "f"
 },
 {
  "section": "204",
  "title": "destruction of document or electronic record to prevent its production as evidence",
  "defines": "s 204",
  "family": "course-of-justice",
  "offenceFn": "offence under s 204",
  "chargeFn": "charge under s 204",
  "definitionFns": [
   "destroys a document to prevent its production as evidence"
  ],
  "factsType": "Evidence Document Facts",
  "factsParam": "f"
 },
 {
  "section": "204A",
  "title": "obstructing, preventing, perverting or defeating the course of justice",
  "defines": "s 204A",
  "family": "course-of-justice",
  "offenceFn": "offence under s 204A",
  "chargeFn": "charge under s 204A",
  "definitionFns": [
   "does an act tending to obstruct, prevent, pervert or defeat the course of justice"
  ],
  "factsType": "Course of Justice Facts",
  "factsParam": "f"
 },
 {
  "section": "204B",
  "title": "bribery of witnesses",
  "defines": "s 204B",
  "family": "course-of-justice",
  "offenceFn": "offence under s 204B",
  "chargeFn": "charge under s 204B",
  "definitionFns": [
   "bribes or suborns a witness"
  ],
  "factsType": "Witness Bribery Facts",
  "factsParam": "f"
 },
 {
  "section": "205",
  "title": "false personation for the purpose of an act or proceeding in a suit",
  "defines": "s 205",
  "family": "course-of-justice",
  "offenceFn": "offence under s 205",
  "chargeFn": "charge under s 205",
  "definitionFns": [
   "falsely personates another in a suit or prosecution"
  ],
  "factsType": "Personation in Suit Facts",
  "factsParam": "f"
 },
 {
  "section": "206",
  "title": "fraudulent removal or concealment of property to prevent its seizure",
  "defines": "s 206",
  "family": "decree-fraud",
  "offenceFn": "offence under s 206",
  "chargeFn": "charge under s 206",
  "definitionFns": [
   "fraudulently removes or conceals property to prevent its seizure"
  ],
  "factsType": "Decree Fraud Facts",
  "factsParam": "f"
 },
 {
  "section": "207",
  "title": "fraudulent claim to property to prevent its seizure",
  "defines": "s 207",
  "family": "decree-fraud",
  "offenceFn": "offence under s 207",
  "chargeFn": "charge under s 207",
  "definitionFns": [
   "fraudulently claims property to prevent its seizure"
  ],
  "factsType": "Decree Fraud Facts",
  "factsParam": "f"
 },
 {
  "section": "208",
  "title": "fraudulently suffering a decree for a sum not due",
  "defines": "s 208",
  "family": "decree-fraud",
  "offenceFn": "offence under s 208",
  "chargeFn": "charge under s 208",
  "definitionFns": [
   "fraudulently suffers a decree for a sum not due"
  ],
  "factsType": "Decree Fraud Facts",
  "factsParam": "f"
 },
 {
  "section": "210",
  "title": "fraudulently obtaining a decree for a sum not due",
  "defines": "s 210",
  "family": "decree-fraud",
  "offenceFn": "offence under s 210",
  "chargeFn": "charge under s 210",
  "definitionFns": [
   "fraudulently obtains a decree for a sum not due"
  ],
  "factsType": "Decree Fraud Facts",
  "factsParam": "f"
 },
 {
  "section": "211",
  "title": "false charge of offence made with intent to injure",
  "defines": "s 211",
  "family": "false-charge",
  "offenceFn": "offence under s 211",
  "chargeFn": "charge under s 211",
  "definitionFns": [
   "falsely charges an offence with intent to injure"
  ],
  "factsType": "False Charge Facts",
  "factsParam": "f"
 },
 {
  "section": "212",
  "title": "harbouring an offender",
  "defines": "s 212",
  "family": "harbouring",
  "offenceFn": "offence under s 212",
  "chargeFn": "charge under s 212",
  "definitionFns": [
   "harbours an offender",
   "harbours within section 216B"
  ],
  "factsType": "Harbouring Facts",
  "factsParam": "f"
 },
 {
  "section": "213",
  "title": "taking gifts to screen an offender from punishment",
  "defines": "s 213",
  "family": "screening",
  "offenceFn": "offence under s 213",
  "chargeFn": "charge under s 213",
  "definitionFns": [
   "takes a gift to screen an offender"
  ],
  "factsType": "Screening Gift Facts",
  "factsParam": "f"
 },
 {
  "section": "214",
  "title": "offering gift or restoration of property in consideration of screening offender",
  "defines": "s 214",
  "family": "screening",
  "offenceFn": "offence under s 214",
  "chargeFn": "charge under s 214",
  "definitionFns": [
   "offers a gift to screen an offender"
  ],
  "factsType": "Screening Gift Facts",
  "factsParam": "f"
 },
 {
  "section": "215",
  "title": "taking gift to help to recover stolen property",
  "defines": "s 215",
  "family": "screening",
  "offenceFn": "offence under s 215",
  "chargeFn": "charge under s 215",
  "definitionFns": [
   "takes a gift to help recover stolen property"
  ],
  "factsType": "Screening Gift Facts",
  "factsParam": "f"
 },
 {
  "section": "216",
  "title": "harbouring an offender who has escaped from custody, or whose apprehension has been ordered",
  "defines": "s 216",
  "family": "harbouring",
  "offenceFn": "offence under s 216",
  "chargeFn": "charge under s 216",
  "definitionFns": [
   "harbours an escaped offender",
   "harbours within section 216B"
  ],
  "factsType": "Harbouring Facts",
  "factsParam": "f"
 },
 {
  "section": "216A",
  "title": "harbouring robbers or gang-robbers",
  "defines": "s 216A",
  "family": "harbouring",
  "offenceFn": "offence under s 216A",
  "chargeFn": "charge under s 216A",
  "definitionFns": [
   "harbours robbers or gang-robbers",
   "harbours within section 216B"
  ],
  "factsType": "Harbouring Facts",
  "factsParam": "f"
 },
 {
  "section": "217",
  "title": "public servant disobeying a direction of law with intent to save person from punishment or property from forfeiture",
  "defines": "s 217",
  "family": "public-servant-justice",
  "offenceFn": "offence under s 217",
  "chargeFn": "charge under s 217",
  "definitionFns": [
   "disobeys a direction of law to save a person from punishment"
  ],
  "factsType": "Public Servant Justice Facts",
  "factsParam": "f"
 },
 {
  "section": "218",
  "title": "public servant framing an incorrect record or writing with intent to save person from punishment, or property from forfeiture",
  "defines": "s 218",
  "family": "public-servant-justice",
  "offenceFn": "offence under s 218",
  "chargeFn": "charge under s 218",
  "definitionFns": [
   "frames an incorrect record to save a person from punishment"
  ],
  "factsType": "Public Servant Justice Facts",
  "factsParam": "f"
 },
 {
  "section": "219",
  "title": "public servant in a judicial proceeding making an order which he knows to be contrary to law",
  "defines": "s 219",
  "family": "public-servant-justice",
  "offenceFn": "offence under s 219",
  "chargeFn": "charge under s 219",
  "definitionFns": [
   "makes an order in a judicial proceeding known to be contrary to law"
  ],
  "factsType": "Public Servant Justice Facts",
  "factsParam": "f"
 },
 {
  "section": "220",
  "title": "commitment for trial or confinement by person having authority who knows he is acting contrary to law",
  "defines": "s 220",
  "family": "public-servant-justice",
  "offenceFn": "offence under s 220",
  "chargeFn": "charge under s 220",
  "definitionFns": [
   "commits a person for trial or confinement knowing it contrary to law"
  ],
  "factsType": "Public Servant Justice Facts",
  "factsParam": "f"
 },
 {
  "section": "221",
  "title": "intentional omission to apprehend on the part of a public servant bound by law to apprehend",
  "defines": "s 221",
  "family": "escape",
  "offenceFn": "offence under s 221",
  "chargeFn": "charge under s 221",
  "definitionFns": [
   "intentionally omits to apprehend a person charged with an offence"
  ],
  "factsType": "Escape by Public Servant Facts",
  "factsParam": "f"
 },
 {
  "section": "222",
  "title": "intentional omission to apprehend on the part of a public servant bound by law to apprehend person under sentence of a court of justice",
  "defines": "s 222",
  "family": "escape",
  "offenceFn": "offence under s 222",
  "chargeFn": "charge under s 222",
  "definitionFns": [
   "intentionally omits to apprehend a person under sentence"
  ],
  "factsType": "Escape by Public Servant Facts",
  "factsParam": "f"
 },
 {
  "section": "223",
  "title": "escape from confinement negligently suffered by a public servant",
  "defines": "s 223",
  "family": "escape",
  "offenceFn": "offence under s 223",
  "chargeFn": "charge under s 223",
  "definitionFns": [
   "negligently suffers a person to escape"
  ],
  "factsType": "Escape by Public Servant Facts",
  "factsParam": "f"
 },
 {
  "section": "224",
  "title": "resistance or obstruction by a person to his lawful apprehension",
  "defines": "s 224",
  "family": "escape",
  "offenceFn": "offence under s 224",
  "chargeFn": "charge under s 224",
  "definitionFns": [
   "resists or escapes lawful apprehension for his own offence"
  ],
  "factsType": "Escape Facts",
  "factsParam": "f"
 },
 {
  "section": "225",
  "title": "resistance or obstruction to the lawful apprehension of another person",
  "defines": "s 225",
  "family": "escape",
  "offenceFn": "offence under s 225",
  "chargeFn": "charge under s 225",
  "definitionFns": [
   "resists the lawful apprehension of another person"
  ],
  "factsType": "Escape Facts",
  "factsParam": "f"
 },
 {
  "section": "225A",
  "title": "public servant omitting to apprehend or suffering other persons to escape in cases not already provided for",
  "defines": "s 225A",
  "family": "escape",
  "offenceFn": "offence under s 225A",
  "chargeFn": "charge under s 225A",
  "definitionFns": [
   "omits to apprehend in a case not otherwise provided for"
  ],
  "factsType": "Escape by Public Servant Facts",
  "factsParam": "f"
 },
 {
  "section": "225B",
  "title": "resistance or obstruction to lawful apprehension, or escape, or rescue, in cases not otherwise provided for",
  "defines": "s 225B",
  "family": "escape",
  "offenceFn": "offence under s 225B",
  "chargeFn": "charge under s 225B",
  "definitionFns": [
   "resists apprehension or escapes in a case not otherwise provided for"
  ],
  "factsType": "Escape Facts",
  "factsParam": "f"
 },
 {
  "section": "225C",
  "title": "offences against laws of Singapore where no special punishment is provided",
  "defines": "s 225C",
  "family": "general-disobedience",
  "offenceFn": "offence under s 225C",
  "chargeFn": "charge under s 225C",
  "definitionFns": [
   "disobeys a law where no special punishment is provided"
  ],
  "factsType": "Disobedience of Law Facts",
  "factsParam": "f"
 },
 {
  "section": "228",
  "title": "intentional insult or interruption to a public servant sitting in a judicial proceeding",
  "defines": "s 228",
  "family": "court-proceedings",
  "offenceFn": "offence under s 228",
  "chargeFn": "charge under s 228",
  "definitionFns": [
   "insults or interrupts a public servant sitting in a judicial proceeding"
  ],
  "factsType": "Court Proceedings Facts",
  "factsParam": "f"
 },
 {
  "section": "229",
  "title": "personation of an assessor",
  "defines": "s 229",
  "family": "court-proceedings",
  "offenceFn": "offence under s 229",
  "chargeFn": "charge under s 229",
  "definitionFns": [
   "personates an assessor"
  ],
  "factsType": "Court Proceedings Facts",
  "factsParam": "f"
 },
 {
  "section": "255",
  "title": "counterfeiting a Government stamp",
  "defines": "s 255",
  "family": "government-stamps",
  "offenceFn": "offence under s 255",
  "chargeFn": "charge under s 255",
  "definitionFns": [
   "counterfeits a Government stamp"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "256",
  "title": "having possession of an instrument or material for the purpose of counterfeiting a Government stamp",
  "defines": "s 256",
  "family": "government-stamps",
  "offenceFn": "offence under s 256",
  "chargeFn": "charge under s 256",
  "definitionFns": [
   "possesses an instrument for counterfeiting a Government stamp"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "257",
  "title": "making or selling an instrument for the purpose of counterfeiting a Government stamp",
  "defines": "s 257",
  "family": "government-stamps",
  "offenceFn": "offence under s 257",
  "chargeFn": "charge under s 257",
  "definitionFns": [
   "makes or sells an instrument for counterfeiting a Government stamp"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "258",
  "title": "sale of counterfeit Government stamp",
  "defines": "s 258",
  "family": "government-stamps",
  "offenceFn": "offence under s 258",
  "chargeFn": "charge under s 258",
  "definitionFns": [
   "sells a counterfeit Government stamp"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "259",
  "title": "having possession of a counterfeit Government stamp",
  "defines": "s 259",
  "family": "government-stamps",
  "offenceFn": "offence under s 259",
  "chargeFn": "charge under s 259",
  "definitionFns": [
   "possesses a counterfeit Government stamp"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "260",
  "title": "using as genuine a Government stamp known to be counterfeit",
  "defines": "s 260",
  "family": "government-stamps",
  "offenceFn": "offence under s 260",
  "chargeFn": "charge under s 260",
  "definitionFns": [
   "uses as genuine a counterfeit Government stamp"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "261",
  "title": "effacing any writing from a substance bearing a Government stamp, or removing from a document a stamp used for it, with intent to cause loss to Government",
  "defines": "s 261",
  "family": "government-stamps",
  "offenceFn": "offence under s 261",
  "chargeFn": "charge under s 261",
  "definitionFns": [
   "removes writing from a Government stamp to cause loss to the Government"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "262",
  "title": "using a Government stamp known to have been before used",
  "defines": "s 262",
  "family": "government-stamps",
  "offenceFn": "offence under s 262",
  "chargeFn": "charge under s 262",
  "definitionFns": [
   "uses a Government stamp known to have been before used"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "263",
  "title": "erasure of mark denoting that stamp has been used",
  "defines": "s 263",
  "family": "government-stamps",
  "offenceFn": "offence under s 263",
  "chargeFn": "charge under s 263",
  "definitionFns": [
   "erases the used mark from a Government stamp"
  ],
  "factsType": "Government Stamp Facts",
  "factsParam": "f"
 },
 {
  "section": "267B",
  "title": "affray",
  "defines": "ss 267A, 267B",
  "family": "public-order",
  "offenceFn": "offence under s 267B",
  "chargeFn": "charge under s 267B",
  "definitionFns": [
   "commits an affray"
  ],
  "factsType": "Affray Facts",
  "factsParam": "f"
 },
 {
  "section": "267C",
  "title": "uttering words, making document, etc., containing incitement to violence",
  "defines": "s 267C",
  "family": "public-order",
  "offenceFn": "offence under s 267C",
  "chargeFn": "charge under s 267C",
  "definitionFns": [
   "utters words or makes a document containing incitement to violence"
  ],
  "factsType": "Incitement Facts",
  "factsParam": "f"
 },
 {
  "section": "268A",
  "title": "communicating false information of harmful thing",
  "defines": "s 268A",
  "family": "public-order",
  "offenceFn": "offence under s 268A",
  "chargeFn": "charge under s 268A",
  "definitionFns": [
   "communicates false information of a harmful thing"
  ],
  "factsType": "Harmful Thing Hoax Facts",
  "factsParam": "f"
 },
 {
  "section": "268B",
  "title": "placing or sending thing with intent to cause fear of harm",
  "defines": "s 268B",
  "family": "public-order",
  "offenceFn": "offence under s 268B",
  "chargeFn": "charge under s 268B",
  "definitionFns": [
   "places or sends a thing with intent to cause fear of harm"
  ],
  "factsType": "Harmful Thing Hoax Facts",
  "factsParam": "f"
 },
 {
  "section": "268C",
  "title": "placing or sending thing causing fear of harm",
  "defines": "s 268C",
  "family": "public-order",
  "offenceFn": "offence under s 268C",
  "chargeFn": "charge under s 268C",
  "definitionFns": [
   "places or sends a thing causing fear of harm"
  ],
  "factsType": "Harmful Thing Hoax Facts",
  "factsParam": "f"
 },
 {
  "section": "269",
  "title": "negligent act likely to spread infection of any disease dangerous to life",
  "defines": "s 269",
  "family": "public-health",
  "offenceFn": "offence under s 269",
  "chargeFn": "charge under s 269",
  "definitionFns": [
   "negligently does an act likely to spread infection"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "270",
  "title": "intentional or rash act likely to spread infection of any disease dangerous to life",
  "defines": "s 270",
  "family": "public-health",
  "offenceFn": "offence under s 270",
  "chargeFn": "charge under s 270",
  "definitionFns": [
   "intentionally does an act likely to spread infection"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "271",
  "title": "disobedience to a quarantine rule",
  "defines": "s 271",
  "family": "public-health",
  "offenceFn": "offence under s 271",
  "chargeFn": "charge under s 271",
  "definitionFns": [
   "disobeys a quarantine rule"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "272",
  "title": "adulteration of food or drink which is intended for sale",
  "defines": "s 272",
  "family": "public-health",
  "offenceFn": "offence under s 272",
  "chargeFn": "charge under s 272",
  "definitionFns": [
   "adulterates food or drink intended for sale"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "273",
  "title": "sale of noxious food or drink",
  "defines": "s 273",
  "family": "public-health",
  "offenceFn": "offence under s 273",
  "chargeFn": "charge under s 273",
  "definitionFns": [
   "sells noxious food or drink"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "274",
  "title": "adulteration of drugs",
  "defines": "s 274",
  "family": "public-health",
  "offenceFn": "offence under s 274",
  "chargeFn": "charge under s 274",
  "definitionFns": [
   "adulterates drugs"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "275",
  "title": "sale of adulterated drugs",
  "defines": "s 275",
  "family": "public-health",
  "offenceFn": "offence under s 275",
  "chargeFn": "charge under s 275",
  "definitionFns": [
   "sells adulterated drugs"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "276",
  "title": "sale of any drug as a different drug or preparation",
  "defines": "s 276",
  "family": "public-health",
  "offenceFn": "offence under s 276",
  "chargeFn": "charge under s 276",
  "definitionFns": [
   "sells a drug as a different drug"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "277",
  "title": "fouling the water of a public spring or reservoir",
  "defines": "s 277",
  "family": "public-health",
  "offenceFn": "offence under s 277",
  "chargeFn": "charge under s 277",
  "definitionFns": [
   "fouls the water of a public spring or reservoir"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "278",
  "title": "making atmosphere noxious to health",
  "defines": "s 278",
  "family": "public-health",
  "offenceFn": "offence under s 278",
  "chargeFn": "charge under s 278",
  "definitionFns": [
   "makes the atmosphere noxious to health"
  ],
  "factsType": "Public Health Facts",
  "factsParam": "f"
 },
 {
  "section": "279",
  "title": "rash driving or riding on a public way",
  "defines": "s 279",
  "family": "public-safety",
  "offenceFn": "offence under s 279",
  "chargeFn": "charge under s 279",
  "definitionFns": [
   "drives rashly on a public way"
  ],
  "factsType": "Rash Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "280",
  "title": "rash navigation of a vessel",
  "defines": "s 280",
  "family": "public-safety",
  "offenceFn": "offence under s 280",
  "chargeFn": "charge under s 280",
  "definitionFns": [
   "navigates a vessel rashly"
  ],
  "factsType": "Rash Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "281",
  "title": "exhibition of a false light, mark or buoy",
  "defines": "s 281",
  "family": "public-safety",
  "offenceFn": "offence under s 281",
  "chargeFn": "charge under s 281",
  "definitionFns": [
   "exhibits a false light, mark or buoy"
  ],
  "factsType": "Rash Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "282",
  "title": "conveying person by water for hire in a vessel overloaded or unsafe",
  "defines": "s 282",
  "family": "public-safety",
  "offenceFn": "offence under s 282",
  "chargeFn": "charge under s 282",
  "definitionFns": [
   "conveys a person by water in an unsafe vessel"
  ],
  "factsType": "Rash Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "283",
  "title": "danger or obstruction in a public way or navigation",
  "defines": "s 283",
  "family": "public-safety",
  "offenceFn": "offence under s 283",
  "chargeFn": "charge under s 283",
  "definitionFns": [
   "causes danger or obstruction in a public way"
  ],
  "factsType": "Rash Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "284",
  "title": "rash or negligent conduct with respect to dangerous or harmful substance",
  "defines": "s 284",
  "family": "public-safety",
  "offenceFn": "offence under s 284",
  "chargeFn": "charge under s 284",
  "definitionFns": [
   "does a rash act with a dangerous substance"
  ],
  "factsType": "Dangerous Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "285",
  "title": "causing or contributing to risk of dangerous fire",
  "defines": "s 285",
  "family": "public-safety",
  "offenceFn": "offence under s 285",
  "chargeFn": "charge under s 285",
  "definitionFns": [
   "causes or contributes to the risk of a dangerous fire",
   "is presumed to have substantially contributed to the risk of fire within section 286"
  ],
  "factsType": "Dangerous Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "287",
  "title": "rash or negligent conduct with respect to any machinery",
  "defines": "s 287",
  "family": "public-safety",
  "offenceFn": "offence under s 287",
  "chargeFn": "charge under s 287",
  "definitionFns": [
   "does a rash act with machinery"
  ],
  "factsType": "Dangerous Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "288",
  "title": "negligence in pulling down or repairing buildings",
  "defines": "s 288",
  "family": "public-safety",
  "offenceFn": "offence under s 288",
  "chargeFn": "charge under s 288",
  "definitionFns": [
   "omits precautions in pulling down or repairing a building"
  ],
  "factsType": "Dangerous Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "289",
  "title": "negligence with respect to any animal",
  "defines": "s 289",
  "family": "public-safety",
  "offenceFn": "offence under s 289",
  "chargeFn": "charge under s 289",
  "definitionFns": [
   "omits precautions with an animal"
  ],
  "factsType": "Dangerous Conduct Facts",
  "factsParam": "f"
 },
 {
  "section": "290",
  "title": "public nuisance",
  "defines": "ss 268, 290",
  "family": "public-order",
  "offenceFn": "offence under s 290",
  "chargeFn": "charge under s 290",
  "definitionFns": [
   "is guilty of a public nuisance"
  ],
  "factsType": "Public Nuisance Facts",
  "factsParam": "f"
 },
 {
  "section": "291",
  "title": "continuance of nuisance after injunction to discontinue",
  "defines": "s 291",
  "family": "public-order",
  "offenceFn": "offence under s 291",
  "chargeFn": "charge under s 291",
  "definitionFns": [
   "continues a public nuisance after injunction",
   "is guilty of a public nuisance"
  ],
  "factsType": "Public Nuisance Facts",
  "factsParam": "f"
 },
 {
  "section": "292",
  "title": "sale of obscene objects",
  "defines": "s 292",
  "family": "obscenity",
  "offenceFn": "offence under s 292",
  "chargeFn": "charge under s 292",
  "definitionFns": [
   "deals in an obscene object",
   "the object is obscene within section 292"
  ],
  "factsType": "Obscenity Facts",
  "factsParam": "f"
 },
 {
  "section": "292(1C)",
  "title": "distributing obscene objects by electronic means on 2 or more occasions",
  "defines": "s 292(1C)",
  "family": "obscenity",
  "offenceFn": "offence under s 292(1C)",
  "chargeFn": "charge under s 292(1C)",
  "definitionFns": [
   "the object is obscene within section 292"
  ],
  "factsType": "Obscenity Facts",
  "factsParam": "f"
 },
 {
  "section": "292A",
  "title": "possession, distribution, etc., of child sex-doll",
  "defines": "s 292A",
  "family": "obscenity",
  "offenceFn": "offence under s 292A",
  "chargeFn": "charge under s 292A",
  "definitionFns": [
   "deals in a child sex-doll"
  ],
  "factsType": "Obscenity Facts",
  "factsParam": "f"
 },
 {
  "section": "292B",
  "title": "obscene object on online location",
  "defines": "s 292B",
  "family": "obscenity",
  "offenceFn": "offence under s 292B",
  "chargeFn": "charge under s 292B",
  "definitionFns": [
   "runs an online location for obscene objects",
   "the object is obscene within section 292"
  ],
  "factsType": "Obscenity Facts",
  "factsParam": "f"
 },
 {
  "section": "293",
  "title": "sale, etc., of obscene objects to young person",
  "defines": "s 293",
  "family": "obscenity",
  "offenceFn": "offence under s 293",
  "chargeFn": "charge under s 293",
  "definitionFns": [
   "deals in an obscene object with a young person",
   "the object is obscene within section 292"
  ],
  "factsType": "Obscenity Facts",
  "factsParam": "f"
 },
 {
  "section": "294",
  "title": "obscene acts",
  "defines": "s 294",
  "family": "obscenity",
  "offenceFn": "offence under s 294",
  "chargeFn": "charge under s 294",
  "definitionFns": [
   "does an obscene act in a public place"
  ],
  "factsType": "Obscenity Facts",
  "factsParam": "f"
 },
 {
  "section": "298",
  "title": "uttering words, etc., with deliberate intent to wound the racial feelings of any person",
  "defines": "s 298",
  "family": "race",
  "offenceFn": "offence under s 298",
  "chargeFn": "charge under s 298",
  "definitionFns": [
   "wounds the racial feelings of a person"
  ],
  "factsType": "Racial Feelings Facts",
  "factsParam": "f"
 },
 {
  "section": "298A",
  "title": "promoting enmity between different groups on grounds of race and doing acts prejudicial to maintenance of harmony",
  "defines": "s 298A",
  "family": "race",
  "offenceFn": "offence under s 298A",
  "chargeFn": "charge under s 298A",
  "definitionFns": [
   "promotes enmity between racial groups"
  ],
  "factsType": "Racial Feelings Facts",
  "factsParam": "f"
 }
]
```
