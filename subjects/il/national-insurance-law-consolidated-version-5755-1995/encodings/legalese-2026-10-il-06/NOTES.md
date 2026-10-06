# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-06`

National Insurance Law [Consolidated Version], 5755-1995, **ss 66, 67 and 68** (the child allowance: the right to it, the count of children, the amount), with **s 65** and the parts of **s 1** they read, encoded in L4 by one agent in one session (run `IL-06-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

## 0. What `check.sh` prints

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to cabal store entry `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`, and no record beside it names the commit it was built from.

```
module                                    errors satisfied  failed  refused  expected
nii-il06-family-on-a-day.l4                    0         0       0        0         0
nii-il06-nouns.l4                              0         0       0        0         0
nii-il06-period.l4                             0         0       0        0         0
nii-il06-published-figures.l4                  0         0       0        0         0
nii-il06-tests.l4                              0       117       0        0         0
nii-s1-basic-amount.l4                         0         0       0        0         0
nii-s65-interpretation.l4                      0         0       0        0         0
nii-s66-entitlement.l4                         0         0       0        0         0
nii-s67-count-of-children.l4                   0         0       0        0         0
nii-s68-amount.l4                              0         0       0        0         0
TOTAL (10 modules)                             0       117       0        0
```

`check.sh` exit 0.
The tests module has 117 `#ASSERT` directives, of which 11 are `#ASSERT REFUSED`; all 117 are satisfied, and no failure or refusal is expected.
(`l4 run` prints each result twice, so a raw grep finds 234 `assertion satisfied` lines; `check.sh` counts only the diagnostic half.)
The rule modules carry no assertions of their own.
The tests module takes about 40 seconds to run: every child's count is recomputed for every person who is asked about.

To show the harness can fail, a scratch copy of the tests with four planted defects (three expected values altered, one assertion pointed at a day before 1 May 2015) reported 113 satisfied, 3 failed, 1 refused.
Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

Mechanical checks over every file, with the scripts in `tools/` (run them with `python3 -I`):
`tools/srcquote.py SOURCE FILE.l4…` regenerates every `-- src:N | …` comment from line N of the source file (regenerating left all ten modules byte-identical); `tools/hebcheck.py SOURCE FILE…` checks that every other run of Hebrew in the modules and the Markdown files occurs verbatim in the source.
Both pass.
Both scripts are copied from row IL-03; `hebcheck.py` has one change, stated in its header: it also skips lines tagged `-- ext:[TAG] |`, which quote a source other than the Law.
Those quotations were checked separately (section 7).

## 1. What is encoded and what is not

**Encoded:** s 66 in full; s 67(a) and (b) in full for the shapes of family the text describes, with a named refusal for each shape it does not; s 68(a), (b)(2), (b)(3) and (c) in full.
The definitions they read are encoded as far as they need: s 65(a) "מבוטח" (insured, both limbs), s 65(a) "ילד" (child, both limbs and the proviso), s 65(b) (a child out of Israel), s 1 "ילד" (stepchild, adopted child, married minors), and s 1 "הסכום הבסיסי" paragraph (2)(a)-(c) (which basic amount fixes the allowance for a child at each place in the count).

**Not encoded:** s 1's updating clause for the basic amount (row IL-04's s 1); s 69 (to whom paid), s 69A (several women), s 71 (a parent who died or ceased to be insured), s 72 (which months are paid), s 238 ("housewife"), s 381 and the rounding regulations; the Income Tax Ordinance s 121B (row IL-03); the Income Support Law; the Maintenance (Assurance of Payment) Law; the Family Allowance Regulations under s 65.
Each of these that feeds a provision in scope enters as an **input**, with its citation in the nouns module; s 69A and s 71, which displace or decide cases this row would otherwise answer, are **named refusals** consulted before s 67 answers.

