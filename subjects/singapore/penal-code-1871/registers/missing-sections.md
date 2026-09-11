# Penal Code 1871 — missing-section register

**Run date:** 2026-09-11 (regenerated after the Chapter 16 pass, part 2)
**Question answered:** which live sections of the Act have no `@ref` in any `.l4` module,
named one by one with the Act's own marginal heading.

This is the companion to `coverage-register.md`. That register counts coverage and
enumerates the gaps only for the chapters that are partially encoded; for the thirteen
chapters where nothing is encoded it gives a section *range* and a total. This register
names all 325 missing sections, so that a reader deciding what to encode next is choosing
from a list rather than from a range.

**Method.** The arrangement of sections at the head of `registers/source-bundle/PC1871.txt`
(SSO current version as at 09 Sep 2026) was parsed for all 600 listed sections; the Act's
body was parsed independently for the same 600 and supplied the marginal headings. The two
passes agree on the section set exactly, which is the check that the parse is sound. Every
`@ref` in the twenty-three `.l4` modules was expanded (`ss X, Y, Z` lists, `ss X to Y` ranges,
parenthesised subsections and `Explanation N` / `Exception N` tails stripped) and matched
against that set.

Counts reproduce `coverage-register.md` exactly: **600 listed, 75 repealed, 525 live,**
**200 encoded, 325 not encoded.** Repealed sections are listed below for completeness but
are struck from every count.

As in the coverage register, this is a mechanical record of citation, not of fidelity.
A section counted as encoded has an `@ref`; whether the rule reads it correctly is answered
by `verification-register.md` and `verification-register-pass-2.md`.

---

Seven of the 325 are **deliberate** and documented in the module itself under their own
`§§` heading -- sections that state no factual test to decide. They are marked *deliberate*
in the tables below and explained in `coverage-register.md` §3. Discounting them, **318**
live sections are unencoded for reasons of scope rather than of drafting.

## 1. Missing sections by chapter

| chapter | live | encoded | **missing** |
| --- | ---: | ---: | ---: |
| **Chapter 1** — PRELIMINARY | 7 | 6 | 1 |
| **Chapter 2** — GENERAL EXPLANATIONS | 54 | 49 | 5 |
| **Chapter 3** — Punishments | 10 | 10 | 0 |
| **Chapter 4** — General Exceptions | 21 | 20 | 1 |
| **Chapter 4A** — Right of private defence | 12 | 12 | 0 |
| **Chapter 5** — Abetment | 16 | 7 | 9 |
| **Chapter 5A** — Criminal Conspiracy | 2 | 2 | 0 |
| **Chapter 6** — Offences against the State | 15 | 0 | 15 |
| **Chapter 6A** — Piracy | 2 | 0 | 2 |
| **Chapter 6B** — Genocide | 2 | 0 | 2 |
| **Chapter 7** — Offences relating to the armed forces | 12 | 0 | 12 |
| **Chapter 8** — Offences relating to unlawful assembly | 18 | 0 | 18 |
| **Chapter 9** — Offences by or relating to public servants | 11 | 0 | 11 |
| **Chapter 10** — Contempts of the lawful authority of public servants | 19 | 0 | 19 |
| **Chapter 11** — False evidence and offences against public justice | 43 | 0 | 43 |
| **Chapter 12** — Offences relating to government stamps | 9 | 0 | 9 |
| **Chapter 13** — *(wholly repealed)* | 0 | 0 | 0 |
| **Chapter 14** — Offences affecting the public tranquility, public health, safety, convenience, decency and morals | 35 | 0 | 35 |
| **Chapter 15** — Offences relating to race | 2 | 0 | 2 |
| **Chapter 16** — Offences affecting the human body | 120 | 74 | 46 |
| **Chapter 17** — Offences against property | 76 | 12 | 64 |
| **Chapter 18** — Offences relating to documents or electronic records, false instruments, and to currency and bank notes | 28 | 2 | 26 |
| **Chapter 20** — *(wholly repealed)* | 0 | 0 | 0 |
| **Chapter 21** — Defamation | 4 | 1 | 3 |
| **Chapter 22** — Criminal intimidation, insult and annoyance | 5 | 4 | 1 |
| **Chapter 23** — Attempts to commit offences | 2 | 1 | 1 |
| **total** | **525** | **200** | **325** |

