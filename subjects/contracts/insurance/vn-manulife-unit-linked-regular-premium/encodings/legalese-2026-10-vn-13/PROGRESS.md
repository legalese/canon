# PROGRESS — VN-13 (enc-vn-13)

State on disk, for a resumed session. Read BRIEF.md first, then this.

## How the .l4 files are made

- Templates live in `scratchpad/enc-vn-13/tpl/vn13-*.l4` (scratchpad = `~/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad`).
- `scratchpad/enc-vn-13/build13.sh` expands every template into DEPOSIT: `{{src:N-M}}` lines become `-- src:N | …` via `tools/vnsrc.py quote`; `{{gen:MODE}}` lines become the output of `tools/gen_tables.py RAW MODE` (charge-table, charge-tests, equity-bands, equity-tests).
- EDIT THE TEMPLATES, then run build13.sh. Editing a DEPOSIT .l4 directly is lost at the next build.
- `scratchpad/enc-vn-13/l4err.sh check|run FILE` prints error diagnostics only; `l4sum13.sh FILE OUT` prints counts.
- If the scratch directory is lost, the DEPOSIT .l4 files are the truth: edit them directly and stop using the build.

## Done

- Modules (all typecheck): vn13-nouns, vn13-art01-02-definitions, vn13-art03-benefits, vn13-art04-08-conditions, vn13-art09-10-premiums, vn13-art11-12-funds, vn13-art13-charges, vn13-art14-20-general, vn13-annex1-funds, vn13-annex2-procedures, vn13-fixtures.
- vn13-tests-cover.l4: last run 145 #ASSERT, 145 satisfied, 0 failed, 0 refused, 0 errors (6 #TRACE, results as intended).
- tools/gen_tables.py (tables generated from the raw text).

- vn13-tests-mechanics.l4: 191/191 satisfied (before the 9.4 year gate was added; 2 asserts added since).
- vn13-findings.l4 written and typechecks (Findings 1-11 evidence).
- 9.4 grace rule now gated on policy year >= 2; year 1 shortfall REFUSEs (finding 4).

## In progress

- check.sh over all modules (output in scratchpad/enc-vn-13/check1.out).
- DONE: GLOSSARY.md, COMPARABLES.md, NOTES.md (sections 6 and 7 hold placeholders TOTALS_PLACEHOLDER / VNSRC_PLACEHOLDER to fill from check.sh and vnsrc).
- DONE: encoding.json, SOURCE-LICENSE.md (782 src lines, 770 distinct).
- DONE: check.sh TOTAL (14 modules) 0 / 358 / 0 / 0, exit 0 (2026-10-07); vnsrc gate 782 src lines, 0 problems; NOTES 6-7 and encoding.json filled.
- TODO: final report to team-lead.

## L4 traps met (for NOTES §0)

- `f x 5%` applies `%` to the whole application `(f x 5)%`: parenthesise every percent argument.
- A one-argument mixfix may not end with a keyword segment (renamed 4 rules).
- `(expr)'s field` does not parse inside a directive; use a helper.

## Remaining, in order

1. Fix mechanics tests; run; every failure is a finding, never edit an expected value.
2. vn13-findings.l4: evidence for the findings (alternative readings + #EVAL/#ASSERT).
3. check.sh over everything; record TOTAL.
4. NOTES.md (§0-§8), GLOSSARY.md, COMPARABLES.md, encoding.json, SOURCE-LICENSE.md.
5. vnsrc gate: `python3 -I tools/vnsrc.py check ../../source/raw/manulife-maxx.txt *.l4` plus every .md except BRIEF.md.
6. Final report to team-lead.

## Decisions and forks so far (to go in NOTES.md §3)

- Counting: "N days/years from X" counted from the next day, last day = the corresponding date (X+21; X+60; add years X 2), calendar units.
- Next Valuation Date = strictly after (valuation list; REFUSE when none supplied).
- Paid-to date taken as an input; annualised premium = instalment × instalments a year.
- 3.3: "end of 15th anniversary year" = 15th anniversary of Effective Date.
- 3.2(i): offence of the Life Insured only (literal: anyone's → murder victim excluded; finding).
- Order in death claim: in force → Art 18 time → Art 7 → Art 6 → Art 8 → 3.2 → 3.1 (less 9.4 grace charges).
- Premium debt deducted twice in 3.1 and 3.2, encoded as written (finding).
- Art 6: insurable ages = 18-65 at issue; two years from Effective Date to discovery; contract ends on discovery.
- Art 7: barred if decision after 2nd anniversary of issue/latest reinstatement AND insured alive then; no intent required (LAW Art 22(2) fork).
- Art 8 two years from later of issue/reinstatement (LAW Art 40(1)(a) counts from first premium).
- 9.1/9.4: payment on due date is on time; lapse date = due + 61; year 2+ no grace from missed premium.
- 9.4 year 2+: 60 days from the determination that opened the grace (literal "most recent" never ends: finding).
- 9.3 riders end without notice in year 2+: REFUSE; resumed premium: REFUSE.
- 9.5 a first-year lapse payout is not "surrender for SV".
- 11.2 weekly = no gap > 7 days; 11.4/11.7 notice at least 3 days; 11.4 failing request → REFUSE (Annex 2 has no procedure).
- 13 charge change needs notice ≥ 3 months AND written agreement; 13.9 c/e year-on-year 115%; f = max; "2.5%" = 0.025.
- 17.2 20% minimum applies to each fund named, not every fund.
- 18: time bar 1 year from event (+force majeure days; discovery only for the Policyholder); late claim barred; interest after 2 months at the Company's rate (REFUSE).
- 20(iv): age-99 anniversary; SV valued then (first valuation on/after it).
- Annex 1 3.7: 15% read relative (10% → 11.5%); not applied to 3.6.
- Annex 2 A: 8:30-15:00 inclusive same day; after 15:00 next working day; else REFUSE; pending → REFUSE.
- Annex 2 F: written always; evidence + extra premium for increase; approved after/on paid-to date → REFUSE.

## Incident

- 2026-10-06 22:51: a shared-scratchpad name clash (my build.sh calling another encoder's expand.py) overwrote enc-vn-11's two templates in scratchpad/tpl/. Reported to enc-vn-11 and team-lead. My files now live only in scratchpad/enc-vn-13/.
