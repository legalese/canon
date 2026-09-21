# `ofek hadash` — a Hebrew-canonical L4 encoding

Working notes for the encoding in this directory. Written at integration, after the seven modules
were wired into one import graph and run together. Everything here was measured on
`../l4-vinyl` on 2026-09-19; where a claim is a judgement rather than a measurement it says so.

---

## 1. Status

| module | lines | `#ASSERT` | satisfied | failed | not evaluated | errors |
| --- | --- | --- | --- | --- | --- | --- |
| `he-domain.l4` | 378 | 7 | 7 | 0 | 0 | 0 |
| `he-tavlaot.l4` | 859 | 65 | 65 | 0 | 0 | 0 |
| `he-mishra.l4` | 1315 | 80 | 80 | 0 | 0 | 0 |
| `he-sachar-meshulav.l4` | 1413 | 107 | 107 | 0 | 0 | 0 |
| `he-gmulim.l4` | 957 | 35 | 35 | 0 | 0 | 0 |
| `he-brutto.l4` | 887 | 53 | 53 | 0 | 0 | 0 |
| `he-cases.l4` | 1377 | 110 | 110 | 0 | 0 | 0 |
| **total** | **7186** | **457** | **457** | **0** | **0** | **0** |

`l4-vinyl check` exits clean on every module. `l4-vinyl format` round-trips every module
byte-identically. Zero bidi control characters (U+200E/200F, U+202A–202E, U+2066–2069) and zero
combining marks (Unicode category `Mn`) anywhere in the set; every filename is ASCII.

**Read the count carefully.** The runner logs each satisfied assertion twice, so a raw
`grep -c 'assertion satisfied'` gives double these figures. The numbers above count the
`Message:  assertion satisfied` form, which appears once per assertion, and they match the count of
`^#ASSERT` lines in each file exactly.

---

## 2. The import graph

```
prelude
  └── he-domain          types only: no rule, no number, no table
        ├── he-tavlaot   the printed grids, and lookup off them
        ├── he-mishra    hours ⇄ post size; the 2008 work-week ladders
        │     └── he-sachar-meshulav   placement, progression, darga-indexed money
        │           └── he-gmulim      role supplements and hour-priced work
        │                 └── he-brutto  the payslip: month-specific items and the reduction
        │                       └── he-cases  eighteen worked cases, and nothing else
```

Each module imports every module above it that it needs, and nothing imports downward. There are
**no duplicate declarations anywhere in the set**: a mechanical scan of every top-level
`DECLARE` / `MEANS` name across all seven files returns no name defined twice.

### What integration changed, and why

The seven modules were written in parallel by encoders who could not see each other's work, so each
stood alone and three of them had duplicated a neighbour's material. Four changes reconciled them.
No rule was deleted and no expected value was adjusted.

1. **The seven 2008 work-week ladders lived in both `he-tavlaot` and `he-mishra`** — 111 rows,
   transcribed twice, independently, from the same signed annexes. Before removing either copy the
   two were compared **mechanically, field by field**: all seven ladders, all 111 rows, identical in
   every column. That agreement is the most valuable single piece of evidence in this encoding and
   it exists only because of the duplication, so it is recorded here rather than thrown away with
   the copy. The ladders now live only in `he-mishra`, which is where the plan puts them (§3.2) and
   which is the only module with rules that read them. `he-tavlaot` is generated, so the deletion
   was made in its generator (`../work/gen.py`) and the module regenerated; a hand edit there would
   be silently reverted on the next run. Cost: 20 of `he-tavlaot`'s assertions went with the data.
   Fifteen equivalent assertions remain in `he-mishra`.
2. **`he-brutto` had re-typed the `הבראה` day table and the 511.6 ₪ day value**, which the plan
   assigns to `he-tavlaot` (§3.3). Both copies agreed. `he-brutto` now keeps its local names —
   `ערך יום הבראה בשנת תשפ"ו`, `ימי הבראה לפי ותק של` — as one-line pointers at `he-tavlaot`'s
   definitions, so its eight assertions survive and now test the owning module's data. One truth,
   two names.
3. **Three names collided outright**: `ערך יום הבראה בשנת תשפ"ו` (`he-brutto` + `he-cases`),
   `שיעור תוספת תואר שלישי` (`he-sachar-meshulav` + `he-cases`) and `שבוע יסודי מלא`
   (`he-sachar-meshulav` + `he-cases`). In all three the two definitions carried the same value.
   `he-cases` now imports the first two rather than re-declaring them; `he-sachar-meshulav`'s local
   test fixture was renamed `שבוע יסודי מלא לבדיקות השיבוץ`, because `he-cases` is the module the
   plan makes the owner of fixtures.
