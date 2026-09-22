# il/traffic-ordinance-bac

**Israel's drink-driving alcohol thresholds — Traffic Ordinance s.64B(a) "intoxicated" and Traffic Regulations reg. 169A — in L4, with the threshold on the rule-effective-time axis, so one rule asked under two vintages of the law gives two answers.**

Yaniv Roznai (*Law "Wants to be Free"*, HaPraklit 52, 2013) searched for the Traffic Ordinance and found that the top Google result served a text without **Amendment No. 97 of 2010**, the amendment that set a 50-microgram breath threshold for new drivers, drivers under 24, drivers of heavy commercial vehicles and drivers of public vehicles, where the general threshold is 240.
A citizen relying on that text would have read the wrong limit.

This row encodes the definition once and asks it twice:

```
#EVAL `EVAL UNDER RULES EFFECTIVE AT` (YMD 2010 12 8) (`the driver is intoxicated` `a 22-year-old with a full licence, driving a private car` (`breath sample` 100))
-- `not intoxicated`
#EVAL `EVAL UNDER RULES EFFECTIVE AT` (YMD 2010 12 9) (`the driver is intoxicated` `a 22-year-old with a full licence, driving a private car` (`breath sample` 100))
-- intoxicated
```

Amendment 97 was published in Sefer HaChukim 2265 on 9 December 2010 (deposited in `source/`) and has no commencement clause.

| where | what |
| --- | --- |
| `encodings/legalese/drink-driving.l4` | s.64B(a) paragraphs (3) and (3A), reg. 169A, s.62(3); the threshold is a function of `RULES EFFECTIVE DATE` |
| `encodings/legalese/drink-driving-tests.l4` | 30 assertions: the flip on 9 December 2010 for every class paragraph (3A) lists, the boundaries, the dates the encoding refuses, the valid-time axis |
| `encodings/legalese-he/` | the Hebrew-canonical twin, hand-written, held token-for-token to the English row by `source/twin-check.py` and `glossary.json` |
| `encodings/legalese/NOTES.md` | which instrument carries which number, how the commencement date was established, the forks, the limits, the verification output |
| `source/` | pinned Wikisource revisions of both instruments, the two gazette issues, digests |

No goldens, no registers, no report, no gates: deposited source, two encodings, tests, notes.

---

# il/traffic-ordinance-bac — בעברית

**ספי ריכוז האלכוהול בנהיגה בשכרות – ההגדרה ”שיכור“ שבסעיף 64ב(א) לפקודת התעבורה ותקנה 169א לתקנות התעבורה – בשפת L4, כשהסף מונח על ציר מועד התחילה של הכללים, כך שכלל אחד, הנשאל לפי שתי גרסאות של הדין, נותן שתי תשובות.**

יניב רוזנאי (*החוק ”רוצה להיות חופשי“*, הפרקליט נב, 2013) חיפש את פקודת התעבורה ומצא שהתוצאה הראשונה בגוגל הגישה נוסח ללא **תיקון מס׳ 97 משנת 2010**, התיקון שקבע סף של 50 מיקרוגרם בליטר אוויר נשוף לנהג חדש, לנהג שטרם מלאו לו 24, לנהג רכב מסחרי כבד ולנהג רכב ציבורי, מקום שהסף הכללי הוא 240.
אזרח שהסתמך על אותו נוסח היה קורא את הגבול הלא נכון.

הקידוד כאן מקודד את ההגדרה פעם אחת ושואל אותה פעמיים:

```
#EVAL `EVAL UNDER RULES EFFECTIVE AT` (YMD 2010 12 8) (`הנהג שיכור` `נהג בן 22 שאינו נהג חדש, ברכב פרטי` (`דגימת נשיפה` 100))
-- `אינו שיכור`
#EVAL `EVAL UNDER RULES EFFECTIVE AT` (YMD 2010 12 9) (`הנהג שיכור` `נהג בן 22 שאינו נהג חדש, ברכב פרטי` (`דגימת נשיפה` 100))
-- שיכור
```

תיקון מס׳ 97 פורסם בספר החוקים 2265 ביום 9.12.2010 (מופקד ב־`source/`) ואין בו סעיף תחילה.

הקידוד האנגלי (`encodings/legalese/`) הוא האורקל; הקידוד העברי (`encodings/legalese-he/`) נכתב ביד, ו־`source/twin-check.py` מוכיח שהוא זהה לו אסימון לאסימון דרך `glossary.json`, ו־`check.sh` מוכיח שהם משיבים אותן תשובות. המילים הן של הפקודה והתקנות עצמן היכן שיש להן מילים; `glossary.json` מסמן את השאר `composed`.
