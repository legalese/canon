# Fork register — Chapters 1-2, the Punishment record and the charge machinery (ontology agent)

Each fork: the text, the readings, the one taken, and why.
Where a fork decides something every encoder inherits, it says so.

## G-1. s 22 — "property" has no closed test

**Text.** "'property' means money and all other property, movable or immovable, including things in action, other intangible or incorporeal property and virtual currency"; "'movable property' includes property of every description, except immovable property".
**Readings.** (a) Encode "property" as a disjunction of the listed kinds. (b) Treat it as inclusive and encode only the definitions that draw a line.
**Taken.** (b). The definition is circular ("all other property") and inclusive ("including"), so a disjunction of the listed kinds would wrongly exclude an ordinary chattel, which is property but is none of money, a thing in action, intangible property or virtual currency. "Immovable" has a closed test and is encoded; "movable" is its complement, exactly as the Code says ("every description, except immovable"), so a thing in action and virtual currency are movable property — tested.

## G-2. s 28 Explanation 2 — a presumption in a definition

**Text.** "Where a person causes one thing to resemble another thing and the resemblance is such that a person might be deceived thereby, it shall be presumed until the contrary is proved that the person … intended … to practise deception or knew it to be likely …"
**Readings.** (a) A rule of evidence, outside the ladder; the leaves "intending … deception" and "knowing it to be likely …" are answered by whoever weighs the evidence, presumption included. (b) A third route to the mental element on the ladder, closed by a leaf "the contrary is proved".
**Taken.** (b), so that an investigator toggling leaves sees why a close imitation is counterfeiting without proof of intent. The cost: the leaf "the contrary is proved" is a defence-side fact, and an investigator filling the record will leave it FALSE — which is the Code's own default ("until the contrary is proved").

## G-3. s 26B — good faith is defined only negatively

**Text.** "Nothing is said to be done or believed in good faith which is done or believed without due care and attention."
**Readings.** (a) Due care and attention is necessary AND sufficient: the ladder is the one leaf. (b) It is necessary only; good faith needs something more the Code does not state (honesty), so a TRUE answer should be a refusal or a second leaf.
**Taken.** (a), because the Code gives no other content. Whether Singapore case law adds honesty to care is **not settled by this job's inputs**, and I did not look it up. An encoder whose section needs honesty as well adds that leaf beside `in good faith` in its own ladder, not inside this one. The NOT case (no care, no good faith) is the only one tested, because it is the only one the text settles.

## G-4. ss 26D(3), 26E(3), 26F(2) — do the substitutes chain?

**Text.** 26D(3): knowingly "is also established where that act is done intentionally or with wilful blindness". 26E(3): rashly "is also established where that act is done intentionally or knowingly". 26F(2): negligently "… intentionally, knowingly or rashly".
**Readings.** (a) Literal: each subsection's list is its own, so wilful blindness establishes knowingly but not rashly or negligently. (b) Chained: rashly is established "knowingly", and knowingly is established by wilful blindness, so wilful blindness establishes rashly (and negligently).
**Taken.** (a), and asserted as such (`NOT (the fault element rashly is established by with wilful blindness)`), because 26D(3) says it applies "where doing an act knowingly is a fault element", which rashness is not. Reading (b) is arguable and a court may take it; flipping to it is a one-line change in `the fault element … is established by …`.

## G-5. s 26G — whose elements, proven against whom

**Text.** (2) "Where all the fault elements and physical elements of the offence have been proven … and assuming no defence or exception applies, the accused person shall be guilty … despite …"; (3) "applies only where the accused person did or caused the physical elements … negligently in respect of the person or thing mentioned".
**Readings.** The physical elements are proven as against the person or thing actually affected, the fault elements as against the one intended; the atoms could separate the two.
**Taken.** One leaf each for "all the fault elements … are proven" and "all the physical elements … are proven", with the @desc saying which person each is read against. Illustration (3)(b) (the vase and the clay pot) has the same atoms as (3)(a), so it is noted beside (a) rather than asserted twice. The s 26G(5) defence rule is taken as the single leaf "a defence or exception applies"; wiring it to Chapter 4/4A is the exceptions group's.

## G-6. Numeric thresholds and the charge generator's schema completion — inherited by every encoder

**Text.** `reference/charge-generator-README.md`: "A partial facts record is completed against the export's schema before the wire: an unknown element is FALSE, because a charge cannot assert what is not known."
**Readings.** (a) Put ages and amounts on the facts record as NUMBERs and compare in the ladder. (b) Put a BOOLEAN leaf in the Code's words on the ladder, and a NUMBER→BOOLEAN helper beside it that fixtures and the interview use to set it.
**Taken.** (b) (`PLAN.md` §3.5). Under (a) an unknown age would be completed as some number — if 0, "below 16 years of age" becomes TRUE and a charge is framed on a fact nobody supplied; the README does not say what a NUMBER is completed to, and I did not find out. Under (b) the unknown leaf is FALSE, which is the safe direction, and the threshold is still tested on the helper. The same reasoning excludes `MAYBE` and `LIST` fields from anything an exported ladder reads.

