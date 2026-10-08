# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-08`

The National Insurance Law half of row IL-08, the extension of the Israel tier: Schedule A1 Part D, s 72 and s 335, and the dispositions of ss 65 and 67A, taken in the order row IL-07's `GAPS.md` needs them.
One agent, one session, no sub-agents (run `IL-08-20261007`, encoder `enc-il-08`, 2026-10-07).
Status: **draft**.
No domain expert has read it; HG1 has not been sought; no independent test pass has been run.

The Income Tax Ordinance half, whose `NOTES.md` carries the parts common to both (the binary, the semi-cleanroom record, what was read), is `../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-08/`.

## 0. What `check.sh` prints

Run from 2026-10-07T00:22:32Z to 00:22:41Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset, with the binary the other half records (`jl4-0.1-ff13a0ea`, sha256 `f6501568…dbfa8bc`).
No module changed during the run.

```
module                                    errors satisfied  failed  refused  expected
nii-il08-nouns.l4                              0         0       0        0         0
nii-il08-tests-part-d.l4                       0        37       0        0         0
nii-il08-tests-s72-s335.l4                     0        22       0        0         0
nii-s335-branches.l4                           0         0       0        0         0
nii-s72-period-of-allowance.l4                 0         0       0        0         0
nii-schedule-a1-part-d.l4                      0         0       0        0         0
TOTAL (6 modules)                              0        59       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` exit 0.
59 assertions, all satisfied; 2 of them are `#ASSERT REFUSED … BECAUSE "…"`.
No assertion is expected to fail; there is no expected-red module.
The two Warnings about differing copies of `prelude` and `daydate` under `~/.local/share/jl4/libraries/` are printed as for every row.

That the harness can fail: a scratch copy of these six modules with one expected value altered (a woman born in January 1930 asserted at 781 months), one `#ASSERT REFUSED` pointed at an expression that answers, and one plain `#ASSERT` on an expression that refuses (s 335 for 2025) printed `2 failed, 1 refused`, exit 1.

Every assertion was satisfied on the first run that evaluated it; before that, the tests modules failed to compile once (a one-argument mixfix name ending in a keyword), which a rename fixed, no expected value changing.
`python3 -I tools/srcquote.py SOURCE *.l4` regenerates every `-- src:N |` line; `python3 -I tools/hebcheck.py SOURCE *.l4 *.md` finds every other run of Hebrew verbatim in the source (exit 0).

## 1. What is encoded, and what is not

| module | lines | holds |
| --- | ---: | --- |
| `nii-il08-nouns.l4` | 93 | the nine branches (as rows IL-04 and IL-05 spell them), the person for s 335, the entitlement for s 72; `DECLARE` only |
| `nii-schedule-a1-part-d.l4` | 96 | Part D: a woman's age by month of birth, in months, and the day she reaches it |
| `nii-s72-period-of-allowance.l4` | 90 | s 72(a)-(c): whether the child allowance is paid for a month |
| `nii-s335-branches.l4` | 131 | s 335(a)-(j): the branches in which a person pays |
| `nii-il08-tests-part-d.l4` | 74 | 37 assertions: every band of Part D at both its edges |
| `nii-il08-tests-s72-s335.l4` | 85 | 22 assertions |

