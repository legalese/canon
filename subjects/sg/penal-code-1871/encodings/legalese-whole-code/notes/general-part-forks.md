# Fork register — general-part (Chapters 1, 3, 5, 5A, 23)

Each fork gives the text, the readings, the one taken, and why.
Two of them (GP-10, GP-14) are **findings**: an Illustration that does not follow from the Code's current text.
Each has an assertion left failing in `pc-general-part-tests.l4`.

## GP-1. The section a charge of abetment, conspiracy or attempt is laid under — inherits G-7

**Text.** CPC 2010 s 123(4): "the law and section of the law against which the offence is said to have been committed must be mentioned in the charge".
s 109: "be punished with the punishment provided for the offence"; s 116(1): "in the same manner as if the abettor had committed the offence"; s 115: its own term; s 120B: "in the same manner as if he had abetted the offence"; s 511 defines an attempt and s 512 (since Act 15 of 2019) punishes it.
**Readings.** An abetment could be charged "punishable under section 109" alone, or "under section <offence> read with section 109". An attempt could be "read with section 511" (the long-standing form) or "read with section 512". A conspiracy could be "120B read with <offence>" or "<offence> read with 120B".
**Taken.**
- s 109 and s 116: "<offence section> read with section 109 / 116", because the punishment is the offence's own, so the offence's section is the one "against which" it is punishable; it is the form I recall from reported abetment charges, but I have not verified it against any charge in this job's inputs.
- s 115 and s 117-120: the section alone, because each fixes its own punishment. The s 115 recital names the offence abetted and its section.
- s 120B: "120B read with section <offence section>", because s 120B is the punishing section and the offence section identifies the object.
- s 512(1), s 512(2): "<offence section> read with section 511".
**Not verified against any reported post-2019 charge** — none is in this job's inputs. Each is one argument to `frame the charge read with` in the `charge under` function, so changing it is a one-line edit per section; the tests pin the choice (`'s section EQUALS "379 read with 511"`), so a change will show.

## GP-2. The Schedule's ranges ("sections 379 to 382")

**Text.** Items 3-14 name ranges of sections.
**Readings.** (a) Only the whole-numbered sections in the range. (b) Every section the Code prints between the ends, including lettered ones (379A) and definition sections (470, 473C).
**Taken.** (b), from the table of contents of `inputs/PC1871.txt`. A definition section in a range defines no offence, so listing it is harmless. Sections before a range's first number (416A before 417) are outside it. Item 15 (fraud, dishonesty or deception, excluding the Prevention of Corruption Act 1960 and the Securities and Futures Act 2001) is a separate limb over two booleans.

## GP-3. s 74(2)(a) — are offences punishable with death or life inside or outside?

**Text.** "(a) an offence under this Code except sections 298 and 298A, and an offence which is punishable with death or imprisonment for life".
**Readings.** (a) "and an offence which is punishable …" is a second thing *included*. (b) It is a second thing *excepted*, parallel to 298/298A.
**Taken.** (b). Every sibling (ss 73(4)(b), 74A(3)(b), 74B(1)(c), 74C(1), 74D(1)) excepts offences punishable with death or life. Under (a), s 74 would double a punishment that has no maximum to double. Grammatically (a) is at least as natural, so this is a real ambiguity. Flipping it means deleting one `AND NOT` line in `enhanced penalty under s 74`.

## GP-4. s 74C(5) — factors are not a ladder

**Text.** The court "may determine whether [A] was or is in an intimate relationship with [B] having regard to all the circumstances of the case, including the following: (a) … (f)". Two of them say they are "not necessary".
**Taken.** One leaf, `the victim was or is in an intimate relationship with the offender`, with the six factors in its `@desc`. Any ladder over (a)-(f) would make some combination sufficient or necessary, and the Code makes none of them either.

## GP-5. s 74E(2)(a) — what "does not apply to enhance such punishment" leaves alone

**Text.** "Where any punishment prescribed for an offence is (a) a specified minimum sentence or a mandatory minimum sentence of imprisonment or caning, section 73 … does not apply to enhance such punishment".
**Readings.** (a) Only the minimum is not doubled. But ss 73-74D double the *maximum* and never touch a minimum, so on this reading (a) says nothing. (b) Where the imprisonment carries a minimum, that imprisonment, including its maximum, is not enhanced at all.
**Taken.** (b), because it gives (a) some effect, and because it errs toward the lower exposure. `twice the maximum punishment of` p `under section` s leaves `maximum term in months` unchanged when `minimum term in months` is set. That is tested on s 392 (max 120 months stays 120). The fine is still doubled in that case, since (2)(a) names only imprisonment and caning. (2)(b) is unambiguous: the maximum strokes are never doubled.

## GP-6. ss 116(2) and 512(3) — "such sentence or combination of sentences as the court thinks fit"

**Readings.** Every kind the offence prescribes becomes (a) `or with` (alternatives, which may be combined: `or with both` TRUE), or (b) `shall also be liable to` (discretionary, in addition to something mandatory).
**Taken.** (a). Once the court is not bound by the minimum, nothing is mandatory, so there is no mandatory punishment for (b)'s "in addition" to attach to. The s 512(4) Illustration ("6 months imprisonment with no caning") fits (a). s 116(3) / s 512(4) are kept by leaving a kind the offence does not prescribe `not prescribed`: robbery's fine stays `not prescribed` ("the court may not sentence A to a fine"). `or with both` is one flag (G-12), so it does not say which kinds combine; `words` is authoritative.

## GP-7. s 116 Illustrations (c) and (d) — a police officer who is no longer in the text

**Text.** (c) "A, a police officer, whose duty it is to prevent robbery, abets the commission of robbery. Here, though the robbery is not committed, A is liable to the maximum term of imprisonment provided for that offence." (d) "B abets the commission of a robbery by A, a police officer … B is liable to the same punishment as if he had committed the offence of robbery."
**Reading.** These read as survivals of an earlier s 116. The earlier text is not in this job's inputs, so that is my inference and not a verified fact. It seems to have given an ordinary abettor a fraction of the term and a police officer the whole of it. The current (1)-(3) say nothing about office: every abettor of an offence punishable with imprisonment that is not committed is "punished in the same manner as if the abettor had committed the offence".
**Taken.** Both Illustrations are asserted as offences under s 116, and no leaf asks about the abettor's office. What (c) says is still true under the current text, because the maximum term is the offence's own. It just no longer distinguishes anything.

## GP-8. ss 119, 120 — a fraction of "the longest term provided for that offence"

**Text.** s 119: "one-half" / "one-fourth part of the longest term provided for that offence", with separate terms (15 and 7 years) where the offence is punishable with death or life. s 120: "one-fourth" / "one-eighth", with **no** such proviso.
**Readings.** For s 120 and an offence punishable with imprisonment for life: (a) life has no term, so there is no fraction; (b) take life as some number of years. I recall that the repealed s 57 once did that (the inputs show only "57. [Repealed by Act 51 of 2007]", so this is unverified); nothing in force does.
**Taken.** (a). `the fraction` k `of the longest term provided for` p REFUSES by name when the offence prescribes imprisonment for life, or states no maximum term. Where the offence is punishable with death or life, s 118 is the likelier charge anyway. The `offence under s 120` ladder itself does not refuse: whether "punishable with imprisonment" includes imprisonment for life is pc-general's `punishable with imprisonment`, which counts it.

## GP-9. s 511(2) — the examples are not sufficient

**Text.** "an act is a substantial step … if it is strongly corroborative of an intention to commit the offence and the following are examples of acts which in the circumstances of each case **may** constitute taking a substantial step: (a) … (g)".
**Taken.** The test is the one leaf, `the act is strongly corroborative of an intention to commit the offence`. The seven examples are its `@desc`. A limb for each example would make lying in wait sufficient in every case, which "may … in the circumstances of each case" denies.

## GP-10. FINDING — the s 512(4) Illustration and s 393

**Text.** s 512(2) applies "where no express provision is made by this Code … for the punishment of such attempt". s 393: "Whoever attempts to commit robbery shall be punished with imprisonment for a term of not less than 2 years and not more than 7 years and shall also be liable to caning." The s 512(4) Illustration: "A attempts to commit robbery … As the court is not bound to impose the minimum mandatory punishment prescribed for robbery, A may be sentenced to 6 months imprisonment with no caning for attempted robbery."
**The conflict.** s 393 is an express provision for attempted robbery, so on the Code's words s 512(2)-(3) do not govern it. s 393 also has its own 2-year minimum, so 6 months is not available.
**Encoded.** The Illustration's arithmetic *is* encoded and tested: `the punishment under s 512(2) for attempting an offence punishable with` over s 392's punishment drops the minimum, keeps caning as optional, and allows no fine. The Illustration's conclusion on the offence is asserted and **left failing**: `#ASSERT offence under s 512(2) (s 512(4) illus)`, with the leaf `no express provision …` FALSE because of s 393.
**Reading for a human.** The Illustration probably means "an attempt to commit an offence like robbery" rather than robbery itself. A reviewer should say whether it means anything more.

