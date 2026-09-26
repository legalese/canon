# Penal Code 1871 — verification register, pass 8

**Run date:** 2026-09-16
**Scope:** the seven sections added on 16 Sep 2026 -- ss 1, 7, 8, 9, 49, 50 and 79A -- which
every register from 09 to 15 Sep listed as deliberately not encoded, on the view that each
states no factual test. With this pass every live section of the Act has a rule.
**Method:** every rule read back against the deposited source text in
`registers/source-bundle/PC1871.txt`, clause by clause, after it was written and
machine-checked. Same method as passes 1 to 7. Not an adversarial review.

**Result: no defect found in read-back; 1 policy change recorded; 1 drafting note recorded;
1 observation on the toolchain recorded.**

---

## 1. What this pass covers, and the limit of it

The same limit as passes 3 to 7: the rules were written and read back on one day, so a
misreading shared by the rule and the read-back is invisible. The pass is small -- seven
sections, eleven rules, 40 assertions -- and the sections are short, so the limit weighs less
here than in pass 7; but it is the same limit.

A second limit is particular to this pass. Five of the seven sections are drafting
conventions, and a drafting convention can be encoded in more than one way that is faithful
to its words. The read-back below checks that each rule says what its section says; it does
not, and cannot, check that the rule is the most useful shape the section could have taken.
`coverage-register.md` §3 rates the weight of each so that the count of 525 is not read as
525 sections of equal substance.

## 2. No defect found in read-back

Nothing was changed after the read-back. The clause-by-clause record is §6.

## 3. One drafting note

### N32 — section 79A(2) is decided, and sections 79(2) and 80(2) are not

ss 79(2), 79A(2) and 80(2) are burden rules of one shape: "to avoid doubt, where a person
alleges [a mistake] that may negate the fault element ..., the prosecution must prove the
fault element". Pass 1 left ss 79(2) and 80(2) undecided as rules of proof that add no
condition to the exception beside them, and that treatment stands. s 79A(2) is decided in
this pass. The reasons are two, and neither is a principle: s 79A(1) is a FALSE, and an
agent handed a FALSE about ignorance of the law needs the one place the Code says that
ignorance may still matter; and s 79A has no exception limb of its own to carry its
coverage, where ss 79 and 80 do. A later pass that wants the three consistent can decide
ss 79(2) and 80(2) the same way in two rules of two conjuncts each, or can withdraw s 79A(2)
without touching s 79A(1) or the screen. This register records the inconsistency so that it
is a choice and not an oversight.

## 4. One policy change, recorded

### P2 — the "no factual test" class is empty

From 09 to 15 Sep 2026 every register carried a class of live sections that were
"deliberately not encoded" because they state no factual test. The class was seven strong
and never changed. This pass empties it, and the reasoning is worth stating because the
earlier reasoning was not wrong so much as incomplete.

The earlier view was that a rule of construction, a short title or a definition of
"section" has no facts to decide over. That is true of the sections as addressed to a human
reader. It is not true of the sections as addressed to an agent that asks a question: "does
the actor's ignorance of the law help?" is a question s 79A answers; "how many months is a
term of 2 years?" is a question s 49 answers; "does 'he' in this section reach a woman?" is
a question ss 8 and 10 answer together. Once those three had rules, the remaining four were
cheap to give the shape the module's other defined terms already have, and there was no
longer a principled line between them and, say, s 48 "vessel" or s 51 "oath", which were
encoded as a facts record and a predicate from the start.

What the policy change does not do is claim weight for the nominal ones. s 1 is a string
constant and an equality test; s 50 is two facts conjoined. They are decided so that the
count is a count of rules, and `coverage-register.md` §3 says which of the seven carry
substance.

## 5. One observation on the toolchain, recorded

### T8 — the run cost is in the import graph, not in the fixtures or the assertions

Pass 7 §T7 located the cost of `l4 run agent-cases.l4` in the proposed-act bundle. This pass
measured it, and the location is different.

