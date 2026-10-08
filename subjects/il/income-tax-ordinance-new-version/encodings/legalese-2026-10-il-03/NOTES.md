# NOTES — il/income-tax-ordinance-new-version, encoding row `legalese-2026-10-il-03`

Income Tax Ordinance [New Version], **s 120B** (indexation), **s 121** (the individual's rate of tax) and **s 121B** (additional tax on high incomes), encoded in L4 by one agent in one session (run `IL-03-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**. Version **0.2.0** (2026-10-08): repairs of the independent pass's two observations (O1, O2) and seven riders (BACKLOG IL-16); one helper's answer for 2025 is now declined, a silent 2028 answer is now declined by name, and four names were renamed; see "Version 0.2.0" below.
No domain expert has read it against the source; HG1 has not been sought.

## Version 0.2.0 (2026-10-08): repairs (BACKLOG IL-16)

Backlog row IL-16 (job C in `l4-pipeline/findings/il-2026-10-08/jobs.txt`), repair agent `rep-il-16`, one session, no sub-agents, on Meng's request of 2026-10-08 to fix the unrepaired findings, as the lead relayed it.
Item ids are those of `l4-pipeline/findings/il-2026-10-08/inventory.tsv`.
Nothing below was deleted; entries this version touches are marked **(0.2.0)** in place.
The section "Comparison with Axiom's RuleSpec", `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` are untouched.
Line numbers that those three cite in the `.l4` files are lines of version 0.1.0 (the comparison names each module's sha256); this version moves some of them.

| item | class | files | what changed |
| --- | --- | --- | --- |
| 03-O1 | OURS-WRONG | `ito-121b-additional-tax.l4`, `ito-il03-tests.l4` | the two s 121B(e) helpers decline 2025 (and earlier) with the section's own refusal, as its rule does; one expected value changed, six added |
| 03-O2 | OURS-WRONG (silent) | `ito-il03-nouns.l4`, `ito-120b-indexation.l4`, `ito-il03-tests.l4`; `tests-independent.l4` line 310 (as the lead authorised) | `amount on 1 January 2024, before rounding` is a MAYBE NUMBER; 2028 with NOTHING is declined by name; five assertions added, three inputs wrapped in `JUST` |
| 03-F7 | WORDING | `NOTES.md`, `encoding.json` | fork F7 answered from s 7 of the enacted 5786 Law; assumption A3 cites its ss 5-6; no answer changed |
| 03-721 | NOT-ENCODED (data) | new `ito-il03-published-figures.l4`, `ito-il03-tests.l4`, `NOTES.md`, `encoding.json` | the Tax Authority's 721,560 for 2026, carried as a published figure, not law; six assertions added |
| 03-W1 | WORDING | `NOTES.md`, `encoding.json` | "the independent test pass was not run" marked stale |
| CHK-03 | WORDING | `check.sh`, `encoding.json` | `expected_refused` added; the tester's 6 failed and 2 refused declared line by line; `check.sh` exits 0 |
| 03-T1 | TESTER-WRONG | `check.sh`, `NOTES.md`, the lead's note at the end of `tests-independent.l4` | annotated: F02 and F03 (`tests-independent.l4` lines 285, 286) stay failing, values unchanged |
| 01-W5 (IL-03 half) | WORDING | `ito-il03-nouns.l4`, `ito-120b-indexation.l4`, `ito-il03-tests.l4`; `tests-independent.l4` lines 315, 317, 351, 352 (as the lead authorised) | "pension point" renamed "allowance point" in three names (the lead's choice, assumed, not ruled); no answer moved |
| 03-N4 (IL-03 half) | WORDING | `ito-il03-nouns.l4`, `ito-121-individual-rates.l4`, `ito-121b-additional-tax.l4`; `tests-independent.l4` lines 167, 172 (as the lead authorised) | `A problem with the facts` renamed `A problem with the facts, for sections 121 and 121B`; no answer moved |

### 03-O1: the 2025 residential threshold, answered by a helper and refused by the rule

Recorded at `INDEPENDENT-FINDINGS.md` line 81 (observation O1); class OURS-WRONG.
In 0.1.0 `the text fixes the residential-apartment sale value for tax year` was TRUE for 2025 and 2026, and `the residential-apartment sale value in section 121B(e) for tax year` answered 5,385,285 for 2025, while `the additional tax under section 121B for` declines every year before 2026 at its first arm.
So the note on line 4462, "(נקוב לשנת 2025; בשנת 2026, 5,385,285 ש״ח)", was read as answering 2025 by the helpers and as not answering it by the rule.
The note says what the figure is in 2025; it does not say that s 121B as amended in 5785 reaches tax year 2025, and the deposited text does not say from when that amendment applies (assumption A1, question 4; amendment 276, Sefer HaChukim 3342, is not deposited, BACKLOG IL-31).
The inventory's other option, letting the rule answer 2025, waits on that deposit (03-S13) and was not taken.
Both helpers now decline 2025 and earlier with the section's own refusal, "section 121B for tax years before 2026 is not encoded in this model" (`ito-121b-additional-tax.l4` lines 77-80 and 99-104).
The predicate answers TRUE for 2026 and FALSE from 2027; the threshold answers 5,385,285 for 2026 and declines from 2027 under RE Law s 9(c2), as before.
The section's rule reaches neither helper before 2026, so none of its answers moves, and the tester's S25 (`tests-independent.l4` line 384) is refused as before.

### 03-O2: a rounded 2024 figure silently accepted for 2028

Recorded at `INDEPENDENT-FINDINGS.md` line 86 (observation O2) and at line 350 of this file as it stood at 0.1.0; class OURS-WRONG (silent).
For 1 January 2028, s 120B(e)(2) adjusts "הסכומים כפי שהיו ביום כ׳ בטבת התשפ״ד (1 בינואר 2024) טרם עיגולם" (line 4345), the amounts as they were on 1 January 2024 before rounding.
The Tax Authority publishes the rounded figures. In 0.1.0 the record `An amount on 1 January of a tax year` required a NUMBER before rounding, so a caller who held only the rounded figure had to put something there, and the rounded figure gave a plausible 2028 amount with exit 0.
As the inventory proposed, the field `amount on 1 January 2024, before rounding` is now a `MAYBE NUMBER` (`ito-il03-nouns.l4` line 153).
`s 120B — the amount for the tax year` reads it only for 2028, and on `NOTHING` declines by name: "section 120B(e)(2) adjusts the 1 January 2024 amount before rounding, and that amount was not supplied" (`ito-120b-indexation.l4`, a new refusal above the dispatcher; the 2028 arm is now a `WHERE` binding, `the 2028 adjustment`).
`s 120B — the amount in force in the tax year` reaches the same refusal first, because it must have the amount before it asks for the rounding Order.
The frozen years 2025-2027 read only the figure after rounding, and 2029 on reads the previous year's base, so they answer as before with `NOTHING` in the field.
The capstone's adapter (`il07-adapter-il03.l4` line 114) passes a polymorphic named refusal into this field; that still typechecks against a `MAYBE NUMBER` and is never forced for 2025-2027, so it needs no change, though job IL-22 may prefer to pass `NOTHING`.
The tester's file built the record with `IS before`, a NUMBER, which no longer typechecks (probed on a scratch copy: 1 error, no assertion run); the lead authorised changing that one line, 310, to `IS JUST before` (see "The tester's file" below).

### 01-W5 (IL-03's half): "allowance point", not "pension point"

Recorded at row IL-01's `NOTES.md` line 237 (as it stood before IL-01's own repairs of 2026-10-08), the capstone's `RECONCILE.md` line 56 (N13), and IL-01's comparison X06; class WORDING.
"נקודת קיצבה" (s 33A, line 1564) is now "allowance point" here, as row IL-01 renders it where s 33A defines it, and as row IL-08 (s 40) and IL-01's independent tester render it.
**The choice is the lead's, 2026-10-08, assumed, not ruled** (the inventory left it to the owner); the lead is telling `rep-il-14`, and IL-01 is not edited here.
Renamed, with no answer moved:

- the constructor `the amount of a pension point` → `the amount of an allowance point`;
- the record `A pension-point amount in a tax year` → `An allowance-point amount in a tax year`;
- the rule `s 120B(b) — the pension-point amount from the month of an agreed cost-of-living increment` → `s 120B(b) — the allowance-point amount from the month of an agreed cost-of-living increment`;
- and the section heading, comments and test fixture names that said "pension-point".

The tester's file uses the second and third names on lines 315, 317, 351 and 352, adapted as the lead authorised; its own fixture `a pension point of 1,000` keeps its name.
The comparison section below, which quotes the old names, is untouched.

### 03-N4 (IL-03's half): `A problem with the facts`, qualified

Recorded at the capstone's `RECONCILE.md` line 47 (N4); class WORDING.
Rows IL-03 and IL-06 both declared a type `A problem with the facts`, so no module could import both rows and name either.
IL-03's is now `A problem with the facts, for sections 121 and 121B`, after the sections whose rules return it (the style of RECONCILE's N3); its three constructors are unchanged.
It is named in `ito-il03-nouns.l4` (the declaration), in `ito-121-individual-rates.l4` lines 227 and 237, and in two signatures of `ito-121b-additional-tax.l4`, renames only.
The lead authorised the edit to `ito-121-individual-rates.l4`, which jobs.txt had listed as untouched; it is vendored by the capstone.
The tester's file names the type on lines 167 and 172, adapted as the lead authorised.

### 03-F7: fork F7, read against the enacted 5786 Law; assumption A3 re-based

Recorded at lines 131 (F7), 217 (question 3) and 373-374 (comparison, follow-up 2) of this file as it stood at 0.1.0, and at the capstone's `RECONCILE.md` lines 79-81; class WORDING.
The Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Year 2026), 5786-2026, Sefer HaChukim 3511 of 31 March 2026, is deposited at `../../registers/source-bundle/amending-laws/25_lsr_12235101.pdf` (commons a862cb5; sha256 `72244dba…4734155`, re-checked 2026-10-08).
Its chapter C, "ריווח מדרגות מס הכנסה", is on PDF p. 4 (printed Sefer HaChukim p. 416), read with `pdftotext` on 2026-10-08:

