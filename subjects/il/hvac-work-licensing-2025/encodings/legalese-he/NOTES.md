# הערות — `legalese-he`, הקידוד העברי

**מצב: טיוטה. לא נבדק.**
זהו התאום העברי של [`../legalese`](../legalese): אותם חמישה מודולים, אותם כללים, אותן קביעות (assertions), כשכל מזהה, כל כותרת `§` וכל תרגום ברירת־המחדל הם בעברית.
**האורקל הוא הקידוד האנגלי.** דבר לא נגזר כאן מחדש: אף מספר לא חושב שוב, אף כלל לא שונה, אף קביעה לא נוספה ולא נגרעה. אם נתון כלשהו כאן חולק על הקידוד האנגלי — הטעות כאן, לא שם.

**הקובץ הזה נוצר אוטומטית.** `../../source/revoice.py` קורא את חמשת המודולים האנגליים ואת `glossary.json` שבתיקייה זו, ומייצר מהם את חמשת המודולים העבריים. לחידוש:

```
python3 subjects/il/hvac-work-licensing-2025/source/revoice.py
sh check.sh
```

**המילים הן של החוק עצמו היכן שיש לו מילים.** `GLOSSARY.md` רושם לכל מזהה אם המילה לקוחה מן החוק (`law`), מן התוספת השנייה (`schedule`), מתקנות האגרות (`regulations`), או שהיא שלנו (`composed`). הנחוצות לבדיקה אנושית הן אלה שסומנו `composed`.

**שתי בדיקות שונות חסרות, ואין לערבב ביניהן.** *החוק* כאן לא נבדק בידי מי שמכיר את רישוי המקצועות בישראל — כל מה ש[`../legalese/NOTES.md`](../legalese/NOTES.md) אומר על כך חל כאן ללא שינוי. *העברית* כאן לא נבדקה בידי איש, וזו חסרה אחרת, עם בודק אחר. מה שכן נבדק: שהעברית עוברת ניתוח תחבירי, בדיקת טיפוסים, הרצה — ושהיא מחזירה בדיוק את אותן תשובות. זו טענה על המכונה, לא על הלשון.

---

# NOTES — `legalese-he`, the Hebrew-canonical row

**Status: `draft`, not reviewed.**
This row is the Hebrew-canonical twin of [`../legalese`](../legalese), deposited 2026-09-21.

## 1. What this is, and what it is not

The **same five modules** as `../legalese`, the same rules, the same assertions, with every identifier, record field, enum constructor, `§` title and default rendering in Hebrew.

It is a **revoicing, not a re-derivation**, and the distinction is the whole of its status.
`../legalese` is the oracle.
No number was recomputed here, no rule restructured, no assertion added or dropped.
If a figure in this row ever disagrees with the English one, this row is wrong **by construction**, and the repair belongs here or in `glossary.json`, never there.

**It is generated, not written.** `../../source/revoice.py` reads the five English modules plus `glossary.json` and emits the five Hebrew ones by exact-token substitution. It refuses to write anything if the glossary is not injective, if a backticked identifier in the English row has no entry, or if an `@nlg` has lost its paired `@nlg:he`. It also warns when a glossary entry has stopped being used or a quoted comment no longer matches — both of which mean the English row moved and this one has not caught up.

Why bother, given that `../legalese` already renders Hebrew on demand. Because a rendering is not an encoding. In the English row the Hebrew is an `@nlg:he` string hanging off an English name, so a Hebrew reader reads Hebrew sentences about `the registrar shall grant the licence`; the `§` headings stay English whatever `--lang` says; and nothing a reviewer can check is in Hebrew except the prose. Here the names themselves are the statute's words, and the English is the thing hanging off them.

## 2. How to run it

```
sh check.sh                      # binary and prelude from the worktree named inside it
HVAC_L4=/path/to/l4 HVAC_LIBS=/path/to/jl4-core/libraries sh check.sh
python3 ../../source/revoice.py  # regenerate the five modules and GLOSSARY.md
```