4. **`he-gmulim` and `he-brutto` were standalone**, each collecting its upstream quantities into a
   local record passed to every money rule. Both now genuinely `IMPORT` their parents, and each
   gained exactly one constructor function that fills that record from the instruments:
   `נתוני השכר של` in `he-gmulim` and `השכר החודשי הרגיל של` in `he-brutto`. **No rule above either
   constructor changed shape.** The fields that remain inputs are the ones no instrument in the
   corpus derives — the two special-ed/gifted frontal shares, the identity of the supplements
   counted in the pension-determining salary (gap **G1**), and the monthly hour-priced and
   trip-escort totals, which depend on a report rather than on a teacher.

---

## 3. The naming convention

Hebrew has to yield **three distinct strings** for one concept, because L4 needs the type, the record
field and the free parameter to be different names. The convention invented here, and held without
drift across all seven modules:

| position | form | example |
| --- | --- | --- |
| type | bare citation form | `` `דרגה` `` |
| record field | the definite form | `` `הדרגה` `` |
| free parameter | construct state, named for its owner | `` `דרגת המורה` `` |

Every name is backticked, including single-word ones, for uniformity. Functions are verb or noun
phrases long enough that they cannot collide with a type (`` `השכר המשולב במשרה מלאה של` ``).

One extension was needed and is worth keeping. In `he-brutto` a payslip money field would have
collided with the identically-named member of `רכיב שכר` in `he-domain`, so money-bearing fields
carry the prefix `סכום ה־`: `` `סכום השכר המשולב` ``. It reads as ordinary Hebrew ("the amount of")
and cannot collide with a component name.

Every `DECLARE` and every rule carries an `@ref` naming the instrument and the article. `@nlg:he`
is used where it attaches correctly — see §7.

---

## 4. What is encoded

- **`he-domain`** — base §3 (scope), §7 (definitions), the three hour kinds, the 17-step darga
  ladder, the five dirug codes, the closed list of twelve gmul-bearing roles, the pay-component
  taxonomy of takanon §1.1. No rule, no number, no table.
- **`he-tavlaot`** — the printed grids: `שכר משולב` appendices `א'1`–`א'7` (36 seniority rows each),
  `תוספת אופק 2022` appendices `ב'` and `ג'`, `תוספת שקלית 2016`, and the `הבראה` day bands.
  Generated from the corpus HTML by `../work/gen.py`; a hand edit is reverted on the next run.
- **`he-mishra`** — base §§14–34: the five-day week, the primary and junior-high full weeks, §17א
  role hours, special education, `מורה אם` and post-maternity, §26 age hours, §27 part-time and its
  floors, §28's monthly reckoning, §32–§33א's caps — and the seven annex work-week ladders.
  **No money.**
- **`he-sachar-meshulav`** — base §35–§38, 2022 §§4–5, 19.3.2017 §2: which appendix, darga and
  seniority row a teacher stands in; how they move; and the three amounts that follow.
- **`he-gmulim`** — base §29–§31, §33(ד), §39–§42, 2022 §§10–12: the percentage role supplements
  with their floors and the two-supplement cap, and everything priced per hour.
- **`he-brutto`** — the payslip: the monthly sum, June's `הבראה` and `יובל`, July's `ביגוד`, the
  monthly `מעונות`, and the statutory reduction of the 27.3.2025 law and the 29.6.2026 agreement.
  The only module that knows what month it is.
- **`he-cases`** — eighteen worked cases and 110 assertions. No rule.

---

## 5. What is not encoded, and why

Each of these is a **named refusal in the code**, carrying its citation, not a silent omission. A
refusal evaluates as a warning and propagates; it is never a zero and never a neighbouring value.

**Gaps in the corpus** (the instrument exists but its text does not):

- **G1** — the 31.8.2008 agreement on the pension-determining salary, pointed to by base §150. Its
  absence is why `he-gmulim` takes the *amount* of pension-counted role supplements as a payslip fact
  rather than deriving *which* supplements those are. A judgement worth a reviewer's eye: refusing
  instead would make §30 and §29(ד)/(ה) unevaluable for every teacher.
- **G2** — the 30.9.2016 agreement has no text in the corpus (unreadable OCR). It is the origin of
  `תוספת שקלית 2016`, of the half-dargot and of `תוספת שמירת שכר`. Entitlement under its §4(ג) and
  the `תוספת שמירת שכר` formula are both refusals; the supplement's **cancellation** on promotion is
  encoded, because the 19.3.2017 amendment quotes that clause in full.
