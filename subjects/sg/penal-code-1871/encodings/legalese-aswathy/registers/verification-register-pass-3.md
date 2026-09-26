# Penal Code 1871 — verification register, pass 3

**Run date:** 2026-09-11
**Scope:** the eighteen sections added on 11 Sep 2026 — Chapter 4A in full (ss 96 to 106A),
Chapter 5 ss 111, 113 and 114, and Chapter 1 ss 3, 4A and 5 — together with the rewiring of
the nineteen offence wrappers onto the combined s 6 predicate.
**Method:** every rule read back against the deposited source text in
`registers/source-bundle/PC1871.txt`, clause by clause, after it was written and
machine-checked. Same method as passes 1 and 2. Not an adversarial review.

**Result: no defect found in read-back. 3 traps in the Act's drafting were identified at
authoring time and are recorded below; 2 caller traps are documented rather than fixed.**

---

## 1. What this pass covers, and the limit of it

Passes 1 and 2 read back rules that already existed, written on an earlier day. This pass
reads back rules written the same day, which is a **weaker check**: the same reading that
produced the rule produced the verification of it, so a misreading shared by both is
invisible here. That limit is the most important thing on this page, and no count below
should be read as evidence against it.

Two things partly compensate. The Chapter 4A sections carry Illustrations, and every
Illustration that states an outcome was turned into an assertion in `agent-cases.l4` rather
than into prose here, so the engine checks them and a later reader can re-run them. And the
three gaps this pass closes were described in `coverage-register.md` §6 *before* any rule was
written, so the target was fixed in advance rather than fitted to the result.

`NOTES.md` §3 states every interpretive choice, so a later reader who disagrees with one can
find it without re-deriving it from the rules.

### Why this register records no defects

Passes 1 and 2 each found defects, and it would be easy to present this pass as having found
some too. It did not. The read-back of all eighteen sections against the source text found no
rule whose limbs departed from its provision. Reporting that plainly is worth more than a
manufactured symmetry with the earlier passes — and it is a much weaker claim than it looks,
for the reason in the paragraph above. Three provisions did have drafting traps sharp enough
to be worth recording, and they are below; all three were dealt with when the rule was first
written, not discovered afterwards.

## 2. Three traps in the drafting, and how each was handled

These are the places in the eighteen sections where a straightforward encoding would have
been wrong. Each is recorded in the module itself as well as here.

### N1 — s 105(1) opens with a fact the right already required

s 105(1) reads "where the defender reasonably believes that there was a danger to property
(either his own or that of any other person) arising from any of the following descriptions".
That is word for word the s 104(1) belief. Carried as a second fact, it would have given a
caller two flags to set for one proposition, and the s 105 rule would have returned FALSE
whenever only the s 104(1) flag was set — silently capping the property right below death on
facts where the Code allows it.

The rule therefore relies on the s 104(1) fact and does not restate it. The right cannot
reach s 105 without having started under s 104(1) anyway.

### N2 — s 104's continuance limbs are not independently disjoinable

s 104(2) to (5) give four continuance rules. The theft limb is a conjunction of negations —
the right "continues till" retreat, or assistance obtained, or recovery — so on facts about a
*robbery* none of the three theft-terminating events is set and a free-standing theft limb
would return TRUE. Disjoining four such limbs would make the property right continue
indefinitely against every offence.

Each limb is therefore keyed to its offence kind, so exactly one is live on any given facts.
The two theft assertions in `agent-cases.l4`, before and after the retreat, are the regression
test for this.

### N3 — s 114 is not confined to the s 108 abettor

s 114 opens "Whenever any person who, if absent, would be liable to be punished as an
abettor". The natural reading on a first pass is the s 108 abettor. But s 111 makes an abettor
liable for a *different act* from the one abetted, and such a person is equally one who, if
absent, would be liable to be punished as an abettor. The words are not confined to s 108.

The rule therefore disjoins the s 108 abettor and the s 111 abettor.

## 3. Two caller traps, documented rather than fixed

These are not defects in the rules. They are places where the Act's own drafting makes it
easy for a caller to assert an incomplete set of facts, and where the encoding cannot tell
that they have. Both are recorded as `CALLER NOTE` blocks in the module, next to the rule
they affect.

### T1 — s 100's opening fact and s 102(a) are near neighbours

s 100 speaks of "an assault which causes the defender to reasonably believe that death would
be caused to him or to any other person". s 102(a) speaks of "an assault where the defender
reasonably believes that death will otherwise be the consequence of such assault". On most
facts where one is true the other is too, but they are worded differently and do different
work: s 100 licenses the risk to a bystander, s 102(a) lifts the ceiling on harm to the
assailant.

They are kept as two facts, because merging them would put a proposition in the encoding that
neither section states. A caller who sets only one gets a narrower justification than the
Code allows. That direction is safe — it can withhold a justification, never invent one — and
it is the direction this encoding errs in throughout.

### T2 — house-breaking is in s 104(5) but not in the s 104(1) list

s 104(1) starts the property right against theft, robbery, mischief or criminal trespass.
s 104(5) continues it against house-breaking, which s 104(1) does not name. House-breaking is
an aggravated form of criminal trespass (ss 442 to 449), so it is within the s 104(1) list —
but none of ss 442 to 449 is encoded in this subject, so the containment is **stated in the
module, not computed**. A caller asserting the house-breaking limb must assert the s 104(1)
belief as well.

This is the one place in Chapter 4A where the encoding leans on an unencoded part of the
Code. It is recorded rather than fixed because fixing it means encoding the Chapter 17
trespass sections, which is a scope decision and not a defect.

## 4. Clause-by-clause read-back

Every row was checked against the source text. "As written" means the rule's limbs correspond
one to one with the provision's, in the same polarity.

