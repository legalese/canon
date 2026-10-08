# INDEPENDENT-FINDINGS: the il-36 encoding of the Encouragement of Aliyah and Return (Temporary Provision) Law, 5786-2026

Tester: fid-il-36, run id IL-56-36-20261008 (BACKLOG row IL-56, part for IL-36).
Date: 2026-10-09.

## 1. Order of work (for the lead to verify from the transcript)

1. The PDF pages 4-6 were rendered and read as images (150 dpi, and crops at 260 dpi for s 1); the deposited ITO was read for ss 1, 14, 62A(d), 88.
2. DECIDED-ANSWERS.md was written in the scratch directory and then copied into the encoding directory, then made read-only; it has 130 cases (ids A01-I04).
3. sha256 of DECIDED-ANSWERS.md: `b057647897854ef1a86cb4ef54c7be531d8f9209a7e66853bf1bd37c2d520298` (recomputed after all work, unchanged).
4. The only look at the encoding directory before that was the `ls` that listed file names in the same command as the copy; no file content was opened.
5. Only after the freeze were BRIEF.md, NOTES.md, check.sh and the il36-*.l4 modules read.
6. No Axiom material, RuleSpec, tests, ENCODING-GAPS, manifest or "Comparison with Axiom" section was read.

## 2. Result