---

## 2. The missing sections, named

Each table lists every live section of the chapter that no module cites. Sections already
encoded are omitted; repealed sections are omitted and noted in the chapter's preamble.

### Chapter 1 — PRELIMINARY

6 of 7 live sections encoded.

**1 missing:**

| s | heading | |
| --- | --- | --- |
| 1 | Short title | *deliberate* -- short title; no test to decide |

### Chapter 2 — GENERAL EXPLANATIONS

49 of 54 live sections encoded; 2 repealed and excluded.

**5 missing:**

| s | heading | |
| --- | --- | --- |
| 7 | Expression once explained is used in the same sense throughout this Code | *deliberate* -- rule of construction, no factual test |
| 8 | "Gender" | *deliberate* -- drafting convention; encoding is gender-neutral |
| 9 | "Number" | *deliberate* -- drafting convention (singular/plural) |
| 49 | "Year" and "month" | *deliberate* -- every period here is Gregorian by construction |
| 50 | "Section" | *deliberate* -- names a portion of a Chapter; no test |

### Chapter 3 — Punishments

10 of 10 live sections encoded; 3 repealed and excluded.

**Nothing missing — every live section in this chapter is cited.**

### Chapter 4 — General Exceptions

20 of 21 live sections encoded.

**1 missing:**

| s | heading | |
| --- | --- | --- |
| 79A | Mistake of law or ignorance of law not defence | *deliberate* -- closure rule, contributes no limb to the exceptions |

### Chapter 4A — Right of private defence

12 of 12 live sections encoded.

**Nothing missing — every live section in this chapter is cited.**

### Chapter 5 — Abetment

7 of 16 live sections encoded.

**9 missing:**

| s | heading | |
| --- | --- | --- |
| 109 | Punishment of abetment if the act abetted is committed in consequence, and where no express provision is made for its punishment |  |
| 110 | Punishment of abetment if the person abetted does the act with a different intention from that of the abettor |  |
| 112 | Abettor, when liable to cumulative punishment for act abetted and for act done |  |
| 115 | Abetment of offence punishable with death or imprisonment for life |  |
| 116 | Abetment of offence punishable with imprisonment |  |
| 117 | Abetting the commission of an offence by the public or by more than 10 persons |  |
| 118 | Concealing a design to commit an offence punishable with death or imprisonment for life |  |
| 119 | A public servant concealing a design to commit an offence which it is his duty to prevent |  |
| 120 | Concealing a design to commit an offence punishable with imprisonment |  |

### Chapter 5A — Criminal Conspiracy

2 of 2 live sections encoded.

**Nothing missing — every live section in this chapter is cited.**

### Chapter 6 — Offences against the State

0 of 15 live sections encoded.

**15 missing:**

| s | heading | |
| --- | --- | --- |
| 121 | Waging or attempting to wage war or abetting the waging of war against the Government |  |
| 121A | Offences against the President's person |  |
| 121B | Offences against authority |  |
| 121C | Abetting offences under section 121A or 121B |  |
| 121D | Intentional omission to give information of offences against section 121, 121A, 121B or 121C by a person bound to inform |  |
| 122 | Collecting arms, etc., with the intention of waging war against the Government |  |
| 123 | Concealing with intent to facilitate a design to wage war |  |
| 124 | Assaulting President, etc., with intent to compel or restrain the exercise of any lawful power |  |
| 125 | Waging war against any power in alliance or at peace with Singapore |  |
| 126 | Committing depredation on the territories of any power in alliance or at peace with Singapore |  |
| 127 | Receiving property taken by war or depredation mentioned in sections 125 and 126 |  |
| 128 | Public servant voluntarily allowing prisoner of State or war in his custody to escape |  |
| 129 | Public servant negligently suffering prisoner of State or war in his custody to escape |  |
| 130 | Aiding escape of, rescuing, or harbouring such prisoner |  |
| 130A | "Harbour" |  |

### Chapter 6A — Piracy

0 of 2 live sections encoded.

**2 missing:**

| s | heading | |
| --- | --- | --- |
| 130B | Piracy by law of nations. Cf. 12 and 13 Victoria c. 96 (Admiralty Offences (Colonial) Act 1849) |  |
| 130C | Piratical acts |  |