- **s 5** (amendment no. 288 of the Ordinance) amends s 121: in (a)(1) the figure becomes "301,200"; (a)(2) is replaced, "על כל שקל חדש מ־301,201 שקלים חדשים עד 560,280 שקלים חדשים - 35%"; in (b)(1)(c) the top becomes 228,000; (b)(1)(d) is replaced, "מ־228,001 … עד 301,200 … 31%". It leaves (b)(1)(a) (84,120), (b)(1)(b) (120,720) and every rate alone.
- **s 6**: "תחילתו של פרק זה ביום י"ב בטבת התשפ"ו (1 בינואר 2026) והוא יחול על הכנסה שהופקה או נצמחה ביום האמור או לאחריו" (in force on 1 January 2026, for income produced or accrued on or after that day). Chapter C is not marked a temporary provision (chapter D, on the same page, is), and s 6 gives no end date.
- **s 7**, headed "הוראת מעבר" (transitional provision): "לעניין תיאום הסכומים הנקובים בפרק זה לפי סעיף 120ב(ה) לפקודת מס הכנסה (בפרק זה - הסכומים), יראו אותם כאילו היו הסכומים המתואמים ליום כ' בטבת התשפ"ד (1 בינואר 2024)" (for the adjustment under s 120B(e) of the amounts stated in this chapter, they are regarded as if they were the amounts adjusted to 1 January 2024).

