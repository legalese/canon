# PROGRESS — VN-25 (enc-vn-25), run VN-25-20261006

Working state, kept on disk in case the session is killed. Read this and BRIEF.md first, then re-run `check.sh`.

## How the .l4 files are made

Each module is written as a template in the scratch directory `scratchpad/vn25/tpl/<module>.l4` (under `/Users/mengwong/.claude/tmp/claude-502/-Users-mengwong-src-legalese-l4-pipeline/9efa11ae-1dd6-427f-9147-a0be56160d6d/`).
A template line `{{Q:233-234,236}}` stands for the `-- src:N |` quotations of those source lines.
`python3 -I scratchpad/vn25/expand.py TEMPLATE OUT` expands it: it calls `scratchpad/vn25/q.py`, which calls `tools/vnsrc.py quote` once per line and drops watermark and page-furniture lines.
The deposited `.l4` files are those expansions.
If the scratch directory is lost, edit the deposited `.l4` directly and make every new `src:` line with `tools/vnsrc.py quote`.

## Done (typechecks; deposited)

- `aptduv-nouns.l4`: every DECLARE.
- `aptduv-ch1-definitions.l4`: Article 1 (1.1 to 1.33), plus ages, anniversaries, monthiversaries, contract year, insurance age, maturity date (and the 1.9-with-1.32 reading), TPD, cancer and waiting period, Accident.
- `aptduv-ch1-general.l4`: Articles 2 to 6.
- `aptduv-ch2-benefits.l4`: Articles 7 and 8, and the death and disability totals.
- `aptduv-ch3-policyholder-rights.l4`: Articles 9 to 13.
- `aptduv-ch8-9-fund-disputes.l4`: Articles 30 to 33.

Also done: aptduv-ch4-premiums-account.l4, aptduv-ch5-charges.l4, aptduv-ch6-changes-termination.l4, aptduv-ch7-claims.l4, aptduv-tests.l4 (333 assertions and 4 traces, all satisfied or FULFILLED in a scratch run on 2026-10-07).
`scratchpad/vn25/deploy.sh` re-expands every template into the deposit and runs check.sh and the quote gate (it takes several minutes; run it in the background).
Last full check.sh before the tests: 10 modules, 0 errors.

## Remaining, in order

(done: `aptduv-findings.l4`, 37 assertions satisfied and one residual trace in a scratch run; findings FD1-FD28 numbered as in that file)
7. (done: GLOSSARY.md, COMPARABLES.md, NOTES.md with {{CHECK}} and {{VNSRC}} placeholders in sections 6 and 7, SOURCE-LICENSE.md with a {{SRCCOUNT}} placeholder) encoding.json; then fill the placeholders from the final deploy.log.
Full check.sh on 2026-10-07 (before the nouns and findings modules stopped quoting): 12 modules, 0 errors, 370 satisfied, 0 failed, 0 refused, exit 0; vnsrc 1123 src: lines, 0 problems.

## Quote-check gate

The lead's ruling: the gate is `python3 -I tools/vnsrc.py check ../../source/raw/aia-an-phuc.txt` over every `.l4` and every `.md` EXCEPT BRIEF.md, ending `0 problems`.
BRIEF.md:23 fails on its own: the checker's two-plain-token gap swallows the English word "to" between two Vietnamese words into one run.
Report both lines, and say which one is the gate.

## Forks taken so far (short; NOTES.md will hold the register)

F1 maturity = the first anniversary strictly after the 100th birthday (Article 4), with 1.9 read with 1.32 kept as finding FD1. F3: 1.3 needs at least 30 days of age and an insurance age of 65 or less. F4: "trước 70 (bảy mươi) tuổi" limits the TPD only. F5: 7.2.3 rows are first-match. F6: the 7.4 limit read as a cap (LAW, Art. 24), with the condition reading kept. F8: the 7.5 base is not reduced by 7.2.3. F9: a second cancer is REFUSEd. F11: an 8.1 exclusion pays the AV only, with no 7.4. F12: 1.30(e) uses reading A. F13: the 90-day window includes its start day. F18: interest is an input. F23: the non-smoker status is an input. F25: insurance age is used everywhere. F26: 7.7 row 10 = year 6. F30: an anniversary that falls on 29 Feb clamps. F31: effective date = the later of completion and payment. F33: 5.1 "tai nạn" = the 1.31 Accident. F34: the 5.1 refund replaces the benefit. F37: 6.3's alive-and-in-force test is applied at the end of the two years. F39: 1.31's 180 days include day 180. F41: 11.1's 90 days include day 90. F42: periods are calendar days, months and years. F47: the 8.1 suicide window includes the end of month 24.

## State at 2026-10-07 (latest)

All deliverables exist. The nouns and findings modules no longer quote clauses (they cite line numbers), which removed about 300 duplicate `src:` lines.
The final run is `scratchpad/vn25/deploy.sh > scratchpad/vn25/final.log`; then `python3 -I scratchpad/vn25/fill.py` writes its numbers into NOTES.md sections 6 and 7, SOURCE-LICENSE.md and encoding.json.
After that, re-run the quote gate on the edited `.md` files, and send the final report.

## Finished, 2026-10-07

Final check.sh: 12 modules, TOTAL 0 errors, 370 satisfied, 0 failed, 0 refused, exit 0.
Quote gate (every .l4 and .md except BRIEF.md): 823 src: lines, 513 Vietnamese runs, 0 problems.
The literal command, BRIEF.md included: 1 problem, in BRIEF.md:23.
Nothing remains but the lead's commit.