### Chapter 6B — Genocide

0 of 2 live sections encoded.

**2 missing:**

| s | heading | |
| --- | --- | --- |
| 130D | Genocide |  |
| 130E | Punishment for genocide |  |

### Chapter 7 — Offences relating to the armed forces

0 of 12 live sections encoded.

**12 missing:**

| s | heading | |
| --- | --- | --- |
| 131 | Abetting mutiny, or attempting to seduce an officer or a serviceman from his duty |  |
| 132 | Abetment of mutiny, if mutiny is committed in consequence thereof |  |
| 133 | Abetment of an assault by an officer or a serviceman on his superior officer, when in the execution of his office |  |
| 134 | Abetment of such assault, if the assault is committed |  |
| 135 | Abetment of the desertion of an officer or a serviceman |  |
| 136 | Harbouring a deserter |  |
| 137 | Deserter concealed on board merchant vessel through negligence of master |  |
| 138 | Abetment of act of insubordination by an officer or a serviceman |  |
| 139 | Saving |  |
| 140 | Wearing the dress of a serviceman |  |
| 140A | "Harbour" |  |
| 140B | Application of Chapter 7 to Singapore Police Force |  |

### Chapter 8 — Offences relating to unlawful assembly

0 of 18 live sections encoded; 3 repealed and excluded.

**18 missing:**

| s | heading | |
| --- | --- | --- |
| 141 | Unlawful assembly |  |
| 142 | Being a member of an unlawful assembly |  |
| 143 | Punishment |  |
| 144 | Joining an unlawful assembly armed with any deadly weapon |  |
| 145 | Joining or continuing in an unlawful assembly, knowing that it has been commanded to disperse |  |
| 146 | Force used by one member in prosecution of common object |  |
| 147 | Punishment for rioting |  |
| 148 | Rioting, armed with a deadly weapon |  |
| 149 | Every member of an unlawful assembly to be deemed guilty of any offence committed in prosecution of common object |  |
| 150 | Hiring, or conniving at hiring, of persons to join an unlawful assembly |  |
| 151 | Knowingly joining or continuing in any assembly of 5 or more persons after it has been commanded to disperse |  |
| 152 | Assaulting or obstructing public servant when suppressing riot, etc. |  |
| 153 | Intentionally or rashly giving provocation, with intent to cause riot |  |
| 154 | Owner or occupier of land on which an unlawful assembly is held |  |
| 155 | Liability of person for whose benefit a riot is committed |  |
| 156 | Liability of agent of owner or occupier for whose benefit a riot is committed |  |
| 157 | Harbouring persons hired for an unlawful assembly |  |
| 158 | Being hired to take part in an unlawful assembly or riot |  |

### Chapter 9 — Offences by or relating to public servants

0 of 11 live sections encoded.

**11 missing:**

| s | heading | |
| --- | --- | --- |
| 161 | Public servant taking a gratification, other than legal remuneration, in respect of an official act |  |
| 162 | Taking a gratification in order, by corrupt or illegal means, to influence a public servant |  |
| 163 | Taking a gratification, for the exercise of personal influence with a public servant |  |
| 164 | Punishment for abetment by public servant of the offences above defined |  |
| 165 | Public servant obtaining any valuable thing, without consideration, from person concerned in any proceeding or business transacted by such public servant |  |
| 166 | Public servant disobeying a direction of the law, with intent to cause injury to any person |  |
| 167 | Public servant framing an incorrect document or electronic record with intent to cause injury |  |
| 168 | Public servant unlawfully engaging in trade |  |
| 169 | Public servant unlawfully buying or bidding for property |  |
| 170 | Personating a public servant |  |
| 171 | Wearing garb or carrying token used by public servant, with fraudulent intent |  |

### Chapter 10 — Contempts of the lawful authority of public servants

0 of 19 live sections encoded.

**19 missing:**

