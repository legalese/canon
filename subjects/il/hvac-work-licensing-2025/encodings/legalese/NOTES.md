# NOTES — il/hvac-work-licensing-2025, encoding row `legalese`

## Verification status, 2026-09-26

Run with an `l4` built from l4-ide `unstable` at `64c71638b` (macOS arm64), with
`JL4_LIBRARY_PATH` unset so the binary used its own embedded stdlib, on the deposited files
as they stand.

- `check.sh` exits 0 in both rows. All assertions are satisfied: `hvac-law.l4` 27,
  `hvac-fees.l4` 18, `hvac-tests-simplex.l4` 63, `hvac-tests-generated.l4` 343. As
  intended, `hvac-tests-simplex-red.l4` fails on exactly 3.
- Section 3's rendering check passes in both rows. That covers the `@lang` and
  `@nlg:he` annotations and the English and Hebrew `l4 nlg` output.
- The twin's section 4 cross-row comparison passes: every `Result:` block is identical
  after unmapping.
- `projections/` in both rows was regenerated from these files with the same binary.

Mechanical only. No Hebrew speaker has reviewed the Hebrew renderings. Under
`--lang he` the frame words ("is equal to", "with", "not") are still English, and dates
print as `` `YMD` with y, m and d ``. Both are l4-ide renderer limits, not encoding
defects.

---

**Status: `draft`.** Deposited 2026-09-21 on the drafts shelf. Not reviewed by anyone who knows Israeli vocational-licensing law (HG1 not sought).
An adversarial model review against the Hebrew text was run before deposit; section 5 records what it found and what was done about it.

## 1. What this is

Two instruments, one encoding row:

- **The Law.** חוק הסדרת העיסוק בעבודה במערכת קירור או מיזוג אוויר, התשפ״ה–2025, Sefer HaChukim 3349 p. 182, published 14 January 2025.
  A licensing statute: three licence grades by cooling output, a registrar, exam-and-training conditions, five-year licences, temporary licences for foreign experts, inspectors, and administrative sanctions.
  `hvac-law.l4` encodes the parts the Fees Regulations lean on: ss.2, 3, 6 (with the whole Second Schedule), 7, 8, 9, 16, 17, 63.
- **The Fees Regulations.** תקנות הסדרת העיסוק בעבודה במערכת קירור או מיזוג אוויר (אגרות), התשפ״ה–2025, Kovetz HaTakanot 5785 p. 2116, signed 6 July 2025, published 9 July, in force 16 July 2025, amended by Kovetz HaTakanot 5786 p. 2062.
  `hvac-fees.l4` encodes regs 1-5 in full. The two **enacted** texts of reg. 2 sit on L4's
  **rule-effective-time axis** — one rule, reading `RULES EFFECTIVE DATE`, with commencement
  boundaries at 16 July 2025 and 4 May 2026 — and the never-enacted SimpLEX draft sits
  beside it as an explicitly-labelled counterfactual, off the axis (sections 3 and 3.1 below).

## 2. Why: Figure 4 of *When Computers Speak Laws*

Elhanan Schwartz, Ittai Bar-Siman-Tov & Roy Gelbard, *When Computers Speak Laws: Legislative Engineering in the Age of AI*, 8 Law, Society and Culture 353 (2025), Figure 4, is a screen capture of the Israeli Ministry of Justice's SimpLEX drafting-and-testing tool.
The document being edited is the **draft** of these Fees Regulations.
On the left is a table of test scenarios, each with an expected outcome and a citation:

| # | scenario | expected outcome | cites |
| --- | --- | --- | --- |
| 5 | registration for a theoretical examination | registration approved | reg. 2(a) |
| 6 | registration for a practical examination | registration approved | reg. 2(b) |
| 7 | appeal with payment (40 NIS) | appeal under review | reg. 2(c) |
| 8 | registration for an examination without payment | registration refused | reg. 4 |

and a worked example: a candidate registered for the theoretical examination and did not pay; outcome, refused, reg. 4.

The paper's argument is that drafters should test as they draft, the way programmers do.
This row takes the paper at its word: `hvac-tests-simplex.l4` transcribes that table and runs it, and `hvac-tests-simplex-red.l4` runs the draft's expectations against the text that was actually made.