**F7's answer: reading (iii), which comes to (ii).**
For each amount s 5 states (301,200 in (a)(1) and (b)(1)(d), 560,280 in (a)(2), 228,000 in (b)(1)(c), and the band starts 301,201 and 228,001), the base that s 120B(e)(2) adjusts on 1 January 2028 is the figure s 5 states, not the figure the paragraph carried on 1 January 2024.
**Before or after rounding**, which the inventory asks: s 7 does not say in words.
It regards the stated figure as "the adjusted amount" on 1 January 2024, which is what s 120B(a) produces and what the rounding rules of (d) then round (line 4341: "כללים לעיגול סכומים שתואמו לפי סעיף זה"), so it stands where (e)(2) reads the amount "before rounding".
Read the other way, with "adjusted" meaning the adjusted amount as rounded, s 7 still supplies one figure and only one for each stated amount, so (e)(2) has no other figure to restart from.
Either way the 2028 base of each stated amount is the figure s 5 prints; and for 2026 and 2027 the figure in force is that same figure, by s 5 and s 6 directly.
For 84,120 and 120,720, which s 5 does not restate, (e)(2) restarts from their own 1 January 2024 amounts before rounding, which no deposited source gives (an input, as before).
**No answer in this row changes.**
s 121 from 2028 is still declined, now because the 2027 index readings and the rounding Order are not in this row, not because F7 was open; the refusal's words, "the section 121 ceilings from tax year 2028 are not determined by the deposited text", stay true.
The header of `ito-121-individual-rates.l4` (lines 22-23: the 1 January 2024 figures "which for the amended ceilings the deposited text does not give") and its `@ref` on line 62 are now out of date in that clause; this job may only rename in that module (03-N4, renames only, as the lead authorised), so they are recorded here and left for its next edit.
Fork F5 (2027's rise only) is unchanged: s 7 says what is adjusted, not by which index.
**A3**: for the four figures s 5 states, the basis is now the enacted Law, s 5 with s 6's commencement, and it agrees with the text exactly (the capstone found the same, `RECONCILE.md` line 79).
For 84,120 and 120,720 the basis is unchanged: the note at line 4350, the editorial tables at lines 4429-4447 (which show both figures unchanged from 2024-2025 to 2026-2027), and s 120B(e)(1).

### 03-721: the Tax Authority's 2026 figure for s 121B(a), carried as a published figure

Recorded at the capstone's `RECONCILE.md` line 82; class NOT-ENCODED (data).
New module `ito-il03-published-figures.l4`, labelled "NOT ENCODED LAW", modelled on IL-01's `ito-credit-points-published-figures.l4`.
It carries one figure, `the amount in section 121B(a) published by the Israel Tax Authority for tax year` 2026 = 721,560, and declines every other year by name ("no s 121B(a) amount published by the Israel Tax Authority for this tax year has been sourced in this encoding").
Source: the Tax Authority's 2026 monthly withholding booklet, recorded by link and hash in `../../registers/source-bundle/amending-laws/SOURCES.json` ("pointers_only") and not deposited.
Re-checked on 2026-10-08: a local copy of the Internet Archive capture (the capstone encoder's fetch) has the recorded sha256 `282bb886…6e86285`, and PDF p. 8 reads "יחיד אשר הכנסתו החייבת בשנת המס עלתה על ₪ 721,560 ( ₪ 60,130לחודש)" in `pdftotext -layout` with bidi controls removed (the extractor moves punctuation about).
The page is printed as page 8; the capstone's `il07-published-figures.l4` calls it "PDF p. 8 (printed page 7)", which is off by one (observation for job IL-22; the capstone is not edited here).
The same page prints the 2026 residential threshold as 5,385,285, the text's own figure; it is not carried, because the rule reads the text.
The s 121B rule still takes the amount as a required argument: the published figure is offered to callers and used by the tests, not read by any rule.
2025 and 2027 are not carried, though s 120B(e)(1) would give them the same figure: that is law applied to a published figure, and a test shows it (2027 through `s 120B — the amount in force in the tax year`) rather than the figures module asserting it.
Section 5's answer table now names the figure for 2026.

### 03-W1: "the independent test pass was not run"

Recorded at line 223 of this file as it stood at 0.1.0 (section 9); class WORDING.
Marked **(0.2.0)** in place: the pass was run after the line was written (commons a7f987f).
`encoding.json` `not_reviewed.note` said the same and is updated.

### CHK-03 and 03-T1: the tester's counts declared

Recorded at `check.sh` lines 29-34 and in `red-checks.txt` (CHK-03), and at `INDEPENDENT-FINDINGS.md` lines 57-62 (03-T1).
`check.sh` exited 1 at 0.1.0 because it did not list the tester's module and had no `expected_refused`.
It now has `expected_refused`, as IL-04's does, and lists `tests-independent.l4` with 6 failed and 2 refused, with a comment naming each line, its inventory id and class: lines 267-269 (D03-D05, 03-F2, AMBIGUITY), 284 (F01, 03-F1, AMBIGUITY), 285-286 (F02, F03, 03-T1, TESTER-WRONG), and refused 371 and 384 (S13, S25, 03-S13, AMBIGUITY, waiting on the deposit of amendment 276).
03-T1 is annotated there, here and in the lead's note at the end of the tester's file: by the tester's own account (`INDEPENDENT-FINDINGS.md` lines 57-62) F02's every placement gives 12,300 and F03's `LEFT` is the refusal meant; the encoding's answers stand and the two stay failing, their expected values unchanged.
`encoding.json` gains `expected_red`.

### The tester's file: seven lines adapted, one note appended

As the lead authorised on 2026-10-08, under the precedent of IL-04 v0.3.1, seven lines of `tests-independent.l4` were changed in place to follow the renamed interface, and nothing else: no expected value, no input, no fixture's own name.

| line | before | after | item |
| --- | --- | --- | --- |
| 167, 172 | `GIVETH AN EITHER` `A problem with the facts` `NUMBER` | the type `A problem with the facts, for sections 121 and 121B` | 03-N4 |
| 310 | `IS before` | `IS JUST before` | 03-O2 |
| 315, 317 | `A pension-point amount in a tax year` | `An allowance-point amount in a tax year` | 01-W5 |
| 351, 352 | `s 120B(b) — the pension-point amount from the month of an agreed cost-of-living increment` | `s 120B(b) — the allowance-point amount from …` | 01-W5 |

A dated "NOTE BY THE LEAD, 2026-10-08" is appended after the file's last line (lines 395-415, after a blank line) and lists each line and why; nothing was inserted above it, so every line the findings and `check.sh` cite still holds.
The first 393 lines differ from 0.1.0's only on those seven lines (checked by `diff`), and the file's counts are unchanged: 118 satisfied, 6 failed, 2 refused, on the same eight lines.

### Expected values changed or added (`ito-il03-tests.l4`)

Every value below was worked from the text, or from the published figure, before the assertion was run.

| assertion | 0.1.0 | 0.2.0 | why |
| --- | --- | --- | --- |
| `the residential-apartment sale value in section 121B(e) for tax year` 2025 | 5,385,285 | declined: "section 121B for tax years before 2026 is not encoded in this model" | 03-O1: s 121B is not answered for 2025 |
| the same, 2024 | — | declined, same refusal | 03-O1 (added) |
| the same, 2027 | — | declined: "… from 2027 moves under section 9(c2) of the Real Estate Taxation Law …" | line 4462 (added) |
| `the text fixes the residential-apartment sale value for tax year` 2025 / 2026 / 2027 | — | declined (before 2026) / TRUE / FALSE | 03-O1 (added) |
| `the betterment on` a residential sale for 5,385,286 `counts for section 121B in tax year` 2025 | — | declined (before 2026) | 03-O1 (added) |
| `s 120B — the amount for the tax year`, 2028, `NOTHING` before rounding (rounded 1,000; previous base 1,050; index 100 to 102) | — | declined: "section 120B(e)(2) adjusts the 1 January 2024 amount before rounding, and that amount was not supplied" | 03-O2 (added) |
| `s 120B — the amount in force in the tax year`, the same, 2028 | — | declined, same refusal | 03-O2 (added) |
| `s 120B — the amount for the tax year`, the same, 2026 | — | `fixed by section 120B(e)(1) at` 1,000 | (e)(1) reads only the rounded figure (added) |
| `s 120B — the amount in force in the tax year`, the same, 2026 | — | 1,000 | the same (added) |
| `s 120B — the amount for the tax year`, the same, 2029 | — | `adjusted, before rounding, to` 1,071 (1,050 × (1 + (102 − 100)/100)) | (a) reads the previous base (added) |
| `the amount in section 121B(a) published by the Israel Tax Authority for tax year` 2026 | — | 721,560 | booklet p. 8 (added) |
| the same, 2025 and 2027 | — | declined: "no s 121B(a) amount published by the Israel Tax Authority for this tax year has been sourced in this encoding" | only 2026 is sourced (added) |
| the published 2026 figure equals the editorial note's figure used above | — | TRUE (721,560 = 721,560) | (added) |
| `the additional tax under section 121B for`, 2026, a dividend of 1,000,000, at the published figure | — | `RIGHT` 13,922: (a) 3% × (1,000,000 − 721,560 = 278,440) = 8,353.2; (a1) 2% × 278,440 = 5,568.8 | (added) |
| `the amount in section 121B(a) in force, under section 120B, from` 2027, the published 2026 figure as the 1 January 2024 figure after rounding | — | 721,560 | (e)(1) (added) |

Inputs changed, values not: the before-rounding figures of three fixtures (`the hypothetical amount, in tax year`, 1,000.4; `the s 121B(a) amount, in tax year`, 721,563.7; and the new `… after rounding as published for 2026 …`, 721,563.7) are wrapped in `JUST`.
No other expected value changed; the 86 assertions of 0.1.0 are all still there, one with the new value above, and 17 were added (103).

### What `check.sh` prints at 0.2.0

Run on 2026-10-08 from 07:03:55Z to 07:04:11Z with `L4=/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset; the binary is `~/.local/bin/l4` → the cabal store, `/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-d4290e25/bin/l4`, sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`, the same before and after the run.
The 0.1.0 baseline was re-run on the same binary before any edit and printed 0.1.0's table with `tests-independent.l4` at 6 errors, 118 satisfied, 6 failed, 2 refused, exit 1.

```
module                                    errors satisfied  failed  refused  expected
ito-120b-indexation.l4                         0         0       0        0         0
ito-121-individual-rates.l4                    0         0       0        0         0
ito-121b-additional-tax.l4                     0         0       0        0         0
ito-il03-nouns.l4                              0         0       0        0         0
ito-il03-published-figures.l4                  0         0       0        0         0
ito-il03-tests.l4                              0       103       0        0         0
tests-independent.l4                           6       118       6        2       6/2
TOTAL (7 modules)                              6       221       6        2
(a failed assertion is also an error; any other error, or a refused assertion a module is not expected to have, makes the run red; "expected" is failed/refused where a module may refuse)
```

`check.sh` exit 0.
The six errors are exactly the six declared failures of the tester's file; its two refusals are declared.
`tools/srcquote.py` regenerates every `src:N` line of every module unchanged, and `tools/hebcheck.py` passes on every changed module, `check.sh` and `encoding.json` against the source.
Against the source alone it flags, in `ito-il03-published-figures.l4` and this file, only Hebrew quoted from the booklet and the 5786 Law; against a file of the source with the cleaned `pdftotext` of the Law's p. 4 and the booklet's pp. 1 and 8 appended, it passes.

### For job IL-22 (the capstone), names this version adds or renames

| kind | 0.1.0 | 0.2.0 | in vendored module | capstone users found |
| --- | --- | --- | --- | --- |
| type | `A problem with the facts` | `A problem with the facts, for sections 121 and 121B` | `ito-il03-nouns.l4`, used in `ito-121-individual-rates.l4`, `ito-121b-additional-tax.l4` | none by name: `il07-adapter-il03.l4` matches `LEFT p`; its comment on line 15 names the old type |
| field type | `amount on 1 January 2024, before rounding` IS A NUMBER | IS A MAYBE NUMBER | `ito-il03-nouns.l4` | `il07-adapter-il03.l4` line 114 passes a named refusal, which still typechecks |
| constructor | `the amount of a pension point` | `the amount of an allowance point` | `ito-il03-nouns.l4` | none |
| type | `A pension-point amount in a tax year` | `An allowance-point amount in a tax year` | `ito-il03-nouns.l4` | none |
| rule | `s 120B(b) — the pension-point amount from the month of an agreed cost-of-living increment` | `s 120B(b) — the allowance-point amount from the month of an agreed cost-of-living increment` | `ito-120b-indexation.l4` | none |
| refusal (new) | — | `section 120B(e)(2) adjusts the 1 January 2024 amount before rounding, and that amount was not supplied` | `ito-120b-indexation.l4` | — |
| behaviour | the two s 121B(e) helpers answer 2025 | they decline 2025 | `ito-121b-additional-tax.l4` | none call them |
| module (new, not vendored) | — | `ito-il03-published-figures.l4`: `the amount in section 121B(a) published by the Israel Tax Authority for tax year`, and its refusal | — | the capstone's own `il07-published-figures.l4` carries the same figure |

The four vendored modules that changed are `ito-il03-nouns.l4`, `ito-120b-indexation.l4`, `ito-121-individual-rates.l4` (renames only) and `ito-121b-additional-tax.l4`; the capstone's `vendor.sh --check` fails on them until IL-22 re-records.
"Users found" is from `grep` over the capstone's own `.l4` files on 2026-10-08.
Observation for IL-22: `il07-published-figures.l4` says the booklet's figure is on "PDF p. 8 (printed page 7)"; the page is printed 8.

## 0. What `check.sh` prints

**(0.2.0)** This is 0.1.0's run; the table at 0.2.0 is in "Version 0.2.0" above.

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, a local cabal build in store entry `jl4-0.1-0ee0100b`, modified 2026-10-06 21:20 (local), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`, and no record beside it names the commit it was built from.
It was rebuilt at 21:20, one minute before this directory was created; every run recorded here was made after that.

```
module                                    errors satisfied  failed  refused  expected
ito-120b-indexation.l4                         0         0       0        0         0
ito-121-individual-rates.l4                    0         0       0        0         0
ito-121b-additional-tax.l4                     0         0       0        0         0
ito-il03-nouns.l4                              0         0       0        0         0
ito-il03-tests.l4                              0        86       0        0         0
TOTAL (5 modules)                              0        86       0        0
```

`check.sh` exit 0.
The tests module has 86 `#ASSERT` directives and all 86 are satisfied; no failure or refusal is expected and none occurs.
The rule modules carry no assertions of their own.
To show the harness can fail, a scratch copy with six expected values deliberately altered was run: it reported 6 failed, 6 errors, exit 1.
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary chooses its embedded copies, and the warnings are not errors.

Two mechanical checks were run over every file, with the scripts in `tools/` (run them with `python3 -I`):
`tools/srcquote.py SOURCE FILE.l4…` regenerates every `-- src:N | …` comment from line N of the source file, reducing the wiki templates; `tools/hebcheck.py SOURCE FILE…` checks that every other run of Hebrew in the modules, the Markdown files and `encoding.json` occurs verbatim in the source (raw or template-reduced).
Both passed; the second fails on a planted non-source string.

## 1. What is encoded and what is not

**Encoded:** s 120B(a), (b), (d) and (e) as a mechanism over supplied index readings and supplied amounts; s 121(a) and (b) in full, with the figures the text prints, for tax years 2026 and 2027; s 121B(a), (a1), (b) and (e) in full, for tax years from 2026, with the (a) amount supplied by the caller.
The definitions those sections use are encoded as far as they need: s 1 "שיעור עליית המדד" and "סכום מתואם" as arithmetic; s 1 "הכנסה חייבת", "הכנסה מיגיעה אישית", "פנקסים קבילים" and "שנת מס" as the shape of the inputs.

**Not encoded:** s 121A (repealed; row IL-08); credit points, ss 33A-36A (row IL-01), which reduce the tax computed here; s 66 (row IL-02), which decides whose income an item is; the sections that charge particular income at rates of their own (ss 91, 122, 125B, 125C and others); s 8(c) spreading; the Real Estate Taxation Law (betterment, its inflationary amount, exemptions, s 9(c2) adjustment); and the Income Tax (Rules for Rounding Amounts) Order 5746-1986.
Each of these that feeds a provision in scope enters as an **input**, with its citation in the nouns module.

**No figure in this encoding comes from anywhere but the text.**
The consumer price index and every amount the Israel Tax Authority publishes are inputs with no default (section 7 says why nothing was fetched).
Figures that appear only in the consolidation's editorial notes are not encoded; the tests supply one of them (721,560) as a labelled scenario value.
**(0.2.0)** 721,560 is now also carried for 2026 as the Tax Authority's published figure, labelled as not law, in `ito-il03-published-figures.l4` (repair 03-721); the s 121B rule still takes the amount as an argument.

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt`.
Totals: **25 encoded, 4 inert, 1 out-of-scope, 0 deferred** (30 rows).

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 120B(a) | 4338 | adjust on 1 January by the rise in the index over the previous tax year | encoded | `s 120B(a) — adjust`, `s 120B — the amount for the tax year` |
| s 120B(b) | 4339 | pension-point amounts adjusted mid-year when a cost-of-living increment is agreed | encoded | `s 120B(b) — the pension-point amount from the month of …` **(0.2.0: renamed `s 120B(b) — the allowance-point amount from the month of …`, 01-W5)** |
| s 120B(c) | 4340 | (repealed) | inert | comment |
| s 120B(d) | 4341-4342 | the Minister's rounding power; the 5746-1986 Order is noted as made | encoded (as a named refusal: the Order is not in the sources) | `the rounding rules made under section 120B(d) are not encoded in this model` |
| s 120B(e) chapeau | 4343 | notwithstanding (a) and (b) | encoded | arm order in the dispatcher and in (b) |
| s 120B(e)(1) | 4344 | no adjustment on 1 January 2025-2027; the 1 January 2024 amounts after rounding | encoded | `s 120B(e)(1) — no adjustment in tax year` |
| s 120B(e)(2) | 4345 | on 1 January 2028, the 1 January 2024 amounts before rounding, by the 2027 index | encoded | `s 120B(e)(2) — adjust on 1 January 2028` |
| s 121(a) chapeau | 4350 | the tax on an individual's taxable income in the tax year | encoded | `the tax under section 121 for` |
| s 121(a)(1) | 4351 | first 301,200 at 31% | encoded | `s 121(a) — the tax on` |
| s 121(a)(2) | 4352 | 301,201-560,280 at 35% | encoded | same |
| s 121(a)(3) | 4353 | each further shekel at 47% | encoded | same |
| s 121(b)(1) chapeau | 4354 | notwithstanding (a)(1): income from personal exertion, and income of an individual who has reached 60 | encoded | `s 121 — the tax on … , of which eligible …`, `eligible for the reduced rates`, `aged 60 or more by the end of the tax year` |
| s 121(b)(1)(a) | 4355 | first 84,120 at 10% | encoded | `s 121(b)(1) — the tax at the reduced rates on` |
| s 121(b)(1)(b) | 4356 | 84,121-120,720 at 14% | encoded | same |
| s 121(b)(1)(c) | 4357 | 120,721-228,000 at 20% | encoded | same |
| s 121(b)(1)(d) | 4358 | 228,001-301,200 at 31% | encoded | same |
| s 121(b)(2) | 4359 | no reduced rates on income for which books were required and acceptable books not kept | encoded | `eligible for the reduced rates` |
| s 121, note: simulator | 4361-4362 | editorial link to the Tax Authority's simulator | inert | comment |
| s 121, note: tables 2019-2027 | 4364-4450 | editorial tables of brackets by year | inert (the 2026-2027 table is used once in the tests as a second transcription) | comment; tests |
| s 121A | 4452-4453 | (repealed) | out-of-scope | see below |
| s 121B(a) | 4456 | 3% on taxable income above 640,000 (as at 2017) | encoded | `s 121B(a) — the additional tax on`, `the amount printed in section 121B(a), as at 2017` |
| s 121B(a1) | 4457 | a further 2% on capital-source income above the same amount | encoded | `s 121B(a1) — the additional tax on` |
| s 121B(b) | 4458 | s 91(d) on advance payments does not apply | encoded (the one answer it gives) | `s 121B(b) — section 91(d) on advance payments applies …` |
| s 121B(c) | 4459 | applies notwithstanding any enactment | inert | comment: no other enactment is encoded here for it to override |
| s 121B(d) | 4460 | s 8(c) spreading applies in computing taxable income for s 121B | encoded (as an input convention) | `amount` is taken after s 8(c) spreading |
| s 121B(e) "הכנסה חייבת" | 4462 | s 1 and s 89 income, less inflationary amounts, plus betterment, with the residential-apartment limb | encoded | `the taxable income for section 121B of`, `the betterment on … counts …`, `the residential-apartment sale value in section 121B(e) for tax year` |
| s 121B(e) "הכנסה חייבת ממקור הוני" | 4463 | taxable income other than … | encoded | `from a capital source` |
| s 121B(e) cap. source (1) | 4464 | s 2(1)/(2) income excluded | encoded | same |
| s 121B(e) cap. source (2) | 4465 | other personal-exertion income excluded | encoded | same |
| s 120A "תקרות הכנסה" (used, not in slice) | 4335 | what "income ceilings" means for s 120B | encoded (as the record `The income ceilings of section 121`, and the reason the s 121B(a) amount is adjusted by s 120B) | nouns |

**s 121A, out of scope.**
The deposited text shows only "(בוטל)" (repealed) under the section number, with its amendment tags (5750, 5753, 5754).
Its former text is not in the source, so there is nothing here to encode but the fact of repeal, and that fact belongs to row IL-08, to which the lead has assigned s 121A: a repeal stub here as well would put two records of one provision in canon with nothing to keep them in step.
Its pre-repeal text could matter only to tax years in the early 1990s or before, and this row answers no tax year before 2025 (assumption A1).

## 3. Assumptions

**A1. The tax years answered.**
s 121: tax years **2026 and 2027** only.
s 121B: tax years **from 2026**, with the s 121B(a) amount supplied; a residential-apartment sale is answered only for 2026 (the text fixes that threshold for 2025 and 2026, and from 2027 it moves under a Law not encoded).
**(0.2.0)** The two s 121B(e) helpers now decline 2025 as well, so no name in the row answers s 121B for 2025 (repair 03-O1).
s 120B: adjustments **from 1 January 2025**.
Everything earlier is declined by a named `REFUSE`, and so is s 121 from 2028.
Why: the source is a consolidation "as amended at retrieval", and the three sections' amendment lists end in 5785 (ss 120B, 121B) and 5786 (s 121).
The text as it stood before those amendments is not in the sources, and answering an earlier year from the text as amended would borrow one vintage's figures for another.
For s 121 the 2026 boundary is also visible in the source's own aids: the editorial tables (lines 4429-4448) show the (a)(1)/(b)(1)(d) and (b)(1)(c) figures moving between "2024-2025" and "2026-2027".

**A2. The tax year is an explicit input, and the dated arms select on it.**
The skill's rule-effective-time axis (`RULES EFFECTIVE DATE`) was not used.
In this subject the question "which version of the law" is answered by the tax year whose income is being taxed, not by the date of evaluation: s 120B speaks of "1 January of each tax year", and the figures are stated per tax year.
Taking the year as a field of the case keeps it on the return where it belongs, and every dated arm (`BRANCH IF … tax year …`) carries its citation.

**A3. The figures printed in s 121 are the figures for 2026 and 2027.**
Basis: the consolidation's note at line 4350 ("(הסכומים מתואמים לשנים 2026–2027)"), the matching editorial table at lines 4441-4447, and s 120B(e)(1), under which no indexation intervenes in 2025-2027.
The consolidation's editors write adjusted figures into the text; the official base figures in the amending Laws could not be compared (section 7).
**(0.2.0)** Four of the six figures now rest on the enacted Law: s 5 of the 5786 Economic Efficiency Law states 301,200 ((a)(1) and (b)(1)(d)), 560,280 ((a)(2)) and 228,000 ((b)(1)(c)), and its s 6 commences them on 1 January 2026; 84,120 and 120,720, which s 5 does not restate, still rest on the basis above (repair 03-F7, in "Version 0.2.0").

**A4. Figures found only in editorial notes are not encoded.**
In particular the s 121B(a) amount for 2024-2027 (721,560) and for 2023 (698,280), and the s 121B(e) note that the residential threshold is 5,385,285 "in 2026" (that one is used only to say the printed figure holds for 2026, alongside the text's own figure).
The text of s 121B(a) prints 640,000 "nominal for 2017", the base s 120B indexes from; the figure in force is an input.
**(0.2.0)** 721,560 is still not encoded as law, but is carried for 2026 as the Tax Authority's published figure (repair 03-721).

**A5. Classifications outside the slice are inputs.**
Whether an item is from personal exertion; whether it is s 2(1)/(2) income; whether another section charges it at its own rate; whether books were required and acceptable books not kept; the s 88 inflationary amount; the betterment, its s 47 inflationary amount, the sale value and any exemption of a real-estate sale; which spouse's income an item is (s 66); and any s 8(c) spreading.
Each is recorded on a return or an assessment, so a caller can supply it (phrasebook 1.6, reading 1).

**A6. The s 121 result is the tax before credit points.**
Credit points (row IL-01) are deducted from it elsewhere.
s 121B is computed separately and is not added to it here.

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | s 121(b)(1), line 4354 | When an individual under 60 has both personal-exertion income and other income on the scale, which shekels of the scale does the eligible income occupy? | (i) the eligible income at the bottom; (ii) the other income at the bottom; (iii) pro rata | **(i)**. (b)(1)(a) speaks of "the first 84,120 shekels"; under (ii) those shekels would be other income and the reduced rates would never reach an individual with other income above 84,120, which empties (b)(1) for exactly the mixed case it names. Where the Ordinance does order income, it puts special-rate income at the highest step (s 91(b)(1), line 3347; s 125C(b), line 4530), which points the same way. Not settled by any text in the slice. |
| F2 | s 121(b)(1), line 4354 | "of an individual who has reached 60": tested when? | (i) at any time up to the end of the tax year; (ii) at the start of the tax year; (iii) only income derived after the 60th birthday | **(i)**: the provision attaches the age to the individual and the income to the tax year, and the year is the unit of assessment. (iii) would need the income split by date, which the text does not ask for. |
| F3 | s 121(b)(2), line 4359 | Does (b)(2) reach the over-60 individual's income that is not from personal exertion? | (i) yes, any income for which books were required and not kept; (ii) only personal-exertion income | **(i)**: the text says "income" without qualification. |
| F4 | s 120B(a), line 4338; s 1, line 180 | If the index falls, is the amount reduced? | (i) yes, the s 1 arithmetic gives a negative rate and it is applied; (ii) no, "עליית" (rise) means only rises count | **(i)**: the definition is a formula and yields a negative number on its own terms. The editorial tables show amounts falling from 2020 to 2021 (e.g. 75,960 to 75,480, lines 4382 and 4394), which fits (i); they are aids, not authority. |
| F5 | s 120B(e)(2), line 4345 | "the index in the previous tax year … shall be the index of tax year 2027": only 2027's rise, or the rise since 2024? | (i) 2027's rise only, so 2024-2026 inflation is not recovered; (ii) cumulative | **(i)**: it names one tax year's index, and (a)'s mechanism measures over one tax year. |
| F6 | s 120B(a) | Does the year-on-year chain carry rounded or unrounded figures? | (i) unrounded, rounding only the figure in force; (ii) rounded | **(i)**: (e)(2) restarts "before rounding", which is natural only if the chain runs unrounded. It changes no answer this row gives, because every rounded figure is either supplied or declined. |
| F7 | s 120B(e)(2) with s 121 as amended in 5786 | What is the 2028 base for the ceilings the 5786 amendment moved ((a)(1), (b)(1)(c), (b)(1)(d))? | (i) their 1 January 2024 figures, which would undo the 5786 change; (ii) the figures as amended; (iii) whatever the amending Law provides | **not answered**: s 121 from 2028 is declined by name. The amending Law could not be read (section 7). **(0.2.0) Answered: (iii), which comes to (ii).** Section 7 of the 5786 Law, now deposited, regards the amounts its chapter states as the amounts adjusted to 1 January 2024 for s 120B(e), so their 2028 base is the stated figure; see "Version 0.2.0", 03-F7. No answer here changes: s 121 from 2028 is still declined, for want of the 2027 index and the rounding Order. |
| F8 | s 121(a)(1), (b)(1)(d) | The text prints the top of the 31% band twice (301,200). If the two ever differ, which governs? | — | **declined**: a supplied set of ceilings in which they differ is refused; the printed figures agree, and a test says so. |
| F9 | s 121B(e), line 4462 | Does "and the sale is not exempt" govern only the residential limb? Is the s 47 inflationary amount excluded from a sale whose betterment does not count? | (i) the exemption condition is part of the residential limb only, and a sale that does not count contributes nothing; (ii) the exemption condition applies to all betterment; the inflationary amount is excluded from income generally | **(i)**: the condition sits inside the clause opened by "ואולם לגבי מכירת זכות במקרקעין בדירת מגורים"; subtracting an uncounted sale's inflationary amount from other income would tax less than the income. |
| F10 | s 121B(e), line 4462 | Which year's residential threshold applies to a sale? | (i) the tax year in which the betterment is counted; (ii) the date of the sale under the Real Estate Taxation Law's own calendar | **(i)**, the case's tax year; the two coincide for a sale in that year. |
| F11 | s 121B(a1), line 4457 | (a1) says "ממקורות הוניים" (plural); (e) defines "הכנסה חייבת ממקור הוני" (singular). | (i) the defined term; (ii) an undefined term | **(i)**. |
| F12 | s 1 "שנת מס", line 202 | A special assessment period. | — | **not modelled**: the tax year is a calendar year. Omitting the second limb can only mis-time a case that has one; nothing in this row would tell. |
| F13 | s 120B(e)(1), line 4344 | "שנות המס 2025 עד 2027": is 2027 included? | (i) inclusive; (ii) exclusive | **(i)**: (e)(2) restarts on 1 January 2028 from the 2024 figures by the index of 2027, which presupposes no adjustment on 1 January 2027; the notes at lines 4350 and 4456 agree. |
| F14 | s 121B(a), (a1), (e) | "עלתה על" / "עולה על" (exceeded / exceeds) at exactly the threshold. | — | **strict** (`GREATER THAN`). For (a) and (a1) the tax at the threshold is 0 either way; for the residential limb it decides whether the betterment counts, and a test sits on the boundary. |
| F15 | s 121B(e) cap. source | Is betterment under the Real Estate Taxation Law capital-source income? | — | **yes**: it is neither s 2(1)/(2) income nor personal-exertion income, which are the only exclusions. |
| F16 | s 121, "על כל שקל חדש" | Is income or tax rounded to whole shekels? | — | **no rounding**: the slice says nothing about it; amounts are continuous. |
| F17 | s 120B(b), line 4339, with (e)(1) | Does the freeze also stop a mid-year cost-of-living adjustment in 2025-2027? | — | **yes**: (e) opens "notwithstanding (a) and (b)" and (e)(1) says no adjustment "under (a) and (b)". |

## 5. Answer table

Figures from the text (lines 4351-4358, 4456, 4462) unless marked.
"Declined" means a named `REFUSE`.

| provision | 2025 | 2026 | 2027 | 2028 on |
| --- | --- | --- | --- | --- |
| s 121(a)(1) top of the 31% band | declined | 301,200 | 301,200 | declined (F7; **(0.2.0)** F7 answered, still declined for want of the 2027 index and the rounding Order) |
| s 121(a)(2) top of the 35% band | declined | 560,280 | 560,280 | declined |
| s 121(b)(1)(a) top of the 10% band | declined | 84,120 | 84,120 | declined |
| s 121(b)(1)(b) top of the 14% band | declined | 120,720 | 120,720 | declined |
| s 121(b)(1)(c) top of the 20% band | declined | 228,000 | 228,000 | declined |
| s 121(b)(1)(d) top of the reduced 31% band | declined | 301,200 | 301,200 | declined |
| rates, s 121 | — | 31 / 35 / 47; reduced 10 / 14 / 20 / 31 | same | — |
| s 121B(a) amount | declined | input: the 1 Jan 2024 figure after rounding (s 120B(e)(1)); editorial note says 721,560; **(0.2.0)** published by the Tax Authority as 721,560 (booklet 2026, PDF p. 8), carried as a figure, not law, in `ito-il03-published-figures.l4` | input (same; no published figure carried) | input: adjusted under s 120B(e)(2) and rounded |
| s 121B rates | — | 3% (a); 2% (a1) | same | same |
| s 121B(e) residential threshold | 5,385,285 (helper only); **(0.2.0)** declined, as s 121B is for 2025 (03-O1) | 5,385,285 | declined (RE Law s 9(c2)) | declined |
| s 120B amounts | fixed at 1 Jan 2024, after rounding | same | same | 1 Jan 2024 before rounding × (1 + 2027 rate), then rounded (declined) |

Worked figures the tests assert (tax year 2026; the same for 2027):

| facts | s 121 tax |
| --- | --- |
| 301,200 of other income, under 60 | 93,372 |
| 560,280 of other income, under 60 | 184,050 |
| 84,120 salary | 8,412 |
| 120,720 salary | 13,536 |
| 228,000 salary | 34,992 |
| 301,200 salary | 57,684 |
| 560,280 salary | 148,362 |
| 100,000 salary + 50,000 other income, under 60 | 26,135.2 (F1) |
| 150,000 other income, 60 by 31 December | 19,392 (F2) |
| 200,000 business income without the acceptable books it required | 62,000 |

| facts (s 121B(a) amount supplied as 721,560) | s 121B tax |
| --- | --- |
| 800,000 salary | 2,353.2 |
| 1,000,000 dividend | 13,922 (8,353.2 + 5,568.8) |
| 1,000,000 salary | 8,353.2 |
| capital gain 900,000, of which 100,000 inflationary | 3,922 |
| residential apartment sold for exactly 5,385,285 | 0 (F14) |

## 6. Nouns to reconcile at IL-07

Read from the sibling deposits (read-only) at the end of this session; nothing here depends on them and nothing in them was changed.

- **The individual.** This row: `An individual in a tax year` (tax year, date of birth, items of income, real-estate sales). IL-01: `Individual` (residence, sex and status flags) inside `Person`. IL-02: `A spouse` and `Spouses in a tax year`. Three records for one taxpayer.
- **Items of income.** This row: `An item of income` with flags (personal exertion, s 2(1)/(2), charged at the s 121 rates, books, s 88 inflationary amount). IL-02: `An item of income from personal exertion` (kind, taxable amount) plus per-spouse totals by source. The s 121 scale needs the personal-exertion split; s 121B needs the capital-source split; s 66 needs the attribution. One item record could carry all three.
- **The tax year.** All three take it as a `NUMBER`, but scope it differently: this row answers s 121 for 2026-2027; IL-02 records 2024 as the first year its s 66 text governs.
- **The credit-point amount.** IL-01 holds a per-year published value; this row treats "the amount of a credit point" as one of the s 120B amounts, frozen in 2025-2027 at its 1 January 2024 rounded figure. The two should agree, and that is a test IL-07 can write.
- **Age.** This row takes a date of birth; IL-02 takes a child's tax year of birth.

## 7. Sources: what was fetched, and what was not

Only the deposited source was read (sha256 `b87f2cf4…6b81b6`, verified on 2026-10-06 before use).
Three fetches were attempted on 2026-10-06 and all failed, so no official publication supplies any figure here:

- the 5786 Economic Efficiency Law (Knesset `25_lsr_12235101.pdf`) and the 5785 freezing Law (`25_lsr_5396578.pdf`) from `fs.knesset.gov.il`: both returned the same 131,618-byte HTML page titled "Unavailable" instead of a PDF, with and without browser headers;
- a `www.gov.il` page of the Tax Authority: HTTP 403, a Cloudflare challenge.

Nothing was kept from those responses.
The amending Laws were identified only by their position and title in the file's own list of amending Laws (line 5): tag 5785-2 is the Economic Efficiency Law for the 2025 budget year ("freezing of tax updates and surtax", Sefer HaChukim 5785 p. 150); tag 5786-6 falls in the Economic Efficiency Law for the 2026 budget year (5786 pp. 415-416).
That identification is by counting entries and was not checked against the Laws.

**(0.2.0)** The 5786 Law has since been deposited, from an Internet Archive capture of the Knesset's PDF (commons a862cb5, `../../registers/source-bundle/amending-laws/25_lsr_12235101.pdf`, sha256 `72244dba…4734155`, re-checked on 2026-10-08).
Its chapter C ("ריווח מדרגות מס הכנסה", widening of the income-tax brackets), ss 5-7, is on PDF p. 4, which is printed as Sefer HaChukim p. 416; that agrees with the 5786 pp. 415-416 placed above by list position.
`SOURCES.json` says "PDF p. 4, Sefer HaChukim p. 415"; the page's own number is 416 (checked 2026-10-08 with `pdftotext`: PDF pp. 2-5 are printed 414-417).
It is read for fork F7 and assumption A3 in "Version 0.2.0".
The 2026 Tax Authority booklet is recorded beside it by link and hash only (`SOURCES.json`, "pointers_only"), and is carried for one figure in `ito-il03-published-figures.l4`.
The 5785 Law (amendment 276, Sefer HaChukim 3342) is still not deposited.

**Observations about the source**, for whoever maintains it:

- Line 4462 repeats a phrase: "המדד שפורסם ביום המדד שפורסם ביום ז׳ בשבט התשפ״ז". Whether the error is the consolidation's or the Law's could not be checked.
- The editorial table for 2023 (lines 4419-4421) misnumbers two band edges: "116,711" where the band must start at 116,761, and "187,481" where it must start at 187,441.
- The editors treat the two sections differently: s 121 has adjusted figures written into its text, s 121B keeps the 2017 base in its text and puts the adjusted figures in a note.

## 8. Open questions for a domain expert

1. F1: in practice, does the Tax Authority place personal-exertion income at the bottom of the s 121 scale for an individual under 60 with other income? Is there a provision or ruling outside this slice that says so?
2. F2: for the year in which an individual turns 60, are the reduced rates applied to the whole year's income?
3. F7: does the 5786 amendment of s 121 say how its new ceilings are treated on 1 January 2028 under s 120B(e)(2), or is the bracket change a temporary provision for 2026-2027? **(0.2.0) Answered by the enacted Law**: its s 7 regards them as the amounts adjusted to 1 January 2024 for s 120B(e), and its s 6 commences them on 1 January 2026 with no end date (see "Version 0.2.0", 03-F7).
4. Does the 5785 amendment say from which tax year s 121B(a1) applies? (If from 2025, this row could answer s 121B for 2025.)
5. Is the duplicated phrase at line 4462 in the Law as published?

## 9. What was not done

- **The independent test pass** (skill step 8) was not run: the brief for this row is one session with no sub-agents. Every expected value was worked by hand from the text before it was asserted, but no second reader has derived them.
  **(0.2.0) Stale since 2026-10-06 (repair 03-W1).** The lead ran the pass after this was written, in a separate session (`fid-il-03`): commons a7f987f added `DECIDED-ANSWERS.md` (91 scenarios, decided before any `.l4` file was opened), `tests-independent.l4` (126 assertions) and `INDEPENDENT-FINDINGS.md`.
  Its counts, 118 satisfied, 6 failed and 2 refused, are declared in `check.sh` from 0.2.0 (CHK-03), and its two observations O1 and O2 are repaired in 0.2.0.
- **HG1**, a human who knows Israeli income tax reading the modules against the Hebrew, has not been sought.
- **Semi-cleanroom** (ruled 2026-10-06): nothing from the Axiom Foundation, any RuleSpec repository, or the paths the brief lists was read, searched or fetched in this session.

## Comparison with Axiom's RuleSpec (2026-10-06)

Written by `lad-il-03` (one session, no sub-agents) after this encoding and its independent test pass were deposited, under the semi-cleanroom ruling of 2026-10-06, which held Axiom's encoding back until then.
Nothing above this heading was changed, and no `.l4` file was edited: a divergence here is a finding, not a fix.
The modules compared are the deposited ones (sha256 `5cfa2088…` `ito-120b-indexation.l4`, `48e158a9…` `ito-121-individual-rates.l4`, `da3bc13f…` `ito-121b-additional-tax.l4`, `f399a74c…` `ito-il03-nouns.l4`).

### What was read

Axiom's side is the local clone `/Volumes/transcend/src/Axiom/rulespec-il` at commit `95c6f32c87c75e318631cbd77c14b840bc536c15`, read only, not pulled.

- In full: `il/statutes/income-tax-ordinance/section-120b.yaml`, `section-121.yaml`, `section-121b.yaml` and their three `.test.yaml` companions. None of the three imports a file outside itself; every import in `section-121b.yaml` is to its own rules.
- `NOTICE`, and the opening lines of `LICENSE` and `LICENSE-CODE`.
- `.axiom/encoding-manifests/il/statutes/income-tax-ordinance/section-120b.json`, `section-121.json`, `section-121b.json`: run `44dee41d` (gpt-5.6-terra), `f9f8d0e4` (gpt-6-astra) and `17f7e7e7` (gpt-6-astra), all generated 2026-09-06.
- `docs/ENCODING-GAPS.md`, the entries on these sections: lines 104-106, 192-250, 276-313, 383-392 and 431-461.
- `data/coverage/tax-benefit-source-map.json`: the five values that name ss 120B, 121, 121A or 121B. `known-missing-money-atoms.yaml` and `known-validation-gaps.yaml` have no entry for these sections.

**Read outside that list, and said here so a reviewer can weigh it.**
A grep of `README.md` for licence terms also matched the word "yaml" and printed about twenty lines of its module table, one line per module, including modules for ITO ss 33A, 34, 36, 36A and 66 and for the National Insurance Law.
A line-matching grep of `docs/ENCODING-GAPS.md` for these section numbers printed single lines from entries on other sections, among them Axiom's s 33A credit-point figure and a National Insurance Law provision that cites s 121B.
Reading lines 107-113 and 687-703 of that file (the second because it mentions s 121) showed a process note on two National Insurance Law modules and figures from Axiom's credit-point and s 66 encodings.
The listing of that file's entry headings showed the titles of entries on other sections.
None of it bears on this row and none of it is repeated here; it touches rows IL-01 and IL-02, and whoever compares those rows should know this reader saw it.
In the clone `git rev-parse HEAD` and `git status --short` were run to confirm the commit; the second can refresh git's index cache but changes no tracked file.

### Licence

`NOTICE` puts the encodings, companion test cases, parameter values and provenance metadata under **CC BY 4.0** (`LICENSE`) and tooling under Apache 2.0 (`LICENSE-CODE`), so the YAML files compared here are CC BY 4.0.
Attribution as `NOTICE` suggests it: "Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation".
They are quoted below only in short snippets that identify a point; nothing of theirs is copied into this encoding.

### Method

Both encodings read the same consolidation: Axiom's corpus holds it as at 2026-06-08 (`ENCODING-GAPS.md:220-221`), ours was retrieved 2026-10-06.
Every `excerpt` in the three modules occurs verbatim in our source, at L4344, L4350-L4359, L4456-L4457, L4462 and L4464-L4465 (checked by script after reducing the wiki templates and subsection labels); the module summaries match too once the consolidation's notes are dropped, except `section-120b.yaml:8`, which paraphrases L4344-L4345.
Axiom's cases were put through our modules in a scratch copy with the same `l4` binary and `JL4_LIBRARY_PATH` unset; counts were read from the diagnostics, because `l4 run` exited 0 on a run in which three assertions failed (a fixture error of the comparer's, since corrected).
To compute Axiom's answers outside its own cases, its formulas (`section-121.yaml:179-186`, `253-273`; `section-121b.yaml:136-289`) were restated in scratch L4, and the restatement reproduces all six of Axiom's expected values it was checked against.
The Axiom engine was not run.

### How each encoding is built

| | this encoding | Axiom |
| --- | --- | --- |
| s 120B | s 1 rate of rise and adjusted amount, (a), (b), (d) as a named refusal, (e)(1), (e)(2), a dispatcher by tax year; index readings and amounts supplied | one judgment, `annual_amounts_indexation_suspended`, equal to the caller's boolean `tax_year_is_in_indexation_freeze_period` (`section-120b.yaml:10-27`) |
| s 121 | the scale over a list of items, each flagged personal exertion, s 2(1)/(2), on the s 121 scale, books; age from date of birth | five supplied inputs: `taxable_income`, `taxable_income_from_personal_exertion`, the two no-books amounts, and a boolean `individual_has_reached_age_sixty` |
| s 121B | (a), (a1), and the (e) base computed from items and real-estate sales; the (a) amount is a required argument | (a) and (a1) over three supplied figures: the completed (e) base, its s 2(1)/(2) part, and its other personal-exertion part; the amount is fixed inside |
| result | `EITHER` a named problem or a number, or a named refusal | a figure per output, with band indices and excesses as intermediate outputs |

Where the text is silent or a figure is outside the sources, this encoding refuses by name or takes an input with no default; Axiom takes an input, or falls back on the printed figure, an undated version (`0001-01-01`, which `ENCODING-GAPS.md:193-197` says answers any earlier year with the current text), or a clamp to 0.

Tax years each one answers:

| | 2024 and earlier | 2025 | 2026 | 2027 | 2028 on |
| --- | --- | --- | --- | --- | --- |
| s 120B, ours | declined | (e)(1): the supplied 1 January 2024 figure after rounding | same | same | (e)(2) in 2028, (a) after; the figure in force declined for want of the rounding Order |
| s 120B, Axiom | no version | the caller's boolean | same | same | same; no amount computed |
| s 121, ours | declined | declined | printed figures | printed figures | declined |
| s 121, Axiom | no version | no version | printed figures | printed figures | printed figures, unadjusted (no end date) |
| s 121B, ours | declined | declined | (a) and (a1) at the supplied amount; residential threshold 5,385,285 | same; a residential sale declined | same |
| s 121B, Axiom | 640,000; (a) and (a1) | same | same | same | same |

### Divergences

Classes: ours wrong, theirs wrong, genuine ambiguity (the text supports both), scope difference, representational difference (same answer, different shape).
Line numbers `L…` are lines of the source file; file references without a directory are to this encoding or to Axiom's `il/statutes/income-tax-ordinance/`.

| id | provision | ours | Axiom | source | class | repair to ours |
| --- | --- | --- | --- | --- | --- | --- |
| X01 | s 121B(a), the amount | an input with no default; the printed 640,000 is read by no rule (`ito-121b-additional-tax.l4:39`, `:213-216`) | `additional_tax_threshold` is 640000 from `0001-01-01`, every year (`section-121b.yaml:33-50`) | L4335 makes the s 121B amount an income ceiling; L4338 adjusts income ceilings every 1 January; L4344 fixes 2025-2027 at the 1 January 2024 figure after rounding; the note at L4456 marks 640,000 as the 2017 nominal figure | **theirs wrong**, and conceded (`ENCODING-GAPS.md:276-286`) | none |
| X02 | s 121B(a1), years before 2025 | declined (every year before 2026) | applied in every year; its four companion cases are all dated 2024, and one asserts an (a1) charge of 3,200 (`section-121b.test.yaml:1-16`) | L4455 lists the 5785 amendment; the deposited text does not say from when (a1) applies | **scope difference** on the deposited text. Axiom's gap file cites the commencement of the amending Law (amendment 276, Sefer HaChukim 3342, s 3: 1 January 2025) and concedes the defect (`ENCODING-GAPS.md:289-308`); not verified here | none |
| X03 | s 121B, tax year 2025 | declined (assumption A1; section 8 Q4) | answered, at 640,000 | L4455 (the 5785 tag); the note at L4462 "נקוב לשנת 2025" | **genuine ambiguity** on the deposited text; the commencement Axiom cites (X02) would resolve it toward answering 2025 | none; see follow-up 1 |
| X04 | s 121, tax years 2028 on | declined (`ito-121-individual-rates.l4:62-74`) | every version runs from `2026-01-01` with no end, so the 2026 figures answer 2028 on (`section-121.yaml:29` and the other nine `effective_from`) | L4345 adjusts the amounts on 1 January 2028; L4335 makes the s 121 amounts income ceilings | **theirs wrong** from 2028. Axiom records that the indexation, (e)(2) included, is not encoded (`ENCODING-GAPS.md:383-391`, `:240-249`), but not that its s 121 answers 2028 | none |
| X05 | s 120B | the mechanism, over supplied readings and amounts | (e)(1) only; (a)-(d) and (e)(2) not encoded (`ENCODING-GAPS.md:383-391`) | L4338-L4345 | **scope difference** | none |
| X06 | s 120B(e)(1), which years | computed: 2025 to 2027 inclusive (`ito-120b-indexation.l4:131-133`; F13) | the years appear in the excerpt and in `effective_from: '2025-01-01'`, not in the formula; by the formula, a caller who supplies `true` for 2028 gets "holds" | L4344 | **representational**: the year test is left to the caller | none |
| X07 | s 121(b)(1), the age of 60 | from date of birth, 60th birthday on or before 31 December of the tax year (`ito-121-individual-rates.l4:203-204`; F2) | a boolean input (`section-121.yaml:180`) | L4354 names no date | **representational**: Axiom leaves F2 to the caller; the text does not decide it | none |
| X08 | s 121, the income on the scale | the items flagged `charged at the rates in section 121` (`ito-121-individual-rates.l4:192-194`) | `taxable_income` as supplied; nothing excludes income another section charges at its own rate | L4350 "המס על הכנסתו החייבת של יחיד"; the special-rate sections are outside the slice | **scope difference** at the interface: wages 84,120 with a dividend of 1,000,000 left in Axiom's `taxable_income` gives 412,589.60 there and 8,412 here | none |
| X09 | s 121, negative income | `LEFT an amount of income is negative` (`ito-121-individual-rates.l4:228-231`) | clamped to 0 (`section-121.yaml:253-254`) | silent | **representational** | none |
| X10 | s 121(a)(1) and (b)(1)(d), the two tops of the 31% band | declined if they differ (F8; `ito-121-individual-rates.l4:176-180`) | (a)(1)'s top bounds the general band, (b)(1)(d)'s bounds the credit-back, unchecked (`section-121.yaml:254`, `:261`) | L4351, L4358 | **representational**: the same answer with the printed figures | none |
| X11 | s 121, band edges | the tops only; each band is the slice above one top up to the next | the tops plus "first shekel" figures (301,201; 84,121; 120,721; 228,001), each band `min(x, top) - first + 1` | L4351-L4358 | **representational**: the same continuous arithmetic (F16) | none |
| X12 | s 121B(e), the income base | computed: s 88 and Real Estate Taxation Law s 47 inflationary amounts out, betterment in, the residential limb with its threshold and exemption (`ito-121b-additional-tax.l4:54-147`) | deferred: the caller supplies `taxable_income_for_section_121b` complete (`section-121b.yaml:13-31`); the 5,385,285 parameter is dated `0001-01-01` and read by no rule | L4462 | **scope difference** | none |
| X13 | s 121B(b), (c), (d) | (b) as its one answer, (c) inert, (d) an input convention | in the module summary only (`ENCODING-GAPS.md:456-458`) | L4458-L4460 | **scope difference**; no answer differs | none |
| X14 | s 120B(e)(2), its wording | F5: the 1 January 2024 amounts before rounding, adjusted by the 2027 rise only | not encoded; the summary drops "as they were on 1 January 2024 before rounding" (`section-120b.yaml:8`), and the gap file calls (e)(2) "the 2028 catch-up" (`ENCODING-GAPS.md:388`) | L4345 | **representational**: no value is computed on Axiom's side; "catch-up" leans toward the cumulative reading F5 rejects, but it is a label | none |

Totals: **0 ours wrong, 2 theirs wrong, 1 genuine ambiguity, 5 scope differences, 6 representational** (14).

Where both encodings answer, they agree:
the s 121 figures and rates for 2026-2027 (L4351-L4358); declining s 121 for 2025; F1, eligible income at the bottom of the scale (`section-121.yaml:253-273`, described at `ENCODING-GAPS.md:438-442`, without the alternatives); F3, (b)(2) reaching the over-60 individual's other income (`section-121.yaml:180-183`); R0.9 of the independent pass, (a1) measured on capital-source income alone against the (a) amount; the s 121B rates, 3% and 2% (L4456-L4457); the residential figure 5,385,285 (L4462), which Axiom holds but does not use; the capital-source definition (L4463-L4465), with counted betterment falling in it as the residual (F15); nothing due at exactly the amount (F14); and the exemption condition read as part of the residential limb (the first half of F9; Axiom's deferral note, `section-121b.yaml:28-31`).
Two encoders reaching F1 separately is evidence for it, not proof: neither text nor Axiom says why the eligible income sits at the bottom.

### Axiom's cases through this encoding

Scratch file `axiom-cases.l4`, run 2026-10-06.
Axiom's band indices have no counterpart here; the tax and the reduced-rate base were compared instead.

| Axiom case | year | facts | Axiom expects | this encoding | result |
| --- | --- | --- | --- | --- | --- |
| `indexation_is_suspended_during_freeze_period` | 2025 | the freeze, as a supplied boolean | holds | `s 120B(e)(1) — no adjustment in tax year` 2025 is TRUE | match |
| `indexation_is_not_suspended_after_freeze_period` | 2028 | as above | not holds | FALSE for 2028 | match |
| `personal_exertion_income_uses_reduced_schedule` | 2026 | 600,000, of which 300,000 personal exertion; other income without books 100,000; under 60 | base 300,000; tax 167,030.40 | 300,000; `RIGHT 167030.4` | match |
| `unacceptable_books_exclude_personal_exertion_income` | 2026 | as above, but 100,000 of the personal-exertion income without books | 200,000; 170,110.40 | 200,000; `RIGHT 170110.4` | match |
| `age_sixty_income_above_reduced_schedule_ceiling` | 2026 | as above, aged 60 (born 1960 here) | 400,000; 167,030.40 | 400,000; `RIGHT 167030.4` | match |
| `non_personal_income_below_age_sixty_uses_general_schedule` | 2026 | 600,000 of other income | 0; 202,718.40 | 0; `RIGHT 202718.4` | match |
| `auto_zero_general_income_band` | 2026 | everything 0 | band index 0 | no counterpart; the tax is `RIGHT 0` | not comparable |
| `both_additional_taxes_apply_after_distinct_capital_income_exclusions` | 2024 | base 1,000,000; s 2(1)/(2) 100,000; other personal exertion 100,000 | capital 800,000; (a) 10,800; (a1) 3,200; total 14,000 | refused: before 2026 | **diverge** |
| `neither_tax_applies_at_exact_threshold` | 2024 | 640,000, all capital | 0 | refused | **diverge** |
| `excluded_capital_categories_remain_subject_to_general_additional_tax` | 2024 | 1,000,000: s 2(1)/(2) 800,000, other personal exertion 200,000 | capital 0; 10,800 | refused | **diverge** |
| `neither_tax_applies_below_threshold` | 2024 | 600,000; capital 400,000 | 0 | refused | **diverge** |

**Matched 6, diverged 4, not comparable 1.**
The four divergences are all the year: moved to 2026 with Axiom's 640,000 supplied as the amount, the totals, the capital-source income and, where not zero, the (a) and (a1) parts all match (12 assertions); Axiom's "excess" outputs follow from those.
On the text, the first and third of those 2024 expectations are wrong by X01 alone, since the amount in 2024 was 640,000 as adjusted under s 120B, not 640,000; the second and fourth come to 0 either way.
With the 721,560 the editorial note gives, the first and third come to 9,922 and 8,353.20 in 2026 here.

### The independent pass's disagreements, on Axiom's side

| item (`INDEPENDENT-FINDINGS.md`) | this encoding | Axiom |
| --- | --- | --- |
| D03-D05, 60 during the tax year | 10,635.20 for 100,000 of rent (F2 (i)) | the caller decides: its boolean gives 10,635.20 if true, 31,000 if false |
| F01, wages 60,000 and rent 60,000, under 60 | 24,600 | 24,600: the same reading |
| F02 (the independent author's own error) | 12,300 | 12,300 |
| F03 (the same), wages -1,000 | `LEFT` | 0 |
| S13, 2025, dividend 900,000 | declined | 13,000, at 640,000 with (a1); the independent author expected 8,922 at 721,560 |
| S25, 2025, residential sale | declined | the base is the caller's; given 800,000 with 600,000 of s 2 income, 4,800; expected 2,353.20 |
| O1, the 2025 residential threshold reachable only by a direct call | as reported | no counterpart: the threshold is undated and read by no rule |
| O2, a rounded 2024 figure in the before-rounding field gives a plausible 2028 amount | as reported | no counterpart, since (e)(2) is not encoded; Axiom's silent failures of the same kind are X01 and X04, plausible figures with no diagnostic; its gap file concedes the first and records the second only as missing indexation |

On S13 and S25 Axiom supports the independent author's reading of the year (if its cited commencement holds) and not the author's figure.

### What Axiom has that this encoding does not, and the reverse

Axiom read the amending Laws, which this session could not fetch (section 7), and reports three things from them; none is verified here:

- amendment 288 (Sefer HaChukim 3511, 13 Nisan 5786), s 5 replaced four figures of s 121, (a)(1), (a)(2), (b)(1)(c) and (b)(1)(d), and left 84,120, 120,720 and the rates alone (`ENCODING-GAPS.md:226-229`);
- its s 6 commences it on 1 January 2026 for income derived or accrued from that day (`:200-203`), which agrees with the 2026 boundary of assumption A1;
- its s 7 treats the new figures, for adjustment under s 120B(e), as the amounts adjusted to 1 January 2024 (`:241-244`), which bears directly on fork F7 and on question 3 of section 8.

It also names the 5785 amendment of s 121B as amendment 276, Sefer HaChukim 3342 of 26 December 2024 (`:291-293`), and the 5786 one as Sefer HaChukim 3511, a 2026 Economic Efficiency Law by the file name it gives (`:204`); section 7 above placed them, by list position, at 5785 p. 150 and 5786 pp. 415-416, and booklet and page have not been reconciled.
Axiom carries a source excerpt on every parameter and intermediate outputs (band indices, the excess over the amount).

This encoding has, and Axiom does not: the s 120B mechanism and the s 1 arithmetic (with F4-F6 recorded); the s 121B(e) base computed from items and sales; the s 121B amount as a required input rather than a stale constant; a named refusal for every year or figure the text does not fix (s 121 from 2028, s 121B before 2026, a residential sale from 2027, the rounding Order); age from date of birth; special-rate items kept off the scale; rejection of invalid input; the check on the two tops of the 31% band; and a fork register.

### Follow-ups

No divergence is classed ours wrong, so no repair is proposed.
Three follow-ups depend on reading the amending Laws, which neither this comparison nor Axiom's citations can stand in for:

1. If amendment 276, s 3, commences s 121B(a1) on 1 January 2025 as Axiom reports, s 121B can answer 2025 with the amount supplied: the boundary at `ito-121b-additional-tax.l4:217` (and the refusal at `:80-81` and `:91`) would move to 2025, which also removes observation O1. Check first whether that amendment changed anything else in s 121B for 2025.
2. If amendment 288, s 7, reads as Axiom quotes it, F7 is answered by reading (iii), which here comes to (ii): the 2028 base for the moved ceilings is the 5786 figures. No answer here changes while the rounding Order is declined; the fork register and question 3 would record the answer.
3. Amendment 288, s 6, if confirmed, gives assumption A1's 2026 boundary for s 121 a basis in the Law rather than in the editorial tables.

### Bottom line

Where both encodings answer, they compute the same numbers: every comparable Axiom case matches, and its four s 121B cases match once moved into a year this encoding answers.
They part on time and on what is an input.
Axiom applies the 2017 figure of 640,000 as the s 121B amount in every year and, by its dating, the 2026 s 121 figures from 2028 on; the text says otherwise (L4335, L4338, L4344-L4345), and Axiom's own gap file records the first gap and the missing indexation behind the second.
This encoding declines those years and takes the amount as an input, which is more conservative and, for s 121B in 2025, possibly too conservative.
Axiom encodes s 120B as a pass-through and takes the s 121B(e) base and the age test from the caller; this encoding computes all three, and so carries the forks (F2, F4-F7, F9-F10) that Axiom leaves with its callers.
No divergence found this encoding wrong on the Hebrew.
The most useful thing Axiom offers this row is not its YAML but what it read in the amending Laws, and that should be verified at source before anything here changes.
