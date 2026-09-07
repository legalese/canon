# Ofek Hadash — encoding notes

**Status: draft, not reviewed.** No Israeli labour lawyer, and no payroll officer at the
Ministry of Education, has read this against the agreements. Every figure in it was checked
against the source documents mechanically and several were checked by hand, but that is a
different thing from review, and §8 says exactly what would have to happen for that word to
be used. Law stated as at **7 September 2026**, from the corpus commit recorded in
`registers/source-bundle.json`.

---

## 1. What this is

Israeli teachers are paid under **Ofek Hadash** (אופק חדש, "New Horizon"), a reform agreed
between the State of Israel and the Teachers' Union (הסתדרות המורים) in 2007–2008 and
amended ever since. It is not legislation. It is a **collective agreement**, layered with
later collective agreements, decisions of a joint follow-up committee, and ministry
circulars — and, since 2025, cut across by a temporary provision in the State budget.

A teacher's monthly pay is the sum of a cell in a 36×9 table, a levelling supplement that
runs the opposite way to the table, a doctorate uplift, up to two percentage supplements for
the jobs they do, a flat supplement for a school role, and a subtraction the war made
necessary. Five of those six behave differently on a part-time post, and the differences are
stated in five different instruments signed eighteen years apart.

This encoding computes that sum, and — more to the point — makes the interactions between
those instruments **checkable** rather than asserted.

## 2. The source

