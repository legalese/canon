# Forks — Chapter 17, Offences against property (ss 378-462)

Every ambiguity met while encoding, with the readings, the one taken, and why.
Where a fork is a design choice about the encoding rather than about the law, it says so.
Places looked for ambiguity: every defining section's connectives ("or", "and", "such"), every punishing clause's verbs, every Explanation and in-section defence, and every place the reference row (`reference/drafts-row/`) and this text differ.

## P-1 (design) — aggravations as flat leaves of one facts record, not nested records

**Readings.** (a) The reference row nests: `Theft in Dwelling Facts` holds a `Theft Facts` and adds the place; `Aggravated CBT Facts` holds a `CBT Facts`. (b) One record per family, with the aggravating leaves of ss 379A-382 on `Theft Facts` and of ss 407-409 on `CBT Facts`.
**Taken:** (b).
**Why:** PLAN §3.1 says one facts record per family is the single input of every export for that family; with (b) the charge generator asks one set of questions and every theft card (379, 379A, 380, 381, 382) reads the same record, and schema completion fills the aggravations FALSE for a plain theft.
**Consequence for the catalogue:** the reference row's `Theft in Dwelling Facts` and `Aggravated CBT Facts` do not exist here; s 380's `factsType` is `Theft Facts`, and ss 407-409's is `CBT Facts`. Robbery still nests `Theft Facts` and `Extortion Facts`, as the reference row does, because s 390 is built from two whole offences.

## P-2 — s 382 "restraint" and s 440 "wrongful restraint"

s 382 says "preparation for causing death or hurt or restraint, or fear of death or of hurt or of restraint"; s 440 and s 452 say "wrongful restraint".
**Readings.** (a) s 382 means wrongful restraint (s 339), and the word is elliptical. (b) s 382 reaches any restraint.
**Taken:** neither is decided; the leaf quotes each section's own word, and its `@desc` names hurt (s 319) as body-a's.
**Why:** the investigator answers the section's words; which reading a court takes is not something the encoding can answer.

## P-3 — s 390(2): does "voluntarily" govern "attempts to cause"?

"voluntarily causes or attempts to cause". **Taken:** one `voluntarily` leaf over both, as the reference row does. The alternative (voluntarily governs only "causes") would let an attempt be made out without it; an attempt is intentional by nature, so the difference is small.

## P-4 (design) — s 420 split into (1) and (2); the reference row's single s 420 is not kept

s 420(1) and (2) have different elements (s 420(2) needs cheating by remote communication, s 416B) and different punishments.
**Taken:** `offence under s 420(1)` / `offence under s 420(2)` and `charge under s 420(1)` / `charge under s 420(2)`, per PLAN §2.
The reference row's `by remote communication` leaf is replaced by s 416B's words, `the deception is conducted mainly by way of remote communication with the person deceived`, plus the Minister's exclusion (`a system or method the Minister has declared is not remote communication`).
**Deliberate inconsistency:** `charge under s 420(1)` frames the section as "420", not "420(1)", so that the reported Lewis Christine charge ("an offence punishable under section 420") still reproduces byte for byte (asserted). Every other subsection charge names its subsection ("411(1)", "414(2)", "416A(1)", "420(2)", "424A(1)", "427(1)", "453(1)"). Which form a charge sheet uses today is a question for a practitioner.
**Consequence for the catalogue:** the entry `offenceFn: 'offence under s 420'` must become two entries.

## P-5 — s 397 is an enhancement, charged here as its own offence

s 397 prescribes caning "in addition to any other punishment to which he may be liable under any other section". In practice the charge is under s 392 (or 393) read with s 397.
**Readings.** (a) A charge under s 397 alone. (b) `frame the charge read with` "392" (LIST "397").
**Taken:** (a), section "397", because the brief asks for `charge under s N` per punishing section, and the robbery or attempt it rides on is already an element of the ladder. s 458A, which is worded as an enhancement of a named offence ("liable to caning in addition to the punishment prescribed for that offence"), IS framed read-with ("451 read with 458A"), because the underlying section is one of four the charge must name. The two choices should probably be made the same way at integration; the readings are recorded so a reviewer can pick.

