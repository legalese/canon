# PROGRESS — row VN-14 (enc-vn-14)

State on disk, so a resumed session can continue. Read this and `BRIEF.md` first, then re-run `check.sh`.

## Done

- All `.l4` modules written and green: `vn14-nouns`, `vn14-ch1-definitions` (Art 1-2), `vn14-ch1-temporary-cover` (Art 3), `vn14-ch1-duties-and-changes` (Art 4-11), `vn14-ch2-benefits` (Ch 2 tax paragraph, Art 12-15), `vn14-ch3-premium-and-account` (Art 16-23), `vn14-ch4-fund-and-charges` (Art 24-25), `vn14-ch5-claims-and-termination` (Art 26-29); tests `vn14-tests-ch1`, `vn14-tests-ch2`, `vn14-tests-ch3-ch5`, generated `vn14-tests-tables`; `vn14-findings` (evidence for findings).
- Last full `check.sh` seen (2026-10-06, before the src-quote trimming, which touched comments only): `TOTAL (13 modules) 0 errors, 365 satisfied, 0 failed, 0 refused`, exit 0. The rerun after trimming was killed by the usage limit; rerun it.
- `vnsrc check` over `*.l4` after trimming: `693 src: lines, 20 Vietnamese runs, 0 problems`.

## Remaining, in order

1. DONE 2026-10-07: `check.sh` TOTAL (13 modules) 0 errors, 365 satisfied, 0 failed, 0 refused, exit 0.
2. DONE 2026-10-07: `NOTES.md`, `GLOSSARY.md`, `COMPARABLES.md` (25 rows), `encoding.json`, `SOURCE-LICENSE.md`. NOTES.md §7 filled. Gate (every .l4 and .md except BRIEF.md): `vnsrc check: 693 src: lines, 485 Vietnamese runs, 0 problems`.
3. DONE. Gate: `python3 -I tools/vnsrc.py check ../../source/raw/manulife-group-linked.txt vn14-*.l4 NOTES.md GLOSSARY.md COMPARABLES.md SOURCE-LICENSE.md PROGRESS.md` (every .l4 and .md except BRIEF.md) must end `0 problems`.
4. Final report sent to the lead, 2026-10-07. Nothing remains.

## How the files are made

- The rule and test modules are edited in `scratchpad/vn14/src/` (scratchpad = this session's scratchpad directory) with `--@src N M` / `--@cite N M` placeholder lines, and written into this directory by `python3 -I scratchpad/vn14/bin/build.py scratchpad/vn14/src DEPOSIT`, which generates every `-- src:` line by running `tools/vnsrc.py quote`. The deposited `.l4` files are complete without the scratch copies; an edit made directly in DEPOSIT is fine if the scratch copy is not rebuilt over it.
- `vn14-tests-tables.l4` is generated: `python3 -I tools/gen_table_tests.py ../../source/raw/manulife-group-linked.txt > vn14-tests-tables.l4`.

## Forks and findings (numbering used in the modules' comments)

Forks F1-F37 and findings X1-X26 are referenced by number in the `.l4` comments; NOTES.md must use the same numbers. Key: F1 age-last-birthday; F2 age date for 1.4 and 29.3; F3 calendar days, N days end on start+N; F4 month-end anniversaries; F5 temp period includes end date; F6/F7 16.2.2/16.2.3 windows; F8 riders cancelled -> cash to basic; F9 6.2 tie; F10 vested = ratio x PH account; F11 per-payee deductions refused; F12 12.3 actual age in months; F13 suicide window excludes 2nd anniversary; F14 funeral from 1st anniversary; F15 funeral is an advance; F16 grace = trigger+60; F17 21.1(a) 80% of (IMAV-fee-debt); F18 21.2 SA reduced by withdrawal; F19 23.1(d) strictly after; F20 25.2 step per month; F21 credited = max(declared, guaranteed); F22 monthly interest is input; F23 25.6 new rate > 2.5%; F24 1.4 continuing; F25 LAW 4.1 v Law 22(3); F26 26.1 FM sentence = late-only exception; F27 no employment = 0 years; F28 3.2 before premium switch; F29 temp start = later of stamp and premium; F30 lapsed/suspended part pays no DB; F31-F33 LAW Art 40 (suicide anchor, other beneficiaries, refund to PH); F34 LAW 22(2) v 5.2; F35 LAW 35 free look absent; F36 LAW 30 claim period; F37 LAW 24 contra proferentem favours employer.
Findings: X1 1.4 continuing ends cover at 66/abroad; X2 temp accident pays less than suicide refund (+ silence on refund); X3 temp payee in application; X4 no temp cover for later-added members; X5 Art 5 gaps; X6 6.2 double-deducts withdrawals; X7 death during suspension pays nothing; X8 16.2.1 v 16.2.3; X9 Art 15 dangling "hoặc", PH crime, no payee; X10 no floors; X11 10.2 no consequence, duty on PH; X12 discretion without criteria; X13 10.2 copy-over and different deductions; X14 9.3 common disaster; X15 unstated min/max SA; X16 12.2 Contract v part, "xem xét"; X17 25.2 v 25.3 dates; X18 termination charge trigger; X19 26.1 literal "chỉ"; X20 26.2(v) website list; X21 26.3(ii) undefined rate; X22 27.2 forum; X23 29.3 not on voluntary end; X24 premium between death and claim kept; X25 auto-withdrawal forfeits bonus; X26 drafting slips (1.8 "(ii)" twice, two CHƯƠNG 4).