| s | heading | |
| --- | --- | --- |
| 172 | Absconding to avoid arrest on warrant or service of summons, etc., proceeding from a public servant |  |
| 173 | Preventing service of summons, etc., or preventing publication thereof |  |
| 174 | Failure to attend in obedience to order from public servant |  |
| 175 | Omission to produce document or electronic record to public servant by person legally bound to produce such document or electronic record |  |
| 176 | Omission to give notice or information to public servant by person legally bound to give such notice or information |  |
| 177 | Furnishing false information |  |
| 178 | Refusing oath when duly required to take oath by a public servant |  |
| 179 | Refusing to answer public servant authorised to question |  |
| 180 | Refusing to sign statement |  |
| 181 | False statement on oath to public servant or person authorised to administer an oath |  |
| 182 | False information, with intent to cause a public servant to use his lawful power to the injury of another person |  |
| 183 | Resistance to taking of property by lawful authority of public servant |  |
| 184 | Obstructing sale of property offered for sale by authority of public servant |  |
| 185 | Illegal purchase or bid for property offered for sale by authority of public servant |  |
| 186 | Obstructing public servant in discharge of his public functions |  |
| 187 | Omission to assist public servant when bound by law to give assistance |  |
| 188 | Disobedience to order duly promulgated by public servant |  |
| 189 | Threat of injury to a public servant |  |
| 190 | Threat of injury to induce any person to refrain from applying for protection to a public servant |  |

### Chapter 11 — False evidence and offences against public justice

0 of 43 live sections encoded; 3 repealed and excluded.

**43 missing:**

| s | heading | |
| --- | --- | --- |
| 191 | Giving false evidence |  |
| 192 | Fabricating false evidence |  |
| 193 | Punishment for false evidence |  |
| 194 | Giving or fabricating false evidence with intent to procure conviction of a capital offence |  |
| 195 | Giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment |  |
| 196 | Using evidence known to be false |  |
| 197 | Issuing or signing a false certificate |  |
| 198 | Using as a true certificate one known to be false in a material point |  |
| 199 | False statement made in any declaration which is by law receivable as evidence |  |
| 200 | Using as true any such declaration known to be false |  |
| 201 | Causing disappearance of evidence of an offence committed, or giving false information touching it, to screen the offender |  |
| 202 | Intentional omission to give information of an offence, by person bound to inform |  |
| 203 | Giving false information respecting an offence committed |  |
| 204 | Destruction of document or electronic record to prevent its production as evidence |  |
| 204A | Obstructing, preventing, perverting or defeating course of justice |  |
| 204B | Bribery of witnesses |  |
| 205 | False personation for the purpose of any act or proceeding in a suit |  |
| 206 | Fraudulent removal or concealment of property to prevent its seizure as a forfeiture, in execution of a decree or under or pursuant to an enforcement order |  |
| 207 | Fraudulent claim to property to prevent its seizure as a forfeiture, in execution of a decree or under or pursuant to an enforcement order |  |
| 208 | Fraudulently suffering a decree for a sum not due |  |
| 210 | Fraudulently obtaining a decree for a sum not due |  |
| 211 | False charge of offence made with intent to injure |  |
| 212 | Harbouring an offender |  |
| 213 | Taking gifts, etc., to screen an offender from punishment |  |
| 214 | Offering gift or restoration of property in consideration of screening offender |  |
| 215 | Taking gift to help to recover stolen property, etc. |  |
| 216 | Harbouring an offender who has escaped from custody, or whose apprehension has been ordered |  |
| 216A | Harbouring robbers or gang-robbers, etc. |  |
| 216B | "Harbour" |  |
| 217 | Public servant disobeying a direction of law with intent to save person from punishment or property from forfeiture |  |
| 218 | Public servant framing an incorrect record or writing with intent to save person from punishment, or property from forfeiture |  |
| 219 | Public servant in a judicial proceeding making an order, etc., which he knows to be contrary to law |  |
| 220 | Commitment for trial or confinement by person having authority who knows he is acting contrary to law |  |
| 221 | Intentional omission to apprehend on the part of a public servant bound by law to apprehend |  |
| 222 | Intentional omission to apprehend on the part of a public servant bound by law to apprehend person under sentence of a court of justice |  |
| 223 | Escape from confinement negligently suffered by a public servant |  |
| 224 | Resistance or obstruction by a person to his lawful apprehension |  |
| 225 | Resistance or obstruction to the lawful apprehension of another person |  |
| 225A | Public servant omitting to apprehend or suffering other persons to escape in cases not already provided for |  |
| 225B | Resistance or obstruction to lawful apprehension, or escape, or rescue, in cases not otherwise provided for |  |
| 225C | Offences against laws of Singapore where no special punishment is provided |  |
| 228 | Intentional insult or interruption to a public servant sitting in any stage of a judicial proceeding or mediation or other alternative dispute resolution process |  |
| 229 | Personation of an assessor |  |