## G-7. The number a charge is "read with" — inherited by general-part

**Text.** CPC s 123(4): "the law and section of the law against which the offence is said to have been committed must be mentioned". Penal Code s 511 defines an attempt; s 512 (since Act 15 of 2019) punishes it.
**Readings.** An attempted theft is charged "punishable under section 379 read with section 511" (the long-standing form) or "… read with section 512".
**Taken.** Neither: `frame the charge read with` takes the list of sections as data, and the general-part encoder decides and records the fork. The rider joins several with " and section " and puts s 34 last ("read with section 511 and section 34"); that ordering is a choice, not a quotation — I found no reported charge in the inputs that combines them.

## G-8. Chapter 2 words as flat leaves — inherited by every encoder

**Text.** s 7 and CPC s 126: a word keeps its Chapter 2 meaning everywhere.
**Readings.** (a) Nest the Chapter 2 facts record in each offence record and call its ladder, so `dishonestly` is computed. (b) A flat BOOLEAN leaf `dishonestly` whose @desc cites s 24, with s 24's ladder exported as a drill-down.
**Taken.** (b), the reference row's recorded design call: a call is drawn as one untoggleable box, and the charge generator's `DEFINITION_LADDERS` already offers the drill-down for ss 24 and 25. The cost, stated so nobody is surprised: nothing checks that the leaf agrees with the definition's ladder — the investigator answers both.

## G-9. s 30 — what must "purport"

**Text.** "a document or an electronic record which is, or purports to be, a document or an electronic record whereby any legal right is created, extended, transferred, restricted, extinguished, or released, or whereby any person acknowledges …"; (2) cards "notwithstanding the generality of subsection (1)".
**Taken.** Subsection (1) needs both a s 29 document or an electronic record, and the right-creating (or acknowledging) character, which the leaf asks about as "is or purports to be". Subsection (2) cards are valuable securities whether or not they are also s 29 documents — "notwithstanding the generality" is read as widening, not as a condition.

## G-10. s 40 — how the context is given

**Text.** (2) "In Chapters 4, 4A, 5 and 5A, and in sections 4, 187, …"; (3) "In sections 141, 176, …, 'offence' has the same meaning when the thing punishable under any other law … is punishable … with imprisonment for a term of 6 months or upwards".
**Taken.** The ladder takes the Chapter and the section in which the word is read as two strings, and the lists as named constants, so a caller cites the provision it is reading. (3)'s "the same meaning when" is read as: an offence under this Code, or a thing punishable under another law with 6 months or upwards. The 6-month question is a leaf, not a call to s 41, because the other law's punishment is not encoded.

## G-11. s 41 — a punishment with no stated maximum

**Text.** "punishable with imprisonment for a specified term or upwards includes an offence for which the specified term is the maximum term".
**Taken.** Maximum term at least the specified term (inclusive, as s 41 says); imprisonment for life always qualifies; no imprisonment never does; imprisonment with no stated maximum is REFUSED by name rather than guessed.

## G-12. `Punishment` — one "or with both" flag

**Text.** s 417 "imprisonment … or with fine, or with both"; s 420(1) "shall also be liable to fine or to caning or to both".
**Taken.** One BOOLEAN `or with both` per record. It does not say which pair "both" joins; where that matters, `words` (verbatim) is authoritative and the reader of the record must read it. A richer shape (a list of alternatives) was not built, because nothing in this job reads it yet.

## G-13. s 21 Explanation 2 — not a condition

**Text.** "Wherever the words 'public servant' occur, they shall be understood of every person who is in actual possession of the situation of a public servant, whatever legal defect there may be in his right to hold that situation."
**Taken.** Not a leaf. The (a)-(j) atoms ask what office the person holds and what duties it carries, as facts; Explanation 2 says a defect in the appointment does not matter, so no atom asks about it. Making "in actual possession" a conjunct would have turned an extension into a restriction.

## G-14. The task's range "ss 6-52B"

The source's Chapter 2 ends with "52. [Repealed by Act 15 of 2019]" (line 2094 of `inputs/PC1871.txt`); there is no s 52A or 52B in the text or in its table of contents. The coverage table follows the source.

## G-15. Evidence Act burden for general exceptions — a citation not verified

`PLAN.md` §5 cites Evidence Act 1893 s 107 for the rule that the accused bears the burden of bringing a case within a general exception. That Act is not in this job's inputs, and I did not check the section number; the PLAN says so and asks the exceptions encoder to verify or drop it. Nothing in the encoding depends on the citation — only the explanation of why a charge is not refused when an exception might apply.