- **G3** — the 2022 signed appendices are truncated after `א'5`. `א'6`/`א'7` and `ב'5`–`ב'7` survive
  only in the takanon portal. **Correction to the plan**, measured on the pages themselves: the plan
  says those printings are "captioned 1.9.2016" and therefore six years stale. They are not —
  `nispach-alef-6` and `-7` both say `טבלה מעודכנת החל מיום 1.9.2022`, and `nispach-bet-5/6/7` say
  `מעודכן החל מיום 1.9.2022` with their `ג'` twins at 1.9.2023. G3's real content is the truncation,
  not the staleness. No worked case uses dirug codes 105 or 106 all the same.
- **G4** — the latest `קצובת ביגוד` circular is `תשע"ח/7` (2018). Eight annual updates are missing,
  so no case quotes a clothing allowance; `he-brutto` takes it as an input and refuses the
  indexed/unindexed difference that 29.6.2026 §20 needs.
- **G5** — the Ministry's letter of 25.12.2008, which §38(א)(2) makes a condition of every promotion.
  The promotion criteria are therefore fields of `בקשת קידום`, not rules.
- **G6** — §25 and §7(ג) are truncated in the transcription of the base agreement. **Partly
  discharged**: §25 reads complete in the signed registry copy and is encoded from it. §7(ג)'s tail
  was not needed and was not checked.

**Further gaps found during encoding, beyond the plan's list:**

- §11 of the 12.1.2011 framework agreement — the *source* of the `תוספת מעונות` entitlement — is not
  in the corpus. What is there is a rates circular: it prices a first child (372) and a second (251),
  says nothing about a third, and nothing about who is entitled.
- The 25.12.2008 Wage Commissioner's letter that §22(ג) conditions on.
- The `נוהל שיסוכם בין הצדדים` of §38(ח).
- The §40(ב) trip-escort table inserted by `הסכם השלמה` art 29 has **both** column headings printed
  as `[לא קריא]`. The seven figures are legible; what they measure is not. The shekel conversion
  refuses while the raw figure is still returned.
- Art 14 of the 29.6.2026 agreement is mostly missing, and the corpus says so in its own margin.
- The `שילוב` and para-medical work-week annexes: the instrument itself left a blank line where the
  annex number should be (`הסכם השלמה` art 17(ב)).
- The number of weeks in a month that §28(ב) orders a monthly reckoning by. Refused rather than
  borrowing the 4.33 that §31(ב) states for a different purpose.

**Deliberate non-isomorphism**, recorded in the code as commented articles rather than omissions:
§12 and §18 of the 29.6.2026 agreement (no training-fund or pension line exists in this encoding to
reduce), and §42 of the base agreement, whose entire operative content is the word `בלבד` opening
§39 — which the type system already enforces, since a supplement for an off-list role is not
expressible.

---

## 6. The forks

The plan named eleven. Each is recorded in the module that owns it, in the instruments' own words.

