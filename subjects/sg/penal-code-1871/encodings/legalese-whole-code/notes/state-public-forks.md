# state-public — fork register

Penal Code 1871, Chapters 6, 6A, 6B, 7, 8, 9 and 10 (ss 121–190).
Every place the text admits more than one reading, or the encoding had to choose a shape the text does not dictate: the readings, the one taken, why, and the words that license each.
Where I looked and found nothing is at the end.

## Tooling

### SP-0 — a rule named like a field of its own input silently calls itself

Measured, not a reading of the law.
s 121's defining predicate was first named `` `wages war against the Government` ``, which is also the name of the first leaf of `` `Waging War Facts` ``.
Inside the rule, `` f's `wages war against the Government` `` resolved to the rule itself: `l4 check` was clean, and `l4 run` reported `assertion could not be evaluated: Stack overflow: Recursion depth of 1000000 exceeded` on each assertion that reached it — no diagnostic at the definition.
Renamed to `` `wages, attempts or abets war against the Government` ``; `notes/state-public-gen/build.py` now refuses to build when any exported rule shares a name with any facts-record field.
PLAN section 2 warns that fields and constructors share a namespace and "the error names neither"; this is the silent form of the same trap, and belongs in `writing-l4-rules/references/gotchas.md`.

## Shape of the charge

### SP-1 — paragraphs (a) "in the case of an individual" and (b) "in any other case"

ss 173–177, 179, 183–188 punish in two paragraphs that differ only in punishment.

- **Reading A (taken):** one offence, one charge; the leaf `` `the accused is an individual` `` chooses the punishment words and the paragraph the charge cites ("punishable under section 186(1)(a)"). The paragraph is the punishing provision, and Singapore charges cite it.
- **Reading B:** two offences per subsection (`` `offence under s 186(1)(a)` `` / `(b)`), because they are distinct punishing provisions (CPC s 123(4)).
- **Reading C:** cite only the subsection ("186(1)").

B doubles the catalogue for no difference in elements; C drops the provision that fixes the sentence.
**Consequence to flag for the charge generator:** schema completion fills an unanswered leaf with FALSE, so an investigator who never answers `the accused is an individual` gets a charge under paragraph (b) — fine only. The leaf does not affect `made out`; the app should ask it up front (or default the UI to "individual").
s 173(1) numbers its punishment paragraphs (d) and (e), not (a) and (b), and the charge cites them as printed.

### SP-2 — sections that define and punish in one clause

