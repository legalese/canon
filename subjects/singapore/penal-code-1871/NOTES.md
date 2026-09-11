# Penal Code 1871 -- encoding notes

This subject's idiosyncrasies, in prose, for humans. No script reads this file.

---

## 1. What this subject is

An L4 encoding of **Penal Code 1871** (2020 Revised Edition, SSO current version as at 09 Sep 2026) built so an AI agent can screen a proposed act against the constitutive tests of selected offences and ask whether s 6 takes the act outside "offence" -- by a Chapter 4 general exception, or by the Chapter 4A right of private defence.

The agent-facing entry points are in `agent-compliance.l4`:

| question | answered by |
| --- | --- |
| Which encoded offences are indicated on these facts? | `the offence screen of` |
| Is any encoded offence indicated? | `any screened offence is indicated` |
| Is the act justified, by a Chapter 4 exception or a Chapter 4A private defence? | `the act is taken outside offence by Chapter 4 or Chapter 4A` |
| Was it done in the exercise of the right of private defence? | `a private defence justification applies` |

Modules, in dependency order:

```
types.l4                      the nouns: records and enums, no rules
chapter-1-preliminary.l4      ss 2, 3, 4, 4A, 4B location facts, and the s 5 saving
chapter-2-definitions.l4      ss 6A-12, 17, 19-22A, 27-31A, 40-51 (the defined terms)
chapter-2-explanations.l4     ss 23-26, 26A-26H (dishonestly, fraudulently, rashly, ...)
chapter-2-participation.l4    ss 32-38 (common intention, cooperation, attribution)
chapter-3-punishments.l4      ss 53, 54, 72, 73, 74, 74A-74E (the punishment vocabulary)
chapter-4-exceptions.l4       ss 6, 76-95 (the whole of Chapter 4)
chapter-4a-private-defence.l4 ss 96-106A (the whole of Chapter 4A), and s 6 combined
chapter-5-abetment.l4         ss 107, 108, 108A, 108B, 111, 113, 114
chapter-5a-conspiracy.l4      ss 120A, 120B
chapter-17-cheating.l4        ss 415, 416, 416B, 418, 420, 420A
chapter-17-property.l4        ss 378, 403, 405
chapter-17-fraud.l4           ss 416A, 424A, 424B
chapter-18-forgery.l4         ss 463, 464
chapter-21-22-speech.l4       ss 499, 503, 504, 505
chapter-23-attempts.l4        s 511
agent-compliance.l4           the screen and the Schedule-to-4B classifier
agent-cases.l4                scenario fixtures, machine-asserted
registers/source-bundle/      PC1871.txt / .pdf as retrieved 09 Sep 2026
registers/verification-register.md  the fidelity pass over the pre-existing rules
registers/coverage-register.md      which sections are modelled, and which are not
registers/verification-register-pass-2.md  the fidelity pass over the rules added 09 Sep
registers/verification-register-pass-3.md  the fidelity pass over the rules added 11 Sep
registers/missing-sections.md       every live section with no rule, named one by one
report/machine-evaluation.md  how the encoding was machine-checked, and against what
```

The three Chapter 2 and Chapter 3 modules are **freestanding**: they define terms,
attribution rules and punishment records that the Code's own offence sections rely on, but
no offence module encoded here imports them yet, and `agent-compliance.l4` does not call
them. They are directly callable by an agent through their `@export` entry points. Wiring
them into the offence wrappers is the next piece of work, not something this draft claims
to have done.

## 2. What is deliberately not encoded

The Code lists 600 sections, of which 75 are repealed. This draft encodes **126 of the 525
live sections -- about 24%**. `registers/coverage-register.md` records which ones, chapter by
chapter and section by section; what follows is the policy behind those numbers.

The general parts are close to complete (Chapter 1: 6 of 7; Chapter 2: 49 of 54; Chapter 3:
10 of 10; Chapter 4: 20 of 21; **Chapter 4A: 12 of 12**; Chapter 5A: 2 of 2 -- and every gap
there is a section with no factual test to decide). The offence chapters remain a deliberate
thin slice: the provisions an AI agent is most likely to walk into when checking its own
output or a user's requested act.