### Chapter 12 — Offences relating to government stamps

0 of 9 live sections encoded; 26 repealed and excluded.

**9 missing:**

| s | heading | |
| --- | --- | --- |
| 255 | Counterfeiting a Government stamp |  |
| 256 | Having possession of an instrument or material for the purpose of counterfeiting a Government stamp |  |
| 257 | Making or selling an instrument for the purpose of counterfeiting a Government stamp |  |
| 258 | Sale of counterfeit Government stamp |  |
| 259 | Having possession of a counterfeit Government stamp |  |
| 260 | Using as genuine a Government stamp known to be counterfeit |  |
| 261 | Effacing any writing from a substance bearing a Government stamp, or removing from a document a stamp used for it, with intent to cause loss to Government |  |
| 262 | Using a Government stamp known to have been before used |  |
| 263 | Erasure of mark denoting that stamp has been used |  |

### Chapter 13 — *(wholly repealed)*

All 4 sections repealed. Nothing to encode.

### Chapter 14 — Offences affecting the public tranquility, public health, safety, convenience, decency and morals

0 of 35 live sections encoded.

**35 missing:**

| s | heading | |
| --- | --- | --- |
| 267A | Affray |  |
| 267B | Punishment for committing affray |  |
| 267C | Uttering words, making document, etc., containing incitement to violence, etc. |  |
| 268 | Public nuisance |  |
| 268A | Communicating false information of harmful thing |  |
| 268B | Placing or sending thing with intent to cause fear of harm |  |
| 268C | Placing or sending thing causing fear of harm |  |
| 269 | Negligent act likely to spread infection of any disease dangerous to life |  |
| 270 | Intentional or rash act likely to spread infection of any disease dangerous to life |  |
| 271 | Disobedience to a quarantine rule |  |
| 272 | Adulteration of food or drink which is intended for sale |  |
| 273 | Sale of noxious food or drink |  |
| 274 | Adulteration of drugs |  |
| 275 | Sale of adulterated drugs |  |
| 276 | Sale of any drug as a different drug or preparation |  |
| 277 | Fouling the water of a public spring or reservoir |  |
| 278 | Making atmosphere noxious to health |  |
| 279 | Rash driving or riding on a public way |  |
| 280 | Rash navigation of a vessel |  |
| 281 | Exhibition of a false light, mark or buoy |  |
| 282 | Conveying person by water for hire in a vessel overloaded or unsafe |  |
| 283 | Danger or obstruction in a public way or navigation |  |
| 284 | Rash or negligent conduct with respect to dangerous or harmful substance |  |
| 285 | Causing or contributing to risk of dangerous fire |  |
| 286 | Presumption of cause of fire |  |
| 287 | Rash or negligent conduct with respect to any machinery in possession or under charge of offender |  |
| 288 | Negligence in pulling down or repairing buildings |  |
| 289 | Negligence with respect to any animal |  |
| 290 | Punishment for public nuisance |  |
| 291 | Continuance of nuisance after injunction to discontinue |  |
| 292 | Sale of obscene objects, etc. |  |
| 292A | Possession, distribution, etc., of child sex-doll |  |
| 292B | Obscene object on online location |  |
| 293 | Sale, etc., of obscene objects to young person |  |
| 294 | Obscene acts |  |

### Chapter 15 — Offences relating to race

0 of 2 live sections encoded; 3 repealed and excluded.

**2 missing:**

| s | heading | |
| --- | --- | --- |
| 298 | Uttering words, etc., with deliberate intent to wound the racial feelings of any person |  |
| 298A | Promoting enmity between different groups on grounds of race and doing acts prejudicial to maintenance of harmony |  |

### Chapter 16 — Offences affecting the human body

74 of 120 live sections encoded; 6 repealed and excluded.

**46 missing:**