## 3. Draft, as made, as amended — and which of the three is a point in time

| item | the SimpLEX draft (Fig. 4) | as made, KT 5785 p. 2116 (16 Jul 2025) | as amended, KT 5786 p. 2062 |
| --- | --- | --- | --- |
| theoretical examination | 273 | **no fee** | 158 (new reg. 2(a1)) |
| practical examination | 194 | 194 | 194 |
| appeal, 40 NIS per appeal | theoretical **or practical** | "the examination score", in addition to the fee under (a): the **practical** one, the only examination the text as made defines | **theoretical** only, in addition to the fee under (a1): the appeal fee moved |
| licence, s.5 | 284 **on the application** ("בעד בקשה לקבלת רישיון או לחידושו") | 284 **on receipt** ("בעד קבלת רישיון או חידושו"): a refused applicant owes nothing | same as made |
| what an appellant tenders in all (appeal fee + the examination fee it is "in addition to") | **313** for either examination: 2(c) adds the 40 to "the fee under (a)", the theoretical one | 234 (practical); no theoretical appeal | 198 (theoretical); no practical appeal |
| temporary licence for a foreign expert | 398, citing **"s.8 of the Law"** | 398, citing s.9 | same |
| preamble | after consulting the Finance Minister, s.39 Budget Foundations Law | with the Finance Minister's approval, s.39B; ss.59 **and 60** | same |
| reg. 3 indexation, reg. 4 payment precondition | present | same | same |

Three consequences the encoding makes explicit:

1. Under the Regulations as made, the theoretical examination had no fee, so reg. 4 had nothing to withhold and scenario 8's candidate is admitted to it. ``#ASSERT `EVAL UNDER RULES EFFECTIVE AT` `a day under the Regulations as made` (`the service may be provided` `theoretical examination` 0)`` is satisfied.
2. The appeal fee moved. As made, reg. 2(b) attached it to "the examination score" in addition to the fee under (a), and reg. 1 defined only the practical examination, so the practical one it was. The amendment defined the theoretical examination, inserted (a1) for it, and rewrote (b) to attach the appeal fee to the theoretical score and to (a1). An earlier draft of these notes said (b) as made pointed at a non-existent (a1); that was read off Wikisource's amended text and is wrong, which is why the gazette issue is now deposited in `source/`.
3. The draft's "s.8 of the Law" for the foreign-expert licence is wrong against both the bill as tabled for second and third reading and the Act; s.8 is validity and renewal. The screenshot's worked example likewise cites "s.9 of the Law" for eligibility to sit the examination, which no section of the Act provides. Both would be caught by a check that resolves citations against the parent Act, which is the "legality check" panel SimpLEX itself shows.

### 3.1 Two of the three are vintages; one is a draft

Until 2026-09-22 all three columns above were values of a hand-rolled `DECLARE Vintage IS
ONE OF`, with a separate `DECIDE` per column. They are no longer alike, because they were
never alike:

- **The two enacted texts are points on a timeline.** There is now ONE rule for reg. 2,
  `the fee prescribed for`, which reads the nullary `DATE` builtin `RULES EFFECTIVE DATE`
  — L4's rule-effective-time axis, the "which version of the law applies" axis — and
  answers as the text in force on that day answers. Callers pin it with
  `EVAL UNDER RULES EFFECTIVE AT <date>`. Three regimes, two inclusive boundaries: nothing
  prescribed before 16 July 2025, the text as made from 16 July 2025, the text as amended
  from 4 May 2026. The first boundary is not written down as a constant — it is computed
  by reg. 5 itself, `the Regulations commence on (YMD 2025 7 9)`, so reg. 5 is load-bearing
  and the encoding would notice if its seven days were wrong.
- **The draft is not a point on any timeline.** It is encoded beside the axis, as
  `the fee the SimpLEX draft prescribes for` and companions, which take no date and read no
  axis. The axis is indexed by commencement and a draft has no commencement; there is no
  day on which "what did the law say?" could correctly return 273. Putting the draft on the
  axis would mean inventing a date it never had, and the encoding would then assert —
  silently, and falsely — that on some real day the theoretical examination cost 273
  shekels. The naming keeps the subjunctive visible at every call site: the draft *would
  have required*, *would have allowed*.