- **Not encoded:** Chapters 6 to 16 (State, armed forces, unlawful assembly, public servants, false evidence, public health, religion, offences affecting the human body including hurt, sexual offences, wrongful confinement), most of Chapter 17 (extortion, robbery, stolen property, criminal trespass), currency offences, and the ten exceptions to s 499 as individual tests.
- **s 499 exceptions** are a single caller-asserted flag `a section 499 exception applies`.
- **Punishment** is not computed for any particular offence. `chapter-3-punishments.l4` encodes the Chapter 3 vocabulary -- what a `Punishment` is (s 53, s 54), how to pick the lower of two where it is doubtful which offence was committed (s 72), and the six enhanced-penalty sections that double a maximum (ss 73 to 74E). It does **not** attach a punishment to any offence section: no `the proposed act constitutes ...` wrapper returns one, and the doubling rules take the base maximum as a caller-supplied argument. The encoding still answers whether the constitutive test is met, not what sentence a court would pass.
- **ss 32 to 38** are encoded as standalone attribution tests. They are not applied automatically to the offence wrappers: an agent that wants s 34 common-intention liability must call `the person is liable under section 34 as if he did the act alone` itself.
- **The defined terms** in `chapter-2-definitions.l4` (ss 11, 19, 21, 22, 29, 30, 40, 43, 44, 51 and the rest) are likewise callable but not spliced into the offence tests, which continue to take the underlying facts as booleans asserted by the caller.
- **Chapter 5, ss 109, 110, 112 and 115 to 120** are not encoded. They are punishment and concealment provisions, consistent with this subject not computing sentence. The three substantive liability rules in that range -- ss 111, 113 and 114 -- are now encoded.
- **Computer Misuse Act 1993** is a different Act and is not in the source bundle.

## 3. Interpretive choices

- **s 415** "whether or not such deception was the sole or main inducement" is encoded by not treating that flag as a precondition.
- **s 415 Explanation 4 and 5** (a company can be deceived / induced even if no individual officer is personally deceived) are encoded as facts the caller may assert; they do not change the boolean test, which still requires `deceives a person` (s 11: "person" includes a company).
- **s 4B(1)(a)** is encoded as either relevant act in Singapore and another outside, or the reverse.
- **s 416A(3)** defence to the supply limb is encoded as: the supply limb fires unless both (purpose is not supply for an offence) and (no knowledge it will be so used).
- **s 424A / 424B** split on `is directly connected with a written or oral contract for the supply of goods or services`. Materiality is ignored (s 424A(2), s 424B(2)).
- **s 405** "intentionally suffers any other person to do so" is treated as sufficient without a separate dishonesty check on the sufferer limb, matching the disjunctive last clause of s 405.
- **s 6** is applied in every `the proposed act constitutes ...` wrapper, and since 11 Sep it is applied in full: the wrappers call `the act is taken outside offence by Chapter 4 or Chapter 4A`, so a Chapter 4A private-defence justification takes the act outside the offence exactly as a Chapter 4 exception does. `a general exception applies` is unchanged and still means Chapter 4 alone; the offence screen reports the two separately.
- **s 6A** carve-out is encoded as written: the ss 22A-26H explanations carry across to other written laws, but "dishonestly" (s 24) and "fraudulently" (s 25) do not, and any express definition in the other law displaces the Code explanation.
- **s 22 "property"** has no subsections; the four definitions are encoded as one record. "Movable property" is derived rather than asserted -- it is anything that is property under s 22 and is not immovable -- so money, things in action, intangibles and virtual currency all come out movable, which is what the definition of "movable property" ("property of every description, except immovable property") requires.
- **s 38** is permissive -- it removes an obstacle to charging participants differently rather than imposing a condition -- so it is encoded as the fact that the differing-offences outcome is open, not as a test that must be passed.
- **s 72** orders punishments as death > imprisonment for life > the longer maximum term. Fine, caning and forfeiture do not enter the ordering; where two punishments are equal on all three ranked limbs the first is not treated as the lower.
- **ss 73 to 74E** are encoded on the doubling trigger, the excluded-offence carve-outs and the statutory defence of each section. `the punishment after enhancement of` doubles the maximum imprisonment and the maximum fine **once**, however many of ss 73 to 74D are engaged, which is s 74E(1)(a). s 74E(1)(b) -- which of the engaged sections the court picks -- is not encoded, and does not matter while every section doubles by the same factor.
- **s 74E(2)** is satisfied structurally rather than by a rule. A prescribed minimum passes through `the punishment after enhancement of` unchanged, so no minimum sentence of imprisonment or caning is ever enhanced (s 74E(2)(a)); and the `Punishment` record carries no maximum number of strokes at all, only a minimum, so no maximum can be enhanced (s 74E(2)(b)).
- **s 81's Explanation** ("it is a question of fact whether the harm to be prevented was of such a nature and so imminent as to justify or excuse the risk") is encoded as a conjunct, not as commentary, on the view that without it the section does not excuse.
- **s 27** is given a first limb the section does not state -- `the person has the property physically`. s 27 is a deeming rule about possession through a spouse, clerk or servant; the encoding carries the ordinary case it builds on so the predicate is usable on its own.
- **s 84** remains encoded on the opening fact plus the s 84(1)(a)-(c) capacity limbs and the s 84(2) both-limbs requirement, as corrected in `registers/verification-register.md` (V1).

