# הערות — `legalese-he`, הקידוד העברי

**מצב: טיוטה. לא נבדק בידי אדם.**
זהו התאום העברי של [`../legalese`](../legalese): אותם שני מודולים, אותם כללים, אותן 30 קביעות (assertions), כשכל מזהה, כל כותרת `§` וכל כותרת־תרגום (`@nlg`) הם בעברית, וההערות המצטטות את החיקוק מצטטות את המקור העברי.
**האורקל הוא הקידוד האנגלי.** דבר לא נגזר כאן מחדש. אם נתון כלשהו כאן חולק על הקידוד האנגלי – הטעות כאן, לא שם.

**שני הקידודים נכתבו ביד, ומכונה מחזיקה אותם יחד.** `../../source/twin-check.py` מפרק כל מודול אנגלי ואת תאומו העברי לאסימונים – מזהים במרכאות־גרש, מחרוזות, מילים – לאחר השמטת הערות וטקסט של `@nlg`/`@desc`/`@export`, ממפה את האנגלי דרך `glossary.json`, ודורש זהות אסימון לאסימון. כלומר: השניים רשאים להיבדל בשמות, בהערות ובכותרות־תרגום, ובשום דבר אחר – לא במספר, לא במילת מפתח, לא בצורת `CONSIDER`. אחר כך `check.sh` מריץ את שניהם ודורש שכל בלוק `Result:` יהיה זהה, אחרי מיפוי השמות העבריים חזרה.

**המילים הן של הפקודה והתקנות עצמן היכן שיש להן מילים.** `glossary.json` רושם לכל מזהה אם המילה לקוחה מן הפקודה (`ordinance`), מן התקנות (`regulations`) או שהיא שלנו (`composed`), ומדוע. הנחוצות לבדיקה אנושית הן אלה שסומנו `composed`: `קביעה` (הפקודה אינה קוראת בשם לתוצאת החלת ההגדרה), `אינו שיכור`, `גיל בשנים`, `הרכב שבו נהג`, `הריכוז שמעליו הנהג שיכור`, ושמות הנהגים שבבדיקות.

**שתי בדיקות שונות חסרות, ואין לערבב ביניהן.** *הדין* כאן לא נבדק בידי מי שמכיר את דיני התעבורה בישראל – כל מה ש[`../legalese/NOTES.md`](../legalese/NOTES.md) אומר על כך חל כאן ללא שינוי. *העברית* כאן לא נבדקה בידי איש, וזו חסרה אחרת, עם בודק אחר. מה שכן נבדק: שהעברית עוברת ניתוח תחבירי, בדיקת טיפוסים והרצה – ושהיא מחזירה בדיוק את אותן תשובות. זו טענה על המכונה, לא על הלשון.

---

# NOTES — `legalese-he`, the Hebrew-canonical row

**Status: `draft`, not reviewed by a human.** Deposited 2026-09-22 on the drafts shelf, together with its English oracle.

## 1. What this is

The **same two modules** as `../legalese`, the same declarations, rules and 30 assertions, with every identifier, record field, enum constructor, `§` title and `@nlg` herald in Hebrew, and every statute-quoting comment quoting the Hebrew original rather than a translation.
The maintainer's commentary in the module headers is Hebrew too; this file is English below the Hebrew summary, because it is addressed to whoever maintains the encoding alongside `../legalese/NOTES.md`.

It is a **revoicing, not a re-derivation**: no number was recomputed, no rule restructured, no assertion added or dropped. If a figure here ever disagrees with the English row, this row is wrong by construction.

## 2. How the two rows are held together

Both rows are written by hand — the encoding is about 150 lines, and hand-written Hebrew reads better than a token-substituted one — so the guarantee that they are *the same encoding* has to be mechanical. Two checks, both in `check.sh` (and in `../legalese/check.sh`):