**The figures.** The text prints the basic amounts only as their 2015 base (150, 188, 140).
The amounts in force on a day are an input to the rules; the National Insurance Institute's published table of them, 1 May 2015 to 2026, is a separate module (`nii-il06-published-figures.l4`) that says on its face it is not encoded law.
Figures that appear only in the consolidation's editorial notes are not encoded.

**The question answered.** For a family on a day: which persons are insured, which children are "children", in whose count each child is, and each person's monthly allowance and s 68(c) supplement at the basic amounts in force that day, **before rounding**.

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.
Totals: **26 encoded, 4 inert, 10 out-of-scope, 0 deferred** (40 rows).

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| s 65(a) chapeau | 800 | "in this Chapter" | encoded | scope of `nii-s65-interpretation.l4` (Chapter 4 only) |
| s 65(a) "מבוטח" (1) | 801-802 | insured under Chapter 11, except a s 238 housewife | encoded | `s 65 "insured" (1) — …` |
| s 65(a) "מבוטח" (2) | 803 | resident individual, not absent beyond a reasonable temporary absence, not insured under Chapter 11, except a s 238 housewife | encoded | `s 65 "insured" (2) — …`, `s 65 — insured` |
| s 65(a) "ילד" (1) | 804-805 | the child of an insured or formerly insured person | encoded | `s 65 "child" (1) — …`, `s 65 — one who was insured` |
| s 65(a) "ילד" (2) | 806 | a child the insured supported, as proven | encoded | `s 65 "child" (2) — …` |
| s 65(a) "ילד" proviso | 807 | in Israel and under 18; "father", "mother", "parent" construed accordingly | encoded | `s 65 — in Israel on`, `s 65 — under 18 on`, `s 65 — a parent for this Chapter, …` |
| s 65(a) note | 808 | Family Allowance Regulations 5720-1960 published | inert | comment; the regulations' period for (2) is not in the sources, and the proof under (2) is an input |
| s 65(b) | 809 | out of Israel for no more than three months is not abroad; the Institute may deem otherwise | encoded | `s 65(b) — the absence, as at …`, `s 65 — in Israel on` |
| s 66 | 813-814 | insured parent entitled for each child, except one with income chargeable to additional tax | encoded | `s 66 — entitled …`, `s 66 — an insured parent with income chargeable to additional tax` |
| s 67(a) | 817 | one count only | encoded (by construction, and as a rule the family answer consults) | `s 67(a) — no child is counted with more than one insured parent, in` |
| s 67(b) first limb | 818 | two parents: the insured father, unless the child is with the mother only | encoded | `s 67(b), first limb — …` |
| s 67(b) second limb | 818 | a natural parent and another parent, both insured: the one the child is with | encoded | `s 67(b), second limb — …` |
| s 67(b), the cases it does not answer | 818 | two parents of one sex; natural and other parent with both or neither; neither limb; three or more | encoded (as four named refusals) | `section 67(b) does not say …` |
| s 67, order of the count | — | "the first child", "the fourth child" (used by s 68 and s 1) | encoded (assumption, fork F4) | `s 67 — the count of children, in` |
| s 68 chapeau | 820 | the amount of the allowance | encoded | `nii-s68-amount.l4` |
| s 68(a) | 821 | the basic amount fixed for the child | encoded | `s 68 — the provision that fixes …`, `s 68 — the monthly allowance, before rounding, under` |
| s 68(b) chapeau | 822 | children born before 1 June 2003, fourth and later | encoded | `born before 1 June 2003:` |
| s 68(b)(1) | 823 | (deleted) | inert | comment |
| s 68(b)(2) | 824 | fourth child: (2)(a) amount × 2.24 | encoded | `section 68(b)(2), …` |
| s 68(b)(3) | 825 | fifth and later: (2)(a) amount × 2.36 | encoded | `section 68(b)(3), …` |
| s 68(c) | 826 | Income Support or maintenance payment, three or more children: 70% of (2)(c) for the third and the fourth | encoded | `s 68(c) applies to …`, `s 68(c) — the supplement, …` |
| s 68(d)-(יא) | 827-834 | (repealed) | inert | comment |
| s 68, a person's allowance | 813-826 | ss 66-68 composed for one person | encoded | `s 68 — the child allowance, in … of` |
| s 1 "ילד" | 170 | includes a stepchild and an adopted child; excludes a married boy or girl | encoded (as s 65 reads it, fork F1) | `the child is the person's child`, `s 1 — not a married boy or girl` |
| s 1 "הסכום הבסיסי" (2) chapeau | 186 | for the child allowance under Chapter 4 Mark B | encoded | `nii-s1-basic-amount.l4` |
| s 1 "הסכום הבסיסי" (2)(a) | 187 | first and fifth and later child: 150 | encoded | `paragraph (2)(a) fixes …`, `the amount printed in paragraph (2)(a)` |
| s 1 "הסכום הבסיסי" (2)(b) | 188 | second, third and fourth: 188 | encoded | same, and `the amount printed in paragraph (2)(b)` |
| s 1 "הסכום הבסיסי" (2)(c) | 189 | Income Support Law benefit or s 68(c) supplement: 140 | encoded (the s 68(c) use) | `the basic amount for a supplement under section 68(c), under` |
| s 1 "הסכום הבסיסי", the base figures | 187-189 | 150, 188, 140 | encoded (as the printed base; not used as the figure in force) | `the basic amounts printed in paragraph (2)` |
| s 1 "המוסד", "המינהלה" | 123, 125 | the Institute; its Administration | inert | used only to name whose determinations are inputs |
| s 1 "הסכום הבסיסי", updating clause chapeau and (3) | 192, 197 | child-allowance amounts updated each 1 January from 2015 by the index; not on 1 January 2025 | out-of-scope | s 1 is row IL-04's, and the update needs index readings this row does not hold; the Institute's published result is used instead, in a module marked not-law. Touched to say so, and to check that the 2025 row equals 2024's. |
| s 1 "הסכום הבסיסי" (1), (2א), (3); updating (1), (2), (4) | 176-185, 190-191, 193-196, 198-202 | basic amounts and updates for other benefits | out-of-scope | not read by ss 65-68; row IL-04 (s 1) and the benefit rows |
| s 69 | 836-840 | to whom the allowance is paid | out-of-scope | it says who receives the payment, not whether or how much; no rule here reaches it. Its default, payment to the mother, differs from s 67's count, which goes with the father: a reader should not take the count for the payee. |
| s 69A | 842-845 | an insured man with children by more than one woman | out-of-scope (declined by name where reached) | it applies "notwithstanding anything elsewhere in this Mark" and recasts the count; encoding it needs each woman's count and a proof by the mother, which are a unit of their own |
| s 71 | 850-851 | a parent who died or ceased to be insured | out-of-scope (declined by name where reached) | it pays "by virtue of" a parent who is no longer an insured parent, which this row's per-person answer cannot express |
| s 72 | 853-856 | the months for which the allowance is paid; seven days alive; three months after death | out-of-scope | this row answers a day; mapping days to paid months is s 72's job, and a reader asking about a month must apply it |
| s 238 "עקרת בית" | 2401 ff. | housewife (Chapter 11) | out-of-scope (input) | a status the Institute records under Chapter 11, outside this row |
| s 381 | 4168-4170 | rounding of amounts, by rules the Minister makes | out-of-scope | the rounding regulations of 5746-1985 are not in the sources; every amount here is before rounding, and the tests compare with the Institute's rounded figures only to within one shekel |
| Income Tax Ordinance s 121B | (ITO) | income chargeable to additional tax | out-of-scope (input) | decided under the Ordinance; row IL-03 encodes it; fork F5 on which tax year |
| Income Support Law; Maintenance (Assurance of Payment) Law 5732-1972 | — | the payments s 68(c) turns on | out-of-scope (inputs) | whether a person is paid either for the month is recorded by the Institute |