Three things follow that the enum could not express.

1. **"Before it was in force" became a real answer.** The enum had no cell for it. The axis
   does, and the honest answer there is `NOTHING` — not "no fee was payable under a rule"
   but "no such rule yet existed" — and reg. 4, having nothing to withhold, lets everyone
   through. Family (g) of the generated suite asserts this on ten sample days.
2. **The presumption against retroactivity is now the default, for free.** `RULES EFFECTIVE
   DATE` falls back to the valid-time pin and only then to today, so asking about a 2025
   fact gets the 2025 law without anyone having to say so.
3. **regs 3, 4 and 5 are genuinely encoded once.** reg. 4 is now a function of whatever fee
   is prescribed, `regulation 4 is satisfied`, and both the enacted rule and the draft's
   counterfactual feed it — which is faithful, because the draft's reg. 4 is word for word
   the reg. 4 that was made.

The demonstration is at the foot of `hvac-fees.l4`: the same question about an appellant's
total outlay, asked at 2025-07-01, 2025-07-16 and 2026-05-04, answered by one rule as
`NOTHING`, `JUST 234` and `NOTHING`, and its mirror on the theoretical examination
answering `NOTHING`, `NOTHING` and `JUST 198`.

`hvac-tests-simplex-red.l4` is **meant to fail** on exactly three of six rows (5, 7 theoretical, 8 theoretical); `check.sh` counts them and reports a wrong count as a failure. It is also the positive control: proof that this harness can go red.

## 4. Forks (interpretive choices)

- **F1, s.8 validity.** "תוקפו של רישיון יהיה לחמש שנים או עד 31 במרץ של השנה החמישית מהשנה שבה ניתן הרישיון, לפי המוקדם."
  Read as: the fifth year *from* the grant year is grant year + 5, so a licence granted 2025-09-01 expires 2030-03-31 and one granted 2025-01-15 expires 2030-01-15.
  The alternative, counting the grant year as the first, gives grant year + 4 (2029-03-31 for the September grant), under which the 31 March cap binds in every case and "five years" is wholly inoperative. The adopted reading keeps both limbs live. Stronger evidence, from the review: the Knesset bill records a rejected amendment that moved both numbers together, "five years" to "six years" and "the fifth" to "the sixth", so the drafters treated the cardinal and the ordinal as naming the same year, which is coherent only on grant + 5. Ordinary Hebrew usage of "השנה החמישית מ־X" still counts X as the first year, so the fork stays recorded.