1. **Structural identity.** `../../source/twin-check.py` tokenises each English module and its Hebrew twin — backtick spans, string literals, bare words — after dropping comments and the text of `@nlg`, `@desc` and `@export`. It maps the English tokens through `glossary.json` and requires the two token streams to be identical. The rows may differ in names, comments and heralds, and in **nothing else**. The first divergence is reported with both line numbers. Measured 2026-09-22: `drink-driving-he.l4` is `drink-driving.l4` renamed, 303 tokens identical, 106 of them through the glossary; `drink-driving-tests-he.l4` is `drink-driving-tests.l4` renamed, 572 tokens identical, 172 through the glossary.
2. **Answer identity.** `check.sh` runs both test modules, maps this row's output back through the inverse of `glossary.json` (`twin-check.py --unmap`; the glossary is checked for injectivity first, so the inverse is well defined), and requires the `Result:` blocks to be identical line for line — every `#EVAL` and every `#ASSERT`, in order, including the enum constructors and the `JUST`/`NOTHING` wrappers. Measured 2026-09-22: 34 Result blocks identical.

**Positive control.** Before either check was believed it was made to fail: the paragraph (3A) breath figure was changed from 50 to 51 in `drink-driving-he.l4` alone. `twin-check.py` reported the divergence at the exact token (`50` expected, `51` found, with both line numbers), the Hebrew test module went from 30 satisfied assertions to fewer, the cross-row comparison reported a disagreement, and `check.sh` exited 1. Restoring the figure returned exit 0. The transcript is in `../legalese/NOTES.md` section 10.

## 3. The multilingual mechanism, and its limits on this binary

The binary the row was checked on (legalese/prereleases `unstable-20260907-9d6536a`) **predates `@lang`, `@nlg:he` and `l4 nlg --lang`** (l4-ide PR #432, 2026-09-19): `@lang en` fails to parse on it. So neither row uses language-tagged heralds. Each row carries untagged `@nlg` heralds in its own language, and `l4 nlg` on this row produces Hebrew heralds around English connective vocabulary (`with`, `and`), exactly the asymmetry `il/hvac-work-licensing-2025/encodings/legalese-he/NOTES.md` § 3 records. Once the rows move to a binary at or after PR #432, the English row can carry `@nlg:he` and this row `@nlg:en`, and `twin-check.py` will need to learn to strip the tagged variants too (its `ANNOT` pattern is the one place).

Identifiers are Hebrew in every rendering. `§` titles are Hebrew because they are Hebrew in the source, which is what a Hebrew-canonical row is for.

## 4. Filenames

Latin basenames with a `-he` suffix, not Hebrew. `il/hvac-work-licensing-2025/encodings/legalese-he/NOTES.md` § 4 measured on a 2026-09-21 binary that an `IMPORT` of a Hebrew basename resolves to nothing, silently. That measurement was not repeated here; the workaround is inherited, and the reason is recorded so that it can be re-tested rather than trusted.

## 5. Hebrew choices a reviewer should look at first

- **`סף`** for the type that pairs a breath figure with a blood figure. Paragraph (4) of the definition uses the word for both pairs ("הסף שנקבע בתקנות לפי פסקה (3) או ... הסף כאמור בפסקה (3א)"), which is why it was chosen over `ריכוז`; but the paragraph uses it in the singular for each, and the type here holds two numbers.
- **`ריכוז אלכוהול בגוף`** as the *name of the general threshold rule*. That is reg. 169A's defined term, and reg. 169A defines it as exactly the 240/50 pair, so the rule and the term coincide. A reader of the Regulations may still expect the term to denote a property of a person rather than a pair of figures.
- **`הרכב שבו נהג`** for the record field. Paragraph (3A)(c)-(d) say "בעת נהיגה ברכב ..."; a field needs a noun phrase, and the verb in this one is a past tense that may read oddly beside a present-tense herald.
- **`נהג ברכב בדרך או במקום ציבורי`** as a BOOLEAN parameter name: s.62(3)'s own words, but as a bare proposition.
- **The fixtures** (`נהג בן 22 שאינו נהג חדש, ברכב פרטי` and the rest) are masculine, as the statute's "נהג" is; the English fixtures say "her".
- **`אינו שיכור`** for the state the Ordinance never names.

The `composed` marks in `glossary.json` are the index to these.

## 6. How to run

```
sh check.sh                          # l4 on PATH
BAC_L4=/path/to/l4 sh check.sh
python3 ../../source/twin-check.py   # structural check alone
```

`JL4_LIBRARY_PATH` must be **unset** so the binary uses its own embedded standard library; `check.sh` unsets it.