## 3. Assumptions

**A1. The period answered: days from 1 May 2015.**
s 29(a) of the Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Years 2015 and 2016), 5776-2015 (Sefer HaChukim 2511, 30.11.2015, p. 247) commences ss 1 and 68 "as worded in this Mark" on 1 May 2015.
That Law's s 28 substituted s 1 "הסכום הבסיסי" paragraph (2) and amended s 68(b) and (c); its paragraph (2) matches the deposited lines 186-189 word for word (checked by script, section 7).
The latest amendment tag on any of ss 65-68 in the deposited text is that Law's (תשע״ו־3, on s 68); s 65's last is תשס״ט־4 and s 66's תשע״ג־3; s 67 has none.
So the deposited text is the text in force from 1 May 2015, and a day before it is declined by name.
The identification of תשע״ו־3 with that Law is by counting the entries of the file's own list of amending Laws (line 7), confirmed by the Law's own contents (it amends ss 1, 68 and adds s 74B, as the deposited text's tags show).
Nothing in the sources ends the period; the figures are bounded separately (A3).

**A2. The day is an explicit input; `RULES EFFECTIVE DATE` is not used.**
For a monthly benefit the day asked about fixes, at once, the child's age, the facts about absence and payments, the text in force and the figures in force.
Taking it as a field of the case (`A family on a day`) keeps those together, and every dated arm (the period gate, the figures table) selects on it with its citation.

**A3. The Institute's table: each row applies from its date to the next row's.**
The table's date column is headed "from the day" and has rows for 1.05.2015 and then 1.01.2018-1.01.2026, with none for 2016 or 2017; 1 May 2015 to 31 December 2017 is therefore read as 150 / 188 / 140.
The table has no row from 1 January 2027, and the updating clause requires one, so days from 1 January 2027 are declined.

**A4. Figures found only in the consolidation's editorial notes are not encoded.**
The notes at lines 187-189 give the 2024-2026 amounts; they agree with the Institute's table, which is what the encoding cites.

**A5. Classifications outside the slice are inputs.**
Chapter 11 insurance; the s 238 housewife; residence, and the authorised employee's view of an absence; formerly insured (died or ceased); income chargeable to additional tax; payment of an Income Support benefit or a maintenance payment for the month; children by more than one woman (for the s 69A gate); how a person stands to a child, and whether the child is with them; the authorised person's satisfaction that an insured person supported a child; a child's marriage, absence from Israel, and the Institute's decision under s 65(b).

**A6. Amounts are before rounding, per month.**
s 381 leaves rounding to rules the Minister makes, which are not in the sources.

**A7. A person's answer is for the count s 67 gives that person.**
Each person in the family gets one answer; a person with no child in the count and entitled under s 66 gets an allowance with no lines (0 shekels).

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | s 65(a) "ילד" (1), line 805; s 1 "ילד", line 170 | Does "his child" in s 65 carry s 1's extension (stepchild, adopted child) and exclusion (married boy or girl)? | (i) yes: s 65 defines which children count for the Chapter but uses "child" within its own definition, which can only mean the Law's general sense; (ii) no: s 65 displaces s 1, so a stepchild counts only under (2) on proof of support, and a married minor is a child | **(i)**. Reading (ii) makes s 65's own definition circular, and the extension to stepchildren is in the Law's own general definition. A test asserts the married-minor exclusion. |
| F2 | s 65(a) proviso, line 807; s 65(b), line 809 | Date arithmetic where the calendar has no corresponding day: an 18th birthday for a 29 February birth; three months from 30 November. | (i) clamp to the last day of the shorter month (28 February); (ii) roll into the next month (1 March, 2 March) | **(i)**, `add years` / `add months`. The text says nothing; the clamp is the conservative choice for both (the child stops being a child, and an absence stops being short, no later than the rolled date). Each changes the answer on one or two days. Tests sit on both. |
| F3 | s 65(b), line 809 | "left Israel for a period not exceeding three months", for an absence that has not ended on the day asked. | (i) measure from the day of leaving to the day asked; (ii) the intended length of the trip; (iii) the actual length, known only afterwards | **(i)** where no return day is supplied; a caller who knows the return day (past or planned) supplies it and the full period is measured. |
| F4 | s 68(a)-(c), s 1 (2), lines 187-188, 821-826 | How is the count ordered: which child is "the first", "the fourth"? | (i) by date of birth, eldest first; (ii) by the order children entered the count | **(i)**, children born the same day keeping the order of the family's list. The Institute's page computes the allowance "according to the number of children in the family, the children's dates of birth" and lists amounts by the child's "place in the family"; that supports (i) but is practice, not text. Only s 68(b) and the s 68(c) supplement's attribution depend on it; totals without (b) do not. |
| F5 | s 66, line 814 | "has income chargeable to additional tax": for which tax year? | (i) the tax year in which the month falls; (ii) the last assessed year | **not decided**: the input is the caller's answer for the day asked. |
| F6 | ss 66 and 67(b), lines 814, 818 | Is a child whose insured father has income chargeable to additional tax still in the father's count? | (i) yes: s 66 keeps him "an insured parent", and s 67(b) counts with "the insured father", so the child is in his count and no allowance is paid for it; (ii) no: a parent excluded from the allowance is not a candidate, and the child goes to the other insured parent | **(i)**, the literal reading; it can deny a family the allowance although the mother has no such income. Tests assert it, labelled. Open question 1. |
| F7 | s 67(b), line 818 | Only one of the child's parents is insured. | (i) that parent's count, wherever the child is; (ii) the first limb literally: with "the insured father" unless with the mother only, so a child with an uninsured mother only is in no count | **(i)**: s 67 chooses among insured parents, and with one there is nothing to choose. |
| F8 | s 67(b), line 818 | What are "two parents" (first limb) and "a natural parent and another parent" (second limb)? | (i) first limb: the child's own parents, natural or adoptive; second: a natural parent and a step-parent or a person who supported the child; (ii) second limb: a natural parent and any parent who is not natural, adoptive included | **(i)**: an adopter is the child's parent in every respect, and reading adoption into the second limb would send a child of a stepparent adoption to whichever parent it is "with", which it is with both. |
| F9 | s 67(b) second limb, line 818 | A natural parent and another parent, both insured, and the child is with both of them (or with neither). | (i) the text does not say: declined; (ii) fall back on the first limb (the father, unless with the mother only) | **(i)**, a named refusal. This is the common blended family, so the refusal is reached often. Open question 3. |
| F10 | s 67(b) first limb, line 818 | Two insured parents who are both fathers or both mothers. | (i) the text, which names "the father" and "the mother", does not say: declined; (ii) the Institute's practice, stated on its page "to whom is the allowance paid?", that a same-sex couple living together may receive one allowance for all their common children | **(i)**, a named refusal. The Institute's practice is noted, not encoded. |
| F11 | s 67(b), line 818 | Three or more insured parents; or two who fit neither limb (a step-parent and a supporter, an adopter and a step-parent). | — | **declined**, two named refusals. |
| F12 | s 67(b) first limb, line 818 | "unless he is with the mother only". | — | with the mother and not with the father; a third person the child is also with (a step-parent, say) does not matter. |
| F13 | s 69A, line 843 | "ילדים ממספר נשים": children by more than one woman, or by more than one wife? | (i) women; (ii) wives | **(i) for the refusal gate only**: s 69A is not encoded, and the wider reading declines every case it might reach. |
| F14 | s 68(c), line 826 | The parent paid Income Support is not the parent in whose count the children are. | (i) no supplement: (c) speaks of a parent paid the benefit "and entitled … for three or more children"; (ii) the supplement attaches to the family | **(i)**, literal. A test asserts it, labelled. |
| F15 | s 65(a) "ילד" (2), line 806 | Must the supporter be insured, or may they have been insured? | — | insured: "the insured supported him". A person who is a parent only under (2) is therefore always an insured parent. |
| F16 | s 65(a) "מבוטח" (2), line 803 | The absence limb has three parts: temporary, reasonable in the authorised employee's opinion, and not contradicting the claim of residence. | — | one input, `absent from Israel beyond a reasonable temporary absence`, which is the authorised employee's determination on all three. |
| F17 | s 68(c), line 826 | "entitled … for three or more children": counted how? | — | the number of children in the parent's count, children under s 68(b) included. |

Places where no fork was found, read for one and listed so a reviewer can disagree: s 68(b)'s "born before 1 June 2003" (strict: a child born on 1 June is not before it; the Institute's own heading "born until 31 May 2003" agrees, and a test sits on both days); "has not reached 18" (a child on the day before the 18th birthday, not on it); s 68(c)'s "the third child and the fourth child" (a parent with three children gets one supplement, with four or more two).