- **F2, reg. 3 rounding.** "יעוגל לשקל החדש השלם הקרוב" says nearest and is silent at exactly one half. Half-up adopted (`FLOOR (x PLUS 0.5)`). Only matters when fee × index ratio lands on .5 exactly; the generated tests include such cases so the choice is visible.
- **F3, the draft vintage.** Transcribed from a published screenshot, not from a deposited draft. Fee amounts and the appeal wording are legible; the preamble is legible; item lettering (a)-(e) is as shown. The tazkirim.gov.il consultation page for the draft exists but is a JavaScript application that could not be fetched headlessly, so the transcription was not cross-checked against it.
- **F4, Second Schedule Part B, the Ministry of Education five-unit certificate.** Item 1 (column A: no prior training) lists the certificate in column B as one of two things that satisfy the requirement; item 5 lists the same certificate in column A and asks 50 hours of training in column B. The two rows conflict for a holder of that certificate. The encoding follows item 5, the row whose column A names the holder, so the applicant owes 50 hours; the reading under item 1(2) would owe nothing. Recorded here rather than resolved silently; a drafter would fix the table.
- **F5, the licence fee's charging event, and the appeal aggregate.** Found by all four THERMOSTAT arms (2026-09-21) and missed by this row until then. (i) The draft's reg. 2(d) charges the APPLICATION ("בעד בקשה לקבלת רישיון או לחידושו"); the text as made charges the RECEIPT ("בעד קבלת רישיון או חידושו"). Law s.59 lists application and grant as separate fee heads, so these are two services, and each text answers NOTHING on the head it does not price. (ii) Every text makes the 40 payable "in addition to" an examination fee, and the draft's 2(c) names "(a)" -- the theoretical fee -- whichever examination is appealed, so a practical-examination appellant under the draft tenders 313 on the literal reading; the purposive reading (194 + 40 = 234) is not encoded. `the total to be tendered for` (and, for the draft, `the total the SimpLEX draft would have required for`) carries the literal reading; reg. 4's "in full" is read against the service's own fee (40 for an appeal), not the aggregate, which is the reading SimpLEX's row 7 needs to come out "appeal under review" on a tender of 40.
- **F6, the commencement of the 5786 amendment.** Recorded 2026-09-22, when the two enacted
  texts were moved onto the rule-effective-time axis and the amendment's commencement stopped
  being decorative and became a boundary the answers turn on.
  The amending regulations — Kovetz HaTakanot 12383 of י״ז באייר התשפ״ו (4 May 2026),
  5786 p. 2062 — were read in full from the gazette issue itself
  (`olaw.org.il/takanot/takanot-12383.pdf`, two pages). **They contain no תחילה
  (commencement) provision at all**: two amending regulations, the signature of Yariv Levin
  dated י״א באייר התשפ״ו (28 April 2026), and three footnote citations. Wikisource's
  consolidated text carries reg. 5 of the principal Regulations and nothing else, so it does
  not answer the question either.
  Adopted: **4 May 2026, the day of publication**, under **s.17 of the Interpretation
  Ordinance [New Version]** (פקודת הפרשנות [נוסח חדש]): "תקנות בנות־פעל תחיקתי יפורסמו
  ברשומות, ותחילת תקפן ביום פרסומן, אם אין הוראה אחרת בענין זה" — legislative regulations are
  published in Reshumot and commence on the day of publication unless they provide otherwise.
  There is no other provision, so the default applies. (s.21 of the Interpretation Law,
  5741–1981 fixes the hour at 00:01 of that day; this encoding works in whole days.)
  Rejected: **11 May 2026**, on the argument that an amendment which writes text *into* the
  principal Regulations rides that instrument's own reg. 5, "seven days from publication".
  It is rejected because reg. 5 fixed the commencement of the Regulations it belongs to, an
  event completed in July 2025; the amending regulations are a separate חיקוק with their own
  commencement, and s.17 supplies it. The fork is recorded rather than buried because the
  Interpretation Ordinance is a general statute not deposited in `source/`, so the reader
  cannot check the step from the sources in this subject alone.
  `hvac-tests-simplex.l4` § "Tier 2 — the day the amendment commenced" asserts 3, 4 and
  11 May explicitly: those are the assertions that go red if F6 is ever resolved the other
  way, and `source/gen-tests.py` recomputes the date rather than copying it, so the
  independent Python reading would have to be changed too.
- **s.6(a)(4)(b), the registry limb.** The chapeau subjects all three limbs to the Second Schedule ("והכול בהתאם לתנאים שבתוספת השנייה"), so registry membership is encoded as a column A entry and not as a free-standing route: a registered technician reaches Grade 2 through Part B item 2 (with the completion course) or item 6 (50 hours without it), a registered practical engineer reaches Grade 3 through Part C items 2 and 7, and Part A has no registry row at all.
- **s.6(a)(3)** (unfit by reason of a conviction "in the registrar's opinion") and **s.9(a)(3)** (recognised by the registrar as of repute) are discretionary; both are inputs, not decided.
- **s.3(b)** exemptions by ministerial order are an input; no order has been located.

## 5. Review findings

An adversarial review against the Hebrew text (model review, 2026-09-21, before deposit) found seven fidelity defects and one point on fork F1. All seven were fixed in the same session; the state of the tree is post-fix.

