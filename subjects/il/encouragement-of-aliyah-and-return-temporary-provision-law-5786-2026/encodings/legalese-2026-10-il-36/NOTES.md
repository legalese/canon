# NOTES: the Encouragement of Aliyah and Return (Temporary Provision) Law, 5786-2026 (row IL-36)

Version 0.1.0, 2026-10-08.
Status `draft`: no domain expert has read this encoding against the source, and no independent test pass has been run.
Every expected value in `il36-tests.l4` was worked by hand from the Hebrew text before the module was run.

## 0. The text, and how it was read

The Law is chapter D of the 5786 Economic Efficiency Law, enacted by that Law's section 9 (Sefer HaChukim 3511, pp. 416-418).
It has six sections of its own, which section 9 prints inside quotation marks, and sections 8 and 9 of the enacting chapter name it and enact it.
The deposited PDF is `income-tax-ordinance-new-version/registers/source-bundle/amending-laws/25_lsr_12235101.pdf` (sha256 `72244dba261c44d2818f80708fa2dece5d8b99f75e788f48e290942ff4734155`, recomputed on 2026-10-08), PDF pp. 4-6.

**The PDF's text layer does not extract cleanly.**
`pdftotext -layout` returns the Hebrew words in logical order, one visual line at a time, with the margin notes (the section numbers and headings) interleaved on the same line.
It scrambles digits, hyphens and the parentheses around numerals: "(1)" comes out as "( )1", "2026 ותושב" as "2026ותושב", "התשי״ב-1952" as "התשי״ב1952-", "( 5בנובמבר  )2025" for "(5 בנובמבר 2025)".
So no quotation of the raw extraction could be trusted for paragraph numbers or figures.

**What was done instead.**
The three pages were rendered with `pdftoppm -r 110` and read as images, and the Law was transcribed from the images: `registers/source-bundle/encouragement-of-aliyah-and-return-law-5786-2026.he.txt` (sha256 `06d620400050687865427cd4c96813312f91d764fc48e4da16ff8ef772cec69c`), one printed clause per line, gershayim and geresh as ״ and ׳, superscript footnote marks omitted.
`tools/transcheck.py` checks that the multiset of Hebrew words and the multiset of digit runs of the transcription equal those of the PDF's own text layer for chapter D (it does not check order; order was checked by reading the images).
It prints `transcheck: OK` (run 2026-10-08).
The raw extraction is deposited beside it (`...pdftotext-layout.txt`, sha256 `749d94946e6a9b5a8aaf25198fc67ac6b45fb6a101e5ec66393cca7e3f5e64e9`) as provenance.
Every `-- src:N |` comment in the modules is generated from line N of the transcription by `tools/srcquote.py`; `tools/hebcheck.py` checks that every other run of Hebrew in the modules occurs verbatim in it (`hebcheck: OK`).
Every figure in this encoding was read off the page image: 600,000; one million; 350,000; 150,000; 140,000; 75; 5 November 2025; 31 December 2026 (end of tax year 2026); 1 January 2026.
The figures in the lead's task note all agree with the text.

**Toolchain.**
`l4` is `~/.local/bin/l4`, which resolves to `/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-6df1397b/bin/l4`, sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (the same at the start of the session, before and after the last `check.sh` run).
`JL4_LIBRARY_PATH` is unset.

## 1. What is encoded and what is not

