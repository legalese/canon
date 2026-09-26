# body-a coverage - Penal Code 1871, Chapter 16, ss 299-358

Group body-a: Chapter 16 from "Offences affecting life" to "Criminal force and assault".
Modules: `deposit/pc-body-a-life.l4` (ss 299-318), `deposit/pc-body-a-hurt.l4` (ss 319-338), `deposit/pc-body-a-force.l4` (ss 339-358), tests in `deposit/pc-body-a-tests.l4`.
Source: `inputs/PC1871.txt` (SSO, current version as at 09 Sep 2026).

Row count: 70 rows - 56 encoded, 10 deferred, 3 repealed, 1 not a section (s 303).

What `deposit/check.sh` printed over these modules (run on a copy of pc-domain, pc-general and the four body-a files only, `JL4_LIBRARY_PATH` unset, 2026-09-26): 0 errors, 146 assertions satisfied, 0 failed; the three encoding modules are also free of linter warnings.
One assertion failed on the first run - `offence under s 354(2)` on the lift fixture - because the fixture omitted the s 350 purpose; the expected value was not changed, the fixture was completed (F-8). That failure is also the positive control that the harness can fail.

| s | heading | disposition | module | functions / reason |
| --- | --- | --- | --- | --- |
| 299 | Culpable homicide | encoded | pc-body-a-life.l4 | `commits culpable homicide` (defining; no charge of its own - punished under s 304) |
| 300 | Murder | encoded | pc-body-a-life.l4 | `murder within the meaning of section 300(a)`..`(d)`, `commits murder`, `Exception 1 to section 300 applies`..`Exception 7 ...`, `an Exception to section 300 applies`, `commits culpable homicide not amounting to murder`, helpers `above 18 years of age`, `below 12 months of age` (defining; punished under s 302) |
| 301 | Culpable homicide by causing the death of a person other than the person whose death was intended | deferred | pc-body-a-life.l4 | Deeming rule with no charge of its own (F-9). Already encoded in the reference row's `culpable-homicide-301.l4`; not re-encoded for time. s 26G(5)/301(2) wiring is the exceptions group's (PLAN §5). |
| 302 | Punishment for murder | encoded | pc-body-a-life.l4 | `offence under s 302(1)`, `charge under s 302(1)`, `offence under s 302(2)`, `charge under s 302(2)` |
| 303 | [There is no section 303] | n/a | - | The Code prints "[There is no section 303.]" |
| 304 | Punishment for culpable homicide not amounting to murder | encoded | pc-body-a-life.l4 | `offence under s 304(a)`, `charge under s 304(a)`, `offence under s 304(b)`, `charge under s 304(b)` |
| 304A | Causing death by rash or negligent act | encoded | pc-body-a-life.l4 | `offence under s 304A(a)`, `charge under s 304A(a)`, `offence under s 304A(b)`, `charge under s 304A(b)` (over `Rash Act Facts` from pc-body-a-hurt) |
| 304B | Causing death of child below 14, domestic worker or vulnerable person by sustained abuse | deferred | - | Time; also needs "domestic worker" (s 73(4)) and "vulnerable person" (s 74A(5)), which are general-part's, and a course-of-conduct count ("2 or more occasions") that must be a BOOLEAN leaf with a helper. |
| 304C | Causing or allowing death of child below 14, domestic worker or vulnerable person in same household | deferred | - | Time; same dependency on ss 73(4), 74A(5); subsection (2)'s either-limb rule and (3)'s defence need care. |
| 305 | Abetment of suicide or attempted suicide of minor or person who lacks mental capacity | encoded | pc-body-a-life.l4 | `offence under s 305(1)(a)`/`(b)`/`(c)`, `charge under s 305(1)(a)`/`(b)`/`(c)`, helper `below 18 years of age` |
| 306 | Abetment of suicide or attempted suicide | encoded | pc-body-a-life.l4 | `offence under s 306`, `charge under s 306` |
| 307 | Attempt to murder | encoded | pc-body-a-life.l4 | `offence under s 307(1)`, `charge under s 307(1)` (hurt limb chooses the punishment), `offence under s 307(2)`, `charge under s 307(2)` |
| 308 | Attempt to commit culpable homicide | encoded | pc-body-a-life.l4 | `offence under s 308`, `charge under s 308` (hurt limb chooses the punishment) |
| 308A | Causing death in furtherance of group's object | deferred | - | Time; "group" is defined by the Organised Crime Act 2015 s 2(1), not in this job's inputs. |
| 308B | Concealment, desecration or disposal of corpse | encoded | pc-body-a-life.l4 | `offence under s 308B`, `charge under s 308B` (charged as punishable under s 308B(2)) |
| 309 | (Repealed) | repealed | - | [Repealed by Act 15 of 2019] |
| 310 | Infanticide | deferred | - | Time. Its conditions are encoded as s 300 Exception 6 (the murder question); the offence and its charge are not. |
| 311 | Punishment for infanticide | deferred | - | Time; follows s 310. |
| 312 | Causing miscarriage | encoded | pc-body-a-life.l4 | `offence under s 312`, `charge under s 312` (the >16-weeks limb chooses the punishment), helper `more than 16 weeks' duration`. The Termination of Pregnancy Act 1974 is a leaf, not encoded. |
| 313 | Causing miscarriage without woman's consent | encoded | pc-body-a-life.l4 | `offence under s 313`, `charge under s 313` |
| 314 | Death caused by act done with intent to cause miscarriage | deferred | - | Time. |
| 315 | Child destruction before, at or immediately after birth | deferred | - | Time; subsection (2) is an evidential presumption (28 weeks) - needs source-pattern 07. |
| 316 | Causing death of a quick unborn child by an act amounting to culpable homicide | deferred | - | Time. |
| 317 | Exposure and abandonment of a child below 12 years of age | encoded | pc-body-a-life.l4 | `offence under s 317`, `charge under s 317`, helper `below 12 years of age` |
| 318 | Concealment of birth by secret disposal of dead body | encoded | pc-body-a-life.l4 | `offence under s 318`, `charge under s 318` |
| 319 | Hurt | encoded | pc-body-a-hurt.l4 | `causes hurt` (defining, with its Explanation) |
| 320 | Grievous hurt | encoded | pc-body-a-hurt.l4 | `grievous hurt within section 320`, helper `lasts the space of 20 days` (defining) |
| 321 | Voluntarily causing hurt | encoded | pc-body-a-hurt.l4 | `voluntarily causes hurt` (defining) |
| 322 | Voluntarily causing grievous hurt | encoded | pc-body-a-hurt.l4 | `voluntarily causes grievous hurt` (defining, with its Explanation) |
| 323 | Punishment for voluntarily causing hurt | encoded | pc-body-a-hurt.l4 | `offence under s 323`, `charge under s 323` |
| 323A | Punishment for voluntarily causing hurt which causes grievous hurt | encoded | pc-body-a-hurt.l4 | `offence under s 323A`, `charge under s 323A` |
| 324 | Voluntarily causing hurt by dangerous weapons or means | encoded | pc-body-a-hurt.l4 | `offence under s 324`, `charge under s 324`, `by dangerous weapons or means` |
| 325 | Punishment for voluntarily causing grievous hurt | encoded | pc-body-a-hurt.l4 | `offence under s 325`, `charge under s 325` |
| 326 | Voluntarily causing grievous hurt by dangerous weapons or means | encoded | pc-body-a-hurt.l4 | `offence under s 326`, `charge under s 326` |
| 327 | Voluntarily causing hurt to extort property or to constrain to an illegal act | encoded | pc-body-a-hurt.l4 | `offence under s 327`, `charge under s 327`, `to extort property or to constrain to an illegal act` |
| 328 | Causing hurt by means of poison, etc., with intent to commit an offence | encoded | pc-body-a-hurt.l4 | `offence under s 328`, `charge under s 328` |
| 329 | Voluntarily causing grievous hurt to extort property, or to constrain to an illegal act | encoded | pc-body-a-hurt.l4 | `offence under s 329`, `charge under s 329` |
| 330 | Voluntarily causing hurt to extort confession or to compel restoration of property | encoded | pc-body-a-hurt.l4 | `offence under s 330`, `charge under s 330`, `to extort confession or to compel restoration of property` |
| 331 | Voluntarily causing grievous hurt to extort confession or to compel restoration of property | encoded | pc-body-a-hurt.l4 | `offence under s 331`, `charge under s 331` |
| 332 | Voluntarily causing hurt to deter public servant from his duty | encoded | pc-body-a-hurt.l4 | `offence under s 332`, `charge under s 332`, `to a public servant in the discharge of his duty, or to deter him from it` |
| 333 | Voluntarily causing grievous hurt to deter public servant from his duty | encoded | pc-body-a-hurt.l4 | `offence under s 333`, `charge under s 333` |
| 334 | Voluntarily causing hurt on provocation | encoded | pc-body-a-hurt.l4 | `offence under s 334`, `charge under s 334`, `on grave and sudden provocation, subject to the provisos of Exception 1 to section 300` |
| 334A | Punishment for voluntarily causing hurt on provocation which causes grievous hurt | encoded | pc-body-a-hurt.l4 | `offence under s 334A`, `charge under s 334A` |
| 335 | Causing grievous hurt on provocation | encoded | pc-body-a-hurt.l4 | `offence under s 335`, `charge under s 335` (its Explanation is the provocation ladder above) |
| 335A | Allowing neglect, physical or sexual abuse of domestic worker or vulnerable person | deferred | - | Time; needs ss 73(4), 74A(5) (general-part's) and CPC s 2(1) "sexual offence". |
| 335B | Act which endangers life or personal safety of others with knowledge or belief that it is likely to cause death | encoded | pc-body-a-hurt.l4 | `offence under s 335B`, `charge under s 335B` |
| 336 | Act which endangers life or the personal safety of others | encoded | pc-body-a-hurt.l4 | `offence under s 336(a)`/`(b)`, `charge under s 336(a)`/`(b)`, `does an act so rashly or negligently as to endanger human life or the personal safety of others`, `a rash act`, `a negligent act` |
| 337 | Causing hurt by an act which endangers life or the personal safety of others | encoded | pc-body-a-hurt.l4 | `offence under s 337(a)`/`(b)`, `charge under s 337(a)`/`(b)` |
| 338 | Causing grievous hurt by an act which endangers life or the personal safety of others | encoded | pc-body-a-hurt.l4 | `offence under s 338(a)`/`(b)`, `charge under s 338(a)`/`(b)` |
| 339 | Wrongful restraint | encoded | pc-body-a-force.l4 | `wrongfully restrains` (defining, with its Exception) |
| 340 | Wrongful confinement | encoded | pc-body-a-force.l4 | `wrongfully confines` (defining) |
| 341 | Punishment for wrongful restraint | encoded | pc-body-a-force.l4 | `offence under s 341`, `charge under s 341` |
| 342 | Punishment for wrongful confinement | encoded | pc-body-a-force.l4 | `offence under s 342`, `charge under s 342` |
| 343 | (Repealed) | repealed | - | [Repealed by Act 15 of 2019] |
| 344 | (Repealed) | repealed | - | [Repealed by Act 15 of 2019] |
| 345 | Wrongful confinement of person for whose liberation a writ has been issued | encoded | pc-body-a-force.l4 | `offence under s 345`, `charge under s 345` |
| 346 | Wrongful confinement in secret | encoded | pc-body-a-force.l4 | `offence under s 346`, `charge under s 346` |
| 347 | Wrongful confinement for the purpose of extorting property or constraining to an illegal act | encoded | pc-body-a-force.l4 | `offence under s 347`, `charge under s 347` |
| 348 | Wrongful confinement for the purpose of extorting confession or of compelling restoration of property | encoded | pc-body-a-force.l4 | `offence under s 348`, `charge under s 348` |
| 349 | Force | encoded | pc-body-a-force.l4 | `uses force` (defining) |
| 350 | Criminal force | encoded | pc-body-a-force.l4 | `uses criminal force` (defining) |
| 351 | Assault | encoded | pc-body-a-force.l4 | `commits an assault` (defining, Explanation in the leaf's @desc), `assaults or uses criminal force` |
| 352 | Punishment for using criminal force otherwise than on grave and sudden provocation | encoded | pc-body-a-force.l4 | `offence under s 352`, `charge under s 352`, `on grave and sudden provocation given by that person, within the Explanation to section 352` |
| 353 | Using criminal force to deter a public servant from discharge of his duty | encoded | pc-body-a-force.l4 | `offence under s 353`, `charge under s 353` |
| 354 | Assault or use of criminal force with intent to outrage modesty | encoded | pc-body-a-force.l4 | `outrages the modesty of that person`, `offence under s 354(1)`/`(2)`, `charge under s 354(1)`/`(2)`, helper `below 14 years of age` |
| 354A | Outraging modesty in certain circumstances | encoded | pc-body-a-force.l4 | `offence under s 354A(1)`/`(2)`, `charge under s 354A(1)`/`(2)` |
| 355 | Assault or criminal force with intent to dishonour otherwise than on grave and sudden provocation | encoded | pc-body-a-force.l4 | `offence under s 355`, `charge under s 355` |
| 356 | Assault or criminal force in committing or attempting to commit theft of property carried by a person | encoded | pc-body-a-force.l4 | `offence under s 356`, `charge under s 356` (theft is a leaf: join owed, F-17) |
| 357 | Assault or criminal force in attempting wrongfully to confine a person | encoded | pc-body-a-force.l4 | `offence under s 357`, `charge under s 357` |
| 358 | Assaulting or using criminal force on grave and sudden provocation | encoded | pc-body-a-force.l4 | `offence under s 358`, `charge under s 358` |

## Illustrations and whether they are asserted

Asserted (cited `-- s N illus (x)` in the tests): s 299 (a), (b); s 300 (a), (b) both limbs, (c), (d); s 300 Exception 1 (a), (b), (c) [also standing for (d)], (e), (g); Exception 4 (a), (b); Exception 5; s 307 (a) [also (b)], (c) both halves; s 308; s 312 Explanation; s 319 Explanation; s 322 and its Explanation; s 323A; s 330 (a) [also (c)], (b); s 339 and its Exception; s 340 (a) [also (b)]; s 350 (a), (b), (c), (d), (e), (h), and (a) with consent; s 351 (a) [also (b)] and its Explanation.

Not asserted, and why:
- s 300 Exception 1 illus (f) (the bystander who hands B a knife): A's liability is as abettor/instigator of B's killing; on A's own atoms it is s 300(a) with no Exception, which the (a) fixture already asserts. Abetment (s 107) is general-part's.
- s 307 illus (d) (poison in A's keeping vs on Z's table): the same shape as (c) - the circumstances leaf is FALSE, then TRUE. Not separately fixtured.
- s 350 illus (f), (g): the same atoms as (d) and (e) respectively.
- s 351 illus (c): the Code says the gesture "may amount" to an assault - it does not say it does, so there is no expected value to assert.
- s 316 illus: s 316 is deferred.

## Cross-module joins owed

| leaf (record) | section | owner | edge allowed by PLAN §1? |
| --- | --- | --- | --- |
| `in committing or attempting to commit theft of any property which that person is then wearing or carrying` (Criminal Force Facts) | s 356 -> s 378 | property | **No.** body-a -> property is not listed, and property -> body-a is, so this edge would make a cycle. The leaf stays a leaf; any join belongs in the charge sheet above both. |
| `abets the commission of such suicide or attempted suicide` (Suicide Abetment Facts) | ss 305, 306 -> s 107 | general-part | yes (every group -> general-part) |
| `without that person's consent` (Criminal Force Facts); `suffers death or takes the risk of death with his own consent` (Homicide Facts) | ss 350, 300 Exc 5 -> s 90 | exceptions | yes |
| `the sufferer is a public servant` (Hurt Facts); `that person is a public servant` (Criminal Force Facts) | ss 332, 333, 353 -> s 21 | pc-general | drill-down, as a DEFINITION_LADDERS entry |
| `causes hurt to any person`, `causes grievous hurt to any person` (Rash Act Facts); `hurt is caused to any person by such act` (Homicide Facts); `hurt is caused to any person in the course of the attempted suicide`; the s 354A hurt/restraint leaves | ss 337, 338, 307, 308, 305, 354A -> ss 319, 320, 339 | body-a (this group) | within the group; not joined because they sit on different facts records. A later pass can nest a `Hurt Facts` where the ladder should drill down. |
| `not amounting to culpable homicide` (Rash Act Facts) | s 304A -> s 299 | body-a | within the group; same remark |
| `not a treatment authorised by the Termination of Pregnancy Act 1974` | s 312 | none - another Act | not encoded anywhere |

Edges other groups owe INTO body-a (PLAN §1): property -> body-a for ss 382, 394, 397, 459-460 should call `voluntarily causes hurt` / `voluntarily causes grievous hurt` over `Hurt Facts`; body-b -> body-a for s 367 should call `grievous hurt within section 320`.

## DEFINITION_LADDERS entries (Chapter 2 drill-downs read as flat leaves)

```ts
{ fn: 'voluntarily within section 26A', leaf: 'voluntarily obstructs that person', section: '26A' },
{ fn: 'in good faith within section 26B', leaf: 'the obstruction is of a private way over land or water which he in good faith believes himself to have a lawful right to obstruct', section: '26B' },
{ fn: 'rashly in respect of an effect within section 26E(2)', leaf: 'does the act rashly', section: '26E' },
{ fn: 'negligently within section 26F', leaf: 'does the act negligently', section: '26F' },
{ fn: 'public servant within section 21', leaf: 'the sufferer is a public servant', section: '21' },
{ fn: 'public servant within section 21', leaf: 'that person is a public servant', section: '21' },
{ fn: 'illegal within section 43', leaf: 'intending by the use of such force illegally to cause injury, fear or annoyance to that person', section: '43' },
{ fn: 'valuable security within section 30', leaf: 'for the purpose of extorting from the sufferer, or from any person interested in the sufferer, any property or valuable security', section: '30' },
```

## OFFENCES entries for the catalogue

New `family` slugs proposed: `homicide`, `rash-act`, `restraint`, `criminal-force`, `suicide-abetment`, `corpse`, `miscarriage`, `child-exposure`, `concealment-of-birth`. `hurt` exists.
The existing s 323A entry must be re-pointed: its `definitionFns` stays `['voluntarily causes hurt']`, but the `Hurt Facts` fields are renamed (F-1).

```ts
  { section: '302(1)', title: "murder", defines: 's 300(a)', family: 'homicide', offenceFn: 'offence under s 302(1)', chargeFn: 'charge under s 302(1)', definitionFns: ['commits culpable homicide', 'murder within the meaning of section 300(a)', 'an Exception to section 300 applies'], factsType: 'Homicide Facts', factsParam: 'f' },
  { section: '302(2)', title: "murder", defines: 's 300(b)-(d)', family: 'homicide', offenceFn: 'offence under s 302(2)', chargeFn: 'charge under s 302(2)', definitionFns: ['commits culpable homicide', 'murder within the meaning of section 300(b)', 'murder within the meaning of section 300(c)', 'murder within the meaning of section 300(d)', 'an Exception to section 300 applies'], factsType: 'Homicide Facts', factsParam: 'f' },
  { section: '304(a)', title: "culpable homicide not amounting to murder", defines: 'ss 299, 300', family: 'homicide', offenceFn: 'offence under s 304(a)', chargeFn: 'charge under s 304(a)', definitionFns: ['commits culpable homicide not amounting to murder', 'commits culpable homicide', 'commits murder'], factsType: 'Homicide Facts', factsParam: 'f' },
  { section: '304(b)', title: "culpable homicide not amounting to murder", defines: 'ss 299, 300', family: 'homicide', offenceFn: 'offence under s 304(b)', chargeFn: 'charge under s 304(b)', definitionFns: ['commits culpable homicide not amounting to murder', 'commits culpable homicide', 'commits murder'], factsType: 'Homicide Facts', factsParam: 'f' },
  { section: '304A(a)', title: "causing death by rash act", defines: 's 304A', family: 'rash-act', offenceFn: 'offence under s 304A(a)', chargeFn: 'charge under s 304A(a)', definitionFns: ['a rash act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '304A(b)', title: "causing death by negligent act", defines: 's 304A', family: 'rash-act', offenceFn: 'offence under s 304A(b)', chargeFn: 'charge under s 304A(b)', definitionFns: ['a negligent act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '305(1)(a)', title: "abetment of suicide of minor or person who lacks mental capacity", defines: 's 305', family: 'suicide-abetment', offenceFn: 'offence under s 305(1)(a)', chargeFn: 'charge under s 305(1)(a)', definitionFns: [], factsType: 'Suicide Abetment Facts', factsParam: 'f' },
  { section: '305(1)(b)', title: "abetment of attempted suicide of minor or person who lacks mental capacity", defines: 's 305', family: 'suicide-abetment', offenceFn: 'offence under s 305(1)(b)', chargeFn: 'charge under s 305(1)(b)', definitionFns: [], factsType: 'Suicide Abetment Facts', factsParam: 'f' },
  { section: '305(1)(c)', title: "abetment of attempted suicide of minor or person who lacks mental capacity where hurt is caused", defines: 's 305', family: 'suicide-abetment', offenceFn: 'offence under s 305(1)(c)', chargeFn: 'charge under s 305(1)(c)', definitionFns: [], factsType: 'Suicide Abetment Facts', factsParam: 'f' },
  { section: '306', title: "abetment of suicide or attempted suicide", defines: 's 306', family: 'suicide-abetment', offenceFn: 'offence under s 306', chargeFn: 'charge under s 306', definitionFns: [], factsType: 'Suicide Abetment Facts', factsParam: 'f' },
  { section: '307(1)', title: "attempt to murder", defines: 's 307', family: 'homicide', offenceFn: 'offence under s 307(1)', chargeFn: 'charge under s 307(1)', definitionFns: [], factsType: 'Homicide Facts', factsParam: 'f' },
  { section: '307(2)', title: "attempt to murder by a person under sentence of imprisonment for life", defines: 's 307', family: 'homicide', offenceFn: 'offence under s 307(2)', chargeFn: 'charge under s 307(2)', definitionFns: ['offence under s 307(1)'], factsType: 'Homicide Facts', factsParam: 'f' },
  { section: '308', title: "attempt to commit culpable homicide", defines: 's 308', family: 'homicide', offenceFn: 'offence under s 308', chargeFn: 'charge under s 308', definitionFns: [], factsType: 'Homicide Facts', factsParam: 'f' },
  { section: '308B', title: "concealment, desecration or disposal of corpse", defines: 's 308B(1)', family: 'corpse', offenceFn: 'offence under s 308B', chargeFn: 'charge under s 308B', definitionFns: [], factsType: 'Corpse Facts', factsParam: 'f' },
  { section: '312', title: "causing miscarriage", defines: 's 312', family: 'miscarriage', offenceFn: 'offence under s 312', chargeFn: 'charge under s 312', definitionFns: [], factsType: 'Miscarriage Facts', factsParam: 'f' },
  { section: '313', title: "causing miscarriage without woman's consent", defines: 'ss 312, 313', family: 'miscarriage', offenceFn: 'offence under s 313', chargeFn: 'charge under s 313', definitionFns: ['offence under s 312'], factsType: 'Miscarriage Facts', factsParam: 'f' },
  { section: '317', title: "exposure and abandonment of a child below 12 years of age by parent or person having care of it", defines: 's 317', family: 'child-exposure', offenceFn: 'offence under s 317', chargeFn: 'charge under s 317', definitionFns: [], factsType: 'Child Exposure Facts', factsParam: 'f' },
  { section: '318', title: "concealment of birth by secret disposal of dead body", defines: 's 318', family: 'concealment-of-birth', offenceFn: 'offence under s 318', chargeFn: 'charge under s 318', definitionFns: [], factsType: 'Concealment of Birth Facts', factsParam: 'f' },
  { section: '323', title: "voluntarily causing hurt", defines: 'ss 319, 321', family: 'hurt', offenceFn: 'offence under s 323', chargeFn: 'charge under s 323', definitionFns: ['voluntarily causes hurt', 'causes hurt', 'offence under s 323A', 'offence under s 334'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '323A', title: "voluntarily causing hurt which causes grievous hurt", defines: 'ss 319-321, 323A', family: 'hurt', offenceFn: 'offence under s 323A', chargeFn: 'charge under s 323A', definitionFns: ['voluntarily causes hurt', 'causes hurt', 'grievous hurt within section 320'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '324', title: "voluntarily causing hurt by dangerous weapons or means", defines: 'ss 321, 324', family: 'hurt', offenceFn: 'offence under s 324', chargeFn: 'charge under s 324', definitionFns: ['voluntarily causes hurt', 'by dangerous weapons or means', 'offence under s 334'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '325', title: "voluntarily causing grievous hurt", defines: 'ss 320, 322', family: 'hurt', offenceFn: 'offence under s 325', chargeFn: 'charge under s 325', definitionFns: ['voluntarily causes grievous hurt', 'voluntarily causes hurt', 'grievous hurt within section 320', 'offence under s 323A', 'offence under s 334A', 'offence under s 335'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '326', title: "voluntarily causing grievous hurt by dangerous weapons or means", defines: 'ss 322, 326', family: 'hurt', offenceFn: 'offence under s 326', chargeFn: 'charge under s 326', definitionFns: ['voluntarily causes grievous hurt', 'by dangerous weapons or means', 'offence under s 335'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '327', title: "voluntarily causing hurt to extort property or to constrain to an illegal act", defines: 'ss 321, 327', family: 'hurt', offenceFn: 'offence under s 327', chargeFn: 'charge under s 327', definitionFns: ['voluntarily causes hurt', 'to extort property or to constrain to an illegal act'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '328', title: "causing hurt by means of poison, etc., with intent to commit an offence", defines: 's 328', family: 'hurt', offenceFn: 'offence under s 328', chargeFn: 'charge under s 328', definitionFns: [], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '329', title: "voluntarily causing grievous hurt to extort property or to constrain to an illegal act", defines: 'ss 322, 329', family: 'hurt', offenceFn: 'offence under s 329', chargeFn: 'charge under s 329', definitionFns: ['voluntarily causes grievous hurt', 'to extort property or to constrain to an illegal act'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '330', title: "voluntarily causing hurt to extort confession or to compel restoration of property", defines: 'ss 321, 330', family: 'hurt', offenceFn: 'offence under s 330', chargeFn: 'charge under s 330', definitionFns: ['voluntarily causes hurt', 'to extort confession or to compel restoration of property'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '331', title: "voluntarily causing grievous hurt to extort confession or to compel restoration of property", defines: 'ss 322, 331', family: 'hurt', offenceFn: 'offence under s 331', chargeFn: 'charge under s 331', definitionFns: ['voluntarily causes grievous hurt', 'to extort confession or to compel restoration of property'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '332', title: "voluntarily causing hurt to deter public servant from his duty", defines: 'ss 321, 332', family: 'hurt', offenceFn: 'offence under s 332', chargeFn: 'charge under s 332', definitionFns: ['voluntarily causes hurt', 'to a public servant in the discharge of his duty, or to deter him from it'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '333', title: "voluntarily causing grievous hurt to deter public servant from his duty", defines: 'ss 322, 333', family: 'hurt', offenceFn: 'offence under s 333', chargeFn: 'charge under s 333', definitionFns: ['voluntarily causes grievous hurt', 'to a public servant in the discharge of his duty, or to deter him from it'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '334', title: "voluntarily causing hurt on provocation", defines: 'ss 321, 334', family: 'hurt', offenceFn: 'offence under s 334', chargeFn: 'charge under s 334', definitionFns: ['voluntarily causes hurt', 'on grave and sudden provocation, subject to the provisos of Exception 1 to section 300'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '334A', title: "voluntarily causing hurt on provocation which causes grievous hurt", defines: 'ss 321, 334A', family: 'hurt', offenceFn: 'offence under s 334A', chargeFn: 'charge under s 334A', definitionFns: ['voluntarily causes hurt', 'on grave and sudden provocation, subject to the provisos of Exception 1 to section 300', 'grievous hurt within section 320'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '335', title: "causing grievous hurt on provocation", defines: 'ss 322, 335', family: 'hurt', offenceFn: 'offence under s 335', chargeFn: 'charge under s 335', definitionFns: ['voluntarily causes grievous hurt', 'on grave and sudden provocation, subject to the provisos of Exception 1 to section 300'], factsType: 'Hurt Facts', factsParam: 'f' },
  { section: '335B', title: "act which endangers life or personal safety of others with knowledge or belief that it is likely to cause death", defines: 's 335B', family: 'rash-act', offenceFn: 'offence under s 335B', chargeFn: 'charge under s 335B', definitionFns: [], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '336(a)', title: "rash act which endangers life or the personal safety of others", defines: 's 336', family: 'rash-act', offenceFn: 'offence under s 336(a)', chargeFn: 'charge under s 336(a)', definitionFns: ['does an act so rashly or negligently as to endanger human life or the personal safety of others', 'a rash act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '336(b)', title: "negligent act which endangers life or the personal safety of others", defines: 's 336', family: 'rash-act', offenceFn: 'offence under s 336(b)', chargeFn: 'charge under s 336(b)', definitionFns: ['does an act so rashly or negligently as to endanger human life or the personal safety of others', 'a negligent act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '337(a)', title: "causing hurt by a rash act which endangers life or the personal safety of others", defines: 's 337', family: 'rash-act', offenceFn: 'offence under s 337(a)', chargeFn: 'charge under s 337(a)', definitionFns: ['does an act so rashly or negligently as to endanger human life or the personal safety of others', 'a rash act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '337(b)', title: "causing hurt by a negligent act which endangers life or the personal safety of others", defines: 's 337', family: 'rash-act', offenceFn: 'offence under s 337(b)', chargeFn: 'charge under s 337(b)', definitionFns: ['does an act so rashly or negligently as to endanger human life or the personal safety of others', 'a negligent act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '338(a)', title: "causing grievous hurt by a rash act which endangers life or the personal safety of others", defines: 's 338', family: 'rash-act', offenceFn: 'offence under s 338(a)', chargeFn: 'charge under s 338(a)', definitionFns: ['does an act so rashly or negligently as to endanger human life or the personal safety of others', 'a rash act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '338(b)', title: "causing grievous hurt by a negligent act which endangers life or the personal safety of others", defines: 's 338', family: 'rash-act', offenceFn: 'offence under s 338(b)', chargeFn: 'charge under s 338(b)', definitionFns: ['does an act so rashly or negligently as to endanger human life or the personal safety of others', 'a negligent act'], factsType: 'Rash Act Facts', factsParam: 'f' },
  { section: '341', title: "wrongful restraint", defines: 's 339', family: 'restraint', offenceFn: 'offence under s 341', chargeFn: 'charge under s 341', definitionFns: ['wrongfully restrains'], factsType: 'Restraint Facts', factsParam: 'f' },
  { section: '342', title: "wrongful confinement", defines: 'ss 339, 340', family: 'restraint', offenceFn: 'offence under s 342', chargeFn: 'charge under s 342', definitionFns: ['wrongfully confines', 'wrongfully restrains'], factsType: 'Restraint Facts', factsParam: 'f' },
  { section: '345', title: "wrongful confinement of person for whose liberation a writ has been issued", defines: 'ss 340, 345', family: 'restraint', offenceFn: 'offence under s 345', chargeFn: 'charge under s 345', definitionFns: ['wrongfully confines'], factsType: 'Restraint Facts', factsParam: 'f' },
  { section: '346', title: "wrongful confinement in secret", defines: 'ss 340, 346', family: 'restraint', offenceFn: 'offence under s 346', chargeFn: 'charge under s 346', definitionFns: ['wrongfully confines'], factsType: 'Restraint Facts', factsParam: 'f' },
  { section: '347', title: "wrongful confinement for the purpose of extorting property or constraining to an illegal act", defines: 'ss 340, 347', family: 'restraint', offenceFn: 'offence under s 347', chargeFn: 'charge under s 347', definitionFns: ['wrongfully confines'], factsType: 'Restraint Facts', factsParam: 'f' },
  { section: '348', title: "wrongful confinement for the purpose of extorting confession or of compelling restoration of property", defines: 'ss 340, 348', family: 'restraint', offenceFn: 'offence under s 348', chargeFn: 'charge under s 348', definitionFns: ['wrongfully confines'], factsType: 'Restraint Facts', factsParam: 'f' },
  { section: '352', title: "using criminal force otherwise than on grave and sudden provocation", defines: 'ss 349-351', family: 'criminal-force', offenceFn: 'offence under s 352', chargeFn: 'charge under s 352', definitionFns: ['assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault', 'on grave and sudden provocation given by that person, within the Explanation to section 352'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '353', title: "using criminal force to deter a public servant from discharge of his duty", defines: 'ss 349-351, 353', family: 'criminal-force', offenceFn: 'offence under s 353', chargeFn: 'charge under s 353', definitionFns: ['assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '354(1)', title: "assault or use of criminal force to a person with intent to outrage modesty", defines: 'ss 349-351, 354', family: 'criminal-force', offenceFn: 'offence under s 354(1)', chargeFn: 'charge under s 354(1)', definitionFns: ['outrages the modesty of that person', 'assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '354(2)', title: "assault or use of criminal force to a person below 14 years of age with intent to outrage modesty", defines: 'ss 349-351, 354', family: 'criminal-force', offenceFn: 'offence under s 354(2)', chargeFn: 'charge under s 354(2)', definitionFns: ['outrages the modesty of that person', 'assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '354A(1)', title: "outraging modesty in certain circumstances", defines: 's 354A', family: 'criminal-force', offenceFn: 'offence under s 354A(1)', chargeFn: 'charge under s 354A(1)', definitionFns: [], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '354A(2)', title: "outraging modesty in certain circumstances", defines: 's 354A', family: 'criminal-force', offenceFn: 'offence under s 354A(2)', chargeFn: 'charge under s 354A(2)', definitionFns: ['offence under s 354A(1)'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '355', title: "assault or criminal force with intent to dishonour otherwise than on grave and sudden provocation", defines: 'ss 349-351, 355', family: 'criminal-force', offenceFn: 'offence under s 355', chargeFn: 'charge under s 355', definitionFns: ['assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault', 'on grave and sudden provocation given by that person, within the Explanation to section 352'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '356', title: "assault or criminal force in committing or attempting to commit theft of property carried by a person", defines: 'ss 349-351, 356', family: 'criminal-force', offenceFn: 'offence under s 356', chargeFn: 'charge under s 356', definitionFns: ['assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '357', title: "assault or criminal force in attempting wrongfully to confine a person", defines: 'ss 349-351, 357', family: 'criminal-force', offenceFn: 'offence under s 357', chargeFn: 'charge under s 357', definitionFns: ['assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault'], factsType: 'Criminal Force Facts', factsParam: 'f' },
  { section: '358', title: "assaulting or using criminal force on grave and sudden provocation", defines: 'ss 349-351, 358', family: 'criminal-force', offenceFn: 'offence under s 358', chargeFn: 'charge under s 358', definitionFns: ['assaults or uses criminal force', 'uses criminal force', 'uses force', 'commits an assault', 'on grave and sudden provocation given by that person, within the Explanation to section 352'], factsType: 'Criminal Force Facts', factsParam: 'f' },
```

(56 entries, one per punishing provision encoded. s 308B's offenceFn/chargeFn are named `s 308B`; its charge recites section 308B(2), the punishing subsection.)

