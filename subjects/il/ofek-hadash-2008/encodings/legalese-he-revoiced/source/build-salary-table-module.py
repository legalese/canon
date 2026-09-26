"""Generate ofek-salary-table.l4 in HEBREW — the two combined-salary tables, as L4.

The Hebrew counterpart of ../../legalese/source/build-salary-table-module.py.
Same 648 amounts, same layout arithmetic, Hebrew identifiers and Hebrew prose.

The 648 amounts come from source/tables.py, a verbatim copy of the English
one — it parses the follow-up committee's corrected agorot appendices of 14
January 2025 and emits nothing into the module but numbers, so there is
nothing in it to translate. The layout comes from source/_tablefmt.py, which
IS translated: it is a copy rather than an import of the English file because
that one is also read by build-catala-module.py, which stays English.

WHY THE HEBREW GOES THROUGH THE GENERATOR AND NOT THROUGH A HAND EDIT. The
tables are written with ditto carets, and a caret resolves by EXACT COLUMN.
Hebrew names are not the width of their English counterparts, so every column
in the grid moves — the ruler comment, the constructor, OF, THEN and all nine
amount columns. _tablefmt computes every one of those from len(SUBJ) and
len(CTOR), so translating the two constants moves the whole grid together. A
hand translation would have had to recompute 36 lines x 2 tables of padding,
and ditto fails SILENTLY when a caret lands on the wrong token.

The prose around the tables lives in this file rather than beside the L4,
because a generated file that is half hand-edited is a file nobody dares
regenerate.

Run:  OFEK_CORPUS=<checkout> python3 source/build-salary-table-module.py > ofek-salary-table.l4
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _tablefmt  # noqa: E402
import tables  # noqa: E402

ROOT = tables.corpus_root(sys.argv)
D = tables.load(ROOT)
MARGINS, RANK_STEP = tables.margins_from_shekel_printing(ROOT)
N = tables.l4num
OUT = []

ROW = '`השורה`'
RANK = '`הדרגה`'
FIELDS = [f'`בדרגה {d}`' for d in range(1, 10)]


def w(s=''):
    OUT.append(s)


def declare_row():
    """The record: nine NUMBER fields, one per rank."""
    out = [f'DECLARE {_tablefmt.CTOR} HAS']
    width = max(len(f) for f in FIELDS)
    for f in FIELDS:
        out.append(f'    {f.ljust(width)} IS A NUMBER')
    return out


def rank_reader():
    """The nine-armed BRANCH that reads one field out of a row.

    Dittoed the same way the tables are, and for the same reason: every column
    is computed, so the carets cannot drift when the names change width. A
    backtick identifier is ONE token, so the field names themselves cannot be
    dittoed away; the record and its genitive can.
    """
    out = []
    for d in range(1, 10):
        first, last = d == 1, d == 9
        subj = RANK if first else '^'.ljust(len(RANK))
        row = ROW if first else '^'.ljust(len(ROW))
        gen = "'s" if first else '^ '
        then = 'THEN' if first else '^   '
        if first:
            head = f'    BRANCH IF {subj} AT MOST 1 '
        elif last:
            head = '           OTHERWISE'.ljust(len(f'           IF {subj} EQUALS  1 '))
            then = '    '
        else:
            head = f'           IF {subj} EQUALS  {d} '
        out.append(f'{head}{then} {row}{gen} {FIELDS[d - 1]}')
    return out


w('''@lang he

IMPORT prelude
IMPORT `ofek-domain`

§ `טבלאות השכר המשולב`

-- ===========================================================================
-- קובץ מחולל — אין לערוך ביד.
--   source/build-salary-table-module.py, מן הרשתות שמנתח source/tables.py
--   ובפריסה של source/_tablefmt.py. לחילול מחדש:
--     OFEK_CORPUS=<checkout> python3 source/build-salary-table-module.py > ofek-salary-table.l4
--
-- טבלת השכר המשולב, § 35 להסכם 2008 כפי שהוחלף מיום 1 בספטמבר 2022 בסעיף 4.1
-- להסכם הקיבוצי מיום 19 באוקטובר 2022.
--
-- איזו הדפסה היא המחייבת. ההסכם משנת 2022 צירף את טבלאותיו מעוגלות לשקל.
-- החלטה של ועדת המעקב המשותפת מיום 14 בינואר 2025 תיקנה טעות סופר באותו הסכם
-- והחליפה את נספחים א׳1 ו-א׳2 בטבלאות הנקובות באגורות, בתוקף מאותו 1 בספטמבר
-- 2022. טבלאות האגורות הן אפוא הנוסח שבתוקף לכל התקופה, והן שמודול זה מקודד:
--   /agreements/ofek-hadash/2025-01-14_ofek-hadash_vaadat-maakev_taut-sofer-correction_agorot-salary-tables.html
-- ההדפסה השקלית שב-/tables/2022-09-01_ofek-hadash_salary-table_BA.html ואחותה
-- לבעלי תואר שני מעגלות סכומים אלה וזהות להם בכל יתר הפרטים; אותן ימצא הקורא
-- קרוב לוודאי ראשונות, ומשום כך ההבדל נאמר כאן.
--
-- מהי הטבלה. השורות הן ותק (§ 37), 1 עד 36. העמודות הן דרגה (§§ 36 ו-38), 1
-- עד 9. תא הוא השכר המשולב החודשי בשקלים חדשים למשרה מלאה; § 33 והסכם 2022
-- § 5.3 מחשבים אותו באופן יחסי למשרה חלקית.
--
-- התאים הממוזגים. הטבלה אינה נותנת 324 מספרים נבדלים. היא נותנת 224,
-- וההדפסה השקלית פורשת כל אחד מהם על פני הדרגות שלצדו כתא ממוזג: בוותק 3 היא
-- מדפיסה סכום אחד תחת דרגה 1 וסכום אחר המשתרע על דרגות 2 עד 9. מודול זה
-- משחזר זאת — הערך האחרון שהוגדר חוזר בכל דרגה שמעבר לו — ורושם את הגבול
-- בנפרד להלן, משום שהגבול הוא החלק שקורא יכול לבדוק מול § 38. הדפסת האגורות
-- והטבלאות מיום 1.1.2015 מותירות את אותם מקומות עצמם ריקים במקום למזגם,
-- ומשום כך NOTES.md § 5 מתייחס לשאלה "מה פירושו של תא ממוזג" כשאלת פרשנות
-- פתוחה ולא כקריאה מוכרעת.
--
-- כיצד לקרוא את שתי הטבלאות שלהלן. כל אחת מהן היא טבלת החלטה, שורה אחת לכל
-- ותק. הרשומה נבנית לפי מיקום באמצעות OF, כך שהדרגה נישאת בעמודה ולא בשם שדה
-- חוזר, והערת הסרגל שמעל כל טבלה נוקבת בשמות העמודות פעם אחת. נושא התנאי,
-- THEN, הבנאי ו-OF נכתבים בשורה הראשונה ומועתקים אחריה באמצעות ^ — הסימן ^
-- הוא האסימון שבאותה עמודה בשורה שמעליה. מה שנותר בשורה הוא מה שמשתנה:
-- הוותק ותשעת הסכומים.
-- ===========================================================================

§§ `שורה בטבלה`
''')

for line in declare_row():
    w(line)

w()
w(f'GIVEN {ROW} IS A {_tablefmt.CTOR}')
w(f'      {RANK} IS A NUMBER')
w('GIVETH A NUMBER')
w(f'`הסכום בשורה לפי דרגה` {ROW} {RANK}')
w('    @nlg הסכום בשורה לפי הדרגה הנתונה')
w('    MEANS')
w('    -- הדרגות נעות בין 1 ל-9 (§ 38). דרגה הנמוכה מ-1 קוראת את העמודה')
w('    -- הראשונה ודרגה הגבוהה מ-9 את האחרונה; אף אחת מהן אינה נגישה דרך § 38,')
w('    -- ומודול השיבוץ דוחה דרגה כזו עוד לפני שנקראת כאן.')
w('    -- מזהה בגרשיים אחוריים הוא אסימון אחד, ולכן אי אפשר להחליף את שמות')
w('    -- השדות בסימן ^; את הרשומה ואת הסמיכות שלה כן אפשר.')
for line in rank_reader():
    w(line)

w()
w('§§ `נספח א׳1 — טבלת השכר למורים בעלי תואר ראשון, קוד דירוג 101`')
w()
for line in _tablefmt.signature('שורת טבלת תואר ראשון לפי ותק',
                                'טבלת תואר ראשון (קוד דירוג 101)'):
    w(line)
for line in _tablefmt.rows(D['BA'], N):
    w(line)

w()
w('§§ `נספח א׳2 — טבלת השכר למורים בעלי תואר שני, קוד דירוג 102`')
w()
for line in _tablefmt.signature('שורת טבלת תואר שני לפי ותק',
                                'טבלת תואר שני (קוד דירוג 102)'):
    w(line)
for line in _tablefmt.rows(D['MA'], N):
    w(line)

w(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_salary-table-tail.l4'),
       encoding='utf8').read().rstrip('\n'))

sys.stdout.write('\n'.join(OUT) + '\n')
