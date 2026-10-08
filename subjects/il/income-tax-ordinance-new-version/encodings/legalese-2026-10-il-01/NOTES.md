# IL-01: Income Tax Ordinance ss 33A, 34, 36, 36A (credit points) — notes

Row `legalese-2026-10-il-01`, run `IL-01-20261006`, encoder `enc-il-01` (one session, no sub-agents).
Status: **draft, version 0.2.0** (repairs of 2026-10-08, BACKLOG IL-14).
No domain expert has read it against the source; HG1 not sought.
An independent test pass was run on 2026-10-06 (commons `6343ef6`) and a comparison with Axiom's RuleSpec the same day (`30afa7e`); the repairs below answer findings from both.

Read this file first.
The brief is `BRIEF.md`; the self-check is `check.sh`; `render_source.py` renders source lines and checks every Hebrew quotation in the modules against the deposited text.

## Version 0.2.0 (2026-10-08): repairs (BACKLOG IL-14)

Repair agent `rep-il-14`, one session, no sub-agents, working job A of `l4-pipeline/findings/il-2026-10-08/jobs.txt` under the lead's repair brief.
Item ids are those of `l4-pipeline/findings/il-2026-10-08/inventory.tsv`.
Text below that 0.2.0 changed is marked "(0.2.0)" in place; nothing was deleted.

### What changed, item by item

| item | class | what changed | where |
| --- | --- | --- | --- |
| 01-S09 | OURS-WRONG | s 3A(f) (line 471) is encoded. A new record, `Taxpayer in a tax year`, carries the two facts of its two limbs: `an Israeli citizen who is a resident of the Area` and `an Israeli citizen who operates in the Area`. The year-aware rules treat either "as if" an Israeli resident, so ss 34 and 36 give 2 and 1/4 where 0.1.0 gave 0 and 0 with no diagnostic. s 3A's own text is held from tax year 2017 only (its last listed amendment is of 5776), so the s 3A(f) route refuses an earlier year. Facts that call the taxpayer both an Israeli citizen (a s 3A(f) fact) and not one (the s 48 fact) are refused by name. The residence field's comment now says it carries the s 1 status only and points to the record. | `ito-credit-points-nouns.l4`; `ito-s34-s36-s36a-credits.l4`, `§§ Section 3A(f)`; tests at `§§ Section 3A(f) — illustrations (0.2.0)` |
| 01-YR | OURS-WRONG | Every rule that answers a question about a taxpayer or an amount now has a year-aware twin that takes the tax year and refuses a year before its section's last listed amendment (the 504 constant and `section 36A, as written, applies to`, which read no year, have none): s 34 from 1976, s 36 from 1978, s 36A from 1997, s 33A from 2005, s 3A(f) from 2017. The s 48A refusal is dated from s 48A's enactment: from tax year 2002 (5763), the section's own answer before. The s 48 refusal stays undated. Section 1's "since 5764" is restated below. The `@export` moved to the year-aware amount. Every year-free entry point (12 in `ito-s34-s36-s36a-credits.l4`, 4 in `ito-s33a-credit-point.l4`) now carries a `@desc` saying that it answers on the text as it now stands, does not check the tax year, and which year-aware twin to use. | `ito-s33a-credit-point.l4`, `§§ Section 33A — the tax years …` and `… for a tax year`; `ito-s34-s36-s36a-credits.l4`, from `§§ The tax years the deposited text governs`; `NOTES.md` §1 |
| 01-W1 | WORDING | The nouns comment on `a resident of the Area who is not an Israeli citizen` gives "Israeli citizen" its s 3A(a) meaning (lines 455-459), under which every Israeli resident is one. The fixture `a man resident in Israel who is also recorded as an Area resident and not a citizen` and its assertion are labelled as describing a combination s 3A(a)(2) rules out. Comments only. | `ito-credit-points-nouns.l4`; `ito-credit-points-tests.l4` |
| 01-W2 | WORDING | The `@export` (now the year-aware one) says "under … ss 34, 36 and 36A for a taxpayer in a tax year, before ss 41 and 66 apply (not the taxpayer's total credit points)". | `ito-s34-s36-s36a-credits.l4`, last rule |
| 01-W3 | WORDING | §5's "No independent test pass … has been run" is marked stale and corrected; so is the same sentence in `encoding.json` `not_reviewed.note`. | `NOTES.md` §5; `encoding.json` |
| 01-W4 | WORDING | The published-figures module says that, by s 120B(e)(1) (line 4344), its 2025 figure is in law the figure for 2025 to 2027, and that it still answers only 2025. Comment only. | `ito-credit-points-published-figures.l4` |
| 01-W5 | WORDING | IL-01's half of the English name for "נקודת קיצבה": "allowance point", the name IL-01 already used, so nothing was renamed; a comment records the shared choice. See "01-W5" below. | `ito-s33a-credit-point.l4`, comment only |

### Assumed, not ruled

