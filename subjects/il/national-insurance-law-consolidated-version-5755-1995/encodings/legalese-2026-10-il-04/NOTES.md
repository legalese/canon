# NOTES — il/national-insurance-law-consolidated-version-5755-1995, encoding row `legalese-2026-10-il-04`

National Insurance Law [Consolidated Version], 5755-1995: **s 334** (interpretation for Chapter 15, insurance contributions), **s 337** (the rate of insurance contributions), **Schedule J** (לוח י׳, the rates), and the **s 1** definitions they use, encoded in L4 by one agent in one session (run `IL-04-20261006`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**. Version **0.4.0** (2026-10-07): fork F6 ruled, a fall in the index or the average wage declined by default; see "Version 0.4.0" below. Version 0.3.1: the independent tests re-pointed to the items' reading. Version 0.3.0: the Schedule J switch, fork F4 ruled.
No domain expert has read it against the source; HG1 has not been sought.

## Version 0.4.0 (2026-10-07): fork F6, a fall in the index or the average wage, as a switch

Backlog row IL-12, encoder `enc-il-12`, one session, no sub-agents, on Meng's ruling of 2026-10-07 (TRIDENT) as the lead relayed it.
Nothing below was deleted; the F6 row of the fork register (section 4) is marked **(0.4.0)** in place.
The section "Comparison with Axiom's RuleSpec" at the end, `tests-independent.l4`, `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` are untouched.

### The fork and its three readings

s 334(a)(1) (source line 3606) updates the reduced collection threshold "לפי שיעור עליית המדד", by the rate of rise of the index; s 334(a)(2) (line 3607) "לפי שיעור עליית השכר הממוצע", by the rate of rise of the average wage.
Neither says what follows when the later reading is below the earlier one.
The three readings are kept by name, as the constructors of `A reading of section 334(a) where the index or the average wage falls` (`nii-il04-nouns.l4`):

| reading | name in the encoding | who holds it |
| --- | --- | --- |
| (i) the fall is applied: the rate of rise is negative, and the threshold goes down by it | `the fall is applied` | this row, versions 0.1.0 to 0.3.1 (fork register F6, "taken") |
| (ii) no update on a fall: the threshold stays where it was | `the threshold stays where it was` | the Axiom Foundation's encoding, as BACKLOG row IL-12 records it; this row did not read Axiom's material (the semi-cleanroom ruling of 2026-10-06) |
| (iii) declined: the text provides for a rise and says nothing of a fall | `a fall is declined` | the independent tester, fid-il-04: T7, `tests-independent.l4` line 787, "My decided answer: REFUSE (genuine ambiguity)"; its `DECIDED-ANSWERS.md` adds that "rise" makes (ii) at least as strong as (i) |

**The default is (iii), declined.** The ruling's reason: this project's rule is to decline where the text does not decide, and on a fall s 334(a) does not decide.
The refusal reads "section 334(a) updates the threshold by the rate of rise of the index or of the average wage, and says nothing of a fall".

**The default is not waiting on evidence.** On 2026-10-07 Meng declined to look up the Institute's past practice on a falling index as evidence for a reading: "whatever they did last time is no guarantee of how they'll do next time".

A rise, or no change, is answered the same under all three readings: the reading is consulted only where the later reading is below the earlier.

### What changed

1. **The type**, in `nii-il04-nouns.l4`: `A reading of section 334(a) where the index or the average wage falls`, one of `the fall is applied`, `the threshold stays where it was`, `a fall is declined`.
2. **The switch** is one named rule in `nii-s334-interpretation.l4`, `section 334(a) — the reading this row takes where the index or the average wage falls`, now `a fall is declined`; another reading is a one-line change there.
3. **The refusal** is a rule of its own there, `section 334(a) updates the threshold by the rate of rise of the index or of the average wage, and says nothing of a fall`.
4. **Reading forms.** `the sum … updated by the rate of rise from … to …`, `s 334(a)(1) — the threshold on 1 January of …` and `s 334(a)(2) — the threshold on 1 January of …` each have a form that takes the reading as an argument (`…, reading a fall as` r); the three old names now follow the switch. The year checks of (1) and (2) come before the reading, so a year outside a paragraph is refused for the year under every reading.
5. **What it does not touch.** `s 334(a) — the reduced collection threshold for a month in` answers 2026 with the published 7,703 and declines 2027 on by name, and computes no update, so no s 337 or Schedule J answer moves. No other rule module changed. The capstone (row IL-07) vendors `nii-s334-interpretation.l4` and `nii-il04-nouns.l4`; see its version 0.2.2.

### Assertions changed or added

`nii-il04-tests.l4`, one assertion changed (line number at 0.3.1):

| line | assertion | 0.3.1 | 0.4.0 |
| ---: | --- | --- | --- |
| 368 | s 334(a)(1), 2027, from 8,000, index 100 to 99 | 7920 (the fall applied, the only reading) | re-pointed to reading (i) by name, `, reading a fall as` `the fall is applied`, 7920 unchanged; at the default the same case is declined (added below) |

Added (21, its "Section 334(a)" section, each value worked by hand from s 334(a)(1)-(2) before the run):

- the switch's value, `a fall is declined`;
- the index falling 100 to 99 from 8,000 in 2027: (ii) 8,000; (iii) declined; the default declined;
- the average wage falling 10,000 to 9,900 from 8,000 in 2029, rate of rise −100 / 10,000 = −0.01: (i) 7,920; (ii) 8,000; (iii) declined; the default declined;
- a year outside the paragraph refused for the year under a named reading: (1) in 2029 at (ii), (2) in 2028 at (i);
- a rise under each reading: index 100 to 105, 8,000 to 8,400 in 2028; average wage 10,000 to 10,500, 8,000 to 8,400 in 2029 (six);
- no change under each reading and by default: index 100 to 100 in 2027 (four), average wage 10,000 to 10,000 in 2029 by default (one); 8,000 stays 8,000.

`nii-il04-tests.l4`: **181 satisfied**, 0 failed, 0 refused (0.3.1: 160).
`tests-independent.l4` (not edited): **641 satisfied, 5 failed, 0 refused** (0.3.1: 640, 6, 0). The one change, compared line by line: T7, line 787, failed at 0.3.1 and is satisfied at 0.4.0. The five that stand are the pre-repair F3 expectations (lines 756, 924, 929-931), unchanged. `check.sh` now expects 5 failures from it.
`nii-il04-tests-expected-red.l4`: 26 satisfied, 15 failed, unchanged.

### What `check.sh` prints at 0.4.0

```
module                                    errors satisfied  failed  refused  expected
nii-il04-nouns.l4                              0         0       0        0         0
nii-il04-published-figures.l4                  0         0       0        0         0
nii-il04-tests-expected-red.l4                15        26      15        0        15
nii-il04-tests.l4                              0       181       0        0         0
nii-s1-definitions.l4                          0         0       0        0         0
nii-s334-interpretation.l4                     0         0       0        0         0
nii-s337-rates.l4                              0         0       0        0         0
nii-schedule-j-tables.l4                       0         0       0        0         0
nii-schedule-j.l4                              0         0       0        0         0
tests-independent.l4                           5       641       5        0         5
TOTAL (10 modules)                            20       848      20        0
```

Exit 0. Full run 2026-10-07 09:46:06Z to 09:46:24Z.
The `l4` binary changed since 0.3.1: `~/.cabal/bin/l4` is now a symbolic link into the cabal store, `jl4-0.1-d8a7263f/bin/l4`, sha256 `4476e7580ea3c5c0d06c1d029ba801b6627070fcce8c7c40fae47d5521559fac`, the same before and after the run (0.3.1 ran on `3a1843a0…`, not a store build).
The 0.3.1 baselines were re-run on the new binary before any edit (`nii-il04-tests.l4` 160/0/0, `tests-independent.l4` 640/6/0, `nii-il04-tests-expected-red.l4` 26/15/0), so every difference above is the edit's, not the binary's.
`tools/srcquote.py` left `nii-s334-interpretation.l4` unchanged, and `tools/hebcheck.py` passes on the three changed modules.

Row IL-05 was re-run, as asked: it re-declares IL-04's types rather than importing them (cross-directory IMPORT does not resolve), so no IL-04 change reaches it; its `check.sh` exits 0 with 18 errors, 305 satisfied, 18 failed, 2 refused, as at its 0.3.0.

## Version 0.3.1 (2026-10-07): the independent tests re-pointed to the items' reading

The lead, on Meng's go-ahead of 2026-10-07, re-pointed 22 assertions in `tests-independent.l4` (fid-il-04's) to fork F4's items' reading by name: `, reading Schedule J as` `the items govern` was added to each, and the s 337(a)(1) entries without a threshold were spelled out as their own body spells them (the threshold s 334(a) gives for the year, no order under Amendment 252 s 7(b)).
No expected value and no input changed, no line was added above them, and the six other failures were not touched.
A dated note at the end of the file says the same.
No rule module changed, so the capstone's vendored copies are unaffected.

Why re-point rather than change the values: the tester decided the items' reading on purpose and before the ruling ("the rows are the law", its section 3).
Its figures are independent evidence for the reading the ruling preserves, so they now test that branch of the fork instead of failing against the default.

- **The 13 that failed** at 0.3.0 now pass: lines 505, 507-510, 801-803, 846-848, 856, 933.
- **The 9 that were refused** at 0.3.0 now pass: lines 805-810, 854, 858, 895.
- **The 6 that stand** are unchanged findings: T7 (line 787, fork F6) and the five pre-repair F3 expectations (lines 756, 924, 929-931).

`tests-independent.l4`: **640 satisfied, 6 failed, 0 refused** (0.3.0: 618, 19, 9; 0.2.0: 640, 6, 0).
`check.sh` now expects 6 failures and no refusals from it.
Full run 2026-10-07 07:50:16Z to 07:51:02Z, `l4` sha256 `3a1843a0e51ce1663cd71b4307e061fa425f2f9f23d78afb8ffa9be6fd20278f` (not a store build), the same before and after: 21 errors, 826 satisfied, 21 failed (15 expected-red, 6 independent), 0 refused, exit 0.

## Version 0.3.0 (2026-10-07): the Schedule J switch

Backlog row IL-11, encoder `enc-il-11`, one session, no sub-agents, on Meng's ruling of 2026-10-07 as the lead relayed it: Schedule J is read at its **printed totals** by default where its totals row and its items differ, and the items' reading is **kept as the alternative of fork F4**, not deleted.
Nothing in the sections below was deleted; entries this version changes are marked **(0.3.0)** in place.
The section "Comparison with Axiom's RuleSpec" at the end, `tests-independent.l4`, `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` are untouched.

### What changed

1. **Fork F4 is ruled.** Where a printed total (source lines 4730, 4748) differs from the sum of its items, the printed total governs by default; where they agree the reading changes nothing. The cells that differ are those section 0 lists: column D's upper part in every version (7.00 against 4.67); column C above the threshold for an employee (2026 and 2027 as read in 2024-2027: 14.60 against 14.49; 2028 on: 14.50 against 14.39); and, in the permanent version only, column C not above the threshold for an employee (2027: 3.95 against 4.26; 2028 on: 3.85 against 4.16).
2. **The switch** is one named rule in `nii-schedule-j.l4`, `Schedule J — the reading this row takes where its totals row and its items differ`, now `the printed totals govern`; the other reading is a one-line change there, to `the items govern`. The type, `A reading of Schedule J where its totals row and its items differ`, is in `nii-il04-nouns.l4`.
3. **How a reading is computed.** At the items, as before: each branch's figure on each part, summed. At the printed totals: the items' figure, plus, on each part of the income whose cell differs, the part times the difference between the printed total and the items' sum, for the branches together. A total is the schedule's figure for every branch that prints a figure in its column; for fewer branches the schedule prints no total, and where the items do not reach the total it cannot say which item the difference belongs to, so such a case is **declined**: "the printed total of Schedule J in this column is for every branch that prints a figure in it, together; the items do not add up to it, and these are fewer branches". A part that is nil adds nothing, so a case wholly below the threshold in 2026 is answered at either reading for any branches.
4. **Which rules read it.** `the contributions under … in the branches …`, `the combined percentage in column C of …` and `the column D deduction under …`, and through them every s 337(a)(1) and (a)(2) entry point, now read the schedule as the switch says. Each also has a form that takes the reading as an argument (`…, reading Schedule J as` r), and the items' reading under its old body has a name of its own (`…, at the items`). The most general s 337(a)(1) and (a)(2) entry points (with the threshold and the extension order) have a reading form too; `the combined percentage in column D of …, reading Schedule J as` r is new. A reading is an argument, never a field of the case records, so the records `tests-independent.l4` builds still build.
5. **What it does not touch.** Column E, the per-branch figures (`the percentage in column C of`, `the percentage in column D of`), `the contribution under … in the branch of …` (one branch: the items, by definition), and the totals checks of the red module, which compare the source with itself.

### Assertions whose expected value changed, or that now ask the items by name

`nii-il04-tests.l4` (line numbers at 0.2.0):

