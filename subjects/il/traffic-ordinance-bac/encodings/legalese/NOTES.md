# NOTES — il/traffic-ordinance-bac, encoding row `legalese`

**Status: `draft`.** Deposited 2026-09-22 on the drafts shelf. **Verified**: `check.sh` exit 0 on legalese/prereleases `unstable-20260907-9d6536a` (linux-x64); the output is pasted in section 10. Not reviewed by anyone who knows Israeli traffic law (HG1 not sought).

## 1. What this is

The drink-driving alcohol thresholds of Israeli law, put on L4's **rule-effective-time axis** so that one rule, asked under two vintages of the text, gives two answers. Two instruments, one encoding row:

- **The Ordinance.** פקודת התעבורה [נוסח חדש], התשכ״א–1961. `drink-driving.l4` encodes s.64B(a)'s definition of "שיכור" (intoxicated), paragraphs (3) and (3A), and s.62(3), the offence of being intoxicated while driving on a road or in a public place.
- **The Regulations.** תקנות התעבורה, התשכ״א–1961. `drink-driving.l4` encodes reg. 169A's definition of "ריכוז אלכוהול בגוף" (alcohol concentration in the body), the general threshold.

`drink-driving-tests.l4` holds 30 assertions and the two `#EVAL`s that go on a slide.

## 2. Why: Roznai's stale copy

Yaniv Roznai, *Law "Wants to be Free"* (HaPraklit 52, 2013), searched for the Traffic Ordinance and found that the first Google result — a parking-ticket portal — served a text without **Amendment No. 97** (חוק לתיקון פקודת התעבורה (מס׳ 97), התשע״א–2010), the amendment that inserted paragraph (3A) into the definition and so changed the threshold for new, young and professional drivers. A citizen relying on that text would have read the wrong limit.

That is a story about *which version of the text* a reader gets, and it is exactly what the rule-effective axis exists for. The encoding does not hold two copies of the definition; it holds one, whose threshold is a function of `RULES EFFECTIVE DATE`, and the tests pin that date to the day before publication and the day of it.

## 3. Which instrument carries which number, and why it matters

| threshold | who | breath (µg / litre exhaled air) | blood (mg / 100 ml) | where | since |
| --- | --- | --- | --- | --- | --- |
| general | every driver, s.64B(a)(3) "the concentration the Minister prescribed" | 240 | 50 | **reg. 169A**, Traffic Regulations | 10 November 2009 (K.T. 6825 p. 114, Amendment No. 3 of 5770) |
| paragraph (3A) | a new driver; a driver under 24; a driver of a commercial or work vehicle whose permitted gross weight exceeds 3,500 kg; a driver of a public vehicle | 50 | 10 | **s.64B(a)(3A)**, the Ordinance itself | 9 December 2010 (S.H. 2265 p. 91, Amendment No. 97) |

So the answer to "does the Ordinance or the Regulations carry the numbers" is **both, and it is the split that makes the case interesting**: the Knesset put the strict figures for the listed classes into primary legislation while leaving the general figure to the Minister. A reader with a stale Ordinance and a current set of Regulations would get the general threshold right and the young-driver threshold wrong, which is precisely Roznai's reader.

Paragraph (3A) in the consolidated Wikisource text (revision 3081544) is, word for word, the paragraph the 2010 gazette inserted: the same four classes, the same lettering, the same figures. s.64B carries later amendment marks (תשע״ב־4, תשע״ט, תשפ״ב־2); whatever they changed, it was not the text of (3A), because the two texts were compared. So the encoding holds one vintage of (3A), not two, and that is a finding from the deposit rather than an assumption.

**A drafting defect found on the way.** Amendment No. 3 of 5770 deleted the defined term "המידה הקבועה" from reg. 169A and inserted "ריכוז אלכוהול בגוף" in its place. But reg. 169B's title and subregulation (c), reg. 169D(b) and reg. 169F still say "עולה על המידה הקבועה" — a term the Regulations no longer define, sixteen years on. This is the kind of thing a legality check that resolves defined terms would flag; SimpLEX shows such a panel. It is recorded here and does not affect the encoding, which reads the substituted definition.

## 4. Amendment 97's commencement date, and how it was established

**From the deposited gazette issue**, `source/sefer-hachukim-2265-p91-amendment-97.pdf`, text layer extracted with PyMuPDF and read phrase by phrase (Hebrew comes out of a PDF in visual order; nothing was eyeballed in a terminal):

- The Act is **one section**, s.1, amending s.64B(a): paragraph (1) inserts (3A) after (3); paragraph (2) adds "או מהסף כאמור בפסקה (3א), לפי העניין" to paragraph (4).
- **There is no commencement (תחילה) section.**
- The footnote records adoption by the Knesset on כ״ב בכסלו התשע״א (**29 November 2010**) and the bill in Hatza'ot Chok HaKnesset 335 of 5 July 2010 p. 196.
- The issue footer reads ספר חוקים 2265, ב׳ בטבת התשע״א, **9.12.2010**.