| s | heading | |
| --- | --- | --- |
| 302 | Punishment for murder |  |
| 304 | Punishment for culpable homicide not amounting to murder |  |
| 311 | Punishment for infanticide |  |
| 323 | Punishment for voluntarily causing hurt |  |
| 325 | Punishment for voluntarily causing grievous hurt |  |
| 341 | Punishment for wrongful restraint |  |
| 342 | Punishment for wrongful confinement |  |
| 363 | Punishment for kidnapping |  |
| 363A | Punishment for abduction |  |
| 375 | Rape |  |
| 376 | Sexual assault involving penetration |  |
| 376A | Sexual penetration of minor below 16 years of age |  |
| 376AA | Exploitative sexual penetration of minor of or above 16 but below 18 years of age |  |
| 376B | Commercial sex with minor below 18 years of age |  |
| 376C | Commercial sex with minor below 18 years of age outside Singapore |  |
| 376D | Tour outside Singapore for commercial sex with minor below 18 years of age |  |
| 376E | Sexual grooming of minor below 16 years of age |  |
| 376EA | Exploitative sexual grooming of minor of or above 16 but below 18 years of age |  |
| 376EB | Sexual communication with minor below 16 years of age |  |
| 376EC | Exploitative sexual communication with minor of or above 16 but below 18 years of age |  |
| 376ED | Sexual activity or image in presence of minor below 16 years of age |  |
| 376EE | Exploitative sexual activity or image in presence of minor of or above 16 but below 18 years of age |  |
| 376F | Procurement of sexual activity with person with mental disability |  |
| 376G | Incest |  |
| 376H | Procurement of sexual activity by deception or false representation |  |
| 377 | Sexual penetration, etc., of a corpse |  |
| 377B | Sexual penetration with living animal |  |
| 377BA | Word or gesture intended to insult modesty of any person |  |
| 377BB | Voyeurism |  |
| 377BC | Distribution of voyeuristic image or recording |  |
| 377BD | Possession of or gaining access to voyeuristic or intimate image or recording and production of intimate image or recording |  |
| 377BE | Distributing or threatening to distribute intimate image or recording |  |
| 377BF | Sexual exposure |  |
| 377BG | Using or involving child in production of child abuse material |  |
| 377BH | Producing child abuse material |  |
| 377BI | Distributing or selling child abuse material |  |
| 377BJ | Advertising or seeking child abuse material |  |
| 377BK | Possession of or gaining access to child abuse material |  |
| 377BL | Exploitation by abusive material of minor of or above 16 but below 18 years of age |  |
| 377BM | Defences to offences relating to intimate image or recording and voyeurism |  |
| 377BN | Defences to child abuse material offences |  |
| 377BO | Child abuse material offences outside or partially outside Singapore |  |
| 377C | Interpretation of sections 375 to 377BO (sexual offences) |  |
| 377CA | Meaning of exploitative relationship |  |
| 377CB | Consent given under misconception in sexual offences |  |
| 377D | Mistake as to age in sexual offences |  |

### Chapter 17 — Offences against property

12 of 76 live sections encoded; 17 repealed and excluded.

**64 missing:**

