# Ofek Hadash — the Hebrew re-voicing, notes

**Status: draft, not reviewed — and in two distinct senses, which must not be collapsed.**

1. The **law** here is not reviewed. No Israeli labour lawyer and no Ministry of Education
   payroll officer has read it against the agreements. Everything `../legalese/NOTES.md` § 8
   says about that applies to this file unchanged, because this encoding decides nothing that
   the English one does not decide.
2. The **Hebrew** here is not reviewed either, and that is a *second* gap with a different
   reviewer. Whether `רמת הסמכה` is the right collective noun for § 7's four statuses, whether
   `מזערי` or `מינימלי` is the word § 10 would want — these are judgements no mechanical check
   reaches. What has been checked is that the Hebrew lexes, parses, evaluates, and computes the
   same numbers. That is a claim about the *machine*, not about the language.

Law stated as at **7 September 2026**, from the same corpus commit as `../legalese`. Checked on
**17 September 2026** against the `l4` binary at `l4wt/ofek-build`.

**Re-labelled and re-homed 19 September 2026 (GM session, on Meng's word: AMBER).** This directory
was `legalese-he/` until today. It is a re-voicing of `../legalese` (§ 1), not an encoding taken
from the Hebrew instruments directly, and it is kept as a **derived reference, not as the Hebrew
encoding**. Meng's objection, which decided this: a Hebrew text encoded in English and re-voiced
into Hebrew is a photocopy of a photocopy; the pathway that scales is a pipeline run from the Hebrew
corpus straight into a Hebrew-canonical encoding. That run is owed and not yet made (brief VINYL,
2026-09-19); it deposits to `../legalese-he/`, and this directory is what it is checked against:
the 254 assertions for the numbers, and the 321 instrument-cited names in `GLOSSARY.md` for the
words. If the direct run agrees on both, this directory retires.

The 56 `@nlg` heralds are tagged `@nlg:he` as of today. `specs/todo/MULTILINGUAL-NLG-SPEC.md` § 3
(R-M2) makes an untagged annotation mean English, so the untagged Hebrew here would have declared
itself English the moment selection lands. Nothing selects on the tag yet (l4-ide PR #423 recognises
and preserves it), and the bare inline `[…]` form cannot carry one. When a module-level `@lang`
declaration lands, which Meng prefers, the 56 tags collapse to one line per module. Re-checked on
19 September 2026 with `check.sh` against an `l4` built at l4-ide `origin/unstable`
`ae74ae717` (2026-09-19): all nine modules `ok`, and `l4 nlg` renders no `:he` into prose, so the tag is consumed rather than leaked.

**This file is in English on purpose, and it is a choice that could go the other way.** Its
sibling `GLOSSARY.md` is in English, and its job is to be read *beside* `../legalese/NOTES.md`
by someone comparing the two encodings. The Hebrew is inside the `.l4` files, where the law is.
A reviewer who reads only Hebrew is therefore served by the modules and not by this note, which
is a real cost and is recorded here rather than defended.

**Section numbers are load-bearing.** Sixteen comments across seven modules cite `NOTES.md § 4`,
`§ 5` and `§ 6`, and they mean the same sections those numbers name in `../legalese/NOTES.md`.
Renumbering this file breaks those citations silently.

---

## 1. What this is

The **Hebrew sibling of [`../legalese`](../legalese)**: the same eight modules, the same rules,
the same 254 assertions, with every identifier and every comment in Hebrew.

It is a **re-voicing, not a re-derivation**. `../legalese` is the oracle. No number was
recomputed here, no rule was restructured, no assertion was added to or dropped from the eight
modules. If a figure in this encoding ever disagrees with the English one, this encoding is
wrong by construction, and the repair is here, not there.

Why bother. Israeli teachers' pay is stated in Hebrew, argued about in Hebrew, and administered
in Hebrew. An encoding a payroll officer or a union representative cannot read is an encoding
they cannot check, and an encoding nobody can check is an assertion. The point of the exercise
is the last mile: `שכר משולב` on the screen is the phrase on the page, and `גמול חינוך כיתה` is
what the § 39 supplement is actually called.

The secondary point is a language claim, and it is worth stating plainly because it was not
obvious in advance: **L4 takes Hebrew identifiers, Hebrew type names, Hebrew enum constructors,
Hebrew record fields, Hebrew mixfix and Hebrew section titles without a single accommodation in
the language.** The whole encoding is 2,759 lines of it. See § 5.5 for the one hard limit.

## 2. The source, and where the Hebrew words come from

The corpus is the same: **[מאגר אופק חדש](https://morimovilimcatala.github.io/ofek-hadash-corpus/)**,
282 documents, whose own caveats `../legalese/NOTES.md` § 2 reproduces and which are adopted here
without softening.

For this encoding the corpus does a second job. **A Hebrew name was taken from an instrument
wherever an instrument had one**, and `GLOSSARY.md` records, per identifier, which document and
which article the word came from. Measured over the 408 glossary entries:

| provenance | count | what it means |
| --- | --- | --- |
| `corpus` | 321 | the word appears in an instrument, and the note says where |
| `composed` | 79 | no instrument names this thing; the note says why, and what was composed from |
| `keep` | 8 | deliberately not renamed — see § 5.4 |

The 79 composed names are where a reviewer's time is best spent, because they are the ones a
reader of the agreement will not recognise. Ten of them are flagged individually in
`GLOSSARY.md`'s "Open questions", summarised at § 9 below.

## 3. What is encoded

**Nine modules. 321 assertions, all passing** — the eight oracle modules carrying 254, and one
Hebrew-only module carrying 67.

| module | what it carries | asserts |
| --- | --- | --- |
| `ofek-domain.l4` | the ontology every other module reads | 6 |
| `ofek-salary-table.l4` | both combined-salary tables, the frontier, the printed step rates | 47 |
| `ofek-placement.l4` | §§ 36–38 — entry, seniority, promotion, rank quotas | 37 |
| `ofek-worktime.l4` | §§ 14–33 — the 36-hour week, age reductions, § 31's hourly value | 41 |
| `ofek-supplements.l4` | § 39 supplements, the 2022 floors, Tosefet Ofek 2022, § 22 | 37 |
| `ofek-fiscal-2025.l4` | the 2025–2026 wage reduction | 37 |
| `ofek-pay.l4` | the assembly: a month's pay, and the value of an hour | 0 |
| `ofek-cases.l4` | three teachers computed end to end | 49 |
| `ofek-luach.l4` | **Hebrew-only.** The calendar library — see § 8 | 67 |

Run everything with `./check.sh`, which lists the nine in dependency order and pins
`JL4_LIBRARY_PATH` to the worktree the binary came from. It takes about 18 seconds.

**`check.sh` greps for `DiagnosticSeverity_Error` rather than trusting the exit code**, because
`l4 run` exits 0 on a *failed* assertion. A green exit status is not evidence here; the grep is.

## 4. What is NOT encoded

Read this before relying on any answer.

**Everything `../legalese/NOTES.md` § 4 excludes is excluded here, identically** — seniority and
rank as inputs (F4, F5), non-academic teachers placed in the BA table (F6), the conversion
chapters §§ 43–50 and 54–61 (F7), everything but primary and junior-high classroom teaching
(F8), and the 205 circulars, which are registered rather than encoded. This encoding adds no
coverage and removes none.

**What is additionally not here, relative to `../legalese`:**

- **`ofek-catala.l4` and the whole `catala/` export are not translated, and should not be.**
  See § 7 — it is the one part of the English row where translating would make things worse
  rather than better.
- **`registers/` is not duplicated.** The document register (282 rows, one per instrument) is a
  map of the corpus, not part of the encoding, and a second copy would be a second thing to keep
  in step. Read `../legalese/registers/`.
- **`README.md`, `SOURCE-LICENSE.md` and `encoding.json` are not duplicated**, for the same
  reason. The licence position of the source documents does not change with the language of the
  encoding.
- **`source/` carries only what this encoding generates**: `tables.py` (byte-identical to the
  English copy — it emits numbers, so there is nothing in it to translate), `_tablefmt.py`
  (translated), `build-salary-table-module.py` (translated) and `_salary-table-tail.l4`. The
  Catala toolchain — `build-catala-module.py`, `run-catala.sh`, `wrap-catala.py`, `_fixtures.py`
  — is absent, following § 7.

**And one thing that is here but wired to nothing: `ofek-luach.l4`.** No module imports it. It
type-checks, its 67 assertions pass, and it is dead code today. § 8 says what it is for and what
would have to happen for it to earn its place.

## 5. Things worth knowing before reading the code

§§ 5.1 to 5.3 of `../legalese/NOTES.md` — that the table's 224 distinct cells are generated by
the two rates printed in its own margins (F11), that half a post is not half the pay, and that
the **agorot** printing of 14 January 2025 is the text in force rather than the shekel printing —
are all true of this encoding in the same words, because it carries the same numbers. They are
not restated. What follows is what is different *because* it is Hebrew.

### 5.1 The tables are generated, and Hebrew is the reason they had to be

`ofek-salary-table.l4` is emitted by `source/build-salary-table-module.py`. It is **not** a hand
translation of the English module, and it could not have been.

The tables are written with **ditto carets**, and a caret resolves by *exact source column* — it
copies whatever token sits above it. Hebrew names are not the width of their English
counterparts, so translating `the seniority` to `הוותק` moves every column in the grid: the ruler
comment, the constructor, `OF`, `THEN`, and all nine amount columns. `_tablefmt.py` computes
every one of those widths from `len(SUBJ)` and `len(CTOR)`, so translating those two constants
moves the whole grid together and keeps the carets under what they mean to copy.

This matters more than a formatting preference, because of the asymmetry
`../legalese/NOTES.md` § 9.2 records: **a caret that resolves to nothing fails loudly, and a
caret that resolves to the wrong token fails silently** — you get the neighbouring rank's money,
zero errors, exit 0. A hand translation would have had to recompute 36 rows × 2 tables of
padding with no diagnostic if it got one wrong.

`source/_tablefmt.py` is a **copy** of the English file rather than a shared import, because the
English one is also read by `build-catala-module.py`, which stays English (§ 7). Translating it
in place would have changed that generator's output too.

The claim that this works is not taken on trust: § 10 records a 648-cell differential run
against the corpus parse, on both encodings independently.

### 5.2 Hebrew column widths are the lexer's widths

`_tablefmt.py` uses Python's `len()` to compute columns, and L4 counts source columns in
codepoints. Hebrew as written here is one codepoint per character and carries no combining
marks — no niqqud, no combining cantillation — so the two measures agree. **This would stop
being true if vowel points were ever added to an identifier**, and the failure would be a
mis-aligned ditto caret, i.e. the silent kind. Do not point a table.

### 5.3 Definiteness does the work English gets from articles

L4 needs the type, the record field and the free parameter to be three distinct strings. English
gets that for free from `a stage of education` / `stage of education` / `the stage`. Hebrew gets
it from the definite article and the construct state:

| role | form | example |
| --- | --- | --- |
| type, enum constructor | indefinite | `שלב חינוך`, `מורה`, `טבלת שכר` |
| record field | definite construct | `שלב החינוך`, `ההסמכה` |
| free parameter, function | definite head | `השלב`, `המורה`, `הטבלה` |

This is not decoration. It is the mechanism that keeps 413 identifiers distinct, and it is why
the convention is stated in `GLOSSARY.md` rather than left to each translator.

### 5.4 What is deliberately left in Latin script, and why

Eight identifiers. Seven are the module names in `IMPORT` — **filenames stay ASCII**, because
macOS normalises filenames (NFC/NFD) and a Hebrew filename risks breaking import resolution.
The eighth is `is before`, defined in the imported `daydate` library at `daydate.l4:738`:
renaming it would simply not resolve.

Beyond those, the only Latin text in the operative code is L4's own keywords, the prelude and
`daydate` names `ROUND`, `EMPTY`, `BELOW`, `map`, `max`, `DATE_YEAR`, `DATE_MONTH`, `add years`,
`add months`, `is after`, and the Latin sub-paragraph letters inside article citations —
`סעיף 36(e)`, `סעיף 38(c)(5)` — which are discussed at § 9, open question 1.

### 5.5 The one hard limit: no bidi control characters, ever

RLM (U+200F), LRM (U+200E) and the embedding/isolate marks (U+202A–U+202E, U+2066–U+2069) are a
**lex error inside backticks** — `expecting printable char except backticks`. They must never
appear in a `.l4` file. Display order is the viewer's business, decided by the Unicode
bidirectional algorithm from the characters themselves.

Everything else that was wanted works: geresh `׳` (U+05F3), gershayim `״` (U+05F4), maqaf `־`
(U+05BE), the em dash, ASCII digits, parentheses and hyphens, and the genitive `'s` after a
Hebrew name. `l4 format` round-trips Hebrew byte-identically.

The practical consequence for anyone editing these files: **mixed-direction lines look wrong in
an editor and are right in the file.** A line reading `#ASSERT \`תא תואר ראשון\` 11 4 EQUALS 9_172`
will render its numbers and its Hebrew in an order that depends on the viewer. Do not "fix" it
by inserting a mark. Check the file with `grep -P '[\x{200E}\x{200F}]'` instead, which is what
§ 10 does.

### 5.6 Gender

Identifiers are masculine, which is what the agreements use and what their own § 2 licenses
("בכל מקום בהסכם זה בו דובר בלשון זכר, הכוונה גם ללשון נקבה"). The three case fixtures —
`יעל`, `דבורה`, `נעה` — take feminine agreement in their own section titles, because they are
named women.

## 6. Three worked payslips

`ofek-cases.l4` computes the same three teachers as `../legalese/ofek-cases.l4`, from the same
49 assertions, to the same figures: **Yael** (`יעל`) at 11,008.03 on a full post and 6,004.38 on
half of one; **Dvora** (`דבורה`) at 18,300.50 before 1.9.2026 and 18,900.50 after it; **Noa**
(`נעה`) at 5,000.99 with 211.00 of § 36(d)(2) doctorate uplift. The narrative
`../legalese/NOTES.md` § 6 gives is not repeated; the numbers are identical and were verified
identical (§ 10).

## 7. Why there is no Catala export here, and why that is the right answer

`../legalese/ofek-catala.l4` is a **generated** module, emitted by `build-catala-module.py` and
compiled onward to `catala/ofek_hadash.catala_en` — which typechecks under catala 1.2.1 and runs
six worked cases.

Translating it would be wrong on three counts, in increasing order of how much it would cost:

1. **It is generated.** Hand-translating a generated file produces a file nobody dares
   regenerate — the exact failure `build-salary-table-module.py`'s own header warns about.
2. **Its target is English.** `catala_en` is Catala's English surface syntax. A Hebrew L4 module
   lowered through it produces Hebrew scope names inside English Catala keywords, which is a
   third language nobody reads. Catala has other localisations; adopting one is a project, not
   a translation.
3. **It would fork the oracle.** The English `ofek-catala.l4` is tied to `ofek-cases.l4` by
   assertion: the figures the generated module asserts are the figures the cases module asserts,
   so if the two drift, one goes red. A Hebrew second copy would be a third thing in that
   relationship with nothing tying it in.

So the Catala route runs once, in English, over numbers this encoding shares. That is a
deliberate asymmetry between the two encodings and it is recorded here so that its absence is
not read as an oversight. `../legalese/NOTES.md` § 7.3 records the two upstream findings that
came out of it, including [smucclaw/l4-ide#958](https://github.com/smucclaw/l4-ide/issues/958);
neither is Hebrew-specific.

## 8. The date library, and what has not adopted it

`ofek-luach.l4` — *luach*, `לוח`, a calendar — collects the date arithmetic that the other
modules perform inline and gives it names. It is built on `daydate` and rests on three facts the
agreements state:

- the school year opens **1 September** (§ 44(b)(4), (b)(5), in terms) and is named for the year
  it opens in, so "שנת הלימודים 2024" runs 1.9.2024 to 31.8.2025;
- it closes **31 August** — not defined in any definitions article, but treated as the last day
  of the employment year by the follow-up committee decision of 19.9.2010;
- **age is measured on 31 December**, not on a birthday (§ 26(d)). A teacher who turns 55 in
  March is entitled from the preceding 1 September; one who turns 55 the following February is
  not entitled that year. This is the rule most easily got wrong by hand.

It also carries a `daydate` caveat rather than hiding it: **smucclaw#961** — `the month before`
is silently wrong in January. The module does not use it, builds every date from components with
`YMD`, and relies on `daydate`'s month arithmetic only through `add years` inside `הגיל בתאריך`,
where the January boundary and 29 February are both asserted explicitly.

**Nothing imports it.** That is the honest state of it, and it is a defect, not a design.

### 8.1 What ought to adopt it

In rough order of how much it would buy:

| site | today | with `ofek-luach` |
| --- | --- | --- |
| `ofek-worktime.l4` § 26 | `הגיל ביום 31 בדצמבר של שנת הלימודים` is a bare `NUMBER` **input** | `הגיל ביום 31 בדצמבר של שנת הלימודים עבור` derives it from a birth date and a school year |
| `ofek-fiscal-2025.l4:98` | § 9(a)/(b)'s two windows as a hand-rolled `BRANCH` over `is before` and `AT MOST` | `התאריך חל בתקופה שבין`, which is exactly that predicate |
| `ofek-supplements.l4` (4 sites), `ofek-fiscal-2025.l4` (2 sites) | `daydate`'s `is before` applied directly to threshold dates | the same, named |
| `ofek-supplements.l4:276-278`, `ofek-cases.l4:24-27` | fixture dates written `MEANS YMD 2024 9 1` | `היום הראשון של שנת הלימודים` of a school year |
| `ofek-placement.l4` | seniority is a bare `NUMBER` | `הוותק הצבור בשנת הלימודים`, which makes the 31.8 / 1.9 step observable |

**Why none of it has been done.** Every one of those edits would make this encoding structurally
diverge from `../legalese`, and structural identity is currently what *proves* this encoding
correct — see § 10, where the two are shown to be token-for-token identical once identifiers and
prose are blanked. Adopting `ofek-luach` unilaterally would retire that differential and replace
it with nothing.

**So the adoption order is: English first.** Build the equivalent library in `../legalese`,
adopt it there, then mirror the change here and re-run the skeleton differential. Doing it the
other way round costs the only cheap check this encoding has.

One name-collision hazard, already avoided and worth not re-introducing: `ofek-worktime.l4`'s
parameter is `הגיל ביום 31 בדצמבר של שנת הלימודים` and `ofek-luach.l4`'s function is the same
string plus `עבור`. The glossary disambiguates them deliberately. If the parameter is ever
replaced by the function, the `עבור` is what keeps the import resolvable.

### 8.2 The Hebrew calendar section is a label, not a conversion

`§ לוח השנה העברי — תווית בלבד` returns the Hebrew year *number* of a school year, by adding
3761 to the opening year. **It is not a calendar conversion and must not be used as one.** The
school year opens on 1 September, which is before Rosh Hashanah: on 1.9.2025 the Hebrew date is
still 5785, while the school year is called תשפ״ו (5786). The function gives the name the
agreements use for the year, not the Hebrew date of any day in it.

It is deliberately disconnected from the pay path — no function returning a date or an amount
calls it — and it is asserted against the two instruments that print such a label (2022 § 22.1
"שנת הלימודים תשפ״ו (המתחילה ביום 1.9.2025)", and 2026 § 19's replacement of it by תשפ״ז).

## 9. The glossary, and the open questions it leaves

`GLOSSARY.md` and `glossary.json` are the same table in two forms: every identifier in the
English encoding, with the Hebrew name this encoding uses for it. They were written **before**
the translation, as a contract for five agents working in parallel, which is why the conventions
read as rules rather than as observations. The ones that most affect a reader:

- **Article citations keep their printed English form.** `section 36(e)` becomes `סעיף 36(e)`,
  not `סעיף 36(ה)`.
- **Never end an identifier with a one-letter Hebrew particle.** An identifier applied to an
  argument is followed by a space, so a name ending in `ל`/`ב`/`מ`/`ש`/`כ`/`ו`/`ה` renders as
  `… ל המורה`, which is not Hebrew. Function names end in a standalone word: `עבור`, `של`,
  `לפי`, `בטבלה`, `בתאריך`.
- **Two instrument synonyms are split by role.** The agreement uses `היקף משרה` (§ 27) and
  `חלקיות משרה` (§ 27(g)) interchangeably; the encoding needs two names, so the record field is
  `היקף המשרה` and the threaded parameter is `חלקיות המשרה`. Both are the agreement's words. Do
  not swap them.
- **"Step" is two things and gets two words.** In `ofek-salary-table` a step is a printed margin
  percentage (`שיעור העלייה בוותק של`); in `ofek-fiscal-2025` § 16 it is the annual increment the
  reduction withholds (`קידום הוותק`). They must not converge.

**Ten questions are open, and they are decisions rather than defects.** They are listed in full
at the end of `GLOSSARY.md`; the two that most deserve a ruling:

1. **Latin or Hebrew sub-paragraph letters in citations (open question 1).** This encoding writes
   `סעיף 36(e)`, `סעיף 38(c)(5)`, `סעיף 38(i)`. The instruments themselves write `(ה)`, `(ג)(5)`,
   `(ט)`. The argument for Latin is that a citation then greps identically across the English
   encoding, this one, the comments and the glossary; the argument for Hebrew is that it is what
   the page says. It affects 5 identifiers and many comments, and it can be swept mechanically
   **because it is uniform now** — which is the only reason to keep it uniform while it is
   undecided. **Meng should rule.**
2. **`the teacher worked normally on 4 May 2025` (open question 5).** The 2026 agreement's § 24
   is damaged in the corpus transcription exactly where the date would be: the text reads
   `שננקטו ביום` and then breaks to the next page. The English encoding names 4 May 2025 and this
   encoding carried that date over **without being able to confirm it against the instrument**.
   This one is worth checking against the scan before anyone relies on the § 24 rule.

The remaining eight concern composed terms — `רמת הסמכה` for the qualification ladder, `מזערי`
against the instrument's own `מינימלי`, the plene spelling `ביטחון` against § 39(a)(7)'s
defective `בטחון`, the five enum type names the instruments list members of without naming, the
all-Hebrew rendering of the tables' own mixed-script `תואר BA` headings, `שנת ההתמחות` as a blend
of § 37(a)'s `תקופת ההתמחות` and § 7(i)(2)'s `שנת סטאז׳`, the frontier and step vocabulary which
has no counterpart in any instrument at all, and the three fixture names.

## 10. How this was checked

Independently, by a session that did not write any of the modules, on 17 September 2026. Stated
as measurements rather than as a verdict, so that a later reader can re-run them.

| check | result |
| --- | --- |
| `./check.sh`, all nine modules | 0 `DiagnosticSeverity_Error` lines; exit 0 |
| assertion outcomes across all nine | **321 satisfied, 0 unsatisfied, 0 warnings** — every diagnostic emitted by the whole encoding is `Information: assertion satisfied` |
| `#ASSERT` count, per module, EN vs HE | **identical in all eight**: 6 / 47 / 37 / 41 / 37 / 37 / 0 / 49 = **254 = 254** |
| numeric literals, operative code, per module | **identical multisets in all eight** (954 literals each) |
| structural skeleton — comments dropped, every backticked identifier replaced by a placeholder, annotations collapsed | **token-for-token identical in all eight modules**, 1,486 lines each side |
| article citations (`§ n`, sub-parts) | 369 of 370 match; the single difference is § 10.1 below |
| Latin-script identifiers in Hebrew code | **zero** untranslated. The residue is L4 keywords, the seven ASCII module names, `daydate`/prelude names, and Latin sub-paragraph letters inside citations — all of which § 5.4 accounts for |
| bidi control characters, all `.l4`, `.md`, `.sh` and `source/` files | **zero**, and zero Unicode `Cf` characters of any kind |
| glossary coverage | **408 of 408** entries used; **zero** Hebrew identifiers invented outside the glossary |
| `ofek-salary-table.l4` regenerated from its generator | **byte-identical** to the committed file (`OFEK_CORPUS=… python3 source/build-salary-table-module.py \| diff -` → empty). Not hand-edited |
| `source/tables.py`, EN vs HE | byte-identical, md5 `79ff2092…` — one place where a number enters, shared |

Two differentials were run beyond comparing the files, because file identity does not prove that
a **ditto caret resolves to the same token** in a grid whose columns have all moved (§ 5.1) —
that is the silent failure, and the one a diff of the two encodings cannot see.

- **F11, the 648 salary cells.** A probe asserting every cell of both tables against the value
  parsed out of the 14 January 2025 corrected appendices was generated from `tables.py` and run
  against **each encoding independently**: **648 satisfied, 0 errors, in both.** The Hebrew grid
  therefore reproduces the corpus, not merely the English file. The 21 in-module step assertions
  that constitute the F11 property proper — base cell × printed margin rate lands within 0.011 of
  the next printed cell, across both tables, at ranks 1–9 and seniorities 1–36 — are present in
  the Hebrew module verbatim and pass.
- **The § 15 / § 17 working-week tables**, which are the other dittoed grid: 72 assertions over
  both stages and eight grade sizes, run against each encoding. **72 satisfied, 0 errors, in
  both.**

Both probes were deleted afterwards. Nothing was committed; the whole directory is still
untracked in `canon`.

**What none of this establishes.** That the Hebrew is good Hebrew, that a composed term is the
term a practitioner would use, that the article a comment cites says what the comment says it
says, or that the underlying English encoding is a correct reading of the agreements. The first
two need a Hebrew-reading reviewer, the third a reader of the instruments, and the fourth is
`../legalese/NOTES.md` § 8, unchanged.

### 10.1 One citation lost its sigil

`ofek-salary-table.l4:12` writes `בסעיף 4.1 להסכם הקיבוצי` where `../legalese/ofek-salary-table.l4:13`
writes `§ 4.1 of the collective agreement`. It is in a header comment, the citation is intact and
greppable as `4.1`, and the Hebrew word `סעיף` is the encoding's normal rendering of "section" in
prose. But it is the **only one of 501 `§` sigils** that does not survive as a sigil, so it is
recorded rather than left for someone to rediscover as a discrepancy. Either form is defensible;
uniformity is the thing worth having, and open question 1 is the place it gets ruled.

## 11. What review would mean

Everything at `../legalese/NOTES.md` § 8 — settling forks F1, F3 and F9, and checking the three
worked payslips against an actual payslip — applies unchanged, and is a review of the **law**,
which this encoding shares rather than restates.

This encoding adds a second review, of the **Hebrew**, and it needs a different reader: someone
who works with these agreements in Hebrew, who would go through `GLOSSARY.md`'s 79 composed
terms and its ten open questions, and say which of them a payroll officer or a union
representative would actually recognise. That review has not happened, and until it does the
Hebrew here is *checkable* — it runs, and it computes the right numbers — without yet being
*checked*.
