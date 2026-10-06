# IL-07 — reconciling the six rows' nouns, and the changes proposed to the rows

The six rows were encoded in parallel, each with its own nouns module, and each row's NOTES.md ends with a list of "nouns to reconcile at IL-07".
This file is the reconciliation: every clash found, how the capstone resolves it, and what each row should change to make composition cleaner.
**No row was edited.** Every proposal here is for the row's own encoder or the lead.

File and line references are to the vendored copies in this directory, which `VENDORED.sha256` pins byte for byte to the rows' files.

## 1. How the capstone composes at all

**Cross-directory IMPORT does not work** with this `l4` (sha256 `64bbcb15…e118`), verified 2026-10-07 in the scratchpad: ``IMPORT `../…/legalese-2026-10-il-01/ito-credit-points-nouns` `` fails with "I could not find a module with this name: ito-credit-points-nouns", and a symlink to `ito-s34-s36-s36a-credits.l4` resolves but its own imports (`ito-credit-points-nouns`, `ito-s33a-credit-point`) are then looked for beside the link and not found.
Row IL-05 found the same (its NOTES.md section 8).

**So the rows' rule modules are vendored**: `vendor.sh` copies 36 modules (each row's import closure: nouns, rules, published figures; never tests) flat into this directory under their own names, `VENDORED.sha256` records each one's sha256, row and commons commit, `.gitignore` keeps the copies out of git, and `check.sh` begins with `vendor.sh --check`.
No two rows share a module file name (checked: the only duplicate name across the six directories is `tests-independent.l4`, never vendored).

**L4 imports are transitive** (measured: a module importing an adapter sees the names the adapter imported).
So adapters do not hide a row's names from the pipeline.
What they do is make every *reference* unambiguous: each adapter imports this row's nouns and ONE row, resolves that row's names in a scope where only that row defines them, and exposes plain numbers, booleans, dates, or this row's own small records, under names beginning "IL-0N:".
The pipeline refers only to those names.

**How a clash behaves**, measured 2026-10-07 by importing two rows' nouns into one probe module:

| clash | measured behaviour |
| --- | --- |
| a type name declared by two rows, used as a type (`A child` from IL-02 and IL-06; `A problem with the facts` from IL-03 and IL-06) | error: "There are multiple definitions for the identifier … and I do not have sufficient information to make a choice between them" |
| a value of the same name and type in two rows (IL-04's and IL-05's `the reduced collection threshold for 2026, as published by the National Insurance Institute`) | the same error |
| constructors of the same name in two rows' types, where nothing fixes the expected type (IL-04's and IL-05's `maternity`, `children` in a bare `LIST`) | the same error |
| constructors of the same name where the expected type is fixed (IL-02's `Sex` and IL-05's age-limb type both have `a woman`, `a man`; compared with a `Sex`) | resolved by type, no error |
| a record field and a constructor of the same name (IL-01's field `a woman`, IL-02's constructor `a woman`) | resolved by type, no error |
| two modules that declare the same names, imported but not referred to | no error |

So a clash is harmless until a module refers to the name where the type does not decide it.
Adapters guarantee that never happens.

## 2. Every noun clash, and its resolution

