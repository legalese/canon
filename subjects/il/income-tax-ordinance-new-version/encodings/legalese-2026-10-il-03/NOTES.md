# NOTES — il/income-tax-ordinance-new-version, encoding row `legalese-2026-10-il-03`

Income Tax Ordinance [New Version], **s 120B** (indexation), **s 121** (the individual's rate of tax) and **s 121B** (additional tax on high incomes), encoded in L4 by one agent in one session (run `IL-03-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

## 0. What `check.sh` prints

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, a local cabal build in store entry `jl4-0.1-0ee0100b`, modified 2026-10-06 21:20 (local), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`, and no record beside it names the commit it was built from.
It was rebuilt at 21:20, one minute before this directory was created; every run recorded here was made after that.

```
module                                    errors satisfied  failed  refused  expected
ito-120b-indexation.l4                         0         0       0        0         0
ito-121-individual-rates.l4                    0         0       0        0         0
ito-121b-additional-tax.l4                     0         0       0        0         0
ito-il03-nouns.l4                              0         0       0        0         0
ito-il03-tests.l4                              0        86       0        0         0
TOTAL (5 modules)                              0        86       0        0
```

`check.sh` exit 0.
The tests module has 86 `#ASSERT` directives and all 86 are satisfied; no failure or refusal is expected and none occurs.
The rule modules carry no assertions of their own.
To show the harness can fail, a scratch copy with six expected values deliberately altered was run: it reported 6 failed, 6 errors, exit 1.
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary chooses its embedded copies, and the warnings are not errors.

Two mechanical checks were run over every file, with the scripts in `tools/` (run them with `python3 -I`):
`tools/srcquote.py SOURCE FILE.l4…` regenerates every `-- src:N | …` comment from line N of the source file, reducing the wiki templates; `tools/hebcheck.py SOURCE FILE…` checks that every other run of Hebrew in the modules, the Markdown files and `encoding.json` occurs verbatim in the source (raw or template-reduced).
Both passed; the second fails on a planted non-source string.

## 1. What is encoded and what is not

**Encoded:** s 120B(a), (b), (d) and (e) as a mechanism over supplied index readings and supplied amounts; s 121(a) and (b) in full, with the figures the text prints, for tax years 2026 and 2027; s 121B(a), (a1), (b) and (e) in full, for tax years from 2026, with the (a) amount supplied by the caller.
The definitions those sections use are encoded as far as they need: s 1 "שיעור עליית המדד" and "סכום מתואם" as arithmetic; s 1 "הכנסה חייבת", "הכנסה מיגיעה אישית", "פנקסים קבילים" and "שנת מס" as the shape of the inputs.

**Not encoded:** s 121A (repealed; row IL-08); credit points, ss 33A-36A (row IL-01), which reduce the tax computed here; s 66 (row IL-02), which decides whose income an item is; the sections that charge particular income at rates of their own (ss 91, 122, 125B, 125C and others); s 8(c) spreading; the Real Estate Taxation Law (betterment, its inflationary amount, exemptions, s 9(c2) adjustment); and the Income Tax (Rules for Rounding Amounts) Order 5746-1986.
Each of these that feeds a provision in scope enters as an **input**, with its citation in the nouns module.

**No figure in this encoding comes from anywhere but the text.**
The consumer price index and every amount the Israel Tax Authority publishes are inputs with no default (section 7 says why nothing was fetched).
Figures that appear only in the consolidation's editorial notes are not encoded; the tests supply one of them (721,560) as a labelled scenario value.

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/income-tax-ordinance-new-version.he.wiki.txt`.
Totals: **25 encoded, 4 inert, 1 out-of-scope, 0 deferred** (30 rows).

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 120B(a) | 4338 | adjust on 1 January by the rise in the index over the previous tax year | encoded | `s 120B(a) — adjust`, `s 120B — the amount for the tax year` |
| s 120B(b) | 4339 | pension-point amounts adjusted mid-year when a cost-of-living increment is agreed | encoded | `s 120B(b) — the pension-point amount from the month of …` |
| s 120B(c) | 4340 | (repealed) | inert | comment |
| s 120B(d) | 4341-4342 | the Minister's rounding power; the 5746-1986 Order is noted as made | encoded (as a named refusal: the Order is not in the sources) | `the rounding rules made under section 120B(d) are not encoded in this model` |
| s 120B(e) chapeau | 4343 | notwithstanding (a) and (b) | encoded | arm order in the dispatcher and in (b) |
| s 120B(e)(1) | 4344 | no adjustment on 1 January 2025-2027; the 1 January 2024 amounts after rounding | encoded | `s 120B(e)(1) — no adjustment in tax year` |
| s 120B(e)(2) | 4345 | on 1 January 2028, the 1 January 2024 amounts before rounding, by the 2027 index | encoded | `s 120B(e)(2) — adjust on 1 January 2028` |
| s 121(a) chapeau | 4350 | the tax on an individual's taxable income in the tax year | encoded | `the tax under section 121 for` |
| s 121(a)(1) | 4351 | first 301,200 at 31% | encoded | `s 121(a) — the tax on` |
| s 121(a)(2) | 4352 | 301,201-560,280 at 35% | encoded | same |
| s 121(a)(3) | 4353 | each further shekel at 47% | encoded | same |
| s 121(b)(1) chapeau | 4354 | notwithstanding (a)(1): income from personal exertion, and income of an individual who has reached 60 | encoded | `s 121 — the tax on … , of which eligible …`, `eligible for the reduced rates`, `aged 60 or more by the end of the tax year` |
| s 121(b)(1)(a) | 4355 | first 84,120 at 10% | encoded | `s 121(b)(1) — the tax at the reduced rates on` |
| s 121(b)(1)(b) | 4356 | 84,121-120,720 at 14% | encoded | same |
| s 121(b)(1)(c) | 4357 | 120,721-228,000 at 20% | encoded | same |
| s 121(b)(1)(d) | 4358 | 228,001-301,200 at 31% | encoded | same |
| s 121(b)(2) | 4359 | no reduced rates on income for which books were required and acceptable books not kept | encoded | `eligible for the reduced rates` |
| s 121, note: simulator | 4361-4362 | editorial link to the Tax Authority's simulator | inert | comment |
| s 121, note: tables 2019-2027 | 4364-4450 | editorial tables of brackets by year | inert (the 2026-2027 table is used once in the tests as a second transcription) | comment; tests |
| s 121A | 4452-4453 | (repealed) | out-of-scope | see below |
| s 121B(a) | 4456 | 3% on taxable income above 640,000 (as at 2017) | encoded | `s 121B(a) — the additional tax on`, `the amount printed in section 121B(a), as at 2017` |
| s 121B(a1) | 4457 | a further 2% on capital-source income above the same amount | encoded | `s 121B(a1) — the additional tax on` |
| s 121B(b) | 4458 | s 91(d) on advance payments does not apply | encoded (the one answer it gives) | `s 121B(b) — section 91(d) on advance payments applies …` |
| s 121B(c) | 4459 | applies notwithstanding any enactment | inert | comment: no other enactment is encoded here for it to override |
| s 121B(d) | 4460 | s 8(c) spreading applies in computing taxable income for s 121B | encoded (as an input convention) | `amount` is taken after s 8(c) spreading |
| s 121B(e) "הכנסה חייבת" | 4462 | s 1 and s 89 income, less inflationary amounts, plus betterment, with the residential-apartment limb | encoded | `the taxable income for section 121B of`, `the betterment on … counts …`, `the residential-apartment sale value in section 121B(e) for tax year` |
| s 121B(e) "הכנסה חייבת ממקור הוני" | 4463 | taxable income other than … | encoded | `from a capital source` |
| s 121B(e) cap. source (1) | 4464 | s 2(1)/(2) income excluded | encoded | same |
| s 121B(e) cap. source (2) | 4465 | other personal-exertion income excluded | encoded | same |
| s 120A "תקרות הכנסה" (used, not in slice) | 4335 | what "income ceilings" means for s 120B | encoded (as the record `The income ceilings of section 121`, and the reason the s 121B(a) amount is adjusted by s 120B) | nouns |

**s 121A, out of scope.**
The deposited text shows only "(בוטל)" (repealed) under the section number, with its amendment tags (5750, 5753, 5754).
Its former text is not in the source, so there is nothing here to encode but the fact of repeal, and that fact belongs to row IL-08, to which the lead has assigned s 121A: a repeal stub here as well would put two records of one provision in canon with nothing to keep them in step.
Its pre-repeal text could matter only to tax years in the early 1990s or before, and this row answers no tax year before 2025 (assumption A1).

## 3. Assumptions

**A1. The tax years answered.**
s 121: tax years **2026 and 2027** only.
s 121B: tax years **from 2026**, with the s 121B(a) amount supplied; a residential-apartment sale is answered only for 2026 (the text fixes that threshold for 2025 and 2026, and from 2027 it moves under a Law not encoded).
s 120B: adjustments **from 1 January 2025**.
Everything earlier is declined by a named `REFUSE`, and so is s 121 from 2028.
Why: the source is a consolidation "as amended at retrieval", and the three sections' amendment lists end in 5785 (ss 120B, 121B) and 5786 (s 121).
The text as it stood before those amendments is not in the sources, and answering an earlier year from the text as amended would borrow one vintage's figures for another.
For s 121 the 2026 boundary is also visible in the source's own aids: the editorial tables (lines 4429-4448) show the (a)(1)/(b)(1)(d) and (b)(1)(c) figures moving between "2024-2025" and "2026-2027".

**A2. The tax year is an explicit input, and the dated arms select on it.**
The skill's rule-effective-time axis (`RULES EFFECTIVE DATE`) was not used.
In this subject the question "which version of the law" is answered by the tax year whose income is being taxed, not by the date of evaluation: s 120B speaks of "1 January of each tax year", and the figures are stated per tax year.
Taking the year as a field of the case keeps it on the return where it belongs, and every dated arm (`BRANCH IF … tax year …`) carries its citation.

**A3. The figures printed in s 121 are the figures for 2026 and 2027.**
Basis: the consolidation's note at line 4350 ("(הסכומים מתואמים לשנים 2026–2027)"), the matching editorial table at lines 4441-4447, and s 120B(e)(1), under which no indexation intervenes in 2025-2027.
The consolidation's editors write adjusted figures into the text; the official base figures in the amending Laws could not be compared (section 7).

**A4. Figures found only in editorial notes are not encoded.**
In particular the s 121B(a) amount for 2024-2027 (721,560) and for 2023 (698,280), and the s 121B(e) note that the residential threshold is 5,385,285 "in 2026" (that one is used only to say the printed figure holds for 2026, alongside the text's own figure).
The text of s 121B(a) prints 640,000 "nominal for 2017", the base s 120B indexes from; the figure in force is an input.

**A5. Classifications outside the slice are inputs.**
Whether an item is from personal exertion; whether it is s 2(1)/(2) income; whether another section charges it at its own rate; whether books were required and acceptable books not kept; the s 88 inflationary amount; the betterment, its s 47 inflationary amount, the sale value and any exemption of a real-estate sale; which spouse's income an item is (s 66); and any s 8(c) spreading.
Each is recorded on a return or an assessment, so a caller can supply it (phrasebook 1.6, reading 1).

**A6. The s 121 result is the tax before credit points.**
Credit points (row IL-01) are deducted from it elsewhere.
s 121B is computed separately and is not added to it here.

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | s 121(b)(1), line 4354 | When an individual under 60 has both personal-exertion income and other income on the scale, which shekels of the scale does the eligible income occupy? | (i) the eligible income at the bottom; (ii) the other income at the bottom; (iii) pro rata | **(i)**. (b)(1)(a) speaks of "the first 84,120 shekels"; under (ii) those shekels would be other income and the reduced rates would never reach an individual with other income above 84,120, which empties (b)(1) for exactly the mixed case it names. Where the Ordinance does order income, it puts special-rate income at the highest step (s 91(b)(1), line 3347; s 125C(b), line 4530), which points the same way. Not settled by any text in the slice. |
| F2 | s 121(b)(1), line 4354 | "of an individual who has reached 60": tested when? | (i) at any time up to the end of the tax year; (ii) at the start of the tax year; (iii) only income derived after the 60th birthday | **(i)**: the provision attaches the age to the individual and the income to the tax year, and the year is the unit of assessment. (iii) would need the income split by date, which the text does not ask for. |
| F3 | s 121(b)(2), line 4359 | Does (b)(2) reach the over-60 individual's income that is not from personal exertion? | (i) yes, any income for which books were required and not kept; (ii) only personal-exertion income | **(i)**: the text says "income" without qualification. |
| F4 | s 120B(a), line 4338; s 1, line 180 | If the index falls, is the amount reduced? | (i) yes, the s 1 arithmetic gives a negative rate and it is applied; (ii) no, "עליית" (rise) means only rises count | **(i)**: the definition is a formula and yields a negative number on its own terms. The editorial tables show amounts falling from 2020 to 2021 (e.g. 75,960 to 75,480, lines 4382 and 4394), which fits (i); they are aids, not authority. |
| F5 | s 120B(e)(2), line 4345 | "the index in the previous tax year … shall be the index of tax year 2027": only 2027's rise, or the rise since 2024? | (i) 2027's rise only, so 2024-2026 inflation is not recovered; (ii) cumulative | **(i)**: it names one tax year's index, and (a)'s mechanism measures over one tax year. |
| F6 | s 120B(a) | Does the year-on-year chain carry rounded or unrounded figures? | (i) unrounded, rounding only the figure in force; (ii) rounded | **(i)**: (e)(2) restarts "before rounding", which is natural only if the chain runs unrounded. It changes no answer this row gives, because every rounded figure is either supplied or declined. |
| F7 | s 120B(e)(2) with s 121 as amended in 5786 | What is the 2028 base for the ceilings the 5786 amendment moved ((a)(1), (b)(1)(c), (b)(1)(d))? | (i) their 1 January 2024 figures, which would undo the 5786 change; (ii) the figures as amended; (iii) whatever the amending Law provides | **not answered**: s 121 from 2028 is declined by name. The amending Law could not be read (section 7). |
| F8 | s 121(a)(1), (b)(1)(d) | The text prints the top of the 31% band twice (301,200). If the two ever differ, which governs? | — | **declined**: a supplied set of ceilings in which they differ is refused; the printed figures agree, and a test says so. |
| F9 | s 121B(e), line 4462 | Does "and the sale is not exempt" govern only the residential limb? Is the s 47 inflationary amount excluded from a sale whose betterment does not count? | (i) the exemption condition is part of the residential limb only, and a sale that does not count contributes nothing; (ii) the exemption condition applies to all betterment; the inflationary amount is excluded from income generally | **(i)**: the condition sits inside the clause opened by "ואולם לגבי מכירת זכות במקרקעין בדירת מגורים"; subtracting an uncounted sale's inflationary amount from other income would tax less than the income. |
| F10 | s 121B(e), line 4462 | Which year's residential threshold applies to a sale? | (i) the tax year in which the betterment is counted; (ii) the date of the sale under the Real Estate Taxation Law's own calendar | **(i)**, the case's tax year; the two coincide for a sale in that year. |
| F11 | s 121B(a1), line 4457 | (a1) says "ממקורות הוניים" (plural); (e) defines "הכנסה חייבת ממקור הוני" (singular). | (i) the defined term; (ii) an undefined term | **(i)**. |
| F12 | s 1 "שנת מס", line 202 | A special assessment period. | — | **not modelled**: the tax year is a calendar year. Omitting the second limb can only mis-time a case that has one; nothing in this row would tell. |
| F13 | s 120B(e)(1), line 4344 | "שנות המס 2025 עד 2027": is 2027 included? | (i) inclusive; (ii) exclusive | **(i)**: (e)(2) restarts on 1 January 2028 from the 2024 figures by the index of 2027, which presupposes no adjustment on 1 January 2027; the notes at lines 4350 and 4456 agree. |
| F14 | s 121B(a), (a1), (e) | "עלתה על" / "עולה על" (exceeded / exceeds) at exactly the threshold. | — | **strict** (`GREATER THAN`). For (a) and (a1) the tax at the threshold is 0 either way; for the residential limb it decides whether the betterment counts, and a test sits on the boundary. |
| F15 | s 121B(e) cap. source | Is betterment under the Real Estate Taxation Law capital-source income? | — | **yes**: it is neither s 2(1)/(2) income nor personal-exertion income, which are the only exclusions. |
| F16 | s 121, "על כל שקל חדש" | Is income or tax rounded to whole shekels? | — | **no rounding**: the slice says nothing about it; amounts are continuous. |
| F17 | s 120B(b), line 4339, with (e)(1) | Does the freeze also stop a mid-year cost-of-living adjustment in 2025-2027? | — | **yes**: (e) opens "notwithstanding (a) and (b)" and (e)(1) says no adjustment "under (a) and (b)". |

## 5. Answer table

Figures from the text (lines 4351-4358, 4456, 4462) unless marked.
"Declined" means a named `REFUSE`.

| provision | 2025 | 2026 | 2027 | 2028 on |
| --- | --- | --- | --- | --- |
| s 121(a)(1) top of the 31% band | declined | 301,200 | 301,200 | declined (F7) |
| s 121(a)(2) top of the 35% band | declined | 560,280 | 560,280 | declined |
| s 121(b)(1)(a) top of the 10% band | declined | 84,120 | 84,120 | declined |
| s 121(b)(1)(b) top of the 14% band | declined | 120,720 | 120,720 | declined |
| s 121(b)(1)(c) top of the 20% band | declined | 228,000 | 228,000 | declined |
| s 121(b)(1)(d) top of the reduced 31% band | declined | 301,200 | 301,200 | declined |
| rates, s 121 | — | 31 / 35 / 47; reduced 10 / 14 / 20 / 31 | same | — |
| s 121B(a) amount | declined | input: the 1 Jan 2024 figure after rounding (s 120B(e)(1)); editorial note says 721,560 | same | input: adjusted under s 120B(e)(2) and rounded |
| s 121B rates | — | 3% (a); 2% (a1) | same | same |
| s 121B(e) residential threshold | 5,385,285 | 5,385,285 | declined (RE Law s 9(c2)) | declined |
| s 120B amounts | fixed at 1 Jan 2024, after rounding | same | same | 1 Jan 2024 before rounding × (1 + 2027 rate), then rounded (declined) |

Worked figures the tests assert (tax year 2026; the same for 2027):

| facts | s 121 tax |
| --- | --- |
| 301,200 of other income, under 60 | 93,372 |
| 560,280 of other income, under 60 | 184,050 |
| 84,120 salary | 8,412 |
| 120,720 salary | 13,536 |
| 228,000 salary | 34,992 |
| 301,200 salary | 57,684 |
| 560,280 salary | 148,362 |
| 100,000 salary + 50,000 other income, under 60 | 26,135.2 (F1) |
| 150,000 other income, 60 by 31 December | 19,392 (F2) |
| 200,000 business income without the acceptable books it required | 62,000 |

| facts (s 121B(a) amount supplied as 721,560) | s 121B tax |
| --- | --- |
| 800,000 salary | 2,353.2 |
| 1,000,000 dividend | 13,922 (8,353.2 + 5,568.8) |
| 1,000,000 salary | 8,353.2 |
| capital gain 900,000, of which 100,000 inflationary | 3,922 |
| residential apartment sold for exactly 5,385,285 | 0 (F14) |

## 6. Nouns to reconcile at IL-07

Read from the sibling deposits (read-only) at the end of this session; nothing here depends on them and nothing in them was changed.

- **The individual.** This row: `An individual in a tax year` (tax year, date of birth, items of income, real-estate sales). IL-01: `Individual` (residence, sex and status flags) inside `Person`. IL-02: `A spouse` and `Spouses in a tax year`. Three records for one taxpayer.
- **Items of income.** This row: `An item of income` with flags (personal exertion, s 2(1)/(2), charged at the s 121 rates, books, s 88 inflationary amount). IL-02: `An item of income from personal exertion` (kind, taxable amount) plus per-spouse totals by source. The s 121 scale needs the personal-exertion split; s 121B needs the capital-source split; s 66 needs the attribution. One item record could carry all three.
- **The tax year.** All three take it as a `NUMBER`, but scope it differently: this row answers s 121 for 2026-2027; IL-02 records 2024 as the first year its s 66 text governs.
- **The credit-point amount.** IL-01 holds a per-year published value; this row treats "the amount of a credit point" as one of the s 120B amounts, frozen in 2025-2027 at its 1 January 2024 rounded figure. The two should agree, and that is a test IL-07 can write.
- **Age.** This row takes a date of birth; IL-02 takes a child's tax year of birth.

## 7. Sources: what was fetched, and what was not

Only the deposited source was read (sha256 `b87f2cf4…6b81b6`, verified on 2026-10-06 before use).
Three fetches were attempted on 2026-10-06 and all failed, so no official publication supplies any figure here:

- the 5786 Economic Efficiency Law (Knesset `25_lsr_12235101.pdf`) and the 5785 freezing Law (`25_lsr_5396578.pdf`) from `fs.knesset.gov.il`: both returned the same 131,618-byte HTML page titled "Unavailable" instead of a PDF, with and without browser headers;
- a `www.gov.il` page of the Tax Authority: HTTP 403, a Cloudflare challenge.

Nothing was kept from those responses.
The amending Laws were identified only by their position and title in the file's own list of amending Laws (line 5): tag 5785-2 is the Economic Efficiency Law for the 2025 budget year ("freezing of tax updates and surtax", Sefer HaChukim 5785 p. 150); tag 5786-6 falls in the Economic Efficiency Law for the 2026 budget year (5786 pp. 415-416).
That identification is by counting entries and was not checked against the Laws.

**Observations about the source**, for whoever maintains it:

- Line 4462 repeats a phrase: "המדד שפורסם ביום המדד שפורסם ביום ז׳ בשבט התשפ״ז". Whether the error is the consolidation's or the Law's could not be checked.
- The editorial table for 2023 (lines 4419-4421) misnumbers two band edges: "116,711" where the band must start at 116,761, and "187,481" where it must start at 187,441.
- The editors treat the two sections differently: s 121 has adjusted figures written into its text, s 121B keeps the 2017 base in its text and puts the adjusted figures in a note.

## 8. Open questions for a domain expert

1. F1: in practice, does the Tax Authority place personal-exertion income at the bottom of the s 121 scale for an individual under 60 with other income? Is there a provision or ruling outside this slice that says so?
2. F2: for the year in which an individual turns 60, are the reduced rates applied to the whole year's income?
3. F7: does the 5786 amendment of s 121 say how its new ceilings are treated on 1 January 2028 under s 120B(e)(2), or is the bracket change a temporary provision for 2026-2027?
4. Does the 5785 amendment say from which tax year s 121B(a1) applies? (If from 2025, this row could answer s 121B for 2025.)
5. Is the duplicated phrase at line 4462 in the Law as published?

## 9. What was not done

- **The independent test pass** (skill step 8) was not run: the brief for this row is one session with no sub-agents. Every expected value was worked by hand from the text before it was asserted, but no second reader has derived them.
- **HG1**, a human who knows Israeli income tax reading the modules against the Hebrew, has not been sought.
- **Semi-cleanroom** (ruled 2026-10-06): nothing from the Axiom Foundation, any RuleSpec repository, or the paths the brief lists was read, searched or fetched in this session.