| line | assertion | 0.2.0 | 0.3.0 |
| ---: | --- | --- | --- |
| 211 | s 337(a)(1), 2026, senior citizens and survivors only, 10,000 | 306.2999 | re-pointed to the items by name, 306.2999 (at the printed totals: declined, one branch above the threshold) |
| 215 | the same, maternity only, 7,704 | 18.5012 | re-pointed, 18.5012 |
| 217 | the same, work injury only, 10,000 | 93.5362 | re-pointed, 93.5362 |
| 223, 224 | 2027 / 2028, work injury, 10,000, threshold 8,000 | 78.8 / 68.8 | re-pointed, 78.8 / 68.8 |
| 233 | 2026, senior citizens and survivors only, with the s 343 flag | 306.2999 | re-pointed, 306.2999 |
| 468, 469, 471 | 2027 / 2028 work injury with and without an order | 89.2 / 87.2 / 78.8 | re-pointed, unchanged |
| 317 | column D, 2027 permanent version, 10,000, threshold 8,000 | 125.4 | re-pointed, 125.4; and at the default, **172** (8,000 × 0.40% + 2,000 × 7%) |
| 328 | column D, 2026, 7,704 | 80.1579 | re-pointed, 80.1579; and at the default, **80.1812** (7,703 × 1.04% + 1 × 7%) |
| 329 | column D, 2026, 20,000 | 654.3811 | re-pointed, 654.3811; and at the default, **940.9012** (7,703 × 1.04% + 12,297 × 7%) |
| 449 | column D, 2026, 10,000 | 187.3811 | re-pointed, 187.3811; and at the default, **240.9012** (+ 2,297 × 7%) |

Added (13, its last section, worked by hand from the cells before the run): the switch's value; all nine branches at 10,000 in 2026, **762.8785** at the printed totals (7,703 × 5.55% + 2,297 × 14.60%) and 760.3518 at the items (× 14.49%); one branch above the threshold declined, and below it answered (7,000 × 2.22% = 155.4); all nine at 6,000 in 2027 with the scenario threshold 8,000, **237** printed (× 3.95%) and 255.6 by the items (× 4.26%); the composites, 14.6 and 7 at the printed totals, 14.49 and 4.67 at the items, the controlling shareholder's declined; the self-employed column, which meets its total, answered for one branch (work injury above the threshold, 0.78).

`nii-il04-tests-expected-red.l4`: its two composite assertions that used the generic rule (the employee's 14.6, the controlling shareholder's 14.17) now ask the items' reading by name (`…, at the items`), so they still compare the items with the Institute and still fail; the count stays 15. (At the default the employee's composites are reached, and the controlling shareholder's are declined: both asserted in `nii-il04-tests.l4`.)

### What `check.sh` prints at 0.3.0