## 5. Answer table

Basic amounts from the Institute's table [nii-basic]; the amounts by place are s 68 applied to them, before rounding.
"(b)" columns are for a child born before 1 June 2003; every such child reached 18 by 31 May 2021, so they cannot arise later.
In brackets, the Institute's own per-child page where one was fetched [nii-rates-YYYY].

| from | (2)(a) | (2)(b) | (2)(c) | 1st | 2nd-4th | 5th+ | 4th, (b)(2) | 5th+, (b)(3) | s 68(c) supplement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 May 2015 | 150 | 188 | 140 | 150 | 188 | 150 | 336 | 354 | 98 |
| 1 Jan 2018 | 150 | 189 | 140 | 150 [150] | 189 [189] | 150 [150] | 336 [336] | 354 [354] | 98 [98] |
| 1 Jan 2019 | 152 | 191 | 142 | 152 | 191 | 152 | 340.48 | 358.72 | 99.4 |
| 1 Jan 2020 | 152 | 192 | 142 | 152 [152] | 192 [192] | 152 [152] | 340.48 [340] | 358.72 [359] | 99.4 [99] |
| 1 Jan 2021 | 152 | 192 | 142 | 152 | 192 | 152 | 340.48 (to 30 May) | 358.72 (to 30 May) | 99.4 |
| 1 Jan 2022 | 156 | 197 | 145 | 156 | 197 | 156 | — | — | 101.5 |
| 1 Jan 2023 | 164 | 207 | 153 | 164 | 207 | 164 | — | — | 107.1 |
| 1 Jan 2024 | 169 | 214 | 158 | 169 [169] | 214 [214] | 169 [169] | — | — | 110.6 [111] |
| 1 Jan 2025 | 169 | 214 | 158 | 169 [169] | 214 [214] | 169 [169] | — | — | 110.6 [111] |
| 1 Jan 2026 | 173 | 219 | 162 | 173 [173] | 219 [219] | 173 [173] | — | — | 113.4 [113] |
| 1 Jan 2027 | declined | declined | declined | | | | | | |
| before 1 May 2015 | declined | | | | | | | | |