| s | heading | |
| --- | --- | --- |
| 379 | Punishment for theft |  |
| 379A | Punishment for theft of a motor vehicle |  |
| 380 | Theft in dwelling house, etc. |  |
| 381 | Theft by clerk or servant of property in possession of master |  |
| 382 | Theft after preparation made for causing death or hurt in order to commit theft |  |
| 383 | Extortion |  |
| 384 | Punishment for extortion |  |
| 385 | Putting person in fear of harm in order to commit extortion |  |
| 386 | Extortion by putting a person in fear of death or grievous hurt |  |
| 387 | Putting person in fear of death or of grievous hurt in order to commit extortion |  |
| 388 | Extortion by threat of accusation of an offence punishable with death, or imprisonment, etc. |  |
| 389 | Putting person in fear of accusation of offence, in order to commit extortion |  |
| 390 | Robbery |  |
| 391 | Gang-robbery |  |
| 392 | Punishment for robbery |  |
| 393 | Attempt to commit robbery |  |
| 394 | Voluntarily causing hurt in committing robbery |  |
| 395 | Punishment for gang-robbery |  |
| 396 | Gang-robbery with murder |  |
| 397 | Robbery when armed or with attempt to cause death or grievous hurt |  |
| 399 | Making preparation to commit gang-robbery |  |
| 400 | Punishment for belonging to gang-robbers |  |
| 401 | Punishment for belonging to gang of thieves |  |
| 402 | Assembling for purpose of committing gang-robbery |  |
| 404 | Dishonest misappropriation of property possessed by a deceased person at the time of his death |  |
| 406 | Punishment of criminal breach of trust |  |
| 407 | Criminal breach of trust of property entrusted for purposes of transportation or storage |  |
| 408 | Criminal breach of trust by employees |  |
| 409 | Criminal breach of trust by public servant, or by banker, merchant, agent, director, officer, partner, key executive or fiduciary |  |
| 410 | Stolen property |  |
| 411 | Receiving stolen property |  |
| 412 | Receiving property stolen in the commission of a gang-robbery |  |
| 413 | Habitually dealing in stolen property |  |
| 414 | Assisting in concealment or disposal of stolen property |  |
| 417 | Punishment for cheating |  |
| 419 | Punishment for cheating by personation |  |
| 421 | Dishonest or fraudulent removal or concealment of property to prevent distribution among creditors |  |
| 422 | Dishonestly or fraudulently preventing a debt or demand due to the offender from being made available for his creditors |  |
| 423 | Dishonest or fraudulent execution of deed of transfer containing a false statement of consideration |  |
| 424 | Dishonest or fraudulent removal or concealment of property or release of claim |  |
| 425 | Mischief |  |
| 426 | Punishment for committing mischief |  |
| 427 | Punishment for committing mischief causing disruption to key service, etc. |  |
| 428 | Mischief by killing or maiming any animal |  |
| 435 | Mischief by fire or explosive substance with intent to cause damage |  |
| 436 | Mischief by fire or explosive substance with intent to destroy a house, etc. |  |
| 437 | Mischief with intent to destroy or make unsafe a decked vessel or a vessel of 20 tons burden |  |
| 438 | Punishment for the mischief described in section 437 when committed by fire or any explosive substance |  |
| 439 | Punishment for intentionally running vessel aground or ashore with intent to commit theft, etc. |  |
| 440 | Mischief committed after preparation made for causing death or hurt |  |
| 441 | Criminal trespass |  |
| 442 | House-breaking |  |
| 447 | Punishment for criminal trespass |  |
| 448 | Punishment for house-breaking |  |
| 449 | House-breaking in order to commit an offence punishable with death |  |
| 450 | House-breaking in order to commit an offence punishable with imprisonment for life |  |
| 451 | House-breaking in order to commit an offence punishable with imprisonment |  |
| 452 | House-breaking after preparation made for causing hurt, etc. |  |
| 453 | Possession of house-breaking implements or offensive weapons |  |
| 458A | Punishment for subsequent offence under section 449, 450, 451 or 452 |  |
| 459 | Grievous hurt caused while committing house-breaking |  |
| 460 | House-breaking when death or grievous hurt caused |  |
| 461 | Dishonestly breaking open any closed receptacle containing or supposed to contain property |  |
| 462 | Punishment for same offence when committed by person entrusted with custody |  |

### Chapter 18 — Offences relating to documents or electronic records, false instruments, and to currency and bank notes

2 of 28 live sections encoded.

**26 missing:**

