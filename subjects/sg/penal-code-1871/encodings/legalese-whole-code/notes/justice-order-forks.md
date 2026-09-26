# Forks - justice-order group (Penal Code 1871, Chapters 11-15)

Every ambiguity met while encoding ss 191-298A: the readings, the one taken, why, and the text that licenses each.
Numbered `JO-n`; the modules cite them by number.
None has been settled by a court or a domain expert in this job; each is the encoder's reading, open for HG1 review.

Where I looked: every section of Chapters 11, 12, 14 and 15 was read against its punishing words and Explanations while writing its ladder.
Chapters 12's live sections (255-263) and 13 (wholly repealed) raised none.

## JO-1 - s 191 Explanation 2: a false statement of belief

**Text.** "a person may be guilty of giving false evidence by stating that he believes a thing which he does not believe".
**Readings.** (a) "The statement is false" means the fact stated is false. (b) A statement of belief is false when the belief is not held, whatever the fact.
**Taken.** (b), in the `the statement is false` leaf's @desc. Illustration (c) is then a case where the statement is *not* false (the belief is held), which is how the Code explains it: "true as to his belief".

## JO-2 - ss 196-200: "in the same manner as if he gave false evidence"

**Text.** ss 196-200 punish "in the same manner as if he gave [or fabricated] false evidence"; s 193 has two limbs, 7 years for a stage of a judicial proceeding and 3 years "in any other case".
**Readings.** (a) Use the s 193 limb the use, certificate or declaration would fall under: a stage of a judicial proceeding or not. (b) Always the lighter limb, since a certificate is not "evidence given". (c) Always the heavier.
**Taken.** (a). A leaf, `in any stage of a judicial proceeding`, selects the limb, and the charge's `punishment` recites the section's own phrase followed by "(section 193: <the limb's words>)". The Code does not name the limb, so a reviewer may prefer to recite the phrase alone.

## JO-3 - tiered punishments that depend on the predicate offence

**Text.** ss 201, 212, 213, 214, 216 ("if the offence is punishable with death ... (b) ... imprisonment for life or ... 20 years ... (c) ..."), 221, 222.
**Readings.** (a) The tier is part of the offence: where none holds (for example the screened offence is punishable with fine only, or for s 212(1)(c) with imprisonment of less than one year), the section prescribes no punishment and no charge can be framed. (b) The offence is made out anyway and only the punishment is unknown, which would be a `REFUSE` in the punishment.
**Taken.** (a). The tier disjunction is a conjunct of `offence under s N`, so the charge refuses and names the tier. A `REFUSE` inside a `Charge`'s punishment string would crash the charge generator, which reads that field unconditionally.
**Note the Code's own drift.** Paragraph (c) says "any term not extending to 20 years" in s 201, "which may extend to one year and not to 20 years" in ss 212 and 216, and "not extending to 20 years" in ss 213 and 214. Each leaf uses its section's words, so a fine-only offence satisfies no tier in any of them, and an offence of under a year satisfies s 201(c) but not s 212(1)(c).
**Owed at integration.** The tier leaves are facts about another offence's punishment. They could be computed from that offence's `Punishment` record with `pc-general`'s `punishable with death or imprisonment for life` and `punishable with imprisonment for ... within section 41`. That needs a "predicate offence" noun (proposed below).

## JO-4 - s 198 reads "knowing"; s 197 says "knowing or believing"

**Text.** s 197 "knowing or believing that such certificate is false"; s 198 "knowing the same to be false".
**Taken.** Separate leaves: s 198 reads `knowing the certificate to be false in any material point`, so belief short of knowledge does not satisfy it. (An earlier draft shared the s 197 leaf and over-included; fixed before delivery.)

## JO-5 - s 204: what "with the intention of preventing ..." attaches to

**Text.** "secretes or destroys any document ... or obliterates or renders illegible ... with the intention of preventing the same from being produced ..., or after he has been lawfully summoned or required to produce the same".
**Readings.** (a) The intention, or alternatively the summons, attaches to every act (secreting, destroying, obliterating). (b) It attaches only to the obliterating limb, so secreting or destroying a producible document needs no intention.
**Taken.** (a). Reading (b) would make innocent destruction of any producible record an offence.

## JO-6 - s 220: which section the charge cites

**Text.** s 220(1) defines the offence ("shall be guilty of an offence"); s 220(2) punishes it.
**Taken.** `offence under s 220` / `charge under s 220`, with section string "220". The `Punishment` record's `section` is "220(2)". A reviewer may prefer "220(1)" in the charge's closing words ("punishable under section 220(2)"). The same shape recurs in ss 267C(3), 268B(1), 268C(1), 284(3), 285(2), 287(3), 288(2), 289(2) and 292A(1), where the charge also cites the bare section.

## JO-7 - s 225: more than one aggravating paragraph

**Text.** (b) life or 20 years; (c) punishable with death; (d) under a sentence of 10 years or upwards; (e) under sentence of death. The Code gives no order among them.
**Taken.** The charge picks, in order, (e), then (c), then (d), then (b), and otherwise (a). That is heaviest first, with (c) and (d) (both 10 years plus fine) ordered by paragraph.

## JO-8 - result-graded offences: one offence or one per paragraph