| fork | the question | reading taken | how it is supported here |
| --- | --- | --- | --- |
| **F1** | the `ערך שעה` denominator for a teacher with age hours: 36, or this teacher's own 34 | **B — the teacher's own** | The annex labels the 34-hour and 32-hour weeks **100.00%**, so the instrument itself treats the reduced week as this teacher's full post. Independently confirmed: §26's prose applied to the full week reproduces the annex's 100% row in all six stage×band combinations. |
| **F2** | the base of a percentage `גמול תפקיד` | **`שכר משולב` + `תוספת אופק 2022`** | 2022 §5.4 is explicit, and the silence about `תוספת שקלית 2016` is a silence in an instrument that knew how to say it. **Wider than the plan stated**: §5.4 also names the hour value for substitution and school activities, absence deductions, and §33(ד). Encoded that way; the 1,000 ₪ floor of 2022 §10.1 binds at case C3 exactly as predicted. |
| **F3** | which `תוספת אופק` appendix a whole-darga teacher reads | **`ב'1`/`ג'1` for the whole-darga set, `ב'3`/`ג'3` for the converted** | The `א'3`/`ב'3` pairing is the existing-teacher set. The 0.23 ₪ gap at darga 4 is carried, not smoothed. Case 12 is the test: a half-darga teacher is sent to the `א'3`/`ג'3` family and the figures that come back are the ones the plan names for that family. |
| **F4** | the effective date of `ג'3` (1.1.2023) against §5.2 and its siblings (1.9.2023) | **not resolved** | `he-tavlaot` carries the caption verbatim and declines to choose: a date is not a table lookup. The choice belongs to whichever module asks for a value *at a date*, and no module in this set does. |
| **F5** | does `גמול השתלמות` survive for a reform teacher | **B — it does not** | A named, reasoned refusal in `he-gmulim` citing §44(ב)(1), §46א and takanon §1.26 ¶1.2 against takanon §1.1(ו). The largest single money question in the encoding. |
| **F6** | `תוספת 2001/2008/2011` and `תוספת הסכם הוראה 94` | **absorbed at conversion** | Carried as an explicit refusal rather than an omission, since the takanon is the corpus's only systematic statement of payslip composition. |
| **F7** | §31(ב)'s lost fraction bar | **division**, on the 2012 replacement text | No competing reading. Recorded because it is evidence the transcription can lose a *relation*, not only a character. |
| **F8** | the `מענק יובל` threshold for a primary teacher: 25 or 30 | **the circular** (30 primary, 25 junior high) | Most recent, most specific, addressed to the bodies that pay. The 2008 agreement's title is recorded as competing evidence, and the circular's colleges-on-both-sides contradiction is recorded as a defect rather than resolved. |
| **F9** | what `הבסיס הקובע` excludes | **school-activity pay is inside** | No operative clause excludes it. The unused definition is flagged: it is the signature of a clause the corpus does not have. |
| **F10** | the pension-determining salary in `מענק יובל` | **combined + `תוספת אופק 2022` + pension-counted supplements** | Same reasoning as F2, resting on an instrument the corpus does not contain (G1). |
| **F11** | encode the §44 `המרה` at all | **placement is an input** | Half-dargot are first-class values. Said on the page: this encoding computes the salary of a teacher on darga 4.5 and cannot say **why** they are there. §44 is the answer, and it is not encoded. |

Module-local forks also recorded in the code: **F-B1**, the `הבראה` table's silent jump from "first 3
years" to "4–10 years" (read as: whole years, so anything above 3 and below 11 earns 9 days).

---

## 7. Toolchain facts measured on `l4-vinyl`

Carried here because each cost a check cycle, and because the first two fail **silently enough to
ship**.

- **`@nlg` binds to the node BEFORE it, not the declaration below it.** An `@nlg:he` line written
  above a `DECLARE` lands on the *preceding* declaration's last child and raises
  `More than one NLG annotation attached to: …` — a **warning**, never an error, so a green `check`
  would have shipped the wrong rendering into a wizard. One draft had 17 such lines and 9 collisions.
  The inline form (`DECLARE T @nlg:he … IS ONE OF`) is a parse error. There is therefore no working
  spelling for a type-level `@nlg` on any declaration after the first in a file. It binds correctly
  on enum constructors, on record fields, and on a rule whose preceding node is a `§§` heading —
  which is why the payment functions in `he-sachar-meshulav` do carry one. `@ref` above a `DECLARE`
  binds correctly and is untouched.
- **Positional `OF` construction is silently order-dependent.** Swapping two same-typed fields in a
  row literal changes the value with no diagnostic. Every generated ladder and grid in this encoding
  therefore carries a field-order comment directly above it, and none of them uses the ditto
  operator: a caret landing on the wrong token is the same failure with the same silence.
- `#ASSERT <expr> EQUALS n` **cannot span lines**. The spreading form is `#ASSERT n EQUALS` on the
  head line with the expression indented beneath. `#EVAL` is strictly one line.
- A `GIVEN` parameter typed `IS A LIST OF T` opens a layout block, so it must come **last**; a comma
  after it is swallowed into the element type, and parenthesising `LIST OF T` is rejected.
- Function application binds tighter than the genitive: `f x's y` parses as `(f x)'s y` and needs
  parentheses.
- A `LIST` of positionally-constructed records needs each row parenthesised, or the row's own commas
  are read as further `OF` arguments. The diagnostic is an indentation complaint pointing at the
  *second* element.
- Nested `LIST` on separate lines is a layout error. An `IF … ELSE IF … ELSE IF` chain at one
  indentation is a layout error; a printed band table is better expressed as a `LIST OF PAIR` plus a
  recursive lookup, which is also closer to the instrument.
- Comparison operators are `AT MOST` / `AT LEAST` / `LESS THAN` / `GREATER THAN`; the prelude's
  `__LEQ__` family is for `MAYBE NUMBER` only. List membership is `elem x list`, not `IN`. `max` and
  `min` are prefix. There is no `abs`, so a tolerance test is two assertions or a named helper.
