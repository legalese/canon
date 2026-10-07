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
