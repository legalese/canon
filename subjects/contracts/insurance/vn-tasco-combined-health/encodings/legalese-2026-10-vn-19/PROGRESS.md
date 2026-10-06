# PROGRESS — row VN-19 (enc-vn-19)

Working state, for a resumed session. Read this and BRIEF.md first, then re-run check.sh.

## How the files are made

- Scratch: `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/scratchpad/vn19/` (call it S).
- Every `.l4` module is EXPANDED from a template `S/tpl/<name>.l4` by `python3 -I S/expand.py S/tpl/<name>.l4 DEPOSIT/<name>.l4`.
  Templates carry `@@src N [M]` (→ `vnsrc.py quote`), `@@qsrc ID N [M]` (qualified quote) and `@@file PATH` (generated rows). Edit the TEMPLATE, then re-expand; never edit the deposit `.l4` by hand.
- Generated data: `S/gdata.txt` (guarantee list rows), `S/edata.txt` (excluded list rows), `S/gtests.txt`, `S/etests.txt`, `S/list211.txt` (Article 2.11 list).
  Regenerate with `tools/annexes.py` (data from `pdftotext -bbox` output in `S/bbox/`; tests from the `-layout` text): see its docstring.
- `tools/vnsrc.py` is EXTENDED (backward-compatible): qualified `src:ID:N` lines and the `in:ID` and `cell:ID:N-M` markers (in square brackets). Pristine copy: `S/vnsrc.orig.py`.

## Done (typechecks clean, vnsrc 0 problems on each)

- tasco-vn19-nouns.l4
- tasco-vn19-ch1-general.l4 (Arts 1-6, defs of Art 2)
- tasco-vn19-art10-waiting.l4 (Art 10)
- tasco-vn19-ch3-exclusions.l4 (Art 11)
- tasco-vn19-ch2-cover.l4 (Arts 7-9 + outcome: `the outcome of` claim)
- tasco-vn19-ch4-claims.l4 (Arts 12-13), tasco-vn19-ch5-6-parties-disputes.l4 (Arts 14-17)
- tasco-vn19-annex-guarantee-list.l4, tasco-vn19-annex-excluded-list.l4 (data), tasco-vn19-tests-annexes.l4 (378 satisfied)
- tools/vnsrc.py (extended), tools/annexes.py

## State on 2026-10-07: complete

All deliverables exist. check.sh: TOTAL (14 modules) 0 errors, 618 satisfied, 0 failed, 0 refused, exit 0 (NOTES section 6).
The quotation gate (every .l4 and .md except BRIEF.md) is recorded in NOTES section 7.
Nothing remains but the final report to the lead. If resumed: re-run check.sh (slow on this machine; run it detached with nohup) and the gate, and compare with NOTES sections 6 and 7.

## Forks referenced in the modules (written up in NOTES §3)

F1 over-60 / "from 60"; F2 2.30 age strictly before; F3 Art 1.2 as at start; F7 2.11 not matched by name; F9 "start date" = this contract; F11 24h test where hours not recorded; F12 whole 24h days; F13 first 10 days per stay, special cap on whole stay; F14 premature birth = other maternity; F15 programme by scope SI; F16 B and C caps aggregate; F17 Art 9 window on day consequence began / 2.21(b) 180-day floor on both loss-of-function kinds; F18 2.26 gear qualifier literal; F19 Art 3 only cost-based benefits; F20 end date covered; F21 4.1(c) per scope; F22 4.1(e) refund 100% pro rata days; F23 calendar days; F24 4.2(a) refund declined if a claim; F25 4.4 consequence = day began; hours stay past end → REFUSE; F26 renewal same/next day, full year; F27 lower SI breaks continuity, increase waits from start; F28 waiting from chain start; F29 day N first covered; F30 exactly 100 persons → REFUSE; F31 row 2 includes surgery, 10.2 = III.1/III.2; F32 10.2(d) ratio from anchor, other complications keep table; F33 exclusion nexus = present in this event; F34 11.3 units as printed (0.25, 50); F35 "at insured's request" = no indication; F36 11.17 illness only, chain start; F37 accident never scope C; F38 cost by non-2.16 doctor = 0; F39 III.4 proration no rounding; F40 lists have no effect on cover; F41 force majeure days added (12.1, 12.2); F42 LAW Art 30.2 not encoded; F43 LAW Art 19.2 proof of explanation; F44 16.2 vs other law unverified.

## Findings (written up in NOTES §4, X1-X30)

X1 no column for exactly 100 persons; X2 injury/surgery tables not in source; X3 chỉnh hình; X4 4.2(a) refund lost on any claim; X5 renewal discretion + over-60 + lowered SI; X6 climbing with gear excluded, without not; X7 no nexus 11.4/11.14; X8 2.18 day-count methods disagree; X9 11.3 units; X10 2.11 non-diseases; X11 11.8 vs 11.17; X12 2.24 injury only; X13 2.27 unused; X14 4.1(c) literal ends whole contract; X15 4.4 cites Art 8 for Art 9 rule; X16 row 4 TPD from illness, no benefit; X17 Art 9 + 2.21(b) one-day window. To add: 12.1 vs 12.2 (notice after death can fall after 1-year bar); 12.4 vs 12.5 15/30 days; 12.5 verification no deadline; 13.7 open-ended docs; 13.4 gap at exactly 20m; 11.9 vs 2.11 (TB, malaria, dialysis); 4.1(e) premium kept; lists not incorporated by the rules, "PHỤ LỤC 5" implies annexes 1-4; no decision number/date in the rules. [in:tasco-guarantee-hospitals]

## Last check.sh totals

2026-10-07: TOTAL (14 modules) 0 errors, 618 satisfied, 0 failed, 0 refused; exit 0.