### Chapter 4A

| s | provision | reading |
| --- | --- | --- |
| 96 | nothing done in private defence is an offence | The aggregate of the two rights. As written. |
| 97(a) | body of self or any other person, against an offence affecting the human body | As written, with s 99 as an alternative to the offence element. |
| 97(b) | property movable or immovable, of self or any other, against theft, robbery, mischief, criminal trespass or an attempt | As written, with s 99 as an alternative. |
| 98(1) | no more harm than reasonably necessary | As written, as a shut-out. |
| 98(2) | no right where reasonable opportunity to have recourse to a public authority | As written, as a shut-out. Illustration (b)'s timing point is carried by the fact being about the circumstances, not the outset. |
| 99 | right survives the doer's youth, immaturity, unsoundness, intoxication or misconception | Encoded as an alternative offence element inside ss 97, 101 and 104, not as a limb of s 96. |
| 100 | right extends to running the risk of harm to an innocent person | Both conjuncts of the section present. Encoded as an enlargement, needed only where an innocent person is in fact harmed. See T1. |
| 101(1) | right starts on reasonable belief of danger to the body from an offence against the human body, or an attempt or threat | As written, including "though the offence may not have been committed" — carried by the fact being about belief, not commission. |
| 101(2) | continues as long as that belief continues | As written, as a conjunct. |
| 102(a)–(f) | six descriptions lifting the ceiling to death | All six present, disjoined, each as written. |
| 103 | otherwise no death, but any harm short of death | Encoded with s 102 as one ceiling test on the harm actually caused. |
| 104(1) | right starts on reasonable belief of danger to property from theft, robbery, mischief, criminal trespass or an attempt | As written. See T2. |
| 104(2) | against theft, continues **till** retreat, assistance obtained, or recovery | Three terminating events, each a negated conjunct. Trap N2 is here. |
| 104(3) | against robbery, while the offender causes or attempts death, hurt or wrongful restraint, or the fear continues | As written. |
| 104(4) | against criminal trespass or mischief, while the offender continues in it | As written. |
| 104(5) | against house-breaking, while it continues | As written. See T2. |
| 105(1)(a)–(d) | four descriptions lifting the property ceiling to death | All four present. (b) conjoins the 7 p.m. to 7 a.m. window and the 6 ways. Trap N1 is here. |
| 105(2)(a)–(f) | the 6 ways of entry or leaving | All six present, disjoined. Each is phrased "enters or leaves", which is what s 105(2) does in every paragraph; s 105(1)(b)(i) and (ii) are thereby merged. |
| 106 | otherwise no death, but any harm short of death | Encoded with s 105 as one ceiling test. |
| 106A(1) | no right against a public servant's act raising no reasonable belief of death or grievous hurt | The section's double negative is preserved: the first conjunct is a negation. Explanation 1 is a conjunct. |
| 106A(2) | the same for an act by a public servant's direction | As written. Explanation 2's two routes are disjoined. |

### Chapter 5

| s | provision | reading |
| --- | --- | --- |
| 111 | abettor liable for a different act done | s 107 conduct conjoined; both proviso limbs conjoined. Not conjoined with s 108: the section fixes the abettor with the act done, not the one intended. Illustrations (a) and (b) are assertions. |
| 113 | abettor liable for a different effect caused | s 107 conduct conjoined; the knowledge proviso conjoined. The Illustration is an assertion, with its negation as the control. |
| 114 | abettor present is deemed to have committed | Disjoins the s 108 abettor and the s 111 abettor. Trap N3 is here. |
| 112 | cumulative punishment | Not encoded; recorded in the module. This subject does not compute sentence. |

### Chapter 1

| s | provision | reading |
| --- | --- | --- |
| 3 | person triable here for an act beyond Singapore is dealt with as if it were within | Read as wholly outside Singapore, matching s 4. The triability precondition is caller-asserted: no other written law is in the source bundle. |
| 4A | citizen or PR committing a Chapter 6 or 6B offence abroad is deemed to commit it here | As written. The Chapter 6 / 6B classification is caller-asserted, neither Chapter being encoded. Not confined to public servants, unlike s 4. |
| 5 | this Code does not affect any other law in force | Decided, though it adds no limb to any offence test. `NOTES.md` §3 gives the reason. |

## 5. The rewiring

Nineteen `the proposed act constitutes ...` wrappers across eight modules were changed from
`a general exception applies` to `the act is taken outside offence by Chapter 4 or Chapter
4A`. This is a behavioural change to rules that passes 1 and 2 had already verified, so it
was checked separately:

- `a general exception applies` is **unchanged** in name, meaning and `@ref`. It still means
  Chapter 4 alone, and `chapter-4-exceptions.l4` was not modified.
- The new predicate is a disjunction of that and the Chapter 4A aggregate, so it can only
  take *more* acts outside offence, never fewer. No act that was previously not an offence
  becomes one.
- The offence screen reports the two routes in separate fields, so a caller can tell which
  fired.
- All 55 assertions that existed before this pass still hold, unchanged.

The end-to-end check is `disarming an assailant` in `agent-cases.l4`: a taking that satisfies
every element of s 378, asserted against the private-defence facts of a person fending off an
assault. `constitutes theft` is TRUE on the taking facts alone; `the proposed act constitutes
theft` is FALSE; `a general exception applies` is FALSE; and the screen's
`a private defence justification applies s 96` field is TRUE. Before this pass the same facts
returned theft.

## 6. Machine check

18 modules, **0 type errors, 88 of 88 assertions satisfied** — 55 pre-existing and 33 added
by this pass. `report/machine-evaluation.md` §7 records how the run was made and two blind
spots in the available engine that the run does not cover.