`tests-independent.l4` holds 151 assertions citing 124 of the 130 decided cases by id (some cases take more than one assertion, for example a named reading and the default's refusal; a few ids share one assertion where the rows differ only in an input flag).
All 151 are satisfied; none failed; none was refused.
Of the 151, 12 are `#ASSERT REFUSED` (the default refuses and I had flagged the same ambiguity); they are satisfied.
check.sh, run after adding the file and a comment (the module list is the `*.l4` glob, so no list edit was needed; no failures or refusals are declared because none are expected):

```
module                                    errors satisfied  failed  refused  expected
il36-answers.l4                                0         0       0        0         0
il36-builders.l4                               0         0       0        0         0
il36-nouns.l4                                  0         0       0        0         0
il36-s1-definitions.l4                         0         0       0        0         0
il36-s2-exemption.l4                           0         0       0        0         0
il36-s3-entity.l4                              0         0       0        0         0
il36-s4-departure.l4                           0         0       0        0         0
il36-s5-s6-commencement.l4                     0         0       0        0         0
il36-tests.l4                                  0       262       0        0         0
tests-independent.l4                           0       151       0        0         0
TOTAL (10 modules)                             0       413       0        0
```

Exit code 0.
`l4` sha256 before and after: `f0759b2ef2f1d1b2a577c68f059c54f487de9d913553fc9f0d9bf0f7f5dab0d8` (the same).
Control for vacuity: on a scratch copy I changed one expected value (D09 940,000 to 941,000) and turned one `#ASSERT REFUSED` into a value assertion; check-style counting then showed one `assertion failed` and one `assertion refused`, so the assertions do discriminate.

## 3. Disagreements, classified

There is no case in which the encoding's value differs from a value I decided.
Every difference is a refusal where I decided a reading, or a gap in my own list.

| id | what | class | detail |
| --- | --- | --- | --- |
| D07, D08 | relatives' income in 2030 at the default | AMBIGUITY | The default refuses by name (fork F3). I decided paragraph (4) stands (150,000): the text says `במקום פסקאות (1) עד (3)` and `2026 עד 2029`, so (4) is untouched; the encoding's first reading gives the same 150,000 (asserted with the reading named). The encoder keeps the 140,000 reading alive as a purposive alternative. Both readings are arguable; mine is the literal one, my confidence in the text was H. The lead's task note says 140,000 "in each year including 2030"; the text does not say that for 2030. |
| H15 | income attributed under ITO s 62A from a transparent corporation | AMBIGUITY | Default refuses (fork F2). I decided it is qualifying (the `למעט ... לפי סעיף 62א` exception to the second exclusion), the encoding's first reading agrees (asserted with the reading named, 300,000). I flagged only M; the other reading, that it is a further exclusion, is arguable but makes the exception empty. |
| C01-C07, C10, C11, C13 | 2026 pro rata at the default | AMBIGUITY (agreed) | I flagged AMB-1 (days or months); the default refuses; my days values hold on the named reading (480,000; 120,000; 240,000; 360,000; 110,400,000/365; 600,000/365; 600,000 x 364/365; 112,000; 28,000; 212,000). The encoder's months reading is calendar months with at least one day, which is the larger of my two month conventions (500,000, 150,000, 250,000, 400,000, 300,000), so the encoder's alternative equals my "arrival month included" alternative. |
| A13 | adaptation-year election | AMBIGUITY (agreed) | I flagged AMB-6; the default refuses (fork F4); on the reading I took (the election changes nothing) the exempt amount is 100,000, which the encoding gives on its second F4 reading. |
| F13 | entity income dated before the 2026 arrival day | AMBIGUITY (agreed) | I flagged AMB-7 at L; the default refuses (fork F7); my reading (exempt only from arrival) gives 0 on the first F7 reading. |
| G12, G13 | s 4, which year's days count | AMBIGUITY (agreed) | I flagged AMB-4; the default refuses (fork F9); the literal reading disqualifies and the year-of-ceasing reading does not, as I worked it. |
| G14 | s 4 and the entity's s 3 exemption | AMBIGUITY (agreed) | I flagged AMB-5 at L; the default refuses (fork F8); on my reading (unaffected) the amount is 500,000. |
| F10 | transparent foreign entity, he holds 5%, 250,000 of 1,000,000 attributed to Israeli residents | TESTER-WRONG on my fact pattern, encoding right | The value 750,000 is asserted with the entity flagged as a "transparent corporation" and it passes. But the Law's own s 1 defines `תאגיד שקוף` as an ITO s 64(a) transparent corporation in which an oleh or veteran is a material shareholder (10% or more), other than one wholly owned by him; in my pattern nobody qualifying holds 10%, so on the Law's defined term the entity is not a "transparent corporation" and s 3(b)(2) would not bite (exempt 1,000,000, assuming he is not himself a material shareholder). If he were the material shareholder, s 3(b)(1) removes the whole exemption and (b)(2) adds nothing. So (b)(2) bites only where some other oleh or veteran is a material shareholder. The encoder took the flag as an input, which is correct; my pattern in DECIDED-ANSWERS.md F10 was wrongly built. Not edited (frozen). |
| A08, F03, H13, H16, I01, I02 (not asserted); A12, D16, D17, H03-H09, H18 (asserted only as the Law's consequence of an input flag) | Ordinance facts (the 10% test, the ten-year test, the relative test, the kind of income, the chargeable base, s 5 savings) | SCOPE | The encoding takes each as an input flag, as its BRIEF says; I asserted the Law's consequence of the flag, not the Ordinance test itself. A08 and F03 are therefore not tested as such. I01 and I02 (ITO ss 14 and 97 untouched by this Law) are inert in the encoding and I did not test them. |
| (F6) | whether the s 2(c) total cap is prorated in 2026 | gap in my list, AMBIGUITY | The encoding forks this (F6); I did not flag it. My cases C13 and C17 do not discriminate (212,000 and 156,000 are under both the prorated cap and 600,000), so they hold under either reading. The text (`תקרות ההכנסה המנויות בסעיף קטן (א)` in (c); `על אף האמור בסעיפים קטנים (א) ו־(ב)` in (d)) does not decide; the encoder's fork is right. |

## 4. The encoder's reading of the source

I compared `registers/source-bundle/encouragement-of-aliyah-and-return-law-5786-2026.he.txt` with the page images, line by line, for the figures and dates, and for the wording of ss 1-6.
Figures: 600,000; מיליון; 350,000; 150,000; 140,000; 75; 5 November 2025 (14 Cheshvan 5786); 31 December 2026 end of tax year 2026; 12 Tevet 5786 (1 January 2026); the years 2026-2030, 2026-2029 (s 2(b)), 2028 or 2029 (s 4): all match the images.
The statute references (ITO ss 2(1) and (2), 14, 62A(d), 64(a), 88, 97; Law of Return 5710-1950; Absorption Basket Law 5754-1994 s 2; Citizenship Law 5712-1952 s 11) match.
The definitions in s 1 match, including the two carve-outs for wholly owned (`קרוב` and `תאגיד שקוף`) and the Ministry's certificate.
The (b)(1) and (b)(2) wording of s 3 matches.
I found nothing the encoder read wrongly in the source.
Two small observations that are not errors: the English field name says "Ministry of Aliyah and Integration" for `משרד העלייה והקליטה` (the Ministry's current English name; the Hebrew in the Law says "absorption"); and the ITO s 14(b)(1) quotation in NOTES.md is consistent with the deposited ITO line 1141.

## 5. Cases decided but not asserted

Six of the 130 decided cases are not cited by any assertion: A08, F03, H13, H16, I01, I02.
A08 (nine years abroad is not a veteran) and F03 (9.9% is not a material shareholder) are Ordinance tests that the encoding takes as input flags; H13 (the taxable base), H16 (a wholly owned corporation is not a transparent corporation) likewise; I01 and I02 (s 5 savings) are inert in the encoding.
All six are classed SCOPE above.