| # | finding | severity | what changed |
| --- | --- | --- | --- |
| 1 | s.6(a)(4)(b) encoded as a free-standing route, so a registered technician was granted Grade 3; the chapeau subjects every limb to the Second Schedule, whose Part C admits only a practical engineer and whose Part A has no registry row | wrong answer | registry membership became two `Prior qualification` entries routed through the Schedule; the free-standing field was removed |
| 2 | Part B item 2 and Part C item 2 require registration **and** completion of a study programme with the completion course; a registrant without it falls under Part B item 6 / Part C item 7 (50 hours), neither of which was encoded | wrong answer | compound constructors added for item 2; plain registration now maps to items 6 and 7 |
| 3 | Part B: the five-unit certificate returned "no further requirements" citing items 1(2) and 5(3); item 5(3) asks 50 hours | wrong answer, and a genuine conflict in the Schedule | follows item 5; recorded as fork F4 |
| 4 | s.3 encoded on cooling output alone while s.3(a) is about works listed in the First Schedule; the rule's name promised more than it answered | narrower question than named | renamed `the licence grade reaches the system`, with the limit stated in its comment |
| 5 | one prior qualification per applicant; an applicant holding two could not be represented and no best-route search happened | missing case | `prior qualifications` is a list; any open row satisfies s.6(a)(4) |
| 6 | s.17(a) counted hours only; the field-of-the-licence limb and "met the requirements of those courses" were dropped, and s.17(d) (the duty is a licence condition) was absent | missing limbs | two inputs added; s.17(d) noted in the comment |
| 7 | s.17(c) tested only "at most three months", satisfied by zero and by negative months, and dropped its preconditions (duty unmet, council consulted, special and justified circumstances) | missing limbs | four conditions added |
| 8 | fork F1 (s.8): ordinary Hebrew usage of "השנה החמישית מ־X" counts X as the first year, which favours grant + 4; the reviewer's own arithmetic favours the adopted grant + 5 | open | recorded under F1; unchanged |

The reviewer also confirmed, from Kovetz HaTakanot 11951 and 12383 fetched independently, the as-made appeal-fee correction in the previous commit, and had no other finding on the fees module.

### 5.1 Hebrew heralds, smaller drops, and what to add next

Thirteen Hebrew heralds were re-voiced on the reviewer's proposals: the ungrammatical `למי ש%prior%` became `לבעלי %prior%`; "רישיון %grade%" became "רישיון בדרגה %grade%" to match the defined term; the s.6(a)(3) herald now uses the statute's own words instead of a double negative; s.17(a), s.17(c), s.8 renewal and the Chapter F heading quote the Act; reg. 3's herald restores "המדד החדש" and "השקל החדש"; reg. 4's uses "מבקש הרישיון או השירות" and "שקלים חדשים"; the vintage heralds use "כנוסחן עם התקנתן" / "כנוסחן לאחר תיקון". One herald said the wrong thing: s.63(a)(2) is about a refrigerant "not one listed in the Fourth Schedule", not "non-flammable", and the rule was renamed to match. The s.8 heralds still differ on purpose: the English commits to the F1 reading, the Hebrew quotes the statute's ambiguous words.

Smaller drops, fixed or noted: s.9 now requires an applicant "from a foreign country" and similar systems to those invited for; s.7(a)'s narrowing to paragraphs (1)-(7) of reg. 7 of the Electricity (Licences) Regulations, s.16's "in the manner the registrar directs", s.63(a)(1)'s "provided its use is permitted under any law" and reg. 3(b)'s publication duty are stated in comments and not modelled. The "(adjusted to 2025/2026)" tags are Wikisource's editorial annotations and appear in neither gazette issue; the fees module no longer attributes one to the regulation. The amendment is Kovetz HaTakanot 12383 of 4 May 2026, signed 28 April 2026 by Yariv Levin.