- A backtick inside a `§§` heading ends the heading name; write the heading in plain words.
- Decimal literals compare exactly (`8038.19 EQUALS 6955.71 PLUS 1082.48` is satisfied), but a
  quotient compared against a hand-copied decimal does not round-trip through the printed
  representation. Six assertions in `he-gmulim` therefore compare through an explicit
  `ההפרש זניח בין … לבין …` (< 1e-6), each with a comment saying why. The other 451 are exact.
- Hebrew works in every name position. Colons, maqaf (U+05BE), geresh, gershayim and an escaped
  gershayim inside a string all parse. Not verified and therefore avoided: a bare ASCII double quote
  inside a backticked identifier.

---

## 8. What a reviewer has to settle

Ordered by how much money moves.

1. **`גמול חינוך מיוחד` — two modules currently answer the same question two ways.** §39(א)(3) prints
   four rates (5.5%, 8.5%, 9%, 14%) and conditions them on eligibility rules "that existed on the eve
   of this agreement's signing", which are not in the corpus. `he-gmulim` **refuses** to pick.
   `he-cases` names **9%** as a quoted constant. Both positions cannot stand. The disagreement is now
   visible in the code: the last two `#EVAL`s in `he-cases` print the refusal and the 9% side by
   side, with a comment saying the ruling is a reviewer's. Nothing breaks mechanically — the two
   never meet in a computation — which is exactly why it needed to be made visible.
2. **F5, `גמול השתלמות`.** If reading B is wrong, every payslip in this encoding is short by a
   percentage of combined salary. It is a refusal, so a wrong answer cannot be produced silently —
   but a missing line is still a wrong payslip.
3. **G1 handled as an input rather than a refusal** (`he-gmulim`). Turning it into a fourth refusal is
   a one-line change. The argument for the present treatment is that refusing makes §30 and §29(ד)/(ה)
   unevaluable for every teacher; the argument against is that an input invites a caller to supply a
   number nobody has derived.
4. **Whole shekels or agorot for `תוספת אופק 2022`.** The plan's worked cases quote 1,586 / 1,086 /
   586 / 1,665; this encoding returns 1,585.54 / 1,085.54 / 585.54 / 1,664.87, following the plan's
   own §4.1 precision rule and the 14.1.2025 `ועדת מעקב` correction, whose whole purpose was to undo
   the rounding. The 0.46 ₪ gap is deliberate and commented at the site. Same family as the 0.23 ₪
   `ב'1`/`ב'3` gap at darga 4 under F3.
5. **F4's date**, still open by design.
6. **`he-domain`'s institution list.** `סוג מוסד` carries four members; base §3 also names
   `אשכול פיס` and `מרכז פסג"ה`. They were left out because §18 — the only article giving an
   institution type a distinct work-week consequence — names only the four. If a later module needs
   them for *scope* rather than for hours, this file must change, and that is the cut line's own
   stated test failing.
7. **Should `he-domain` carry a children field?** `תוספת מעונות` scales by number of children and no
   such field exists. Adding one is a `he-domain` decision nobody has taken, which is why no worked
   case exercises the allowance.
8. **The 5% doctorate supplement and pro-rating.** §36(ד)(2) says "of his combined salary in the
   table" — three words that put the base on the table salary rather than the gmul base, and an
   assertion pins that. Whether the 5% is itself pro-rated to the post is stated nowhere; it is
   computed here from the already-pro-rated combined salary, and the code says so.

---

## 9. What the 41 new cross-checks are, and why they matter

Until integration, every assertion in `he-cases` compared quoted constants to each other — internal
relations the instruments themselves carry (the 2% seniority step, the 7.5% darga step, three annex
columns summing to their labelled post percentage), which arm of a two-arm rule wins, and cited
thresholds against a case's own datum. Good tests, but blind to the rules.

The final section of `he-cases`, `החיווט`, now puts each quoted constant against the rule that ought
to produce it: 8 table salaries, 7 `תוספת אופק 2022` amounts, 4 `תוספת שקלית 2016` amounts, 6 post
sizes and full-post hour counts, the doctorate supplement, 9 role-supplement rates, floors and caps,
and the `הבראה` day count. **All 41 pass.** That is two independent paths — a figure read off a
printed page by one encoder, and a rule written by another encoder reading a different instrument —
arriving at the same number, and it is the strongest evidence in the set that the transcription and
the rules agree.

The constants were **not** replaced by the calls. They stay as the expected side, exactly as the
original author's `מה נותר לחיווט` contract promised, so the printed evidence survives the wiring.