`check.sh` does four things, and the fourth is the one that matters:

1. The four green modules run with zero errors, and it counts the satisfied assertions.
2. `hvac-tests-simplex-red-he.l4` fails on **exactly three** assertions, as its English twin does. It is the positive control: proof the harness can go red.
3. The renderings are checked **in both directions**. The default rendering must contain no English herald word, and the `--lang en` rendering no Hebrew herald text, once backticked identifiers are struck out. Identifiers are Hebrew in both and are not a finding.
4. **Cross-row agreement.** For each of the four comparable modules it runs the English row and this one, maps this row's output back through the inverse of `glossary.json`, and requires the `Result:` blocks to be **identical line for line** — not merely equal in count. That compares every `#EVAL`'s answer, in order, including enum constructors, `MAYBE` wrappers and dates.

Measured 2026-09-21, both rows on the same binary:

| module | assertions, `../legalese` | assertions, here | `Result:` blocks |
| --- | --- | --- | --- |
| law | 27 | 27 | 31, identical |
| fees | 4 | 4 | 5, identical |
| tests-simplex | 39 | 39 | 51, identical |
| tests-generated | 193 | 193 | 193, identical |
| tests-simplex-red | 3 failed | 3 failed | — |

The agreement check was given a positive control before being believed: changing one licence fee from 284 to 285 in `hvac-fees-he.l4` alone turns `hvac-tests-simplex-he.l4` red and `check.sh` exits 1. Restoring it returns exit 0.

## 3. The multilingual mechanism, and its one asymmetry

Each module declares `@lang he` once, so the **untagged** `@nlg` herald is the Hebrew one and is what every annotation reader falls back to. The English wording rides along as `@nlg:en`. The revoicer performs that swap: where `../legalese` has `@nlg <english>` trailing the rule and `@nlg:he <hebrew>` on the line below, this row has `@nlg <hebrew>` trailing the rule and `@nlg:en <english>` below.

What follows is therefore true here and false in the English row: `l4 nlg` with no flag, and `l4 render --format html` with no flag, give a **Hebrew** document.

**Three things do not translate, and two of them are the tooling's, not ours.**

- **The linearizer's own connective vocabulary stays English** — `with`, `and`, `is equal to`, `not`, and the trace frame `executing contract … party … did … at`. A tag names a rendering; it does not localise the frame around it, and `@lang he` does not change that either. `check.sh` strikes exactly these words out before judging herald language, and the list is written out there so it can be re-checked rather than trusted.
- **Identifiers stay Hebrew under `--lang en`.** That is not a defect; it is what "Hebrew-canonical" means. The English rendering reads `the lowest licence grade that may work on a system whose cooling output is `תפוקה` kW`.
- **`l4 nlg` does not substitute `%name%` inline** — it prints the bare parameter name and appends `with <arguments>`. `l4 render` does substitute inline. Both are the tooling's behaviour, identical in the English row, and the heralds are written to read acceptably either way.

**`§` titles are not language-tagged**, which is precisely the gap `../legalese/NOTES.md` § 6 says a Hebrew-canonical twin would close. It is closed here: the headings are Hebrew in both renderings, because they are Hebrew in the source.

## 4. Hebrew filenames do not work — measured, not assumed

The five modules carry **Latin basenames with a `-he` suffix**. That is a fallback, and here is the measurement behind it, taken 2026-09-21 on the binary `check.sh` names.

| probe | result |
| --- | --- |
| a module named `חוק-קירור.l4`, run on its own | **green**, assertion satisfied |
| a module named `בדיקות3.l4` importing `` `hvac-law-he` `` | **green**, zero errors |
| a module importing `` `חוק-קירור` `` | 3 errors |
| a module importing `` `קירור` `` (no hyphen) | 3 errors |
| a module importing bare `קירור` | 3 errors |
| a module importing `` `קירור` `` and referencing **nothing** from it | **green**, 0 errors |

