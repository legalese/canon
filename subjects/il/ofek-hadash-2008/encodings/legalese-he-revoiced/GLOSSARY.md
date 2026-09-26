# Ofek Hadash — the Hebrew term contract

**What this is.** Every backtick identifier in the eight-module English encoding at
`../legalese/`, with the Hebrew name the Hebrew re-encoding at `../legalese-he-revoiced/` (renamed from `legalese-he/` on 2026-09-19; see NOTES.md) must use for it.
`glossary.json` is the machine-readable form of the same table; the two are generated together and
must not drift apart.

**Status: the term contract, not a translation.** Five agents translate modules in parallel against
this file. If an identifier is here, use exactly the string in the Hebrew column — do not improve
it locally. If an identifier is *not* here, that is a bug in this file: say so rather than
inventing a name, because the same invention will not be made twice.

**Scope, measured.** 373 distinct backticked identifiers across the eight modules
(`ofek-domain`, `ofek-salary-table`, `ofek-placement`, `ofek-worktime`, `ofek-supplements`,
`ofek-fiscal-2025`, `ofek-pay`, `ofek-cases`), extracted mechanically. There are **no** bare
declared names anywhere in the encoding: every declaration, field, parameter, constructor and
`§`/`§§` title is backticked, so the backtick sweep is the whole population. 365 are renamed; 8 are
deliberately kept (the seven module names, and `is before`, which is defined in the imported
`daydate` library, not here).

**Verified.** All 365 Hebrew names were written into a probe `.l4` file and run through the `l4`
binary at `l4wt/ofek-build`: zero `DiagnosticSeverity_Error` lines. That establishes only that they
lex and parse as identifiers — not that any encoding built from them is correct.

---

## Conventions

**The English encoding is the oracle.** Renaming is all that happens. Every numeric assertion keeps
its exact value; if a number moves, that is a bug in the translation, not a glossary question.

**Grounded in the instruments first.** A term marked `corpus` appears in the Ofek Hadash corpus at
`~/src/ofek-hadash-corpus` and the note says where — mostly the 2008 base agreement
(`agreements/ofek-hadash/2008-12-25_ofek-hadash_base-agreement.html`), the 2022 wage agreement and
its signed appendices, the 2026 approved agreement, and the printed salary tables. A term marked
`composed` has no counterpart in any instrument and the note says why; those are the ones a reviewer
should read first.

**Article citations keep their printed form.** `section 36(e)` becomes `סעיף 36(e)`, not
`סעיף 36(ה)`. The instruments themselves letter their sub-paragraphs in Hebrew — `(א)`, `(ג)`,
`(ט)` — so this is a deliberate departure, taken so that a citation is one greppable string across
the English encoding, the Hebrew encoding, the comments and this file. It is flagged in Open
questions; if it is ruled the other way it can be swept mechanically, which is exactly why it must
be uniform now.

**Definiteness carries the role the English article carries.** L4 needs the type, the record field
and the free parameter to be three distinct strings, and English gets that from `a stage of
education` / `stage of education` / `the stage`. Hebrew gets it the same way:

| role | form | example |
| --- | --- | --- |
| type / enum constructor | indefinite | `שלב חינוך`, `מורה`, `טבלת שכר` |
| record field | definite construct | `שלב החינוך`, `ההסמכה` |
| free parameter, function | definite head | `השלב`, `המורה`, `הטבלה` |

**Two instrument synonyms, split by role.** The agreement uses **היקף משרה** (§ 27) and **חלקיות
משרה** (§ 27(g)) interchangeably for the same quantity, and the English encoding needs two names for
it. So: `fraction of a full post` (the `מורה` record field) is **`היקף המשרה`**, and `the fraction
of a full post` (the free parameter threaded through `ofek-worktime`, `ofek-supplements` and
`ofek-fiscal-2025`) is **`חלקיות המשרה`**. Both are the agreement's own words. Do not swap them.

**"Step" is two different things and gets two different words.** In `ofek-salary-table` a *step* is
the percentage printed in the table's margin — `שיעור העלייה בוותק של`, `שיעור העלייה בדרגה`. In
`ofek-fiscal-2025` § 16 a *seniority step* is the annual increment the reduction withholds —
`קידום הוותק`, `שווי קידום הוותק`. They must not converge.

**Never end an identifier with a one-letter Hebrew particle.** An L4 identifier applied to an
argument is followed by a space, so a name ending in `ל`/`ב`/`מ`/`ש`/`כ`/`ו`/`ה` renders as
`… ל המורה`, which is not Hebrew. Function names therefore end in a standalone word — `עבור`,
`של`, `לפי`, `בטבלה`, `בתאריך`. Every name in this file was checked for this mechanically.

**No bidi control characters, ever.** RLM (U+200F) and LRM (U+200E) are a lex error inside
backticks. Geresh `׳` (U+05F3), gershayim `״` (U+05F4), maqaf `־` (U+05BE), the em dash `—` and
ASCII digits, parentheses and hyphens were all probed and all work. Rely on the viewer's bidi
algorithm for display.

**Filenames stay ASCII.** `ofek-domain.l4`, `ofek-pay.l4` and the rest keep their names, and the
seven `IMPORT` identifiers keep theirs with them. Hebrew goes inside files.

**Gender.** Identifiers are written in the masculine, which is what the agreements use and what
their own § 2 ("בכל מקום בהסכם זה בו דובר בלשון זכר, הכוונה גם ללשון נקבה") licenses. The three
case fixtures are the exception: `יעל`, `דבורה` and `נעה` take feminine agreement in their own
section titles, because they are named women.


## Names that are NOT translated

| identifier | why it stays |
| --- | --- |
| `ofek-domain` | module name in IMPORT; filenames stay ASCII (see brief) |
| `ofek-salary-table` | module name in IMPORT; filenames stay ASCII (see brief) |
| `ofek-placement` | module name in IMPORT; filenames stay ASCII (see brief) |
| `ofek-worktime` | module name in IMPORT; filenames stay ASCII (see brief) |
| `ofek-supplements` | module name in IMPORT; filenames stay ASCII (see brief) |
| `ofek-fiscal-2025` | module name in IMPORT; filenames stay ASCII (see brief) |
| `ofek-pay` | module name in IMPORT; filenames stay ASCII (see brief) |
| `is before` | defined in the imported daydate library (daydate.l4:738), not in this encoding — renaming it breaks the import |