| module | imports (transitive) | fixtures | assertions | `l4 run` |
| --- | ---: | ---: | ---: | --- |
| `chapter-2-definitions.l4` | 2 | 12 | 33 | seconds |
| scratch: s 1 and s 79A, section level | 4 | 4 `Exception Facts` | 9 | 10 s |
| scratch: s 79A over the proposed act | 7 | 48, incl. 3 full `Proposed Act`s | 4 | 6 s |
| scratch: the same 48 fixtures, the 15 new assertions, `agent-cases.l4`'s 40 imports | 42 | 48 | 15 | killed at 33 min, ~3 GB, no output |
| scratch: `agent-cases.l4` with every directive but the 15 new ones commented out | 42 | ~250 | 15 | killed at 48 min, ~6 GB, no output |
| scratch: the 2 screen assertions, importing `agent-compliance.l4` alone | 42 | 48 | 2 | **2 of 2 satisfied, 20 min 9 s**, ~3.5 GB |

Same 48 fixtures, same three `Proposed Act`s, four of the same assertions: 6 seconds with
seven modules in the graph, no result in half an hour with forty-two -- and two assertions
alone on the forty-two-module graph took twenty minutes, so the per-directive cost on the
full graph is of the order of a minute or more, on top of the elaboration. `l4 check` on the
same files is unaffected -- the whole 45-module tree type-checks in under two minutes when
the machine is otherwise idle -- so whatever the evaluator does per imported module, the
type-checker does not. This is a property of the April 2026 CLI build and not of the
encoding; it is recorded here because it decides where assertions can be run. The practical
rule: an assertion that needs only a chapter module's rules belongs in that chapter module,
where it costs seconds; an assertion that needs the screen needs the whole graph, and at
45 modules the whole graph does not evaluate in a sitting. Splitting `agent-cases.l4` by
chapter would not help by itself -- each piece would still import `agent-compliance.l4` --
unless the screen were also split, which is a design change and not a fixture change.

One consequence for the record: pass 7 cited a `machine-evaluation.md` §14 for the run that
"was finally accepted", and no §14 was written. On the evidence above, this register does
not assume that the 535 assertions of `agent-cases.l4` as it stood on 15 Sep were ever
evaluated in one run against the 45-module tree. §14, written in this pass, says what was
run and what was not.

## 6. Clause-by-clause read-back

### Section 1

| clause | rule | check |
| --- | --- | --- |
| "This Act is the Penal Code 1871." | `the short title of this Act` MEANS "Penal Code 1871" | the string is the section's, character for character |
| (the same) | `the citation names this Act by its short title` IF citation EQUALS the short title | exact comparison; a chapter number or edition year is not part of the short title and does not match, which the `@desc` says |

### Section 7

| clause | rule | check |
| --- | --- | --- |
| "Every expression which is explained in any part of this Code" | `the expression is explained in any part of this Code` (new field on `Definition Reach Facts`) | any part, not only ss 22A to 26H -- that is why the s 6A field `the term is explained in sections 22A to 26H` was not reused |
| "is used in every part of this Code in conformity with the explanation" | AND `the offence is in this Code` | the s 6A record's name for the use being a use in this Code; reused rather than duplicated, and the module comment says so |
| (ss 6A and 7 together) | `the Code explanation governs the expression as used` IF s 7 rule OR s 6A rule | a use in the Code passes by s 7; a use in another written law passes by s 6A alone, with its ss 24 and 25 carve-outs and the express-definition displacement intact. The fixtures `public servant as used in section 161` (s 21 term, in the Code: TRUE) and `public servant as used in another written law` (s 21 term, outside: FALSE, since s 6A carries ss 22A to 26H only) are the pair that shows the two rules are not one |

### Sections 8 and 10

| clause | rule | check |
| --- | --- | --- |
| s 8 "The pronoun 'he' and its derivatives are used of any person, whether male or female" | `the word reaches a person of that sex` IF w EQUALS the pronoun he or a derivative | no condition on `Sex`: the disjunct is TRUE for both values, which is "any person, whether male or female" |
| s 10 "'man' denotes a male human being of any age" | OR (w EQUALS the word man AND s EQUALS man) | one sex; age is absent from the rule, as "of any age" requires |
| s 10 "'woman' denotes a female human being of any age" | OR (w EQUALS the word woman AND s EQUALS woman) | the same |
| (the pair) | assertions: he/woman TRUE, he/man TRUE, man/man TRUE, man/woman FALSE, woman/woman TRUE, woman/man FALSE | all six cells of the 3 × 2 table are asserted |