## GP-11. The enhancements of ss 73-74D are not charges here

**Text.** Each says "the court may sentence the person … to twice the maximum punishment".
**Readings.** (a) A charge "punishable under section 323 read with section 73". (b) A sentencing power over a charge laid under the offence's own section.
**Taken.** Neither is built as a `charge under`. Each enhancement is an exported ladder over its own facts record, plus one function over `Punishment`. A read-with charge would need the underlying offence's `Charge`, which lives in another group's module. The integration step owed: a builder that takes an offence's `Charge` and adds " read with section 73(1)", so that the section, closing words and punishment all change together. Whether Singapore charges plead the enhancement in the charge (reading (a)) is **not settled by this job's inputs**.

## GP-12. Negative-polarity leaves, and NOT over a defence-side leaf, under schema completion

The charge generator completes an unknown leaf as FALSE.
- "if that offence is **not** committed in consequence of the abetment" (ss 115, 116) is a positive leaf, `that offence is not committed in consequence of the abetment`. Written as `NOT (committed in consequence …)`, an unknown would read as "not committed", and a charge would be framed on a fact nobody supplied. The same design call as the reference row's `without that person's consent`. The cost: nothing checks that this leaf and the s 109 limbs agree. The investigator answers both.
- The burden-on-the-offender provisos (ss 73(2), 74A(2A), 74B(3), 74C(3), 74D(3)) and the excluded offences are under `NOT`. An unknown reads as "not proved" or "not excluded", so the enhancement is shown as available. That is the right default for a proviso the offender must prove. For the exclusions (s 304B and so on) it relies on the investigator knowing which offence they are dealing with.
- s 116's exclusion of offences punishable with death or life (GP-13) and s 512(2)'s "(other than an offence mentioned in subsection (1))" is `NOT f's the offence attempted is punishable with death or imprisonment for life`. If that is unknown, a s 512(2) charge can be framed. Its punishment words ("such punishment as is prescribed for that offence") are right in either case, but the section would be wrong for a capital offence. The alternative, a second positive leaf, invites contradiction. The @desc tells the investigator to decide the leaf from the offence's `Punishment`.