**Encoded:** s 1 (the Law's own definitions: "עולה", "תושב חוזר ותיק", "קרוב", and the kind of income that is "הכנסה מזכה"); s 2(a) (who, which years, the ceilings, the election), (b) (the ceiling for income received from a relative), (c) (both kinds in one year), (d) (the pro rata of 2026), (e) (the day of first residence is found without ITO s 14(b)(1)); s 3 (a non-resident entity's business income) with its proviso and both exceptions; s 4; s 6.
**Inert:** s 5 (a savings clause about ITO ss 14 and 97), and ss 8 and 9 of the enacting chapter (the name and the enacting words).
**Out of scope, taken as inputs:** the Income Tax Ordinance's definitions of "resident", "chargeable income", "income from personal exertion", "other income", "relative", "material shareholder", "transparent corporation" and "veteran returning resident" (and the day a person became or ceased to be a resident); the Law of Return (an oleh visa or certificate), the Absorption Basket Law (a class entitled to a basket) and the Citizenship Law (s 11, cancellation).
Each input is one field of `il36-nouns.l4`, named for the provision that decides it.
The Ordinance's own text, deposited in the neighbouring subject, was consulted only for citations (ss 1, 2(1)-(2), 14(a)-(b), 62A(d), 64(a), 88).

Hebrew from the Ordinance, quoted in this file, was checked by `grep -F` against `income-tax-ordinance-new-version/registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt` on 2026-10-08 (the number is the line of that file):

```
-- ext:[ITO-117] | ״הכנסה חייבת״ – הכנסה לאחר הניכויים, הקיזוזים והפטורים שהותרו ממנה לפי כל דין;
-- ext:[ITO-1141] | לא יראו יחיד שהיה לתושב ישראל לראשונה או לתושב חוזר ותיק, כתושב ישראל, במשך שנה אחת מהמועד שבו עלה או שב לישראל
```

## 2. Coverage table

