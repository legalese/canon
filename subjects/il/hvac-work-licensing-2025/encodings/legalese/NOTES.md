# NOTES — il/hvac-work-licensing-2025, encoding row `legalese`

**Status: `draft`.** Deposited 2026-09-21 on the drafts shelf. Not reviewed by anyone who knows Israeli vocational-licensing law (HG1 not sought).
An adversarial model review against the Hebrew text was run before deposit; section 5 records what it found and what was done about it.

## 1. What this is

Two instruments, one encoding row:

- **The Law.** חוק הסדרת העיסוק בעבודה במערכת קירור או מיזוג אוויר, התשפ״ה–2025, Sefer HaChukim 3349 p. 182, published 14 January 2025.
  A licensing statute: three licence grades by cooling output, a registrar, exam-and-training conditions, five-year licences, temporary licences for foreign experts, inspectors, and administrative sanctions.
  `hvac-law.l4` encodes the parts the Fees Regulations lean on: ss.2, 3, 6 (with the whole Second Schedule), 7, 8, 9, 16, 17, 63.
- **The Fees Regulations.** תקנות הסדרת העיסוק בעבודה במערכת קירור או מיזוג אוויר (אגרות), התשפ״ה–2025, Kovetz HaTakanot 2116, signed 6 July 2025, published 9 July, in force 16 July 2025, amended by Kovetz HaTakanot 2062 (5786).
  `hvac-fees.l4` encodes regs 1-5 in full, with reg. 2 in **three vintages** (section 3 below).

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

## 3. Draft, as made, as amended

| item | the SimpLEX draft (Fig. 4) | as made, KT 2116 (16 Jul 2025) | as amended, KT 2062 (5786) |
| --- | --- | --- | --- |
| theoretical examination | 273 | **no fee** | 158 (new reg. 2(a1)) |
| practical examination | 194 | 194 | 194 |
| appeal, 40 NIS per appeal | theoretical **or practical** | theoretical only, "in addition to the fee under (a1)" | same |
| licence issue or renewal, s.5 | 284 | 284 | 284 |
| temporary licence for a foreign expert | 398, citing **"s.8 of the Law"** | 398, citing s.9 | same |
| preamble | after consulting the Finance Minister, s.39 Budget Foundations Law | with the Finance Minister's approval, s.39B; ss.59 **and 60** | same |
| reg. 3 indexation, reg. 4 payment precondition | present | same | same |

Three consequences the encoding makes explicit:

1. Under the Regulations as made, the theoretical examination had no fee, so reg. 4 had nothing to withhold and scenario 8's candidate is admitted to it. `#ASSERT the service may be provided the Regulations as made theoretical examination 0` is satisfied.
2. As made, reg. 2(b) charged an appeal fee "in addition to the fee under subregulation (a1)" while no (a1) existed. The cross-reference dangled for ten months until the amendment supplied it.
3. The draft's "s.8 of the Law" for the foreign-expert licence is wrong against both the bill as tabled for second and third reading and the Act; s.8 is validity and renewal. The screenshot's worked example likewise cites "s.9 of the Law" for eligibility to sit the examination, which no section of the Act provides. Both would be caught by a check that resolves citations against the parent Act, which is the "legality check" panel SimpLEX itself shows.

`hvac-tests-simplex-red.l4` is **meant to fail** on exactly three of five rows (5, 7 practical, 8 theoretical); `check.sh` counts them and reports a wrong count as a failure. It is also the positive control: proof that this harness can go red.

## 4. Forks (interpretive choices)

- **F1, s.8 validity.** "תוקפו של רישיון יהיה לחמש שנים או עד 31 במרץ של השנה החמישית מהשנה שבה ניתן הרישיון, לפי המוקדם."
  Read as: the fifth year *from* the grant year is grant year + 5, so a licence granted 2025-09-01 expires 2030-03-31 and one granted 2025-01-15 expires 2030-01-15.
  The alternative, counting the grant year as the first, gives grant year + 4 (2029-03-31 for the September grant), which would make the "five years" limb nearly dead letter. The adopted reading keeps both limbs live. A drafter or the registrar's practice would settle it in a sentence.
- **F2, reg. 3 rounding.** "יעוגל לשקל החדש השלם הקרוב" says nearest and is silent at exactly one half. Half-up adopted (`FLOOR (x PLUS 0.5)`). Only matters when fee × index ratio lands on .5 exactly; the generated tests include such cases so the choice is visible.
- **F3, the draft vintage.** Transcribed from a published screenshot, not from a deposited draft. Fee amounts and the appeal wording are legible; the preamble is legible; item lettering (a)-(e) is as shown. The tazkirim.gov.il consultation page for the draft exists but is a JavaScript application that could not be fetched headlessly, so the transcription was not cross-checked against it.
- **s.6(a)(3)** (unfit by reason of a conviction "in the registrar's opinion") and **s.9(a)(3)** (recognised by the registrar as of repute) are discretionary; both are inputs, not decided.
- **s.3(b)** exemptions by ministerial order are an input; no order has been located.

## 5. Review findings

_Filled in after the adversarial review; see the commit that lands it._

## 6. Multilingual design

The module body is English (`@lang en`), because English is the working language of the people this was built for tomorrow; every rule carries an English `@nlg` herald and a Hebrew `@nlg:he` herald.
`l4 nlg --lang he` and `l4 render --lang he --format html` therefore produce a Hebrew document from the same source; the four renderings are in `projections/`.

Two limits of the current tooling, observed on the l4-ide `unstable` binary of 2026-09-19:

- `%name%` placeholders in a herald are rendered as the bare parameter name followed by "with <arguments>", not substituted inline. `ok/nlg-module-lang.l4`'s own golden shows the same, so the heralds here are written to read acceptably either way.
- `§` section titles are not language-tagged, so the Hebrew rendering carries English headings. A Hebrew-canonical twin row (Hebrew identifiers and headings, English `@nlg:en` heralds, the same test files) would fix that and is cheap, since identifiers take Hebrew directly; it is not deposited.

## 7. What is not here

- Chapter F (administrative enforcement) and the Third Schedule (sanction amounts): out of scope by decision.
- The First Schedule (which works each grade may do) and the Fourth Schedule (flammable refrigerants): the grade thresholds are encoded, the work lists are not.
- ss.10-15 (refusal, cancellation, suspension; registry; non-transfer; standards; presenting the licence; reporting) and s.18 (operators).
- No `EVAL UNDER RULES EFFECTIVE AT` law-time axis: the three vintages are an explicit enum, because the draft was never in force and has no effective date.
- No `cases/`, `report/` or `gates/`; no fork register file beyond section 4 here.
- Goldens: none. The modules are outside l4-ide's corpus globs; `check.sh` is the guard, and it is not run by any CI.

## 8. How to run

```
sh check.sh                      # binary and prelude from the worktree named inside it
HVAC_L4=/path/to/l4 HVAC_LIBS=/path/to/jl4-core/libraries sh check.sh
l4 nlg hvac-fees.l4              # English
l4 nlg --lang he hvac-fees.l4    # Hebrew
l4 render --lang he --format html hvac-law.l4 > projections/hvac-law.he.html
python3 ../../source/gen-tests.py   # regenerates hvac-tests-generated.l4
```

The binary must be at or after l4-ide `unstable` PR #432 (2026-09-19) for `--lang`.
