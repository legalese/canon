# PROGRESS — row VN-26 (enc-vn-26)

State on disk, in case the session is killed.
If resumed: read BRIEF.md, this file, then re-run `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.

## Key decision (approved by the lead)

The PDF holds BOTH the 2-page summary notes (src 1-97) and the full 22-page Rules and Terms (src 98-1103).
Both layers are encoded, kept apart: `pru-notes.l4` is "from the summary notes"; every other rules module is "from the Rules and Terms".
NOTES.md must say the brief described the file as notes-only and that this was wrong.
COMPARABLES.md draws on the R&T with its lines, marking values found only in the notes.

## Done (typecheck clean, `l4 check` exit 0)

- `pru-nouns.l4` — DECLARE only.
- `pru-annex.l4` — payout-rate table, one WHEN per row; fracture grouping read from page image p.24 (`[page-read p.24]`).
- `pru-general.l4` — Part I, Articles 1-7.
- `pru-exclusions.l4` — Article 11.
- `pru-benefits.l4` — Article 8 (8.1-8.10), with @export on entry points.
- `pru-claims.l4` — Articles 9, 10.
- `pru-contract.l4` — Articles 12-17.
- `pru-notes.l4` — notes items 1-4 (written; placeholders not yet expanded/checked at time of writing).

## How src lines are made

Write `--@SRC N [M]` placeholder lines, then run
`python3 -I <scratch>/tools/expand.py ../../source/raw/prudential-notes.txt FILE.l4`
(scratch = `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn26/`).
It writes `-- src:K | <line K>` exactly as `tools/vnsrc.py quote` does.

## Status (2026-10-07): COMPLETE

All deliverables exist. check.sh: TOTAL (12 modules) 0 errors, 293 satisfied, 0 failed, 0 refused; exit 0.
vnsrc gate (all .l4 and .md except BRIEF.md): `vnsrc check: 525 src: lines, 373 Vietnamese runs, 0 problems`.
Final report sent to the lead. Forks and findings: see NOTES.md sections 3 and 4 (the lists below are the working notes they came from).

## Forks so far (numbering used in module comments)

- F-01 days are calendar days, counted from the day after; "within N days of X" = on or before X+N.
- F-02 term end = earlier of chosen anniversary and anniversary on/after the 70th birthday.
- F-03 8.1 "in force" attaches to the death, not only the accident.
- F-04 annex section 3 grouping from the page image (legs 30%, arms 15%).
- F-05 "one or more" fracture rows paid once per Accident; other rows per bone.
- F-06 burns: first matching row in table order (= highest).
- F-07 burns: "phỏng độ 2" counts second-degree area only.
- F-15 Article 11.3 carves the several-beneficiaries case out of 11.1(f).
- F-16 11.3: the whole benefit is shared among the innocent beneficiaries pro rata.
- F-17 debts deducted once from the total paid, not per benefit.
- F-18 Article 9 "ngay khi đủ 18 tuổi" read as on the 18th birthday.
- F-19 Article 10.4 documents: (a) and (b) and one of (c), (d), (e).
- F-21 Article 10.8 "thứ tự ưu tiên": the first limb that yields a recipient.
- F-22 notes "hoặc và" read as the lesser of.
- Also: Article 5 deductions apply after the max; 11.2 has no 180-day limit and is checked before 8.1's 180 days; 8.6 in-force via 12.1(h).

## Findings so far (to write up)

F-01 accidental death after day 180: no Article pays (8.1 needs 180 days; 8.7 needs non-accidental), while an excluded accidental death gets 11.2.
F-02 permanent injury paid to the maximum ends the contract, so a later death from the same accident gets no 8.1 benefit.
F-03 accidental blindness with eyeballs intact, and accidental paralysis/81% loss of capacity: in no table row (8.2), and 8.8 only covers non-accidental disability.
F-04 fingers: thumb 15 + 4x5 = 35% > "all fingers of one hand" 25%.
F-05 fracture/burn cap for under-6 is 50% SA uncapped in VND: above SA 500m a toddler's cap exceeds a teenager's, above 1bn an adult's.
F-06 ankle (15%) overlaps tibia/fibula (leg bones, 30%).
F-07 burn rows overlap; kidney 5% each and both kidneys 10%.
F-08 10.5 docs within 60 days of the Accident; 8.6 transfer can come later.
F-09 Article 3 silent on non-accidental death during temporary cover (REFUSE); temporary-cover exclusions differ from 11.1 (war not excluded).
F-10 notes item 1: three options, no criteria; 12.2(a) gives criteria; LAW Art 22(2) requires premium refund, 12.2(a) refuses it.
F-11 notes exclusions: "related to", all benefits, crime without authority finding; suicide excluded in notes but 8.7 pays.
F-12 notes caps: fracture/burn without age bands; ambulance without 1m per Accident.
F-13 10.8: sole predeceased beneficiary (individual policyholder) — no recipient; organisation policy: the insured never receives.
F-14 discretion without criteria: Art 9, 12.2(d), 12.1(b) minimums, 12.1(e)-(g) approval with no time, 10.7.
F-15 Article 6 incontestability never protects against cancellation (material misstatements always contestable).
F-16 reinstatement requested in time can be defeated by Prudential's own delay (Art 16, 24 months).
F-20 notes are not among the contract documents of 2.1.
LAW forks: Art 22(2) refund; Art 30 time-bar knowledge/force majeure; Art 37(4) automatic premium loan; Art 40(3) excluded injury; Art 41(3) beneficiary change must be confirmed by the insurer; Art 24 contra proferentem; Art 28(1) assignment consent. Law aid ends at Art 130; commencement/transitional articles not in it.

## Tests written

- `pru-fixtures.l4` (named cases, no directives).
- `pru-tests-annex.l4` generated: 50 satisfied.
- `pru-tests.l4`: 189 #ASSERT, all satisfied (l4 run, 2026-10-07); 7 #TRACE behave as intended.
- Next: `pru-tests-findings.l4` (evidence for findings, notes vs R&T).

## Last check.sh totals

2026-10-07: TOTAL (12 modules) 0 errors, 293 satisfied, 0 failed, 0 refused; exit 0.