Run from 2026-10-07T07:19:52Z to 07:20:10Z as `L4=/Users/mengwong/.local/bin/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset.
The binary is `~/.local/bin/l4` → `~/.cabal/bin/l4`, now a regular file, not a cabal store link: 233,037,424 bytes, modified 2026-10-07T05:35:45Z, sha256 `6015a4c3fa181842c597c95948290fe45537963d279ae5b5918a106a0c3b54a6`, the same before and after the run; it is neither `jl4-0.1-0ee0100b` (sections 0 and Repair) nor `jl4-0.1-ff13a0ea`. Before any change of 0.3.0 the same binary reproduced the Repair's table exactly (15 / 143 / 640 with 6 failed). No module changed during the run.

```
module                                    errors satisfied  failed  refused  expected
nii-il04-nouns.l4                              0         0       0        0         0
nii-il04-published-figures.l4                  0         0       0        0         0
nii-il04-tests-expected-red.l4                15        26      15        0        15
nii-il04-tests.l4                              0       160       0        0         0
nii-s1-definitions.l4                          0         0       0        0         0
nii-s334-interpretation.l4                     0         0       0        0         0
nii-s337-rates.l4                              0         0       0        0         0
nii-schedule-j-tables.l4                       0         0       0        0         0
nii-schedule-j.l4                              0         0       0        0         0
tests-independent.l4                          19       618      19        9      19/9
TOTAL (10 modules)                            34       804      34        9
(a failed assertion is also an error; any other error, or a refused assertion a module is not expected to have, makes the run red; "expected" is failed/refused where a module may refuse)
```

**Re-run on a new binary.** `~/.cabal/bin/l4` was replaced at 2026-10-07T07:25:28Z, after the run above: sha256 3a1843a0e51ce1663cd71b4307e061fa425f2f9f23d78afb8ffa9be6fd20278f (233,039,712 bytes, modified 2026-10-07T07:25:28Z, again a regular file, not a store build). Re-run from 07:28:41Z to 07:28:53Z on it, the binary unchanged during the run and no module changed: the same table, exit 0.
`check.sh` exit 0; every error is a failed assertion.
`nii-il04-tests.l4`: 160 of 160 (143, of which 13 re-pointed, plus 4 default twins and 13 added), every new value satisfied on the first run that evaluated it.
`check.sh` now also has `expected_refused` (9 for `tests-independent.l4`, 0 for every other module), and `expected_failed` lists `tests-independent.l4` with 19.
`tools/srcquote.py` over the changed modules changes nothing; `tools/hebcheck.py` passes on every `.l4` module, `BRIEF.md` and `encoding.json`.

### The independent tests at 0.3.0

`tests-independent.l4` (fid-il-04's, not edited), 646 assertions: **618 satisfied, 19 failed, 9 refused** (0.2.0: 640, 6, 0). Compared assertion by assertion with the run before the change:

- **6 failures stand**, unchanged: T7 (line 787, fork F6) and the five pre-repair F3 expectations (lines 756, 924, 929-931).
- **13 that passed now fail**, each an items' figure where the default now reads the printed total: the composites for an employee above the threshold in 2026, 2027 and 2028 and not above it in 2027 and 2028 (lines 505, 507-510); s 337(a)(1) for all nine branches in 2026 at 7,704, 10,000 and 60,000 (lines 801-803), in 2027 at and around the scenario threshold 7,857.06 and at 10,000 (846-848), and in 2028 at 10,000 (856); column D in 2027 at 10,000 (933).
- **9 that passed are now refused**, each fewer branches than the totals row covers, above the threshold: one branch in 2026 at 10,000 (lines 805-810: senior citizens and survivors, work injury, unemployment, maternity, children, disability), work injury in 2027 and 2028 (854, 858), and the seven branches of a controlling shareholder (895).

None of these is a defect of the tests: each was decided against fork F4's items reading, which version 0.2.0 took and 0.3.0, by ruling, does not. They are left for the tester to reclassify. **(0.3.1)** Superseded: the lead re-pointed all 22 to the items' reading by name; see "Version 0.3.1".

## Repair 2026-10-07

Run `IL-09-20261006` (claim row IL-09), encoder `enc-il-04`, on Meng's ruling YOGHURT as the lead relayed it: repair this row against the enacted amending Laws.
Nothing in sections 0-9 was deleted.
Entries whose answer changed are marked **(revised 2026-10-07)** and keep a sentence saying what they said before; entries that only gained evidence are marked **(added 2026-10-07)**.
The section "Comparison with Axiom's RuleSpec" at the end, `tests-independent.l4`, `DECIDED-ANSWERS.md` and `INDEPENDENT-FINDINGS.md` are untouched.

### The enacted Laws

| Law | Sefer HaChukim | file, or how fetched | sha256 | what this row takes from it |
| --- | --- | --- | --- | --- |
| National Insurance Law (Amendment No. 252 and temporary provision), 5785-2025 | 3347, pp. 176-178 (14 January 2025) | deposited: `../../registers/source-bundle/amending-laws/25_lsr_5482787.pdf` (from `https://fs.knesset.gov.il/25/law/25_lsr_5482787.pdf`) | `d6c450ca0b869d1edb036b0f96bffbd79be6670336d9b5aa888da6cf2ecc8904` | s 6: commencement 1 January 2025; s 7(a): the Law is read, "for national insurance contributions collected in respect of the years 2025 and 2026", until 31 December 2026, with s 7(a)(3) replacing the lower sub-columns of columns C and D of Schedule J only; s 7(a)(3)(a): item 2's lower figure for those who are neither printed as 0.17, the column's total as 6.92; s 7(b): the Minister of Finance may extend that period by order to 2027 and then 2028, one year at a time |
| Law for Achieving the Budget Targets and Implementing the Economic Policy for Budget Year 2025 (Legislative Amendments), 5785-2025 | 3384, pp. 395-396 | deposited: `../../registers/source-bundle/amending-laws/25_lsr_6133485.pdf` (from `https://fs.knesset.gov.il/25/law/25_lsr_6133485.pdf`) | `eba7e1fa570a3ece265d87f379543024da038ee51af3f959d4c74162f5edecfa` | s 19 (Amendment No. 256): (2) inserts the definition of the reduced collection threshold into s 334(a); (6) "in Schedule J, everywhere", for "60% of the average wage" substitutes "the reduced collection threshold as defined in s 334(a)"; s 20(1): in Amendment 252 s 7(a)(3)(a), 0.17 becomes 0.16; s 21: the chapter commences on 1 January 2026 |
| Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Years 2023 and 2024), 5783-2023, s 24 (National Insurance, Amendment No. 234, temporary provision) | 3045, p. 169 | fetched 2026-10-06 21:39:39 UTC through the lead's Israeli-IP SOCKS proxy (an `ssh -D` tunnel to an EC2 instance in il-central-1) from `https://fs.knesset.gov.il/25/law/25_lsr_2572039.pdf`, 414,996 bytes, 32 pages; **not deposited** (outside this directory's lane; the bytes are kept in the encoder's scratchpad for the lead) | `6d90d3c4393a55874bca61b2cf7d3a57cba60ec900df57560563d1d2cc7474af` | from 1 January 2024 to 31 December 2027, Schedule J is read with item 4 for an employee at 2.06 above the split (for 1.96) and 0.47 below it (for 0.37), and the totals at 14.60 (for 14.50) and 3.95 (for 3.85): the enacted source of the editors' "2024 to 2027" notes (the comparison's N3) |

Text was read with `pdftotext -raw` (visual order, word order reversed per line) and, for Amendment 252 p. 177, by rendering the page to an image; the 0.17 was read off the image.
No Hebrew from these PDFs is quoted in the modules (the Hebrew check is against the consolidation only); they are cited in English.

### What changed

1. **F3, column D's upper part (revised).** Amendment 252 never replaced column D's upper sub-column, and s 19(6) amended its heading from 1 January 2026; so in every reading of the schedule for 2026 on the upper part begins at the reduced collection threshold. The flag on the two temporary versions changed from TRUE to FALSE. The heading the consolidation prints at line 4718 ("above 60% of the average wage") is a stale copy of the pre-2026 text: still quoted, no longer followed. The refusal for the "gap" is still defined, and is now reachable only through the 2025 version kept as data. (Comparison R1, D11; IL-05's NOTES section 9 reads the three texts the same way.)
2. **A1, the 2025 text (added).** Item 2's lower figure for those who are neither, as enacted for 2025 (0.17), is kept as data in `nii-schedule-j.l4`, in a 2025 version no year arm selects. With 0.17 the column's items sum to 6.93 against the printed 6.92; s 20(1) made it 0.16 from 1 January 2026, and then the column meets its total. 2025 stays declined.
3. **F1 (added).** Amendment 252 s 7(a)'s "in respect of the years 2025 and 2026" confirms reading (i).
4. **An extension order under Amendment 252 s 7(b) (added; assumption A8).** `Schedule J — the version for a contribution month in` *year* `, the temporary provision extended to that year by an order under Amendment 252 s 7(b):` *order*, and s 337(a)(1) and (a)(2) entry points that take the same argument. With an order, 2027 and 2028 read the temporary lower sub-columns; an order for 2029 on is declined. The year-only rules assume no order. It is an argument, not a field of the case records, so that the records `tests-independent.l4` builds still build. (The comparison's R2 proposed declining when the input is not given; the lead's instruction set the default instead.)
5. **F18, the temporary sub-columns' own headings (added fork).** See section 4.
6. **Column E's comment (revised; comparison R4).** The nouns module no longer calls column E a percentage; s 32(c1)(1) divides the Treasury's allocations among the branches "as in Schedule J" (line 495).
7. **F4, A3, F5, section 7 (added evidence)**, and new forks F19 and F20; see their entries.
8. `nii-s334-interpretation.l4`'s vintage refusal cites the enacted s 19(2) and s 21 in place of the Wikisource page.

### Assertions whose expected value changed

All three are in `nii-il04-tests.l4`, section "Schedule J, column D — the two headings", 2026, the deduction branches, threshold 7,703.

| assertion | was | now | why |
| --- | --- | --- | --- |
| deduction on a wage of 7,704, average wage 13,566 | `REFUSED` (the gap) | 80.1579 (7,703 × 1.04% + 1 × 4.67%) | 2025 budget-year Law s 19(6) and s 21 (SH 3384 p. 396); Amendment 252 s 7(a)(3) (SH 3347 p. 177) |
| deduction on a wage of 20,000, average wage 13,769 | `REFUSED` | 654.3811 (7,703 × 1.04% + 12,297 × 4.67%) | the same |
| `where column D's upper part begins in` the 2026 version | 8,139.6 (60% of 13,566) | 7,703 | the same |

The comparison's R1 gives the same two figures (80.1579, 654.3811).
No other expected value in this row's own modules changed.
Added: 23 assertions in `nii-il04-tests.l4` (its last section), each worked by hand from the cells and the enacted figures before it was run, and 1 in `nii-il04-tests-expected-red.l4` (family 3).

### What `check.sh` prints after the repair

Run on 2026-10-07 with the same binary as section 0 (`jl4-0.1-0ee0100b`, sha256 `64bbcb15…e118`), `JL4_LIBRARY_PATH` unset:

```
module                                    errors satisfied  failed  refused  expected
nii-il04-nouns.l4                              0         0       0        0         0
nii-il04-published-figures.l4                  0         0       0        0         0
nii-il04-tests-expected-red.l4                15        26      15        0        15
nii-il04-tests.l4                              0       143       0        0         0
nii-s1-definitions.l4                          0         0       0        0         0
nii-s334-interpretation.l4                     0         0       0        0         0
nii-s337-rates.l4                              0         0       0        0         0
nii-schedule-j-tables.l4                       0         0       0        0         0
nii-schedule-j.l4                              0         0       0        0         0
tests-independent.l4                           6       640       6        0         6
TOTAL (10 modules)                            21       809      21        0
```

`check.sh` exit 0; every error is a failed assertion, read line by line from the diagnostics, none "could not be evaluated".

- `nii-il04-tests.l4`: 143 of 143 (120 before, 23 added).
- `nii-il04-tests-expected-red.l4`: 15 of 41 fail, the 14 of section 0 and the 2025 text (line 137).
- `tests-independent.l4` (the independent tester's; not edited): 646 assertions, 640 satisfied, 6 failed. One is T7 (line 787, fork F6), failing before the repair. **Five encode the pre-repair F3** and now fail: line 756 (the 2026 version's flag asserted TRUE), line 924 (upper part begins at 8,139.6), and lines 929-931 (refusals at 7,703.01, 8,000 and 10,000, for which the enacted Laws give, on the items, 80.111667, 93.9811 and 187.3811; this row's tests now assert 187.3811). They stay failing and are left for the tester to reclassify. `check.sh`'s `expected_failed` table now lists `tests-independent.l4` with 6 (the encoder's change to `check.sh`, made so that the run's exit status reflects the expected count; the tester's file is unchanged).

**Mechanical checks after the repair.** `tools/srcquote.py` over the nine `nii-*.l4` modules changes nothing; `tools/schedule_j.py` still reproduces `nii-schedule-j-tables.l4` byte for byte (the 2025 row is hand-written in `nii-schedule-j.l4`, not generated, because it is not in the consolidation); `tools/hebcheck.py` passes on every `.l4` module (`tests-independent.l4` included), `BRIEF.md`, `SOURCE-LICENSE.md`, `encoding.json`, and this file up to the comparison section. It flags five Hebrew runs inside the comparison section (lines 493-536 at the time of writing), which quote the enacted Laws, not the consolidation the tool checks against; that section is the comparison author's and is not edited here. (Section 0's sentence that the check passes on "this file" was true when written, before the comparison section was appended.)

### Still not sourced

The consumer price index: the Central Bureau of Statistics API returned an empty reply through the Israeli proxy too (2026-10-06 21:40 UTC), so the index stays an input and the 2026 threshold stays the Institute's published 7,703 (not checked against s 334(a)(1)'s formula). The threshold for 2027 on, and any order under Amendment 252 s 7(b), were not published at retrieval.

## 0. What `check.sh` prints

(As run on 2026-10-06, before the repair; the numbers after it are in "Repair 2026-10-07" above.)

Run on 2026-10-06 with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, which resolves to the cabal store entry `jl4-0.1-0ee0100b` (modified 2026-10-06 21:20 local), sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`, and no record beside it names the commit it was built from.

```
module                                    errors satisfied  failed  refused  expected
nii-il04-nouns.l4                              0         0       0        0         0
nii-il04-published-figures.l4                  0         0       0        0         0
nii-il04-tests-expected-red.l4                14        26      14        0        14
nii-il04-tests.l4                              0       120       0        0         0
nii-s1-definitions.l4                          0         0       0        0         0
nii-s334-interpretation.l4                     0         0       0        0         0
nii-s337-rates.l4                              0         0       0        0         0
nii-schedule-j-tables.l4                       0         0       0        0         0
nii-schedule-j.l4                              0         0       0        0         0
TOTAL (9 modules)                             14       146      14        0
```

`check.sh` exit 0.
The 14 errors are the 14 failed assertions of `nii-il04-tests-expected-red.l4`, which `check.sh`'s `expected_failed` table and `encoding.json`'s `expected_red` both name with that count; there is no other error.
They were predicted before that module was first run, and the run failed exactly those 14, read line by line from the diagnostics (none is "could not be evaluated"):

- **10 of 36 totals checks.** Schedule J's printed totals row does not equal the sum of the items above it in these cells:
  - temporary version, as printed: column C above the threshold, employee (printed 14.50, items 14.39); column D upper part (7.00, items 4.67);
  - temporary version, as read in 2024-2027: the same two (14.60 against 14.49; 7.00 against 4.67);
  - permanent version, as printed: column C above, employee (14.50 against 14.39); column C not above, employee (3.85 against 4.16); column D upper part (7.00 against 4.67);
  - permanent version, as read in 2024-2027: the same three (14.60 against 14.49; 3.95 against 4.26; 7.00 against 4.67).
  The other 26 cells agree.
- **4 of 4 composites above the threshold.** The National Insurance Institute's rate pages print, for 2026, composites the items of the 2026 version do not reach: employee 14.6% (items 14.49); employee's deduction 7% (items 4.67); controlling shareholder 14.17% (items 14.12); controlling shareholder's deduction 6.79% (items 4.46).

Both families are findings about the source, not defects of the encoding (fork F4, open questions 1-2).
`nii-il04-tests.l4`: 120 assertions, 120 satisfied. The first 116 were satisfied on the first run that evaluated them; four more were added after it, when ss 341 and 343 were found to displace s 337 (three refusals, and one check that the s 343 flag leaves a case without the work-injury branch at its ordinary 306.2999), and were satisfied on their first run. No expected value was changed after any run.
(Before that run, four test helpers were renamed because they used a parameter name as a mixfix keyword, and two self-employed boundary scenarios were corrected to test the boundary their comments named: 11.9 hours became 19.9, and an income of 2,034.89 became 6,782.99.)

Every run also prints two Warnings that differing copies of `prelude` and `daydate` exist under `~/.local/share/jl4/libraries/`; the binary uses its embedded copies, and the warnings are not errors.

**The harness can fail.** In a scratch copy, two expected values in the tests module were altered (306.2999 to 306.3; 333 to 334): `check.sh` reported 2 failed and exited 1.

**Mechanical checks** (scripts in `tools/`, run with `python3 -I`):

- `tools/srcquote.py SOURCE FILE.l4…` regenerates every `-- src:N | …` comment from line N of the source; re-running it over every module changed nothing.
- `tools/schedule_j.py SOURCE OUT.l4` generates `nii-schedule-j-tables.l4` from the two tables of Schedule J; re-running it (then `srcquote.py`) reproduces the deposited module byte for byte. It stops on any cell whose shape it does not recognise.
- `tools/hebcheck.py SOURCE FILE…` checks that every run of Hebrew outside a `src:` line occurs verbatim in the source; it passes on every `.l4` module, `BRIEF.md`, this file and `encoding.json`, and fails on a planted invented string.

The convention for the first and last of these follows row `legalese-2026-10-il-03` of the Income Tax Ordinance; these copies are self-contained and also reduce the schedule templates that row did not meet.

## 1. What is encoded and what is not

**Encoded:** s 334(a), its three definitions and both update paragraphs, and s 334(b); s 337(a)(1), (a)(2), (b) and (c); Schedule J in full, both tables, all ten items, all nine figure columns and both totals rows, with the 2024-2027 figures the editors note in item 4 and the totals; and from s 1, "employee" (with "employer"), "self-employed person", "the average wage" (with "compensation", "the compensation rate" and "update day"), "the index", "tax year" and "the Minister".

**Years answered:** contribution months from **January 2026** (assumption A1).
For 2026 the encoding computes a contribution end to end, using the reduced collection threshold the Institute publishes; for 2027 and later it computes from a threshold the caller supplies, and declines by name to supply one itself.

**Not encoded:** who pays which branch (s 335); what counts as income and its maximum, minimum and exemptions (ss 344-351, s 348 and Schedule K, row IL-05); the employer's deduction (s 342, row IL-05); the special work-injury and maternity rates (s 340); the reduced rates by order (s 341) and the reduced work-injury contributions of large employers (s 343), each of which declines a case it reaches; the payment period (s 336); s 2's adjustment of the average wage; Schedule A; the Treasury allocation (s 32).
Each of these that feeds a provision in scope enters as an **input**, with its citation in the nouns module.

**Figures not in the text** come from the National Insurance Institute's own pages, fetched 2026-10-06 with sha256 recorded (section 7): the 2026 reduced collection threshold (7,703) and the 2026 average wage (13,566 under s 1; 13,769 under s 2).
The consumer price index could not be fetched; it is an input with no default.

## 2. Coverage table

Line numbers are lines of `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.

**Totals.** s 334, s 337 and Schedule J: **24 encoded, 3 inert, 0 out-of-scope, 0 deferred** (27 rows).
s 1: **9 encoded** (of which 4 as inputs or input conventions), **60 out-of-scope**, 0 deferred (69 rows, one per definition line).
Provisions outside the slice that the slice refers to, or that displace it: **14 out-of-scope** rows, each with its reason.
Enacted amending Laws (added 2026-10-07): **8 encoded** rows, below.
Altogether **41 encoded, 3 inert, 74 out-of-scope, 0 deferred** (33, 3, 74 and 0 before the repair).

### s 334, s 337 and Schedule J

| provision | line | gist | disposition | where |
| --- | --- | --- | --- | --- |
| Chapter 15 heading, Sign A heading | 3598-3599 | "Chapter 15: insurance contributions", "Sign A: general provisions" | inert | `src:` comment heading `nii-s334-interpretation.l4` |
| s 334 heading and amendment tag | 3601 | interpretation; tag תשפ״ה־7 | encoded (as the vintage boundary) | `section 334(a) as it stood before 1 January 2026 is not in the deposited text` |
| s 334(a) chapeau | 3602 | "in this Chapter –" | inert | comment; the module is the Chapter's interpretation |
| s 334(a) "תקופת תשלום" | 3603 | payment period | encoded (a carrier of words) | `s 334(a) — "payment period"` |
| s 334(a) "מועד תשלום" | 3604 | payment date | encoded (a carrier of words) | `s 334(a) — "payment date"` |
| s 334(a) "מדרגת גבייה מופחתת" | 3605 | 7,522 NIS, updated on 1 January each year | encoded | `the sum printed in section 334(a)`, `s 334(a) — the reduced collection threshold for a month in` |
| s 334(a) "מדרגת גבייה מופחתת" (1) | 3606 | 2026-2028: by the rise in the index | encoded | `s 334(a)(1) — the threshold on 1 January of` |
| s 334(a) "מדרגת גבייה מופחתת" (2) | 3607 | from 2029: by the rise in the average wage | encoded | `s 334(a)(2) — the threshold on 1 January of` |
| s 334(b) | 3608 | wage fixed by a Law or Knesset resolution: an employee; the payer the employer | encoded (the employee limb; the employer limb is a fact, F14) | `s 334(b) — the person is an employee for Chapter 15` |
| s 337 heading and tags | 3625 | rate of insurance contributions | inert | `src:` comment |
| s 337(a)(1) | 3626 | employee: monthly, Schedule J percentages of monthly income | encoded | `s 337(a)(1) — the monthly contributions for` (two arities) |
| s 337(a)(2) | 3627 | other insured: annual, of annual income divided into advance periods | encoded (monthly periods; others declined, F8) | `s 337(a)(2) — the contributions for each advance period, for`, `s 337(a)(2) — the annual contributions for` |
| s 337(b) | 3628 | the Minister's power to change the rates by order, and its conditions | encoded (as the test whether an order is within the power) | `s 337(b) — the order is within the Minister's power` |
| s 337(c) | 3629 | a change carries proportionally to the s 342(c) deduction | encoded (F9) | `s 337(c) — the deduction of` |
| Schedule J heading, references, sub-heading | 4709-4711 | "לוח י׳"; ss 28, 32, 337-342; rates for April 2011 onward | encoded (the sub-heading fixes the year axis, F1) | `nii-schedule-j.l4` heading; nouns `calendar year of the month` |
| Schedule J temporary table: tags and label | 4713-4714 | "(הוראת שעה לשנים 2025–2026)" | encoded (as the 2026 arm; 2025 declined, A1) | `Schedule J — the version for a contribution month in` |
| Schedule J temporary table: column headings | 4716-4719 | columns A-E; C: above / not above × three columns; D: above 60% of the average wage / not above the threshold; E: Treasury | encoded | nouns `A row of Schedule J`; `the column C cell for`; `where column D's upper part begins in` |
| Schedule J temporary table: items 1-10 | 4720-4729 | ten items, nine figure columns | encoded (generated) | `Schedule J (temporary version), item 1` … `item 10` |
| Schedule J temporary table: item 4 note | 4723 | 2.06 in 2024-2027 | encoded (A3) | `Schedule J (temporary version), item 4, with the figures noted for 2024-2027` |
| Schedule J temporary table: totals | 4730 | totals row, with its note | encoded (as data; compared in the red module) | `Schedule J (temporary version), totals as printed`, `… as read in 2024-2027` |
| Schedule J permanent table: label | 4732 | "(הנוסח הקבוע)" | encoded (the 2027 and 2028-on arms) | `Schedule J — the version for a contribution month in` |
| Schedule J permanent table: column headings | 4734-4737 | as the temporary table, but column D's upper part is "above the reduced collection threshold" | encoded | as above |
| Schedule J permanent table: items 1-10 | 4738-4747 | ten items | encoded (generated) | `Schedule J (permanent version), item 1` … `item 10` |
| Schedule J permanent table: item 4 notes | 4741 | 2.06 and 0.47 in 2024-2027 | encoded (A3) | `Schedule J (permanent version), item 4, with the figures noted for 2024-2027` |
| Schedule J permanent table: totals | 4748 | totals row, with its notes | encoded (as data; compared in the red module) | `Schedule J (permanent version), totals as printed`, `… as read in 2024-2027` |
| Schedule J: "–" cells | 4720-4747 | no figure printed | encoded (NOTHING; a branch paid with a dash is declined, F10) | `the percentage in column C of`, `the percentage in column D of` |
| Schedule J column D, applied | 4717-4718, 4735-4736 | what the deduction columns apply to | encoded (revised 2026-10-07: as the enacted headings say from 2026, the upper part from the threshold, F3; before, the temporary version's "gap" was declined) | `the column D deduction under` |

### Enacted amending Laws (added 2026-10-07)

| provision | where | gist | disposition | where in the encoding |
| --- | --- | --- | --- | --- |
| Amendment 252 ss 6, 7(a) | SH 3347 pp. 177 | commencement 1.1.2025; the temporary provision for contributions in respect of 2025 and 2026, to 31.12.2026 | encoded (as the 2026 arm, and the reason 2025 differs) | `Schedule J — the version for a contribution month in` |
| Amendment 252 s 7(a)(3) | SH 3347 p. 177 | replaces the lower sub-columns of columns C and D only | encoded (the temporary versions; F3, F18) | `nii-schedule-j.l4` |
| Amendment 252 s 7(a)(3)(a), item 2, neither | SH 3347 p. 177 | 0.17 as enacted for 2025 | encoded (as data; 2025 not answered) | `Schedule J (temporary version), item 2, as enacted for 2025` |
| Amendment 252 s 7(b) | SH 3347 p. 178 | extension by order to 2027, then 2028 | encoded (as an input, default no order: A8, F20) | the version rule and s 337 entry points with the order argument |
| 2025 budget-year Law s 19(2) | SH 3384 p. 396 | inserts "reduced collection threshold" into s 334(a) | encoded (the vintage boundary of s 334(a)) | `section 334(a) as it stood before 1 January 2026 is not in the deposited text` |
| 2025 budget-year Law s 19(6) | SH 3384 p. 396 | Schedule J "everywhere": 60% of the average wage becomes the threshold | encoded (F3) | the version flags |
| 2025 budget-year Law ss 20(1), 21 | SH 3384 p. 396 | 0.17 to 0.16; commencement 1.1.2026 | encoded (the 2026 figure, and the vintage boundary) | tests; `Schedule J as it stood before 1 January 2026 is not in the deposited text` |
| Economic Efficiency Law 5783-2023 s 24 | SH 3045 p. 169 | 2024-2027: item 4 at 2.06 and 0.47, totals 14.60 and 3.95 | encoded (as the "read in 2024-2027" versions; A3) | `Schedule J (… version), item 4, with the figures noted for 2024-2027` |

### s 1, every defined term

"Used" means the term occurs in the text of s 334, s 337 or Schedule J, or inside a definition this row encodes; it was checked by searching those lines for each term.

| term | line | used by this row's provisions? | disposition | where, or why not |
| --- | --- | --- | --- | --- |
| בעל שליטה | 122 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| המוסד | 123 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| המועצה | 124 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| המינהלה | 125 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| השר | 126 | yes | encoded (a carrier of words) | `s 1 — "the Minister"`; s 337(b)'s order record |
| ועדת העבודה והרווחה | 127 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| בית הדין לעבודה | 128 | no | out-of-scope | The Institute's organs, the Minister's committee and the labour court: no provision in this row names them. |
| אשתו | 129 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גיל הפרישה | 130-132 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גמול פרישה | 133 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גמלה | 134 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| גמלת אזרח ותיק מיוחדת | 135 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| דמי הסתגלות מיוחדים | 136 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| הסכם בדבר מתן גמלאות אזרח ותיק ושאירים מיוחדות | 137 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| חבר קיבוץ מתחדש | 138 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| חברת מעטים | 139 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| חוק ביטוח בריאות | 140 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק בית הדין לעבודה | 141 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הבטחת הכנסה | 142 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק האימוץ | 143 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הגנת השכר | 144 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק המשטרה | 145 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הנוער | 146 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הנכים | 147 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק העונשין | 148 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק העמותות | 149 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק השבות | 150 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק חדלות פירעון ושיקום כלכלי | 151 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק חופשה שנתית | 152 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק חיילים משוחררים | 153 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק יישום תכנית ההתנתקות | 154 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק הכניסה לישראל | 155 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק משפחות חיילים | 156 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק נכי המלחמה בנאצים | 157 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק נכי רדיפות הנאצים | 158 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק נפגעי פעולות איבה | 159 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק עבודת נשים | 160 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק פיצויי פיטורים | 161 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות אזרחי | 162 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות בטחון | 163 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות בתי הסוהר | 164 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות המדינה | 165 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירות התעסוקה | 166 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שירותי הכבאות | 167 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק שכר מינימום | 168 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| חוק תגמול לחייל | 169 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| ילד | 170 | no | out-of-scope | The word appears in this row's provisions only inside the branch name "ילדים" (children); the definition decides who is a child for the children's benefits (row IL-06), not any rate. |
| מדד | 171 | yes | encoded (as an input convention) | index readings are arguments of the s 334(a)(1) rules |
| מעביד / מעסיק | 172 | yes | encoded | `s 1 — the person is an employee` (the core limb) |
| משרת בשירות לאומי–אזרחי | 173 | no | out-of-scope | National, civic or community service: used by the provisions on volunteers and service members, none of which is in this row. |
| מתנדב בשירות לאומי או בהתנדבות קהילתית | 174 | no | out-of-scope | National, civic or community service: used by the provisions on volunteers and service members, none of which is in this row. |
| הסכום הבסיסי | 175-202 | no | out-of-scope | The basic amount: used by Schedule K's maximum income (row IL-05) and by the benefits (its paragraph (2), the child allowance, by row IL-06); not by ss 334, 337 or Schedule J. |
| עגונה | 203 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| עובד | 204 | yes | encoded | `s 1 — the person is an employee`, `s 1 — the family-member limb of "employee"` |
| עובד לשעה | 205 | no | out-of-scope | A casual employee: used by the provisions on short engagements (outside this row); ss 334, 337 and Schedule J do not distinguish one. |
| עובד עצמאי | 206-211 | yes | encoded | `s 1 — a self-employed person in the period:` and its three limbs |
| פיצוי | 212 | yes | encoded (as an input) | the compensation rate in `The data for an update of the average wage` |
| פקודת החברות | 213 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| פקודת הנזיקין | 214 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| פקודת השותפויות | 215 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| פקודת פשיטת הרגל | 216 | no | out-of-scope | A short title for another enactment. None of ss 334, 337 or Schedule J cites it. |
| קיבוץ מתחדש | 217 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| קיבוץ שיתופי | 218 | no | out-of-scope | A status term that s 335 or the contribution rules for kibbutzim and closely-held companies use; s 335 is an input to this row and the kibbutz rules (ss 3, 3A and Chapter 15's special rules) are not in it. |
| קצבת התאמה | 219 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |
| שיעור הפיצוי | 220 | yes | encoded (as an input) | same |
| שירות לאומי / התנדבות קהילתית / שירות אזרחי | 221 | no | out-of-scope | National, civic or community service: used by the provisions on volunteers and service members, none of which is in this row. |
| השכר הממוצע | 222-226 | yes | encoded | `s 1 — the average wage on an update day, from`, its two limbs, `s 1 — the update days of the average wage in tax year` |
| שנת מס | 227 | yes | encoded (as an input convention) | a tax year is a calendar year (fork F12) |
| תקופת אכשרה | 228 | no | out-of-scope | A benefit-side term (a benefit, an age, a qualifying period, a family status). The contributions arithmetic of this row does not use it; the benefit rows do. |

### Provisions outside the slice that the slice refers to, or that displace it

| provision | line | referred to by | disposition | reason, and how this row takes its result |
| --- | --- | --- | --- | --- |
| s 335 | 3610-3620 | s 337(a)(1)-(2) ("the contributions under section 335") | out-of-scope | It decides, branch by branch, for whom contributions are paid (non-resident employees maternity only; no unemployment or insolvency for a controlling shareholder in a closely-held company; and so on). Not assigned to this row. Its answer is the input `branches for which contributions are payable under section 335`; the tests state the lists they read from it and the Institute's composites confirm two of them. |
| s 336 | 3622-3623 | s 334(a) "payment period"; s 337(a)(2) by implication | out-of-scope | It makes a payment period a month unless the Minister sets otherwise. Not assigned to this row. Used only as the reason s 337(a)(2) is encoded for monthly periods (F8). |
| s 340 | 3637-3653 | Schedule J column C heading ("sections 337(a) and 340(a)"); s 340(a)(2) for work injury of one who is neither | out-of-scope | The work-injury and maternity rates for particular groups (other insured persons at rates the Minister sets, residents of the Area). Not assigned to this row. A work-injury branch in the neither column is declined with s 340(a)(2) named. |
| s 342 | 3658-3676 | Schedule J column D heading; s 337(c) | out-of-scope (row IL-05) | The employer's duty to pay and to deduct. Column D's figures are encoded as data, and what its headings say they apply to; who deducts, and for which branches, is row IL-05's, and enters here as an input list. |
| s 348 and Schedule K | 3762; 4751- | the income on which contributions are computed | out-of-scope (row IL-05) | The maximum and minimum income. The income inputs are taken after them. |
| ss 344-351 (other than 348) | 3684-3836 | "his monthly income", "his annual income" | out-of-scope | What counts as income for contributions, exemptions (the Institute's worked example removes 3,442 NIS before the rates apply), and the special cases. The income inputs are taken after them. |
| s 2 | 230-239 | s 1 "the average wage" | out-of-scope | Changes the calculation of the average wage "for benefits and contributions" for exceptional pay months. The rules take the average wage as an argument; which figure to supply is fork F5. |
| s 32 | 476-514 | Schedule J column E heading | out-of-scope | The Treasury allocation. Column E's figures are encoded as data only. |
| s 28 | 448-451 | Schedule J's reference note (line 4710) | out-of-scope | The branch accounts: s 28(a) credits every contribution to the branches' accounts "in the ratio of the rates in Schedule J". No figure in this row is applied under it; it is evidence for fork F4. |
| Schedule A | 4360-4365 | s 1 "self-employed person" (3) | out-of-scope | "15% of the average wage as at the first of the quarter's first month"; the sum is an argument of the definition, and the tests compute it from this line for 2026 as a labelled scenario value. |
| ss 66-68 | — | (none; the children branch funds them) | out-of-scope (row IL-06) | The child allowance. Not referred to by this row's provisions; listed because the lead named it. |
| the s 335(b) "insured" of s 65(a)(1) | — | through s 335(b) | out-of-scope (row IL-06 encodes s 65) | Decides who pays the children branch; enters through the s 335 branch list. |
| s 341 | 3654-3656 | displaces s 337 ("notwithstanding sections 337 and 340") | out-of-scope | The Minister's reduced rates by order (an order of 5759-1999 is noted). Neither the section nor the order is in this row. A case it reaches is declined by name, on an input flag (`reduced rates under an order made under section 341 apply to this income`). |
| s 343 | 3677-3680 | displaces the work-injury rate for an approved employer | out-of-scope | Reduced work-injury contributions for an employer of at least 500 employees. Not in this row. An employee's month with this flag and the work-injury branch is declined by name. |

## 3. Assumptions

**A1. Contribution months from January 2026 only; earlier months are declined by name.**
s 334 carries one amendment tag (תשפ״ה־7) and Schedule J's tables carry תשפ״ה־3, תשפ״ה־7 and תשפ״ה־8 (source lines 3601, 4713).
The tags count entries in the year's list of amending Laws at the head of the source (line 7).
For 5785 that list has 11 entries but the tags in the file run to ־12, so the one entry with a double page reference, "395, 395" (the Law for the 2025 budget year), counts twice: tags ־7 and ־8 are that Law, ־3 is Amendment 252 with its temporary provision.
The check: tags ־9 to ־12 then fall on Amendment 257, Amendment 258, Amendment 7 of the National-Civic Service Law and the Economic Assistance Law, and the provisions carrying ־11 (ss 1, 158, 160, 163, 238, 287, 348) include s 1, which defines a person serving in national-civic service; that is consistent with the Law being an amendment of the National-Civic Service Law.
The Law for the 2025 budget year, as Hebrew Wikisource prints it (fetched 2026-10-06, section 7), says in its s 21 that its National Insurance chapter (ss 19-20, the second amending "Amendment 252 and temporary provision") commences on 1 January 2026.
So the deposited s 334 and Schedule J are the text in force from 1 January 2026; what they said in 2025 is not in the sources, and answering 2025 from the amended text would borrow one vintage's figures for another.
The identification is by counting and by the commencement section of a Wikisource page; the Laws themselves could not be fetched from the Knesset (section 7).
**(added 2026-10-07)** Verified against the enacted Laws: the 2025 budget-year Law s 19(2) inserts the threshold's definition, s 19(6) changes Schedule J's headings, s 20(1) changes item 2's lower figure for those who are neither from 0.17 to 0.16, and s 21 commences all of it on 1 January 2026. So the 2025 text demonstrably differs (0.17; every heading "60% of the average wage"), and the refusal of 2025 is required by the sources, not only by the brief.

**A2. The year of the contribution month is an explicit input, and the dated arms select on it.**
The skill's rule-effective-time axis (`RULES EFFECTIVE DATE`) was not used.
Schedule J's own sub-heading speaks of the month for which contributions are paid ("rates for April 2011 onward"), and s 334(a) updates the threshold "on 1 January of every year"; the year belongs to the case, and every dated arm carries its citation.
Row IL-03 made the same choice for the same kind of reason.

**A3. The editors' notes that date the temporary provisions are relied on.**
The text itself prints two tables; which governs when is said only by the editors' labels ("(הוראת שעה לשנים 2025–2026)", "(הנוסח הקבוע)") and the item-4 notes ("(הוראת שעה בשנים 2024 עד 2027: …)").
Without them there is no rule choosing a table, so they are used, as aids, and every use is cited.
The Institute's pages corroborate the 2026 selection: its published composites for the self-employed (4.47 / 12.83, and 0.26 / 0.78 for work injury alone) and for those who are neither (6.92 / 7.00), and the employee's 5.55 and 1.04 up to the threshold, are exactly the sums of the 2026 version's items.
They also date the employee's 14.6% composite "from 01.02.2025", where the note says 2024; that difference touches only months this row declines.
**(added 2026-10-07)** Each note now has an enacted source: the temporary table is Amendment 252 s 7 (for contributions in respect of 2025 and 2026), and the item-4 and totals figures are the Economic Efficiency Law 5783-2023 s 24 (1 January 2024 to 31 December 2027). The Institute's "from 01.02.2025" for the 14.6% composite remains unexplained by either.

**A4. Published figures.**
Used: the reduced collection threshold for 2026 (7,703), and the 2026 average wage under s 1 (13,566) and under s 2 (13,769), each from the Institute's pages with URL, time and sha256 (`nii-il04-published-figures.l4`).
The consolidation's editorial notes give the same three figures (lines 3605, 226, 233).
Not used: any figure for 2027 on, which did not exist at retrieval.

**A5. Classifications outside the slice are inputs.**
Which branches a person pays (s 335); the income on which contributions are computed (with ss 344-351, s 348 and Schedule K applied); whether a relationship is one of employment; the Schedule A sum; the number of advance periods; the consumer price index; the CBS wage figures and the compensation rate; whether an order under s 341, or an approval under s 343, reaches the case.
Each is recorded somewhere a caller can read it (phrasebook 1.6, reading 1).

**A6. Nothing is rounded.**
Neither s 334 nor s 337 nor Schedule J says to round; contributions and the updated threshold are exact (F7).

**A7. Each branch is listed once, and income is not negative.**
These are input conventions stated in the nouns module, not checked.

**A8. No order under Amendment 252 s 7(b) (added 2026-10-07).**
The rules that take only a year assume the temporary provision was not extended to 2027 or 2028: it ends on 31 December 2026 by its own terms, and no extension order was known at retrieval (an order must be brought to the Knesset Labour and Welfare Committee at least two months before the year). Callers who know of an order use the entry points that take it as an argument.

## 4. Fork register

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | Schedule J sub-heading (4711), label (4714) | "For the years 2025-2026": years of what? | (i) the calendar year of the month for which contributions are paid; (ii) the year of payment; (iii) the tax year of the income | **(i)**: the sub-heading dates the rates by the month contributions are "for" ("בעד אפריל"). (i) and (iii) coincide for an employee's monthly contributions. |
| F2 | items 4 and totals (4723, 4741, 4730, 4748) | The 2024-2027 notes: which table do they modify in which year? | (i) each table's own notes apply while that table is in force (temporary in 2026, permanent in 2027); (ii) the notes apply to both tables in all of 2024-2027 | **(i)**, and it makes no difference: both tables note the same 2.06 above the threshold; only the permanent table notes 0.47 below it, and the permanent table governs only 2027 of those years. The temporary table's 0.60 below the threshold carries no note and stands. |
| F3 | Schedule J temporary version, column D (4718) | **(revised 2026-10-07)** The consolidation prints column D's upper heading in the temporary table as "above 60% of the average wage" and the lower as "not above the reduced collection threshold"; in 2026 they do not meet (7,703 against 8,139.6 or 8,261.4). | (i) as printed: no figure for the part between; (ii) the upper heading is stale, and the upper part begins at the threshold; (iii) the lower part runs up to 60% of the average wage | **(ii), on the enacted Laws.** Amendment 252 s 7(a)(3) replaced only the lower sub-columns, so the upper sub-column is the principal Law's, and the 2025 budget-year Law s 19(6) changed "60% of the average wage" to "the reduced collection threshold" everywhere in Schedule J from 1 January 2026 (s 21). Line 4718's upper heading is a stale copy. The Institute applies the employee's 7% "on the part of the wage above the reduced collection threshold", and row IL-05 read the texts the same way. *Before the repair:* (i), declined, with every 2026 wage above 7,703 refused. |
| F4 **(0.3.0: ruled by Meng on 2026-10-07: the printed totals by default, the items kept as the alternative; "Version 0.3.0" above. The choice recorded in this row, (i), is now the alternative.)** | totals rows (4730, 4748) | Ten printed totals differ from the sums of the items above them (section 0). Which governs? | (i) the items: s 335 imposes contributions branch by branch, s 337(a) applies "the rates under section 335", and s 28(a) credits contributions to the branches' accounts "in the ratio of the rates in Schedule J" (line 449); (ii) the totals: the Institute charges composites equal to them (14.6, 7.00) | **(i) for computing; the totals are data and are compared, red, in their own module.** Consequence: an employee in 2026 is charged 14.49% above the threshold here where the Institute charges 14.6%, and the deduction on the upper part sums to 4.67% where the Institute deducts 7%. The two items of evidence point in opposite directions; this is open question 1. **(added 2026-10-07)** Two enacted precedents: the 2025 budget-year Law s 20(1) changed a row so that it met its printed total (0.17 to 0.16), and the Economic Efficiency Law 5783-2023 s 24 moved item 4 and the totals together by 0.10. Both treat a total as tracking its items; neither says which is right where they already differ, and the gaps (0.11, 2.33, 0.31) predate both. Choice unchanged. |
| F5 | s 1 "the average wage" (222-226), s 2(b) (236) | Which figure is "the average wage" in Schedule J's column D heading, in "self-employed person" (2), and in s 334(a)(2)? | (i) the s 1 figure (13,566 for 2026); (ii) the figure as calculated under s 2, which s 2(b) applies "for benefits and contributions" (13,769) | **not decided**: every rule takes the average wage as an argument. The tests supply 13,566 (the s 1 figure, which the editors' note at line 226 also gives). The column D gap (F3) exists under either. The Institute publishes both, each "for contributions". **(added 2026-10-07)** After the F3 repair Schedule J no longer reads the average wage at all; the fork remains for "self-employed person" (2) and s 334(a)(2). Row IL-05 (its fork F1) found that every Institute figure for Chapter 15 it checked (3,442; 143; 171; the 2025 table's 3,134, 627 and 1,880) fits the s 2 figure and not the s 1 figure, which is evidence for (ii) in contributions; the s 1 definition of "self-employed person" serves benefits as well, so the rules still take the figure as an argument. |
| F6 **(0.4.0: ruled by Meng on 2026-10-07 (TRIDENT): a fall is declined by default, all three readings kept by name; "Version 0.4.0" above. The choice recorded in this row, (i), is now an alternative.)** | s 334(a)(1)-(2) (3606-3607) | If the index or the average wage falls, does the threshold fall? | (i) yes, the rate of rise is negative and is applied; (ii) no, "עליית" (rise) counts only rises; **(0.4.0)** (iii) neither is decided: the text provides for a rise and says nothing of a fall, so the case is declined | **(i)**: the update is a rate computed from two readings; a test shows a 1% fall lowering 8,000 to 7,920. **(0.4.0)** Now **(iii)** by default; (i) and (ii) are answered when a caller names them. |
| F7 | s 334(a) | Is the updated threshold rounded? | (i) no; (ii) to the shekel, as the Institute publishes it | **(i)**: the section says nothing about rounding. The published 2026 figure is a whole number; the encoding uses it as published for 2026 and computes unrounded for any later year a caller supplies readings for. |
| F8 | s 337(a)(2) (3627) | "annual income divided into the periods set for advances": equal shares? and does the threshold scale for a period longer than a month? | (i) equal shares, threshold per monthly period, other periods declined; (ii) the threshold scaled by the period's length | **(i)**: s 336 makes the payment period a month unless the Minister sets otherwise, and the Institute applies the threshold to monthly income; the text does not say how it scales. |
| F9 | s 337(c) (3629) | "in the same way and proportionally": by what? | (i) the deduction multiplied by the ratio of new rate to old; (ii) the deduction moved by the same absolute change | **(i)**: "proportionally" is a ratio. Which column C figure pairs with which column D figure is left to the caller's arguments; the natural pairing is the employee's figure on the same part of the wage. A change from a rate of 0 is declined. |
| F10 | Schedule J "–" cells | Is a dash a rate of 0? | (i) no figure: a branch paid with a dash in the person's column is declined; (ii) zero | **(i)**: where s 335 makes a person pay a branch, a dash leaves the schedule silent, and in one case the Law supplies the rate elsewhere (s 340(a)(2)); a zero would hide that. The totals check is the one place a dash adds nothing, because that is what a total of printed figures means. |
| F11 | s 1 "employer" (172), "employee" (204) | The family-member limb of "employee" expressly has no employment relationship, but "employer" is defined by one. Is the relative an employer? | — | **not decided**: no rule in this row turns on it. It matters to s 342 (row IL-05). |
| F12 | s 1 "tax year" (227) | A special assessment period under the Income Tax Ordinance. | — | **not modelled**: a tax year is a calendar year. |
| F13 | s 1 "employee" (204) | The definition "includes" a family member; what is its core? | (i) the ordinary meaning, a person employed within an employment relationship, which is also how s 1 defines the employer; (ii) open-ended | **(i)**, with the relationship itself an input. |
| F14 | s 334(b) (3608) | "and the person liable to pay the wage is regarded as his employer" | — | Encoded as a comment: no rule in this row needs to name the employer. |
| F15 | Schedule J items 1-2 | Item 2 is "maternity – an insured person who is neither employee nor self-employed". Is it a tenth branch? | (i) the same branch, the column decides which item applies; (ii) a separate branch | **(i)**: s 335 imposes maternity contributions (in (a) and (i)) as one branch; items 1 and 2 never both print a figure in one column (a test checks this for every version and column). |
| F16 | s 1 "self-employed person" (207-209) | "לפחות" (at least), "לא פחתה מ" (not less than) at the boundary | — | **inclusive** (`AT LEAST`); tests sit on each boundary. |
| F17 | Schedule J column C (4718) | Is the rate applied to the whole income according to its band, or to each part? | (i) marginal, each figure "on the part"; (ii) slab | **(i)**: the headings say "on the part above" and "on the part not above". At exactly the threshold all the income is "not above". |
| F18 | Amendment 252 s 7(a)(3) | **(added 2026-10-07)** The temporary lower sub-columns Amendment 252 inserts carry their own headings, "not above 60% of the average wage"; the 2025 budget-year Law s 20 amended that section's figures but not those headings, and s 19(6) amends "Schedule J, everywhere". Read literally for 2026 the lower part would run to 60% of the average wage while the upper part starts at the threshold: an overlap. | (i) the threshold: s 19(6) reaches Schedule J as read under the temporary provision; (ii) literal: the lower part runs to 60% of the average wage | **(i)**, the only workable reading, and the one the consolidation (line 4718) and the Institute follow. Not settled by any text read. |
| F19 | item 4, employee, not above the split, 2026 (4723) | **(added 2026-10-07)** Two temporary provisions reach the same cell in 2026: the Economic Efficiency Law 5783-2023 s 24 reads 0.47 into the principal sub-column, and Amendment 252 s 7(a)(3) replaces that sub-column with its own (0.60). | (i) Amendment 252's sub-column, 0.60; (ii) 0.47 | **(i)**: s 7(a)(3) replaces the whole sub-column, and is the later Law; the consolidation prints 0.60, and the Institute's 2026 composite (5.55) includes it. |
| F20 | Amendment 252 s 7(b) | **(added 2026-10-07)** The extension is "one year at a time": does an order for 2028 presuppose one for 2027? | — | **not checked**: the order is an input per year. |

**Where I looked for others and found none:** s 334(a)'s two carrier definitions; s 337(b)'s conditions (each a fact the order records); Schedule J's column E (data only).

## 5. Answer table

Composite percentages are sums of the items of the version in force, for the branch lists the tests state (all nine branches for an employee; seven for the self-employed; six for one who is neither; six deduction branches for column D).
**(0.3.0)** From version 0.3.0 the rules read the printed totals by default (the figures in brackets below, "printed"), and the items by name; the worked figures below are the items'.
"Declined" means a named `REFUSE`.

| | 2025 | 2026 | 2027 | 2028 on |
| --- | --- | --- | --- | --- |
| Schedule J version | declined (A1) | temporary, with item 4 at 2.06 | permanent, with item 4 at 2.06 and 0.47 | permanent as printed |
| reduced collection threshold | declined | 7,703 (published) | supplied by the caller (index-updated; declined if not) | supplied by the caller (2029 on: wage-updated) |
| employee, not above / above | declined | 5.55 / 14.49 (printed totals 5.55 / 14.60) | 4.26 / 14.49 (printed 3.95 / 14.60) | 4.16 / 14.39 (printed 3.85 / 14.50) |
| self-employed, not above / above | declined | 4.47 / 12.83 | 2.87 / 12.83 | 2.87 / 12.83 |
| neither, not above / above | declined | 6.92 / 7.00 | 4.61 / 7.00 | 4.61 / 7.00 |
| column D, not above / upper part | declined | 1.04 / 4.67 (printed 1.04 / 7.00); upper part from the threshold (F3, revised 2026-10-07; before: from 60% of the average wage) | 0.40 / 4.67 (printed 0.40 / 7.00) | 0.40 / 4.67 (printed 0.40 / 7.00) |
| with an order under Amendment 252 s 7(b) (added 2026-10-07) | declined | (no order needed) | the temporary lower sub-columns: employee 5.55 / 14.49, self-employed 4.47 / 12.83, neither 6.92 / 7.00, column D 1.04 / 4.67 | 2028: the temporary lower sub-columns, upper as printed: employee 5.55 / 14.39; 2029 on: declined |

Worked figures the tests assert (2026 unless marked):

| facts | contributions (NIS) |
| --- | --- |
| employee, senior citizens and survivors only, 10,000 | 306.2999 |
| employee, maternity only, 7,703 / 7,704 | 18.4872 / 18.5012 |
| employee, work injury only, 10,000 | 93.5362 |
| employee, all branches, 6,000 | 333 |
| employee, work injury only, 10,000, threshold 8,000 (scenario): 2027 / 2028 | 78.8 / 68.8 |
| neither, the Institute's January 2026 example (base 8,558) | 592.8976 (with health at 5.17%: 1,035.3462; the Institute prints 931.29 + 104.05 = 1,035) |
| self-employed, 240,000 a year in 12 monthly advances | 1,922.0292 a month; 23,064.3504 a year |
| column D, permanent version, wage 10,000, threshold 8,000 (scenario) | 125.4 |
| column D, temporary version, wage 7,000 / 7,703 / 7,704 | 72.8 / 80.1112 / 80.1579 (revised 2026-10-07; before: declined) |
| column D, temporary version, wage 10,000 / 20,000 (added 2026-10-07) | 187.3811 / 654.3811 |
| employee, work injury only, 10,000, threshold 8,000 (scenario), with an order: 2027 / 2028 (added 2026-10-07) | 89.2 / 87.2 |
| self-employed, 2027, 240,000 a year, threshold 8,000 (scenario): with an order / without (added 2026-10-07) | 1,897.2 / 1,769.2 a month |

## 6. Nouns to reconcile at IL-07

Read from the sibling deposit `legalese-2026-10-il-06` (read-only) at the end of this session; nothing here depends on it and nothing in it was changed.

- **The person.** This row: `A person who works` (employment relationship, family-member limb, wage fixed by Law), `A person's occupation in a period` (self-employed limbs), and the two contribution cases. IL-06: `A person` (insured under Chapter 11, resident, a housewife under s 238, …). One insured-person record could carry both; s 335(i) turns on "insured under Chapter 11 other than a housewife and a widow pensioner under s 238", which IL-06 already models.
- **The children branch.** s 335(b) makes "an insured person as defined in s 65(a)(1)" pay the children branch; IL-06 encodes s 65 (`s 65 "insured" (1)`). Here the branch enters through the input list; at IL-07 the two can be joined.
- **Section 1.** Both rows have a s 1 module (`nii-s1-definitions.l4` here; `nii-s1-basic-amount.l4` there) and a published-figures module. They define different terms and should merge into one s 1 module without collision.
- **Published figures.** Both rows take figures from the Institute's pages with the same provenance convention and decline the next year by a named refusal; the refusal texts differ in wording.

## 7. Sources: what was fetched, and what was not

The deposited source was read and its sha256 verified (`78bf47ee…2a97`) on 2026-10-06 before use.
Fetched on 2026-10-06 (curl; bytes not deposited, the site reserving its rights; sha256 of what was fetched):

| what | URL | UTC | sha256 | what it says that this row uses |
| --- | --- | --- | --- | --- |
| NII rates page, employees | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%a9%d7%9b%d7%99%d7%a8%d7%99%d7%9d.aspx` | 14:07:32 | `63457694f21874d7e1eee490811ec86b60c83aff49f733aae6aadb85b9129aba` | threshold 7,703 from 01.01.2026; National Insurance employer 4.51 / employee 1.04 / total 5.55 up to it, 7.6 / 7 / 14.6 above; health 3.23 / 5.17; form 102 "column 2" (controlling shareholder) totals with health 8.71 / 19.34, employee 4.25 / 11.96 |
| NII rates page, self-employed | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9c%d7%a2%d7%a6%d7%9e%d7%90%d7%99%d7%9d.aspx` | 14:07:34 | `5abe5977d369d0da10e26269ab90aec5ae216247b6018e6721ba760fc7d33f22` | 4.47 / 12.83; under 18 or receiving an old-age pension 0.26 / 0.78, "National Insurance only" |
| NII rates page, neither | `https://www.btl.gov.il/Insurance/Rates/Pages/%d7%9e%d7%99%20%d7%a9%d7%90%d7%99%d7%a0%d7%9d%20%d7%a2%d7%95%d7%91%d7%93%d7%99%d7%9d%20%d7%95%d7%91%d7%a2%d7%9c%d7%99%20%d7%94%d7%9b%d7%a0%d7%a1%d7%94%20%d7%a9%d7%9c%d7%90%20%d7%9e%d7%a2%d7%91%d7%95%d7%93%d7%94.aspx` | 14:07:36 | `36c88a5e9666a9410a13dbe50ebdb0778b2653305d0a33688682029edd24d183` | 6.92 / 7; health 5.17; the worked example for January 2026 |
| NII average wage | `https://www.btl.gov.il/Mediniyut/GeneralData/Pages/%d7%a9%d7%9b%d7%a8%20%d7%9e%d7%9e%d7%95%d7%a6%d7%a2.aspx` | 14:08:43 | `fe4d43b1bc1f007839567cbee759f8135558c94c89e3a10a531b5baecaf31b1f` | from 01.01.2026: 13,566 under s 1 and 13,769 under s 2, each for benefits and for contributions; for 2025, contributions 12,379 (s 1) and 12,536 (s 2) |
| Law for the 2025 budget year, Hebrew Wikisource raw text | `https://he.wikisource.org/w/index.php?title=%D7%97%D7%95%D7%A7%20%D7%9C%D7%94%D7%A9%D7%92%D7%AA%20%D7%99%D7%A2%D7%93%D7%99%20%D7%94%D7%AA%D7%A7%D7%A6%D7%99%D7%91%20%D7%95%D7%9C%D7%99%D7%99%D7%A9%D7%95%D7%9D%20%D7%94%D7%9E%D7%93%D7%99%D7%A0%D7%99%D7%95%D7%AA%20%D7%94%D7%9B%D7%9C%D7%9B%D7%9C%D7%99%D7%AA%20%D7%9C%D7%A9%D7%A0%D7%AA%20%D7%94%D7%AA%D7%A7%D7%A6%D7%99%D7%91%202025%20%28%D7%AA%D7%99%D7%A7%D7%95%D7%A0%D7%99%20%D7%97%D7%A7%D7%99%D7%A7%D7%94%29&action=raw` | 14:10:35 | `8ca6d31272e4a29bf481ac8e3d32ce7c44cbfd43562a7401e08ccb7b93b86361` | Chapter E (National Insurance): s 19 amends the Law, s 20 amends Amendment 252 and its temporary provision, s 21 "this chapter commences on 1 January 2026" |

The Institute's pages describe themselves as general information and not the binding text of the Law; they are used as the regulator's published figures and examples, not as law.

**Attempted and failed:** the amending Laws from `fs.knesset.gov.il` (Amendment 252, `25_lsr_5482787.pdf`) returned a 131,618-byte HTML page in place of a PDF, as it did for row IL-03; the Wayback Machine availability API answered 429 (too many requests); the Central Bureau of Statistics price-index API (`api.cbs.gov.il`) timed out after 40 seconds.
Nothing was kept from those responses.
So the consumer price index is an input, and the commencement of Amendment 252's temporary provision was not read.
**(revised 2026-10-07)** Amendment 252 and the 2025 budget-year Law were fetched the same day through the lead's Israeli-IP proxy and are now deposited at `../../registers/source-bundle/amending-laws/` with `SOURCES.json` (commons commit 7737fa8); the Economic Efficiency Law 5783-2023 was fetched through the proxy at 21:39:39 UTC and is not deposited ("Repair 2026-10-07" above has all three, with their sha256). The Central Bureau of Statistics API returned an empty reply through the proxy too, so the index is still an input.

**Observations about the source**, for whoever maintains it:

- Ten cells of Schedule J's totals rows differ from the sums of their items (section 0). The gaps are the same in all four readings of the schedule: 2.33 in column D's upper part, 0.11 in column C above the threshold for an employee, and (permanent version only) 0.31 the other way in column C not above the threshold for an employee. Which cell, if any, is wrong cannot be told from the table.
- The temporary version's column D heading ("above 60% of the average wage") does not meet its other heading ("not above the reduced collection threshold") in 2026 (F3). **(revised 2026-10-07)** On the enacted Laws the upper heading is stale: s 19(6) of the 2025 budget-year Law made it "the reduced collection threshold" from 1 January 2026, and the temporary provision never replaced it.
- s 342(e)(3)-(4) (lines 3669-3670) refer to "טור ה׳ בלוח י׳" (column E) for the employee's deduction rates, where the schedule's column E is the Treasury allocation and column D is the deduction (row IL-05's provision; noted for it).
- Line 3605's editorial note calls 7,522 "nominal for 2025"; the text is in force only from 1 January 2026 (A1), so the note dates the base, not a year the text governed.

## 8. Open questions for a domain expert

1. F4: does the Institute collect the employee's 14.6% (and deduct 7%) above the threshold because the totals row governs, or because the items as enacted differ from the consolidation's? If the consolidation mistranscribes an item, which? **(0.3.0: ruled for the printed totals, 2026-10-07; which item is wrong, if any, is still open.)**
2. F4: for a controlling shareholder in a closely-held company the Institute's composite above the threshold (14.17) exceeds the items without unemployment and insolvency (14.12); is there a rule outside s 335(e)-(f) that explains the 0.05?
3. F3: is the temporary version's column D heading "above 60% of the average wage" in the Law as amended, or a remnant of the threshold's earlier definition that the 2025 budget-year Law did not update? **(answered 2026-10-07 by the enacted Laws: a remnant; F3.)** What remains is F18: do the inserted sub-columns' own headings follow s 19(6)?
4. F5: which average wage does Schedule J (temporary column D), the s 1 self-employed test and s 334(a)(2) use: the s 1 figure or the s 2 figure? **(2026-10-07: Schedule J no longer uses it; the question stands for the other two.)**
5. A3: from which month did the 2.06 work-injury rate apply: January 2024 (the editors' note) or February 2025 (the Institute's composite)? **(2026-10-07: the Economic Efficiency Law 5783-2023 s 24 says 1 January 2024; why the Institute dates the 14.6% composite from 1 February 2025 is still open.)**
7. **(added 2026-10-07)** Was an order under Amendment 252 s 7(b) made extending the temporary provision to 2027 (A8)?
6. F8: are the self-employed's advance periods ever other than months, and if so how does the Institute apply the threshold to them?

## 9. What was not done

- **The independent test pass** (skill step 8) was not run by this encoder: the brief for this row is one session with no sub-agents. **(added 2026-10-07)** It was run afterwards by `fid-il-04` (`DECIDED-ANSWERS.md`, `INDEPENDENT-FINDINGS.md`, `tests-independent.l4`); its results after the repair are in "Repair 2026-10-07". Every expected value was worked out before it was asserted, by a Python computation over the source's cells and the Institute's printed figures that does not use this encoding; no second reader has derived them.
- **HG1**, a human who knows Israeli national insurance reading the modules against the Hebrew, has not been sought.
- **Semi-cleanroom** (ruled 2026-10-06): nothing from the Axiom Foundation, any RuleSpec repository, or the paths the brief lists was read, searched or fetched in this session.

## Comparison with Axiom's RuleSpec (2026-10-06)

Comparison author: `lad-il-04`, one session, no sub-agents, after this row was deposited and independently tested (Meng's semi-cleanroom ruling of 2026-10-06 released the Axiom encoding for this row only).
Nothing in this row's encoding was changed; every divergence below is a finding, and where ours is wrong the repair is proposed, not made.

### What was read

**Axiom**: the local clone `/Volumes/transcend/src/Axiom/rulespec-il/` at commit `95c6f32c87c75e318631cbd77c14b840bc536c15` ("Merge pull request #8 from TheAxiomFoundation/encode/il-nii-contributions", 2026-10-03), read-only.

- `il/statutes/national-insurance-law-1995/section-1.yaml` and `section-1.test.yaml` (the test file is `[]`);
- `section-334.yaml` and `section-334.test.yaml` (7 cases);
- `section-337.yaml` and `section-337.test.yaml` (9 cases);
- `schedule-j/sign-1.yaml` and `schedule-j/sign-1.test.yaml` (the test file is `[]`); `schedule-j/` holds nothing else;
- `docs/ENCODING-GAPS.md` lines 570-637 only: the four entries `schedule-j-2025-2026-deduction-heading-still-says-60-percent-of-the-average-wage`, `schedule-j-rows-do-not-sum-to-printed-totals`, `schedule-j-treasury-column-is-kept-as-printed`, `nii-section-334-rate-of-rise-floor-is-an-interpretation`;
- `.axiom/encoding-manifests/il/statutes/national-insurance-law-1995/` `section-1.json`, `section-334.json`, `section-337.json`, `schedule-j/sign-1.json`;
- `data/coverage/tax-benefit-source-map.json`: the National Insurance Law instrument's scalar fields and its one Schedule J entry;
- `known-missing-money-atoms.yaml`, `known-validation-gaps.yaml`: counted, no entry names these provisions.

`section-337.yaml` imports only `schedule-j/sign-1` and `section-334`, both read; no other Axiom file was needed to understand a value.
`section-337.yaml`'s deferral notes refer to Axiom modules for provisions assigned to row IL-05; their content is not reproduced here.
Locating greps also displayed the heading lines of some out-of-row ENCODING-GAPS entries and three single lines; no body of any of them was read (listed in the report to the lead).

The manifests say `section-1` was generated by `gpt-5.6-terra`, `section-334` and `schedule-j/sign-1` by `gpt-6-astra` (2026-09-29), and `section-337` by a deterministic repair of proof-import hashes over an earlier codex output.

**Ours**: the whole of this directory as deposited (NOTES.md, BRIEF.md, the nine modules, `tools/`, `tests-independent.l4`, DECIDED-ANSWERS.md, INDEPENDENT-FINDINGS.md).
**Source**: lines 120-123, 171-172, 204-212, 220-240, 448-449, 477, 492-497, 3598-3630, 3654-3655, 3677-3678 and 4709-4750 of the deposited consolidation (sha256 `78bf47ee…2a97`, re-verified).

**Enacted Laws**, fetched 2026-10-06 15:10 UTC through the Israeli-IP proxy; both hashes match the lead's:

| Law | URL | sha256 | where |
| --- | --- | --- | --- |
| National Insurance Law (Amendment No. 252 and Temporary Provision), 5785-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_5482787.pdf` | `d6c450ca0b869d1edb036b0f96bffbd79be6670336d9b5aa888da6cf2ecc8904` | Sefer HaChukim 3347 (14 January 2025), pp. 176-177 |
| Law for Achieving the Budget Targets and Implementing the Economic Policy for Budget Year 2025 (Legislative Amendments), 5785-2025 | `https://fs.knesset.gov.il/25/law/25_lsr_6133485.pdf` | `eba7e1fa570a3ece265d87f379543024da038ee51af3f959d4c74162f5edecfa` | Sefer HaChukim 3384 (27 March 2025), pp. 395-396 (Chapter E, National Insurance) |

The text was extracted with `pdftotext -raw` (visual order, read with word order reversed per line); the `-layout` pass is garbled on Amendment 252's pages 2-3 by a doubled text layer.
The PDFs were not kept.

### Licence

`NOTICE` says that encodings, companion test cases, parameter values and provenance metadata are CC BY 4.0 (`LICENSE`, the CC BY 4.0 legal code), and incidental tooling is Apache-2.0 (`LICENSE-CODE`); no licence is claimed over the law.
So the YAML read here is **CC BY 4.0**, as earlier comparison agents found.
Attribution for every quotation below: *Axiom Foundation RuleSpec corpus (CC BY 4.0), https://github.com/TheAxiomFoundation*.
Quotations are short; no Axiom file was copied into this row.

### The amending Laws: what was verified

Each of the four claims the lead relayed from our encoder was checked against the PDFs.

1. **Budget Law s 19(6) (Amendment No. 256)**, p. 396: "בלוח י׳, בכל מקום, במקום "60% מהשכר הממוצע" יבוא "מדרגת הגבייה המופחתת כהגדרתה בסעיף 334(א)"" (in Schedule J, everywhere, for "60% of the average wage" substitute "the reduced collection threshold as defined in s 334(a)"). **Verified.**
   The same section's paragraph (2) inserts the definition of "reduced collection threshold" into s 334(a), in the words the consolidation prints at lines 3605-3607; so the term did not exist in the Law before this chapter commenced.
2. **Amendment 252 s 7(a)(3)**, p. 177: during the temporary period the principal Law is read with, in column C, the sub-column headed "על החלק שאינו עולה על 60% מהשכר הממוצע" replaced by a new sub-column, and in column D the sub-column headed "על חלק השכר שאינו עולה על 60% מהשכר הממוצע" replaced likewise. **Verified: only the two lower sub-columns are replaced; the upper sub-columns of C and D are not touched.**
   The period is "לעניין דמי ביטוח לאומי שייגבו בעד השנים 2025 ו־2026", from commencement (1 January 2025, s 6) to 31 December 2026.
   The new sub-columns' figures equal the consolidation's temporary table (lines 4720-4730, columns C-lower and D-lower) in every cell but one: item 2, neither, not above the split, is **0.17** as enacted.
3. **Budget Law s 20(1)**, p. 396: in Amendment 252 s 7(a)(3)(a), "בטור ג׳ ללוח י׳, המובא בו, במקום "0.17" יבוא "0.16"". **Verified**: item 2's figure for those who are neither changes from 0.17 to 0.16 in the temporary lower sub-column. With 0.17 that sub-column's items summed to 6.93 against its printed total 6.92; with 0.16 they sum to 6.92.
   Section 20(2) also lowers the Treasury percentages in s 7(b)(1)-(2) to 44.26 and 45.39.
4. **Budget Law s 21**: "תחילתו של פרק זה ביום י״ב בטבת התשפ״ו (1 בינואר 2026)". **Verified**: ss 19-20 commence on 1 January 2026.
5. **Amendment 252 s 7(b)-(c)**: the Minister of Finance, after consulting the Minister of Labour and with the approval of the Knesset Labour and Welfare Committee, may by order extend the temporary period to contributions for 2027 and 2028, one year at a time; the order is to be brought for approval at least two months before the year. **Verified.**

Two consequences for this row that the encoder's NOTES do not yet record:

- **Assumption A1 is confirmed by the enacted Law**, not only by counting tags and a Wikisource page (NOTES section 3): the reduced collection threshold and the s 19(6) wording exist only from 1 January 2026, and in 2025 the temporary table's item 2 for those who are neither was 0.17.
  The tag identification also holds: the Budget Law's table of contents lists two National Insurance items, Amendment No. 256 (s 19, tag ־7, which is the only 5785 tag on s 334) and the amendment of Amendment 252 (s 20, tag ־8, on Schedule J with ־3 and ־7).
- NOTES section 7 still records the Amendment 252 fetch as failed.

### Divergence table

Lines are lines of the deposited source.
"SH" is Sefer HaChukim.

| id | provision | ours | theirs | source lines and Laws | classification | proposed repair if ours is wrong |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | s 334(a)(1)-(2): the index or the wage falls (our F6; independent T7) | the fall is applied: index 121 to 110 takes 9,101.62 to 8,274.2 | no update: each ratio is wrapped `max(1, …)`, "“rate of rise” is interpreted as excluding a decrease"; ENCODING-GAPS calls it "a disclosed reading, not a grounded figure" | 3606 "לפי שיעור עליית המדד", 3607 "לפי שיעור עליית השכר הממוצע"; nothing in the Laws read here speaks to a fall | **genuine ambiguity**: three readings are now on record (apply; floor at no change; the independent tester's REFUSE), and the text decides none of them | none on the text; Axiom's proposed evidence (how the Institute treated a year in which the index fell) is the right next step, and the choice is Meng's |
| D2 | s 334(a): the 2026 threshold | 7,703, the Institute's published figure (also the editors' note at 3605), on the year-only path; the unrounded formula is a separate rule the caller can use | `7522 × max(1, CPI ratio)`, computed from caller-supplied index readings, unrounded; no published figure | 3605-3606; the text states no rounding (our F7) | **representational**; with real readings the two differ by under a shekel of base (7,703 / 7,522 = 1.02406…) | — |
| D3 | s 334(a): 2027 on | the year-only path refuses; the caller supplies the threshold to the s 337 rules, or computes it with the s 334(a)(1)-(2) rules from the previous threshold and two readings | chained: from 2027-01-01 the formula multiplies the caller's `previous_year_reduced_collection_bracket`; 2026 always starts from 7,522 | 3605-3607 | **representational**: both need the caller's previous figure; neither supplies a default | — |
| D4 | s 334(b) | one input ("wage fixed in a Law or in or under a resolution of the Knesset"), ORed with the s 1 "employee"; the employer limb is a comment only (F14) | three inputs (by law, by Knesset decision, pursuant to a Knesset decision) and a separate rule deeming the payer the employer | 3608 "…ששכרו נקבע בחוק או בהחלטת הכנסת או על פיה, ואת החייב בתשלום השכר רואים כמעבידו" | **scope** (Axiom encodes the employer limb we leave to a comment) and representational for the employee limb | — (optional: encode the employer limb as a rule) |
| D5 | s 337(a)(1) with Schedule J: printed totals or the sum of the items (our F4) | the items, per branch, summed over the s 335 branches given; the totals are data, compared red | the printed totals only: s 337 reads `total_employee_contribution_within_reduced_band` and `…above_reduced_band`; ENCODING-GAPS: "Nothing computed here reads a branch row" | 3626 ("לפי סעיף 335"), 3611-3620 (s 335, branch by branch), 449 (s 28(a)); totals 4730, 4748; new evidence: Budget Law s 20(1) corrected a row so that it met its printed total | **genuine ambiguity**: the text supports the items; the Institute's 2026 composites (14.6, 7) and the one enacted correction (a row changed to meet its total) support the totals. Not settled by anything read. Effects: 2026 employee above the threshold 14.49 (ours) vs 14.60 (theirs); 2027 below 4.26 vs 3.95; 2028 on 4.16 / 14.39 vs 3.85 / 14.50 | add the s 20(1) precedent to F4's evidence; the choice stays open (open question 1) |
| D6 | s 337(a)(1): which branches the employee pays (s 335) | an input list; for a controlling shareholder the list without unemployment and insolvency | none: every employee is charged the all-branch total | 3615-3616 (s 335(e)-(f) exclude a controlling shareholder in a closely-held company from unemployment and insolvency), 3611 (s 335(a)) | **theirs wrong** for any employee who does not pay all nine branches. K16 (controlling shareholder, 10,000, 2026): ours 746.4608; Axiom 762.8785; the Institute's own controlling-shareholder composites (5.48 / 14.17) give 747.6093 | — |
| D7 | s 337: displacement by s 341 (reduced rates by order) and s 343 (approved large employers' work injury) | declined by name on an input flag | not modelled: the ordinary rates are charged | 3654-3656, 3677-3680 | **scope** (Axiom's figure is wrong for an income an order reaches, but it does not claim that case) | — |
| D8 | s 337(a)(1): negative income | input convention A7 (not negative), not checked | clamped, `max(0, …)` | — | **representational** | — |
| D9 | s 337(a)(2): another insured person | encoded for monthly advance periods (F8), other periods declined | deferred: "Applying a monthly bracket directly to annual income would not implement this subsection" | 3627 | **scope** | — |
| D10 | s 337(c): the deduction follows a change, proportionally | the ratio of new rate to old (F9); a change from 0 declined | deferred | 3629 | **scope** | — |
| D11 | Schedule J column D, upper part, contribution months in 2026 (our F3) | refused: the 2026 version's upper part begins "above 60% of the average wage" (line 4718), the lower part ends at the threshold, and **every** 2026 wage above 7,703 is declined (the rule refuses any wage that reaches the gap, not only wages inside it) | a parameter `temporary_employee_deduction_upper_band_average_wage_share` = 0.60, effective 2025-01-01 to 2026-12-31, which nothing reads; ENCODING-GAPS: the heading is "probably not the law in force", and whether s 19(6)'s "everywhere" reaches the temporary table is left "a question for the consolidation's maintainers" | 4718 against 4736; **SH 3347 p. 177, Amendment 252 s 7(a)(3)** (only the lower sub-columns replaced); **SH 3384 p. 396, Budget Law s 19(6) and s 21** (Schedule J "everywhere", from 1 January 2026) | **ours wrong** on the enacted Laws. The upper sub-column of column D was never part of the temporary provision; in 2026 it is the principal Schedule J's, which s 19(6) amended from 1 January 2026 to "above the reduced collection threshold". The heading at line 4718 is a stale copy of the pre-2026 text. Axiom's 0.60 parameter is also wrong for 2026 (inert); its "unsettled" point is real but concerns the lower sub-columns, not this one (N2 below) | R1 |
| D12 | Schedule J before 2026 | declined by name (A1) | parameters dated back: the current permanent table from 2011-04-01, the item-4 figures from 2024-01-01, the temporary lower sub-columns from 2025-01-01 (with item 2, neither, at 0.16); its s 334 and s 337 formulas start 2026-01-01 | 4711 (the heading dates the schedule "for April 2011 onward", not its figures), 4713 (nine amendment tags from 5772, 2011-12, on); SH 3347 s 7(a)(3) (0.17 in 2025); SH 3384 ss 19(2), 20(1), 21 (threshold and 0.16 from 2026) | **theirs wrong**, as data: the 2011-2023 figures are not in the source (Axiom's own coverage map marks the Law `temporal_coverage: current_expression_only`); for 2025 the item-2 figure was 0.17 and the split was 60% of the average wage, not a reduced collection threshold, which did not yet exist. Ours declines correctly | — |
| D13 | Schedule J: a dash (our F10) | `NOTHING`; a branch the person pays with a dash in their column is declined (s 340(a)(2) named for work injury of one who is neither) | an absent key in an item-indexed parameter; no rule in the row reads a per-branch value | 4720-4747 | **representational** (the question never arises in Axiom's computations) | — |
| D14 | Schedule J column E | stored with the other columns; the nouns module's comment calls all the figures percentages "as the column heading says" | `Decimal`, "no unit claimed", deferred: s 32(c1)(1) makes the column a split among branches, not a rate | 4717 (column E's heading says no "אחוזים"); 495 "יחולקו בין ענפי הביטוח השונים כאמור בלוח י׳" | **representational**; Axiom's description is the more exact, and our comment overstates for column E (no rule uses the column) | R4 |
| D15 | Schedule J, applied | column C for all three columns of insured person, column D (with F3), composites, the totals check | parameters only, except the employee's two totals that s 337 reads | 4716-4749 | **scope** | — |
| D16 | s 1 | nine terms: employee, employer, self-employed person, the average wage (with compensation, compensation rate, update day), the index, tax year, the Minister | one term: "the basic amount", paragraph (2), the child-allowance amounts | 120-229; the basic amount at 175-202 is out of scope for this row (row IL-06) | **scope**: the two s 1 modules share no term | — |

**Agreements worth recording.**
All 294 Schedule J cells and totals that either encoding uses for contribution months in 2026, 2027 and 2028 agree, dashes included: checked mechanically by `lad-il-04/tools/cellcheck.py` against lines 4720-4748 (and shown to fail on a planted copy with two altered values).
Both read column C as marginal, with income exactly at the threshold wholly "not above" (F17).
Both select 2026 = temporary lower sub-columns, 2027 = permanent with the 2024-2027 item-4 figures (2.06 above, 0.47 below), 2028 on = permanent as printed; both read the years as the years the contributions are for (F1), which Amendment 252 s 7(a)'s "בעד השנים 2025 ו־2026" supports.
Both apply the s 337(b) provisos only when the order changes that branch (7 of 7 Axiom cases match).
Both leave "the average wage" (F5) to the caller; Axiom's s 334 takes it as an input and its ENCODING-GAPS illustration uses the s 1 figure, 13,566.
Neither rounds a computed threshold (F7).

**Findings neither encoding records.**

- **N1. Extension orders for 2027-2028.** Amendment 252 s 7(b) (verified) lets the Minister of Finance extend the temporary lower rates to 2027 and then 2028, by order brought at least two months before the year. Both encodings answer 2027 from the permanent table without asking whether such an order was made; at retrieval (2026-10-06) that was not knowable from the sources. Classification: a shared silent assumption. Repair R2.
- **N2. The temporary lower sub-columns' own headings.** As enacted, Amendment 252 s 7(a)(3) heads the inserted sub-columns "not above 60% of the average wage", and Budget Law s 20 amended that section without changing those headings. s 19(6) amends "Schedule J, everywhere"; whether that reaches text that exists only as a "read the principal Law as follows" provision is the point Axiom's ENCODING-GAPS leaves open. Read literally for 2026, the upper sub-columns (above the threshold, 7,703) and the lower ones (not above 60% of the average wage, 8,139.6) would overlap rather than leave a gap. The consolidation prints the threshold in both lower headings (line 4718), and both encodings follow it. Classification: **genuine ambiguity** on the letter, with one workable reading. Repair R3 (record it).
- **N3.** The source of the item-4 note "(הוראת שעה בשנים 2024 עד 2027: …)" (lines 4723, 4741, 4730, 4748) is in neither PDF; neither encoding has verified it against an enacted Law.

**Count by class** (D1-D16): ours wrong 1 (D11); theirs wrong 2 (D6, D12); genuine ambiguity 2 (D1, D5); scope 6 (D4, D7, D9, D10, D15, D16); representational 5 (D2, D3, D8, D13, D14). Shared: N1 (silent assumption), N2 (genuine ambiguity), N3 (unverified).

### Axiom's test cases through our encoding

Run in a scratch copy of the modules (`lad-il-04/enc-copy/axiom-cases.l4`), `l4 run`, `JL4_LIBRARY_PATH` unset: 2 Error diagnostics, both the expected failed assertions below; every other assertion satisfied.
Each case's expected value is Axiom's (CC BY 4.0).

| case | inputs | Axiom expects | ours | result |
| --- | --- | --- | --- | --- |
| 334-1 `first_update_uses_statutory_base_and_price_index` | 2026; index 100 to 110; previous bracket 9,000 (Axiom ignores it in 2026); salary fixed by law | bracket 8,274.2; employee deeming holds | `s 334(a)(1)` from 7,522: 8,274.2; `s 334(b)`: TRUE | **match** (our year-only path would instead give 7,703, the published figure: D2) |
| 334-2 `subsequent_update_uses_previous_bracket_and_knesset_salary_qualifies` | 2027; from 8,274.2; index 110 to 121; Knesset decision | 9,101.62; holds | 9,101.62; TRUE | **match** |
| 334-3 `final_price_index_year_preserves_bracket_when_index_falls` | 2028; from 9,101.62; index 121 to 110; pursuant to a Knesset decision | 9,101.62; holds | **8,274.2**; TRUE | **diverge** (D1) on the bracket; match on deeming |
| 334-4 `wage_update_replaces_price_index_and_ordinary_salary_does_not_qualify` | 2029; from 9,101.62; average wage 18,000 to 19,800; ordinary salary | 10,011.782; not holds | `s 334(a)(2)`: 10,011.782; FALSE | **match** |
| 334-5 `liable_statutory_salary_obligor_is_deemed_employer` | payer liable, salary fixed by law | employer deeming holds | no rule (F14) | **could not be run** (D4) |
| 334-6 `employer_deeming_requires_liability_for_same_salary` | not liable | not holds | no rule | **could not be run** |
| 334-7 `ordinary_salary_liability_does_not_trigger_special_employer_deeming` | liable, salary not fixed | not holds | no rule | **could not be run** |
| 337-1 `employee_income_spans_both_contribution_bands` | 2026; income 15,000; bracket 7,522 (index flat) | 1,509.259 (5.55% / 14.60%) | all nine branches, threshold 7,522: **1,501.0332** (5.55% / 14.49%); with the published 7,703: 1,484.8518 | **diverge** (D5) |
| 337-2 `employee_income_entirely_within_reduced_band` | 2026; income 5,000; bracket 7,522 | 277.5 | 277.5 | **match** |
| 337-3 `order_satisfies_all_special_procedural_requirements` | every condition met, both provisos engaged | holds | TRUE | **match** |
| 337-4 `order_requires_ministerial_action` | not made by the Minister | not holds | FALSE | **match** |
| 337-5 `order_requires_finance_committee_approval` | no approval | not holds | FALSE | **match** |
| 337-6 `insolvency_rate_change_requires_prior_consultation` | insolvency changed, no consultation | not holds | FALSE | **match** |
| 337-7 `long_term_care_rate_change_requires_consent` | long-term care changed, no consent | not holds | FALSE | **match** |
| 337-8 `consultation_not_required_for_other_rate_changes` | insolvency unchanged, no consultation | holds | TRUE | **match** |
| 337-9 `consent_not_required_for_other_rate_changes` | long-term care unchanged, no consent | holds | TRUE | **match** |

**16 cases: 11 match, 2 diverge (334-3 on D1, 337-1 on D5), 3 could not be run (334-5 to 334-7, no employer-deeming rule).**
The s 1 and Schedule J test files are empty.

The same scratch module put ENCODING-GAPS' worked example through our column D rule: a 2026 wage of 15,000 is refused (D11), where Axiom's note gives 560.34 on the literal heading and 590.90 as the Institute applies it.
After repair R1 our figure would be 420.8811 on the items (4.67%), or 590.9012 if the printed total (7%) were used: the two divergences D5 and D11 compound here.

### Our independent-test findings, and how Axiom treats each

| finding (INDEPENDENT-FINDINGS.md) | ours | Axiom |
| --- | --- | --- |
| T7, falling index (the one failing assertion) | applies the fall | a third answer: no change (D1) |
| K15, mapping a person to a Schedule J column | not encoded | not encoded either: no s 1 "employee" or "self-employed person", and only the employee's computation exists |
| K17, employee and self-employed in one month | no entry point | none either |
| V1, March 2011 | year-only, refused | no version before 2011-04-01; from April 2011 the parameters assert today's figures (D12) |
| E13, N6, items 1 and 2 | one maternity branch, column decides (F15) | item-indexed, item 2 only in the neither columns: the same in effect |
| T8, missing readings | refusal, or the threshold supplied | the inputs are required; no default |
| "passing, but" 1, totals | items | totals (D5): the opposite of both our encoder and the independent tester |
| "passing, but" 2, F5 | argument | input; illustrated with the s 1 figure |
| "passing, but" 3, 2025 | refused | answered as data, wrongly for item 2 and for the split point (D12); the PDFs show the refusal is required, not merely the brief's scope, which settles the tester's "arguably answers 2025" against the aside |
| "passing, but" 4, K16 | 746.4608 | 762.8785, no s 335 (D6) |
| "passing, but" 5, F3 (and the tester's D3 REFUSE at 7,703.01, 8,000 and 10,000) | refused | parameter kept, unread, called "probably not the law" (D11); on the PDFs both our refusal and the tester's D3 expectation are wrong for 2026, and the tester's "purposive alternative" is the law |

### What Axiom covers that we do not, and the reverse

**Axiom only**: s 334(b)'s employer limb as a rule (D4); a negative-income clamp (D8); a precise account of column E under s 32(c1) (D14); parameters for years before 2026 (D12, which this comparison finds unsupported or wrong); an ENCODING-GAPS register that had already found, with the gazette, what our F3 records as an open question.

**Ours only**: s 337(a)(2) (D9) and s 337(c) (D10); the s 335 branch list as an input (D6); the s 341, s 343 and s 340(a)(2) refusals (D7, D13); column D computed (D11), and columns C for the self-employed and those who are neither (D15); nine s 1 terms with their tests (D16); the 2026 threshold and average wages as published figures with provenance (D2); the named refusal of 2025 (D12); the printed-totals check as an expected-red module.

### Proposed repairs to our encoding (not made)

- **R1 (D11, F3).** For contribution months in 2026, make column D's upper part begin at the reduced collection threshold: the 2026 version's flag `column D upper part begins above 60% of the average wage` becomes FALSE, cited to Budget Law s 19(6) and s 21 (SH 3384 p. 396) and Amendment 252 s 7(a)(3) (SH 3347 p. 177), with line 4718's heading kept in its `src:` comment and marked stale. Then: in `nii-il04-tests.l4` the refusals at 7,704 and 20,000 become values (80.1579 and 654.3811 on the items); in `tests-independent.l4` D3's three refusals would fail, a finding for the tester to reclassify (expected on the items: 80.111667, 93.9811, 187.3811). Update F3 and open question 3 in NOTES; F5 then no longer bears on Schedule J (only on "self-employed person" (2) and s 334(a)(2)).
- **R2 (N1).** For 2027 and 2028, take as an input whether an order under Amendment 252 s 7(b) extended the temporary provision to that year, and decline when it is not given; if extended, the temporary lower sub-columns (with 0.16) apply.
- **R3 (N2).** Add a fork recording that the enacted temporary lower-sub-column headings still say "60% of the average wage", and that the encoding follows the consolidation's threshold reading.
- **R4 (D14).** Correct the nouns comment: column E's heading does not say percentages; s 32(c1)(1) (line 495) makes the column a split of the Treasury's allocation among the branches.
- **R5 (D5, A1, NOTES section 7).** Add the s 20(1) correction to F4's evidence without changing the choice; record that A1 is now verified against SH 3384 ss 19(2), 20(1) and 21; replace section 7's "attempted and failed" for Amendment 252 with the two PDFs' URLs and sha256.

### Bottom line

On the numbers both encodings hold for 2026-2028, every cell agrees.
The two disagree on two genuinely open questions: whether a falling index lowers the threshold (D1), and whether the printed totals or the items govern (D5).
D5 is the one with money in it: 0.11 percentage points on income above the threshold for every employee (and, from 2027, 0.31 points the other way below it), and 2.33 points on the deduction's upper part.
On D5 Axiom matches the Institute's published 2026 composite for an ordinary employee, while ours matches the text's branch-by-branch structure; the one enacted correction found (s 20(1)) leans towards the totals, but proves nothing about the other cells.
Axiom is wrong where it ignores s 335 (D6) and where it dates today's figures into the past (D12).
We are wrong on F3 (D11): the enacted Laws answer the 2026 column D question that our encoding refuses, and Axiom's gap register had already found the gazette text that shows it.
Neither encoding asks whether the temporary rates were extended to 2027 (N1).
Axiom's test suite is thin (16 cases, none on Schedule J or s 1), and on it ours diverges only where the two encodings already disagree on an open question.
