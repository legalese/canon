# Coverage — Chapters 1 and 2 (ontology agent)

Source: `inputs/PC1871.txt`, Chapter 1 at line 1233, Chapter 2 at line 1315, Chapter 3 begins at line 2096.
Modules: `deposit/pc-domain.l4` (nouns), `deposit/pc-general.l4` (rules), `deposit/pc-general-tests.l4` (tests).
Chapter 2 ends at s 52 (repealed): the text has no ss 52A or 52B, although the task named the range "ss 6-52B".
No section of Chapter 2 is an offence, so none has an `offence under s N` or a `charge under s N`.

Dispositions: `encoded` (a ladder or data), `inert` (quoted in a comment, operative only as a convention or through another rule's `@desc`, with the reason), `out-of-scope` (with reason), `deferred` (with reason), `repealed`.

## Chapter 1 — Preliminary (ss 1-5)

Chapter 1 belongs to the general-part group (`pc-general-part.l4`), per `notes/PLAN.md` §1.
The ontology agent supplies only its nouns (`Place`, with `within Singapore`).

| s | heading | disposition | where |
| --- | --- | --- | --- |
| 1 | Short title | deferred — general-part group's | — |
| 2 | Punishment of offences committed within Singapore | deferred — general-part group's | noun: `Place`'s `within Singapore` |
| 3 | Punishment of offences committed beyond, but which by law may be tried within Singapore | deferred — general-part group's | — |
| 4 | Jurisdiction over public servants for offences committed outside Singapore | deferred — general-part group's | reads `public servant within section 21` |
| 4A | Offences against State and genocide committed outside Singapore by citizen or permanent resident | deferred — general-part group's | — |
| 4B | Punishment of specified offences with elements occurring in Singapore but others occurring outside Singapore | deferred — general-part group's | the Schedule is general-part's too |
| 5 | Certain laws not to be affected by this Code | deferred — general-part group's | — |

## Chapter 2 — General explanations (ss 6-52)

| s | heading | disposition | function(s) / reason |
| --- | --- | --- | --- |
| 6 | Definitions in this Code to be understood subject to exceptions | inert — a convention | No offence ladder repeats a general exception; exceptions are their own ladders (PLAN §5). Illustrations (a) and (b) belong to ss 82 and 76 and are the exceptions group's to test. |
| 6A | Definitions to apply to this Code and other written law | inert | Concerns other written law; this encoding covers only this Code. |
| 7 | Expression once explained is used in the same sense throughout this Code | inert — a convention | Why one ladder per word suffices (header of `pc-general.l4`). |
| 8 | "Gender" | inert | `Pronoun` (pc-domain) serves the charge; the Code's "he" needs nothing. |
| 9 | "Number" | inert | Interpretive. |
| 10 | "Man" and "woman" | encoded | `man within section 10`, `woman within section 10`; noun `Sex` |
| 11 | "Person" | encoded (noun) | `Kind of person`, `Person` (pc-domain) |
| 12 | "Public" | inert | Carried in the @desc of any leaf that uses "public". |
| 13-16 | [There are no sections 13 to 16.] | — | — |
| 17 | "Government" | inert | Carried in the @desc of leaves that use it (e.g. `Office`). |
| 18 | [There is no section 18.] | — | — |
| 19 | "Judge" | encoded | `Judge Facts`, `judge within section 19`; illustrations (a), (b), (c) tested |
| 20 | "Court of justice" | encoded | `Court Facts`, `court of justice within section 20` |
| 21 | "Public servant" | encoded | noun `Office` (pc-domain); `public servant within section 21`; s 21(2) as `public servant within section 21, for sections 175, 178, 179, 180 and 228`; Explanations 1 and 2 as the reason no atom asks about appointment |
| 22 | "Property" | encoded | noun `Property`; `immovable property within section 22`, `movable property within section 22`, `virtual currency within section 22`; "property" itself is inclusive with no closed test (FORK G-1); illustration tested |
| 22A | "Fault element" and "physical element" | inert | Names the two kinds of leaf; PLAN §3.7 asks encoders to mark them where it matters. |
| 23 | "Wrongful gain" and "wrongful loss" | encoded | `Gain or Loss Facts`, `wrongful gain within section 23`, `wrongful loss within section 23` (reference row, unchanged); Explanations 1-3 in the @desc |
| 24 | "Dishonestly" | encoded | `Dishonesty Facts`, `dishonestly within section 24` (reference row, unchanged — the catalogue calls it) |
| 25 | "Fraudulently" | encoded | `Fraud Facts`, `fraudulently within section 25` (reference row, unchanged); Explanation 1 as a proviso; Explanation 2 is a rule of pleading, noted |
| 26 | "Reason to believe" | encoded | `Belief Facts`, `reason to believe within section 26` |
| 26A | "Voluntarily" | encoded | `Voluntariness Facts`, `voluntarily within section 26A`; illustration tested |
| 26B | "Good faith" | encoded | `Good Faith Facts`, `in good faith within section 26B` (FORK G-3) |
| 26C | "Intentionally" | encoded | `Fault Facts`, `does the act intentionally within section 26C(1)`, `causes the effect intentionally within section 26C(2)`; (3), (4) and the Explanation are rules of proof, inert |
| 26D | "Knowingly" | encoded | `knowingly in respect of a circumstance within section 26D(1)`, `knowingly in respect of an effect within section 26D(2)`; (3) in `the fault element … is established by …` |
| 26E | "Rashly" | encoded | `rashly in respect of a circumstance within section 26E(1)`, `rashly in respect of an effect within section 26E(2)`; (3) in `the fault element … is established by …` (FORK G-4) |
| 26F | "Negligently" | encoded | `negligently within section 26F`; (2) in `the fault element … is established by …` |
| 26G | "Transferred fault" | encoded | `Transferred Fault Facts`, `guilty despite transferred fault within section 26G`; (4) and (5) as leaves; illustrations (3)(a)-(c), (4)(a)-(c) and (5) tested (FORK G-5) |
| 26H | "Strict liability" | encoded | `Strict Liability Facts`, `strict liability offence within section 26H(1)`, `defence of reasonable care within section 26H(4)`; (2), (3) in the @desc |
| 27 | Property in possession of spouse, clerk or servant | encoded | `Possession Facts`, `in that person's possession within section 27`; Explanation in the @desc |
| 28 | "Counterfeit" | encoded | `Counterfeiting Facts`, `counterfeits within section 28`; Explanation 2 as a rebuttable presumption (FORK G-2) |
| 29 | "Document" | encoded | noun `Document`; `document within section 29` |
| 29A | "Writing" | inert | Carried in the @desc of `is a document in writing`. |
| 29B | "Electronic record" | inert — out-of-scope definition | Has the meaning in the Electronic Transactions Act 2010, which is not in the inputs; carried as the leaf `is an electronic record`. |
| 30 | "Valuable security" | encoded | `valuable security within section 30`; illustrations (a), (b) tested |
| 31 | "A will" | encoded | `a will within section 31` |
| 31A | "Die" and "instrument" | encoded | `instrument within section 31A`; "die" in the @desc of `is a seal or die` |
| 32 | Words referring to acts include illegal omissions | inert | Widens every act-leaf; encoders say so in the @desc where it matters. |
| 33 | "Act" and "omission" | inert | As s 32; (2) and its illustration are a rule of causation-proof. |
| 34 | Each of several persons liable for an act done by all | encoded | `Common Intention Facts`, `each is liable as if he alone did it within section 34`; in a charge through `Particulars`'s `common intention` and the s 34 rider |
| 35 | When such an act is criminal by reason of its being done with a criminal knowledge or intention | encoded | `Joint Knowledge Facts`, `liable for the act within section 35` |
| 36 | Effect caused partly by act and partly by omission | inert | Widens the act-leaf; illustration (murder by starving and beating) is body-a's to test. |
| 37 | Cooperation by doing one of several acts constituting an offence | encoded | `Cooperation Facts`, `commits that offence within section 37`; illustrations (a), (b), (c) tested |
| 38 | Several persons … may be guilty of different offences | inert | Each person's facts are read against each offence separately, which the encoding does by construction; illustration is body-a's (ss 300 Exception 1, 304). |
| 39 | (Repealed) | repealed | Repealed by Act 15 of 2019. |
| 40 | "Offence" | encoded | `Offence Facts`, `offence within section 40` over a Chapter and a section; the three lists as named constants |
| 41 | Offence with specified term of imprisonment | encoded | `punishable with imprisonment for … months or upwards within section 41`, over `Punishment`; refuses where no maximum is stated |
| 42 | "Obscene" | inert | One atom; Chapter 14's encoder carries it as a leaf. |
| 43 | "Illegal", "unlawful" and "legally bound to do" | encoded | `Unlawfulness Facts`, `illegal within section 43`, `legally bound to do within section 43` |
| 44 | "Injury" | encoded | `Injury Facts`, `injury within section 44` |
| 44A | "Bodily injury" | inert | Interpretive (a series counts as one). |
| 45 | "Life" | inert | Interpretive. |
| 46 | "Death" | inert | Interpretive. |
| 47 | "Animal" | inert | Carried in the @desc of the leaf that uses it (s 428, s 289, s 377B). |
| 48 | "Vessel" | inert | Carried in the @desc of the leaf that uses it (ss 280, 282, 437-439). |
| 49 | "Year" and "month" | inert | Gregorian — daydate's calendar is the Code's. |
| 50 | "Section" | inert | Interpretive. |
| 51 | "Oath" | inert | Carried in the @desc of the leaf that uses it (ss 178, 181, 191). |
| 52 | (Repealed) | repealed | Repealed by Act 15 of 2019. |

## Shared machinery (not sections of the Code)

| item | source | where |
| --- | --- | --- |
| `Punishment`, `How a punishment is prescribed`, `punishable with death or imprisonment for life`, `punishable with imprisonment`, `fixed by law or carries a minimum sentence` | Penal Code ss 53, 54 (Chapter 3 is the general-part group's), read by ss 41, 115, 116, 118, 120, 512 | `pc-general.l4` |
| `Charge`, `Particulars`, `Pronoun`, `frame the charge`, `frame the charge read with`, `the closing words of the charge read with`, and the helpers | Criminal Procedure Code 2010 ss 123-126 | `pc-general.l4`, `pc-domain.l4` |

## Check

`pc-domain.l4` 0 errors; `pc-general.l4` 0 errors; `pc-general-tests.l4` 0 errors, 115 `#ASSERT`s, 115 satisfied, 0 failed (measured with the prerelease in `BRIEF.md`, `JL4_LIBRARY_PATH` unset).
All three modules check with 0 warnings. They are ASCII except the `§` / `§§` markers.