ss 121A–121D, 122–130, 130C, 131–133, 135–138, 140, 168 and 169 say "Whoever [does X] shall be punished with …" and give the offence no name or verb of its own.
- **Reading A (taken):** the `` `offence under s N` `` ladder is the defining ladder; `definitionFns` is empty.
- **Reading B:** a separate defining predicate per section (the brief's item 2) with `offence under s N` a one-box ladder calling it.

B adds a second, identical ladder the reader must open to see anything. Where the section DOES give a verb (s 172 "absconds", s 186 "voluntarily obstructs", s 146 "rioting", s 130D "genocide"), the predicate is separate, as in the reference row's s 415 / s 417.

### SP-3 — subsections (2) that punish "an offence under subsection (1)" more severely

ss 173(2), 174(2), 176(2), 177(2), 187(2): "If [condition], any person who is guilty of an offence under subsection (1) shall — …".
- **Reading A (taken):** `` `offence under s 174(2)` `` = `` `offence under s 174(1)` `` AND the condition; the charge cites "174(2)(a)".
- **Reading B:** the charge is under s 174(1), "punishable under section 174(2)(a)".
The condition changes what the prosecution must prove (a court, an offence), so it is an element of the aggravated charge, and A puts it on the ladder. The difference is one clause of wording in the charge; HG1 should say which form the AGC uses.

### SP-172 — s 172's two tiers

s 172 is one sentence with a second punishment "if the summons, notice or order is to attend … before a court of justice". No subsection numbering, so one offence; the leaf chooses the punishment (as the reference row's s 506). The charge cites "172".

### SP-4 — the recital wording is the encoder's

No reported charge was available for any section in these chapters (the reference row pins its charges to judgments; this group has none in its inputs).
The recitals follow the statutory words and CPC s 125 (the manner, "to wit, …", where the leaf `to wit` is filled), in the reference row's form.
Every one needs checking against AGC practice at HG1.

## Chapter 6

### SP-121C — "the punishment provided for those offences"

s 121C gives no punishment of its own. ss 121A and 121B state identical punishments, so the record copies them and the `words` say so. Had they differed, the charge would need to know which offence was abetted.

### SP-125 — "imprisonment … to which fine may be added, or with fine"

`fine` is recorded `or with` (fine alone is a choice); that fine may also be ADDED to a term is not representable in `How a punishment is prescribed` and lives in `words`.

### SP-130 — does "knowingly" govern every limb?

"Whoever knowingly aids or assists … or rescues or attempts to rescue … or harbours or conceals … or offers … resistance …".
- **Reading A (taken):** "knowingly" governs all four limbs — one leaf ANDed with the disjunction.
- **Reading B:** only the first; rescuing, harbouring and resisting are strict as to knowledge.
A is the natural reading of one adverb before a list of verbs sharing a subject, and B would make harbouring a prisoner you do not know is one an offence carrying life imprisonment.

### SP-130A / 140A — "harbour includes"

"includes" enlarges; it does not confine. The ladder keeps the ordinary meaning as a first limb (`harbours the person in the ordinary sense of the word`) beside the listed ones. The definitions are "In this Chapter" only — see SP-157.

### SP-130B — "by the law of nations"

Whether an act is piracy by the law of nations is a question of international law (UNCLOS art 101 in modern form), not in this job's inputs. It is one leaf the investigator answers; the encoding cannot decide it.
The death penalty limb ("if while committing or attempting to commit piracy he murders or attempts to murder … or does any act likely to endanger the life of another person") chooses the punishment, recorded as a second `Punishment` (death, `shall be punished with`). An attempt at piracy alone is not `offence under s 130B(2)` (that needs s 511, general-part).

### SP-130E — "if the offence consists of the killing of any person"

One charge; the leaf chooses paragraph (a) (death, mandatory) or (b), and the charge cites "130E(a)" or "130E(b)", as SP-1.

## Chapter 7

### SP-139 — the saving

s 139 bars punishment under the Code where service-discipline law punishes a corresponding offence. It is encoded as `` `not subject to punishment under this Code within section 139` ``, and — like a general exception (PLAN section 5) — not repeated in the Chapter 7 ladders: it is a bar to punishment, not an element the charge asserts under CPC s 123(5). At integration the charge sheet should read it beside them. The service-discipline law (Singapore Armed Forces Act 1972) is not in the inputs.

### SP-140B — "with the necessary modifications"

s 140B extends Chapter 7 to the Singapore Police Force and attached forces. Encoded as a second leaf ORed beside the armed-forces leaf. "Superior officer", "mutiny", "desertion" and "insubordination" for a police officer are left to the leaves' ordinary meaning; the necessary modifications are not spelled out and the encoding does not spell them.

## Chapter 8

### SP-141 — "offence" in s 141(c)

s 40(3) widens "offence" in s 141 to other written law punishable with 6 months or more. That is in the leaf's `@desc`, not a ladder: pc-general's `offence within section 40` is the drill-down if one is wanted.

### SP-142 / 145 / 146 — who is a "member"

- s 146 makes "every member of such assembly" guilty of rioting. **Taken:** "member" is s 142's defined term (aware of the facts, joins or continues intentionally), so `guilty of rioting` calls `member of an unlawful assembly within section 142`. The alternative — anyone present — reads out s 142's definition, which s 7 says is used "in every part of this Code".
- s 145 ("Whoever joins or continues in an unlawful assembly, knowing that [it] has been commanded … to disperse") does not say "member", so **taken:** it needs the assembly to be unlawful (s 141) and the joining or continuing, but not s 142's awareness of the facts. Knowing of the command to disperse will usually carry that awareness anyway.

### SP-144 — "or with any combination of such punishments"

s 144 allows imprisonment, fine and caning in any combination. The shared `Punishment` record has only `or with both`, set TRUE; `words` carries the Code's phrase. A three-way combination flag would be a shared-record change for the ontology owner.

### SP-149 — no charge of its own

s 149 makes each member "guilty of that offence"; the charge is under that offence's punishing section "read with section 149". The predicate is exported; the charge is framed at integration with pc-general's `frame the charge read with`. Not built here, because the offence charged is another section's (often another group's — hurt, s 323).

### SP-150 — "punishable as a member of such unlawful assembly"

s 150 borrows s 143's punishment; the record is s 143's data with `words` saying so. The second limb (liability for the hireling's further offences "as if he … himself had committed such offence") is another deeming rule like s 149 and is not framed here.

### SP-151 — the Explanation

"If the assembly is an unlawful assembly within the meaning of section 141, the offender will be punishable under section 145."
- **Reading A (taken):** a signpost; it does not take an unlawful assembly out of s 151, so s 151 has no "not an unlawful assembly" leaf.
- **Reading B:** s 151 is confined to assemblies that are NOT unlawful.
B would make the lesser offence unavailable exactly where the facts are worse; A leaves the prosecution its choice.

### SP-154 — "and do not … and do not … do not"

The owner is punishable "if he or his agent or manager … do not give the earliest notice …, and do not, in the case of … reason to believe that it is about to be committed, use all lawful means … to prevent it, and in the event of its taking place, do not use all lawful means … to disperse or suppress".
- **Reading A (taken):** three cumulative duties; failing any one is the offence.
- **Reading B:** all three failures are needed.
B would let an owner who reported late escape by also suppressing; A reads the "and" as listing what the owner must all do. Genuinely arguable.

### SP-155 / 156 — "he or his agent or manager"

s 155's reason to believe and failure to act may be the owner's or the agent's; one leaf each carries both, and the `@desc` says so. s 156 is the agent's own offence on the same record.

### SP-157 — "harbour" in Chapter 8

ss 130A and 140A define "harbour" "In this Chapter" — Chapters 6 and 7. s 157 is in Chapter 8, so "harbours" has its ordinary meaning there. No drill-down.

## Chapter 9

### SP-161 — "being or expecting to be a public servant"

Two leaves ORed. The "Expecting to be a public servant" Explanation (a person not expecting office who deceives others is not guilty) is the `@desc` of `expecting to be a public servant` and a tested negative. The "motive or reward" Explanation widens `as a motive or reward` (illustrations (b) and (c) — a reward for influence never exercised — are satisfied through it).

### SP-164 — one record for ss 162–164

s 164 punishes the public servant "in respect of whom" a s 162 or s 163 offence is committed, who abets it. The record's taking leaves describe the taker (B, in the illustration); `` `the accused is the taker` `` switches ss 162/163 to the accused, and s 164's ladder calls the s 162/163 predicates (not the `offence under` ones) so that the taker need not be the accused. The illustration's two charges — B under s 163, A under s 164 — are two fixtures over the same facts.

### SP-169 — "the property, if purchased, shall be confiscated"

Recorded as forfeiture `shall be punished with`; the "if purchased" condition is in `words` and in the leaf `the property is purchased`, which the record cannot condition on.

## Chapter 10

### SP-175 / 178 / 179 / 180 — s 21(2)

s 21(2) says a judge within the Administration of Justice (Protection) Act 2016 is not a "public servant" for ss 175, 178, 179, 180 (and 228). Those four records' `public servant` leaf says so in its `@desc`, and the drill-down is pc-general's s 21(2) ladder. A test fixture for s 178 answers the leaf FALSE for such a judge.

### SP-177 — the Illustration presupposes the duty

s 177 illus: a landholder "knowing of the commission of a murder … intentionally misinforms the police". s 177 requires that the person be "legally bound to furnish information"; the illustration does not say so (the duty comes from the Criminal Procedure Code 2010, not in the inputs). The fixture answers that leaf TRUE, as the illustration must assume for "A is guilty".

### SP-182 — "knows or believes"; "intending … or knowing it to be likely"

Each split into two leaves so the charge can say which; the ladder ORs them. The two results (use of lawful power to injury or annoyance; doing or omitting what the public servant would not on the true facts) are ORed. Illustration (d) (wasted police time) is the second result.

### SP-186 — s 186(2)

"an obstruction may be caused other than by the use of physical means or threatening language" widens the `obstructs` leaf (its `@desc`); it adds no limb. The illustration (a false report to paramedics) is asserted.

### SP-188 — is subsection (2)'s harm in addition to subsection (1)'s?

s 188(2): "If such disobedience mentioned in subsection (1) causes or tends to cause danger to human life, health or safety, or … a riot or an affray, the person who is guilty of an offence under that subsection shall — …".
- **Reading A (taken):** (2)'s harm is its own condition: `offence under s 188(2)` = the disobedience + (2)'s harm, without (1)'s "obstruction, annoyance or injury … to any person lawfully employed".
- **Reading B:** (2) presupposes guilt under (1), so both harms are needed.
B is the literal effect of "guilty of an offence under that subsection". A is licensed by the Illustration — a procession that "causes danger of riot", with nothing said of any person lawfully employed, and "A has committed the offence defined in this section" — and by the section's pre-2019 form, a single sentence in which the two harms were alternative triggers. Under B the Illustration would not be an offence under s 188(2); it is asserted under A and passes.

### SP-188-Expl — no intent to harm

The Explanation ("It is sufficient that he knows of the order which he disobeys, and that his disobedience produces, or is likely to produce, harm") is why no leaf asks for intent to harm: the knowledge leaf's `@desc` cites it.

## Where I looked and found no fork

ss 121A, 121B, 122, 123, 126–129, 131–138, 140, 143, 147, 148, 152, 153, 158, 162, 163, 165–168, 170, 171, 172–176, 178–181, 183–185, 187, 189, 190: the elements are stated conjunctively with explicit "or"-lists, and the encoding follows them word for word. The recitals in all of them are subject to SP-4.
