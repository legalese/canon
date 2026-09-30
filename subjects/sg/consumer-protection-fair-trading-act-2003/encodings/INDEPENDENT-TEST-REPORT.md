# Independent test pass: tests-independent.l4

Written from `source/CPFTA2003.txt` (expected values decided from the statute), then run against the encoding.

Result of `l4 run tests-independent.l4`: 651 assertions, 650 satisfied, 1 failed, 0 other errors.

`check.sh` globs `*.l4`, so it now picks this file up automatically: the existing modules' rows are unchanged, but the TOTAL row gains 1 failed and check.sh exits non-zero until the finding below is resolved.

## Failing assertion (left failing)

- Line 832, s 22(1) and (6): a warrant that does not name an investigation officer and authorised assistant. The test expects `the warrant is valid in form and in force when exercised` to be FALSE. The encoding answers TRUE, because it checks naming only in `the court may issue a warrant` (s 22(1)) and takes "valid in form" from the s 22(6) list alone (subject matter and purpose, copy of the offences, one month). Section 22(6) does not list naming, so this is probably test-author over-reading, but s 22(1) does say the warrant authorises "by name", so an unnamed warrant is arguably not a warrant at all.

## Not tested, or tested only partly

- The DEONTIC rules (s 9(4)(d) to (f), s 10(6)(c): the 14-day duties to notify or inform the Commission).
- s 6(4)(c) when only some of annual value, annual rent and monthly rent can be ascertained (the encoding's reading is fork F1).
- Exact edge days that are ambiguous in the text: s 14(3) (six months "starting after" delivery, tested only well inside and outside), s 22(6) one month (10 June for a warrant issued 10 May not tested).
- Leap-day anniversaries in s 12.
- The Fourth Schedule "before the expiry of one year" edge (tested only well inside and outside).
- s 8(10) and (11): a Minister's appointment not yet published in the Gazette.
- s 12(2) as a bar inside `the consumer may recover the compensation as a civil debt`.
- Inert or descriptive provisions: ss 1, 5(1) and (2), 7(3), 7(6), 9(5), 20(3) to (5), 21(5), 22(3), (5) and (11), 26(3) against 26(1), and the content of any s 42 or s 43 instrument.
- Third Schedule (repealed).