An Act with no commencement clause commences on publication. That default rule was **not pinned to its current statutory provision**: the Law and Administration Ordinance 5708-1948 s.10(a) states it for ordinances ("כל פקודה תקבל תוקף ביום פרסומה ברשומות, בלתי אם נקבע בה ..."), the Interpretation Ordinance s.17 states it for regulations, and the Transition Law 5709-1949 s.2(c), which stated it for Knesset laws, is marked repealed in the Wikisource text. The rule is uncontroversial, but the encoding's date rests on it, so it is **fork F1** rather than a bare fact. Roznai's "November 2010" is the adoption date; the tests use 8 and 9 December, so the point survives whichever date is preferred.

## 5. The rule-effective axis, in this encoding

```
`Amendment 97 is in force` MEANS
    DATE_SERIAL `RULES EFFECTIVE DATE` AT LEAST DATE_SERIAL `the commencement of Amendment 97`
```

is the whole of the versioning. `the alcohol concentration above which the driver is intoxicated` returns the paragraph (3A) pair when that holds and the driver is in a listed class, the reg. 169A pair otherwise, and `NOTHING` for a rules-effective date before 10 November 2009 (section 6, F2). `the driver is intoxicated` turns that into a three-valued `Finding` — `intoxicated`, `not intoxicated`, `the text in force on that date is not encoded` — so the slide reads as words rather than as `JUST OF TRUE`.

The two lines:

```
#EVAL `EVAL UNDER RULES EFFECTIVE AT` (YMD 2010 12 8) (`the driver is intoxicated` `a 22-year-old with a full licence, driving a private car` (`breath sample` 100))
-- `not intoxicated`      100 µg/L is under the general 240
#EVAL `EVAL UNDER RULES EFFECTIVE AT` (YMD 2010 12 9) (`the driver is intoxicated` `a 22-year-old with a full licence, driving a private car` (`breath sample` 100))
-- intoxicated            paragraph (3A) is in force: 100 exceeds 50
```

The tests also show the other axes: with no pin at all the date falls back to today (intoxicated); with only the **facts** pinned (`EVAL UNDER VALID TIME (YMD 2010 6 1)`) the rule-effective date follows the valid time and the driver stopped in June 2010 is not intoxicated — the presumption against retroactivity as the default, from the multi-temporal tutorial's Step 3.

## 6. Forks (interpretive choices)

- **F1, commencement.** Publication day, 9 December 2010, by the default rule, because the Act has no commencement clause (section 4). Alternative: adoption day, 29 November 2010. Not adopted; the tests straddle 8/9 December so either reading gives the same story.
- **F2, the general threshold before 10 November 2009.** Reg. 169A's present definition dates from K.T. 6825; before it the Regulations defined "המידה הקבועה", inserted by Amendment No. 3 of 5742 (K.T. 4335 p. 830, 1982). That gazette is served by olaw.org.il as a 17-page image-only scan with no text layer; it was fetched, could not be read, and is not deposited. The figures were very probably the same 240/50 — but "very probably" is what Roznai's parking portal offered too. The encoding therefore returns `the text in force on that date is not encoded` for any rules-effective date before 2009-11-10, and a test pins that. Alternative: assume 240/50 back to 1982.
- **F3, "שטרם מלאו לו 24 שנים".** An `age in years` input compared with 24, not date-of-birth arithmetic against the day of the sample. The valid-time axis could carry the birthday; it does not here.
- **F4, "נהג חדש".** An input. s.12A's two years from the first licence, its extensions on indictment or fine, and the exclusion of motorcycle-only prior licences are not derived.
- **F5, "העולה על" / "עולה על".** Strict everywhere: a reading of exactly 50 µg or 10 mg for a listed driver, exactly 240 µg or 50 mg for any driver, and a vehicle of exactly 3,500 kg, are not over the figure. Tests pin each boundary.
- **Vehicle classes.** `private vehicle`, `public vehicle` and `commercial or work vehicle` (with its permitted gross weight) are the only three, because they are the only ones paragraph (3A) distinguishes; a motorcycle or a tractor falls under `private vehicle` for this purpose, which is right for the threshold and wrong as a description.

## 7. What is not here

- Paragraphs (1) (drinking while driving), (2) (dangerous drugs) and (4) (under the influence, with the concentration floor) of the definition.
- The three-hour presumption in paragraph (3) ("וחזקה שריכוז זה היה בגופו בשלוש השעות שקדמו ...") and its rebuttal.
- s.64B(a1)–(o): the sampling powers, saliva tests, consent, detention, and the evidential certificate.
- The "ממונה על הרכב" (person in charge — a driving instructor, an accompanying adult) limb of s.62(3), and the penalty.
- s.64D, refusal to be tested, which the Ordinance treats as intoxication.
- Reg. 169B–169I, the Regulations' own procedure, and the stale "המידה הקבועה" references (section 3).
- No `cases/`, `registers/`, `report/` or `gates/`, no goldens, no pipeline registration: deposited source, two encodings, tests, notes.