| provision | what it says | disposition | where | transcription line |
| --- | --- | --- | --- | --- |
| s 8 | the chapter is the Law, by its name | inert | quoted in `il36-s5-s6-commencement.l4` | 2-3 |
| s 9 | the Law's sections are as follows | inert | quoted in `il36-s5-s6-commencement.l4` | 4-5 |
| s 1 "בעל מניות מהותי" | ITO s 88 | input (the entity's `the individual is a material shareholder in the entity`) | `il36-nouns.l4` | 8 |
| s 1 "הכנסה אחרת" | ITO s 62A(d) | input (`other income as section 62A(d) ...`) | `il36-nouns.l4` | 9 |
| s 1 "הכנסה מזכה" | chargeable income from personal exertion under ITO s 2(1) or (2), not other income, not income attributed from a transparent corporation, except income attributed under s 62A | encoded; fork F2 on the exception; assumption A1 on "chargeable" | `il36-s1-definitions.l4` | 10 |
| s 1 "עולה" | an oleh visa or certificate, or a class entitled to an absorption basket, but not a person whose citizenship was cancelled under s 11 of the Citizenship Law | encoded over three input facts | `il36-s1-definitions.l4` | 11 |
| s 1 "הפקודה" | the Income Tax Ordinance | inert | - | 12 |
| s 1 "קרוב" | ITO s 88, except a company wholly owned by the immigrant | encoded over two input facts | `il36-s1-definitions.l4` | 13 |
| s 1 "תאגיד שקוף" | ITO s 64(a), in which the person is a material shareholder, but not one wholly owned by the person | input (`attributed ... from a transparent corporation`; the entity's `is a transparent corporation as section 1 of the Law defines the term`) | `il36-nouns.l4` | 14 |
| s 1 "תושב חוזר ותיק" | ITO s 14(a), and holding the Ministry's certificate | encoded over two input facts | `il36-s1-definitions.l4` | 15 |
| s 1 "תושב חוץ", "תושב ישראל" | as the Ordinance defines them | input (the day of becoming and of ceasing to be a resident; the entity's `is a non-resident entity`) | `il36-nouns.l4` | 16 |
| s 2(a) | the persons, the period, the years, the ceilings, the election | encoded | `il36-s2-exemption.l4` | 18-22 |
| s 2(b) | the ceiling for income received from a relative; fork F3 for 2030 | encoded | `il36-s2-exemption.l4` | 23 |
| s 2(c) | both kinds in one year; the total may not exceed the ceilings of (a); fork F6 | encoded | `il36-s2-exemption.l4` | 24 |
| s 2(d) | 2026: the ceilings of (a)(1) and (b) in proportion to the period of residence; forks F4, F5 | encoded | `il36-s2-exemption.l4` | 25 |
| s 2(e) | the day of first residence is found without ITO s 14(b)(1); fork F4 on what that leaves | encoded (the day is an input so determined) | `il36-nouns.l4`, `il36-s2-exemption.l4` | 26 |
| s 3(a) | a non-resident entity's business income produced in Israel through the person's exertion, 2026-2030, is exempt; the proviso; fork F7 | encoded | `il36-s3-entity.l4` | 28 |
| s 3(b)(1) | not where the person is a material shareholder in the entity | encoded | `il36-s3-entity.l4` | 30 |
| s 3(b)(2) | for a transparent corporation, not the part attributed to Israeli-resident rights-holders | encoded | `il36-s3-entity.l4` | 31 |
| s 4 | the Law does not apply, from commencement, to a person who ceased to be a resident in 2028 or 2029 and stayed fewer than 75 days in one of those years; forks F8, F9 | encoded | `il36-s4-departure.l4` | 33 |
| s 5 | the Law does not derogate from ITO ss 14 and 97 | inert (a statement about other law; foreign income is outside this Law) | `il36-s5-s6-commencement.l4` | 35 |
| s 6 | commences 1 January 2026; applies to qualifying income from the day of first residence | encoded | `il36-s5-s6-commencement.l4` | 37 |

No row is left `deferred`.

## 3. The modules

| module | what it holds |
| --- | --- |
| `il36-nouns.l4` | `DECLARE` only: the individual, the item of income, the entity and its items, the eight reading enumerations, `The readings`, `A fork` |
| `il36-s1-definitions.l4` | s 1: immigrant, veteran returning resident, relative, qualifying income by its kind (reading F2) |
| `il36-s4-departure.l4` | s 4 at concrete readings (F9) |
| `il36-s5-s6-commencement.l4` | s 5 (inert), ss 8-9 (inert), s 6 |
| `il36-s2-exemption.l4` | s 2: the period, the ceilings, residence on a day, the pro rata, the exempt amount at concrete readings |
| `il36-s3-entity.l4` | s 3 at concrete readings |
| `il36-answers.l4` | the refusals by name; the default readings; the resolution of declined readings; the public questions |
| `il36-builders.l4` | builders for the records, for callers (not law) |
| `il36-tests.l4` | the tests (262 assertions) |

The rules of ss 1-4 take a record of concrete readings and are never called by a caller directly (a rule handed a declined reading refuses with a message that says so).
`il36-answers.l4` is where a declined switch is resolved: the question is asked at each concrete reading of the declined switch, and answered if the readings agree, refused by name if they do not.
A switch the question does not depend on is never expanded.

## 4. Fork register

Meng's ruling (SHRUG, 2026-10-08): where the text is silent or ambiguous, one named switch per ambiguity, the default a refusal by name, the other readings kept by name and tested; a default declines only where the readings give different answers to the question asked.
Forks F2 to F9 are switches in `The readings`.
F1 and F10 to F16 are not switches: each is the text deciding, or an assumption the encoding makes, and each is listed so a reviewer can disagree with it.

| fork | the ambiguity | readings | default | the text that licenses each reading |
| --- | --- | --- | --- | --- |
| **F2** | the exception in "הכנסה מזכה" for income attributed under s 62A | (A) it is an exception to the exclusion of income attributed from a transparent corporation: such income IS qualifying; (B) it is a further exclusion: such income is NOT qualifying | decline, where an item is attributed from a transparent corporation under s 62A (an exempt amount that includes it differs) | line 10: "ואינה הכנסה המיוחסת לעולה או לתושב חוזר ותיק מתאגיד שקוף, למעט הכנסה מתאגיד שקוף המיוחסת לעולה או לתושב חוזר ותיק לפי סעיף 62א לפקודה". (A) follows the position of the exception after the second exclusion. (B) reads "למעט" as governing the whole definition; it then adds nothing, because the second exclusion already removes the income. |
| **F3** | s 2(b) replaces paragraphs (1) to (3) of s 2(a), "בשנות המס 2026 עד 2029", and not paragraph (4), the ceiling for 2030 | (A) paragraph (4) stands: income received from a relative in 2030 has the ceiling of 150,000; (B) the 140,000 holds in 2030 too | decline, where relative-sourced qualifying income in 2030 exceeds 140,000 and the total ceiling does not hide it | line 23. (A) is the literal text and leaves the relative ceiling in 2030 higher than in 2029. (B) is what the purpose of a lower ceiling for relatives suggests. |
| **F4** | ITO s 14(b)(1): an individual who elects it is not treated as an Israeli resident for one year from arrival (the adaptation year); s 2(e) disapplies it only "לעניין בחינת המועד" of first residence | (A) in the elected year the person is not a resident for "בעת שהיו תושבי ישראל" (s 2(a)) and for the period of residence (s 2(d)); (B) the person is a resident throughout | decline, for a person with an elected adaptation year whose income or share falls in it | lines 18, 25, 26. (A): s 2(e) is limited to the date test, so elsewhere s 14(b)(1) applies. (B): s 2(e) shows the legislator did not want the election to cost the exemption. |
| **F5** | s 2(d): "באופן יחסי לתקופת תושבותם בישראל בשנה האמורה"; no unit | (A) days: days of residence in 2026 over 365; (B) months: calendar months of 2026 with at least one day of residence over 12 | decline, wherever the prorated ceiling binds and the readings differ | line 25. The text gives no unit. |
| **F6** | s 2(c) caps the total at "תקרות ההכנסה המנויות בסעיף קטן (א)"; s 2(d) prorates "על אף האמור בסעיפים קטנים (א) ו־(ב)" and does not mention (c) | (A) the total cap in 2026 is the ceiling of (a)(1) prorated under (d); (B) it is 600,000 as listed in (a) | decline, for a mixed 2026 where the sum of the two kinds passes the prorated ceiling | lines 24, 25. |
| **F7** | s 2(a) exempts income "בעת שהיו תושבי ישראל"; s 3(a) has no such words | (A) an entity's business income is exempt only if produced while the person was an Israeli resident (s 6's start day and the residence tests of s 2); (B) whenever produced in tax years 2026 to 2030 | decline, where an entity's item is dated before the person became, or after the person ceased to be, a resident | lines 18, 28, 37. |
| **F8** | s 4: "הוראות חוק זה לא יחולו" and "על יחיד"; s 3's exemption is the entity's | (A) s 4 takes away the exemption of s 3 for an entity's income earned through that individual; (B) it does not | decline, where s 4 applies to the person and an entity item would otherwise be exempt | lines 28, 33. |
| **F9** | s 4: "ושהה בישראל פחות מ־75 ימים באחת מאותן השנים" | (A) fewer than 75 days in either 2028 or 2029, whichever year the person ceased to be a resident; (B) fewer than 75 days in the year the person ceased to be a resident | decline, where the person stayed 75 days or more in the year of ceasing and fewer in the other | line 33. |
| F1 | "הכנסה חייבת" is, by ITO s 1, income after the exemptions allowed under any law (ext:[ITO-117] below), which would include this Law's own; read so, nothing could be both exempt and qualifying | ASSUMPTION A1 (not a switch): the input `chargeable income apart from this Law's own exemption` is the answer before this Law's exemption | the input is the caller's | line 10; ITO s 1 "הכנסה חייבת" (Ordinance transcription line 117). The other reading makes the Law inoperative. |
| F10 | s 4 says "מיום תחילתן": from the commencement, 1 January 2026 (s 6) | TEXT DECIDES: when s 4 applies, the exemption of every tax year from 2026 is lost, including years before the departure | - | line 33: a retrospective clawback that turns on facts of 2028 or 2029. A reading "from the day the person ceased to be a resident" contradicts the words. |
| F11 | the day of ceasing to be a resident; one span of residence | ASSUMPTION A2: the person is a resident from the day of first residence to the day BEFORE the day of ceasing (the input is the first day of non-residence); the span is continuous (a person who ceased and returned is not represented) | the input | lines 18, 33. |
| F12 | years the paragraphs do not list | TEXT DECIDES: 0. Income of 2025 (including 5 November to 31 December 2025, after the day s 6 starts applying) and of 2031 on is not exempt: s 2(a) exempts "בשנות המס המפורטות בפסקאות (1) עד (4)" only | - | lines 18-22, 37. A reader might see s 6's start day in 2025 as a gap; it is not one, because s 2(a) lists no ceiling for 2025. |
| F13 | s 3(a) proviso: "לא הייתה הכנסה מעסק שהופקה בישראל אלמלא יגיעתו האישית" | ASSUMPTION A4: tested over the items supplied for the entity, of whatever year (the text does not say whether it is tested year by year) | the supplied items | line 28. |
| F14 | the election "אלא אם כן ביקשו אחרת, לעניין ההכנסות, כולן או חלקן" | TEXT DECIDES, the shape is the encoder's: the election is a part of each item's amount (all, some or none), so the part is neither exempt nor counted against the ceiling | the item's field | line 18. |
| F15 | the adaptation year, when elected, one year from the day of ascending or returning (ext:[ITO-1141] below) | ASSUMPTION A3: from the arrival day to the day before its first anniversary (`add years` day 1, less one day) | the input day | ITO s 14(b)(1) (Ordinance transcription line 1141). |
| F16 | "מקרוב" in s 2(b): "income received from a relative" | ASSUMPTION A5: the payer of the item is a relative (the item's own fact) | the item's field | line 23. |

How a declined switch behaves (all examples are tests):
- A full-year resident of 2026 is not split by F4, F5 or F6: every default answers.
- A person who became a resident on 1 July 2026 is answered by default for an item of 200,000 (below both prorated ceilings), and refused by name, F5, for an item of 400,000 (302,465.75 on days against 300,000 on months).
- An item attributed from a transparent corporation under s 62A splits F2: A 200,000, B 0, default refused.
- A switch the question does not depend on never matters: an entity's exempt income is refused on F9 only where F8 is at its first reading.
- Where two switches split a question the first in the list of its forks is named (the share of 2026 for a person with an elected adaptation year: F4 before F5).

## 5. The answer table

The ceilings, in new shekels, from lines 19-23.

| tax year | s 2(a) ceiling (income not received from a relative) | s 2(b) ceiling (received from a relative) |
| --- | --- | --- |
| 2025 and before | none: nothing is exempt | none |
| 2026 | 600,000 (line 19), in proportion to the period of residence (line 25) | 140,000 (line 23), in proportion likewise |
| 2027 | 1,000,000 (line 20) | 140,000 |
| 2028 | 1,000,000 (line 20) | 140,000 |
| 2029 | 350,000 (line 21) | 140,000 |
| 2030 | 150,000 (line 22) | 150,000 (F3 reading A) or 140,000 (reading B); declined by default |
| 2031 on | none | none |

The 2026 ceiling of s 2(a)(1) for a person who became a resident on a day in 2026 (not asserted as amounts except for 1 July; the shares are asserted):

| became a resident on | days of residence in 2026 | ceiling on days | months | ceiling on months |
| --- | --- | --- | --- | --- |
| on or before 1 January 2026 | 365 | 600,000 | 12 | 600,000 |
| 1 July 2026 | 184 | 110,400,000 / 365 = 302,465.75 | 6 | 300,000 |
| 15 July 2026 | 170 | 102,000,000 / 365 = 279,452.05 | 6 | 300,000 |
| 1 December 2026 | 31 | 18,600,000 / 365 = 50,958.90 | 1 | 50,000 |
| 31 December 2026 | 1 | 600,000 / 365 = 1,643.84 | 1 | 50,000 |

Section 2(c) for 2026, a person who became a resident on 1 July 2026 with 300,000 not from a relative and 100,000 from a relative, F5 at days: the ordinary ceiling is 302,465.75 (the 300,000 is under it), the relative ceiling 25,760,000 / 365 = 70,575.34, together 135,260,000 / 365 = 370,575.34; the total cap is 110,400,000 / 365 = 302,465.75 (F6 reading A) or 600,000 (reading B), so the exempt amount is 302,465.75 or 370,575.34.
On months the ceilings are 300,000 and 70,000, together 370,000, and the exempt amount is 300,000 or 370,000.

Section 3 states no ceiling: a non-resident entity's business income through the person's exertion is exempt in full in each of tax years 2026 to 2030 (tested at 1,000,000 in 2027 and 2,000,000 in 2026).

Section 4's days: fewer than 75 (74 and below) switch the Law off; 75 do not.

## 6. What `check.sh` prints

Run 2026-10-08T22:40:49Z to 22:41:03Z, `l4` sha256 `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` before and after, exit 0:

```
module                                    errors satisfied  failed  refused  expected
il36-answers.l4                                0         0       0        0         0
il36-builders.l4                               0         0       0        0         0
il36-nouns.l4                                  0         0       0        0         0
il36-s1-definitions.l4                         0         0       0        0         0
il36-s2-exemption.l4                           0         0       0        0         0
il36-s3-entity.l4                              0         0       0        0         0
il36-s4-departure.l4                           0         0       0        0         0
il36-s5-s6-commencement.l4                     0         0       0        0         0
il36-tests.l4                                  0       262       0        0         0
TOTAL (9 modules)                              0       262       0        0
```

No assertion is expected to fail or to refuse; none does.
`#ASSERT REFUSED` assertions (each satisfied) are counted among the 262; those with a `BECAUSE` check the exact message, so they check which fork the refusal names.
No warning-severity diagnostic is printed by any module.
During the first full run one assertion failed: the share of 2026 for a person with an elected adaptation year, at the default, was expected to be refused on F4 and was refused on F5.
Both forks split that question; the code named the deeper one, the design comment promised the first in the list.
The code was changed (the resolution now names the first declined fork that surely splits), the expected value was not (NOTES.md section 7).

## 7. Findings during the work

- The PDF's text layer garbles digits and parentheses (section 0); the Law was transcribed from the page images.
- A question split by two forks, one nested in the other, was first reported on the nested fork. The resolution in `il36-answers.l4` now reports the outer fork where one reading of it leaves the answer undecided and the other gives one answer (that answer cannot agree with all the undecided ones, so the outer fork splits), and the nested fork where both readings leave it undecided. The test that found it is `the share of tax year 2026 ... Pm BECAUSE fork F4`.
- The Law's citizenship exclusion cites s 11 of the Citizenship Law; the capstone's (row IL-07) immigration record cites s 10(d) (for ITO s 35). They are different provisions for different purposes and are not reconciled here.

## 8. How a caller uses it, and what the capstone would need

Entry points, all in `il36-answers.l4` (each has a `, reading` form taking `The readings`, and a default form):
- `the exempt amount of the person's qualifying income` person `items` items `in the tax year` year: the amount of the year's qualifying income that is exempt, in shekels.
- `the qualifying income of the person ...`, `the share of tax year 2026 for which the person was an Israeli resident`, `the ceiling on the exemption of the person's income not received from a relative`, `the person is within section 2(a)`, `section 4 switches the Law off for the person`, `the exempt business income of the entity` (s 3).
- Builders in `il36-builders.l4` (`an immigrant who first became an Israeli resident on` day; `an employment income of` amount `produced on` day).

What the capstone (row IL-07) holds, against what this encoding takes:
- The capstone holds s 35's immigration record: the ground (a Law of Return visa or certificate; a returning resident with six years abroad; another ground), whether citizenship was cancelled under ITO s 10(d), the day, and whether it was the first time.
- This encoding needs, for the person: whether the person holds a visa or certificate or is in a basket class (the capstone's ground, if it is the Law of Return one, maps to the first; its other grounds do not say); whether citizenship was cancelled under **s 11 of the Citizenship Law** (the capstone's field cites 10(d)); for a veteran returning resident, ITO s 14(a)'s **ten** consecutive years abroad (the capstone holds six, which is row IL-08's returning resident, not the veteran) and the Ministry's certificate; the day of first residence found without ITO s 14(b)(1); whether the person elected the adaptation year, and from when; the day of ceasing to be a resident, if any, and the days in Israel in 2028 and 2029.
- For each income item: its day, amount, source (ITO s 2(1), (2) or other), whether it is chargeable income before this exemption, income from personal exertion, other income, attributed from a transparent corporation or under s 62A, produced in Israel, received from a relative, and the part the person asked not to have exempted.
- The capstone computes **monthly** net pay; the exemption is **annual** (a ceiling per tax year, in proportion in 2026).
  The earner's items for the year are needed to find the exempt amount; for a salary of a constant month the annual exempt amount can be spread.
  How the capstone annualises is not decided here.
- The earner's day of becoming a resident may differ from the immigration day in s 35's record (an arrival, an oleh certificate date); the capstone's own comment records this.
- Entry point: `the exempt amount of the person's qualifying income` with the earner's year of items; at the default readings it refuses by name where the Law's readings differ and answers where they agree, so a capstone that wants an answer for every earner must choose the readings (`, reading` form) and say so.

## 9. Open questions for a domain expert

1. F1 (`הכנסה חייבת`): confirm the workable reading, that the exemption applies to income that is chargeable before it.
2. F2: how a "transparent corporation" income attributed under s 62A reaches an immigrant, and whether the exception was meant to make such income qualifying.
3. F3: whether the 150,000 of paragraph (4) was meant to stand as the ceiling for income received from a relative in 2030, above the 140,000 of the years before.
4. F4: whether an immigrant who elects the adaptation year of ITO s 14(b)(1) loses, for that year, the exemption and the proration (this is the largest practical question: it makes the election cost up to a year of exemption).
5. F5: days or months for the 2026 proration.
6. F6: whether s 2(d) prorates the total cap of s 2(c).
7. F7 and F8: whether s 3's exemption is conditioned on the person's residence on the day the entity's income is produced, and whether s 4 disapplies it.
8. F9: which year's days s 4 counts (and, not a switch: whether "stayed in Israel" counts the whole year's days, as the input does, or only the days after ceasing to be a resident).
9. F10: that s 4 claws back the exemption of years before the departure (from "מיום תחילתן"); how the Authority would assess it in 2029.
10. A4: whether the s 3 proviso is tested year by year.
11. A person who ceased to be a resident and became one again is not represented (assumption A2).
12. A person who is both an immigrant and a veteran returning resident, with two days of becoming a resident, is not represented (one day is input; the residence span runs from it).
13. The Law has no updating clause and no ceiling for 2031; nothing here indexes the ceilings.
14. The Law does not say whether a ceiling is per person or per household; each ceiling here is per individual, as each "עולה" is an individual.

## 10. Not reviewed

HG1 (a domain expert reading the modules against the source) has not been sought.
No independent test pass has been run; an independent tester is to write answers from the Hebrew without opening this encoding, and each disagreement is to be classified against the forks above.
Nothing from the Axiom Foundation or any RuleSpec repository was read.
