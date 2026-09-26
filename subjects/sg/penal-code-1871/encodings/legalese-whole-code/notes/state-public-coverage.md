# state-public — coverage

Penal Code 1871 (2020 RE, SSO as at 09 Sep 2026), Chapters 6, 6A, 6B, 7, 8, 9 and 10: ss 121–190, 82 sections.
Encoder: the state-public agent, 2026-09-26.
Status: **draft** — no domain expert has read it against the source.

## What is where

| module | covers |
| --- | --- |
| `deposit/pc-state-public-common.l4` | one shared helper (`the to-wit clause`), no section |
| `deposit/pc-state-public-state.l4` | Chapter 6 (ss 121–130A), 6A (ss 130B–130C), 6B (ss 130D–130E), 7 (ss 131–140B) |
| `deposit/pc-state-public-assembly.l4` | Chapter 8 (ss 141–160) |
| `deposit/pc-state-public-servants.l4` | Chapter 9 (ss 161–171) |
| `deposit/pc-state-public-contempts.l4` | Chapter 10 (ss 172–190) |
| `deposit/pc-state-public-tests.l4` | tests for all of the above |

**The `.l4` files are generated.** `python3 notes/state-public-gen/build.py` writes them from the hand-written ladders, leaves, recitals and tests in `notes/state-public-gen/part_*.py`; `lib.py` does only the mechanical layout (quoting each section's text from `inputs/PC1871.txt`, the `Punishment` records, the charge builders, the fixtures).
Edit the part files and rebuild — a hand-edit to a `.l4` is lost on the next build.
`python3 notes/state-public-gen/notes_gen.py` regenerates this file's table and catalogue block.
The build refuses a rule named like a field of any facts record (FORK SP-0).

## Numbers

`deposit/check.sh` over a copy of the group's modules plus `pc-domain.l4` and `pc-general.l4` (toolchain `l4-unstable-20260926-c76e6b0`, `JL4_LIBRARY_PATH` unset): **0 errors, 0 warnings, 151 assertions satisfied, 0 failed**, in `pc-state-public-tests.l4`; every other module 0 / 0.

- 79 sections encoded — 70 punishing sections carrying 76 punishing provisions, each with a facts record, an `offence under s N` and a `charge under s N`, and 9 definition / deeming / saving / application sections with no charge (said so in the table) — plus 3 repealed and **0 deferred**.
- **Defining predicates.** 52 of the 76 offence ladders call a separate `@export`ed defining predicate (the catalogue's `definitionFns`). The other 24 — ss 121A-121D, 122-130, 130C, 131-133, 135-138, 140, 168, 169 — are sections that define and punish in one clause and give the offence no verb of its own; their `offence under s N` ladder IS the defining ladder, and `definitionFns` is empty (FORK SP-2).
- Every Illustration in these chapters is an `#ASSERT`, cited: ss 121, 144 (and as applied to 148, 158), 161 (a)–(c), 163, 164, 165 (a)–(c), 166, 174 (a)–(b), 177, 182 (a)–(d), 186, 188.
  Explanations are encoded as leaf `@desc`s (ss 130, 141, 161, 177 for 176, 186(2), 188) or tested (s 130's parole Explanation; s 161's "expecting" and "legal remuneration" Explanations).
- Charges asserted as full text: ss 121, 147, 152, 161, 170, 177(2), 182, 186; refusals asserted as full text: ss 121, 147, 170, 174(1), 186.
- Thresholds: s 141 / s 151's "5 or more persons" through the helper `5 or more persons` (4 / 5 / 6). No other number is an element in these chapters; the fines and terms are punishment data, checked through pc-general's readers (s 41 on ss 147, 186(1)(a); `punishable with death or imprisonment for life` on s 121; `fixed by law or carries a minimum sentence` on ss 130B(2), 169).

## Cross-module joins owed (PLAN section 1)

Leaves standing for another group's section, each saying so in its `@desc`:

| leaf | record | section | owner | edge on PLAN's list? |
| --- | --- | --- | --- | --- |
| `abets the waging of such war`, `abets the commission of any of the offences punishable by section 121A or 121B`, `abets the committing of mutiny ...`, `abets an assault ...`, `abets the desertion ...`, `abets what he knows to be an act of insubordination ...`, `abets the offence` (s 164) | Waging War, Plot against the President, War against an Allied Power, Armed Forces, Gratification to Influence | s 107 | general-part | yes |
| `assaults` (ss 124, 152), `uses criminal force to such public servant`, `threatens or attempts to use criminal force to such public servant` | Assaulting the President, Obstructing Riot Suppression | ss 350, 351 | body-a | **no — state-public → body-a is not on the list** |
| `wrongfully restrains`, `attempts wrongfully to restrain` | Assaulting the President | s 339 | body-a | **no** |
| `while committing or attempting to commit piracy, murders or attempts to murder ...` | Piracy | s 300 | body-a | **no** (it chooses the punishment only) |
| `steals a Singapore ship`, `steals or without lawful authority throws overboard ...` | Piratical Acts | s 378 | property | **no — state-public → property is not on the list** |

The two missing edges (state-public → body-a, state-public → property) are proposed; neither creates a cycle with the listed edges (no listed edge leads from body-a or property back to state-public).
Chapter 2 words (s 21 public servant, s 26A voluntarily, ss 26C–26F, s 43 illegal / legally bound, s 44 injury) are flat leaves drilling into pc-general, as PLAN section 3.3 directs.

## `DEFINITION_LADDERS` entries

```ts
  { fn: 'public servant within section 21', leaf: 'public servant', section: '21' },
  { fn: 'public servant within section 21, for sections 175, 178, 179, 180 and 228', leaf: 'public servant', section: '21(2)' }, // Omission to Produce, Refusing Oath, Refusing to Answer, Refusing to Sign Facts only
  { fn: 'voluntarily within section 26A', leaf: 'voluntarily', section: '26A' },
  { fn: 'does the act intentionally within section 26C(1)', leaf: 'intentionally', section: '26C' },
  { fn: 'knowingly in respect of a circumstance within section 26D(1)', leaf: 'knowingly', section: '26D' },
  { fn: 'rashly in respect of a circumstance within section 26E(1)', leaf: 'rashly', section: '26E' },
  { fn: 'negligently within section 26F', leaf: 'negligently', section: '26F' },
  { fn: 'injury within section 44', leaf: 'injury to any person', section: '44' },
  { fn: 'unlawful assembly within section 141', leaf: 'unlawful assembly', section: '141' },   // Hiring for Unlawful Assembly Facts (s 150)
  { fn: 'harbours within section 130A', leaf: 'harbours or conceals any such prisoner who has escaped from lawful custody', section: '130A' },
  { fn: 'harbours within section 140A', leaf: 'harbours such officer or serviceman', section: '140A' },
```

The `public servant` leaf is keyed by record: the same leaf name drills into s 21(2)'s ladder for the four records s 21(2) names, and into s 21(1)'s for every other record.
The harbour ladders take their own `Harbour Facts`, not the offence record, so the drill-down is a separate card, not a toggle.

## Proposed shared nouns

None required. Candidates another group will want: a **vessel** (s 48; ss 130B–130C "Singapore ship", s 137 "merchant vessel" — here STRING particulars), a **weapon** (ss 144, 148, 158 — here a leaf plus a STRING; body-a's s 324 and property's s 397 need the same "deadly weapon / weapon of offence likely to cause death" test), and a **summons / order / process** (ss 172–174, 188 — here STRING particulars; justice-order will meet the same).

## The table

"offence" rows carry, in order, the defining predicate(s) the offence ladder calls (the catalogue's `definitionFns`), then each `offence under s N` and `charge under s N`.
Where a section punishes in (a) "in the case of an individual" / (b) "in any other case", one charge serves both and cites the paragraph from the leaf `the accused is an individual` (FORK SP-1).

| Ch | s | heading | disposition | kind | functions |
| --- | --- | --- | --- | --- | --- |
| 6 | 121 | Waging or attempting to wage war or abetting the waging of war against the Government | encoded | offence | `wages, attempts or abets war against the Government`, `offence under s 121`, `charge under s 121` |
| 6 | 121A | Offences against the President's person | encoded | offence | `offence under s 121A`, `charge under s 121A` |
| 6 | 121B | Offences against authority | encoded | offence | `offence under s 121B`, `charge under s 121B` |
| 6 | 121C | Abetting offences under section 121A or 121B | encoded | offence | `offence under s 121C`, `charge under s 121C` |
| 6 | 121D | Intentional omission to give information of offences against section 121, 121A, 121B or 121C by a person bound to inform | encoded | offence | `offence under s 121D`, `charge under s 121D` |
| 6 | 122 | Collecting arms, etc., with the intention of waging war against the Government | encoded | offence | `offence under s 122`, `charge under s 122` |
| 6 | 123 | Concealing with intent to facilitate a design to wage war | encoded | offence | `offence under s 123`, `charge under s 123` |
| 6 | 124 | Assaulting President, etc., with intent to compel or restrain the exercise of any lawful power | encoded | offence | `offence under s 124`, `charge under s 124` |
| 6 | 125 | Waging war against any power in alliance or at peace with Singapore | encoded | offence | `offence under s 125`, `charge under s 125` |
| 6 | 126 | Committing depredation on the territories of any power in alliance or at peace with Singapore | encoded | offence | `offence under s 126`, `charge under s 126` |
| 6 | 127 | Receiving property taken by war or depredation mentioned in sections 125 and 126 | encoded | offence | `offence under s 127`, `charge under s 127` |
| 6 | 128 | Public servant voluntarily allowing prisoner of State or war in his custody to escape | encoded | offence | `offence under s 128`, `charge under s 128` |
| 6 | 129 | Public servant negligently suffering prisoner of State or war in his custody to escape | encoded | offence | `offence under s 129`, `charge under s 129` |
| 6 | 130 | Aiding escape of, rescuing, or harbouring such prisoner | encoded | offence | `offence under s 130`, `charge under s 130` |
| 6 | 130A | "Harbour" | encoded | definition, no charge | `harbours within section 130A` |
| 6A | 130B | Piracy by law of nations. Cf. 12 and 13 Victoria c. 96 (Admiralty Offences (Colonial) Act 1849) | encoded | offence | `commits piracy`, `offence under s 130B(2)`, `charge under s 130B(2)` |
| 6A | 130C | Piratical acts | encoded | offence | `offence under s 130C`, `charge under s 130C` |
| 6B | 130D | Genocide | encoded | definition, no charge (punished by s 130E) | `commits genocide` |
| 6B | 130E | Punishment for genocide | encoded | offence | `commits genocide`, `offence under s 130E`, `charge under s 130E` |
| 7 | 131 | Abetting mutiny, or attempting to seduce an officer or a serviceman from his duty | encoded | offence | `offence under s 131`, `charge under s 131` |
| 7 | 132 | Abetment of mutiny, if mutiny is committed in consequence thereof | encoded | offence | `offence under s 132`, `charge under s 132` |
| 7 | 133 | Abetment of an assault by an officer or a serviceman on his superior officer, when in the execution of his office | encoded | offence | `offence under s 133`, `charge under s 133` |
| 7 | 134 | Abetment of such assault, if the assault is committed | encoded | offence | `offence under s 133`, `offence under s 134`, `charge under s 134` |
| 7 | 135 | Abetment of the desertion of an officer or a serviceman | encoded | offence | `offence under s 135`, `charge under s 135` |
| 7 | 136 | Harbouring a deserter | encoded | offence | `offence under s 136`, `charge under s 136` |
| 7 | 137 | Deserter concealed on board merchant vessel through negligence of master | encoded | offence | `offence under s 137`, `charge under s 137` |
| 7 | 138 | Abetment of act of insubordination by an officer or a serviceman | encoded | offence | `offence under s 138`, `charge under s 138` |
| 7 | 139 | Saving | encoded | saving (bar to punishment), no charge; not repeated in the Chapter 7 ladders (FORK SP-139) | `not subject to punishment under this Code within section 139` |
| 7 | 140 | Wearing the dress of a serviceman | encoded | offence | `offence under s 140`, `charge under s 140` |
| 7 | 140A | "Harbour" | encoded | definition, no charge | `harbours within section 140A` |
| 7 | 140B | Application of Chapter 7 to Singapore Police Force | encoded | application rule, no charge: the leaf `a member of the Singapore Police Force or any volunteer, auxiliary or special force attached to it`, ORed beside the armed-forces leaf in every Chapter 7 ladder |  |
| 8 | 141 | Unlawful assembly | encoded | definition, no charge; read by ss 143-158 and by other groups | `unlawful assembly within section 141`, `5 or more persons` |
| 8 | 142 | Being a member of an unlawful assembly | encoded | definition, no charge | `member of an unlawful assembly within section 142` |
| 8 | 143 | Punishment | encoded | offence | `member of an unlawful assembly within section 142`, `unlawful assembly within section 141`, `offence under s 143`, `charge under s 143` |
| 8 | 144 | Joining an unlawful assembly armed with any deadly weapon | encoded | offence | `member of an unlawful assembly within section 142`, `unlawful assembly within section 141`, `offence under s 144`, `charge under s 144` |
| 8 | 145 | Joining or continuing in an unlawful assembly, knowing that it has been commanded to disperse | encoded | offence | `unlawful assembly within section 141`, `offence under s 145`, `charge under s 145` |
| 8 | 146 | Force used by one member in prosecution of common object | encoded | definition of rioting, no charge (punished by ss 147, 148) | `guilty of rioting` |
| 8 | 147 | Punishment for rioting | encoded | offence | `guilty of rioting`, `member of an unlawful assembly within section 142`, `unlawful assembly within section 141`, `offence under s 147`, `charge under s 147` |
| 8 | 148 | Rioting, armed with a deadly weapon | encoded | offence | `guilty of rioting`, `member of an unlawful assembly within section 142`, `unlawful assembly within section 141`, `offence under s 148`, `charge under s 148` |
| 8 | 149 | Every member of an unlawful assembly to be deemed guilty of any offence committed in prosecution of common object | encoded | deeming rule, no charge of its own: charged as the other offence read with s 149 | `guilty of that offence within section 149` |
| 8 | 150 | Hiring, or conniving at hiring, of persons to join an unlawful assembly | encoded | offence | `hires persons to join an unlawful assembly`, `offence under s 150`, `charge under s 150` |
| 8 | 151 | Knowingly joining or continuing in any assembly of 5 or more persons after it has been commanded to disperse | encoded | offence | `joins an assembly commanded to disperse`, `offence under s 151`, `charge under s 151` |
| 8 | 151A | (Repealed) | repealed | [Repealed by Act 51 of 2007] |  |
| 8 | 152 | Assaulting or obstructing public servant when suppressing riot, etc. | encoded | offence | `assaults or obstructs a public servant suppressing a riot`, `offence under s 152`, `charge under s 152` |
| 8 | 153 | Intentionally or rashly giving provocation, with intent to cause riot | encoded | offence | `gives provocation with intent to cause riot`, `offence under s 153`, `charge under s 153` |
| 8 | 154 | Owner or occupier of land on which an unlawful assembly is held | encoded | offence | `owner or occupier fails to prevent or report an unlawful assembly`, `offence under s 154`, `charge under s 154` |
| 8 | 155 | Liability of person for whose benefit a riot is committed | encoded | offence | `riot committed for the benefit of that person`, `offence under s 155`, `charge under s 155` |
| 8 | 156 | Liability of agent of owner or occupier for whose benefit a riot is committed | encoded | offence | `riot committed for the benefit of that person`, `offence under s 156`, `charge under s 156` |
| 8 | 157 | Harbouring persons hired for an unlawful assembly | encoded | offence | `harbours persons hired for an unlawful assembly`, `offence under s 157`, `charge under s 157` |
| 8 | 158 | Being hired to take part in an unlawful assembly or riot | encoded | offence | `is hired to take part in an unlawful assembly`, `offence under s 158`, `charge under s 158` |
| 8 | 159 | (Repealed) | repealed | [Repealed by Act 51 of 2007] |  |
| 8 | 160 | (Repealed) | repealed | [Repealed by Act 51 of 2007] |  |
| 9 | 161 | Public servant taking a gratification, other than legal remuneration, in respect of an official act | encoded | offence | `takes a gratification in respect of an official act`, `offence under s 161`, `charge under s 161` |
| 9 | 162 | Taking a gratification in order, by corrupt or illegal means, to influence a public servant | encoded | offence | `takes a gratification to influence a public servant by corrupt means`, `offence under s 162`, `charge under s 162` |
| 9 | 163 | Taking a gratification, for the exercise of personal influence with a public servant | encoded | offence | `takes a gratification for personal influence with a public servant`, `offence under s 163`, `charge under s 163` |
| 9 | 164 | Punishment for abetment by public servant of the offences above defined | encoded | offence | `takes a gratification to influence a public servant by corrupt means`, `takes a gratification for personal influence with a public servant`, `offence under s 164`, `charge under s 164` |
| 9 | 165 | Public servant obtaining any valuable thing, without consideration, from person concerned in any proceeding or business transacted by such public servant | encoded | offence | `obtains a valuable thing from a person concerned in his business`, `offence under s 165`, `charge under s 165` |
| 9 | 166 | Public servant disobeying a direction of the law, with intent to cause injury to any person | encoded | offence | `disobeys a direction of the law with intent to cause injury`, `offence under s 166`, `charge under s 166` |
| 9 | 167 | Public servant framing an incorrect document or electronic record with intent to cause injury | encoded | offence | `frames an incorrect document with intent to cause injury`, `offence under s 167`, `charge under s 167` |
| 9 | 168 | Public servant unlawfully engaging in trade | encoded | offence | `offence under s 168`, `charge under s 168` |
| 9 | 169 | Public servant unlawfully buying or bidding for property | encoded | offence | `offence under s 169`, `charge under s 169` |
| 9 | 170 | Personating a public servant | encoded | offence | `personates a public servant`, `offence under s 170`, `charge under s 170` |
| 9 | 171 | Wearing garb or carrying token used by public servant, with fraudulent intent | encoded | offence | `wears the garb of a public servant`, `offence under s 171`, `charge under s 171` |
| 10 | 172 | Absconding to avoid arrest on warrant or service of summons, etc., proceeding from a public servant | encoded | offence | `absconds to avoid arrest or service`, `offence under s 172`, `charge under s 172` |
| 10 | 173 | Preventing service of summons, etc., or preventing publication thereof | encoded | offence | `prevents service or publication`, `offence under s 173(1)`, `charge under s 173(1)`, `offence under s 173(2)`, `charge under s 173(2)` |
| 10 | 174 | Failure to attend in obedience to order from public servant | encoded | offence | `fails to attend in obedience to an order from a public servant`, `offence under s 174(1)`, `charge under s 174(1)`, `offence under s 174(2)`, `charge under s 174(2)` |
| 10 | 175 | Omission to produce document or electronic record to public servant by person legally bound to produce such document or electronic record | encoded | offence | `omits to produce a document to a public servant`, `offence under s 175`, `charge under s 175` |
| 10 | 176 | Omission to give notice or information to public servant by person legally bound to give such notice or information | encoded | offence | `omits to give notice or information to a public servant`, `offence under s 176(1)`, `charge under s 176(1)`, `offence under s 176(2)`, `charge under s 176(2)` |
| 10 | 177 | Furnishing false information | encoded | offence | `furnishes false information to a public servant`, `offence under s 177(1)`, `charge under s 177(1)`, `offence under s 177(2)`, `charge under s 177(2)` |
| 10 | 178 | Refusing oath when duly required to take oath by a public servant | encoded | offence | `refuses an oath required by a public servant`, `offence under s 178`, `charge under s 178` |
| 10 | 179 | Refusing to answer public servant authorised to question | encoded | offence | `refuses to answer a public servant`, `offence under s 179`, `charge under s 179` |
| 10 | 180 | Refusing to sign statement | encoded | offence | `refuses to sign a statement`, `offence under s 180`, `charge under s 180` |
| 10 | 181 | False statement on oath to public servant or person authorised to administer an oath | encoded | offence | `makes a false statement on oath`, `offence under s 181`, `charge under s 181` |
| 10 | 182 | False information, with intent to cause a public servant to use his lawful power to the injury of another person | encoded | offence | `gives false information to a public servant`, `offence under s 182`, `charge under s 182` |
| 10 | 183 | Resistance to taking of property by lawful authority of public servant | encoded | offence | `resists the taking of property by a public servant`, `offence under s 183`, `charge under s 183` |
| 10 | 184 | Obstructing sale of property offered for sale by authority of public servant | encoded | offence | `obstructs a sale by a public servant`, `offence under s 184`, `charge under s 184` |
| 10 | 185 | Illegal purchase or bid for property offered for sale by authority of public servant | encoded | offence | `makes an illegal purchase or bid at a sale by a public servant`, `offence under s 185`, `charge under s 185` |
| 10 | 186 | Obstructing public servant in discharge of his public functions | encoded | offence | `voluntarily obstructs a public servant`, `offence under s 186`, `charge under s 186` |
| 10 | 187 | Omission to assist public servant when bound by law to give assistance | encoded | offence | `omits to assist a public servant`, `offence under s 187(1)`, `charge under s 187(1)`, `offence under s 187(2)`, `charge under s 187(2)` |
| 10 | 188 | Disobedience to order duly promulgated by public servant | encoded | offence | `disobeys an order duly promulgated by a public servant`, `offence under s 188(1)`, `charge under s 188(1)`, `offence under s 188(2)`, `charge under s 188(2)` |
| 10 | 189 | Threat of injury to a public servant | encoded | offence | `threatens a public servant`, `offence under s 189`, `charge under s 189` |
| 10 | 190 | Threat of injury to induce any person to refrain from applying for protection to a public servant | encoded | offence | `threatens a person to deter an application for protection`, `offence under s 190`, `charge under s 190` |

## Catalogue entries (`OFFENCES`, reference/charge-generator-catalogue.ts)

One per punishing provision, generated from the encoding by `notes/state-public-gen/notes_gen.py`.
Proposed new `family` slugs: `state`, `piracy`, `genocide`, `armed-forces`, `unlawful-assembly`, `public-servant`, `contempt`.

```ts
  {section: "172", title: "absconding to avoid arrest on a warrant or service of a summons, notice or order", defines: "s 172", family: "contempt", offenceFn: "offence under s 172", chargeFn: "charge under s 172", definitionFns: ["absconds to avoid arrest or service"], factsType: "Absconding Facts", factsParam: "f"},
  {section: "173(1)", title: "preventing the service of a summons, notice or order, or the making of a proclamation", defines: "s 173", family: "contempt", offenceFn: "offence under s 173(1)", chargeFn: "charge under s 173(1)", definitionFns: ["prevents service or publication"], factsType: "Preventing Service Facts", factsParam: "f"},
  {section: "173(2)", title: "preventing the service of a summons, notice or order to attend or produce before a court", defines: "s 173", family: "contempt", offenceFn: "offence under s 173(2)", chargeFn: "charge under s 173(2)", definitionFns: ["offence under s 173(1)", "prevents service or publication"], factsType: "Preventing Service Facts", factsParam: "f"},
  {section: "174(1)", title: "failure to attend in obedience to an order from a public servant", defines: "s 174", family: "contempt", offenceFn: "offence under s 174(1)", chargeFn: "charge under s 174(1)", definitionFns: ["fails to attend in obedience to an order from a public servant"], factsType: "Failure to Attend Facts", factsParam: "f"},
  {section: "174(2)", title: "failure to attend court in obedience to an order from a public servant", defines: "s 174", family: "contempt", offenceFn: "offence under s 174(2)", chargeFn: "charge under s 174(2)", definitionFns: ["offence under s 174(1)", "fails to attend in obedience to an order from a public servant"], factsType: "Failure to Attend Facts", factsParam: "f"},
  {section: "175", title: "omission to produce a document or electronic record to a public servant", defines: "s 175", family: "contempt", offenceFn: "offence under s 175", chargeFn: "charge under s 175", definitionFns: ["omits to produce a document to a public servant"], factsType: "Omission to Produce Facts", factsParam: "f"},
  {section: "176(1)", title: "omission to give notice or information to a public servant", defines: "s 176", family: "contempt", offenceFn: "offence under s 176(1)", chargeFn: "charge under s 176(1)", definitionFns: ["omits to give notice or information to a public servant"], factsType: "Omission to Inform Facts", factsParam: "f"},
  {section: "176(2)", title: "omission to give information to a public servant respecting an offence", defines: "s 176", family: "contempt", offenceFn: "offence under s 176(2)", chargeFn: "charge under s 176(2)", definitionFns: ["offence under s 176(1)", "omits to give notice or information to a public servant"], factsType: "Omission to Inform Facts", factsParam: "f"},
  {section: "177(1)", title: "furnishing false information to a public servant", defines: "s 177", family: "contempt", offenceFn: "offence under s 177(1)", chargeFn: "charge under s 177(1)", definitionFns: ["furnishes false information to a public servant"], factsType: "False Information Facts", factsParam: "f"},
  {section: "177(2)", title: "furnishing false information to a public servant respecting an offence", defines: "s 177", family: "contempt", offenceFn: "offence under s 177(2)", chargeFn: "charge under s 177(2)", definitionFns: ["offence under s 177(1)", "furnishes false information to a public servant"], factsType: "False Information Facts", factsParam: "f"},
  {section: "178", title: "refusing an oath when duly required by a public servant", defines: "s 178", family: "contempt", offenceFn: "offence under s 178", chargeFn: "charge under s 178", definitionFns: ["refuses an oath required by a public servant"], factsType: "Refusing Oath Facts", factsParam: "f"},
  {section: "179", title: "refusing to answer a public servant authorised to question", defines: "s 179", family: "contempt", offenceFn: "offence under s 179", chargeFn: "charge under s 179", definitionFns: ["refuses to answer a public servant"], factsType: "Refusing to Answer Facts", factsParam: "f"},
  {section: "180", title: "refusing to sign a statement", defines: "s 180", family: "contempt", offenceFn: "offence under s 180", chargeFn: "charge under s 180", definitionFns: ["refuses to sign a statement"], factsType: "Refusing to Sign Facts", factsParam: "f"},
  {section: "181", title: "false statement on oath to a public servant or a person authorised to administer an oath", defines: "s 181", family: "contempt", offenceFn: "offence under s 181", chargeFn: "charge under s 181", definitionFns: ["makes a false statement on oath"], factsType: "False Statement on Oath Facts", factsParam: "f"},
  {section: "182", title: "giving false information to a public servant", defines: "s 182", family: "contempt", offenceFn: "offence under s 182", chargeFn: "charge under s 182", definitionFns: ["gives false information to a public servant"], factsType: "False Information to Public Servant Facts", factsParam: "f"},
  {section: "183", title: "resistance to the taking of property by the lawful authority of a public servant", defines: "s 183", family: "contempt", offenceFn: "offence under s 183", chargeFn: "charge under s 183", definitionFns: ["resists the taking of property by a public servant"], factsType: "Resisting Taking of Property Facts", factsParam: "f"},
  {section: "184", title: "obstructing a sale of property offered for sale by the authority of a public servant", defines: "s 184", family: "contempt", offenceFn: "offence under s 184", chargeFn: "charge under s 184", definitionFns: ["obstructs a sale by a public servant"], factsType: "Obstructing Sale Facts", factsParam: "f"},
  {section: "185", title: "illegal purchase or bid for property offered for sale by the authority of a public servant", defines: "s 185", family: "contempt", offenceFn: "offence under s 185", chargeFn: "charge under s 185", definitionFns: ["makes an illegal purchase or bid at a sale by a public servant"], factsType: "Illegal Bid Facts", factsParam: "f"},
  {section: "186", title: "obstructing a public servant in the discharge of public functions", defines: "s 186", family: "contempt", offenceFn: "offence under s 186", chargeFn: "charge under s 186", definitionFns: ["voluntarily obstructs a public servant"], factsType: "Obstructing Public Servant Facts", factsParam: "f"},
  {section: "187(1)", title: "omission to assist a public servant when bound by law to give assistance", defines: "s 187", family: "contempt", offenceFn: "offence under s 187(1)", chargeFn: "charge under s 187(1)", definitionFns: ["omits to assist a public servant"], factsType: "Omission to Assist Facts", factsParam: "f"},
  {section: "187(2)", title: "omission to assist a public servant when demanded for the execution of process or the prevention of an offence", defines: "s 187", family: "contempt", offenceFn: "offence under s 187(2)", chargeFn: "charge under s 187(2)", definitionFns: ["offence under s 187(1)", "omits to assist a public servant"], factsType: "Omission to Assist Facts", factsParam: "f"},
  {section: "188(1)", title: "disobedience to an order duly promulgated by a public servant", defines: "s 188", family: "contempt", offenceFn: "offence under s 188(1)", chargeFn: "charge under s 188(1)", definitionFns: ["disobeys an order duly promulgated by a public servant"], factsType: "Disobedience to Order Facts", factsParam: "f"},
  {section: "188(2)", title: "disobedience to an order duly promulgated by a public servant, causing danger to human life, health or safety, or a riot or affray", defines: "s 188", family: "contempt", offenceFn: "offence under s 188(2)", chargeFn: "charge under s 188(2)", definitionFns: ["disobeys an order duly promulgated by a public servant"], factsType: "Disobedience to Order Facts", factsParam: "f"},
  {section: "189", title: "threat of injury to a public servant", defines: "s 189", family: "contempt", offenceFn: "offence under s 189", chargeFn: "charge under s 189", definitionFns: ["threatens a public servant"], factsType: "Threat to Public Servant Facts", factsParam: "f"},
  {section: "190", title: "threat of injury to induce a person to refrain from applying for protection to a public servant", defines: "s 190", family: "contempt", offenceFn: "offence under s 190", chargeFn: "charge under s 190", definitionFns: ["threatens a person to deter an application for protection"], factsType: "Threat to Deter Protection Facts", factsParam: "f"},
  {section: "143", title: "being a member of an unlawful assembly", defines: "ss 141, 142, 143", family: "unlawful-assembly", offenceFn: "offence under s 143", chargeFn: "charge under s 143", definitionFns: ["member of an unlawful assembly within section 142", "unlawful assembly within section 141"], factsType: "Unlawful Assembly Facts", factsParam: "f"},
  {section: "144", title: "joining an unlawful assembly armed with a deadly weapon", defines: "ss 141, 142, 144", family: "unlawful-assembly", offenceFn: "offence under s 144", chargeFn: "charge under s 144", definitionFns: ["member of an unlawful assembly within section 142", "unlawful assembly within section 141"], factsType: "Unlawful Assembly Facts", factsParam: "f"},
  {section: "145", title: "joining or continuing in an unlawful assembly, knowing that it has been commanded to disperse", defines: "ss 141, 145", family: "unlawful-assembly", offenceFn: "offence under s 145", chargeFn: "charge under s 145", definitionFns: ["unlawful assembly within section 141"], factsType: "Unlawful Assembly Facts", factsParam: "f"},
  {section: "147", title: "rioting", defines: "ss 141, 142, 146, 147", family: "unlawful-assembly", offenceFn: "offence under s 147", chargeFn: "charge under s 147", definitionFns: ["guilty of rioting", "member of an unlawful assembly within section 142", "unlawful assembly within section 141"], factsType: "Unlawful Assembly Facts", factsParam: "f"},
  {section: "148", title: "rioting, armed with a deadly weapon", defines: "ss 141, 142, 146, 148", family: "unlawful-assembly", offenceFn: "offence under s 148", chargeFn: "charge under s 148", definitionFns: ["guilty of rioting", "member of an unlawful assembly within section 142", "unlawful assembly within section 141"], factsType: "Unlawful Assembly Facts", factsParam: "f"},
  {section: "150", title: "hiring persons to join an unlawful assembly", defines: "s 150", family: "unlawful-assembly", offenceFn: "offence under s 150", chargeFn: "charge under s 150", definitionFns: ["hires persons to join an unlawful assembly"], factsType: "Hiring for Unlawful Assembly Facts", factsParam: "f"},
  {section: "151", title: "knowingly joining or continuing in an assembly of 5 or more persons after it has been commanded to disperse", defines: "s 151", family: "unlawful-assembly", offenceFn: "offence under s 151", chargeFn: "charge under s 151", definitionFns: ["joins an assembly commanded to disperse"], factsType: "Assembly Commanded to Disperse Facts", factsParam: "f"},
  {section: "152", title: "assaulting or obstructing a public servant when suppressing a riot", defines: "s 152", family: "unlawful-assembly", offenceFn: "offence under s 152", chargeFn: "charge under s 152", definitionFns: ["assaults or obstructs a public servant suppressing a riot"], factsType: "Obstructing Riot Suppression Facts", factsParam: "f"},
  {section: "153", title: "giving provocation with intent to cause riot", defines: "s 153", family: "unlawful-assembly", offenceFn: "offence under s 153", chargeFn: "charge under s 153", definitionFns: ["gives provocation with intent to cause riot"], factsType: "Provocation to Riot Facts", factsParam: "f"},
  {section: "154", title: "failure by the owner or occupier of land to report or suppress an unlawful assembly or riot", defines: "s 154", family: "unlawful-assembly", offenceFn: "offence under s 154", chargeFn: "charge under s 154", definitionFns: ["owner or occupier fails to prevent or report an unlawful assembly"], factsType: "Land of Unlawful Assembly Facts", factsParam: "f"},
  {section: "155", title: "failure by the person for whose benefit a riot is committed to prevent it", defines: "s 155", family: "unlawful-assembly", offenceFn: "offence under s 155", chargeFn: "charge under s 155", definitionFns: ["riot committed for the benefit of that person"], factsType: "Riot for Benefit Facts", factsParam: "f"},
  {section: "156", title: "failure by the agent or manager of the person for whose benefit a riot is committed to prevent it", defines: "s 156", family: "unlawful-assembly", offenceFn: "offence under s 156", chargeFn: "charge under s 156", definitionFns: ["riot committed for the benefit of that person"], factsType: "Riot for Benefit Facts", factsParam: "f"},
  {section: "157", title: "harbouring persons hired for an unlawful assembly", defines: "s 157", family: "unlawful-assembly", offenceFn: "offence under s 157", chargeFn: "charge under s 157", definitionFns: ["harbours persons hired for an unlawful assembly"], factsType: "Harbouring Hired Persons Facts", factsParam: "f"},
  {section: "158", title: "being hired to take part in an unlawful assembly or riot", defines: "s 158", family: "unlawful-assembly", offenceFn: "offence under s 158", chargeFn: "charge under s 158", definitionFns: ["is hired to take part in an unlawful assembly"], factsType: "Hired for Unlawful Assembly Facts", factsParam: "f"},
  {section: "161", title: "public servant taking a gratification, other than legal remuneration, in respect of an official act", defines: "s 161", family: "public-servant", offenceFn: "offence under s 161", chargeFn: "charge under s 161", definitionFns: ["takes a gratification in respect of an official act"], factsType: "Official Gratification Facts", factsParam: "f"},
  {section: "162", title: "taking a gratification in order, by corrupt or illegal means, to influence a public servant", defines: "s 162", family: "public-servant", offenceFn: "offence under s 162", chargeFn: "charge under s 162", definitionFns: ["takes a gratification to influence a public servant by corrupt means"], factsType: "Gratification to Influence Facts", factsParam: "f"},
  {section: "163", title: "taking a gratification for the exercise of personal influence with a public servant", defines: "s 163", family: "public-servant", offenceFn: "offence under s 163", chargeFn: "charge under s 163", definitionFns: ["takes a gratification for personal influence with a public servant"], factsType: "Gratification to Influence Facts", factsParam: "f"},
  {section: "164", title: "abetment by a public servant of an offence under section 162 or 163", defines: "ss 162, 163, 164", family: "public-servant", offenceFn: "offence under s 164", chargeFn: "charge under s 164", definitionFns: ["takes a gratification to influence a public servant by corrupt means", "takes a gratification for personal influence with a public servant"], factsType: "Gratification to Influence Facts", factsParam: "f"},
  {section: "165", title: "public servant obtaining a valuable thing, without consideration, from a person concerned in business transacted by him", defines: "s 165", family: "public-servant", offenceFn: "offence under s 165", chargeFn: "charge under s 165", definitionFns: ["obtains a valuable thing from a person concerned in his business"], factsType: "Valuable Thing Facts", factsParam: "f"},
  {section: "166", title: "public servant disobeying a direction of the law, with intent to cause injury", defines: "s 166", family: "public-servant", offenceFn: "offence under s 166", chargeFn: "charge under s 166", definitionFns: ["disobeys a direction of the law with intent to cause injury"], factsType: "Disobeying Direction of Law Facts", factsParam: "f"},
  {section: "167", title: "public servant framing an incorrect document or electronic record with intent to cause injury", defines: "s 167", family: "public-servant", offenceFn: "offence under s 167", chargeFn: "charge under s 167", definitionFns: ["frames an incorrect document with intent to cause injury"], factsType: "Incorrect Document Facts", factsParam: "f"},
  {section: "168", title: "public servant unlawfully engaging in trade", defines: "s 168", family: "public-servant", offenceFn: "offence under s 168", chargeFn: "charge under s 168", definitionFns: [], factsType: "Public Servant Trading Facts", factsParam: "f"},
  {section: "169", title: "public servant unlawfully buying or bidding for property", defines: "s 169", family: "public-servant", offenceFn: "offence under s 169", chargeFn: "charge under s 169", definitionFns: [], factsType: "Public Servant Trading Facts", factsParam: "f"},
  {section: "170", title: "personating a public servant", defines: "s 170", family: "public-servant", offenceFn: "offence under s 170", chargeFn: "charge under s 170", definitionFns: ["personates a public servant"], factsType: "Personation of Public Servant Facts", factsParam: "f"},
  {section: "171", title: "wearing the garb or carrying the token of a public servant with fraudulent intent", defines: "s 171", family: "public-servant", offenceFn: "offence under s 171", chargeFn: "charge under s 171", definitionFns: ["wears the garb of a public servant"], factsType: "Public Servant Garb Facts", factsParam: "f"},
  {section: "121", title: "waging or attempting to wage war or abetting the waging of war against the Government", defines: "s 121", family: "state", offenceFn: "offence under s 121", chargeFn: "charge under s 121", definitionFns: ["wages, attempts or abets war against the Government"], factsType: "Waging War Facts", factsParam: "f"},
  {section: "121A", title: "offences against the President's person", defines: "s 121A", family: "state", offenceFn: "offence under s 121A", chargeFn: "charge under s 121A", definitionFns: [], factsType: "Plot against the President Facts", factsParam: "f"},
  {section: "121B", title: "offences against authority", defines: "s 121B", family: "state", offenceFn: "offence under s 121B", chargeFn: "charge under s 121B", definitionFns: [], factsType: "Plot against the President Facts", factsParam: "f"},
  {section: "121C", title: "abetting an offence under section 121A or 121B", defines: "s 121C", family: "state", offenceFn: "offence under s 121C", chargeFn: "charge under s 121C", definitionFns: [], factsType: "Plot against the President Facts", factsParam: "f"},
  {section: "121D", title: "intentional omission to give information of an offence against the State", defines: "s 121D", family: "state", offenceFn: "offence under s 121D", chargeFn: "charge under s 121D", definitionFns: [], factsType: "Omission to Inform of Offence against the State Facts", factsParam: "f"},
  {section: "122", title: "collecting arms with the intention of waging war against the Government", defines: "s 122", family: "state", offenceFn: "offence under s 122", chargeFn: "charge under s 122", definitionFns: [], factsType: "Preparing War Facts", factsParam: "f"},
  {section: "123", title: "concealing with intent to facilitate a design to wage war", defines: "s 123", family: "state", offenceFn: "offence under s 123", chargeFn: "charge under s 123", definitionFns: [], factsType: "Concealing Design to Wage War Facts", factsParam: "f"},
  {section: "124", title: "assaulting the President or a Member of Parliament with intent to compel or restrain the exercise of lawful power", defines: "s 124", family: "state", offenceFn: "offence under s 124", chargeFn: "charge under s 124", definitionFns: [], factsType: "Assaulting the President Facts", factsParam: "f"},
  {section: "125", title: "waging war against a power in alliance or at peace with Singapore", defines: "s 125", family: "state", offenceFn: "offence under s 125", chargeFn: "charge under s 125", definitionFns: [], factsType: "War against an Allied Power Facts", factsParam: "f"},
  {section: "126", title: "committing depredation on the territories of a power at peace with Singapore", defines: "s 126", family: "state", offenceFn: "offence under s 126", chargeFn: "charge under s 126", definitionFns: [], factsType: "War against an Allied Power Facts", factsParam: "f"},
  {section: "127", title: "receiving property taken by war or depredation", defines: "s 127", family: "state", offenceFn: "offence under s 127", chargeFn: "charge under s 127", definitionFns: [], factsType: "War against an Allied Power Facts", factsParam: "f"},
  {section: "128", title: "public servant voluntarily allowing a prisoner of State or war in his custody to escape", defines: "s 128", family: "state", offenceFn: "offence under s 128", chargeFn: "charge under s 128", definitionFns: [], factsType: "Prisoner of State Custody Facts", factsParam: "f"},
  {section: "129", title: "public servant negligently suffering a prisoner of State or war in his custody to escape", defines: "s 129", family: "state", offenceFn: "offence under s 129", chargeFn: "charge under s 129", definitionFns: [], factsType: "Prisoner of State Custody Facts", factsParam: "f"},
  {section: "130", title: "aiding the escape of, rescuing or harbouring a prisoner of State or war", defines: "s 130", family: "state", offenceFn: "offence under s 130", chargeFn: "charge under s 130", definitionFns: [], factsType: "Aiding Escape of Prisoner of State Facts", factsParam: "f"},
  {section: "130B(2)", title: "piracy by the law of nations", defines: "ss 130B, 130B(1)", family: "piracy", offenceFn: "offence under s 130B(2)", chargeFn: "charge under s 130B(2)", definitionFns: ["commits piracy"], factsType: "Piracy Facts", factsParam: "f"},
  {section: "130C", title: "piratical acts", defines: "s 130C", family: "piracy", offenceFn: "offence under s 130C", chargeFn: "charge under s 130C", definitionFns: [], factsType: "Piratical Acts Facts", factsParam: "f"},
  {section: "130E", title: "genocide", defines: "ss 130D, 130E", family: "genocide", offenceFn: "offence under s 130E", chargeFn: "charge under s 130E", definitionFns: ["commits genocide"], factsType: "Genocide Facts", factsParam: "f"},
  {section: "131", title: "abetting mutiny, or attempting to seduce an officer or a serviceman from his duty", defines: "s 131", family: "armed-forces", offenceFn: "offence under s 131", chargeFn: "charge under s 131", definitionFns: [], factsType: "Armed Forces Facts", factsParam: "f"},
  {section: "132", title: "abetment of mutiny, mutiny being committed in consequence", defines: "s 132", family: "armed-forces", offenceFn: "offence under s 132", chargeFn: "charge under s 132", definitionFns: [], factsType: "Armed Forces Facts", factsParam: "f"},
  {section: "133", title: "abetment of an assault by an officer or a serviceman on a superior officer", defines: "s 133", family: "armed-forces", offenceFn: "offence under s 133", chargeFn: "charge under s 133", definitionFns: [], factsType: "Armed Forces Facts", factsParam: "f"},
  {section: "134", title: "abetment of an assault by an officer or a serviceman on a superior officer, the assault being committed", defines: "s 134", family: "armed-forces", offenceFn: "offence under s 134", chargeFn: "charge under s 134", definitionFns: ["offence under s 133"], factsType: "Armed Forces Facts", factsParam: "f"},
  {section: "135", title: "abetment of the desertion of an officer or a serviceman", defines: "s 135", family: "armed-forces", offenceFn: "offence under s 135", chargeFn: "charge under s 135", definitionFns: [], factsType: "Armed Forces Facts", factsParam: "f"},
  {section: "136", title: "harbouring a deserter", defines: "s 136", family: "armed-forces", offenceFn: "offence under s 136", chargeFn: "charge under s 136", definitionFns: [], factsType: "Armed Forces Facts", factsParam: "f"},
  {section: "137", title: "deserter concealed on board a merchant vessel through the negligence of the master", defines: "s 137", family: "armed-forces", offenceFn: "offence under s 137", chargeFn: "charge under s 137", definitionFns: [], factsType: "Deserter on Merchant Vessel Facts", factsParam: "f"},
  {section: "138", title: "abetment of an act of insubordination by an officer or a serviceman", defines: "s 138", family: "armed-forces", offenceFn: "offence under s 138", chargeFn: "charge under s 138", definitionFns: [], factsType: "Armed Forces Facts", factsParam: "f"},
  {section: "140", title: "wearing the dress of a serviceman", defines: "s 140", family: "armed-forces", offenceFn: "offence under s 140", chargeFn: "charge under s 140", definitionFns: [], factsType: "Serviceman Garb Facts", factsParam: "f"},
```