## GP-13. ss 115 and 116 overlap on an offence punishable with death or imprisonment for life

**Text.** s 115 and s 116(1) both apply "if that offence is not committed in consequence of the abetment, and no express provision is made by this Code or [by] any other written law for the punishment of such abetment". `punishable with imprisonment` (pc-general) counts imprisonment for life, so an abetted murder that is not committed is "an offence punishable with imprisonment" too.
**The defect this fixed.** The first draft had one leaf for the proviso, shared by both ladders. The same leaf cannot be TRUE for s 115 (no other provision) and FALSE for s 116 (s 115 *is* the provision). Measured: `offence under s 116` held on the s 115 Illustration.
**Taken.** s 115 is read as the express provision that s 116's proviso excludes. `offence under s 116` adds `NOT … the offence abetted is punishable with death or imprisonment for life`, behind an inert string saying why. Asserted: neither the s 115 Illustration nor s 108 Illustration (a) is an offence under s 116. The cost is GP-12's: if that leaf is unknown, s 116 is not blocked.

## GP-14. FINDING — the s 118 Illustration and s 395

**Text.** s 118 needs "an offence punishable with death or imprisonment for life". Its Illustration: A misleads the police about an impending gang-robbery; "A is punishable under this section". s 395: "Whoever commits gang-robbery shall be punished with imprisonment for a term of not less than 5 years and not more than 20 years and shall also be punished with caning with not less than 12 strokes."
**The conflict.** Gang-robbery as s 395 now punishes it is not punishable with death or imprisonment for life, so the facts of the Illustration are s 120, not s 118. (s 396, gang-robbery *with murder*, is capital, but the Illustration describes plain gang-robbery.)
**Encoded.** Two fixtures. `s 118 illus` takes the Illustration's premise as given (the leaf TRUE), and `offence under s 118` holds. `s 118 illus, gang-robbery as s 395 now punishes it` computes the leaf from s 395's words. On it, `offence under s 118` is asserted as the Illustration says and **left failing**, and `offence under s 120` holds.