## 8. Tooling limits observed on this binary

- The binary (l4-ide commit 9d6536a, built 2026-09-07) **predates `@lang`, `@nlg:he` and `l4 nlg --lang`** (PR #432, 2026-09-19): `@lang en` fails at the lexer. Both rows therefore carry untagged `@nlg` heralds in their own language, and the Hebrew twin is a separate row rather than a `--lang he` rendering. See `../legalese-he/NOTES.md` § 3.
- `RULES EFFECTIVE DATE` with no pin requires `TIMEZONE IS "..."` **in every document that evaluates it**, including a test module that only imports the rule. Both modules declare `Asia/Jerusalem`.
- A one-word enum constructor prints bare (`intoxicated`) and a multi-word one backticked (`` `not intoxicated` ``). `twin-check.py --unmap` handles both when comparing the rows' output.
- `l4 nlg` prints `%name%` placeholders as the bare parameter followed by `with <arguments>`, as the HVAC row recorded; the heralds are written to survive that.

## 9. The Hebrew twin

`../legalese-he/` is the same encoding with every identifier, `§` title, herald and statute quotation in Hebrew, hand-written. Two mechanical checks hold it to this row, both run by `check.sh` here and there: `source/twin-check.py` requires the modules to be **token-for-token identical** once `glossary.json` is applied (comments and herald text aside), and the cross-row comparison requires every `Result:` block of the two test modules to be identical after mapping the Hebrew names back. **This row is the oracle.** The glossary marks each name `ordinance`, `regulations` or `composed`, and the composed ones are listed in `../legalese-he/NOTES.md` § 5 for a Hebrew reviewer.

## 10. Verification

Binary: legalese/prereleases tag `unstable-20260907-9d6536a`, linux-x64, archive sha256 `cc6895c765c57fb7c218311e95ad66781e86e88a5694b7b7b4fa40f5446a8226` — the digest embedded in `legalese/l4-plugin` `scripts/install-l4.sh`, verified before unpacking. `JL4_LIBRARY_PATH` unset. Run 2026-09-22:

```
$ sh encodings/legalese/check.sh
drink-driving.l4             ok  (0 of 0 assertions satisfied)
drink-driving-tests.l4       ok  (30 of 30 assertions satisfied)

  the Roznai scenario -- a 22-year-old, 100 micrograms per litre of exhaled air:
    RULES EFFECTIVE AT 2010-12-08   -> `not intoxicated`
    RULES EFFECTIVE AT 2010-12-09   -> intoxicated

drink-driving-he.l4            is drink-driving.l4 renamed: 303 tokens identical, 106 of them through the glossary
drink-driving-tests-he.l4      is drink-driving-tests.l4 renamed: 572 tokens identical, 172 of them through the glossary
drink-driving-tests.l4       agrees with ../legalese-he/drink-driving-tests-he.l4  (34 Result blocks identical)
exit=0

$ sh encodings/legalese-he/check.sh
drink-driving-he.l4          ok  (0 of 0 assertions satisfied)
drink-driving-tests-he.l4    ok  (30 of 30 assertions satisfied)

  התרחיש של רוזנאי – נהג בן 22, 100 מיקרוגרם אלכוהול בליטר אוויר נשוף:
    RULES EFFECTIVE AT 2010-12-08   -> `אינו שיכור`
    RULES EFFECTIVE AT 2010-12-09   -> שיכור

drink-driving-he.l4            is drink-driving.l4 renamed: 303 tokens identical, 106 of them through the glossary
drink-driving-tests-he.l4      is drink-driving-tests.l4 renamed: 572 tokens identical, 172 of them through the glossary
drink-driving-tests-he.l4    agrees with ../legalese/drink-driving-tests.l4  (34 Result blocks identical)
exit=0
```

**Positive control**, run before the checks were believed: the paragraph (3A) breath figure changed from 50 to 51 in `drink-driving-he.l4` alone.

```
drink-driving-tests-he.l4    FAIL: 1 errors, 29 of 30 assertions satisfied
drink-driving-he.l4            DIVERGES from drink-driving.l4 at token 114:
    drink-driving.l4 line 113: 50  ->  expected 50
    drink-driving-he.l4 line 98: 51
drink-driving-tests-he.l4    DISAGREES with ../legalese/drink-driving-tests.l4
21c21
<   assertion satisfied
---
>   assertion failed
exit=1
```

Restoring the figure returned exit 0.

## 11. How to run

```
sh check.sh                        # l4 on PATH
BAC_L4=/path/to/l4 sh check.sh     # or name the binary
l4 run drink-driving-tests.l4      # the raw output
python3 ../../source/twin-check.py # the structural twin check alone
```