### Added 11 Sep 2026

- **Chapter 4A is encoded as two rights with a shared frame.** ss 97, 101, 104 give each right a subject matter and a window; ss 98 and 106A restrict both; ss 102, 103, 105 and 106 cap the harm. The caps are encoded as one test on the harm actually caused rather than as further elements of the right, because that is what ss 103 and 106 say: the right *does extend* to any harm other than death, and extends to death only on a s 102 or s 105 description.
- **s 99 is not a limb of s 96.** It supplies the "is an offence" element that ss 97, 101 and 104 each require, for the case where the act is no offence because of the doer's youth, immaturity, unsoundness of mind, intoxication or misconception. It is therefore encoded as an alternative inside those tests.
- **s 100 enlarges rather than restricts**, so it is a permission needed only where harm to an innocent person is actually risked. The body-right extent test reads: either no innocent person is harmed, or s 100 covers it.
- **s 106A is encoded on its double negative as written.** The bar bites only where the act does *not* cause the defender to reasonably believe that death or grievous hurt would result, so the first conjunct of each limb is a negation. Explanation 1 is a conjunct on the s 106A(1) limb; Explanation 2's two routes are disjoined on the s 106A(2) limb.
- **s 104(2) is encoded as three terminating events.** The right against theft continues *till* retreat, or assistance obtained, or recovery -- so each is a negated conjunct, not a requirement.
- **s 105(1) does not restate the s 104(1) belief.** The two are the same fact, and it is already required for the right to have started at all.
- **House-breaking is treated as within the s 104(1) list.** s 104(1) starts the property right against theft, robbery, mischief or criminal trespass; s 104(5) continues it against house-breaking, which s 104(1) does not name. House-breaking is an aggravated criminal trespass (ss 442 to 449), so it falls within the s 104(1) list — but none of those sections is encoded, so the containment is stated in the module rather than computed, and a caller asserting the house-breaking limb must assert the s 104(1) belief too.
- **The 6 ways in s 105(2) merge entry and leaving.** s 105(1)(b) distinguishes the wrongdoer who *enters* in one of the 6 ways from the one who, having been in the house, *leaves* in one of them. Each of the six facts is phrased "enters or leaves", which is what s 105(2) itself does in every one of its paragraphs.
- **s 3** is read as reaching acts wholly outside Singapore, matching the encoding of s 4. An act partly in and partly outside Singapore is the subject of s 4B, which has its own rule, and is not routed through s 3. Whether the person is liable by law to be tried here is a caller-asserted fact: no other written law is in the source bundle.
- **s 4A** takes the Chapter 6 / Chapter 6B classification as a caller-asserted fact, neither chapter being encoded. It is still decided, because without it the territorial screen reports no reach over a citizen's foreign conduct that the Code plainly reaches.
- **s 5 is decided, where s 79A is not.** Both are closure provisions that add no limb to any offence test. s 5 is given a rule anyway because it carries a consequence an agent needs: a FALSE from the screen is a statement about this Code alone, and where the conduct is or may be punishable under another written law, s 5 preserves that law untouched. `another written law is unaffected and may still apply` is that caution, made callable, and the screen reports it.
- **s 111 conjoins s 107 but not s 108.** The section fixes the abettor with the act actually done, not with the one he had in mind, so it requires abetment conduct but not that the thing abetted pass the s 108 capable-person test.
- **s 114 disjoins the s 108 abettor and the s 111 abettor**, because its opening words -- "who, if absent, would be liable to be punished as an abettor" -- reach both.
- **s 112 is not encoded.** It is a rule about cumulative punishment, and this subject does not compute sentence.

## 4. Status

`draft`. No claim of fidelity. No HG1/HG2 grant.

Machine-checked: 18 modules, 0 type errors, 88 of 88 assertions satisfied
(`report/machine-evaluation.md`). §7.2 of that report records two blind spots in the
available engine which a future run should read it subject to.

Every encoded rule has now been read back against the deposited source text, in three passes:
`registers/verification-register.md` for the rules that existed before 09 Sep 2026 (twelve
defects, all fixed), `registers/verification-register-pass-2.md` for the rules added that day
(four defects, all fixed), and `registers/verification-register-pass-3.md` for the eighteen
sections added on 11 Sep (no defect found; three drafting traps and two caller traps
recorded). No pass is an adversarial review, none can reach the sections
`registers/coverage-register.md` records as absent, and pass 3 read back rules written the
same day, which is a weaker check than passes 1 and 2 -- it says so on its own first page.