Everything is read from **[מאגר אופק חדש](https://morimovilimcatala.github.io/ofek-hadash-corpus/)**,
a published corpus of 282 documents: 37 collective agreements, 205 ministry circulars, 32
salary tables, the Teachers' Service Regulations, and one Act. Every page is one instrument's
own wording, encoded as Akoma Ntoso 3.0 (OASIS LegalDocML).

The corpus states its own caveats and this encoding adopts them without softening: the
`/akn/il/…` identifiers are a repository convention and not citable outside it; a
transcription made by a single reader is marked as such and is not the same as a verified
one; where a source scan is missing pages, the gap is recorded in place rather than closed.
Nothing in the corpus is OCR, because on these scans OCR returns text too corrupt to stand as
the wording of an instrument.

**All 282 documents were read**, and `registers/document-register.json` carries one row each:
title in Hebrew and English, date, what the document *does*, whether it is `operative`
(it fixes a number, rate, formula or eligibility condition that enters the computation of
pay), `procedural` (it governs how pay is administered without changing what is owed), or
`background`; the pay components it touches; what it amends; the figures it fixes; and
whatever the document itself flags about the state of its own text. 257 of the 282 are
operative. Digests are over the corpus HTML this encoding actually read.

That register is **not** the encoding. It is the map that decided what the encoding should
cover, and it is deposited because the reasoning behind a scope decision is worth more than
the decision. Its `kind` field disagrees with the corpus's own Akoma Ntoso document type in
nine places — all circulars that consist mostly of a salary table — and each of those rows
carries a `kind_note` saying so rather than being quietly overwritten.

## 3. What is encoded

Eight modules, 254 assertions, all passing.

| module | what it carries |
| --- | --- |
| `ofek-domain.l4` | the ontology: qualifications, tables, stages, roles, and the teacher record every other module reads |
| `ofek-salary-table.l4` | both combined-salary tables in full, the staircase frontier, and the step percentages that generate them |
| `ofek-placement.l4` | §§ 36–38 — placement on entry, what counts as seniority, and the whole promotion machinery including the rank quotas |
| `ofek-worktime.l4` | §§ 14–33 — the 36-hour week in its ten shapes, the age reductions, the post limits, and § 31's hourly value |
| `ofek-supplements.l4` | § 39 role supplements, the 2022 shekel floors, Tosefet Ofek 2022, and the school-role supplement |
| `ofek-fiscal-2025.l4` | the 2025–2026 wage reduction, as the approved agreement of 29 June 2026 enacts it |
| `ofek-pay.l4` | the assembly: a month's pay, and the hourly value for a given purpose |
| `ofek-cases.l4` | three teachers computed end to end, with every figure traced to its article |

`ofek-catala.l4` is a **generated** ninth module — see §7.

Run everything with `./check.sh`. It pins `JL4_LIBRARY_PATH` to the same worktree the binary
was built from, which matters: an `l4` binary pointed at a newer prelude fails in ways that
look like errors in the encoding.

## 4. What is NOT encoded

Read this section before relying on any answer.

- **Seniority is an input.** § 37 defines it by reference to the Teachers' Service
  Regulations, which are in the corpus as a single 770,000-character document and are not
  encoded. What § 37 says on the face of the agreement *is* encoded. This is the largest gap
  (fork F4).
- **Rank is an input.** § 38's promotion machinery is encoded and can be asked whether a
  given application succeeds, but rank itself depends on ministry criteria, on evaluations,
  and on a quota measured against the national establishment (F5).
- **Teachers who are not academic** have their own tables under §§ 51–53. Those tables are
  not in the corpus, so such a teacher is placed in the BA table, which is wrong for pay
  purposes and is flagged rather than hidden (F6).
- **The conversion chapters** (§§ 43–50, 54–61), which turn an existing teacher's pre-reform
  salary into a place in the new table, are not encoded (F7).
- **Only primary and junior-high classroom teachers.** Not special education, not integration
  or paramedical roles, not principals, deputies, counsellors or kindergarten teachers — and
  not Oz LeTmura, the separate upper-secondary reform the corpus also carries (F8).
- **The circulars are registered, not encoded.** 205 of them set year-by-year amounts —
  clothing allowance, recreation pay, the jubilee grant, childcare subsidy — which are
  outside the pay computation this encoding performs. They are in the document register with
  their figures.

## 5. Two things worth knowing before reading the code

### 5.1 The table is generated by the percentages printed in its own margins

The combined-salary table is a 36×9 grid, but it prints only **224** distinct numbers: beyond
a staircase frontier the shekel printing merges cells, repeating one value across the ranks
to its right.

Taking the base cell and applying only the two rates the table prints in its own margins —
2% down the seniority rows to row 7, 1% from row 8, and 7.5% across the ranks — reproduces
**every one of those 224 cells**, in both the BA and the MA table.

On the corrected agorot printing the worst deviation across the whole grid is **0.005**,
which is exactly the rounding of a figure printed to two decimals. On the shekel printing the
same claim needs a tolerance two hundred times larger, and that is itself the evidence that
the shekel figures are roundings of the agorot ones rather than a separately computed table.
The 1.1.2015 tables, which also print agorot, agree to 0.01.

So the encoding carries **both** — the 648 numbers and the two rates — and asserts that the
second generates the first. That turns 224 printed figures into a base and two percentages,
and it would fail loudly if a figure had been mistranscribed or if a published table had
drifted from the rule it states. It is recorded as finding F11.

### 5.2 Half a post is not half the pay

The single most consequential thing here, and it falls out of reading three articles
together rather than from any one of them:

| component | pro-rated for a part post? | authority |
| --- | --- | --- |
| combined salary | yes | 2008 § 33 |
| Tosefet Ofek 2022 | yes | 2022 § 5.3, expressly |
| doctorate supplement | yes (it is a percentage of the above) | 2008 § 36(d)(2) |
| role supplements | **no** — the full-post figure, if the post is at least ⅓ | 2008 § 39(b) |
| school-role supplement | **no** — the full shekel value | 2022 § 22.9 |

The running fixture takes **11,008.03** on a full post and **6,004.38** on half of one: 54.5%
of the pay for 50% of the work. The excess over half is exactly half the homeroom supplement,
and `ofek-cases.l4` asserts that identity rather than the bare number. A teacher just below a
third of a post loses the supplement outright and drops *below* a proportionate share.

### 5.3 Which printing of the table is authoritative

The 2022 wage agreement attached its tables rounded to the **shekel**. A decision of the joint
follow-up committee of **14 January 2025** corrected a scribal error in that agreement and
replaced those appendices with tables to the **agora**, effective from the same 1 September
2022 — and, in the same decision, corrected the date the increased Tosefet Ofek took effect
from a mis-typed "1.1.23" to 1.9.2023.

The agorot tables are the text in force for the whole period, and they are what this encoding
reads. The shekel printing is what a reader is most likely to find first, which is why the
difference is stated here and in the module header. This was found by reading the document
register, not by reading the tables — the register is what made a January 2025 committee
decision visible as the authoritative source for numbers otherwise attributed to an October
2022 agreement.

### 5.4 The 2025–2026 reduction is encoded from the agreement, not from the Act

Chapter 9 of the Budget Objectives Act 5785-2025 does not itself set the reduction for a group
that reaches a deal. It reduces pay "in accordance with the provisions laid down in a
collective agreement applying to the employee, **approved** for this purpose by the Minister
of Finance or the Wage Commissioner", and only failing such an agreement does the Act's own
rate apply. For teachers that approved agreement is the one of 29 June 2026, and it is the
operative instrument.

It is also the readable one. The corpus's copy of the Act is a PDF extraction of the whole
Budget Act, and PDF-extracted Hebrew in this corpus is bidi-damaged: in Chapter 9 the
definition of "the determining base" arrives duplicated and interleaved with itself. The
agreement carries the same definition cleanly. Encoding from the agreement is therefore both
the legally correct choice and the textually possible one — and it is a choice, recorded here
rather than left to be inferred.

## 6. Three worked payslips

`ofek-cases.l4` computes these end to end. Every figure below was obtained by **evaluating**
the encoding, not by arithmetic done alongside it.

**Yael** — BA, seniority 11, rank 4, full post, homeroom teacher of a class other than the
first grade:

```
combined salary     BA table, seniority 11, rank 4              9,171.76
Tosefet Ofek 2022   BA rank 4, from 1.9.2023                      835.54
                                          the § 39 base       10,007.30
homeroom supplement 10% of that, just above the 1,000 floor    1,000.73
                                                              ─────────
                    before the reduction                      11,008.03
                    November 2025, after § 9(a)'s 0.95%       10,903.45
                    March 2026, after § 9(b)'s 1.2%           10,875.93
```

Her homeroom supplement clears the 2022 § 10 floor by **73 agorot**. A teacher one rank below
her is inside it.

**Dvora** — MA, seniority 30, rank 8, full post, two role supplements, three school-role
units: **18,300.50** before 1.9.2026 and **18,900.50** after it, when the § 22 supplement
starts — a year later than the 2022 agreement said, because § 19 of the 2026 agreement
postponed it. At rank 8 her Tosefet Ofek is **37.37**, against the **1,585.54** a rank-1 BA
teacher receives: the payment at the bottom of the table is more than forty times the payment
at the top, which is the levelling § 5 was for.

**Noa** — doctorate, seniority 6, rank 3, half a post: **5,000.99**, of which **211.00** is
the § 36(d)(2) doctorate uplift.

## 7. The Catala export

`catala/ofek_hadash.catala_en` is this encoding compiled to **Catala**, and it **typechecks
under catala 1.2.1** and computes the same numbers.

### 7.1 Why there is a generated ninth module

`l4 catala` compiles **one** module: a reference into an imported module is rejected as
unbound, and a type declared elsewhere is reported as outside the v1 fragment. The
eight-module encoding is therefore not compilable as it stands.

Flattening it by hand would put a second copy of every number in the tree, and the two would
drift the first time either was corrected. So `ofek-catala.l4` is **generated**, by
`source/build-catala-module.py`, from the **same corpus parse** (`source/tables.py`) that
produced the tables in `ofek-salary-table.l4`. Neither file is derived from the other; both
are derived from the 14 January 2025 decision. They are then tied together by assertions: the
figures the generated module asserts are the figures `ofek-cases.l4` asserts, so if the two
ever disagree, one of them goes red.

It is a **decision core**, not the whole encoding: it carries the computation of pay and omits
the § 38 promotion machinery, the working-week patterns, and the § 39(c) supplement cap. It
also gives a teacher a first and a second role rather than a list — which is not a workaround
but the shape of § 39(c), and it costs the ability to express a third district-approved
supplement.

### 7.2 The round trip actually runs

`source/run-catala.sh` regenerates the module, emits the Catala, typechecks it, and then
**runs** six case scopes through `catala interpret` and compares each against the figure the
L4 encoding asserts:

```
   scope                              catala says      ofek-cases.l4 asserts
   YaelInSeptember2024                11,008.03        11,008.03        ok
   YaelInNovember2025                 10,903.453,715   10,903.453,715   ok
   YaelInNovember2025HavingAdvanced   10,773.453,715   10,773.453,715   ok
   YaelOnHalfAPost                    6,004.38         6,004.38         ok
   DvoraInOctober2026                 18,673.689,801   18,673.689,801   ok
   NoaInSeptember2024                 5,000.987,5      5,000.987,5      ok
```

Typechecking alone would not have caught a lowering that quietly changed the arithmetic.
Running it does.

### 7.3 Two upstream findings, with minimal reproductions

**(a) `#ASSERT` directives are not lowered to `#[test]` scopes.** Every directive in this
module is reported as *"did not become a Catala `#[test]` scope … that is a lowering bug,
please report it"*, and the disclosure is emitted in place of the test. The consequence is
that `catala/ofek_hadash_cases.catala_en` had to be written **by hand**, and must be updated
by hand when the encoding changes. Recorded as fork F12.

Bisected to two distinct triggers. A directive's helper is collected only when its body is
**exactly** an application of the exported decision:

```l4
GIVEN d IS A DATE
GIVETH A NUMBER
`q3` d MEANS `pay` (Rec WITH a IS 5, r IS NOTHING) d 0        -- lowers
`q2` d MEANS `pay` (Rec WITH a IS 5, r IS NOTHING) d 0 PLUS 0 -- dropped
```

and, separately, a **nullary** helper is never collected — while the diagnostic names the
function being applied rather than the constant that was missed:

```l4
GIVETH A NUMBER
`five` MEANS 5
#ASSERT `twice` `five` EQUALS 10   -- dropped, blaming `twice`
#ASSERT `twice` 5      EQUALS 10   -- lowers
```

Even with both worked around, this module's directives are still dropped, so at least one
further trigger remains unidentified. That is stated as a limit of the investigation, not as
a diagnosis.

**(b) `l4 catala` can emit a module that `catala typecheck` rejects, and says nothing.**
Annotating both `the monthly pay of` and the `the full-post percentage base for` it calls made
the latter lower to a *scope*, and the emitted module then called that scope from inside a
toplevel definition. `l4 catala` exits 0; `catala typecheck` rejects it outright:

```
Scope calls are not allowed outside of a scope.
```

**Corrected 2026-09-07.** The lesson first drawn from this — that a function another exported
function calls cannot itself be exported — is **false**, and the correction matters because it
was the reason this module carries a single `@export`. An `@export`ed function lowers to a
scope, and Catala allows a scope call only from inside another scope. So exporting a helper is
fine *provided every caller of it is exported too*. Two exported functions, one calling the
other, typecheck. Insert one **non-exported** definition into the chain and the same two
`@export`s now fail:

```l4
@export the base
GIVEN `the n` IS A NUMBER
GIVETH A NUMBER
`the base` `the n` MEANS `the n` TIMES 10

GIVEN `the n` IS A NUMBER          -- not exported: lowers to a toplevel definition,
GIVETH A NUMBER                    -- and this is the call catala refuses
`the middle` `the n` MEANS `the base` `the n` PLUS 1

@export the pay
GIVEN `the n` IS A NUMBER
GIVETH A NUMBER
`the pay` `the n` MEANS `the middle` `the n` TIMES 2
```

Delete `the middle` and the module typechecks. That is what broke here: `the full-post
percentage base for` also has a non-exported caller, `the supplement for one slot of` at
`ofek-catala.l4:492`.

Measured the whole way, on the real module: putting `@export` on every definition that takes
a `GIVEN` — 28 in all, the 27 added to the one already there — emits **43 scopes** (five of
them fan out into `…EqvAgree` / `…EqvModeA` / `…EqvModeB` triples), `catala typecheck`
succeeds, and the six worked cases return the same six figures as the single-scope build,
digit for digit. So the single `@export` is a **choice** — one published scope instead of
forty-three — and not, as recorded here until today, a limitation.

The bug worth reporting is therefore the **silence**, not the composition: `l4 catala` already
refuses the section-`GIVEN` case with a good diagnostic, so the machinery to refuse exists; it
just does not check whether an exported helper has callers that are not exported. Filed
upstream as [smucclaw/l4-ide#958](https://github.com/smucclaw/l4-ide/issues/958) (7 September
2026, from the reproduction above; both halves of it are since measured independently on two
machines). Recorded as fork F13, restated.

### 7.4 Reproducing it

```sh
export OFEK_CORPUS=/path/to/ofek-hadash-corpus
./source/run-catala.sh
```

Needs `catala` and `clerk` 1.2.1 on an opam switch named `catala`, and an `l4` binary built
from the same tree as the prelude it is pointed at. The script builds each stdlib module
object one at a time, because `clerk build` with no target refuses without a `clerk.toml`.

Two traps if you run `catala` by hand instead of through the script. The switch is a **named**
one, so the binary is at `~/.opam/catala/bin` and a bare `which catala` finds nothing — reach
it with `opam exec --switch=catala --`, which is what the script does. And `catala typecheck`
outside a project directory fails with *"The standard library module Stdlib_en could not be
found at `_build/libcatala`"* — which looks like a broken install but is not, and the message's
own hint names the repair: run `clerk start` in the directory first.

## 8. What review would mean

`report/` and `gates/` are absent, and no human gate has been granted or waived. For this row
to stop saying "not reviewed", someone who knows Israeli teachers' pay would need to:

1. read `ofek-salary-table.l4`'s frontier against § 38 and settle fork **F1** — whether a
   merged cell means "this rank pays that amount" or "this rank does not exist here";
2. settle **F3**, the § 38(g)/§ 38(i) deadlock, which the agreement leaves open and which the
   encoding therefore reports from both sides;
3. confirm **F9** — that the *full-post* Tosefet Ofek enters the § 39(b) base, not the
   teacher's own pro-rated one; on a half post the readings differ by about 42 shekels a
   month for the running fixture;
4. check the three worked payslips in §6 against an actual payslip.

Until then this is an encoding of the text, checked against itself and against the source
documents, and nothing more.

## 9. How the tables are written, and why they look like that

The two salary tables are 648 amounts. Written the obvious way — a 36-arm
`BRANCH`, each arm naming the record's nine fields — a row ran to **320
characters**, of which the great majority was the same tokens repeated
thirty-six times. That is ink carrying no data.

Two changes, both of which the language already had:

**Positional construction.** `Ctor OF a, b, …` builds a record by position, so
the nine field names and their nine `IS` keywords vanish from every row. The
rank is carried by the column, and a ruler comment names the columns once above
the table.

**Ditto.** `^` is "the token at this column on the line above". The guard
subject, `THEN`, the constructor and `OF` are written once on the first row and
dittoed after it. Every column is fixed-width so that each caret sits exactly
under what it copies.

A row is now **184 characters**, and what remains on it is what varies: the
seniority, and nine amounts. Read down a column and you are reading the table
as the agreement prints it.

Two things learned doing this, recorded so the next person does not rediscover
them. `AT MOST` is **two** tokens, so one caret under it resolves to `AT` and
the parser then wants `MOST`; the operator is left written out rather than
dittoed with a pair of carets, because the saving was not worth the fragility.
And a backtick identifier is **one** token, so `` `at rank 2` `` cannot be
dittoed down from `` `at rank 1` `` — only whole names can.

The same treatment is applied to the Tosefet Ofek appendices, the rank lookup,
and the working-week tables in `ofek-worktime.l4`, where `OF` lets § 15's and
§ 17's four bands line up as the four-row tables the articles actually print.

### 9.1 The emitted Catala is wrapped

A 36-arm `BRANCH` lowers to a right-nested `if … then … else (if … )` chain, and
`l4 catala` puts the whole chain on one line: **9,771 characters** for a salary
table. `source/wrap-catala.py` breaks it before each `else (if (`, which puts
one seniority row on each line and takes the longest line in the artifact down
to 659.

Catala is not layout-sensitive inside a code block, so this changes no token —
and that is checked rather than asserted, twice. The script compares the token
streams before and after and refuses to write if they differ; and
`source/run-catala.sh` typechecks the **wrapped** file and re-runs all six
worked cases against it.

## 10. Goldens

There are none, and that is deliberate. The four-goldens-per-file discipline of `jl4-test`
applies to files inside `l4-ide`'s corpus globs; this row is in `canon`, which has no CI, so
committed goldens would be a point-in-time record that nothing regenerates. `check.sh` and
`source/run-catala.sh` are the reproducible gates instead, and both run in seconds.

## 11. Why every rule repeats its own `GIVEN`

The obvious tidy-up, and why it is not applied.

L4 grew a **section `GIVEN`** in September 2026 (`legalese/l4-ide` #333, elaborated by #344):
a `GIVEN` written one indent past a `§` heading is read by every rule under that heading, so
a line repeated on ten consecutive rules is written once. `ofek-pay.l4` looks like the
textbook case — all ten of its top-level `GIVEN`s are that same line, under one `§`, and the
three under `ofek-domain.l4`'s `§§ Reading the record` are three more.

Two measured reasons it is the wrong shape for *this* encoding.

**A rule that reads a section `GIVEN` takes no positional argument, and cannot be supplied
across an `IMPORT`.** The binder is discharged into the rule's parameters at the *evaluation*
entry points only; the type checker still sees arity zero, and a call site that passes a
teacher positionally is a check error:

```
You are giving 1 input to
  `the rank of the teacher` … of type NUMBER
but it is not a function, so it takes none.
```

**Corrected 2026-09-07.** An earlier version of this note said the repair was a
`GIVEN`-parameterised twin per rule, and priced it at the 254 assertions. That was read from
a stale line in the `writing-l4-rules` skill — supplying a section `GIVEN` with `WITH` is not
"proposed, not landed"; it landed with the discharge change and works on this binary. Inside
one module the directives need no twin at all:

```l4
#ASSERT (`the pay of the teacher` WITH `the teacher` IS `Yael`) EQUALS 8000   -- satisfied
```

**The parentheses are load-bearing.** `WITH` binds looser than `EQUALS`, so the unparenthesised
form is a check error — and its diagnostic names the identifier and `__EQUALS__`, never `WITH`,
which is a poor thing to meet on assertion one of two hundred and fifty-four.

What does not work is the boundary this encoding is built across. `WITH` on an **imported**
rule is refused — *"You are giving named inputs to …"*, exit 1 — and that is where the cost
actually sits. `ofek-cases.l4` declares nothing but fixtures, so all **49** of its assertions
reach a rule in an imported module; and the three rules under `§§ Reading the record` are
called from **five** further sites in two other modules (`ofek-pay.l4:64,82,94,107`,
`ofek-placement.l4:60`). A section `GIVEN` in `ofek-pay.l4` or `ofek-domain.l4` puts every one
of those out of reach, and no twin written inside the declaring module reaches them either,
because the caller is outside it.

**What that message is, exactly**, since it matters for anyone reading it as a verdict. It is
not the props programme's ruled refusal, which is ruled and *not built*
(`OPEN-FINDINGS-2026-09-05.md` **OF-7**, ruled at `IMPLICIT-PROPS-DESIGN.md` §11.19,
2026-09-05). It is `IllegalAppNamed`, which predates the whole programme — oldest commit
touching it in `jl4-core/src/L4/TypeCheck.hs` is `294867c7`, 17 March 2025. What routes to it
is new: `inferAppNamed` (`TypeCheck.hs:3343-3358`) admits named arguments on a 0-ary
definition only when every supplied name passes `isSectionBinderSupply`, and that predicate
reads `sectionBinderNames`, built by `collectSectionBinderNames program` over **this** module
(`TypeCheck.hs:215`). Across an `IMPORT` the callee's binder is not in the caller's set, the
guard fails, and control falls through to the old error. So the message is not merely
unhelpful, it is **wrong about the cause**: the callee *is* a function of that binder in its
own module, and the caller simply has no way to name it.

**`l4 catala` refuses a section `GIVEN` read by anything but the exported decision.** The
backends lower the module the author wrote, not the discharged one; that is deliberate
(l4-ide `specs/todo/IMPLICIT-PROPS-DESIGN.md` §11.10, ruling **R10**, ruled 2026-09-04 and
not yet built). Minimal reproduction — a section `GIVEN`, one helper that reads it, one
`@export` decision that calls the helper:

```
l4 catala: cannot compile these decisions to Catala:
  - in `the rank of the teacher`: ASSUMEd input `the teacher` is only readable inside an
    @export decision's scope (where it becomes a scope `input`); pass it to this helper as
    a parameter instead
```

The refusal has an escape hatch, found on the l4-ide side while § 7.3(b) was being written up
there and verified here: marking the **helper** `@export` as well lifts it, because the binder then
becomes an `input` on both scopes and the caller threads its own copy through. It typechecks.
The cost is the one in § 7.3(b) — a published scope per rule that reads the binder, under the
same all-or-nothing condition, since one non-exported caller anywhere in the chain puts the
module back in the shape shown there. For `ofek-pay.l4` that is ten published scopes where ten
helpers were wanted. That is what R10 buys back: the helpers, not the ability to compile.

All of the above was probed on the binary this row is built with (`ofek/build`, at
`origin/unstable` 9d6536a9, which contains #344).

**The two blockers are not the same one twice**, though they are easy to merge and this note
did merge them for a day. The `IMPORT` blocker is about the module boundary. The Catala
refusal is not: it fires in a **single** file, on a section `GIVEN` read by a non-exported
helper, and the reproduction above is one such file. What the eight-module split defeats is
the *escape hatch* — exporting the whole chain — because the chain runs across modules. The
refusal itself would greet a one-file encoding just the same.

What is fair to say once, rather than twice, is about **size**. The repetition a section
`GIVEN` removes grows with the encoding; a large encoding is also the one most likely to be
split across files and to have a `@export` boundary partway down it. So the temptation peaks
where the fit is worst. **Count the callers before hoisting, not the repetitions.** None of
which is a complaint about the feature: the props spec records the cross-`IMPORT` hole as a
known defect with a ruled repair order — refusal first, closure second — at OF-7 and §11.19.

**Revisit when both land** — OF-7's closure for the module boundary, R10 for the Catala one —
and start with `ofek-pay.l4`: it is the one module where every rule under one heading reads
the same fact, and the one a reader is most likely to open. Until then, note that this row
would be the tree's first reachable cross-`IMPORT` section binder; the props spec's
measurement that no file in `jl4/examples`, `jl4-core/libraries` or `doc/` reaches that
configuration (2026-09-05) is scoped to `l4-ide` and is still true there.