Verified correct by the reviewer, so they need not be re-litigated: "עד" is inclusive at 18 and 70 (s.9(a)(1)'s "מעל 70" is the exact complement); the three sunset rows and only those; every hours figure in Parts A and C; reg. 3 as fee × new ÷ base; reg. 4's no-fee branch; reg. 5's seven days.

What a knowledge engineer would add next, in the reviewer's order: a `Work` type from the First Schedule so s.3 answers about an action and not only a size; a best-route choice among a list of prior qualifications (the list is now there; the choice is "any", which is what s.6(a)(4) needs); s.17(d) wired to s.8 renewal and s.10(a) refusal; a total-payable rule for reg. 4 that adds the 40 to the (a1) fee; and reg. 3 chained across successive update days.

## 6. Multilingual design

The module body is English (`@lang en`), because English is the working language of the people this was built for tomorrow; every rule carries an English `@nlg` herald and a Hebrew `@nlg:he` herald.
`l4 nlg --lang he` and `l4 render --lang he --format html` therefore produce a Hebrew document from the same source; the four renderings are in `projections/`.

Two limits of the current tooling, observed on the l4-ide `unstable` binary of 2026-09-19:

- `%name%` placeholders in a herald were rendered by `l4 nlg` as the bare parameter name followed by "with <arguments>", not substituted inline, on the 2026-09-19 binary; the heralds here were written to read acceptably either way. l4-ide PR #458 (2026-09-23) splices the call's arguments into the slots in `l4 nlg` too, in every language, and appends any argument a herald does not mention. The projections in `projections/` predate it; regenerate with a binary at or after that PR to see the difference.
- `§` section titles are not language-tagged, so the Hebrew rendering of THIS row carries English headings. The Hebrew-canonical twin row `encodings/legalese-he/` fixes that: it is generated from this row by `source/revoice.py` through a 173-entry name map (`encodings/legalese-he/glossary.json`, 125 entries in the instruments' own words), with Hebrew identifiers, headings and default heralds and English under `--lang en`; its `check.sh` runs the same five modules and compares every `Result:` block with this row's after unmapping the names, with a positive control. Regenerate with `python3 source/revoice.py`; edit this row, never the twin.
- An `IMPORT` of a Hebrew-named module resolves to nothing, silently: no import diagnostic, only `could not find a definition` for each imported name. The twin therefore uses Latin basenames with a `-he` suffix; see its NOTES.md for the probes.

## 7. What is not here

- Chapter F (administrative enforcement) and the Third Schedule (sanction amounts): out of scope by decision.
- The First Schedule (which works each grade may do) and the Fourth Schedule (flammable refrigerants): the grade thresholds are encoded, the work lists are not. That is why the s.3 rule is named `the licence grade reaches the system` and not "may perform the work": it answers the cooling-output half of s.3(a) only.
- ss.10-15 (refusal, cancellation, suspension; registry; non-transfer; standards; presenting the licence; reporting) and s.18 (operators).
- The **valid-time** and **system-time** axes are not used. The rule-effective-time axis is
  (since 2026-09-22), for the two enacted texts; the SimpLEX draft is deliberately off it,
  for the reason in section 3.1. No `EVAL UNDER VALID TIME`, no ledger of facts with a
  history, no `EVAL AS OF SYSTEM TIME` audit snapshots.
- No `cases/`, `report/` or `gates/`; no fork register file beyond section 4 here.
- Goldens: none. The modules are outside l4-ide's corpus globs; `check.sh` is the guard, and it is not run by any CI.

## 8. How to run

```
HVAC_L4=/path/to/l4 sh check.sh     # the binary's OWN embedded stdlib -- the usual case
HVAC_L4=/path/to/l4 HVAC_LIBS=/path/to/jl4-core/libraries sh check.sh   # a worktree build
sh check.sh                         # the worktree named inside it (a macOS path)
sh ../legalese-he/check.sh          # the twin; its section 4 compares the two rows
l4 nlg hvac-fees.l4                 # English
l4 nlg --lang he hvac-fees.l4       # Hebrew
l4 render --lang he --format html hvac-law.l4 > projections/hvac-law.he.html
python3 ../../source/gen-tests.py   # regenerates hvac-tests-generated.l4
python3 ../../source/revoice.py     # regenerates the whole Hebrew twin
```

With neither `HVAC_LIBS` nor `HVAC_L4_WORKTREE` set, `check.sh` now leaves
`JL4_LIBRARY_PATH` **unset**, so the binary uses its own embedded standard library. That is
what you want unless you are running a binary you built yourself: an `l4` pointed at a
prelude newer than itself reports no version mismatch, it fails as a cascade of
`could not find a definition`.

A prebuilt linux-x64 `l4` can be had from `legalese/prereleases`; the current release tag
and its sha256 travel inside `legalese/l4-plugin`'s `scripts/install-l4.sh`, which is the
supported way to fetch and verify one.

The binary must be at or after l4-ide `unstable` PR #432 (2026-09-19) for `@lang`,
`@nlg:he` and `--lang`. **Before that, the modules do not even lex** — see the verification
banner at the top of this file for what could and could not be checked here.