**Text.** ss 284, 285, 287, 288, 289: subsection (1) lists results (a)-(e/f); a later subsection punishes by paragraph.
**Readings.** (a) One `offence under s 284` whose charge picks the punishing paragraph from the gravest result established. (b) One `offence under s 284(3)(b)` (and so on) per punishing paragraph, each a separate catalogue card.
**Taken.** (a), for one card per section. The cost is that a charge generator cannot show "charged under (1)(c), punishable under (3)(b)"; the charge cites "section 284". Moving to (b) is mechanical.
**Also.** The shared result leaves blur the Code's small differences: s 284(1)(c) says "hurt" where s 287(1)(c) says "hurt or injury", and s 284(1)(d) says "grievous hurt or injury" where s 287(1)(d) says "grievous hurt". Each leaf's @desc records the difference.

## JO-9 - s 267C: subsections (1) and (2) as one offence

**Text.** (1) utterance, placing, publication or communication, with (e) intention or (f) knowledge that violence etc. will occur "as a result"; (2) making or holding for that purpose, with (c) intention or (d) knowledge that it will occur "by the carrying out of the purpose". (3) punishes both.
**Taken.** One ladder with the (1) and (2) acts as alternatives and one pair of mental-element leaves for both. The difference between "as a result" and "by the carrying out of the purpose" is not modelled.

## JO-10 - s 292: (1A) and (1B) collapsed into two leaves

**Text.** (1A)(a)-(h) raise the punishment paragraph by paragraph where the dealing is by electronic means to 10 or more individuals; (1B) raises it where the object depicts a person below 18.
**Taken.** One leaf, `by electronic means, to 10 or more individuals`, and one child-image leaf. The charge picks (1B)(a) where both hold, then (1B)(b) where only the child-image leaf holds, then (1A), then (1). The pairing of (1A)(g)-(h) with the specific (1)(e)-(f) acts is lost. (1C) is its own offence, `offence under s 292(1C)`.

## JO-11 - s 195(1) and (2) overlap

**Text.** (1) "not capital, but punishable with imprisonment for a term of 7 years or upwards"; (2) "not capital, but punishable with imprisonment for life".
**Readings.** (a) Disjoint: (2) takes offences punishable with life, (1) the rest. (b) Overlapping: an offence punishable with "imprisonment for life or imprisonment up to 20 years" meets both.
**Taken.** The leaves are independent and both offences can be made out. Which one to charge is the prosecutor's choice, and the encoding does not decide it.

## JO-12 - s 194: "the person who gives such false evidence"

**Text.** The death limb applies when an innocent person is executed in consequence, to "the person who gives such false evidence". The first limb covers anyone who "gives or fabricates".
**Readings.** (a) Literal: the death limb reaches only one who GIVES. (b) Purposive: "such false evidence" refers back to "gives or fabricates", so fabricators are included.
**Taken.** (a). The charge applies the death-limb punishment only when the execution leaf holds AND `gives false evidence` holds; a fabricator gets the first limb.

## JO-13 - s 193: "intentionally" and fabrication

**Text.** "whoever intentionally gives false evidence ... or fabricates false evidence for the purpose of being used ...; and whoever intentionally gives or fabricates false evidence in any other case".
**Taken.** "Intentionally" is a separate leaf for giving only. Fabrication carries its intention inside s 192 ("intending that ..."), so no further leaf is asked for it.

## JO-14 - negative "not otherwise provided for" elements

**Text.** s 225A "in any case not provided for in section 221, 222 or 223, or in any other law"; s 225B likewise for ss 224, 225; s 225C "when no special punishment is provided by the law"; s 290 "in any case not otherwise punishable by this Code".
**Taken.** Each is a BOOLEAN leaf, which asks the investigator a legal question rather than a factual one. At integration these could be computed by asking whether the more specific offence's ladder holds on the same facts (for example, s 225B's leaf is NOT `offence under s 224` and NOT `offence under s 225`). That needs a join across records.

## JO-15 - exceptions printed inside a section: NOT-limbs, and schema completion

**Text.** s 204A Explanation 1 ("a mere warning ... is insufficient"); ss 213-214 Exception (offence lawfully compoundable); s 215 "unless he uses all means in his power"; s 292 Exception (religious objects) and (3) (authorised dealing); s 286 "until the contrary is proved".
**Taken.** Each is `AND NOT <leaf>` in the ladder, following PLAN.md s 5 for exceptions that are part of their own section.
**Consequence.** The charge generator completes an unknown leaf as FALSE, so an unanswered exception lets the charge frame. That fits the burden on the accused (PLAN.md s 5). But a reviewer should know that the charge does not ask the question.

## JO-16 - s 286's presumption inside the s 285 ladder

**Text.** s 286: in proceedings under s 285, a person who drops a cigarette (etc.) where a fire occurs within 60 minutes "is, until the contrary is proved, presumed to have substantially contributed to the risk of causing that fire".
**Readings.** (a) A rule of evidence, kept off the offence ladder. (b) An alternative way the "substantially contributes" element is established.
**Taken.** (b). The s 285 ladder reads "contributes OR presumed within section 286", and the presumption's own ladder includes `NOT the contrary is proved`. So the rebuttal is visible and can be toggled.

## JO-17 - s 290(b) and (c): the same punishment, two grounds

**Taken.** Two punishment records with identical words. The charge picks (b) (knowledge) before (c) (a second or subsequent conviction). The recital does not say which ground was relied on. Whether a previous conviction belongs in the charge at all (CPC 2010) was not checked in this job's inputs.

## JO-18 - s 204B(1)(d) reads "any person will as a witness ..."

**Text.** (b) "any person called or to be called as a witness"; (d) "any person will as a witness in any judicial proceeding give false testimony".
**Taken.** Both share the witness-understanding leaf, which says "called or to be called". Paragraph (d)'s wording is arguably wider, covering a person not yet called, and the shared leaf's @desc does not say so.