## P-6 — defences inside ss 411(3) and 412(2) sit in the offence ladder

"It is a defence for a person charged ... to prove that he has a reasonable excuse ... and that he exercised reasonable care".
**Readings.** (a) Part of the section, so in the ladder as `NOT defence under s 411(3)` (PLAN §5: exceptions inside an offence's own section go in its ladder). (b) Outside the ladder, like a general exception: CPC s 123(5) asserts the conditions that constitute the offence, and a defence the accused must prove is not one of them.
**Taken:** (a), per PLAN §5. Because schema completion fills unknown leaves FALSE, an unanswered defence does not block a charge, which is the burden the section states. The refusal names the defence when it is proved.
s 412(2) is word-for-word s 411(3), so s 412 reuses `defence under s 411(3)` rather than declaring a twin.

## P-7 — s 410: does "ceases to be stolen property" reach s 410(2)'s converted property?

The proviso ("But if such property subsequently comes into the possession of a person legally entitled ... it then ceases to be stolen property") sits in (1); (2) extends "stolen property" to property into which it was converted.
**Taken:** the proviso applies to both, because (2) extends the defined expression and the proviso qualifies the expression. The other reading (converted property never ceases) has no text for it.

## P-8 — s 412's two limbs

First limb: "receives or retains any stolen property" known or believed transferred by gang-robbery. Second limb: "receives from a person ... [a gang-robber] ... property which he knows or has reason to believe to have been stolen" — only "receives", and "stolen" not "stolen property".
**Taken:** first limb reads `stolen property within section 410`; second limb reads its own leaf `which he knows or has reason to believe to have been stolen`, and only `receives`.

## P-9 (design) — "an offence punishable with ..." is a flat leaf

ss 388, 389 (accusation of an offence punishable with death, life, or 10 years) and ss 449-451 (house-breaking in order to commit an offence punishable with death / life / imprisonment) turn on how ANOTHER offence is punished.
**Readings.** (a) Compute it from that offence's `Punishment` record with pc-general's readers. (b) A flat BOOLEAN leaf whose `@desc` names those readers.
**Taken:** (b). A ladder can only read leaves of its own facts record (PLAN §3), and the intended offence is not identified in it. At integration a caller that knows the intended offence can set the leaf from `punishable with death or imprisonment for life`, `punishable with imprisonment`, or `punishable with imprisonment for` 120 `months or upwards within section 41`.
**Note:** the three limbs of ss 449-451 nest (an offence punishable with death is also punishable with imprisonment), so one set of facts can make out ss 449 and 451 together; the charge generator will show both cards.

## P-10 — s 424B(4): what is left for s 424B

s 424B(1) repeats s 424A(1) word for word; (4) says it "does not apply to any act ... which would constitute an offence under section 424A".
**Taken:** `offence under s 424B` = the shared elements AND NOT `offence under s 424A`, literally. In effect s 424B covers conduct directly connected with a contract for goods or services (the case s 424A(4) excludes). s 424B carries "[Act 15 of 2019 wef 28/07/2023]"; there is no time axis in this encoding, so a pre-commencement act is not distinguished.

## P-11 — s 416A(2) and (3): exceptions restated as requirements

"(2) It is not an offence under (1)(a) if the person obtained or retained ... for a purpose other than [use in or supply for an offence]". "(3) It is not an offence under (1)(b) if (a) the purpose was other than such use and (b) the person did not know or have reason to believe it likely to be so used."
**Taken:** (1)(a) requires the offence purpose; (1)(b) requires the purpose or the knowledge. That is the contrapositive, not a reading choice, but it may move the burden: if the exceptions are for the accused to bring himself within (the section does not say who must prove them), then as encoded an unanswered purpose leaf wrongly means no charge. **This is a fork a reviewer should rule on:** encoding (2) and (3) as `NOT <exception>` instead would let a charge be framed with the purpose unknown.

## P-12 — s 403's defining predicate omits "movable property"

s 404 repeats s 403's verb ("dishonestly misappropriates or converts to his own use") but of "property", not "movable property".
**Taken:** `dishonestly misappropriates or converts to his own use` is the shared verb; `offence under s 403` adds `movable property`; `offence under s 404` adds s 404's knowledge and possession limbs.

## P-13 — s 453: the forfeiture, and the burden

(a) "any instrument or article ... found in the possession of that person shall be forfeited" — recorded as `forfeiture of property` `shall be punished with`. It is forfeiture of the article, which may or may not be s 53's "forfeiture of property"; the words ride verbatim in the charge's punishment field either way.
(b) s 453(2) puts on the accused the burden of showing lawful authority or purpose, and (3) presumes lawful authority for listed persons. Both are negated leaves in the ladder, so an unanswered one does not block the charge — which matches (2).

## P-14 — s 460 does not require the accused to have entered

"every person jointly concerned in committing such house-breaking". **Taken:** the ladder reads `jointly concerned in committing such house-breaking` and the harm leaf, and does not call `commits house-breaking` on the accused; a lookout never inside is within the words.

## P-15 — s 438's attempt limb

"commits or attempts to commit by fire ... such mischief as is described in section 437". **Taken:** the attempt limb requires the vessel and intent leaves of s 437 and `attempts to commit such mischief` (s 511), but not that mischief was committed.

## P-16 — s 391: who "commits gang-robbery"

"every person so committing, attempting, or aiding". **Taken:** the accused commits gang-robbery if the count is met AND he commits robbery, attempts it, or is present and aiding. The counts are leaves decided by the `5 or more persons` helper, per PLAN §3.5.

## P-17 — punishment verbs that the enum does not quite fit

- s 396 and ss 438, 449: a punishment conditional on another ("if he is not sentenced to death, shall also be punished with caning"; "shall, if he is not sentenced to imprisonment for life, also be liable to fine"). Recorded as the unconditional verb (`shall be punished with` caning; `shall also be liable to` fine); the condition is in `words`.
- ss 388, 389, 452: "fine or to caning" with no "or to both" — `or with both` is FALSE.
- s 420A: "liable to imprisonment ... or to fine, or to both" — recorded as `or with` / `or with` / both, like "or with fine, or with both".
- s 458A: "liable to caning in addition" — `shall also be liable to`, no stroke bounds.
- ss 411(2), 414(2): the driving-licence disqualification is not a s 53 punishment; it rides in `words` only. s 379A(2)'s disqualification likewise is noted in a comment, not in the record.

## P-18 — this text differs from the reference row

Measured, not assumed: s 382 is now "10 years, and shall also be liable to caning" and s 384 "not less than 2 years and not more than 7 years and shall also be liable to caning" (both Act 21 of 2025, wef 17/08/2026); the reference row's s 384 said "and with caning", and its s 393 said "shall also be punished with caning with not less than 6 strokes" where this text says "shall also be liable to caning". The punishment records follow this text, and two tests pin the amended s 382 and s 384 caning verbs.

## P-19 — s 405 illustration (b) says "breach of trust"

"A dishonestly sells the goods. A has committed breach of trust." Every other illustration says "criminal breach of trust". **Taken:** read as criminal breach of trust (the illustration is under s 405, and dishonesty is stated); the test asserts `commits criminal breach of trust`.

## P-20 — s 418 split into two leaves

"with the knowledge that he is likely thereby to cause wrongful loss to a person whose interest ... he was bound ... to protect" is two facts (the knowledge; the duty), so two leaves. The knowledge leaf is a fault element (s 26D).

## P-21 (design) — the robbery recitals follow the reference row

The reference row pins "did rob one X of Y" to a reported charge (Chen Weixiong Jerriek v PP [2003] SGHC 103), with no words for the night limb; that text is asserted byte for byte here. The s 394 recital follows the reference row's shape ("were jointly concerned in committing robbery of ... and whilst committing the said robbery, voluntarily caused hurt to ..."), with "attempting to commit" substituted when the robbery was only attempted. Neither of these two s 394 wordings is pinned to a reported charge.