So Hebrew is fine in a filename and fine in an importing module; it is the **import target** that cannot be Hebrew. Hyphen or no hyphen, backticked or bare, it fails the same way.

**Read the error counts in that table as a symptom, not as a measure.** The last row is why: an import that resolved to nothing produces no diagnostic of its own, so the count tracks how many imported names the importing module happens to mention. Three is a property of these probes, not of the defect.

**The failure is silent, which is the part worth remembering.** There is no import diagnostic at all. What you get is `could not find a definition for the identifier` once for every name the import was supposed to supply, plus the `multiple definitions for __EQUALS__` that follows from the missing types — so it reads as a broken module, not as an unresolved import. The file URI is percent-encoded (`%D7%97%D7%95%D7%A7-…`) in every diagnostic, which is the only visible hint that the resolver and the filesystem are not looking at the same string.

**To reproduce.** This recipe was run verbatim, in an empty directory, on the binary `check.sh` names:

```sh
cat > 'קירור.l4' <<'EOF'
@lang he
IMPORT prelude
DECLARE דרגה IS ONE OF `דרגה 1`, `דרגה 2`
GIVEN קוט IS A NUMBER
GIVETH A דרגה
DECIDE `הדרגה הנמוכה ביותר` IS IF קוט AT MOST 18 THEN `דרגה 1` ELSE `דרגה 2`
EOF
cp 'קירור.l4' latin.l4

# control: Latin import target, Hebrew everything else
printf '@lang he\nIMPORT prelude\nIMPORT `latin`\n#ASSERT `הדרגה הנמוכה ביותר` 19 EQUALS `דרגה 2`\n' > control.l4
# probe: the SAME module under its Hebrew name
printf '@lang he\nIMPORT prelude\nIMPORT `קירור`\n#ASSERT `הדרגה הנמוכה ביותר` 19 EQUALS `דרגה 2`\n' > probe.l4
# the same probe with nothing referencing the import
printf '@lang he\nIMPORT prelude\nIMPORT `קירור`\n' > silent.l4

l4 run 'קירור.l4'   # 0 errors -- a Hebrew FILENAME is fine
l4 run control.l4    # 0 errors -- a Hebrew IMPORTER is fine
l4 run probe.l4      # 3 errors, none of them about the import
l4 run silent.l4     # 0 errors
```

The control is what makes this a finding rather than an observation: it isolates the Hebrew basename from the hyphen, from `@lang he`, and from the Hebrew content of the imported module, all of which are fine on their own. Only the Hebrew basename *as an import target* fails.

`silent.l4` is the sharper half, and it was found by running this recipe rather than by reasoning about it. **A module that imports a Hebrew basename and does not use anything from it is GREEN.** The import brought in nothing and nothing complained. So the error count is not a measure of the defect at all — it is a measure of how many imported names the importing module happens to mention, which is why a count quoted from one probe should not be carried to another.

Worth filing upstream. It is the same family as the silent `GraphException` on a self-import that `l4-ide/CLAUDE.md` § 5 records: an import that cannot resolve should say so. Until it does, a Hebrew-canonical row cannot use Hebrew filenames, and the workaround has to be written down wherever the next one is built, because the symptom points at the wrong file.

The probe files are in this session's scratchpad, not in canon: canon holds no non-ASCII filename, by design.

## 5. What the glossary could not take from the instruments

`GLOSSARY.md` carries the full table with a note per entry. The entries marked `composed` are the ones no instrument supplied, and they are where a Hebrew reviewer should start. The ones a reviewer is most likely to want to change:

- **`ניסיון מזכה`** for the experience route. The Second Schedule spells the row out — a year's cumulative experience out of three, or three out of seven — and never names it.
- **`נוסח`** for a *vintage* of regulation 2. Taken from reg. 3(b)'s `נוסח תקנה 2 כפי שהשתנתה`, but the Regulations never contemplate three texts side by side, so the word is doing work the drafter did not ask of it.
- **`תוצאה`** and its three constructors, and **`הערעור נבדק`** in particular. Those are the SimpLEX screen's own phrases, transcribed from Figure 4. Note the screen says **ערעור** where reg. 2(b) says **השגה**; the screen's word is kept, because that enum transcribes the screen rather than the Regulations.
- **`דרגה 1/2/3`** rather than the Law's full defined term `רישיון דרגה 1`. The full term would make the herald read `רישיון רישיון דרגה 1`; the word `רישיון` is carried by the heralds instead.
- **`יום התחילה של החוק`** for the rule, against bare **`יום התחילה`** for the parameter. Both are s.63(a)(1)'s `יום התחילה`, and L4 will not let two identifiers share a name, so one had to be lengthened.
- **`המבקש` / `מבקש`, `הדרגה` / `דרגה`, `השירות` / `שירות`, `הנוסח` / `נוסח`.** The definite form is the parameter, the indefinite the type. A reviewer may prefer a different device for keeping them apart.

**Two bare identifiers could not take the statute's spelling**, because a bare name may carry only letters and digits — L4's lexer ends the token at anything else, and a maqaf is not a letter:

- `kw` is **`תפוקה`**, not the statute's `קילו־ואט`, whose maqaf would split the token. `revoice.py` enforces this and refuses to emit a bare name with a non-letter in it.
- `eighteen` is **`שמונהעשר`**, written solid.

Inside backticks both would have been fine: `isPrint` accepts the maqaf and the geresh, and the section titles here use both (`פרק א׳`, `קירור־ואוויר`). **Bidi control marks are the one hard limit** — RLM and LRM are category `Cf`, `isPrint` is false for them, and they are rejected inside backticks. Nothing here embeds one; the files rely on the viewer's own bidi algorithm, which is why an RTL identifier followed by a number can look transposed in a terminal and is correct in the bytes.

## 6. What stayed English on purpose

**The commentary.** Every comment that explains the encoding — why a fork was taken, what a Schedule item number is, what is not modelled — is English, and this file is English below the Hebrew summary. The rules are for Hebrew readers; the commentary around them is addressed to whoever maintains the encoding, alongside `../legalese/NOTES.md`. That is a real cost to a reviewer who reads only Hebrew, and it is recorded here rather than defended.

**But the statute quotes are not.** Fifteen comment blocks in the English row quote the Law or the Regulations *in English translation*; each is replaced here with the Hebrew original from `../../source/law.wiki` or `../../source/regulations-fees.wiki`. Those are the sentences a reviewer checks the encoding against, so a translation of them would be a translation of the wrong thing.

**One block could not be:** the **SimpLEX draft** vintage of regulation 2. Its only witness is a screen capture in a published paper, so there is no deposited Hebrew to restore; those comments keep the English row's transcription and say so. That is fork F3 showing up in a second place.

**`@desc` and `@export` are translated whole**, from the glossary's `prose` map rather than composed out of renamed parts, because they carry sentences rather than identifiers. There are sixteen.

## 7. Known drift, and one claim in a sibling file that is now false

`../legalese/encoding.json` still says, in `language.note`, that *"A Hebrew-canonical twin row (Hebrew identifiers, English heralds) is NOT deposited; see NOTES.md section 6"*, and `../legalese/NOTES.md` § 6 says the same. **Both are false as of this deposit.** They were not corrected here because this row may edit nothing in the English row except the pointer appended to its `check.sh`. Whoever next touches the English row should fix them; the sentence to replace them with is that the twin is at `../legalese-he`, is generated from the English row, and is checked against it.

The two rows are edited on different clocks, so drift is the standing risk. Three things guard against it, in ascending order of strength: the revoicer **fails** on an uncovered identifier; it **warns** on a glossary entry nothing uses and on a quoted comment that no longer matches; and `check.sh` § 4 **compares the answers themselves**. The first two catch a change in the vocabulary, the third catches a change in the law.