| # | the noun | declared in | resolution in the capstone | proposed change to the row |
| --- | --- | --- | --- | --- |
| N1 | `A branch of insurance` (nine constructors) and `A column of insured persons in Schedule J` (three) | IL-04 `nii-il04-nouns.l4:35`, `:52`; IL-05 `nii-il05-nouns.l4:32`, `:45` (declared again, constructor for constructor, because IL-05 could not import IL-04) | The IL-04 adapter computes Schedule J column D per branch with IL-04's constructors and returns this row's record `IL-07 column D amounts on the earner's wage` (one field per branch); the IL-05 adapter turns that record into IL-05's `A branch's column D amount` list with IL-05's constructors. The branches are matched by name, field to constructor. | **IL-05**: delete its copies and import IL-04's nouns once the two can share a directory or a library path (IL-05 NOTES.md section 6 already says so). Until then, nothing: the copies are exact. |
| N2 | the woman and the man | IL-01 BOOLEAN field `a woman` on `Individual` (`ito-credit-points-nouns.l4:40`); IL-02 `Sex` = `a woman` / `a man` (`ito66-nouns.l4:27`); IL-05 `The insured person, for the age limb of section 342(c)(2)` = `a man` / `a woman HAS` her Part D age (`nii-il05-nouns.l4:203`); IL-06 `Father or mother` (`nii-il06-nouns.l4:88`) | One input, `the earner is a woman` (and `the spouse is a woman`); each adapter maps it: the IL-01 field, IL-02's `Sex`, IL-05's age-limb constructor (with the Part D age input), IL-06's father or mother. | One sex noun in a shared person module for the two subjects, with the Part D age a field of the woman. Low priority: the type-directed resolution makes the overlap harmless in practice. |
| N3 | `A child` | IL-02 `ito66-nouns.l4:90` (tax year of birth, whose child, the mother's (a1) election, the child's s 66(a)(3) income); IL-06 `nii-il06-nouns.l4:123` (name, date of birth, married, absence, parents) | This row's `IL-07 child` (name, date of birth, the (a1) election); the IL-02 adapter derives the tax year of birth with `DATE_YEAR` (s 40(b)(3): the tax year in which the child was born), the IL-06 adapter passes the date. | **IL-02 and IL-06**: qualify the names (`A child, for section 66`; `A child, for the child allowance`), so that one module can name both types. |
| N4 | `A problem with the facts` | IL-03 `ito-il03-nouns.l4:84` (three constructors); IL-06 `nii-il06-nouns.l4:188` (five) | Each adapter turns its row's LEFT into a named refusal of this row (`il07-refusals.l4`), so neither type reaches the pipeline. | **IL-03 and IL-06**: qualify the names. |
| N5 | the 2026 published figures: the reduced collection threshold (7,703) and the two average wages (13,566 under s 1, 13,769 under s 2) | IL-04 `nii-il04-published-figures.l4:34`, `:52`, `:56`; IL-05 `nii-il05-published-figures.l4:32`, `:47`, `:51` (same names, same figures, separate fetches with different sha256s, both rows say) | Each adapter refers only to its own row's figure; `il07-tests.l4` asserts that IL-04's threshold equals IL-05's (satisfied). | **IL-04 and IL-05** (and IL-06's `nii-il06-published-figures.l4`): one published-figures module for the subject, one provenance format. |
| N6 | the person | IL-01 `Person` / `Individual`; IL-02 `A spouse` / `Spouses in a tax year`; IL-03 `An individual in a tax year`; IL-04 `A person who works`, `An employee's month of contributions`; IL-05 `An insured person's period under section 348`, `An employee's month under section 342(c)`; IL-06 `A person`, `A family on a day` | This row's `IL-07 earner`, `IL-07 spouse`, `IL-07 couple`, `IL-07 household in a month`; each adapter builds its row's records from them. No row's person is the capstone's. | None needed for composition. A shared insured-person record (IL-04 and IL-06 notes both suggest it) would shorten two adapters. |
| N7 | **s 36A's half point, twice** | IL-01 `the credit points under section 36A for` (`ito-s34-s36-s36a-credits.l4:203`), with the reach of s 48A; IL-02 `one half point under section 36A, by paragraph (4)` (`ito66-c-credit-points.l4:304`), 0.5 for every woman in a separate calculation | Counted once, from IL-01. A test asserts the two agree for a resident woman (0.5) and a man (0); the red module shows they part for a resident foreign worker (finding R2). | **IL-02**: s 66(c)(4) gives the half point "לפי סעיף 36א", under s 36A. Either drop the field and leave s 36A to IL-01, or make it decline where s 36A as IL-01 encodes it declines (s 48A). |
| N8 | the value of a credit point | IL-01 takes it as an input and publishes the ITA's 2025 value (2,904) and monthly 242 for 2024-2026; IL-03's s 120B gives the 2025-2027 amount as the 1 January 2024 figure after rounding, an input | Composed: IL-03's s 120B for the year, with IL-01's 2025 figure as the 1 January 2024 rounded figure (fork K2). Asserted: 2026 = 2,904; 2025 through IL-03 = IL-01's published 2025; 12 × 242 = 2,904. | **IL-01**: say in its published-figures module that, by s 120B(e)(1), its 2025 figure is the frozen figure for 2025-2027 (its NOTES.md section 4 already leaves this to IL-03). **IL-03**: none. |
| N9 | items of income | IL-02 `An item of income from personal exertion` (`ito66-nouns.l4:60`: kind, amount, pension flags); IL-03 `An item of income` (`ito-il03-nouns.l4:37`: amount and five classification flags) | Each adapter builds its own from the salary (one item of employment income). | One item record carrying both rows' facts, as IL-03's notes suggest; not needed for the capstone. |
| N10 | the period | IL-02 `tax year`; IL-03 `tax year`; IL-04 `calendar year of the month`; IL-05 `tax year` and `month`; IL-06 `the day` | The household's `the year of the month` and `the month of the year`; IL-06's day is the first of the month (fork K6). | None. |
| N11 | age | IL-02 a child's tax year of birth; IL-03, IL-05, IL-06 a date of birth | Dates of birth throughout; IL-02's tax year derived. | None. |
| N12 | the additional-tax link | IL-06 takes `income chargeable to additional tax under section 121B of the Income Tax Ordinance` as a BOOLEAN (its fork F5: which tax year); IL-03 computes s 121B | Joined: TRUE where IL-03's s 121B tax for the tax year in which the month falls is above nil (fork K5). | **IL-06**: record that the join is made at IL-07 and how; its F5 stays open. |
| N13 | the allowance point | IL-01 "allowance point"; IL-03 "pension point" (`the amount of a pension point`) for "נקודת קיצבה" | Not used by the capstone. | **IL-01 and IL-03**: choose one English name. |
| N14 | IL-04's column D average-wage argument | IL-04 `the column D deduction under … and the average wage at …` (`nii-schedule-j.l4:405`) | Every version IL-04 reads for 2026 on starts column D's upper part at the threshold (its F3, repaired), so the average wage is never read; the adapter passes a named refusal there instead of choosing between IL-04's two figures (its open F5). | **IL-04**: note that the argument is dead for 2026 on, or drop it from a 2026-on entry point. |