A family's monthly total in 2026, with no child under s 68(b) and no supplement: 1 child 173; 2 children 392; 3 children 611; 4 children 830; 5 children 1,003; 6 children 1,176; each further child 173.
With the s 68(c) supplement: 3 children 724.4; 4 or more, 226.8 above the figure without it.

## 6. Nouns to reconcile at IL-07

Read from the sibling deposits (read-only) near the end of this session; nothing here depends on them and nothing in them was changed.

- **The person.** This row: `A person` (Chapter 11 insurance, s 238 housewife, residence and absence, formerly insured, additional-tax income, Income Support and maintenance payments, children by more than one woman). IL-04: `A person who works` (employment relationship, the family-member limb of "employee", wage fixed by Law) and `A person's occupation in a period` (the self-employed limbs). One insured-person record could carry both. IL-04's own notes record that its s 335(b) and (i) turn on s 65(a)(1) "insured", which this row encodes as `s 65 "insured" (1) — insured under Chapter 11, other than a housewife`.
- **s 1.** IL-04 encodes several s 1 definitions (`nii-s1-definitions.l4`: "employee", "self-employed person", "the average wage"); this row encodes "ילד" and "הסכום הבסיסי" paragraph (2) (`nii-s1-basic-amount.l4`). They should become one s 1 module; IL-04's notes leave both definitions to this row.
- **Published figures.** Both rows keep a module of figures the Institute publishes (`nii-il04-published-figures.l4`, `nii-il06-published-figures.l4`). They cite different pages; one module, one provenance format.
- **Income chargeable to additional tax.** This row takes it as a BOOLEAN input; row IL-03 (Income Tax Ordinance) computes s 121B's additional tax for a tax year. IL-07 can join them as "chargeable iff the IL-03 additional tax for the tax year is above 0", once fork F5 (which tax year) is settled.
- **The tax year / the day.** IL-03 selects on the tax year; this row on a day. A day falls in exactly one tax year, so the join is mechanical.