| s | heading | |
| --- | --- | --- |
| 465 | Punishment for forgery |  |
| 466 | Forgery of a record of a court of justice, or a public register of births, etc. |  |
| 467 | Forgery of a valuable security or will |  |
| 468 | Forgery for the purpose of cheating |  |
| 469 | Forgery for the purpose of harming the reputation of any person |  |
| 470 | "A forged document" or "a forged electronic record" |  |
| 471 | Using as genuine a forged document or forged electronic record |  |
| 472 | Making or possessing a counterfeit seal, plate, etc., with intent to commit a forgery punishable under section 467 |  |
| 473 | Making or possessing a counterfeit seal, plate, etc., with intent to commit a forgery punishable otherwise |  |
| 473A | Making or possessing equipment for making a false instrument |  |
| 473B | Making or possessing equipment for making a false instrument with intent to induce prejudice |  |
| 473C | Meaning of "prejudice" and "induce" |  |
| 474 | Having possession of certain document or electronic record known to be forged, with intent to use it as genuine |  |
| 475 | Counterfeiting a device or mark used for authenticating documents described in section 467, or possessing counterfeit marked material |  |
| 476 | Counterfeiting a device or mark used for authenticating documents or electronic records other than those described in section 467, or possessing counterfeit marked material |  |
| 477 | Fraudulent cancellation, destruction, etc., of a will |  |
| 477A | Falsification of accounts |  |
| 489A | Forging or counterfeiting currency or bank notes |  |
| 489B | Using as genuine forged or counterfeit currency or bank notes |  |
| 489C | Possession of forged or counterfeit currency or bank notes |  |
| 489D | Making or possessing instruments or materials for forging or counterfeiting currency or bank notes |  |
| 489E | Abetting in Singapore counterfeiting of currency out of Singapore |  |
| 489F | Fraudulently or dishonestly diminishing weight or altering composition of any coin |  |
| 489G | Altering appearance of currency with intent that it shall pass as currency of different description |  |
| 489H | Delivery to another of altered currency |  |
| 489I | Possession of altered currency |  |

### Chapter 20 — *(wholly repealed)*

All 5 sections repealed. Nothing to encode.

### Chapter 21 — Defamation

1 of 4 live sections encoded.

**3 missing:**

| s | heading | |
| --- | --- | --- |
| 500 | Punishment for defamation |  |
| 501 | Printing or engraving matter known to be defamatory |  |
| 502 | Sale of printed or engraved substance containing defamatory matter |  |

### Chapter 22 — Criminal intimidation, insult and annoyance

4 of 5 live sections encoded; 3 repealed and excluded.

**1 missing:**

| s | heading | |
| --- | --- | --- |
| 507 | Criminal intimidation by an anonymous communication |  |

### Chapter 23 — Attempts to commit offences

1 of 2 live sections encoded.

**1 missing:**

| s | heading | |
| --- | --- | --- |
| 512 | Punishment for attempting to commit offences |  |

---

## 3. Repealed sections, for completeness

These 75 are listed in the Act's arrangement but have no content. They are excluded from
every count above, and nothing about them is a gap.


**Chapter 2** — 39, 52

**Chapter 3** — 57, 71, 75

**Chapter 8** — 151A, 159, 160

**Chapter 11** — 209, 226, 227

**Chapter 12** — 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 241A, 242, 243, 243A, 246, 247, 248, 249, 250, 251, 252, 253, 254, 254A

**Chapter 13** — 264, 265, 266, 267

**Chapter 15** — 295, 296, 297

**Chapter 16** — 309, 343, 344, 364A, 369, 377A

**Chapter 17** — 429, 430, 430A, 431, 431A, 432, 433, 434, 443, 444, 445, 446, 454, 455, 456, 457, 458

**Chapter 20** — 493, 494, 495, 496, 498

**Chapter 22** — 508, 509, 510

Beyond these, the Act's arrangement records nine ranges where section numbers were never
used or were wholly removed, and which therefore do not appear above at all:
ss 13–16, 18, 55–56, 58–70, 244–245, 303, 398, 478–489 and 497.

---

## 4. How to regenerate

Same method as `coverage-register.md` §7, with two refinements worth carrying over because
each one silently changed the counts when it was missing:

1. **Section numbers can carry up to three letters** (`377BM`, `377BN`, `377BO`). A
   `\d+[A-Z]?` pattern drops them and undercounts Chapter 16.
2. **The arrangement of sections wraps long headings**, so a wrapped line can begin with a
   number (`376D Tour ... minor below` / `18 years of age`) and read as a section. Section
   numbers ascend monotonically through the Act; rejecting any candidate that sorts below
   the previous one removes these without a hand-maintained exception list.

A citation of the form `s 120A(4) and (5)` must have **every** parenthesised group stripped,
not only the one adjoining the section number, or the trailing `(5)` reads as section 5.
`s 28 Explanation 2` needs the same treatment, and so does `s 300 Exception 1` and
`s 300 Exceptions 1 to 7` -- these number sub-provisions, not sections, and every one of
them reads as a low section number if left in. That trap cost a wrong count twice: once on
`Explanation`, and again on `Exception` when Chapter 16 was added.