## `ofek-domain.l4` — the shared ontology

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `Ofek Hadash — the shared ontology` | `אופק חדש — האונטולוגיה המשותפת` | composed | section title |
| `Who the reform applies to` | `על מי חלה הרפורמה` | corpus | § 3 'הסכם זה יחול על כל העובדים המדורגים בדירוג עובדי הוראה' |
| `a teaching qualification` | `רמת הסמכה` | composed | § 7(f)-(h) name the statuses (מורה מוסמך / מורה בכיר / מורה בלתי מוסמך) but give no collective noun; 'הסמכה' is theirs, 'רמת' is added |
| `academic — holds a recognised first degree` | `אקדמאי — בעל תואר ראשון מוכר` | corpus | § 7(d),(e), § 36(c) 'מורה בעל תואר ראשון' |
| `academic — holds a recognised second degree` | `אקדמאי — בעל תואר שני מוכר` | corpus | § 36(c) 'מורה בעל תואר שני' |
| `academic — holds a doctorate` | `אקדמאי — בעל תואר שלישי` | corpus | § 36(d) 'מורה בעל תואר שלישי (ד"ר)' |
| `certified but not academic` | `מורה מוסמך שאינו אקדמאי` | corpus | § 7(f) 'מורה מוסמך' (mo're musmach) |
| `senior certified but not academic` | `מורה בכיר שאינו אקדמאי` | corpus | § 7(g) 'מורה בכיר' (mo're bachir) |
| `unqualified` | `מורה בלתי מוסמך` | corpus | § 7(h) 'מורה בלתי מוסמך' |
| `a salary table` | `טבלת שכר` | corpus | § 35 'טבלת השכר המשולב', § 36 'שיבוץ בטבלאות השכר' |
| `the BA table — rating code 101` | `טבלת תואר ראשון — קוד דירוג 101` | corpus | table heading: 'טבלת שכר למורים בעלי תואר BA (קוד דירוג 101)'; § 36(c) 'טבלת השכר לבעלי תואר ראשון' |
| `the MA table — rating code 102` | `טבלת תואר שני — קוד דירוג 102` | corpus | table heading: 'טבלת השכר למורים בעלי תואר MA (קוד דירוג 102)' |
| `how the teacher entered the reform` | `אופן הכניסה לרפורמה` | composed | §§ 7(i)-(j) distinguish מורה קיים / מורה חדש; the collective noun is composed |
| `a new teacher placed under section 36` | `מורה חדש ששובץ לפי סעיף 36` | corpus | § 7(j) 'מורה חדש'; § 36(a) 'ישובצו בטבלאות השכר בדרגה 1 ובותק 0' |
| `an existing teacher converted under sections 43 to 50` | `מורה קיים שהומר לפי סעיפים 43 עד 50` | corpus | § 7(i) 'מורה קיים'; § 43 'ההמרה' (hamara) |
| `a stage of education` | `שלב חינוך` | composed | §§ 15 and 17 name the two stages; the collective noun is composed |
| `a primary school` | `בית ספר יסודי` | corpus | § 15 'מורה בבית-ספר יסודי' |
| `a junior high school` | `חטיבת ביניים` | corpus | § 17 'מורה בחטיבת ביניים' |
| `a role carrying a supplement` | `תפקיד המזכה בגמול` | corpus | § 39 heading 'גמולי תפקיד אשר ימשיכו להתקיים ברפורמה' |
| `homeroom teacher of a class other than the first grade` | `מחנך כיתה שאינה כיתה א׳` | corpus | 2022 § 10.1.1.1 '10% מהשכר המשולב למחנך כתה שאינה כתה א׳' |
| `homeroom teacher of a first-grade class` | `מחנך כיתה א׳` | corpus | § 39(a)(2) 'מחנך כיתה א׳' |
| `subject coordinator` | `רכז מקצוע` | corpus | § 39(a)(5) 'רכז מקצוע' |
| `road-safety coordinator` | `רכז זהירות בדרכים` | corpus | § 39(a)(6) 'רכז זהירות בדרכים (ז.ה.ב.)' |
| `security coordinator` | `רכז ביטחון` | corpus | § 39(a)(7) prints 'רכז בטחון'; the plene spelling ביטחון is used here and noted |
| `social-education coordinator` | `רכז חינוך חברתי` | corpus | § 39(a)(8) 'רכז חינוך חברתי' |
| `grade-level coordinator` | `ממונה שכבה` | corpus | § 39(a)(9) 'ממונה (רכז) שכבה'; § 15 'ממונה שכבה' |
| `laboratory coordinator` | `רכז מעבדה` | corpus | § 39(a)(10) 'רכז מעבדה' |
| `assessment and measurement coordinator` | `רכז הערכה ומדידה` | corpus | § 39(a)(11) 'רכז הערכה ומדידה' |
| `The teacher, as one record` | `המורה, כרשומה אחת` | composed | section title |
| `a teacher` | `מורה` | corpus | § 7(b) 'מורה' |
| `qualification` | `ההסמכה` | corpus | record field; § 7(f)-(h) 'הסמכה' |
| `seniority in years` | `ותק בשנים` | corpus | § 37 'ותק בהוראה' (vetek); table margin column is headed 'ותק' |
| `rank` | `דרגה` | corpus | §§ 36, 38 'דרגה' (darga); table margin row is headed 'דרגה' |
| `stage of education` | `שלב החינוך` | composed | record field; definite construct, to stay distinct from the type שלב חינוך |
| `how they entered` | `אופן הכניסה` | composed | record field; short form of אופן הכניסה לרפורמה |
| `fraction of a full post` | `היקף המשרה` | corpus | § 27 'היקף משרה'. The agreement uses היקף משרה and חלקיות משרה interchangeably; this encoding assigns היקף המשרה to the record field and חלקיות המשרה to the free parameter, to keep them distinct |
| `roles` | `תפקידים` | corpus | § 39 'בגין מילוי התפקידים הבאים' |
| `classes in the coordinated grade level` | `כיתות בשכבה המרוכזת` | corpus | § 39(a)(9) 'מספר הכיתות בשכבה'; § 15 table column 'מספר הכיתות בשכבה של ממונה השכבה' |
| `units of the school-role supplement` | `יחידות גמול התפקיד הבית ספרי` | corpus | 2022 § 22.2 'יחידות גמול' |
| `teaches special education` | `מלמד בחינוך מיוחד` | corpus | § 39(a)(3) 'מורה לחינוך מיוחד' |
| `special education percentage` | `שיעור גמול חינוך מיוחד` | corpus | § 39(a)(3) '5.5%, 8.5%, 9% או 14% מהשכר המשולב'; § 39(c) 'גמול חינוך מיוחד' |
| `Reading the record` | `קריאת הרשומה` | composed | section title |
| `the teacher` | `המורה` | corpus | § 7(b) 'מורה', definite |
| `the table the teacher is placed in` | `הטבלה שבה משובץ` | corpus | § 36 'שיבוץ בטבלאות השכר' — 'ישובץ בטבלת השכר' |
| `the teacher is academic` | `המורה הוא אקדמאי` | corpus | § 7(d) 'מורה אקדמאי' |
| `the teacher holds a doctorate` | `המורה בעל תואר שלישי` | corpus | § 36(d) 'מורה בעל תואר שלישי' |
| `Illustrations` | `דוגמאות` | composed | section title |
| `Yael` | `יעל` | composed | fixture; an ordinary Israeli given name, transliterated |
| `Dvora` | `דבורה` | composed | fixture; an ordinary Israeli given name, transliterated |
| `Noa` | `נעה` | composed | fixture; an ordinary Israeli given name, transliterated |

## `ofek-salary-table.l4` — the combined salary tables

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `The combined salary tables` | `טבלאות השכר המשולב` | corpus | § 35 'טבלאות השכר המשולב החדשות' |
| `A row of the table` | `שורה בטבלה` | composed | section title |
| `a row of the combined salary table` | `שורה בטבלת השכר המשולב` | corpus | § 35 'טבלת השכר המשולב' |
| `at rank 1` | `בדרגה 1` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 2` | `בדרגה 2` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 3` | `בדרגה 3` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 4` | `בדרגה 4` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 5` | `בדרגה 5` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 6` | `בדרגה 6` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 7` | `בדרגה 7` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 8` | `בדרגה 8` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `at rank 9` | `בדרגה 9` | corpus | table column heading 'דרגה' 1..9; § 38 'קידום לדרגות' |
| `the row` | `השורה` | composed | parameter |
| `the rank` | `הדרגה` | corpus | §§ 36, 38 'דרגה' (darga), definite |
| `the amount in the row at rank` | `הסכום בשורה לפי דרגה` | composed | reader of a table cell; composed from דרגה + שורה |
| `Appendix alef-1 — the BA table, rating code 101` | `נספח א׳1 — טבלת השכר למורים בעלי תואר ראשון, קוד דירוג 101` | corpus | document title 'נספח א׳1 — טבלת השכר למורים בעלי תואר BA (קוד דירוג 101)' |
| `the seniority` | `הוותק` | corpus | § 37 'ותק בהוראה'; table margin 'ותק', definite |
| `the BA table row at seniority` | `שורת טבלת תואר ראשון לפי ותק` | composed | composed from the table title and § 37 ותק |
| `Appendix alef-2 — the MA table, rating code 102` | `נספח א׳2 — טבלת השכר למורים בעלי תואר שני, קוד דירוג 102` | corpus | document title 'נספח א׳2 — טבלת השכר למורים בעלי תואר MA (קוד דירוג 102)' |
| `the MA table row at seniority` | `שורת טבלת תואר שני לפי ותק` | composed | composed from the table title and § 37 ותק |
| `Reading a cell` | `קריאת תא` | composed | section title |
| `the table` | `הטבלה` | corpus | § 35 'טבלת השכר', definite |
| `the combined salary for a full post` | `השכר המשולב למשרה מלאה` | corpus | § 39(b) '"שכר משולב" - שכר משולב למשרה מלאה (100%)' |
| `The frontier the table actually separates` | `הגבול שהטבלה מפרידה בפועל` | composed | the staircase where the printed table stops giving distinct figures; the instruments name no such thing |
| `the highest rank the table separates at seniority` | `הדרגה הגבוהה ביותר שהטבלה מפרידה לפי ותק` | composed | composed; see the frontier note |
| `the seniority at which rank is first separated` | `הוותק שבו מופרדת לראשונה הדרגה` | composed | composed; see the frontier note |
| `The steps the table prints in its own margins` | `שיעורי העלייה המודפסים בשולי הטבלה` | corpus | § 35(b) 'יעודכנו בשיעורים ובמועדים'; the margins of the printed table carry 2% / 1% / 7.5% |
| `the seniority step at` | `שיעור העלייה בוותק של` | composed | composed from § 35(b) שיעור + § 37 ותק; the margin prints the percentage only |
| `the rank step` | `שיעור העלייה בדרגה` | composed | composed from § 35(b) שיעור + § 38 דרגה; the margin prints 7.5% only |
| `The table agrees with the steps it prints` | `הטבלה מתיישבת עם השיעורים שהיא מדפיסה` | composed | section title |
| `BA cell` | `תא תואר ראשון` | composed | test helper; composed from the table title |
| `MA cell` | `תא תואר שני` | composed | test helper; composed from the table title |
| `the computed amount` | `הסכום המחושב` | composed | test helper |
| `the printed amount` | `הסכום המודפס` | composed | test helper |
| `agrees to the agora` | `תואם עד כדי אגורה` | corpus | 'אגורה' is the coin; the follow-up-committee correction of 14.1.2025 reissued the tables to the agora |
| `The merged cells are repeats, not steps` | `התאים הממוזגים הם חזרות, ולא מדרגות` | composed | section title |
| `Spot checks against the printed page` | `בדיקות מדגם מול הדף המודפס` | composed | section title |

## `ofek-placement.l4` — §§ 36–38, placement, seniority, promotion

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `Placement, seniority and promotion` | `שיבוץ, ותק וקידום` | corpus | § 36 'שיבוץ בטבלאות השכר'; § 37 'ותק בהוראה'; § 38 'קידום בדרגות' |
| `Section 36 — placement on entry` | `סעיף 36 — שיבוץ בכניסה` | corpus | § 36 heading 'שיבוץ בטבלאות השכר' |
| `the rank a new academic teacher starts at` | `הדרגה שבה מתחיל מורה חדש אקדמאי` | corpus | § 36(a) 'ישובצו בטבלאות השכר בדרגה 1 ובותק 0' |
| `the seniority a new academic teacher starts at` | `הוותק שבו מתחיל מורה חדש אקדמאי` | corpus | § 36(a), same sentence |
| `the recognised prior seniority` | `הוותק המוכר הקודם` | corpus | § 36(a) 'מורה חדש אקדמאי בעל ותק מוכר' |
| `the seniority a new academic teacher is placed at with` | `הוותק שבו משובץ מורה חדש אקדמאי בעל ותק מוכר של` | corpus | § 36(a) 'ישובץ בהתאם לויתקו האמור' |
| `the doctorate supplement rate` | `שיעור תוספת התואר השלישי` | corpus | § 36(d)(2) 'תוספת שכר בשיעור של 5% משכרו המשולב בטבלה' |
| `the combined salary` | `השכר המשולב` | corpus | § 36(d)(2) 'שכרו המשולב' |
| `the doctorate supplement for` | `תוספת התואר השלישי עבור` | corpus | § 36(d)(2) |
| `the teacher holds a teaching certificate` | `למורה יש תעודת הוראה או הסמכה להוראה` | corpus | § 36(e) 'אשר אינו בעל תעודת הוראה או הסמכה להוראה' |
| `section 36(e) bars the teacher from advancing in rank` | `סעיף 36(e) מונע מהמורה להתקדם בדרגה` | corpus | § 36(e) 'לא יוכל להתקדם בדרגות' |
| `the degree engages section 36(e)` | `התואר מפעיל את סעיף 36(e)` | composed | composed; § 36(e) applies to a second or third degree holder |
| `Section 37 — what counts as seniority` | `סעיף 37 — מה נחשב ותק` | corpus | § 37 heading 'ותק בהוראה' |
| `a period offered as seniority` | `תקופה המוצעת כותק` | composed | composed; § 37 speaks of 'ותק מוכר' and of תקופות included and excluded |
| `teaching seniority recognised by the service regulations` | `ותק בהוראה המוכר בתקנון שירות עובדי הוראה` | corpus | § 37(a) 'ותק בהוראה ... כהגדרתו היום בתקנון שירות עובדי הוראה' |
| `the internship year` | `שנת ההתמחות` | corpus | § 37(a) 'לא כולל תקופת ההתמחות'; § 7(i)(2) calls it 'שנת סטאז׳' |
| `compulsory military service` | `שירות חובה בצה״ל` | corpus | § 37(a) 'למעט תקופת שירות חובה בצה"ל' |
| `teaching service in the IDF` | `שירות בצה״ל בהוראה` | corpus | § 37(a) 'שירות בצה"ל בהוראה' |
| `national service performed as teaching` | `שירות לאומי בהוראה` | corpus | § 37(a) 'שירות לאומי בהוראה' |
| `the period` | `התקופה` | corpus | § 37, § 38(c) 'תקופות שהייה' |
| `the period counts as recognised seniority` | `התקופה נחשבת ותק מוכר` | corpus | § 37(a) 'ותק מוכר' |
| `the seniority recognised before the crossover` | `הוותק שהוכר ערב המעבר` | corpus | § 37(b) 'כל שנות הותק בהוראה אשר הוכרו לצורך שכרו ערב המעבר שלו' |
| `the seniority carried into the reform by` | `הוותק הנישא לרפורמה עבור` | composed | composed from § 37(b) |
| `Section 38 — promotion in rank` | `סעיף 38 — קידום בדרגות` | corpus | § 38 heading 'קידום בדרגות' |
| `the rank being left` | `דרגת המוצא` | composed | composed; § 38(b) says 'קידום מדרגה 1 לדרגה 2', naming the ranks by number only |
| `the years of standing required to leave rank` | `שנות השהייה הנדרשות ליציאה מדרגה` | corpus | § 38(b) 'פרקי זמן השהייה הנדרשים'; 'שתי (2) שנות שהיה בדרגה 1' |
| `a period away from the classroom` | `תקופת היעדרות מהכיתה` | composed | composed; § 38(c)-(d) list the periods without a collective noun |
| `maternity leave under statute` | `חופשת לידה לפי חוק` | corpus | § 38(c)(1) 'חופשת לידה לפי חוק' |
| `reserve military service` | `שירות מילואים` | corpus | § 38(c)(2) 'שירות מילואים' |
| `service as principal or first deputy that earned no promotion` | `עבודה כמנהל או כסגן מנהל ראשון שלא הקנתה קידום` | corpus | § 38(c)(3) 'תקופת עבודה רצופה בה שימש המורה כמנהל או כסגן מנהל ראשון, ואשר לא הקנתה לו קידום בדרגה' |
| `paid rest leave or paid sick leave` | `חופשת מנוחה בשכר או חופשת מחלה בשכר` | corpus | § 38(c)(4) 'חופשת מנוחה בשכר וחופשת מחלה בשכר' |
| `a sabbatical year meeting a section 38(c)(5) condition` | `שנת שבתון המקיימת תנאי מתנאי סעיף 38(c)(5)` | corpus | § 38(c)(5) 'שנת שבתון — אך ורק אם התקיים ... אחד התנאים הבאים' |
| `a sabbatical year meeting neither section 38(c)(5) condition` | `שנת שבתון שאינה מקיימת אף תנאי מתנאי סעיף 38(c)(5)` | corpus | § 38(d)(2) 'שנת שבתון שבה לא התקיים ... אחד התנאים המפורטים בסעיף קטן (ג)(5)' |
| `unpaid leave of any kind` | `חופשה ללא תשלום מכל סוג` | corpus | § 38(d)(1) 'חופשה ללא תשלום (לסוגיה השונים)' |
| `the years of standing contributed by a year of` | `שנות השהייה שתורמת שנה של` | corpus | § 38(c) closing: 'תיחשב שנת השבתון כחצי שנה לעניין פרק זמן השהייה' |
| `promotion out of rank requires an evaluation` | `הקידום מדרגה מחייב הערכה` | corpus | § 38(e)(3) 'תוצאות ההערכות של המורה ... שיש בהן כדי להמליץ על קידומו' |
| `the rank being entered` | `דרגת היעד` | composed | composed; § 38 names the ranks by number only |
| `the rank is rationed by quota` | `הדרגה מוקצבת במכסה` | corpus | § 38(g)-(i) 'מכסה פנויה'; 'מספר המשרות המשובצות בדרגות 7 עד 9 לא יעלה' |
| `the share of all teaching posts the quota allows at rank` | `שיעור כלל המשרות של עובדי הוראה שהמכסה מתירה בדרגה` | corpus | § 38(g) 'בדרגה 7 — 10% מכלל המשרות של עובדי הוראה' |
| `the posts already at that rank` | `המשרות המשובצות כבר באותה דרגה` | corpus | § 38(g) 'מספר המשרות המשובצות בדרגות 7 עד 9' |
| `all teaching posts` | `כלל המשרות של עובדי הוראה` | corpus | § 38(g) defines '"כלל המשרות של עובדי הוראה"' expressly |
| `a place in the quota is free at rank` | `יש מקום פנוי במכסה בדרגה` | corpus | § 38(i) 'בכפוף לקיומה של מכסה פנויה' |
| `the years a qualifying teacher may be kept waiting for rank` | `השנים שניתן לעכב מורה העומד בתנאים לדרגה` | corpus | § 38(i) 'לא יימנע קידומו לדרגות 7 - 9 ליותר ממספר השנים כמפורט' |
| `Putting section 38 together` | `סעיף 38 כמכלול` | composed | section title |
| `an application for promotion in rank` | `בקשה לקידום בדרגה` | corpus | § 38 'קידום בדרגות'; the record itself is an encoding device |
| `the current rank` | `הדרגה הנוכחית` | corpus | § 38(b) 'שהייה בדרגה הקודמת' |
| `years of standing in the current rank` | `שנות שהייה בדרגה הנוכחית` | corpus | § 38(b) 'שנות שהיה בדרגה' |
| `the ministry criteria are met` | `מתקיימים הקריטריונים של משרד החינוך` | corpus | § 38(a)(2) 'עמידה בקריטריונים שנקבעו על-ידי משרד החינוך' |
| `the evaluations recommend promotion` | `ההערכות ממליצות על קידום` | corpus | § 38(e)(3) 'שיש בהן כדי להמליץ על קידומו של המורה' |
| `the posts already at the rank sought` | `המשרות המשובצות כבר בדרגה המבוקשת` | corpus | § 38(g) |
| `years already waited having qualified` | `שנות ההמתנה לאחר העמידה בתנאים` | corpus | § 38(i) 'אשר מילא את התנאים לקידום' |
| `the application` | `הבקשה` | composed | parameter naming the record above |
| `the rank sought by` | `הדרגה המבוקשת לפי` | composed | composed |
| `the teacher meets the conditions for promotion` | `המורה עומד בתנאי הקידום` | corpus | § 38(a),(e) 'התנאים המצטברים לקידום' |
| `the quota admits the promotion` | `המכסה מתירה את הקידום` | corpus | § 38(g)-(i) 'מכסה' |
| `the teacher has waited as long as section 38(i) allows` | `המורה המתין ככל שסעיף 38(i) מתיר` | corpus | § 38(i) |
| `the teacher may be promoted` | `ניתן לקדם את המורה` | corpus | § 38 'ניתן לקדם מורים' |
| `a promotion from rank 3` | `קידום מדרגה 3` | corpus | § 38(b) 'קידום מדרגה 3 לדרגה 4' |
| `a promotion from rank 3 one year early` | `קידום מדרגה 3 שנה אחת מוקדם מדי` | corpus | fixture built on § 38(b) |
| `a promotion into rank 7 with room` | `קידום לדרגה 7 כשיש מקום במכסה` | corpus | fixture built on § 38(i) 'מכסה פנויה' |
| `a promotion into rank 7 with the quota full` | `קידום לדרגה 7 כשהמכסה מלאה` | corpus | fixture built on § 38(g) |
| `a promotion into rank 7 without an evaluation` | `קידום לדרגה 7 ללא הערכה` | corpus | fixture built on § 38(e)(3) |

## `ofek-worktime.l4` — §§ 14–33, the week, the post, the value of an hour

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `The working week, the post, and the value of an hour` | `שבוע העבודה, היקף המשרה וערך השעה` | corpus | chapter heading 'מבנה שבוע העבודה החדש של מורים בין כתלי בית הספר'; § 31 'חישוב ערך שעה' |
| `Section 14 — the working days` | `סעיף 14 — ימי העבודה` | corpus | § 14 heading 'ימי עבודה בשבוע' |
| `the working days in a full week` | `ימי העבודה בשבוע מלא` | corpus | § 14 'מורה במשרה מלאה יעבוד 5 ימי עבודה בשבוע' |
| `the longest day allowed under the four-day exception` | `יום העבודה הארוך ביותר המותר בחריג ארבעת הימים` | corpus | § 14 'ובלבד שיום העבודה שלו לא יארך יותר מ-9 שעות' |
| `the teacher worked four days before the crossover` | `המורה עבד ארבעה ימים ערב המעבר` | corpus | § 14 'ערב המעבר לרפורמה עבד 4 ימים בשבוע' |
| `the school had already moved to a five-day week` | `בית הספר כבר הנהיג שבוע של חמישה ימים` | corpus | § 14 'בבית-ספר בו הונהג שבוע לימודים של 5 ימים' |
| `the principal agrees` | `מנהל בית הספר מסכים` | corpus | § 14 'בהסכמת מנהל בית הספר' |
| `the teacher may keep working four days` | `המורה רשאי להמשיך לעבוד ארבעה ימים` | corpus | § 14 'יהיה רשאי ... להמשיך לעבוד 4 ימים בשבוע' |
| `Sections 15 and 17 — the shape of the week` | `סעיפים 15 ו-17 — מבנה השבוע` | corpus | §§ 15, 17 'מבנה שבוע העבודה' |
| `a weekly work pattern` | `מבנה שבוע עבודה` | corpus | § 15 'מבנה שבוע העבודה למורה בהיקף משרה של 100%' |
| `frontal hours` | `שעות פרונטליות` | corpus | § 15(b) 'שעות העבודה הפרונטליות בפני כיתה'; the table column is headed 'שעות פרונטאליות' |
| `individual hours` | `שעות פרטניות` | corpus | § 15(c); the table column is headed 'שעות פרטניות' |
| `presence hours` | `שעות שהייה` | corpus | § 15(d) defines '(להלן: "שעות השהיה")' |
| `the pattern` | `המבנה` | composed | parameter naming the record above |
| `the hours in` | `סך השעות של` | corpus | § 15(a) 'שבוע העבודה בבית הספר יהיה בהיקף של 36 שעות' |
| `the stage` | `השלב` | composed | parameter; short for שלב החינוך |
| `the ordinary full-post week in` | `שבוע העבודה הרגיל למשרה מלאה לפי` | corpus | §§ 15(a), 17(a) |
| `the classes in the grade` | `הכיתות בשכבה` | corpus | § 15 table column 'מספר הכיתות בשכבה של ממונה השכבה' |
| `the full-post week of a grade coordinator in` | `שבוע העבודה למשרה מלאה של ממונה שכבה לפי` | corpus | §§ 15, 17 'המשמש בתפקיד של ממונה שכבה' |
| `Section 26 — the age hours` | `סעיף 26 — שעות גיל` | corpus | § 26 heading 'שעות גיל' |
| `the age on 31 December of the school year` | `הגיל ביום 31 בדצמבר של שנת הלימודים` | corpus | § 26(d) 'על-פי גילו ביום 31 בדצמבר באותה שנת הלימודים' |
| `the week after the age reduction for` | `שבוע העבודה לאחר הפחתת שעות הגיל של` | corpus | § 26(a)-(c) 'זכאי להפחתה של שתי שעות הוראה פרונטאליות שבועיות' |
| `Sections 27 and 33 — how large a post may be` | `סעיפים 27 ו-33 — היקף המשרה המותר` | corpus | § 27 'מורה במשרה חלקית'; § 33 'היקף העסקה' |
| `the smallest post in the reform` | `היקף המשרה המזערי ברפורמה` | corpus | § 27(a) 'בהיקף משרה שאינו נמוך מ-1/3 משרה' |
| `the smallest post for a new teacher without approval` | `היקף המשרה המזערי למורה חדש ללא אישור` | corpus | § 27(c) 'לא יועסק בחלקיות משרה הנמוכה מ-50% אלא אם ... אושרו על ידי מנהל אגף כוח אדם בהוראה' |
| `special approval has been given` | `ניתן אישור מיוחד` | corpus | § 27(c) 'אושרו על ידי מנהל אגף כוח אדם בהוראה במשרד החינוך' |
| `the teacher is paramedical or an integration teacher` | `המורה בתפקיד פארא-רפואי או מורה משלב` | corpus | § 27(e) 'מורה המועסק בתפקיד פארא רפואי או כמורה משלב/ת' |
| `the post is large enough` | `היקף המשרה מספיק` | composed | composed from § 27(a),(c) |
| `the new-teacher floor is satisfied` | `רף המורה החדש מתקיים` | composed | composed from § 27(c) |
| `the largest ordinary post` | `היקף המשרה הרגיל המרבי` | corpus | § 33(a) 'בהיקף משרה של עד 100% בלבד' |
| `the longest day beyond a full post` | `היום הארוך ביותר מעבר למשרה מלאה` | corpus | § 33(c)(2) 'לא יעלה על 8.5 שעות ביום אחד, בימים א׳ עד ה׳' |
| `the longest friday beyond a full post` | `יום השישי הארוך ביותר מעבר למשרה מלאה` | corpus | § 33(c)(2) 'וביום ו׳ - 5 שעות' |
| `the longest week beyond a full post` | `השבוע הארוך ביותר מעבר למשרה מלאה` | corpus | § 33(c)(2) 'וכן לא יעלה על 42 שעות בשבוע אחד' |
| `the hours in the day` | `השעות ביום` | corpus | § 33(c)(2) |
| `the hours in the week` | `השעות בשבוע` | corpus | § 33(c)(2) |
| `the day is a friday` | `היום הוא יום שישי` | corpus | § 33(c)(2) 'וביום ו׳' |
| `the section 33 hour caps are respected` | `מגבלות השעות של סעיף 33 מתקיימות` | composed | composed from § 33(c)(2) |
| `Section 31 — the value of an hour` | `סעיף 31 — חישוב ערך שעה` | corpus | § 31 heading 'חישוב ערך שעה' |
| `the weeks in a month for this purpose` | `השבועות בחודש לעניין זה` | corpus | § 31(b) '4.33 (שבועות) X 36 (שעות)' |
| `the hours in a full-post week` | `השעות בשבוע של משרה מלאה` | corpus | § 31(b), same formula |
| `the hours in a full-post month` | `השעות בחודש של משרה מלאה` | corpus | § 31(b) 'הבסיס לחישוב ערך שעה ל-100% משרה' |
| `a purpose for which an hour is valued` | `עניין שלגביו מחושב ערך שעה` | corpus | § 31(a) 'הבסיס לחישוב ערך שעה לעניין הנושאים הבאים' |
| `a substitution hour` | `שעת מילוי מקום` | corpus | § 31(a)(1) 'שעת מילוי מקום'; § 29 heading 'שעות מילוי מקום' |
| `a substitution hour taken in place of a presence hour` | `שעת מילוי מקום המבוצעת במקום שעת שהייה` | corpus | § 31(a)(2) 'שעת מילוי מקום המבוצעת במקום שעת שהיה' |
| `a school activity` | `פעילות בית ספרית` | corpus | § 31(a)(3) 'פעילויות בית ספריות'; § 30 heading |
| `a deduction for an hour of absence` | `הפחתת שכר בשל שעת היעדרות` | corpus | § 31(a)(4) 'הפחתת שכר בשל שעת היעדרות' |
| `an hour worked beyond a full post` | `שעת עבודה מעבר למשרה מלאה` | corpus | § 33(c)(3) 'התגמול עבור שעת עבודה מעבר ל-100% משרה' |
| `the purpose` | `העניין` | corpus | § 31(a) 'לעניין' |
| `the role supplements enter the hourly base for` | `גמולי התפקיד נכללים בבסיס ערך השעה לעניין` | corpus | § 31(a)(2)-(4) 'השכר המשולב וגמולי התפקיד המובאים בחשבון' |
| `the monthly base for the purpose` | `הבסיס החודשי לעניין` | corpus | § 31(a) 'הבסיס לחישוב ערך שעה' |
| `the fraction of a full post` | `חלקיות המשרה` | corpus | § 27(g) 'מורה שחלקיות משרתו'. Paired with היקף המשרה (the record field) so the two stay distinct — see the naming note |
| `the value of an hour on a base of` | `ערך השעה על בסיס של` | corpus | § 31(b) 'אופן חישוב ערך השעה' |
| `Sections 29 and 30 — the hours paid on top` | `סעיפים 29 ו-30 — השעות המשולמות בנוסף` | corpus | § 29 'שעות מילוי מקום'; § 30 'פעילויות בית ספריות' |
| `the rate for a substitution hour` | `שיעור התמורה לשעת מילוי מקום` | corpus | § 29(b) 'בשיעור של 125% כפול ערך שעה' |
| `the rate for a school activity` | `שיעור התמורה לפעילות בית ספרית` | corpus | § 30(a) 'בשיעור של 125% כפול ערך שעה' |
| `the rate for an ordinary presence hour` | `שיעור התמורה הרגילה לשעת שהייה` | corpus | § 29(d) 'התמורה הרגילה עבור אותה שעת שהיה (100%)' |
| `the rate for an hour beyond a full post` | `שיעור התמורה לשעה מעבר למשרה מלאה` | corpus | § 33(c)(3) 'בשיעור של 100% כפול ערך שעה' |
| `the school activity hours allowed in a half year` | `שעות הפעילות הבית ספרית המותרות במחצית` | corpus | § 30(a) 'מספר שעות שלא יעלה על 18 שעות בכל מחצית של שנת הלימודים' |
| `the assembly hours allowed in a half year` | `שעות האסיפה הבית ספרית המותרות במחצית` | corpus | § 30(c) 'אסיפה בית ספרית כללית (עד 4 שעות במחצית)' |
| `the parent and child meeting hours allowed in a half year` | `שעות אסיפת הורים וילדים המותרות במחצית` | corpus | § 30(c) 'אסיפת הורים וילדים פרטנית (עד 8 שעות במחצית)' |
| `the after-hours event hours allowed in a half year` | `שעות הפעילות לאחר שעות בית הספר המותרות במחצית` | corpus | § 30(c) 'פעילות לאחר שעות בית הספר — מסיבה נושאית, מסיבת סיום וכדו׳ (עד 6 שעות במחצית)' |
| `the assembly hours` | `שעות האסיפה הבית ספרית` | corpus | § 30(c) |
| `the parent and child meeting hours` | `שעות אסיפת הורים וילדים` | corpus | § 30(c) |
| `the after-hours event hours` | `שעות הפעילות לאחר שעות בית הספר` | corpus | § 30(c) |
| `the school activity caps are respected` | `מגבלות הפעילות הבית ספרית מתקיימות` | composed | composed from § 30(a),(c) |
| `how the extra hour stood to the presence hour` | `יחס השעה הנוספת לשעת השהייה` | composed | composed from §§ 29(c)-(e), 30(d)-(f) |
| `it fell on the teacher's free day` | `בוצעה ביום החופשי של המורה` | corpus | § 29(c) 'המבצע שעת מילוי מקום ביום החופשי שלו' |
| `it replaced a presence hour that was not made up` | `בוצעה במקום שעת שהייה שלא הושלמה` | corpus | § 29(d) 'במקום שעת שהיה באותו יום ... ולא תשולם לו התמורה הרגילה' |
| `it replaced a presence hour made up on another day` | `בוצעה במקום שעת שהייה שהושלמה ביום אחר` | corpus | § 29(e) 'ובוחר לבצע אותה שעת שהיה ביום אחר' |
| `the case` | `המקרה` | composed | parameter |
| `the value of an hour` | `ערך השעה` | corpus | § 31 'ערך שעה', definite |
| `the pay for one extra hour where` | `התמורה לשעה נוספת אחת כאשר` | corpus | §§ 29, 30 'התמורה עבור' |

## `ofek-supplements.l4` — § 39, the 2022 floors, Tosefet Ofek 2022, § 22 units

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `The supplements` | `הגמולים והתוספות` | corpus | § 39 'גמולי תפקיד'; 2022 § 5 'תוספת אופק 2022' |
| `Section 39 — the role supplements` | `סעיף 39 — גמולי התפקיד` | corpus | § 39 heading 'גמולי תפקיד אשר ימשיכו להתקיים ברפורמה' |
| `the role` | `התפקיד` | corpus | § 39(a) 'בגין מילוי התפקידים הבאים' |
| `the section 39 rate for` | `שיעור הגמול לפי סעיף 39 עבור` | corpus | § 39(a) 'בשיעור הקבוע לכל תפקיד' |
| `the smallest post that carries a role supplement` | `היקף המשרה המזערי המזכה בגמול תפקיד` | corpus | § 39(b) 'ובלבד שעובד ההוראה הועסק ב-1/3 משרה לפחות' |
| `the post carries the role supplements` | `היקף המשרה מזכה בגמולי התפקיד` | composed | composed from § 39(b) |
| `the role supplements a teacher may hold` | `מספר גמולי התפקיד שמורה רשאי לקבל` | corpus | § 39(c) 'זכאי, לכל היותר ... לשני גמולי תפקיד' |
| `the roles held` | `מספר התפקידים הממולאים` | corpus | § 39(c) 'בגין מילוי תפקידים כאמור' |
| `the district director has approved a further supplement` | `מנהל המחוז אישר גמול נוסף` | corpus | § 39(c) 'למעט אם אישר מנהל המחוז לשלם גמול בגין תפקיד נוסף' |
| `the number of role supplements is allowed` | `מספר גמולי התפקיד מותר` | composed | composed from § 39(c) |
| `Section 10 of the 2022 agreement — the shekel floors` | `סעיף 10 להסכם 2022 — הסכומים השקליים המזעריים` | corpus | 2022 § 10 heading 'סכום שקלי מינימלי לגמולי תפקיד' |
| `the date the shekel floors take effect` | `מועד תחילת הסכומים השקליים המזעריים` | corpus | 2022 § 10.1.1 'החל מיום 1.9.2023' |
| `the floor under the homeroom supplement` | `הסכום המזערי לגמול חינוך כיתה` | corpus | 2022 § 10.1 heading 'גמול חינוך'; § 10.1.1.2 '1,000 ₪' |
| `the floor under the grade coordinator supplement` | `הסכום המזערי לגמול ממונה שכבה` | corpus | 2022 § 10.2 heading 'גמול ממונה (רכז) שכבה'; § 10.2.1.2 '1,100 ₪' |
| `the shekel floor under` | `הסכום השקלי המזערי עבור` | corpus | 2022 § 10 'סכום שקלי מינימלי' |
| `the date` | `התאריך` | composed | parameter; the instruments say מועד or 'החל מיום' |
| `the role supplement for` | `גמול התפקיד עבור` | corpus | § 39(a) 'גמול תפקיד' |
| `the percentage amount` | `הסכום האחוזי` | corpus | 2022 § 10.6 'הגמול האחוזי' |
| `Section 5 of the 2022 agreement — Tosefet Ofek 2022` | `סעיף 5 להסכם 2022 — תוספת אופק 2022` | corpus | 2022 § 5 heading 'תוספת אופק 2022' |
| `the date tosefet ofek 2022 takes effect` | `מועד תחילת תוספת אופק 2022` | corpus | 2022 § 5.1 'החל מיום 1.9.2022' |
| `the date tosefet ofek 2022 is increased` | `מועד הגדלת תוספת אופק 2022` | corpus | 2022 § 5.2 'החל מיום 1.9.2023 תוספת אופק 2022 תהיה כמפורט בנספחים ג1 עד ג7' |
| `tosefet ofek 2022 from september 2022 in` | `תוספת אופק 2022 מספטמבר 2022 לפי` | corpus | 2022 § 5.1, appendices bet-1/bet-2 |
| `tosefet ofek 2022 from september 2023 in` | `תוספת אופק 2022 מספטמבר 2023 לפי` | corpus | 2022 § 5.2, appendices gimel-1/gimel-2 |
| `tosefet ofek 2022 for` | `תוספת אופק 2022 עבור` | corpus | 2022 § 5 |
| `the amount at the date` | `הסכום במועד` | composed | local helper |
| `Section 22 of the 2022 agreement — the school-role supplement` | `סעיף 22 להסכם 2022 — גמול תפקיד בית ספרי` | corpus | 2022 § 22 heading 'גמול תפקיד בית ספרי' |
| `the value of one school-role unit` | `ערך יחידת גמול אחת` | corpus | 2022 § 22.4 'כל יחידת גמול תהיה שווה לסכום של 200 ₪ לחודש' |
| `the fewest units a school role may carry` | `מספר יחידות הגמול המזערי לתפקיד בית ספרי` | corpus | 2022 § 22.2 'בין שתי יחידות גמול לחמש יחידות גמול, ביחידות שלמות' |
| `the most units a school role may carry` | `מספר יחידות הגמול המרבי לתפקיד בית ספרי` | corpus | 2022 § 22.2, same sentence |
| `the smallest post that carries the school-role supplement` | `היקף המשרה המזערי המזכה בגמול תפקיד בית ספרי` | corpus | 2022 § 22.9 'ובלבד שהועסק בחלקיות של שליש משרה (33.33%) ומעלה' |
| `the date section 22 was first to take effect` | `המועד שבו היה סעיף 22 אמור להיכנס לתוקף תחילה` | corpus | 2022 § 22.1 'החל משנת הלימודים תשפ״ו (המתחילה ביום 1.9.2025)' |
| `the date section 22 takes effect as postponed` | `מועד כניסת סעיף 22 לתוקף לאחר הדחייה` | corpus | 2026 § 19 substitutes 'החל בשנת הלימודים תשפ״ז (המתחילה ביום 1.9.2026)' |
| `the units` | `היחידות` | corpus | 2022 § 22.2 'יחידות גמול' |
| `the units are within the section 22 range` | `מספר היחידות בתחום שסעיף 22 מתיר` | composed | composed from 2022 § 22.2 |
| `the school-role supplement for` | `גמול התפקיד הבית ספרי עבור` | corpus | 2022 § 22 'גמול תפקיד בית ספרי' |
| `the first day of the 2024 school year` | `היום הראשון של שנת הלימודים 2024` | corpus | 'שנת הלימודים' is the instruments' unit of time throughout |
| `a day in the 2022 school year` | `יום בשנת הלימודים 2022` | corpus | same |
| `a day in the 2026 school year` | `יום בשנת הלימודים 2026` | corpus | same |

## `ofek-fiscal-2025.l4` — the 2025–2026 wage reduction

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `The 2025-2026 wage reduction` | `הפחתות שכר 2025-2026` | corpus | 2026 § 8 heading 'הפחתות שכר 2025-2026' |
| `Sections 6 and 7 — who is caught` | `סעיפים 6 ו-7 — על מי חל ההסכם` | corpus | 2026 § 6 heading 'תחולה' |
| `a place of employment for the 2026 agreement` | `מקום העסקה לעניין הסכם 2026` | composed | composed; 2026 §§ 6-7 list places and roles without a collective noun |
| `an education institution on Ofek Hadash terms` | `מוסד חינוך בתנאי אופק חדש` | corpus | 2026 § 6 'המועסקים במוסדות החינוך ... בתנאי אופק חדש' |
| `an ulpan on Ofek Hadash terms` | `אולפן בתנאי אופק חדש` | corpus | 2026 § 6 'או באולפנים, בתנאי אופק חדש' |
| `an instruction role on Ofek Hadash terms` | `תפקיד הדרכה בתנאי אופק חדש` | corpus | 2026 § 6 'המועסקים בתפקידי הדרכה בתנאי אופק חדש' |
| `a teacher training college` | `מכללה להכשרת עובדי הוראה` | corpus | 2026 § 7 'המועסקים במכללות להכשרת עובדי הוראה' |
| `a supervision or headquarters role` | `תפקיד פיקוח או מטה` | corpus | 2026 § 7 'המועסקים בשירות המדינה בתפקידי פיקוח ומטה' |
| `the place` | `המקום` | composed | parameter |
| `the 2026 agreement applies to work` | `הסכם 2026 חל על עבודה במקום` | corpus | 2026 § 6 'הסכם זה יחול על כל העובדים' |
| `Section 8 — the determining base` | `סעיף 8 — הבסיס הקובע` | corpus | 2026 § 8 '"הבסיס הקובע" — משכורת, למעט כל אחד מאלה' |
| `a component of the pay packet` | `רכיב שכר` | corpus | 2026 § 8(a) 'רכיבי שכר אחרים' |
| `a payment made monthly weekly or daily` | `תשלום המשולם על בסיס חודשי שבועי או יומי` | corpus | 2026 § 8(a), read the other way round |
| `a payment neither periodic nor computed on other components` | `תשלום שאינו עתי ואינו מחושב על בסיס רכיבי שכר אחרים` | corpus | 2026 § 8(a) 'תשלומים שאינם משולמים על בסיס חודשי, שבועי או יומי ואינם מחושבים על בסיס רכיבי שכר אחרים' |
| `the recreation payment` | `דמי הבראה` | corpus | 2026 § 8(b) 'דמי הבראה' |
| `the clothing allowance` | `קצובת ביגוד` | corpus | 2026 § 8(b) 'קצובת ביגוד' |
| `a reimbursement of expenses` | `החזר הוצאות` | corpus | 2026 § 8(c) 'החזר הוצאות' |
| `an employer grossing-up of the employee's tax` | `גילום מס העובד בידי המעסיק` | corpus | 2026 § 8(d) 'גילום חלק מהמס החל על העובד אשר משולם בידי המעסיק' |
| `the component` | `הרכיב` | corpus | 2026 § 8(a) 'רכיבי שכר' |
| `the component is in the determining base` | `הרכיב נכלל בבסיס הקובע` | corpus | 2026 § 8 'הבסיס הקובע' |
| `Section 9 — the rates, and the two periods` | `סעיף 9 — השיעורים ושתי התקופות` | corpus | 2026 § 9(a),(b) 'בתקופה שמיום ... בשיעור של' |
| `the first day of the first reduction period` | `היום הראשון של תקופת ההפחתה הראשונה` | corpus | 2026 § 9(a) 'בתקופה שמיום 1.5.2025' |
| `the last day of the first reduction period` | `היום האחרון של תקופת ההפחתה הראשונה` | corpus | 2026 § 9(a) 'ועד יום 31.12.2025' |
| `the first day of the second reduction period` | `היום הראשון של תקופת ההפחתה השנייה` | corpus | 2026 § 9(b) 'בתקופה שמיום 1.1.2026' |
| `the last day of the second reduction period` | `היום האחרון של תקופת ההפחתה השנייה` | corpus | 2026 § 9(b) 'ועד יום 31.12.2026' |
| `the rate for the first reduction period` | `שיעור ההפחתה בתקופה הראשונה` | corpus | 2026 § 9(a) 'בשיעור של 0.95% מהבסיס הקובע' |
| `the rate for the second reduction period` | `שיעור ההפחתה בתקופה השנייה` | corpus | 2026 § 9(b) 'בשיעור של 1.2% מהבסיס הקובע' |
| `the reduction rate on` | `שיעור ההפחתה לפי תאריך` | corpus | 2026 § 9 |
| `the determining base` | `הבסיס הקובע` | corpus | 2026 § 8 '"הבסיס הקובע"' — a defined term of the agreement |
| `the monthly wage reduction on` | `הפחתת השכר החודשית לפי` | corpus | 2026 § 9 'תופחת משכורתו של עובד הוראה' |
| `the study fund base` | `הבסיס לקרן השתלמות` | corpus | 2026 § 12 'הבסיס לחישוב הסכומים המשולמים בעד עובד ההוראה לקרן השתלמות' |
| `the study fund base after the reduction` | `הבסיס לקרן השתלמות לאחר ההפחתה` | corpus | 2026 § 12, same sentence |
| `Section 18 — what the reduction is NOT allowed to touch` | `סעיף 18 — מה שההפחתה אינה נוגעת בו` | corpus | 2026 § 18 heading 'סייג לעניין תשלומים שונים' |
| `a payment computed on salary` | `תשלום המחושב על בסיס השכר` | composed | composed; 2026 § 18 lists the payments without a collective noun |
| `a one-off payment on the end of employment` | `תשלום חד פעמי עקב סיום עבודה` | corpus | 2026 § 18(1) 'תשלום חד פעמי המשולם לעובד או לשאיריו ... עקב סיום עבודה' |
| `an employer contribution to a pension fund` | `הסכום המשולם לקופת גמל לקצבה` | corpus | 2026 § 18(2) 'הסכום המשולם לקופת גמל לקצבה בעד עובד' |
| `the determining salary for a budgetary pension` | `המשכורת הקובעת לפנסיה תקציבית` | corpus | 2026 § 18(3) 'המשכורת הקובעת לחישוב תשלומי עובדים בפנסיה תקציבית' |
| `a payment of budgetary pension` | `תשלומי פנסיה תקציבית` | corpus | 2026 § 18(4) 'תשלומי פנסיה תקציבית, המשולמת על פי דין או הסכם' |
| `a bridging payment or purchased pension top-up` | `תשלומי גישור או תוספת לקצבה שנרכשה` | corpus | 2026 § 18(5) 'תשלומי גישור או סכום תוספת לקצבה הנרכש מקופת גמל לקצבה' |
| `ordinary monthly pay` | `המשכורת החודשית הרגילה` | corpus | 2026 § 25 'בנוסף על משכורתו החודשית הרגילה' |
| `the payment` | `התשלום` | corpus | 2026 § 18 'התשלומים המפורטים להלן' |
| `the reduction is ignored in computing` | `ההפחתה אינה באה בחשבון בחישוב` | corpus | 2026 § 18 'לא תבואנה בחשבון בעניינים המפורטים להלן' |
| `Sections 15 and 16 — the seniority step, given and taken back` | `סעיפים 15 ו-16 — קידום הוותק, שניתן ונשלל בחזרה` | corpus | 2026 § 15 'הכרה בוותק לצורך התקדמות בוותק'; § 16 'תופחת משכורתו בסכום השווה לעליה' |
| `the first month the seniority step is withheld` | `החודש הראשון שבו נשלל קידום הוותק` | corpus | 2026 § 16 'החל במשכורת חודש ספטמבר' |
| `the last month the seniority step is withheld` | `החודש האחרון שבו נשלל קידום הוותק` | corpus | 2026 § 16 'ועד חודש דצמבר 2025 (כולל)' |
| `the seniority step is withheld on` | `קידום הוותק נשלל בתאריך` | corpus | 2026 § 16 |
| `the value of the seniority step` | `שווי קידום הוותק` | corpus | 2026 § 16 'סכום השווה לעליה במשכורת לה הוא זכאי בשל קידום בוותק' |
| `the teacher advanced in seniority in september 2025` | `המורה התקדם בוותק בספטמבר 2025` | corpus | 2026 § 16 'עובד הוראה אשר זכאי לקידום בוותק ... במשכורת חודש ספטמבר 2025' |
| `the section 16 withholding on` | `שלילת קידום הוותק לפי סעיף 16 לפי` | corpus | 2026 § 16 |
| `Section 20 — the clothing allowance, reduced once` | `סעיף 20 — קצובת הביגוד, הפחתה חד פעמית` | corpus | 2026 § 20 heading 'קצובת ביגוד לשנת 2025'; 'תבוצע הפחתה חד פעמית' |
| `the flat part of the clothing allowance reduction` | `החלק הקבוע בהפחתת קצובת הביגוד` | corpus | 2026 § 20(a)(1)(b) 'סכום של 91 ₪' |
| `the allowance with index linkage` | `הקצובה כולל הצמדה למדד` | corpus | 2026 § 20(a)(1)(a) 'כולל הצמדה למדד המחירים לצרכן' |
| `the allowance without index linkage` | `הקצובה ללא הצמדה למדד` | corpus | 2026 § 20(a)(1)(a) 'ללא הצמדה למדד המחירים לצרכן' |
| `the clothing allowance reduction for 2025` | `הפחתת קצובת ביגוד 2025` | corpus | 2026 § 20(a)(2) '(להלן: הפחתת קצובת ביגוד 2025)' |
| `Sections 24 and 25 — the extra substitution hour` | `סעיפים 24 ו-25 — שעת מילוי המקום הנוספת` | corpus | 2026 § 24 'יבצעו עובדי ההוראה שעת הוראה פרונטלית בודדת כממלאי מקום' |
| `the rate for the section 25 additional hour` | `שיעור התמורה לשעה הנוספת לפי סעיף 25` | corpus | 2026 § 25 'ישולם לעובדי ההוראה 25% מערך שעת עבודתו' |
| `the additional hours required in the 5786 school year` | `מספר השעות הנוספות הנדרשות בשנת הלימודים תשפ״ו` | corpus | 2026 § 24 'בשנת הלימודים תשפ״ו ... שעת הוראה פרונטלית בודדת' |
| `the teacher worked normally on 4 May 2025` | `המורה עבד כרגיל ביום 4 במאי 2025` | corpus | 2026 § 24 ties the hour to the industrial action; the date is carried from the English encoding's own reading of the clause |
| `the additional hour is required of the teacher` | `השעה הנוספת נדרשת מהמורה` | composed | composed from 2026 § 24 |
| `the pay for the section 25 additional hour` | `התמורה לשעה הנוספת לפי סעיף 25` | corpus | 2026 § 25 |
| `Section 17 — one line on the payslip` | `סעיף 17 — שורה אחת בתלוש המשכורת` | corpus | 2026 § 17 'יופיע בשורה אחת בתלוש המשכורת של עובד ההוראה' |
| `the name of the line on the payslip` | `שם השורה בתלוש המשכורת` | corpus | 2026 § 17 'ויכונה "חוק הת. כלכלית אופק"' |
| `the single payslip line for` | `השורה האחת בתלוש המשכורת עבור` | corpus | 2026 § 17 |
| `a day in november 2025` | `יום בנובמבר 2025` | composed | fixture date |
| `a day in march 2026` | `יום במרץ 2026` | composed | fixture date |
| `a day in march 2027` | `יום במרץ 2027` | composed | fixture date |
| `a day in april 2025` | `יום באפריל 2025` | composed | fixture date |

## `ofek-pay.l4` — a month's pay, assembled

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `A month's pay` | `שכר של חודש` | corpus | § 44(a)(1) 'במשכורת חודש מרץ'; משכורת is the instruments' word for a month's pay |
| `The base on which percentages are computed` | `הבסיס שעליו מחושבים הגמולים האחוזיים` | corpus | 2022 § 5.4 'לעניין חישוב תוספות אחוזיות המחושבות על בסיס השכר המשולב' |
| `the full-post percentage base for` | `בסיס הגמולים האחוזיים למשרה מלאה של` | corpus | § 39(b) + 2022 § 5.4 |
| `the full-post combined salary` | `השכר המשולב המלא` | corpus | § 39(b) 'שכר משולב למשרה מלאה'. Kept distinct from השכר המשולב למשרה מלאה, which is the table lookup in ofek-salary-table |
| `the full-post tosefet ofek` | `תוספת אופק המלאה` | corpus | 2022 § 5.3 'בהשוואה לעובד הוראה במשרה מלאה' |
| `The parts of the pay packet` | `מרכיבי תלוש השכר` | corpus | 2026 § 8(a) 'רכיבי שכר'; 2026 § 17 'תלוש המשכורת' |
| `the combined salary payable to` | `השכר המשולב המשתלם עבור` | corpus | § 35 'השכר המשולב' |
| `the tosefet ofek payable to` | `תוספת אופק 2022 המשתלמת עבור` | corpus | 2022 § 5.1 |
| `the doctorate supplement payable to` | `תוספת התואר השלישי המשתלמת עבור` | corpus | § 36(d)(2) |
| `the role supplements payable to` | `גמולי התפקיד המשתלמים עבור` | corpus | § 39(a) 'זכאי לגמול תפקיד' |
| `the amount for one role` | `הסכום עבור תפקיד אחד` | composed | local helper |
| `the school-role supplement payable to` | `גמול התפקיד הבית ספרי המשתלם עבור` | corpus | 2022 § 22 |
| `The month, before and after the reduction` | `החודש, לפני ההפחתה ואחריה` | corpus | 2026 § 9 'תופחת משכורתו' |
| `the monthly pay before the reduction for` | `השכר החודשי לפני ההפחתה של` | corpus | 2026 § 18 'כאילו שולמו במועדם וללא ההפחתה' |
| `the determining base for` | `הבסיס הקובע של` | corpus | 2026 § 8 |
| `the value of any seniority step taken in september 2025` | `שווי קידום הוותק שניתן בספטמבר 2025, אם ניתן` | corpus | 2026 § 16 |
| `the monthly pay of` | `השכר החודשי של` | corpus | 2026 § 8 '"משכורת"' |
| `The value of an hour, for this teacher` | `ערך השעה, למורה זו` | corpus | § 31 'חישוב ערך שעה' |
| `the value of an hour for` | `ערך השעה עבור` | corpus | § 31 |
| `the base for the purpose` | `הבסיס לעניין זה` | corpus | § 31(a) 'הבסיס לחישוב ערך שעה לעניין הנושאים הבאים' |

## `ofek-cases.l4` — three teachers, end to end

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `Worked payslips` | `תלושי שכר מחושבים` | corpus | 2026 § 17 'תלוש המשכורת' |
| `The dates the answers turn on` | `התאריכים שהתשובות תלויות בהם` | composed | section title |
| `a month in the 2024 school year` | `חודש בשנת הלימודים 2024` | corpus | 'שנת הלימודים' throughout the instruments |
| `a month in the first reduction period` | `חודש בתקופת ההפחתה הראשונה` | corpus | 2026 § 9(a) |
| `a month in the second reduction period` | `חודש בתקופת ההפחתה השנייה` | corpus | 2026 § 9(b) |
| `a month after the school-role supplement begins` | `חודש שלאחר תחילת גמול התפקיד הבית ספרי` | corpus | 2022 § 22.1 as amended by 2026 § 19 |
| `Yael — a junior-high homeroom teacher, eleven years in` | `יעל — מחנכת בחטיבת ביניים, אחת עשרה שנות ותק` | corpus | § 17 'מורה בחטיבת ביניים'; § 39(a)(1) 'מחנך כיתה'; § 37 'ותק' |
| `Dvora — a primary-school teacher at the top of the table` | `דבורה — מורה בבית ספר יסודי בראש הטבלה` | corpus | § 15 'מורה בבית-ספר יסודי' |
| `Noa — a doctorate on half a post` | `נעה — בעלת תואר שלישי בחצי משרה` | corpus | § 36(d) 'מורה בעל תואר שלישי'; § 27 'משרה חלקית' |
| `Half a post is not half the pay` | `חצי משרה אינה חצי שכר` | composed | section title, stating the finding |
| `Yael on half a post` | `יעל בחצי משרה` | corpus | § 27 'משרה חלקית' |
| `Yael on just under a third of a post` | `יעל במעט פחות משליש משרה` | corpus | § 27(a) '1/3 משרה'; § 39(b) '1/3 משרה לפחות' |
| `The value of an hour, and why the purpose matters` | `ערך השעה, ומדוע העניין משנה` | corpus | § 31(a) 'לעניין הנושאים הבאים' |
| `The reduction reaches a teacher's savings too` | `ההפחתה מגיעה גם לחיסכון של המורה` | corpus | 2026 § 12 'קרן השתלמות' |
| `Promotion, on the same facts` | `קידום, על אותן עובדות` | corpus | § 38 'קידום בדרגות' |
| `Yael applying for rank 5` | `יעל מבקשת דרגה 5` | corpus | § 38(b) 'קידום מדרגה 4 לדרגה 5' |
| `Dvora applying for rank 9` | `דבורה מבקשת דרגה 9` | corpus | § 38(f)(3) 'קידום מדרגת 8 לדרגה 9' |
| `Dvora applying for rank 9 with room` | `דבורה מבקשת דרגה 9 כשיש מקום במכסה` | corpus | § 38(i) 'בכפוף לקיומה של מכסה פנויה' |
| `The week, on the same facts` | `השבוע, על אותן עובדות` | corpus | §§ 15, 17 'מבנה שבוע העבודה' |

## `ofek-luach.l4` — the calendar: school years, the age on 31 December, effective dates

Added by the Hebrew re-encoding; it has **no English counterpart** in `../legalese/`. It is a
library, not a translation: it names the date arithmetic the eight modules each perform inline.
Nothing here decides a pay question, and no numeric assertion in the English encoding changes.

| English identifier | Hebrew | source | note |
| --- | --- | --- | --- |
| `Ofek Hadash's calendar` | `לוח השנה של אופק חדש` | composed | section title |
| `A school year` | `שנת הלימודים — הטיפוס וקצותיה` | composed | section title; deliberately not the bare `שנת לימודים`, which is the type |
| `Which school year a date falls in` | `באיזו שנת לימודים חל תאריך` | composed | section title |
| `Age` | `הגיל` | composed | section title |
| `A period of application` | `תקופת תחולה` | corpus | section title; 'תחולה' is the instruments' word (§ 26(d) 'ותחול מתחילת שנת הלימודים') |
| `Seniority in school years` | `ותק בשנות לימודים` | corpus | section title; § 37 'ותק בהוראה' |
| `The dates the salary tables take effect` | `מועדי תחילתן של טבלאות השכר` | corpus | section title; the printed tables carry 'מעודכנת החל מיום 1.9.2016' |
| `The Hebrew calendar — a label only` | `לוח השנה העברי — תווית בלבד` | composed | section title; deliberately outside the pay path |
| `a school year` | `שנת לימודים` | corpus | type; § 26(d), § 44(b)(4) 'שנת הלימודים' throughout |
| `the opening year` | `שנת הפתיחה` | corpus | record field; § 44(b)(4) 'תחילת שנת הלימודים (1 בספטמבר)' — a school year is identified by the year it opens in |
| `the school year opening in` | `שנת הלימודים שנפתחת בשנת` | corpus | constructor; 2022 § 22.1 'שנת הלימודים תשפ"ו (המתחילה ביום 1.9.2025)' |
| `the year` | `השנה` | composed | parameter; the calendar year a school year opens in |
| `the school year` | `שנת הלימודים` | corpus | parameter; § 26(d) 'באותה שנת הלימודים' |
| `the first day of the school year` | `היום הראשון של שנת הלימודים` | corpus | § 44(b)(4) 'תחילת שנת הלימודים (1 בספטמבר)' |
| `the last day of the school year` | `היום האחרון של שנת הלימודים` | corpus | 31 August; the vaadat maakav decision of 19.9.2010 treats 'ביום 31 באוגוסט' as the last day of the employment year. The agreements define no closing date in terms, so the note is part of the claim |
| `31 December of the school year` | `יום 31 בדצמבר של שנת הלימודים` | corpus | § 26(d) 'ביום 31 בדצמבר באותה שנת הלימודים' |
| `the school year the date falls in` | `שנת הלימודים שבה חל התאריך` | composed | composed from § 44(b)(4)'s 1 September boundary |
| `the date falls in the school year` | `התאריך חל בשנת הלימודים` | composed | composed; the membership test § 26(d) presupposes |
| `the age on a date` | `הגיל בתאריך` | corpus | § 26(b)-(c) 'מורה ... שגילו 55 ומעלה' / '50 ומעלה' |
| `the date of birth` | `תאריך הלידה` | composed | parameter; the agreements say only 'גילו' and never name the birth date |
| `the difference in years` | `הפרש השנים` | composed | local helper inside the age computation |
| `the age on 31 December of the school year for` | `הגיל ביום 31 בדצמבר של שנת הלימודים עבור` | corpus | § 26(d) 'על-פי גילו ביום 31 בדצמבר באותה שנת הלימודים'. Distinct from ofek-worktime's parameter `the age on 31 December of the school year`, which is the number this function computes |
| `the date falls in the period between` | `התאריך חל בתקופה שבין` | composed | the inclusive window §§ 9 and 16 of the 2026 agreement each rewrite inline |
| `the start of the period` | `תחילת התקופה` | composed | parameter |
| `the end of the period` | `סוף התקופה` | composed | parameter |
| `the school years elapsed between` | `שנות הלימודים שחלפו בין` | corpus | § 37 measures seniority in teaching years, which are school years |
| `the first school year` | `שנת הלימודים הראשונה` | composed | parameter |
| `the seniority at entry` | `הוותק בכניסה` | corpus | § 36(a) 'ישובצו ... בותק 0' |
| `the seniority accrued in the school year` | `הוותק הצבור בשנת הלימודים` | corpus | § 37 'ותק מוכר לצורך התקדמות בותק' |
| `the date the January 2015 tables take effect` | `מועד תחילת טבלאות ינואר 2015` | corpus | table heading 'מעודכנות החל מיום 1.1.2015' |
| `the date the September 2016 tables take effect` | `מועד תחילת טבלאות ספטמבר 2016` | corpus | table heading 'מעודכנת החל מיום 1.9.2016' |
| `the date the September 2022 tables take effect` | `מועד תחילת טבלאות ספטמבר 2022` | corpus | appendices alef-1/alef-2 of the 2022 agreement carry 1.9.22 |
| `the tables' effective date` | `מועד הטבלאות` | composed | parameter |
| `the tables' effective date has already arrived on` | `מועד תחילת הטבלאות כבר חל בתאריך` | composed | composed; which printing applies to a given teacher is ofek-salary-table's question, not this one |
| `the Hebrew year number of the school year` | `מספר השנה העברית של שנת הלימודים` | corpus | 2022 § 22.1 'תשפ"ו'; 2026 § 19 'תשפ"ז'. Label arithmetic (opening year + 3761), NOT a calendar conversion — 1.9.2025 is still 5785 in the Hebrew calendar |

## Open questions

These are the places where I could not settle the Hebrew from the corpus. Each one is a live
decision, not a defect to be quietly fixed downstream: if you change one, change it **here first**
and say so, or the five parallel translations will disagree.

1. **Latin or Hebrew sub-paragraph letters in citations.** This file rules `סעיף 36(e)`,
   `סעיף 38(c)(5)`, `סעיף 38(i)` — the English encoding's printed form — against the instruments'
   own `(ה)`, `(ג)(5)`, `(ט)`. The argument for Latin is that the citation then greps identically
   across four artefacts; the argument for Hebrew is that it is what the page says, and the brief
   requires the audit trail to survive. Affects 5 identifiers and a great many comments. **Meng
   should rule.**

2. **`a teaching qualification` → `רמת הסמכה`.** Composed. § 7(f)–(h) name the four statuses
   (`מורה אקדמאי`, `מורה מוסמך`, `מורה בכיר`, `מורה בלתי מוסמך`) but give them no collective noun.
   A live alternative is `סטטוס`, which § 10(c)(1) does use of exactly this ("הסטאטוס בשכרו"), but
   it reads as a loanword next to nine Hebrew type names.

3. **`security coordinator` → `רכז ביטחון`.** § 39(a)(7) prints the defective spelling
   `רכז בטחון`. I used the plene `ביטחון` because it is current orthography and the identifier is
   read, not cited. If the rule is "the page's spelling wins", this is the one entry that changes.

4. **The frontier and the steps have no name in the instruments.** `the frontier the table actually
   separates`, `the seniority step at`, `the rank step`, `the highest rank the table separates at
   seniority`, `the seniority at which rank is first separated`. The tables print the percentages in
   their margins and nothing else; § 35(b) says only "יעודכנו בשיעורים ובמועדים". Everything here is
   composed from `שיעור` + `ותק`/`דרגה`. A reader of the agreement will not recognise these terms
   because there are none to recognise.

5. **`the teacher worked normally on 4 May 2025`.** 2026 § 24 in the corpus is damaged exactly where
   the date would be — the transcription reads `שננקטו ביום` with nothing after it, the clause
   continuing on the next page. The English encoding names 4 May 2025; I carried that date over
   without being able to confirm it against the instrument. **This one is worth verifying against
   the scan before the encoding is relied on.**

6. **`the internship year` → `שנת ההתמחות`.** § 37(a) excludes `תקופת ההתמחות`; § 7(i)(2) excludes
   `שנת סטאז׳`. The two are the same year under two names, and my form is a blend of them
   (`שנת` from one, `ההתמחות` from the other). Either pure form would also be defensible.

7. **Five enum type names are composed because the instruments list members without naming the
   set.** `a period offered as seniority` → `תקופה המוצעת כותק`; `a period away from the classroom`
   → `תקופת היעדרות מהכיתה`; `a component of the pay packet` → `רכיב שכר`; `a payment computed on
   salary` → `תשלום המחושב על בסיס השכר`; `a place of employment for the 2026 agreement` →
   `מקום העסקה לעניין הסכם 2026`. Of these, `רכיב שכר` is the only one with real corpus support
   (2026 § 8(a) "רכיבי שכר אחרים"); the other four are mine.

8. **`BA` / `MA` rendered as `תואר ראשון` / `תואר שני`.** The printed table headings actually mix
   scripts — `טבלת שכר למורים בעלי תואר BA (קוד דירוג 101)`. I took § 36(c)'s all-Hebrew wording
   instead, so that no identifier mixes scripts. The rating codes 101 and 102 are kept as printed,
   which is what a reader checks the table by.

9. **`מזערי` for "smallest / floor".** Used in six identifiers (`היקף המשרה המזערי…`,
   `הסכומים השקליים המזעריים`, `מספר יחידות הגמול המזערי…`). 2022 § 10's own heading says
   `סכום שקלי מינימלי`. `מינימלי` is the instrument's word; `מזערי` is the Hebrew one. I chose
   consistency across the six over fidelity in one, and it could go the other way.

10. **The three fixtures.** `Yael`/`Dvora`/`Noa` → `יעל`/`דבורה`/`נעה` are ordinary given names,
    not terms of art, and carry no corpus authority at all. They are named here only so that five
    agents spell them the same way.