Not encoded: s 65 (encoded in full by row IL-06), s 67A (no such section), the other Parts of Schedule A1, and the statuses s 335 reads (each another Chapter's answer).

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.
"GAPS" is the item of row IL-07's `GAPS.md` the provision discharges.
**Totals: 17 encoded, 1 inert, 8 out-of-scope, 0 deferred** (26 rows, counted by script; "out-of-scope" includes the statuses taken as inputs).

| provision | lines | gist | disposition | where | GAPS |
| --- | --- | --- | --- | --- | --- |
| Schedule A1, Part D, heading and note | 4431-4433 | "the age of entitlement to a senior citizen pension for women by month of birth"; used by ss 245(a), 342(c), 351(b), 406(a)(4)(a) | encoded | `nii-schedule-a1-part-d.l4` | 10 |
| Schedule A1, Part D, the table | 4437-4453 | sixteen bands, 65 to 70 years | encoded | `Schedule A1, Part D — the age in months fixed for a woman born in month` | 10 |
| Schedule A1, Parts A, B, C, E | 4367-4430, 4456-4477 | retirement age, unemployment age, Chapter 11 age, women exempt from a qualifying period | out-of-scope | Not in the ruled scope (only Part D is), and no rule of this row reads them. Observation, not checked further: Part A's table for women (lines 4385-4397) ends at "מאי 1947 עד דצמבר 1955" (line 4396), with no row for a woman born later, where the other tables end with an open row ("ואילך"). | — |
| s 65(a) "מבוטח" (1), (2) | 801-803 | insured for Chapter 4 | out-of-scope | Encoded in full by row IL-06 (its coverage rows for s 65(a) and (b)); not re-encoded, so that one provision has one encoding. s 335(b) reads "insured as defined in s 65(a)(1)" from the two status fields IL-06 uses (`insured under Chapter 11`, `a housewife as defined in section 238`). "יושב בישראל", the residence (2) turns on, is not defined in the Law: a search on 2026-10-07 for a definition of "תושב ישראל" or "יושב בישראל" in it found none, so residence remains a status. | 13 |
| s 65(a) "ילד", s 65(b) | 804-809 | the child, abroad for three months | out-of-scope | Encoded in full by row IL-06. | — |
| s 67A | — | — | inert | There is no s 67A in the deposited consolidation. "67א" occurs only in the table of old and new section numbers (line 5326), mapping the 1968 consolidation's s 67A to the present s 108, which is repealed ("(בוטל)", lines 1162-1163). Row IL-07's GAPS.md records the same. | — |
| s 72(a), first limb | 854 | entitlement arising by the 15th: paid from the 1st of that month; after: from the next | encoded | `s 72(a) — the first month …`; fork N1 | 6 |
| s 72(a), last limb | 854 | payment ends on the last day of the month entitlement ceased | encoded | `s 72(a), (c) — the last month …` | 6 |
| s 72(b) | 855 | only for a child who lived seven days or left the hospital | encoded | `s 72 — the allowance is paid for month` | 6 |
| s 72(c) | 856 | three months on after the month a child for whom it was paid died | encoded | `s 72(a), (c) — the last month …`; fork N2 | 6 |
| s 72, the period answered | 853 | no amendment tag | encoded (a gate from May 2015, row IL-06's period) | `this row answers months of the child allowance from May 2015 …` | 6 |
| s 335 heading | 3610 | last tag תשע״ח־5 | encoded (a gate from January 2026, rows IL-04 and IL-05's period) | `this row answers section 335 for contribution periods from January 2026` | 9 |
| s 335(a) | 3611 | a worker who is not a resident: maternity | encoded | `s 335(a) — …` | 9 |
| s 335(b) | 3612 | insured as in s 65(a)(1): children | encoded | `s 335(b) — …` | 9 |
| s 335(c), (d) | 3613-3614 | Chapters 5 and 6: work injury, accident injury | encoded | `s 335(c) — …`, `s 335(d) — …` | 9 |
| s 335(e) | 3615 | s 158(1), not a controlling shareholder: unemployment | encoded | `s 335(e) — …` | 9 |
| s 335(f) | 3616 | an employee under Chapter 8, not a controlling shareholder: insolvency | encoded | `s 335(f) — …` | 9 |
| s 335(g), (h) | 3617-3618 | Chapter 9; long-term care | encoded | `s 335(g) — …`, `s 335(h) — …` | 9 |
| s 335(i) | 3619 | Chapter 11, not a housewife or widow pensioner: senior citizens and survivors, and maternity | encoded | `s 335(i) — …`; fork N3 | 9 |
| s 335(j) | 3620 | none detracts from another | encoded | `s 335 — contributions are payable in the branch` (any subsection imposing it) | 9 |
| s 335, the list | 3610-3620 | the branches, in Schedule J's order | encoded | `s 335 — the branches for which contributions are payable, for` | 9 |
| s 238 "עקרת בית", "אלמנה בת קצבה" | 2401 ff. | housewife, widow pensioner (Chapter 11) | out-of-scope (inputs) | Statuses the Institute records under Chapter 11; outside the ruled scope. | 9 |
| s 158 "מבוטח" (1) | — | unemployment insurance | out-of-scope (input) | Chapter 7's definition; outside the ruled scope. | 9 |
| Chapters 5, 6, 8, 9, 11; long-term care | — | who is insured in each branch | out-of-scope (inputs) | Each is its Chapter's own regime; s 335 only maps the statuses to branches. | 9 |
| s 1 "בעל שליטה", "חברת מעטים" | 122, 139 | controlling shareholder, closely-held company | out-of-scope (input) | Row IL-04 lists them as out-of-scope statuses; one input here. | 9 |
| ss 66-68 | 813-834 | the child allowance itself | out-of-scope | Row IL-06. s 72 says which months are paid; how much, and in whose count, is IL-06's. | 6 |

## 3. Assumptions

**A1 — Part D is stated as the deposited text prints it.** No rule takes a date: the table maps a month of birth to an age, its last row is open ("ואילך"), and its tags (תשע״ז־12 on the heading, תש״ף on the Part) predate every period the consuming rows answer.

**A2 — s 72 answers months from May 2015.** s 72 carries no amendment tag, so its text is not dated by any amendment; the row answers the period row IL-06 answers (its A1), with which it composes, and declines an earlier month by name.

**A3 — s 335 answers contribution periods from January 2026.** Its last tag, תשע״ח־5, is by counting the file's list of amending Laws (line 7) the Insolvency and Economic Rehabilitation Law 5778-2018; what that Law changed in s 335, and when it commenced, were not checked. The row answers the period rows IL-04 and IL-05 answer (their A1) and declines an earlier year.

**A4 — the statuses are inputs.** Every fact s 335 reads is another Chapter's answer; every fact s 72 reads (the day entitlement arose or ceased, a death, the seventh day) is the Institute's record.

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| N1 | s 72(a) | "עד 15 בחודש": by the 15th inclusive, or before it? | inclusive; exclusive | **inclusive**: the next limb says "אחרי 15", after the 15th, so the 15th itself falls in the first. Tests on the 15th and the 16th. |
| N2 | s 72(a), (c) | A child for whom no allowance had been paid dies: does (c)'s three months apply? | no; yes | **no**: (c) is about "ילד שבעדו שולמה קצבת ילדים"; (a) then ends payment with the month of death. |
| N3 | s 335(a), (i) | Maternity is imposed by (a) and by (i): one branch or two? | one | **one** (row IL-04's F15): (j) says the subsections do not detract from each other, and Schedule J's two maternity items never both print a figure in one column. |
| N4 | Schedule A1 Part D | The day a woman "reaches" the age, for a 29-31 day of birth and a shorter month | the last day of the shorter month; the first of the next | **the last day** (`add months` clamps), row IL-05's fork F19, so the two rows agree. |

Places read for a fork and none found: Part D's bands (contiguous and disjoint; each tested at both edges); s 335(b)'s cross-reference to s 65(a)(1), which IL-06 encodes as the same two statuses.

## 5. Answer tables

### Schedule A1 Part D

| born | age | in months |
| --- | --- | ---: |
| to June 1939 | 65 | 780 |
| July and August 1939 | 65 and 4 months | 784 |
| September 1939 to April 1940 | 65 and 8 months | 788 |
| May to December 1940 | 66 | 792 |
| January to August 1941 | 66 and 4 months | 796 |
| September 1941 to April 1942 | 66 and 8 months | 800 |
| May 1942 to December 1944 | 67 | 804 |
| January to August 1945 | 67 and 4 months | 808 |
| September 1945 to April 1946 | 67 and 8 months | 812 |
| May to December 1946 | 68 | 816 |
| January to August 1947 | 68 and 4 months | 820 |
| September 1947 to April 1948 | 68 and 8 months | 824 |
| May to December 1948 | 69 | 828 |
| January to August 1949 | 69 and 4 months | 832 |
| September 1949 to April 1950 | 69 and 8 months | 836 |
| May 1950 and after | 70 | 840 |

### s 72

| event | first month paid | last month paid |
| --- | --- | --- |
| born on the 1st-15th of a month | that month | — |
| born on the 16th or later | the next month | — |
| turns 18 (entitlement ceases on the birthday) | — | the month of the 18th birthday |
| entitlement ceases otherwise | — | that month |
| dies, an allowance having been paid | — | the third month after the month of death |
| lived fewer than seven days and never left the hospital | never paid | — |

### s 335

| person | branches |
| --- | --- |
| a resident employee insured in every Chapter | all nine |
| a controlling shareholder in a closely-held company, otherwise the same | all but unemployment and insolvency |
| a non-resident employee insured for work injury only | maternity, work injury |
| a housewife (Chapter 11), insured in Chapters 6, 9 and long-term care | accident injury, disability, long-term care |
| a widow pensioner (Chapter 11), the same | children, accident injury, disability, long-term care |

## 6. What these rows imply for the capstone's adapters

- **GAPS 10, Part D.** The input "the earner's age fixed by Part D … in months, if a woman" becomes `Schedule A1, Part D — the age in months fixed for a woman born on` her date of birth, the unit row IL-05's `The insured person, for the age limb of section 342(c)(2)` takes. H19 can be answered: a woman born in 1980 has 840.
- **GAPS 6, s 72.** Fork K6 (ask row IL-06 about the first day of the month, declining a month with a birth or an 18th birthday after it) can give way to: for each child, whether `s 72 — the allowance is paid for month` M; then ask IL-06 about the family of the children paid for. Under s 72 the month of an 18th birthday is paid in full, and a child born after the 15th starts the next month. Which day of the month to put to IL-06 for the count and the amounts is still the adapter's choice; s 72 does not say.
- **GAPS 9, s 335.** The input convention "an employee pays in all nine branches" can give way to `s 335 — the branches for which contributions are payable, for`, which returns that list for a resident employee insured in every Chapter, and a shorter one for a controlling shareholder, a non-resident or a housewife. The statuses remain inputs.
- **GAPS 13, NII s 65.** Nothing new: IL-06 already encodes it, and residence ("יושב בישראל") remains an undefined status.

## 7. Nouns to reconcile

- **`A branch of insurance`** is declared here constructor for constructor as in rows IL-04 and IL-05 (row IL-07's RECONCILE.md N1). A module that imports two of the three and names a constructor in a bare `LIST` meets the "multiple definitions" error IL-07 measured; one shared nouns module for the subject would end it.
- **The person.** IL-06 `A person` (with `insured under Chapter 11`, `a housewife as defined in section 238`, which this row's `A person in a contribution period, for section 335` spells the same); IL-04 `A person who works`; IL-05 `An insured person, for section 342(a)-(b)`. s 335 reads statuses from all of them.
- **The branch list.** IL-04's and IL-05's input `branches for which contributions are payable under section 335` is this row's output.
- **The Part D age.** IL-05's `a woman` constructor carries `the age fixed for her by her month of birth in Part D of Schedule A1, in months`; this row computes it from a date of birth.
- **The child and the month.** IL-06's `A child` (date of birth) and `A family on a day`; this row's `An entitlement to the child allowance for a child, for section 72` (the day it arose and how it ended). A child's 18th birthday in IL-06 is the day its entitlement ceases here.
- **Month counts.** Two helpers (`the month count of`, `s 72 — the month count of`) do what row IL-08's ITO half calls `the serial number of month`; one shared date module would serve all three.

## 8. Sources

The deposited Law, at the lines cited; its table of old and new section numbers (lines 5247-5458); the three enacted amending Laws deposited under `../../registers/source-bundle/amending-laws/`, searched only to see whether they touch this half (`BRIEF.md`).
Nothing was fetched for this half.
No officially published table of Part D was fetched to cross-check the tests; the expected values are the printed table, row by row.

## 9. Open questions for a domain expert

1. N1: does the Institute pay a child born on the 15th for that month?
2. N2: is the allowance continued three months after the death of a child for whom no payment had yet been made?
3. Part A's table for women ends at December 1955 in the consolidation: is a row missing (the 2021-2022 changes to women's retirement age), or does Part A not apply to later births? Not in this row's scope; noted for whoever encodes Part A.
4. A3: from when does the present text of s 335 apply?

## 10. What was not done

- **No independent test pass**, **HG1 not sought**, **not committed**: as for the other half.
- **No official cross-check of Part D**: the Institute publishes the women's ages by month of birth; a fetched copy would make a second oracle for the 37 assertions.

## Comparison with Axiom's RuleSpec (2026-10-07)

Written by the comparison author for row IL-08 (`lad-il-08`), one session, no sub-agents, on 2026-10-07, after both halves of the row and both independent passes had been deposited, as the semi-cleanroom ruling of 2026-10-06 requires.
This section covers the National Insurance half only; the Income Tax Ordinance half's `NOTES.md` carries its own, including fork F19 (s 40(a)'s pointer to the old s 109 and the repealed Schedule D).
Nothing else in this row, and nothing in the commons, was edited; nothing was repaired.
A divergence below is a finding, not a fix.

### What was read

**Axiom.** A local clone of the Axiom Foundation's `rulespec-il`, read-only, at commit `95c6f32c87c75e318631cbd77c14b840bc536c15` (the merge of its PR #8, 2026-10-03, "encode/il-nii-contributions"); nothing was pulled.
Read: `NOTICE`; the heads of `LICENSE` and `LICENSE-CODE`; `data/coverage/tax-benefit-source-map.json` (whole); `docs/ENCODING-GAPS.md` (lines 140-714, and its headings above); `docs/encoding-charter.md` lines 40-55; `known-missing-money-atoms.yaml` and `known-validation-gaps.yaml` (whole; neither has any entry); `README.md` by search; `il/statutes/national-insurance-law-1995/section-337.yaml`, `section-342.yaml` and `section-348.yaml` (whole) with their `.test.yaml` files; `schedule-j/sign-1.yaml` (its rule list, lines 1-125 and its total-rate rules); the composed pipeline (lines 1-535, and the child facts and outputs of all 15 cases).
No Axiom module exists for Part D, s 72 or s 335 (`ls il/statutes/national-insurance-law-1995/`: ss 1, 66, 67, 68, 334, 337, 342, 348, Schedules J and K), so there was no module or companion test file of theirs for them.
Nothing of any other Axiom repository was read, and nothing under `l4-ide/specs/research/AXIOM-*`.

**Ours.** This row's `BRIEF.md`, `NOTES.md`, `encoding.json`, the four rule and noun modules, `INDEPENDENT-FINDINGS.md`, `DECIDED-ANSWERS.md` and `tests-independent.l4`, in full; row IL-07's `GAPS.md`.
The deposited Law at the lines cited below (sha256 `78bf47ee…552a97`, checked).

**Licence.** `NOTICE` puts Axiom's encodings, companion test cases, parameter values and provenance metadata under CC BY 4.0 (`LICENSE`) and its tooling under Apache 2.0 (`LICENSE-CODE`); confirmed from the three files.
Axiom material appears here only as short attributed snippets: Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation.

**Runs.** Axiom's stated conventions and figures for these provisions were put through a scratch copy of this directory (the session scratchpad, `lad-il-08/nii/zz-axiom-cases.l4`) with `/Users/mengwong/.local/bin/l4 run`, `JL4_LIBRARY_PATH` unset, at 2026-10-07T06:01:08Z, under the binary the other half's section records (sha256 `6015a4c3…3b54a6`, not the build section 0 used).
14 assertions, 14 satisfied, 0 errors (a first run failed to compile on `length`, which this binary's prelude does not define; the two assertions were rewritten with list equality, and no expected value changed).

### Coverage: what Axiom did with each provision of this half

Axiom's inventory, `tax-benefit-source-map.json`, lists this Law's encoded sections as ss 1, 66, 67, 68, 334, 337, 342 and 348, with Schedules J and K (lines 88-109).

| provision (ours) | source lines | ours | Axiom | Axiom file, status |
| --- | --- | --- | --- | --- |
| Schedule A1, Part D | 4431-4453 | encoded: the age in months by month of birth, and the day it is reached | **left out**, named, with a reason: "Three encoder attempts were blocked by the numeric-grounding check"; its absence is one of the reasons they give for deferring the employee deduction of s 342(c)(1) and the women's limb of s 342(c)(2) | source map line 125; `ENCODING-GAPS.md` lines 651-664; `section-342.yaml` lines 24-42; `README.md` line 53 |
| s 72 | 853-856 | encoded: whether the allowance is paid for a month | **left out**, not named anywhere; the composition counts a child for "the allowance month" from two per-case inputs, `child_N_age_at_month_years` (below 18) and `child_N_is_present_in_israel` | composed pipeline lines 72-81, 148-170; `ENCODING-GAPS.md` lines 564-566 |
| s 335 | 3610-3620 | encoded: the branches in which contributions are payable | **left out**, "deliberately out of scope"; **an input** to their s 348 (`contributions_payable_under_section_335`, one Boolean); their s 337 applies Schedule J's printed employee totals, so implicitly all nine branches | `encoding-charter.md` lines 51-52; `section-348.yaml` line 69; `section-337.yaml` lines 74-80; `ENCODING-GAPS.md` line 612 |
| s 65 | 799-809 | not re-encoded here (row IL-06 encodes it) | **applied without a module**: the age-and-presence proviso of s 65(a), per child, inside the composition; the maintained-child limb and s 65(b) not modelled | source map lines 119, 127-133; `ENCODING-GAPS.md` lines 543-568 |
| s 67A | — | inert: no such section | no s 67A either; the identifiers `nii-section-67a-*` are s 67(a) (see below) | `ENCODING-GAPS.md` lines 482-502; `README.md` line 49 |

**Counts**, over the three provisions this half encodes: encoded by Axiom as a module, **0**; handled as an input, **1** (s 335, as one Boolean in s 348); left out, **3** (Part D with a stated reason; s 72 unmentioned; s 335 by its charter).
The one stated reason, for Part D, is a limit of their encoder, not a reading of the text.

### Where Axiom applies one of our provisions

Nowhere: it applies none of Part D, s 72 or s 335.
Three things Axiom states about them were put through our rules instead.

**Part D.** `ENCODING-GAPS.md` (lines 652-654) gives the table's range as "65 for the oldest cohorts, rising to 70 for every woman born in May 1950 or later" and quotes the row for September 1939 to April 1940.
Ours: born June 1939, 780 months; May 1950, 840; January 1990, 840; September 1939 and April 1940, 788 (5 assertions, satisfied).
They agree.
Axiom's stated obstacle, that "a month number taken as input is a literal the text does not print", does not arise in ours: the rule takes a date of birth, and the band edges are typed from the rows (lines 4438-4453) and tested edge by edge, here and by the independent pass.

**s 72.** The composition's summary (lines 72-81) says a child who turns 18 later in the year "still counts for the allowance in the months before the birthday and stops counting after it"; its gap entry (lines 564-566) says the age "is one number for the case, so a child that turns 18 mid-year changes state at the start of the modelled month rather than on its birthday".
Ours, for a child born 20 July 2008 whose entitlement ceases on 20 July 2026: paid for June and July 2026, not August (s 72(a), last limb, line 854).
For a child born 20 March 2026: not paid for March, paid from April (s 72(a), second limb).
5 assertions, satisfied.

**s 335.** Their s 337 charges an employee Schedule J's printed totals, which cover all nine branch rows (items 1 and 3-10).
Ours, for a resident employee insured in every Chapter s 335 reads: all nine branches; for the same person as a controlling shareholder in a closely-held company: seven, without unemployment and insolvency (s 335(e), (f), lines 3615-3616).
4 assertions, satisfied.

### Axiom's cases put through our encoding

| Axiom case(s) (file, line) | what the case takes from our provisions | put through ours | result |
| --- | --- | --- | --- |
| `section-337.test.yaml` 1, 12: an employee's contributions on 15,000 and 5,000 for January 2026 | s 335 implicitly: the Schedule J totals, all nine branches | s 335 for a resident employee insured in every Chapter | **consistent**: nine branches; the case does not state the person's statuses, and the rates are outside this row |
| `section-348.test.yaml` 1, 14, 27, 40 | s 335 as one Boolean (`true` three times, `false` once) | — | **could not be run**: the case supplies s 335's conclusion, not the statuses our rule reads |
| `section-342.test.yaml`, all 5 | s 342(a) and (d) only | — | not applicable: none reaches Part D |
| composed pipeline, all 15 | the monthly child count, which s 72 governs at a birth and at 18 | — | **could not be run**: no case gives a date of birth, and each case's period is the whole of 2026 (2026-01-01 to 2026-12-31) |

### Divergences and differences

| id | provision | ours | Axiom | source lines | classification | repair if ours is wrong |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | Part D | encoded | not encoded (encoder failure); its figures as stated agree with ours | 4431-4453 | scope difference | — |
| B2 | s 342(c)(2), the consumer of Part D | not ours; NOTES section 6 offers Part D to the composer of s 342(c)(2) without remark | names "the operative qualification in section 245(b2)" as a second missing dependency beside Part D | s 342(c)(2) line 3662 makes the women's age "subject to s 245(b2)"; s 245(b2) reads "(בוטל)", line 2474 | **theirs wrong** in a stated reason, on the deposited text: the qualification is repealed, so there is nothing to supply (not checked against their corpus expression of 2026-06-15, though every amendment tag on s 245, line 2464, is older than that) | — (a note for whoever composes Part D with s 342(c)(2): the cross-reference points at a repealed subsection) |
| B3 | s 72 | encoded | not encoded; per-month age and presence supplied by the caller; no 15th-day rule, no seven-day rule, no three months after a death | 853-856 | scope difference; the convention their gap entry states (the state changes at the start of the month of the 18th birthday) would lose the month s 72(a) pays, and nothing in their pipeline declines the month of a birth after the 15th | — |
| B4 | s 335 | encoded: the branch list | not encoded; s 337 charges every employee the full employee total, with no input through which s 335's exclusions reach the rate | 3611, 3615-3616 | scope difference, silent on their side: a controlling shareholder in a closely-held company (no unemployment, no insolvency) or a non-resident worker (s 335(a): maternity, with work injury and insolvency if insured under Chapters 5 and 8) is charged the full employee total, including branches s 335 does not impose on them | — |
| B5 | Schedule J's branch rows against its totals | not ours | recorded as `unexplained` (`ENCODING-GAPS.md` lines 598-617) | checked here on the deposited text: in the 2025-2026 table the employee column above the reduced bracket sums over its nine rows (lines 4720, 4722-4729) to 14.39 against the printed 14.50 (line 4730), and to 14.49 against 14.60 at the 2024-2027 work-injury rate | not a divergence in s 335; a caution for composition: a rate built by summing the rows of our branch list will not reproduce the printed total even for a full employee | — |
| B6 | s 67A | no such section | none either | 817; 5326; 1162-1163 | agreement | — |
| B7 | s 65 | row IL-06's | applied in the composition without a module | 799-809 | scope difference (row IL-06's comparison, not this one) | — |

No divergence shows a rule of this half wrong on the text.

### Our independent pass's findings, and Axiom

| finding (`INDEPENDENT-FINDINGS.md`) | Axiom |
| --- | --- |
| 1-2, 72-57: s 72(c) for a child whose payment window was empty (fork N2) | nothing: s 72 not encoded |
| 3-5, D-46 to D-48: the day a woman reaches the Part D age when the day does not exist (fork N4) | nothing: Part D not encoded, and their man's age under s 342(c)(2) is a parameter (70), with no day computed |
| 6-7, 72-14 and 72-30: the May 2015 gate (A2) | nothing to compare |
| silent paths (the unchecked "was paid" input, the moved day, the gate only on the export) | nothing to compare |
| 72-39, 72-42, 72-44: a 29 February birthday, how seven days are counted, a home birth | nothing: their composition leaves the 18th birthday to the caller as ours does, and has no seven-day rule |
| 335-R1, the rate of contributions; 335-R4, who pays | **Axiom encodes both**: the rates in s 337 and Schedule J, the self-payer judgment of s 342(a) and the multiple-employer rules of s 342(d) |
| D-R1, a man's age under Part D | Axiom carries the man's age of s 342(c)(2), 70, as a parameter (`section-342.yaml` lines 89-104; line 3662); Part D is for women only, as both the tester and our rule names say |

### Our forks, and the s 67A observation

N1, N2 and N4 have no Axiom counterpart.
N3 (one maternity branch from s 335(a) and (i)): their Schedule J keys items 1 and 2 separately, item 2 being maternity for one who is neither an employee nor self-employed (line 4721); the employee column prints nothing for item 2, so nothing for an employee turns on the question, and nothing in Axiom conflicts with N3.

**s 67A.** Axiom's record agrees that there is no s 67A.
Its two gap entries whose identifiers read `nii-section-67a-…` (`ENCODING-GAPS.md` lines 482-502) are about s 67(a), the rule that a child is counted with one insured parent at a time, which they quote word for word from the provision at line 817; `README.md` line 49 calls it "§67(א)'s one-parent-at-a-time limit".
Their source map lists s 67, not s 67A, among the encoded sections (lines 88-97).
So the observation in section 2 stands, and Axiom's material supports it.
A guess, not checked (the backlog was not read in this pass): the "s 67A" in row IL-08's ruled list may be a reading of Axiom's identifier `67a` as a section number; the same list's ITO s 121A matches an item of Axiom's `not_encoded` list.

### What Axiom does that this half does not, and the reverse

**Axiom, not us**: the rates (s 337, Schedule J), the reduced bracket (s 334), the ceiling and small non-work income (s 348, Schedule K), who pays (s 342(a), (d)), the man's age in s 342(c)(2); all outside this row's scope, and the natural consumers of our s 335 list and Part D age.
**Us, not Axiom**: Part D, s 72 and s 335, with forks N1-N4 and the refusals for earlier periods.

### Bottom line

Axiom encodes none of the three provisions of this half.
Part D it tried three times and could not encode for a reason in its tooling, and its absence is one of the reasons Axiom gives for deferring the employee's deduction under s 342(c)(1); our Part D module is that missing piece, and the figures Axiom states for the table agree with ours.
s 335 it left out by charter, and its s 337 charges every employee the full employee rate; our branch list is what a composer needs to charge a controlling shareholder in a closely-held company or a non-resident worker correctly, with the caution that Schedule J's branch rows do not add up to its printed totals.
s 72 does not appear in Axiom's material at all; its monthly child count leaves the first and last months to the caller.
On s 67A the two records agree.
No finding of this comparison shows a rule of this half wrong; one stated reason of Axiom's points at a repealed subsection (B2).
