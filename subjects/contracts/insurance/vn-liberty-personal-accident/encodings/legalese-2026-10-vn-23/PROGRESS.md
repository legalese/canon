# PROGRESS — row VN-23 (enc-vn-23)

State on disk, for a resume. Read BRIEF.md first, then this, then re-run check.sh.

## How the .l4 files are made

The `.l4` modules here are GENERATED from templates in the scratch directory
`/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn23/`:

- `src/*.l4.in` — the templates. A line `-- @@src N M` expands to `vnsrc.py quote` of lines N..M; a line `-- @@arms rate|part` expands to the injury-table arms.
- `tools/build.py SRC_DIR DEPOSIT` — expands every template into DEPOSIT (`python3 -I tools/build.py src <DEPOSIT>`).
- `tools/rows.py` — the 60 table rows (name, source lines); `tools/arms.py` — emits the arms, with the rates TYPED BY HAND (not parsed).

If the scratch directory is lost, edit the deposited `.l4` files directly; they are complete.

## Done (typechecked with `l4 check`)

- `lpa-nouns.l4` — DECLARE only.
- `lpa-definitions.l4` — preamble and ĐỊNH NGHĨA.
- `lpa-injury-tables.l4` — the 60 rows, left-handed swap, finger/toe/teeth/skull/shortening classifiers, ankylosis 50%, second eye, unlisted -> named REFUSE.
- `lpa-benefits.l4` — A.1, A.2 (with 1(a), 5% floor on the partial sum, 100% cap), B (with limitation 2), C (with limitation 4), D, II, per-conveyance limit, 1(b), 1(c), 3.

- `lpa-special-provisions.l4`, `lpa-exclusions.l4`, `lpa-general-provisions.l4`, `lpa-termination.l4`, `lpa-claim.l4` (GP 13 + top-level decision) — all typecheck (2026-10-07).

## Status: COMPLETE (2026-10-07)

- Final check.sh: `TOTAL (12 modules) 0 errors, 524 satisfied, 0 failed, 0 refused`, exit 0 (scratch check-final2.txt).
- vnsrc gate (every .l4 and .md except BRIEF.md): `vnsrc check: 941 src: lines, 574 Vietnamese runs, 0 problems`.
- Traces read from a full `l4 run lpa-tests.l4`: all seven as expected (NOTES.md section 6).
- All deliverables exist; the final report has been sent to the lead.

## Forks taken so far (numbered as in the templates)

F1 payee on death: beneficiary if designated, else heirs. F2 "sự kiện bảo hiểm" date per benefit (death date; permanence date; accident). F3 29 Feb birthday clamps. F4 weeks = 7 days. F5 TTD "time" = max days. F6 left-handed swap on every two-column row. F7 3 teeth -> 3-4 band. F8 5 cm -> "at least 5". F9 remaining eye = partial (52 weeks). F10 24 months inclusive. F11 5% floor on the sum of partial items. F12 TTD stops the day before the determination. F13 medical window 12 months. F14 medical other insurance: limitation 4 excess rule. F15 dental surgery covered (definition b over GE12). F16 hospital: whole 24-hour periods only. F17 1(c) with no A benefit: no cap. F18 instalments 30 days after. F19 SP3/SP4/SP8 conditions bite. F20 disappearance deemed from the day after 12 months. F21 SP5 prevails over GE5(g).
Also planned: GE6(d) "đang thực hiện công việc" read as armed forces/police on duty; short-period table overlaps at 3 and 6 months take the lower rate; day counting "within N days from X" = X+N.

## Findings noted so far (to write up)

Teeth: 8 teeth in no band; 3 teeth in two bands; 1-3 teeth row (3%) below the 5% floor. 10 of 31 finger sets and 20 of 31 toe sets unpriced; toe ankylosis rule has nothing to halve. Medical: 52 weeks vs 12 months; three conflicting other-insurance rules (SE3, lim 4, GP11); dental surgery vs GE12. SP5 vs GE5(g). 1(b) top-up window unreachable (PPD needs 52 weeks, top-up needs death within 52 weeks). 1(c) cap 0 without benefit A. GE6(d) "performing work". GE6(a) any breach of law, no causal link. 7.1(e) termination back-dated to departure after 180 days abroad. 7.1(f) "ngay" notice of any injury vs 13(a) 30 days. 13(a) 1-year filing vs PTD 104 weeks (if event = accident). 16.B(b) 0.1% cap vs 4(b) zero liability and Law art 27. GP5 "một triệu năm trăm" words vs 1.500.000. Unused definitions (Năm bảo hiểm, Đang làm việc, Hiệu lực bảo hiểm, Quê quán, Mất thị lực, Mất chi). SP6 duty on the insured. Precedence puts the application above endorsements. Short-period table overlaps. Property/reinsurance boilerplate (SE4, SE6, SE7, SE8).

## Last check.sh totals

Not yet run (no tests module yet).