### Section 9

| clause | rule | check |
| --- | --- | --- |
| "words importing the singular number include the plural number" | `the word reaches the plural number` IF imports plural OR (imports singular AND NOT contrary) | a word that already imports the plural reaches it without the section; one that imports the singular reaches it by the section, subject to the carve-out |
| "words importing the plural number include the singular number" | `the word reaches the singular number` IF imports singular OR (imports plural AND NOT contrary) | the mirror |
| "Unless the contrary appears from the context" | `the contrary appears from the context`, negated, on the extending disjunct of each rule only | the carve-out limits the extension, not the word's own number: a plural word whose context is contrary still reaches the plural. The fixture `five or more persons as used in section 141` is that case -- plural TRUE, singular FALSE |

### Section 49

| clause | rule | check |
| --- | --- | --- |
| "Wherever the word 'year' or 'month' is used, ... the year or the month is to be reckoned according to the Gregorian calendar" | `the period in calendar months of` years months IS years TIMES 12 PLUS months | the Gregorian year is twelve calendar months; the rule states a period in the smaller unit. It does not count days and the module comment says why: no date is carried in this subject. The assertions pair the rule with s 40(3)'s threshold -- 2 years is 24 months and is "6 months or upwards"; 5 months is not |

### Section 50

| clause | rule | check |
| --- | --- | --- |
| "one of those portions of a Chapter of this Code" | `is a portion of a Chapter of this Code` | conjunct |
| "which are distinguished by prefixed numeral figures" | AND `is distinguished by a prefixed numeral figure` | conjunct. The fixtures: s 378 (both TRUE), an Explanation (portion of a Chapter, no numeral: FALSE), the Schedule (numbered, not a portion of a Chapter: FALSE) |

### Section 79A

| clause | rule | check |
| --- | --- | --- |
| s 79A(1) "A person's mistake of law or ignorance of the law is not a defence to a charge for an offence" | `a mistake of law or ignorance of the law is a defence to the charge` is FALSE on `the person alleges a mistake of law or ignorance of the law` alone | the default is the negative, as the section's title and its first clause both say; the `blank exception facts` and `ignorance of the law` fixtures are asserted FALSE |
| "unless it is otherwise provided by written law" | AND `written law provides that the mistake of law or ignorance of the law is a defence to the charge` | the one route to TRUE; caller-asserted, since no other written law is in the source bundle -- the treatment s 5 and s 79(1) already give the same phrase |
| s 79A(2) "where a person alleges a mistake of law or ignorance of the law that may negate the fault element of the offence that the person is charged with" | `the prosecution must prove the fault element notwithstanding the alleged mistake of law` IF alleges AND `the alleged mistake ... may negate the fault element of the offence` | two conjuncts, both the section's; whether a given mistake can negate a given fault element is a question about the offence charged and is caller-asserted |
| "the prosecution must prove the fault element in order to establish liability under the offence" | the predicate's name | a rule of proof made callable, as s 5 was; it decides nothing about liability itself |
| (relation to Chapter 4) | neither rule is a disjunct of `a general exception applies to`; the screen field `a mistake of law is a defence s 79A` is computed from the first | asserted: `taking a knife under a mistake of law that written law excuses` has the screen field TRUE, `a general exception applies` FALSE, and `the proposed act constitutes theft` TRUE. s 79A(1)'s exception is another written law's defence and s 6 does not take the act outside the offence for it -- the same position s 5 takes |

## 7. Machine check

45 modules, **0 type errors**. The 33 assertions of `chapter-2-definitions.l4` (8 existing,
25 new) all satisfied in a standalone run; the 15 new assertions of `agent-cases.l4` all
satisfied in three scratch modules (9 + 4 + 2); 108 of 108 evaluated in all. The full run of
`agent-cases.l4` was not attempted, and `report/machine-evaluation.md` §14, written after
this register, records why and what that leaves unverified.