## 7. Sources: what was fetched, and how quotations were checked

The deposited Law (sha256 `78bf47ee…552a97`) was verified on 2026-10-06 before use.
Fetched on 2026-10-06 (all fetched bytes were kept only in the session's scratch directory, and are cited here by sha256):

- **[nii-basic]** The Institute's page "the basic amount for computing benefits", fetched directly at 14:10 UTC: `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%D7%94%D7%A1%D7%9B%D7%95%D7%9D%20%D7%94%D7%91%D7%A1%D7%99%D7%A1%D7%99%20%D7%9C%D7%97%D7%99%D7%A9%D7%95%D7%91%20%D7%A7%D7%A6%D7%91%D7%90%D7%95%D7%AA.aspx`, 193,110 bytes, sha256 `d19985509135d947b3c34c0c1c462913adeddf5c9c86509ff4fccf2810994139`.
- **[nii-rates-2026]** The Institute's page of child-allowance amounts, fetched directly at 14:08 UTC: `https://www.btl.gov.il/benefits/children/Pages/%d7%a9%d7%99%d7%a2%d7%95%d7%a8%d7%99%20%d7%94%d7%a7%d7%a6%d7%91%d7%94.aspx`, sha256 `0bf54039e27ec719e1ec190d00e20012d26f88290e9ed2f5a6a4f503c1b4359c`.
- **[nii-rates-2025, -2024, -2020, -2018]** The same page as captured by the Internet Archive, fetched in the raw (`id_`) form: capture `20250420005113`, sha256 `3985123f0d5dfc54d3bd5ef971b23f9ecd59a6f47dd79990ac383ed70b024e64`; `20240806061702`, sha256 `0c7083ccd45f7eb327c3eda843c83b69f8431a5782262a7a8b6aa0fa798632f6`; `20200821105458`, sha256 `36b09fd990aec92110dc64e174edca48fbada24bcb895307d13bec84fc65d93c`; `20181003161656`, sha256 `3a7c5f6f347e48cebd7e199d94d987c0b34419021e4d59c1f1267a81dc5cdb09`.
- **[sh-5776-247]** The Economic Efficiency Law 5776-2015, Sefer HaChukim 2511: a direct fetch of `fs.knesset.gov.il/20/law/20_lsr_316719.pdf` returned a 131,618-byte HTML "Unavailable" page, so the PDF was fetched as Internet Archive capture `20151217003808` (raw form): 44 pp., sha256 `6c99d23c7d2521bd8691d5cc7b62c43eca6d76fec27f8ee0d2958dfee9c50797`.
  Later the same day (14:50 UTC) the same URL, `https://fs.knesset.gov.il/20/law/20_lsr_316719.pdf`, was fetched directly from the Knesset **through the lead's Israeli-IP SOCKS proxy** (an ssh tunnel to an EC2 instance): HTTP 200, `application/pdf`, 434,026 bytes, the same sha256. The Internet Archive copy is byte-identical to the Knesset's.
- Two further Institute pages were read for context and are not relied on for any figure: "eligibility conditions" (`…/benefits/children/Pages/%d7%aa%d7%a0%d7%90%d7%99%20%d7%96%d7%9b%d7%90%d7%95%d7%aa.aspx`, sha256 `bc15afbc4958c3d58e2c679d02067e1f661ed1ec359de4a105292974a98f7966`) and "to whom is the allowance paid?" (`…/benefits/children/Pages/%d7%9c%d7%9e%d7%99%20%d7%9e%d7%a9%d7%95%d7%9c%d7%9e%d7%aa%20%d7%94%d7%a7%d7%a6%d7%91%d7%94.aspx`, sha256 `fc7e745bcb94b1606edbb6fb30d8d6398d86124760ef94670956f6bcab245760`), the second for the same-sex practice noted at F10.

**Quotations from sources other than the Law** are on lines tagged `-- ext:[TAG] |`.
Each `[nii-…]` quotation was checked by script to occur in the text extracted from the page it cites (whitespace and direction marks normalised): ten quotations, all found.
The one `[sh-5776-247]` quotation (s 29(a) of the 5776 Law) was rebuilt from the PDF's text layer, whose lines are stored in visual order, by reversing each line's word order; its 19 Hebrew words were checked by script to occur contiguously in that layer, and its digits and punctuation by eye against page 31 rendered as an image.
The claim in A1 that s 1 paragraph (2) is word for word the 5776 Law's was checked the same way: the Hebrew words of each of lines 186-189 (editorial notes removed) occur contiguously in pages 28-31 of the PDF's text layer.

**Not read, under the semi-cleanroom ruling of 2026-10-06:** nothing from the Axiom Foundation, any RuleSpec repository, `.axiom/` directory or the other paths the brief lists was read, searched or fetched in this session, and no web search was made for encodings of Israeli social-insurance law.

## 8. Open questions for a domain expert

1. F6: when an insured father has income chargeable to additional tax, does the Institute count the children with him (so no allowance is paid for them), or with an insured mother who has no such income?
2. F7: with one insured parent and a child who lives only with the other, uninsured, parent, is the child in the insured parent's count?
3. F9: for a child living with a natural parent and an insured step-parent together, in whose count is the child? Does the Institute apply the first limb (the father) by default?
4. F10: what is the legal basis of the Institute's practice for same-sex parents, and in whose count are the children?
5. F4: does the Institute order the count by date of birth, eldest first, and does the order change when the eldest reaches 18?
6. F5: which tax year's additional-tax liability excludes a parent in a given month?
7. F14: when one parent is paid Income Support and the children are counted with the other, is the s 68(c) supplement paid?
8. The Institute's page lists old-age and survivors' pensioners with an income supplement among those who receive the s 68(c) supplement. Is that supplement "a benefit under the Income Support Law" within s 68(c)?
9. F2: how are a 29 February birthday and a three-month period from the 30th or 31st of a month computed?
10. F13: in s 69A, is "נשים" women or wives?

## 9. What was not done

- **The independent test pass** (skill step 8) was not run: the brief for this row is one session with no sub-agents. Every expected value was worked by hand from the text or from an Institute page before it was asserted, but no second reader has derived them.
- **HG1**, a human who knows Israeli social-security law reading the modules against the Hebrew, has not been sought.
- **s 69A and s 71** are reachable and declined; encoding them is the obvious next unit, and the refusals mark exactly where they would plug in.
- **Performance.** The tests module takes about 40 seconds; the count of every child is recomputed for each person. Nothing here depends on that, but a deployment would want the counts computed once.