## GP-15. s 72 — partial

"The lowest punishment" is ordered only where it is obvious: identical punishments, or the same kinds prescribed the same way and differing only in maximum term. Everything else, such as a capped fine against an uncapped one or caning against none, is refused by name. That is a sentencing judgment, not arithmetic.

## Cross-module joins owed (PLAN §1)

These leaves stand for another group's rule or data and become calls at integration. The only edge needed is general-part → pc-general, which already exists. Every other group → general-part is the direction PLAN allows. **Nothing here needs an edge from general-part to another group**, because the other offence is carried as particulars.

| leaf (record) | owner | becomes |
| --- | --- | --- |
| `would constitute an offence under Chapter 6 or 6B if committed in Singapore` (`Extraterritorial Facts`) | state-public | a call into Chapter 6 / 6B, or stays a leaf |
| `the offence abetted is punishable with death or imprisonment for life`, `… with imprisonment` (`Abetment Facts`) | pc-general over the offence owner's `punishment prescribed by s N` | `punishable with death or imprisonment for life` (…) |
| `the offence designed is punishable with …` (`Concealment of Design Facts`) | the same | the same |
| `the offence attempted is punishable with death or imprisonment for life`, `the punishment prescribed for the offence is fixed by law or a minimum sentence` (`Attempt Facts`) | the same | `punishable with …`, `fixed by law or carries a minimum sentence` |
| every `… punishable with death or imprisonment for life` in the ss 73-74D records | the same | the same |
| `the offence is under section 304B, 304C or 335A` and the like | body-a | a comparison on the offence's section |
| the STRING particulars `the section punishing …`, `the punishment provided for …` | the offence's owner | read from its `punishment prescribed by s N`'s `section` / `words` |

The fuller integration the charge generator wants — `charge under s 379 read with 511` that stacks theft's ladder under the attempt card — would need either a generic "inchoate" wrapper over any offence's `Charge`, or per-offence attempt records nesting the offence's facts. Neither is built. The wrapper is the smaller change: `frame the charge read with` already takes the section list.

## Proposed shared nouns

None required. Two candidates, if other groups find the same need:
- `Kind of inchoate liability` (abetment / conspiracy / attempt), if the charge sheet wants to group read-with charges.
- A `Victim relationship` noun (employer, household member, employment agent, intimate partner, household member with frequent contact), if body-a and body-b encode their own aggravations.

## DEFINITION_LADDERS proposed

`{ fn: 'instigates within section 107', leaf: 'instigates any person to do that thing', section: '107' }`, `{ fn: 'aids within section 107', leaf: 'the aid is intentional', section: '107' }`. These are drill-downs only; the offence ladders already call them.