- **The tax-year limit (the lead's choice, 2026-10-08).** The deposited text of a section governs a tax year that begins after the Hebrew year of its last listed amendment has ended (fork F12).
  The amending Laws are not deposited, so their commencements are unknown.
  The rule can refuse a year an amendment already governed.
  It cannot answer a year an amendment had not reached, unless a Law deferred its own commencement past the next 1 January, and that is not checked.
- **The s 48A refusal from 2002 (the lead's choice, 2026-10-08, made on this agent's objection).** From tax year 2002 the year-aware rules refuse a foreign worker whom ss 34, 36 or 36A would credit; before 2002 they give what the section gives (fork F13).
  s 48A was enacted in 5763 (its amendment list at line 1810 is תשס״ג־3), a Hebrew year that began on 7 September 2002, so 2002 is the first tax year it could reach.
  Counting 5763's entries at line 5, errata included, the third is the Arrangements Law for fiscal 2003 (Sefer HaChukim 5763 p. 189); its date within 5763 is not in the bundle.
  The consolidation counts errata: the headings cite תשל״ו־5 (line 355) and תשס״ג־4 (37 headings), and 5736 and 5763 have five and four entries at line 5 only when errata are counted.
  The lead first chose to date the refusal from tax year 2014, by the Regulations of 5775-2014 that the note at line 1812 records.
  That choice was withdrawn: a note is not law, and naming those Regulations does not say there was no earlier instrument, so it could not license full points for 2002 to 2013.
  The lead's ruling first said "2003"; 2002 is taken because 5763 began in 2002 and the enacting Law's date is unknown, which errs toward refusing, and the lead accepted it.
- **A separate record rather than new fields (this agent's choice).** The s 3A(f) facts and the tax year are fields of a new record, `Taxpayer in a tax year`, not of `Individual`.
  L4 rejects a record construction that leaves out a field, even one with a `TYPICALLY` default ("you have not supplied these inputs", probed on the l4 binary below).
  Every existing `Individual WITH …` therefore stands unchanged: the independent tester's ten, this row's eleven and the one in the capstone's adapter.
  Revert by moving the four fields into `Individual` and editing those constructions.
- **The year-free rules are kept, unchanged (this agent's choice).** The rules over a `Person` (`the credit points under section 34 for` and the rest) still take no year, still refuse s 48A undated, and still cannot see s 3A(f).
  They are the building blocks of the year-aware rules and the interface the independent tests call, and every assertion of 0.1.0 still holds (58 in this row's tests, 78 in the tester's).
  A caller who wants a year answered, or s 3A(f) applied, uses the rules "… in the tax year of" a `Taxpayer in a tax year`.
- **A tax year after 2026** is answered on the text as it stood at retrieval: a projection, as in rows IL-02 and IL-08.

### How the year limits were found

Each section's heading lists the Laws that amended it (raw line, `{{ח:סעיף|…|תיקון: …}}`; `render_source.py` drops the list, so these were checked against the raw lines by `sed -n` on 2026-10-08).
A Hebrew year runs from one autumn to the next: 5735 from September 1974 to September 1975, and so on.
Where the entry can be resolved, the Law is named by counting that year's entries in the list of amending Laws at line 5, the convention rows IL-02 and IL-08 use (IL-08 checked it against Amendment 262, which it fetched and read).
None of the year limits depends on that naming.

| section | heading line | last listed amendment | Hebrew year ended | first tax year answered | the Law, by the line-5 count |
| --- | ---: | --- | --- | ---: | --- |
| s 34 | 1569 | תשל״ה־2 | September 1975 | 1976 | Amendment No. 22, Sefer HaChukim 5735 p. 168 |
| s 36 | 1593 | תשל״ז־4 | September 1977 | 1978 | Amendment No. 28, Sefer HaChukim 5737 p. 318 |
| s 36A | 1596 | תשנ״ו | September 1996 | 1997 | the Arrangements Law, Sefer HaChukim 5756 p. 24 |
| s 33A | 1561 | תשס״ד־2 | September 2004 | 2005 | Economic Policy Law for fiscal 2004, Sefer HaChukim 5764 p. 108 |
| s 3A | 453 | תשע״ו־22 | October 2016 | 2017 | not resolved: the line-5 entries of 5776 count to 18 boxes or 26 pages, and the convention does not say which |
| s 48A (refused from its enactment) | 1810 | תשס״ג־3 | (5763 began 7 September 2002) | refused from 2002 | the Arrangements Law for fiscal 2003, Sefer HaChukim 5763 p. 189 (errata counted) |

So the encoding now answers, for an individual resident in the tax year, every year from 1978 under ss 34 and 36 (from 1976 under s 34 alone), from 1997 under s 36A, and from 2005 as an amount of money.
The independent tester's year scenarios come out as that author decided them: S40 (1970: ss 34, 36 refused), S41 (1990: s 34 = 2, s 36 = 1/4, s 36A refused), S42 (1960: all refused), S38 and S39 (2026, 2024: 9/4).
They are asserted in this row's own tests, not in `tests-independent.l4`, which is the tester's file and was not edited.

The "Comparison with Axiom's RuleSpec" section at the end says that none of its proposed repairs has been applied.
As of 0.2.0, R1 (s 3A(f), both limbs, a field and a test for each) and R2 (take the year and refuse before each section's last listed amendment) have been.
That section is not edited, under the lead's rule for these repairs.

### 01-W5

The inventory left the English name of "נקודת קיצבה" (s 33A, line 1564) to the owner.
The lead decided on "allowance point" (2026-10-08, assumed, not ruled), the name this row has used since 0.1.0 (`the amount of an allowance point, given`); row IL-03 renamed its three "pension point" names to match (its `NOTES.md`, "01-W5 (IL-03's half)").
So IL-01's half changes no name and no answer; a comment in `ito-s33a-credit-point.l4` records the choice.
The grounds, which the lead asked to have recorded here:

- The Chapter's own heading, line 1559: "פרק שלישי: ניכויים, זיכויים וקיצבאות ילדים", deductions, credits and *child allowances*.
- s 40(a), line 1632, which confers them: "יחיד תושב ישראל זכאי לנקודות קיצבה בשל כל אחד מילדיו כקבוע בסעיף 109 לחוק הביטוח הלאומי", and "תשלום נקודות הקיצבה ייעשה בידי המוסד לביטוח לאומי". They are points for each child, paid by the National Insurance Institute under its child-allowance provision: an allowance, not a pension.
- Nothing in the definition at line 1564 speaks of a pension, or of a month ("monthly" is a gloss too, comparison X06).

### For the capstone (BACKLOG IL-22)

The capstone vendors four of this row's modules, `ito-credit-points-nouns.l4`, `ito-s33a-credit-point.l4`, `ito-s34-s36-s36a-credits.l4` and `ito-credit-points-published-figures.l4` (`vendor.sh` line 35), and all four changed.
`jobs.txt` lists only the first three as vendored, but `ito-credit-points-published-figures.l4` is vendored too and changed for 01-W4, in a comment only.
Nothing was removed or renamed: every name the adapter `il07-adapter-il01.l4` uses still exists and answers as before.
In a scratch copy of the capstone with these four modules dropped in, `il07-adapter-il01.l4` and `il07-pipeline.l4` compiled with no error, and the test modules counted as `red-checks.txt` records them (il07-tests 114 satisfied, il07-tests-il08 98, il07-tests-expected-red 2 failed, tests-independent 258 satisfied, 18 failed, 2 refused).
Only `vendor.sh --check` would differ.
To take up the repairs, the adapter would use:

- the new type `Taxpayer in a tax year` (nouns), with fields `the taxpayer` (a `Person`), `the tax year` (a NUMBER, the calendar year in which the tax year begins), `an Israeli citizen who is a resident of the Area` and `an Israeli citizen who operates in the Area` (BOOLEANs, s 3A(f));
- `the credit points under sections 34, 36 and 36A in the tax year of` and `the credit points under section 36A in the tax year of` in place of its two "… for" calls;
- `the amount of` n `credit points at a credit-point value of` v `in tax year` y, and `the tax for the year after setting off` x `against` t `in tax year` y, in place of its two s 33A calls;
- the earner record would need the two s 3A(f) facts, or the capstone would have to state that it takes them as FALSE.

The `@export` moved from `the amount of the credit points under sections 34, 36 and 36A for` p `at a credit-point value of` v (kept, no longer exported) to `the amount of the credit points under sections 34, 36 and 36A in the tax year of` c `at a credit-point value of` v.

### Assertions whose expected value changed or was added

No expected value in either test file changed, and `tests-independent.l4` was not edited: its 78 assertions are satisfied as before.
67 assertions were added to `ito-credit-points-tests.l4`, 26 of them `#ASSERT REFUSED … BECAUSE "…"`.
Every expected value was worked out from the source, in the comments beside it, before the rules were run, and none was edited to match a run.
The s 48A group (lines 405-435) was first written and run for the lead's first date, 2014, and passed; when the lead withdrew that date for s 48A's enactment, the group was rewritten from the new choice (2001 answered, 2002 and 2013 refused) before it was run again, and passed.

The s 48A group, first version against final version.
The first version was written and run (all satisfied) under the lead's first date, 2014, and never committed; the final version follows the lead's revised choice, s 48A's enactment (tax year 2002).

| first version (s 48A from 2014) | expected | final version (s 48A from 2002) | expected | why |
| --- | --- | --- | --- | --- |
| s 34, resident man, foreign worker, 2013 | 2 | the same case, 2013 (line 431) | refused (s 48A) | 2013 is after s 48A's enactment; the 2014 date was withdrawn (F13) |
| s 36A, non-resident woman, foreign worker, 2013 | 1/2 | the same case, 2013 (line 432) | refused (s 48A) | as above |
| s 34, resident man, foreign worker, 2013 | 2 | the same case, 2001 (line 419) | 2 | the last year before s 48A could reach |
| s 36, resident man, foreign worker, 2013 | 1/4 | the same case, 2001 (line 420) | 1/4 | as above |
| ss 34 + 36 + 36A, resident woman, foreign worker, 2013 | 11/4 | the same case, 2001 (line 421) | 11/4 | as above; s 36A's text governs from 1997 |
| s 36A, non-resident woman, foreign worker, 2013 | 1/2 | the same case, 2001 (line 422) | 1/2 | as above |
| s 34, resident man, foreign worker, 1990 | 2 | unchanged (line 424) | 2 | before s 48A existed |
| s 34, resident man, foreign worker, 2014 | refused (s 48A) | the same case, 2002 (line 427) | refused (s 48A) | the first year s 48A could reach |
| s 36, resident man, foreign worker, 2014 | refused (s 48A) | the same case, 2002 (line 428) | refused (s 48A) | as above |
| s 36A, resident woman, foreign worker, 2014 | refused (s 48A) | the same case, 2002 (line 429) | refused (s 48A) | as above |
| s 36A, non-resident woman, foreign worker, 2026 | refused (s 48A) | unchanged (line 433) | refused (s 48A) | after both dates |

Line numbers are lines of `ito-credit-points-tests.l4` as of 0.2.0; "old" is "—" for every row because every row is new.

| line | rule (year-aware) | case | old | new | why |
| ---: | --- | --- | --- | --- | --- |
| 328 | s 34 applies | an Israeli citizen resident in the Area, a man, 2026 | — | TRUE | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 329 | s 34 | an Israeli citizen resident in the Area, a man, 2026 | — | 2 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 330 | s 36 | an Israeli citizen resident in the Area, a man, 2026 | — | 1/4 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 331 | s 36A | an Israeli citizen resident in the Area, a man, 2026 | — | 0 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 332 | ss 34+36+36A | an Israeli citizen resident in the Area, a man, 2026 | — | 9/4 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 333 | ss 34+36+36A | an Israeli citizen resident in the Area, a woman, 2026 | — | 11/4 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 336 | s 34 | an Israeli citizen operating in the Area, a man, 2026 | — | 2 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 337 | s 36 | an Israeli citizen operating in the Area, a man, 2026 | — | 1/4 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 338 | ss 34+36 | an Israeli citizen operating in the Area, a man, 2026 | — | 9/4 | 01-S09: s 3A(f) (l. 471) treats the citizen "as if" resident, meeting the residence limb of s 34 (l. 1570) and s 36 (l. 1594); s 36A needs none |
| 342 | ss 34+36+36A | a non-resident man, 2026 | — | 0 | 01-S09: without either s 3A(f) fact, a plain non-resident (what 0.1.0 answered for both limbs) |
| 346 | s 34 | an Israeli citizen resident in the Area, a man, 2016 | — | refused: this encoding does not hold the text of section 3A for a tax year before 2017 | 01-S09, 01-YR: s 3A last amended תשע״ו־22 (5776, ended Oct 2016), so its text is held from 2017; s 36A does not need it |
| 347 | s 36 | an Israeli citizen operating in the Area, a man, 2016 | — | refused: this encoding does not hold the text of section 3A for a tax year before 2017 | 01-S09, 01-YR: s 3A last amended תשע״ו־22 (5776, ended Oct 2016), so its text is held from 2017; s 36A does not need it |
| 348 | s 36A | an Israeli citizen resident in the Area, a woman, 2016 | — | 1/2 | 01-S09, 01-YR: s 3A last amended תשע״ו־22 (5776, ended Oct 2016), so its text is held from 2017; s 36A does not need it |
| 349 | s 34 | an Israeli citizen resident in the Area, a man, 2017 | — | 2 | 01-S09, 01-YR: s 3A last amended תשע״ו־22 (5776, ended Oct 2016), so its text is held from 2017; s 36A does not need it |
| 352 | s 34 | a resident man who also operates in the Area, in 2010 | — | 2 | 01-S09: an s 1 resident meets s 34 without s 3A(f), so s 3A's year limit is not reached |
| 356 | s 34 | a man entered as both an Israeli citizen and not one, resident in the Area, in 2026 | — | refused: the facts say the taxpayer both is and is not an Israeli citizen within section 3A(a) | 01-S09: citizen (s 3A(f) fact) and non-citizen (s 48 fact) at once; s 3A(f) and s 48 would differ |
| 360 | ss 34+36+36A | a company controlled by an Israeli citizen, operating in the Area, in 2010 | — | 0 | 01-S09: s 3A(a)(4) (l. 459) makes the company an "Israeli citizen", but ss 34, 36 need a "יחיד", so s 3A's 2017 limit is never reached |
| 366 | ss 34+36+36A | a resident man, 2026 | — | 9/4 | 01-YR: a year every section governs answers as the year-free rules do (tester S38, S39) |
| 367 | ss 34+36+36A | a resident man, 2024 | — | 9/4 | 01-YR: a year every section governs answers as the year-free rules do (tester S38, S39) |
| 368 | ss 34+36+36A | a resident woman, 2026 | — | 11/4 | 01-YR: a year every section governs answers as the year-free rules do (tester S38, S39) |
| 369 | ss 34+36+36A | a non-resident woman, 2026 | — | 1/2 | 01-YR: a year every section governs answers as the year-free rules do (tester S38, S39) |
| 370 | ss 34+36+36A | a company, 2026 | — | 0 | 01-YR: a year every section governs answers as the year-free rules do (tester S38, S39) |
| 376 | s 34 | a resident woman, 1990 | — | 2 | 01-YR: 1990 is after 5735 (s 34) and 5737 (s 36), before 5756 (s 36A) ended (tester S41) |
| 377 | s 36 | a resident woman, 1990 | — | 1/4 | 01-YR: 1990 is after 5735 (s 34) and 5737 (s 36), before 5756 (s 36A) ended (tester S41) |
| 378 | ss 34+36 | a resident woman, 1990 | — | 9/4 | 01-YR: 1990 is after 5735 (s 34) and 5737 (s 36), before 5756 (s 36A) ended (tester S41) |
| 379 | s 36A | a resident woman, 1990 | — | refused: this encoding does not hold the text of section 36A for a tax year before 1997 | 01-YR: 1990 is after 5735 (s 34) and 5737 (s 36), before 5756 (s 36A) ended (tester S41) |
| 380 | ss 34+36+36A | a resident woman, 1990 | — | refused: this encoding does not hold the text of section 36A for a tax year before 1997 | 01-YR: 1990 is after 5735 (s 34) and 5737 (s 36), before 5756 (s 36A) ended (tester S41) |
| 384 | s 36A | a resident woman, 1996 | — | refused: this encoding does not hold the text of section 36A for a tax year before 1997 | 01-YR: 5756 ended Sept 1996, so s 36A answers from 1997 |
| 385 | s 36A | a resident woman, 1997 | — | 1/2 | 01-YR: 5756 ended Sept 1996, so s 36A answers from 1997 |
| 389 | s 34 | a resident man, 1970 | — | refused: this encoding does not hold the text of section 34 for a tax year before 1976 | 01-YR: 1970 is before 5735 and 5737 ended (tester S40); the year is checked before the facts |
| 390 | s 36 | a resident man, 1970 | — | refused: this encoding does not hold the text of section 36 for a tax year before 1978 | 01-YR: 1970 is before 5735 and 5737 ended (tester S40); the year is checked before the facts |
| 391 | s 34 | a non-resident man, 1970 | — | refused: this encoding does not hold the text of section 34 for a tax year before 1976 | 01-YR: 1970 is before 5735 and 5737 ended (tester S40); the year is checked before the facts |
| 395 | s 34 | a resident man, 1975 | — | refused: this encoding does not hold the text of section 34 for a tax year before 1976 | 01-YR: 5735 ended Sept 1975 (s 34 from 1976); 5737 ended Sept 1977 (s 36 from 1978) |
| 396 | s 34 | a resident man, 1976 | — | 2 | 01-YR: 5735 ended Sept 1975 (s 34 from 1976); 5737 ended Sept 1977 (s 36 from 1978) |
| 397 | s 36 | a resident man, 1977 | — | refused: this encoding does not hold the text of section 36 for a tax year before 1978 | 01-YR: 5735 ended Sept 1975 (s 34 from 1976); 5737 ended Sept 1977 (s 36 from 1978) |
| 398 | s 36 | a resident man, 1978 | — | 1/4 | 01-YR: 5735 ended Sept 1975 (s 34 from 1976); 5737 ended Sept 1977 (s 36 from 1978) |
| 401 | s 34 | a resident woman, 1960 | — | refused: this encoding does not hold the text of section 34 for a tax year before 1976 | 01-YR: 1960, before every section's last amendment (tester S42) |
| 402 | s 36 | a resident woman, 1960 | — | refused: this encoding does not hold the text of section 36 for a tax year before 1978 | 01-YR: 1960, before every section's last amendment (tester S42) |
| 403 | s 36A | a resident woman, 1960 | — | refused: this encoding does not hold the text of section 36A for a tax year before 1997 | 01-YR: 1960, before every section's last amendment (tester S42) |
| 419 | s 34 | a resident man who is a foreign worker, 2001 | — | 2 | 01-YR: s 48A was enacted in 5763 (l. 1810), which began 7 Sept 2002; before 2002 it could take nothing, so the section's own answer |
| 420 | s 36 | a resident man who is a foreign worker, 2001 | — | 1/4 | 01-YR: s 48A was enacted in 5763 (l. 1810), which began 7 Sept 2002; before 2002 it could take nothing, so the section's own answer |
| 421 | ss 34+36+36A | a resident woman who is a foreign worker, 2001 | — | 11/4 | 01-YR: s 48A was enacted in 5763 (l. 1810), which began 7 Sept 2002; before 2002 it could take nothing, so the section's own answer |
| 422 | s 36A | a non-resident woman who is a foreign worker, 2001 | — | 1/2 | 01-YR: s 48A was enacted in 5763 (l. 1810), which began 7 Sept 2002; before 2002 it could take nothing, so the section's own answer |
| 424 | s 34 | a resident man who is a foreign worker, 1990 | — | 2 | 01-YR: s 48A was enacted in 5763 (l. 1810), which began 7 Sept 2002; before 2002 it could take nothing, so the section's own answer |
| 427 | s 34 | a resident man who is a foreign worker, 2002 | — | refused: section 48A and the regulations made under it are not encoded in this model | 01-YR: from 2002 s 48A and whatever regulations stood under it could decide (the lead's choice, assumed, not ruled); 2013 lies in the window the withdrawn 2014 date would have answered |
| 428 | s 36 | a resident man who is a foreign worker, 2002 | — | refused: section 48A and the regulations made under it are not encoded in this model | 01-YR: from 2002 s 48A and whatever regulations stood under it could decide (the lead's choice, assumed, not ruled); 2013 lies in the window the withdrawn 2014 date would have answered |
| 429 | s 36A | a resident woman who is a foreign worker, 2002 | — | refused: section 48A and the regulations made under it are not encoded in this model | 01-YR: from 2002 s 48A and whatever regulations stood under it could decide (the lead's choice, assumed, not ruled); 2013 lies in the window the withdrawn 2014 date would have answered |
| 431 | s 34 | a resident man who is a foreign worker, 2013 | — | refused: section 48A and the regulations made under it are not encoded in this model | 01-YR: from 2002 s 48A and whatever regulations stood under it could decide (the lead's choice, assumed, not ruled); 2013 lies in the window the withdrawn 2014 date would have answered |
| 432 | s 36A | a non-resident woman who is a foreign worker, 2013 | — | refused: section 48A and the regulations made under it are not encoded in this model | 01-YR: from 2002 s 48A and whatever regulations stood under it could decide (the lead's choice, assumed, not ruled); 2013 lies in the window the withdrawn 2014 date would have answered |
| 433 | s 36A | a non-resident woman who is a foreign worker, 2026 | — | refused: section 48A and the regulations made under it are not encoded in this model | 01-YR: from 2002 s 48A and whatever regulations stood under it could decide (the lead's choice, assumed, not ruled); 2013 lies in the window the withdrawn 2014 date would have answered |
| 435 | ss 34+36+36A | a non-resident man who is a foreign worker, 2026 | — | 0 | s 48A can only take away: where the section gives nothing, 0 stands |
| 439 | s 34 | a man resident in the Area, not an Israeli citizen and not an Israeli resident, 1990 | — | refused: section 48 and the order made under it are not encoded in this model | s 48 is not dated: refused in every year the section governs; s 36A not reached by s 48 |
| 440 | s 36 | a man resident in the Area, not an Israeli citizen and not an Israeli resident, 2026 | — | refused: section 48 and the order made under it are not encoded in this model | s 48 is not dated: refused in every year the section governs; s 36A not reached by s 48 |
| 441 | s 36A | a woman resident in the Area, not an Israeli citizen and not an Israeli resident, 2026 | — | 1/2 | s 48 is not dated: refused in every year the section governs; s 36A not reached by s 48 |
| 447 | amount of points | 1 point at 2,904, tax year 2025 | — | 2904 | 01-YR: s 33A last amended תשס״ד־2 (5764, ended Sept 2004), so its text is held from 2005; values as in 0.1.0 tests |
| 448 | amount of points | 1 point at 2,904, tax year 2004 | — | refused: this encoding does not hold the text of section 33A for a tax year before 2005 | 01-YR: s 33A last amended תשס״ד־2 (5764, ended Sept 2004), so its text is held from 2005; values as in 0.1.0 tests |
| 451 | amount of points | 9/4 points at 2,000, tax year 2005 | — | 4500 | 01-YR: s 33A last amended תשס״ד־2 (5764, ended Sept 2004), so its text is held from 2005; values as in 0.1.0 tests |
| 454 | set-off | 6,534 against 10,000, tax year 2025 | — | 3466 | 01-YR: s 33A last amended תשס״ד־2 (5764, ended Sept 2004), so its text is held from 2005; values as in 0.1.0 tests |
| 455 | set-off | 6,534 against 10,000, tax year 2004 | — | refused: this encoding does not hold the text of section 33A for a tax year before 2005 | 01-YR: s 33A last amended תשס״ד־2 (5764, ended Sept 2004), so its text is held from 2005; values as in 0.1.0 tests |
| 459 | allowance point | given 2,904, tax year 2025 | — | 242 | 01-YR: s 33A last amended תשס״ד־2 (5764, ended Sept 2004), so its text is held from 2005; values as in 0.1.0 tests |
| 460 | allowance point | given 2,904, tax year 2004 | — | refused: this encoding does not hold the text of section 33A for a tax year before 2005 | 01-YR: s 33A last amended תשס״ד־2 (5764, ended Sept 2004), so its text is held from 2005; values as in 0.1.0 tests |
| 466 | @export amount | a resident woman, 2025, at published 2025 figure | — | 7986 | 01-S09, 01-YR: the @export; 2.75 x 2,904 = 7,986, 2.25 x 2,904 = 6,534; 2004 refused by s 33A's limit |
| 467 | @export amount | a resident man, 2025, at 2904 | — | 6534 | 01-S09, 01-YR: the @export; 2.75 x 2,904 = 7,986, 2.25 x 2,904 = 6,534; 2004 refused by s 33A's limit |
| 471 | @export amount | an Israeli citizen resident in the Area, a man, 2025, at 2904 | — | 6534 | 01-S09, 01-YR: the @export; 2.75 x 2,904 = 7,986, 2.25 x 2,904 = 6,534; 2004 refused by s 33A's limit |
| 472 | @export amount | an Israeli citizen resident in the Area, a woman, 2025, at 2904 | — | 7986 | 01-S09, 01-YR: the @export; 2.75 x 2,904 = 7,986, 2.25 x 2,904 = 6,534; 2004 refused by s 33A's limit |
| 473 | @export amount | an Israeli citizen operating in the Area, a man, 2025, at 2904 | — | 6534 | 01-S09, 01-YR: the @export; 2.75 x 2,904 = 7,986, 2.25 x 2,904 = 6,534; 2004 refused by s 33A's limit |
| 477 | @export amount | a resident man, 2004, at 2904 | — | refused: this encoding does not hold the text of section 33A for a tax year before 2005 | 01-S09, 01-YR: the @export; 2.75 x 2,904 = 7,986, 2.25 x 2,904 = 6,534; 2004 refused by s 33A's limit |

**The harness can fail on them.** On a scratch copy outside this directory, three rule edits (s 36A's first year 1996 for 1997, s 3A(f) never treating anyone as resident, s 48A from 2003 for 2002) made `ito-credit-points-tests.l4` print 19 failed; `tests-independent.l4` stayed at 78 satisfied, since it calls only the year-free rules.

### The check, 0.2.0

Run on 2026-10-08 from 07:17:17Z to 07:17:26Z, after the last edit, as `L4=/Users/mengwong/.local/bin/l4 ./check.sh` in this directory.
`~/.local/bin/l4` links to `~/.cabal/bin/l4`, which resolves to `/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-d4290e25/bin/l4`, sha256 `f4f2bd2558f02f828f0deced5f74313a33670f08cc3275ff95b83f2cde71e448`, the same before and after the run (0.1.0 ran on `64bbcb15…`; `red-checks.txt` records 78 of 78 for the tester's file on this newer binary before any edit).

```
module                                    errors satisfied  failed  refused  expected
ito-credit-points-nouns.l4                     0         0       0        0         0
ito-credit-points-published-figures.l4         0         0       0        0         0
ito-credit-points-tests.l4                     0       125       0        0         0
ito-s33a-credit-point.l4                       0         0       0        0         0
ito-s34-s36-s36a-credits.l4                    0         0       0        0         0
tests-independent.l4                           0        78       0        0         0
TOTAL (6 modules)                              0       203       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Exit 0. Every module: 0 errors, 0 failed, 0 refused; nothing is expected to fail, so `check.sh` declares nothing and was not edited.
`python3 -I render_source.py --check *.l4`: 68 Hebrew quotations checked, 0 missing.
The amendment lists quoted from the headings (which `render_source.py` does not render) were checked against the raw lines 453, 1561, 1569, 1593, 1596 and 1810.

## 1. What is encoded, and what is not

Encoded: Income Tax Ordinance [New Version] s 33A (the definitions of a credit point, "נקודת זיכוי", and of an allowance point, "נקודת קיצבה"), s 34 (two points for an individual who was an Israeli resident in the tax year), s 36 (a quarter point, "as a travel credit", for an Israeli resident individual) and s 36A (half a point for a woman), from the Hebrew Wikisource consolidation deposited at `../../registers/source-bundle/` (retrieved 2026-10-06, sha256 `b87f2cf4…b81b6`).

Not encoded, and taken as inputs: the year's indexed value of a credit point (s 120B, row IL-03), the tax against which the credit is set off (s 121 and its neighbours, row IL-03), whether an individual was an Israeli resident in the tax year (the s 1 definition), and whether an individual is a woman, a foreign worker, or an Area resident who is not an Israeli citizen.

(0.2.0) Also encoded: s 3A(f) (line 471), which treats an Israeli citizen who is a resident of the Area, or who operates in the Area, "as if" an Israeli resident; its two limbs are input facts of the new record `Taxpayer in a tax year`, read only by the year-aware rules.
(0.2.0) Also taken as an input: the tax year, by the year-aware rules.

Reached and refused: s 48 (an order of 5755-1995 extends ss 34 and 36 to Area residents who are not Israeli citizens) and s 48A (regulations of 5775-2014 may take the Chapter's credits from a foreign worker).
Where either could decide the case, ss 34, 36 and 36A refuse with a named reason; everywhere else they answer.
(0.2.0) In the year-aware rules the s 48A refusal applies from tax year 2002, s 48A's enactment, only; see version 0.2.0 above.

Not a total: the aggregates are named for the sections they add ("under sections 34 and 36", "under sections 34, 36 and 36A").
A person's total credit points also include ss 35, 37–40D, 45 and others (row IL-08), and ss 41 and 66 rework the points for spouses (rows IL-08, IL-02).

**Tax years (an assumption, not ruled).**
(0.2.0) **Superseded.** The two sentences after this paragraph describe 0.1.0 and understated it: because no rule took a year, the encoding answered *every* year, before 5764 as well, and applied the s 48A refusal in every year, including years before s 48A was enacted in 5763 (independent finding S40–S42; comparison S2; inventory 01-YR, which framed it as years before 2014).
In 0.2.0 the year-free rules still behave so, and the year-aware rules take the tax year and refuse a year before each section's last listed amendment: s 34 before 1976, s 36 before 1978, s 36A before 1997, s 33A before 2005, and s 3A(f) before 2017.
They apply the s 48A refusal from tax year 2002, when s 48A was enacted, only.
The method and its assumptions are in "Version 0.2.0" above.
The amendment lists below are as stated; s 34's and s 36's last entries are of 5735 and 5737, so "since 5764" was the latest of the four, not a date from which the encoding answered.
The slice's own text carries no dated arm, so no rule takes a date and the rule-version mechanism is not used.
The amendment lists in the section headings end at תשס״ד־2 (s 33A, 5764 = 2003–04), תשל״ה־2 (s 34), תשל״ז־4 (s 36) and תשנ״ו (s 36A); on that record — which I have not checked against the amending Acts — the text encoded here has stood since 5764, and the encoding answers any tax year since then for which the caller supplies the point value.
It has been exercised only at the 2025 value (NIS 2,904, published) and checked against the monthly figure for 2024, 2025 and 2026 (NIS 242, published).
For 2025–2027 s 120B(e)(1) (line 4344, row IL-03) freezes the figure at its 1 January 2024 value, which is consistent with the three booklets printing the same monthly 242.

| module | lines | what it holds |
| --- | ---: | --- |
| `ito-credit-points-nouns.l4` | 52 (0.2.0: 94) | `Person` (an individual, or a body of persons) and `Individual` (four facts); (0.2.0) `Taxpayer in a tax year` (a person, the tax year, the two s 3A(f) facts); `DECLARE` only |
| `ito-s33a-credit-point.l4` | 103 (0.2.0: 191) | s 33A: the 504 constant, points to an amount, the set-off, the allowance point; (0.2.0) s 33A's first tax year (2005) and a year-aware twin of each rule |
| `ito-s34-s36-s36a-credits.l4` | 237 (0.2.0: 538) | ss 34, 36, 36A, each as written and as reached by ss 48 and 48A; the two aggregates; ~~the `@export`~~ (0.2.0) the year limits, s 3A(f), the year-aware twin of every rule, and the `@export` |
| `ito-credit-points-published-figures.l4` | 77 (0.2.0: 84) | Israel Tax Authority figures, labelled as published figures and not law |
| `ito-credit-points-tests.l4` | 227 (0.2.0: 477) | 58 assertions, every expected value from the source; (0.2.0) 125, the 67 new ones for the year-aware rules |

## 2. Coverage table

Every provision this row met, with its disposition.
Line numbers are lines of `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` (sha256 `b87f2cf437ccfed35c3164681f4fc7ee015a111633454622751930c8894b81b6`).

### In scope

| provision | heading / words | lines | disposition | where |
| --- | --- | --- | --- | --- |
| s 33A chapeau | "בפרק זה –" | 1562 | encoded | `ito-s33a-credit-point.l4`, `§§ Section 33A`: by placement under the Chapter's heading, with a comment; the confinement changes no answer here because every rule that uses the definitions is in the Chapter |
| s 33A "נקודת זיכוי" limb 1 | an amount of NIS 504 for a tax year | 1563 | encoded | `the amount of a credit point as written in section 33A, before indexation` (504); `the amount of … credit points at a credit-point value of …` |
| s 33A "נקודת זיכוי" limb 2 | indexed "כאמור בסעיף 120א" | 1563 | out-of-scope | The indexation is s 120B's (row IL-03); the year's indexed figure is the input `the value of one credit point`, with no default. Fork F6 records that the cross-reference names s 120A. |
| s 33A "נקודת זיכוי" limb 3 | "המקוזז כנגד המס לאותה שנה" | 1563 | encoded | `the tax for the year after setting off … against …`; fork F5 |
| s 33A "נקודת קיצבה" | the credit point at 31.12.1996, adjusted under s 120B, divided by twelve | 1564 | encoded | `the amount of an allowance point, given …`: limb (3), the division, is encoded; limbs (1)-(2) are one figure s 120B produces (row IL-03), taken as the input |
| s 33A editorial notes | Wikisource figures for 1987, 2023, 2024–2027; pointer to the ITA simulator | 1563, 1564, 1567 | inert | Quoted in comments and marked "NOT statute text, NOT used". Two of the figure pairs are used in tests only as hypothetical inputs for the division by twelve, labelled as such. |
| s 34 | זיכוי לתושב ישראל — two points | 1569–1570 | encoded | `ito-s34-s36-s36a-credits.l4`, `§§ Section 34`: `section 34, as written, applies to`, `section 34 applies to`, `the credit points under section 34 for` |
| s 36 | זיכוי בעד נסיעה למקום ההשתכרות — a quarter point | 1593–1594 | encoded | `§§ Section 36`: the same three rules; forks F2, F3 |
| s 36A | זיכוי לאשה — half a point | 1596–1597 | encoded | `§§ Section 36A`: the same three rules; fork F1 |
| (0.2.0) ss 33A, 34, 36, 36A, 3A, the amendment lists in the headings | "תיקון: …" | 1561, 1569, 1593, 1596, 453 | encoded as year limits | `the first tax year the deposited text of section N governs` (2005, 1976, 1978, 1997, 2017) and a refusal per section; each year-aware rule asks its section's limit first; fork F12 |
| (0.2.0) s 3A(f) | an Israeli citizen who is a resident of the Area or operates in the Area: "הוראות פקודה זו כאילו היה תושב ישראל" | 471 | encoded | `ito-s34-s36-s36a-credits.l4`, `§§ Section 3A(f)`: `section 3A(f), as written, reaches the taxpayer in`, `section 3A(f) treats the taxpayer as an Israeli resident in`, read by the year-aware ss 34 and 36; forks F11, F12 |
| (0.2.0) s 3A(a) "אזרח ישראלי", "תושב אזור" | four kinds of "Israeli citizen"; the s 1 residence test with "the Area" for "Israel" | 455–459, 461 | out-of-scope, input | Neither test is encoded: each s 3A(f) fact of `Taxpayer in a tax year` carries its result for the limb ("an Israeli citizen who is a resident of the Area", "an Israeli citizen who operates in the Area"), as the residence field carries s 1's. The nouns comments give the definitions. |

### Definitions in s 1 that the slice uses

| provision | words | lines | disposition | reason |
| --- | --- | --- | --- | --- |
| s 1 "אדם" | "לרבות חברה וחבר בני־אדם" | 108 | encoded | `ito-credit-points-nouns.l4`: `Person IS ONE OF \`an individual\` …, \`a body of persons\`` |
| s 1 "חבר בני אדם" | a public body, company, association … | 124 | encoded | the constructor `a body of persons`, which has no facts and gets no points under ss 34, 36 or 36A |
| s 1 "תושב ישראל" (a), individuals | centre of life, the 183-day and 30/425-day presumptions, rebuttal, the Minister's power | 143–163 | out-of-scope | The definition is a whole regime of its own: an evaluative "centre of life" test over family, economic and social ties, two rebuttable day-count presumptions that either the individual or the assessing officer may displace, and regulations of 5766-2006 under para (4) that deem some individuals resident and others not. Whether a person was resident in a tax year is the gateway fact of nearly every computation in the Ordinance, not a question this slice owns, so the encoding takes the status as determined under s 1 as an input and encodes none of the test. Encoding the presumptions alone would answer a rebuttable question as if it were conclusive. |
| s 1 "שנת מס" | twelve months from 1 January, or a special assessment period | 202 | out-of-scope | The slice never computes a period: a tax year enters only as the label of the published credit-point figure, and special assessment periods (the second limb) do not reach any rule here. (0.2.0) The year-aware rules take the tax year as a NUMBER, the calendar year in which it begins ("שתחילתה ב־1 בינואר"), and compare it with each section's first year; a special assessment period is still not distinguished. When the tax year took its present calendar form is not checked, so for the oldest years answered (1976 onwards) the label is the caller's. |

### Reached by a rule in scope, not encoded: the rule refuses

| provision | words | lines | disposition | reason |
| --- | --- | --- | --- | --- |
| s 48 | זיכויים לתושבי האזור — the Minister may by order apply ss 34, 36 and 37 to Area residents who are not Israeli citizens "as if they were Israeli residents" | 1806–1808 | out-of-scope, refused | Assigned to IL-08 as a credit section, and its order (5755-1995, known here only from the Wikisource note at line 1808) is not in the source bundle. A rule in this row reaches it exactly when an individual who is not an Israeli resident is an Area resident and not an Israeli citizen: ss 34 and 36 then refuse with `section 48 and the order made under it are not encoded in this model`. s 48 does not name s 36A, so s 36A never reaches it. |
| s 48A | זיכויים לעובד זר — the Minister may disapply the chapter's credits, wholly or partly, to a foreign worker "even if treated as a resident" | 1810–1812 | out-of-scope, refused | Assigned to IL-08 as a credit section; the Regulations of 5775-2014 (line 1812) are not in the source bundle. The power can only remove or reduce credits, so a rule reaches it only where ss 34, 36 or 36A would otherwise give a foreign worker points, and there it refuses with `section 48A and the regulations made under it are not encoded in this model`; where the section gives a foreign worker nothing anyway, the answer 0 stands. (0.2.0) The year-aware rules refuse so only from tax year 2002, s 48A having been enacted in 5763 (line 1810, תשס״ג־3); before 2002 s 48A did not exist and they answer as the section reads (the lead's choice, assumed, not ruled; fork F13). s 48 stays undated. |

### Out of scope

| provision | heading | lines | disposition | reason |
| --- | --- | --- | --- | --- |
| s 35 | זיכוי לעולה | 1572–1588 | out-of-scope | Assigned to IL-08 by the lead. The new-immigrant credit is a month-by-month schedule over 42 or 54 months with two dated regimes (immigration before 2022 and from 2022), a spouse rule in (b), an absence rule in (c), a definition of "עולה" and "תושב חוזר" in (d), and a ministerial power in (e). It shares only the unit (a credit point) with this slice. |
| s 35A | (repealed) | 1590–1591 | out-of-scope | Repealed; a section number with no text under it. Listed so the numbering has no silent gap. |
| s 37 | זיכוי בעד בן־זוג | 1599–1600 | out-of-scope | Assigned to IL-08. A further point for a "יחיד מוטב" who proves to the assessing officer that a spouse was maintained, turning on retirement age, blindness and disability under s 9(5). It is also conditioned on proof "להנחת דעתו של פקיד השומה", a condition ss 34, 36 and 36A do not carry. |
| s 38 | זיכוי בעד בן זוג עובד | 1602–1604 | out-of-scope | Assigned to IL-08. Applies in a joint computation of a registered spouse; it gives "1⁄4 נקודת זיכוי לפי סעיף 36" for a working spouse's income and is cited in the fork register (F2) as evidence about s 36, but it is not encoded. |
| s 39 | זיכוי בעד בן־זוג עוזר | 1606–1608 | out-of-scope | Assigned to IL-08. A spouse who works in the other spouse's business. |
| s 39A | זיכוי לחייל משוחרר | 1609–1618 | out-of-scope | Assigned to IL-08 as one of "the other credit sections": a discharged soldier's credit: a fraction of a point for each of the 36 months after regular service ends, the fraction scaled by the length of service (line 1610–1611). |
| s 39B | זיכוי בעד שירות מילואים כלוחם | 1619–1630 | out-of-scope | Assigned to IL-08 as one of "the other credit sections": a credit in the following tax year for combat reserve duty, scaled by days served (line 1620–1621); its heading lists one amendment, תשפ״ו. |
| s 40 | נקודות קיצבה וזיכוי בעד ילדים | 1631–1647 | out-of-scope | Assigned to IL-08 as one of "the other credit sections". It is the main consumer of the "נקודת קיצבה" defined in s 33A, which this row does encode; s 40 itself (which parent gets which points for which child in which year) is not encoded here. |
| ss 40A–40D | credits for a remarried divorcee, a youth, an academic degree, a vocational qualification | 1648–1682 | out-of-scope | Assigned to IL-08 as "the other credit sections". Each has its own conditions and years; none modifies ss 34, 36 or 36A. |
| s 40E | מניעת כפל | 1683–1685 | out-of-scope | An election between s 40C and s 40D; it does not touch ss 34, 36 or 36A. |
| s 40F | (expired) | 1686–1687 | out-of-scope | Expired ("פקע"); listed so the numbering has no silent gap. |
| s 41 | בן זוג שהיה נשוי חלק מהשנה | 1689–1693 | out-of-scope | Assigned to IL-08. It CONSUMES this slice: a non-registered spouse married for part of the year gets "1⁄12 מנקודות הזיכוי לפי סעיפים 34, 36, 40(ב) ו־40ב" for each unmarried month. It does not change what ss 34 and 36 say, so this row's answers stand and s 41 multiplies them; a caller asking about such a spouse must apply s 41 on top. |
| s 41A | דיווח לכנסת | 1694–1696 | out-of-scope | A reporting duty on officials to the Knesset Finance Committee by 30 June 2019; not a rule about any taxpayer. |
| ss 42, 43 | (repealed) | 1697–1702 | out-of-scope | Repealed; listed so the numbering has no silent gap. |
| ss 44–46C | institutional care, incapacitated persons, insurance premiums, donations | 1703–1762 | out-of-scope | Credits computed as a percentage of an expense rather than in credit points (s 44, 35%, line 1704; s 45A, 25%, line 1715; s 46, 35%, line 1745), or in points with their own conditions (s 45, two points per qualifying child, line 1708). Assigned to IL-08 as "the other credit sections"; none modifies ss 34, 36 or 36A. ss 45B and 46C are repealed. |
| ss 47–47C | deductions for pension and national-insurance payments | 1763–1805 | out-of-scope | Deductions (ניכויים) from income, not credits against tax; outside this row and not credit points at all. s 47B is repealed. |
| s 57 | המס בקיבוץ שיתופי | 1869–1883 | out-of-scope | Applies "סעיפים 34 עד 46א ו־47" to a kibbutz's members as if its income were divided among them; a consumer of this slice in a special regime (Part D). |
| s 66 | חישוב נפרד | 2454–… | out-of-scope | Row IL-02. In a separate computation each spouse is entitled to the credit points of ss 34 and 36 (s 66(c)(1), line 2461), and "האשה תהא זכאית ל־1⁄2 נקודת זיכוי לפי סעיף 36א" (s 66(c)(4), line 2465). This row's rules are what s 66 applies per spouse. |
| s 120A | הגדרות (Part 6.1) | 4327–4335 | out-of-scope | The definitions of Part 6.1. s 33A's cross-reference "צמוד למדד כאמור בסעיף 120א" lands here, where the definition of "מדד" has been deleted; see fork F6. Not assigned to a row I know of. |
| s 120B | הצמדה | 4337–4345 | out-of-scope | Row IL-03. Fixes the indexed value of a credit point and of an allowance point each 1 January, freezes it for 2025–2027 at its 1 January 2024 value (s 120B(e)(1), line 4344), and is the source of the number this row takes as a `GIVEN`. |
| s 121 | שיעור המס ליחיד | 4349–4451 | out-of-scope | Row IL-03. Produces "the tax" against which s 33A says the credit-point amount is set off; this row takes that tax as a `GIVEN`. |
| ss 55(b), 60A(2) | a kibbutz member's assessment on income not passed to the kibbutz | 1864, 1916 | out-of-scope | Consumers in a special regime: in such an assessment the credit points already used in the kibbutz's assessment are not counted again. |
| s 91(e)(1), (e)(2)(b) | spreading a real capital gain over up to four tax years | 3381, 3384 | out-of-scope | A consumer: the tax on each year's slice is computed taking into account "יתרת נקודות הזיכוי" (the balance of credit points) for that year. Cited in fork F5 as evidence that an unused balance of credit points exists, that is, that the set-off is limited by the tax. |
| s 135(1)(a) | the assessing officer's power to demand returns, including of children "שהם זכאים בעדם לנקודות זיכוי" | 4878 | out-of-scope | Mentions credit points only to identify whose capital may be demanded in a return; no effect on the points. |
| s 134A(2) | exemption from filing below three times "סכום נקודות הזיכוי שעל פי סעיפים 34 ו־36" | 4864 | out-of-scope | A consumer. The aggregate it names is provided by this row as its own rule, because the Ordinance names it; s 134A itself (a ministerial power to exempt from filing) is not encoded. |


## 3. Fork register

Every place the text bore more than one reading, the readings, the one taken, and the words that license each.
None of these has been settled by a court or the Tax Authority to my knowledge; I did not search case law.

**F1 — does s 36A require residence?**
Text, line 1597: "בחישוב המס של אשה תובא בחשבון 1⁄2 נקודת זיכוי."
Reading A: no; any woman whose tax is computed gets half a point.
Reading B: yes; the personal credit points are for Israeli residents, and s 36A should be read with ss 34 and 36 beside it.
For A: s 34 says "יחיד שהיה תושב ישראל בשנת המס" and s 36 "יחיד תושב ישראל", so where the legislature wanted residence in this run of sections it said so; and s 48 (line 1807), which lets an order extend credits to non-resident Area residents "as if they were Israeli residents", lists ss 34, 36 and 37 and not s 36A, which is what one would expect if s 36A needed no extending.
For B: the shared context of the Chapter's personal credits; Tax Authority practice, which I have not sourced.
**Taken: A**, because the operative words impose no residence condition and the two textual signals point the same way.
Effect: a non-resident woman gets 0.5 points under this row (tests at `§§ Section 36A — illustrations`). Open question Q1.

**F2 — does s 36 require earning, or travel to a place of earning?**
Text: heading "זיכוי בעד נסיעה למקום ההשתכרות" (line 1593); body "בחישוב המס של יחיד תושב ישראל תובא בחשבון 1⁄4 נקודת זיכוי כזיכוי נסיעה." (line 1594).
Reading A: no; every resident individual gets the quarter point, and "as a travel credit" only names it.
Reading B: only an individual with income from personal exertion (who travels to earn it).
For B: the heading; and s 38(a) (line 1603), which in a joint computation gives "1⁄4 נקודת זיכוי לפי סעיף 36" for the other spouse only once it is proved that spouse's income is from personal exertion — suggesting the legislature linked the s 36 quarter point to earning.
For A: the body has no such condition; s 38(a)'s condition belongs to s 38's own joint-computation regime and is stated there, not in s 36; and, weakly, s 134A(2) (line 4864) measures the income of people with no income from work, business or profession against "סכום נקודות הזיכוי שעל פי סעיפים 34 ו־36" — weak because a yardstick need not be anyone's entitlement.
**Taken: A.** Open question Q2.

**F3 — the residence limb of s 36 has no "in the tax year".**
s 34: "שהיה תושב ישראל בשנת המס"; s 36: "יחיד תושב ישראל".
Reading A: the same test — resident for the tax year whose tax is computed — because s 1's definition determines residence by reference to a tax year (the presumptions at lines 151–153 are "בשנת המס").
Reading B: residence at some other moment (when the tax is computed).
**Taken: A**; both sections read the one field `an Israeli resident in the tax year`.

**F4 — part-year residence.**
"שהיה תושב ישראל בשנת המס" could mean resident for the tax year as a whole (s 1 decides one status per year) or resident at any time during it; and the sections say nothing about apportioning the points for part of a year (contrast s 41, line 1691, which apportions ss 34 and 36 by months for a spouse married part of the year).
**Taken:** residence is one status per tax year, supplied by the caller, and the points are never apportioned by this row. If the Tax Authority apportions for a person who becomes or ceases to be resident during the year, it does so under some provision this row has not met. Open question Q3.

**F5 — what "המקוזז כנגד המס לאותה שנה" does when the credit exceeds the tax.**
Reading A: the credit reduces that year's tax to no less than zero; the excess is not refunded and not carried to another year.
Reading B: the excess is refunded (a negative tax).
For A: "set off against" extinguishes a debt up to its amount; "לאותה שנה" ties it to that year; s 91(e)(1) and (e)(2)(b) (lines 3381, 3384) speak of "יתרת נקודות הזיכוי", a balance of credit points left unused in a year, which exists only if the set-off is capped by the tax; and the Tax Authority describes a credit point as "סכום המופחת מהמס", an amount deducted from the tax ([itc135-2025] p. 4).
**Taken: A**, `max 0 (tax − amount)`.
Not decided here: the order in which several credits are set off against one year's tax, which matters as soon as any other credit is in play.

**F6 — the cross-reference in s 33A points at s 120A.**
s 33A: "צמוד למדד כאמור בסעיף 120א" (line 1563).
s 120A (lines 4327–4335) is the definitions section of Part 6.1, and its definition of "מדד" is deleted ("(נמחקה)", line 4329); the provision that actually indexes "סכומי נקודת זיכוי" is s 120B(a) (line 4338), and "מדד" is defined in s 1 (line 179).
Readings: the reference is to Part 6.1 as a whole (in practice s 120B), or it is a stale reference.
**Taken:** s 120B governs, and the result does not change any answer here, because the indexed figure is an input either way. Recorded because a reviewer reading s 33A alone will look in the wrong section.

**F7 — the editorial figures are not law.**
The notes inside `{{ח:הערה|…}}` at lines 1563 and 1564 give "נקוב לשנת 1987" and figures for 2023 and 2024–2027.
They are Wikisource's, not the Knesset's, and are used nowhere as values.
Two of them appear in tests as hypothetical inputs to the division by twelve (2,820 → 235; 2,904 → 242), labelled as such; both pairs are consistent with "ומחולק בשנים עשר".

**F8 — no claim, no proof.**
ss 34, 36 and 36A say the points "יובאו בחשבון" / "תובא בחשבון" (shall be taken into account), with no claim and no proof "להנחת דעתו של פקיד השומה" — which s 37 (line 1600) does require.
**Taken:** an entitlement computed from the facts, not a permission the taxpayer exercises; no deontic rule.

**F9 — "אשה" is not defined.**
Neither s 1 nor Chapter Three defines "woman".
**Taken:** an input fact, `a woman`. A dispute about who counts is outside what the text settles. Open question Q4.

**F10 — what to answer where ss 48 and 48A reach.**
For a non-resident Area resident who is not an Israeli citizen, and for a foreign worker whom ss 34, 36 or 36A would otherwise credit, the answer depends on an instrument not in the bundle.
Readings: (a) answer as if the instrument did not exist (0 for the Area resident; full points for the foreign worker); (b) answer from the Wikisource note's one-line summary of the 1995 order; (c) refuse.
(a) gives a confidently wrong answer whenever the instrument applies; (b) encodes an order from an editor's paraphrase.
**Taken: (c)**, with the refusal placed so that every case the instrument cannot affect still answers (a foreign worker whom the section gives nothing gets 0; an Israeli resident needs no s 48 order).
The refusals are not dated, because no rule here takes a date: for a tax year before the 2014 Regulations the model still declines on a resident foreign worker, where the law then may well have given full points.
(0.2.0) Still true of the year-free rules. The year-aware rules date the s 48A refusal from tax year 2002, s 48A's enactment (F13); the s 48 refusal stays undated in both.

**F11 (0.2.0) — does s 3A(f) reach the personal credits of ss 34 and 36?**
Text, line 471: "בכפוף להוראות סעיף זה, יחולו על אזרח ישראלי שהוא תושב אזור או פועל באזור, הוראות פקודה זו כאילו היה תושב ישראל, בשינויים המחוייבים לפי הענין."
Reading A: yes; "the provisions of this Ordinance" are the whole Ordinance, ss 34 and 36 among them, so an Israeli citizen who is a resident of, or operates in, the Area meets their residence limb.
Reading B: no; "subject to this section" and "with the necessary modifications" confine (f) to the income-from-the-Area regime of s 3A itself.
For A: the words "הוראות פקודה זו" are unqualified; and s 48 (line 1807) takes "אזור", "תושב אזור" and "אזרח ישראלי" from s 3A and lets an order extend ss 34 and 36 only to Area residents who are *not* Israeli citizens, which is what one would expect if (f) already carried the citizens.
For B: the placement of (f) inside a section headed "הכנסה מאזור" (income from the Area, line 453).
**Taken: A**, for both limbs, as the independent tester (S09, marked H on reflection) and the comparison (R1) read it.
That the second limb, "או פועל באזור", reaches the personal credits was the comparison author's reading, untested by either encoding; it is tested here.
"פועל באזור" (operates in the Area) is undefined and is an input, as "אשה" is (F9).
Where a taxpayer is entered both as an Israeli citizen in the Area and as an Area resident who is not an Israeli citizen, the facts contradict each other and A and s 48 would answer differently, so the rule refuses: "the facts say the taxpayer both is and is not an Israeli citizen within section 3A(a)".
Open question Q7.

**F12 (0.2.0) — from which tax year does the deposited text govern?**
The bundle is one consolidation; each heading lists the Laws that amended the section by Hebrew year; the Laws themselves are not deposited.
Reading A: the deposited text governs a tax year that begins after the Hebrew year of the section's last listed amendment has ended.
Reading B: from the Gregorian year in which that Hebrew year ends (1975 for s 34).
Reading C: from the commencement each amending Law sets, which needs the Laws.
B answers a year the amendment may not have reached; A refuses such a year instead; C is not available from the bundle.
**Taken: A** (the lead's choice, assumed, not ruled). It is wrong only if a Law deferred its own commencement past the following 1 January.
Effect: s 34 from 1976, s 36 from 1978, s 36A from 1997, s 33A from 2005, s 3A(f) from 2017; a year after 2026 is answered on the text at retrieval, as a projection.
Open question Q8.

**F13 (0.2.0) — from which tax year can s 48A take a credit away?**
s 48A (line 1811) is a power, enacted in 5763 (its amendment list at line 1810, תשס״ג־3); the note at line 1812, which is not law, records one exercise of it, the Regulations of 5775-2014.
Reading A: from tax year 2014, the first the 5775-2014 Regulations could reach; before 2014 the section's own answer.
Reading B: from tax year 2002, the first s 48A itself could reach (5763 began on 7 September 2002), because the bundle cannot exclude an earlier instrument; before 2002 the section's own answer, s 48A not yet existing.
Reading C: in every year (0.1.0, and still the year-free rules).
A answers 2002 to 2013 on the strength of the note's silence about any earlier instrument, which is reading (b) of F10, an answer from an editor's note; C refuses years in which s 48A did not exist and could take nothing.
**Taken: B** in the year-aware rules: the lead's choice (2026-10-08, assumed, not ruled), made on this agent's objection to A, which the lead had chosen first.
The first tax year is 2002, which the lead accepted (2026-10-08) after first writing 2003.
The count: s 48A's heading (line 1810) lists one Law, תשס״ג־3, the third Law of 5763, a Hebrew year that began on 7 September 2002.
The list of amending Laws at line 5 gives 5763 four entries: an erratum (p. 122), Amendment 132 (correction) (p. 126), the Arrangements Law for fiscal 2003 (p. 189), and the Economic Recovery Plan Law (pp. 415, 428).
Errata count in this numbering: headings cite תשל״ו־5 (line 355) and תשס״ג־4 (37 headings), which exist only if they do, 5736 having two Laws and three errata at line 5 and 5763 three Laws and one erratum.
So the third is the Arrangements Law for fiscal 2003, Sefer HaChukim 5763 p. 189, which is not deposited; its date within 5763, and so whether it fell in 2002, is unknown.
Refusing from 2002, the first tax year 5763 overlaps, errs toward refusing.
The refusal keeps its 0.1.0 wording, "section 48A and the regulations made under it are not encoded in this model", which row IL-02 now copies and the capstone's expected-red R2 names.
Open question Q8.

## 4. Answer table

Points under each section, for each kind of person, as this row reads the source.
"refused" means the model declines and names the instrument it lacks.

| person | s 34 (l. 1570) | s 36 (l. 1594) | s 36A (l. 1597) | ss 34 + 36 | ss 34 + 36 + 36A |
| --- | ---: | ---: | ---: | ---: | ---: |
| resident man | 2 | 1/4 | 0 | 2 1/4 | 2 1/4 |
| resident woman | 2 | 1/4 | 1/2 | 2 1/4 | 2 3/4 |
| non-resident man | 0 | 0 | 0 | 0 | 0 |
| non-resident woman | 0 | 0 | 1/2 (F1) | 0 | 1/2 |
| body of persons (e.g. a company) | 0 | 0 | 0 | 0 | 0 |
| resident, foreign worker | refused (s 48A) | refused (s 48A) | 0 if a man; refused (s 48A) if a woman | refused | refused |
| non-resident, foreign worker | 0 | 0 | 0 if a man; refused (s 48A) if a woman | 0 | 0 if a man; refused if a woman |
| non-resident Area resident, not an Israeli citizen | refused (s 48) | refused (s 48) | 0 if a man; 1/2 if a woman | refused | refused |
| resident in Israel, also an Area resident and not a citizen | 2 | 1/4 | as for any resident | 2 1/4 | as for any resident |

(0.2.0) The last row describes facts that cannot all be true: by s 3A(a)(2) (line 457) every Israeli resident is an "Israeli citizen" (01-W1).
The table above is the year-free rules', and the year-aware rules' for any tax year from 2002 (none of its people has a s 3A(f) fact).
The year-aware rules add these rows (tax year 2026 unless stated):

| person, in the year-aware rules | s 34 | s 36 | s 36A | ss 34 + 36 | ss 34 + 36 + 36A |
| --- | ---: | ---: | ---: | ---: | ---: |
| Israeli citizen resident in the Area, not resident under s 1 (s 3A(f) limb (i)) | 2 | 1/4 | 0 if a man; 1/2 if a woman | 2 1/4 | 2 1/4 or 2 3/4 |
| Israeli citizen who operates in the Area, not resident under s 1 (limb (ii)) | 2 | 1/4 | as for anyone | 2 1/4 | as for anyone |
| either of the two, tax year before 2017 | refused (s 3A text) | refused (s 3A text) | as for anyone | refused | refused |
| facts both "Israeli citizen in the Area" and "Area resident, not an Israeli citizen" | refused (contradiction) | refused (contradiction) | as for anyone | refused | refused |
| resident, foreign worker, tax year 1997 to 2001 | 2 | 1/4 | 0 if a man; 1/2 if a woman | 2 1/4 | 2 1/4 or 2 3/4 |
| non-resident woman, foreign worker, tax year 1997 to 2001 | 0 | 0 | 1/2 | 0 | 1/2 |
| anyone, tax year 1997 to 2016 (no s 3A(f) fact) | as above | as above | as above | as above | as above |
| anyone, tax year 1978 to 1996 | as above | as above | refused (s 36A text) | as above | refused |
| anyone, tax year 1976 or 1977 | as above | refused (s 36 text) | refused | refused | refused |
| anyone, tax year before 1976 | refused (s 34 text) | refused | refused | refused | refused |

An amount in NIS from the year-aware rules is refused for any tax year before 2005, because the amount is s 33A's.

The credit-point amount, in NIS, at the Tax Authority's published figure:

| tax year | NIS per point, annual | NIS per point, monthly | resident man (2 1/4) | resident woman (2 3/4) | non-resident woman (1/2) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2024 | not sourced (refused) | 242 [booklet-2024 p. 11] | — | — | — |
| 2025 | 2,904 [itc135-2025 p. 4] | 242 [booklet-2025 p. 10] | 6,534 | 7,986 | 1,452 |
| 2026 | not sourced (refused) | 242 [booklet-2026 p. 9] | — | — | — |

The 2025 amounts are the Authority's own rule, "the product of the number of credit points and the value of one credit point", applied to this row's points.
The row does not derive an annual figure from a monthly one; s 120B(e)(1) would make 2026 equal 2024 and 2025, but that is row IL-03's to compute.

## 5. What `check.sh` prints

(0.2.0) This section records the 0.1.0 run; the 0.2.0 run is in "Version 0.2.0" above.

Run on 2026-10-06 as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, with the binary at `/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-0ee0100b/bin/l4`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118` (it has no `--version`; its file time changed to 21:20 that evening, so another session may have reinstalled it during this run).

```
module                                    errors satisfied  failed  refused  expected
ito-credit-points-nouns.l4                     0         0       0        0         0
ito-credit-points-published-figures.l4         0         0       0        0         0
ito-credit-points-tests.l4                     0        58       0        0         0
ito-s33a-credit-point.l4                       0         0       0        0         0
ito-s34-s36-s36a-credits.l4                    0         0       0        0         0
TOTAL (5 modules)                              0        58       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Every module: 0 errors, 0 failed, 0 refused.
The 58 satisfied assertions are all in the tests module, 9 of them `#ASSERT REFUSED … BECAUSE "…"` pinning a refusal's wording.
No assertion is expected to fail, so `expected_failed` is 0 everywhere and there is no red file.

That the harness can fail was checked on a scratch copy outside this directory: one expected value changed and s 36A's half point replaced by a `REFUSE` produced `1 failed, 8 refused`, `exit=1`.

The only diagnostic besides the results is an environment warning: `l4` reports a second copy of `prelude` in `~/.local/share/jl4/libraries/` and uses the copy compiled into the binary.

`python3 -I render_source.py --check *.l4` reports every Hebrew quotation found verbatim in the rendered source (44 checked, 0 missing).

No independent test pass (skill step 8) has been run: the lead asked for one session without sub-agents.
It is the first thing to add.
(0.2.0) Stale since 2026-10-06 (01-W3): an independent test pass was run that day, commons `6343ef6` (`DECIDED-ANSWERS.md`, `INDEPENDENT-FINDINGS.md`, `tests-independent.l4`: 78 assertions, all satisfied), followed by the comparison with Axiom's RuleSpec below (`30afa7e`).

## 6. Open questions for a domain expert

- **Q1 (F1).** Does the Tax Authority give the s 36A half point to a woman who is not an Israeli resident? If it does not, on what text?
- **Q2 (F2).** Is the s 36 quarter point given to a resident with no income from personal exertion (a pensioner on passive income, say)?
- **Q3 (F4).** Are ss 34 and 36 apportioned for an individual who becomes, or ceases to be, an Israeli resident during a tax year? Under which provision?
- **Q4 (F9).** Is "אשה" in s 36A read from the population register, or otherwise?
- **Q5 (F5).** Confirm that an excess of credit-point amount over the tax lapses, outside the s 91 spreading regime.
- **Q6.** The 1995 order under s 48 and the 2014 Regulations under s 48A: are they in force in the form the Wikisource notes describe? Row IL-08 should fetch and encode them. (0.2.0) Now BACKLOG IL-28, deferred by Meng on 2026-10-08.
- **Q7 (F11, 0.2.0).** Does the Tax Authority give the ss 34 and 36 points to an Israeli citizen who is a resident of the Area, or who operates in the Area, by force of s 3A(f)? What does "פועל באזור" require?
- **Q8 (F12, F13, 0.2.0).** From which tax year did each section's last listed amendment apply (Amendment No. 22 of 5735, No. 28 of 5737, the Arrangements Law of 5756, the Economic Policy Law of 5764, and s 3A's of 5776)? On what date in 5763 did the Arrangements Law for fiscal 2003 enact s 48A, was any instrument made under it before the Regulations of 5775-2014, and from which tax year do those Regulations apply?

## 7. Nouns to reconcile at IL-07

Observed on 2026-10-06 by reading the sibling directories; nothing here was changed, and nothing imports from them.

- **The woman.** IL-02 (`ito66-nouns.l4`) declares `Sex IS ONE OF \`a woman\`, \`a man\`` as a field `sex` of `A spouse`; this row declares a BOOLEAN field `a woman` on `Individual`. Same fact (s 36A, s 66(c)(4)), two shapes — and the IL-02 constructor and this row's field share the name `a woman`, which will collide if one module imports both.
- **The individual.** This row: `Person IS ONE OF \`an individual\` HAS \`the individual\` IS AN Individual, \`a body of persons\``, with `Individual` carrying residence, sex, Area status and foreign-worker status and no tax year. IL-03 (`ito-il03-nouns.l4`): `An individual in a tax year` with `tax year`, `date of birth`, items of income. IL-02: `A spouse`. Residence in the tax year appears only here.
  (0.2.0) This row now also has `Taxpayer in a tax year`: a `Person`, `the tax year`, and the two s 3A(f) facts, read by the year-aware rules. Its shape is close to IL-03's `An individual in a tax year`.
- **The allowance point.** This row translates "נקודת קיצבה" as "allowance point" (the Chapter's heading is "…וקיצבאות ילדים", child allowances); IL-03 calls it "pension point" (`A kind of amount adjusted under section 120B`). One English name should be chosen.
  (0.2.0) Chosen: "allowance point" (01-W5, the lead's choice, 2026-10-08, assumed, not ruled); IL-03 renamed its names to match.
- **The credit-point value.** IL-03's `A kind of amount adjusted under section 120B` includes `the amount of a credit point`; its output for a tax year is this row's input `the value of one credit point`. At IL-07 the input can be wired to IL-03's rule.
- **s 36A twice.** IL-02's `ito66-c-credit-points.l4` carries its own "one half point under section 36A, by paragraph (4)"; this row's `the credit points under section 36A for` is the same half point from s 36A itself.

## 8. Sources read, and provenance

- The deposited Wikisource source, read-only, by line number as cited (sha256 checked against the `.meta.json` on 2026-10-06).
- Israel Tax Authority publications, fetched 2026-10-06 as Internet Archive captures because gov.il returned a Cloudflare challenge to direct requests; full URLs, capture timestamps and sha256s are in the header of `ito-credit-points-published-figures.l4`. They are not deposited: they are government publications, not among the classes (statutes, regulations, Knesset records, judicial decisions) that s 6 of the Copyright Act 5768-2007 excludes from copyright, so only short quotations are carried.
- The L4 skills (`encoding-a-subject`, `writing-l4-rules` with `drafting-patterns.md`, `gotchas.md` and the `source-patterns/` pages 01, 03, 04 (4.7–4.8), 09 (9.4–9.5, 9.9) and 11), and the commons layout (`canon-deposit.md`) and the HVAC row's `encoding.json` as the worked example.
- The sibling directories `legalese-2026-10-il-02` and `-il-03`, read-only, for section 7 only.
- Not read: anything from the Axiom Foundation or any RuleSpec encoding, under any of the paths the brief forbids. Web searches were limited to the Tax Authority's own figures on gov.il.
- (0.2.0) Read for the repairs, all read-only: the source bundle's lines 5 (the list of amending Laws), 202, 453–471, 1559–1597, 1806–1812 and 4337–4345; `amending-laws/SOURCES.json` (it holds no Law that amends ss 3A, 33A, 34, 36, 36A or 48A); this row's own files, including the independent tester's (not edited); the tax-year modules of rows IL-02 (`ito66-tax-years.l4`) and IL-08 (`ito-il08-tax-years.l4`), for the counting convention and the refusal wording; IL-04's `encoding.json`, for the shape of a repairs entry; the capstone's `il07-adapter-il01.l4`, `vendor.sh` and `RECONCILE.md` (N8, N13), and a scratch copy of the capstone, to check that it still compiles; `l4-ide/skills/writing-l4-rules/references/source-patterns/07-presumptions-and-defaults.md` §7.4 on `TYPICALLY`. No Axiom file was opened and no web access was used.

## Comparison with Axiom's RuleSpec (2026-10-06)

Comparison author `lad-il-01`, one session, no sub-agents, 2026-10-06.
The lead released the semi-cleanroom rule for this row only, after the encoding above had been deposited and independently tested; no Axiom file was opened before then.
Nothing above this section was changed, no other file was edited, and none of the repairs proposed below has been applied.

### What was read

The local clone `/Volumes/transcend/src/Axiom/rulespec-il/` at commit `95c6f32c87c75e318631cbd77c14b840bc536c15` (2026-10-03, "Merge pull request #8"), read-only, not pulled.

- In full: `il/statutes/income-tax-ordinance/section-33a.yaml`, `section-34.yaml`, `section-36.yaml`, `section-36a.yaml` and their four `.test.yaml` companions. The sha256 of all eight matches the `applied_files` hashes in their manifests.
- In full: `.axiom/encoding-manifests/il/statutes/income-tax-ordinance/section-33a.json`, `section-34.json`, `section-36.json`, `section-36a.json`.
- `docs/ENCODING-GAPS.md`: the entry `credit-conditions-are-inputs-not-derived` (lines 516–520) in full; from the entry `no-executable-oracle` (heading at line 687), its first three lines and the one bullet that names ss 34, 36 and 36A.
- `data/coverage/tax-benefit-source-map.json`: the top-level keys; for the Income Tax Ordinance entry, its scalar fields, its `expressions`, `corpus_expression_dates["income-tax-ordinance"]`, and membership tests on its `encoded_sections` list (the list itself was not printed).
- `known-missing-money-atoms.yaml` and `known-validation-gaps.yaml`: searched for the four sections in Latin and Hebrew forms; no entries.
- `LICENSE` and `LICENSE-CODE` (headers) and `NOTICE` (in full).
- No imported file was needed: the only `import` atoms in the four modules are s 36's, and they point at s 36's own rules.

**Read outside this row, reported so the other rows can judge.**
The search of `ENCODING-GAPS.md` printed two single lines (399 and 408) of an entry about s 66 (row IL-02).
The `no-executable-oracle` bullet, printed for its clause on ss 34, 36 and 36A, also states figures for ss 121, 121B and 66(c) (rows IL-03 and IL-02); they are not reproduced here.
The membership test on `encoded_sections` also showed that Axiom encodes s 120B (row IL-03); that module was not opened.
Rows IL-02 and IL-03 should treat themselves as exposed to those lines.
Nothing under `national-insurance-law-1995/` or `composed/`, no other section's module, and no `l4-ide/specs/research/AXIOM-*` was read.

### Licence

`NOTICE`: "Encodings, companion test cases, parameter values, and provenance metadata in this repository are licensed under the Creative Commons Attribution 4.0 International license (CC BY 4.0)"; tooling is under Apache 2.0 (`LICENSE-CODE`).
The YAML compared here is therefore CC BY 4.0.
Quotations below are short and attributed: Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation.
The manifests record that each of the four modules was machine-generated on 2026-09-06 (`"model": "gpt-5.6-terra"`, `"tool": "axiom-encode encode --apply"`).

### Axiom's encoding, briefly

One RuleSpec module per section.
s 33A: two parameters, `tax_credit_point_base_amount` = 504 (`unit: ILS`, `period: Year`) and `pension_point_monthly_divisor` = 12, and two `deferred_outputs`, the indexed credit-point amount and the pension-point monthly amount, declared and not computed.
s 34: `if individual_is_israeli_resident_in_tax_year: israeli_resident_tax_credit_point_count else: 0`, the count being 2.
s 36: the same input and 1/4, held as a numerator 1 over a denominator 4.
s 36A: `if individual_is_woman: woman_tax_credit_point_count else: 0`, the count being `1 / 2`.
Every version is `effective_from: '0001-01-01'`.
Each source atom carries a Hebrew excerpt and a corpus citation path, not a line number.
The companion tests are two per section for ss 34, 36 and 36A, one on each side of the condition, and none for s 33A (its file is `[]`).
Axiom's encoding was not executed: its answers below are read off its formulas.

### Where the two agree

Every number: 504 (line 1563), 12 (line 1564), 2 (line 1570), 1/4 (line 1594), 1/2 (line 1597).
Every fork that both had to take was taken the same way:

- F1, s 36A has no residence condition (line 1597). Axiom's gap entry: "§36א states no residence requirement and the encoding does not add one" (`ENCODING-GAPS.md` lines 519–520).
- F2, s 36 has no earning or travel condition (line 1594). Axiom conditions s 36 on residence alone.
- F3, s 36's "יחיד תושב ישראל" is residence in the tax year. Axiom's s 36 reads an input named `individual_is_israeli_resident_in_tax_year`, the s 34 name, though its excerpt is "יחיד תושב ישראל".
- F4, residence is one Boolean per tax year, never apportioned.
- F8, the points are computed from the facts, with no claim or proof.
- F9, "אשה" is an input.
- Residence under s 1 (lines 143–163) is an input in both; neither encodes the test.

Two readers taking the same reading is not evidence that the reading is right; Q1 and Q2 stay open.
Axiom's text is a Wikisource revision with `expression_date` 2026-06-08 (coverage map); its excerpts of these four sections match lines 1563–1597 of our bundle word for word.
Its s 34 summary reorders the sentence, and its s 33A summary stops at "בסעיף 120א." and leaves out the set-off limb; no difference in the source text itself was found.

### Divergence table

Classes: ours wrong, theirs wrong, genuine ambiguity, scope difference (one covers what the other does not), representational difference (same answer, different shape).
Where the text does not decide, the row says so and names no winner.

| id | provision | ours | theirs | source lines | class | proposed repair to ours |
| --- | --- | --- | --- | --- | --- | --- |
| X01 | s 48, reached from ss 34 and 36: a non-resident individual who is an Area resident and not an Israeli citizen | ss 34 and 36 refuse: `section 48 and the order made under it are not encoded in this model` | no Area input; the caller enters `individual_is_israeli_resident_in_tax_year: false` and gets 0 and 0 | 1807 (the power); 1808 (Wikisource note, not law: the 5755-1995 order was published and applies ss 34, 36 and 37 "כאילו היו תושבי ישראל") | scope difference. The bundle's operative text gives only a power and does not decide the case; if the order is in force as the note says, Axiom's 0 is wrong. | none |
| X02 | s 48A, reached from ss 34, 36 and 36A: a foreign worker whom a section would credit | refuses: `section 48A and the regulations made under it are not encoded in this model` | no foreign-worker input: 2, 1/4 and, for a woman, 1/2 | 1811 (power to disapply wholly or partly, "אף אם רואים אותו כתושב"); 1812 (note: Regulations 5775-2014 published) | scope difference. The bundle does not say what the Regulations do, so it does not decide whether Axiom's full points are right. | none |
| X03 | s 33A "נקודת זיכוי", limb (3), "המקוזז כנגד המס לאותה שנה" | `max 0 (tax − amount)` (F5) | not encoded; the module summary leaves the words out | 1563 | scope difference | none |
| X04 | s 33A, a number of points as an amount in NIS | points × the year's value, the value an input with no default | `tax_credit_point_amount` is a deferred output, not computed | 1563 | scope difference | none |
| X05 | s 33A "נקודת קיצבה", limbs (1)–(3) | limb (3), the division by twelve, computed from an input that stands for limbs (1)–(2) | the divisor 12 as a parameter; `pension_point_monthly_amount` deferred | 1564 | scope difference | none |
| X06 | s 33A "נקודת קיצבה", its English name | "allowance point"; no period stated | "pension point", and "monthly" | 1564 ("ומחולק בשנים עשר", divided by twelve; the word "month" does not appear); 1559 ("קיצבאות ילדים", child allowances, in the Chapter's heading) | representational. "Monthly" is a gloss the text does not state; no answer depends on it. Our row IL-03 also says "pension point" (§7 above). | none; choose one English name at IL-07 |
| X07 | s 33A, the indexation cross-reference | records that "כאמור בסעיף 120א" lands on a deleted definition and that s 120B(a) indexes credit-point amounts (F6) | its deferral reason cites "the indexation mechanics referenced in section 120A" | 1563; 4329 ("מדד" – "(נמחקה)"); 4338 | representational. The letter of s 33A says 120A and the working indexation is s 120B; neither encoding computes it, so no answer depends on it. | none |
| X08 | the aggregates | `the credit points under sections 34 and 36` (the aggregate s 134A(2) names) and `the credit points under sections 34, 36 and 36A` | none; each section stands alone | 4864 | scope difference | none |
| X09 | the year's credit-point value | the Tax Authority's published figures (2,904 for 2025; 242 a month for 2024–2026), labelled as not law | none in these four modules | not statute; see `ito-credit-points-published-figures.l4` | scope difference | none |
| X10 | who is the taxpayer | `Person` is an individual or a body of persons; a body of persons gets 0 | no such distinction; the inputs are named `individual_is_…` and the entity is `Person` | 108, 124 (s 1 "אדם", "חבר בני אדם"); 1570, 1594 ("יחיד") | representational; the same answer once a caller enters FALSE for a company | none |
| X11 | the residence fact | one field, read by ss 34 and 36 | one input per module: `section-34#input.individual_is_israeli_resident_in_tax_year` and `section-36#input.…` are separate keys in its tests, so the two could be fed different values; how Axiom's composer binds them was not read | 1570, 1594 | representational | none |
| X12 | the type of a number of points | `NUMBER`, written 1/4 and 1/2 as the text writes them | `dtype: Count`, holding 0.25 and 0.5 | 1594, 1597 | representational | none |

Two further rows are not divergences: the encodings agree, and on the text both are wrong or both overreach.

| id | provision | ours | theirs | source lines | class | proposed repair to ours |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | s 3A(f): an Israeli citizen who is an Area resident, or who operates in the Area, and is not an Israeli resident under s 1 (independent finding S09) | 0 under s 34 and 0 under s 36, with no refusal; the comment on `an Israeli resident in the tax year` tells the caller to enter the s 1 status | 0 and 0: no Area input, and its gap entry ties residence to the s 1 definition; s 3A is not among the coverage map's `encoded_sections` | 471 ("יחולו על אזרח ישראלי שהוא תושב אזור או פועל באזור, הוראות פקודה זו כאילו היה תושב ישראל"); 455–458 ("אזרח ישראלי" includes (2) every Israeli resident and (3) a person entitled under the Law of Return who is an Area resident); 1807 (s 48 takes "אזור", "תושב אזור" and "אזרח ישראלי" from s 3A) | ours wrong and theirs wrong: on the words, s 34 gives 2 and s 36 gives 1/4 | R1 |
| S2 | the tax year | no rule takes a date; §1 above says the encoding answers any year since 5764 | every version `effective_from: '0001-01-01'`; the coverage map says `temporal_coverage: current_expression_only` | 1561, 1569, 1593, 1596 (the amendment lists; the bundle carries no earlier text) | both answer years whose text the bundle does not carry, before the last listed amendment and before 1961; for current years both are right | R2 |

Counts: 12 divergences, of which 0 ours wrong, 0 theirs wrong, 0 genuine ambiguity, 7 scope differences (X01–X05, X08, X09) and 5 representational differences (X06, X07, X10–X12); and 2 shared defects (S1, ours and theirs wrong; S2, both overreach).

### Axiom's test cases through our encoding

Run in a scratch copy as `axiom-cases.l4`, which imports our nouns and ss 34/36/36A modules unmodified; the file is not deposited.
Axiom supplies one Boolean per case and our `Individual` takes four, so the fact Axiom does not supply (sex for ss 34 and 36, residence for s 36A) was run both ways, two assertions per case.
The two facts Axiom has no concept of, Area resident not a citizen and foreign worker, were FALSE.
Axiom's period (tax year 2024 or 2025) has no counterpart: our rules take no year.

| Axiom case | section | Axiom input | Axiom expects | ours | result |
| --- | --- | --- | ---: | --- | --- |
| `israeli_resident_receives_two_tax_credit_points` (2025) | 34 | resident: true | 2 | 2, for a man and for a woman | match |
| `nonresident_does_not_receive_resident_tax_credit_points` (2025) | 34 | resident: false | 0 | 0, both | match |
| `israeli_resident_receives_travel_tax_credit_points` (2024) | 36 | resident: true | 0.25 | 1/4, both | match |
| `nonresident_does_not_receive_travel_tax_credit_points` (2024) | 36 | resident: false | 0 | 0, both | match |
| `woman_receives_half_credit_point` (2025) | 36A | woman: true | 0.5 | 1/2, resident and non-resident | match |
| `non_woman_does_not_receive_woman_credit_point` (2025) | 36A | woman: false | 0 | 0, both | match |
| none | 33A | `[]` | — | — | no case |

`L4=/Users/mengwong/.local/bin/l4 ./check.sh` on the scratch copy, 2026-10-06 about 22:15 +08, binary sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`: `axiom-cases.l4` 0 errors, 12 satisfied, 0 failed, 0 refused; the other modules as before (58 and 78 satisfied).
Negative control: with one expectation changed from 0.25 to 0.3 the same harness printed 1 error, 11 satisfied, 1 failed.
6 of 6 cases match, 0 diverge, 0 could not be run.
The cases test only the two sides of each section's one condition; none touches a refusal, a body of persons, s 48, s 48A, s 3A(f) or an amount in NIS, so their passing says nothing about X01–X12, S1 or S2.

### What Axiom does that we do not

- A dated version per number (`versions: - effective_from: …`), so an amendment can be added as a new version; ours has no date mechanism (S2).
- A declared list of outputs it does not compute, each with a reason (`deferred_outputs`); ours takes the missing figures as inputs instead.
- Units and periods as metadata (`unit: ILS`, `period: Year`).
- Signed generation provenance per module: model, run, prompt hash, HMAC signature.
- A stated outside comparison: its `no-executable-oracle` entry says the OECD TaxBEN Israel description agrees on "the 2.25 basic credit points, which this encoding reaches as §34's two plus §36's quarter" and on "§36א's further half point for a woman". That agrees with our answer table; TaxBEN itself was not read.

### What we do that Axiom does not

- Reach ss 48 and 48A and refuse with a named reason (X01, X02).
- Compute s 33A's set-off, the amount in NIS and the allowance-point division (X03–X05).
- Distinguish a body of persons from an individual (X10).
- Provide the s 134A(2) aggregate and the slice total (X08).
- Carry the Tax Authority's published figures with provenance (X09).
- Record the stale s 120A reference (F6), a register of ten forks, and a coverage table of every provision met; carry 58 own and 78 independent assertions against Axiom's six cases.
- Cite the source by line number in every `@ref`; Axiom cites by excerpt.

### Proposed repairs to our encoding (not applied)

- **R1 (S1, s 3A(f)).** The repair the independent pass proposed for S09, widened to the whole of line 471, which covers an Israeli citizen who is an Area resident "או פועל באזור" (or who operates in the Area); S09 framed only the first limb.
  Either say in the comment on `an Israeli resident in the tax year` and in the `@export`'s `@desc` that such a person is entered as resident by force of s 3A(f), with "Israeli citizen" in the s 3A(a) sense (lines 455–459); or add a field for it and make ss 34 and 36 apply.
  Add a test for each limb.
  That "operates in the Area" reaches the personal credits is this author's reading of line 471; neither encoding tests it.
- **R2 (S2, the tax year).** Already proposed by the independent pass: say in §1 that the encoding answers every year, before 5764 too, or take the year and refuse before each section's last listed amendment.
  Axiom's `'0001-01-01'` is the same gap and no reason to keep ours.
- Nothing else. On every divergence the text either does not decide or our encoding is the more careful of the two.

### Bottom line

On what the four sections themselves say, the two encodings give the same answers: every number agrees, every fork both had to take was taken the same way, and all six of Axiom's cases pass through ours.
They differ in reach, not in reading.
Axiom stops at each section's own sentence and answers with full confidence for Area residents and foreign workers, where the answer turns on instruments the bundle does not hold; ours reaches those instruments and refuses, and also computes the three limbs of s 33A that Axiom defers.
Neither handles s 3A(f), and neither refuses a tax year whose text the bundle does not carry.
The comparison found nothing wrong in ours that the independent pass had not already found, and widens the S09 repair by one limb.
Axiom's six two-sided cases and empty s 33A test file are thin evidence either way, so the agreement here is two readers taking the same reading, not a check of that reading against the law.