## 3. Findings: where a row disagrees with another row or with the regulator

Each finding is an assertion in `il07-tests-expected-red.l4`, expected to fail, counted in `check.sh` and `encoding.json`.

- **R1 (IL-04's open fork F4, at household level).** The Institute deducts 7% from an employee above the reduced collection threshold (IL-04 NOTES.md section 7); Schedule J's column D items, which IL-04 computes from, sum to 4.67%.
  For a salary of 15,000 that is 170.0201 a month: IL-04 gives 420.8811, the Institute's composite 590.9012.
  Two assertions fail (the deduction and the net). Nothing to propose beyond what IL-04's F4 and open question 1 already ask: which governs, the items or the printed total.
- **R2 (IL-02 against IL-01).** See N7: for a resident foreign-worker woman in a separate calculation, IL-01 declines s 36A (s 48A) and IL-02 gives its half point. One assertion fails.

Evidence for rows, found in composing them (no assertion fails; offered to the rows):

- **For IL-03: the enacted Law confirms its 2026 brackets.** The Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Year 2026), 5786-2026, Sefer HaChukim 3511, 31 March 2026, pp. 414-416, ch. C ("widening of income tax brackets"), s 5 amends s 121 to exactly the figures IL-03 encodes (301,200; 301,201-560,280 at 35%; 228,000; 228,001-301,200 at 31%); **s 6** commences the chapter on 1 January 2026 for income produced or accrued from that day; **s 7** says that for the adjustment under s 120B(e) the amended amounts are to be treated as the amounts adjusted on 1 January 2024.
  Fetched 2026-10-07 directly from the Internet Archive capture `https://web.archive.org/web/20260718005658id_/https://fs.knesset.gov.il/25/law/25_lsr_12235101.pdf` (40 pp., 519,764 bytes, sha256 `72244dba261c44d2818f80708fa2dece5d8b99f75e788f48e290942ff4734155`), s 5-7 on PDF p. 4; not deposited (the lead decides).
  **Proposed for IL-03**: cite it in place of assumption A3's reliance on the editorial note, and read s 7 against fork F7: it treats the amended figures as the 1 January 2024 adjusted amounts for s 120B(e), which points to reading (ii) (the 2028 base is the amended figure), though whether "adjusted" there means before or after rounding is for IL-03 to read.
- **For IL-03: the s 121B(a) amount for 2026 is published.** The Tax Authority's 2026 withholding booklet (the file IL-01 cites, sha256 `282bb886…6e86285`), PDF p. 8: 721,560 a year, 60,130 a month. The capstone carries it (`il07-published-figures.l4`). **Proposed for IL-03**: carry it as a published figure, and say so in its answer table.
- **The same booklet's 2026 bracket table (PDF p. 7) is stale.** It prints 20% to 193,800 and 31% to 269,280, the pre-amendment figures: the booklet was captured on 7 February 2026, before the 5786 Law was published on 31 March 2026. No row uses the booklet's brackets; noted so that nobody does.
- **For IL-06: its fork F6 has a household-level consequence.** In H7 (the father earns 70,000, the mother is a housewife) the children are in the father's count and he has income chargeable to additional tax: no allowance. In H8 (the mother earns 70,000, the father is at home and insured) the children are in the father's count (s 67(b) first limb) and he has none: an allowance of 392. Same income, same children, opposite answers by the earner's sex. This is the text read literally (IL-06's F6, open question 1), not a defect of the composition.

## 4. What the capstone owns, and what it does not

The capstone owns: its nouns, its named refusals (13 in `il07-refusals.l4`, four in the adapters, one in the figures module), one published figure (the s 121B(a) amount for 2026), and the forks in NOTES.md section 4.
It owns no rule of law.
Every rate, threshold, count and amount is computed by a row, through its adapter.
