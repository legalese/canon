# IL-01 independent test pass: findings

Independent test author, 2026-10-06, one session, no sub-agents.
Expected values are in `DECIDED-ANSWERS.md` (pre-encoding part finished 2026-10-06T14:02:44Z, sha256 of that part `684306d6…f75446`); the assertions are in `tests-independent.l4`.

## Order of work, as it actually happened

1. Read `l4-ide/skills/encoding-a-subject/references/second-pass.md` and `writing-l4-rules/SKILL.md`.
2. Read the source bundle (sha256 verified `b87f2cf4…b81b6`): ss 33A, 34, 35 (by position), 36, 36A, 37, the s 1 definitions, and, to settle cross-references, ss 3A, 7, 14, 41, 48, 48A, 57, 66, 120A, 120B, 134A. Read `BRIEF.md`.
   Before step 3 I ran one `ls` of the encoding directory, so I saw its filenames; I opened none of them.
3. Wrote and timestamped `DECIDED-ANSWERS.md` (45 scenario rows).
4. Copied the encoding directory to scratch; read the four rule/figure modules and the encoder's own tests module (not `NOTES.md`).
5. Wrote `tests-independent.l4` and ran it in the scratch copy with the copy's `check.sh`.
   Ran a separate negative-control probe (not delivered) to confirm the harness can fail.
6. Only then read `NOTES.md`.

Nothing from the Axiom Foundation, any `rulespec-*` path, or any other forbidden path was read, searched or fetched. No web access was used at all.

## What `check.sh` printed

`L4=/Users/mengwong/.local/bin/l4 ./check.sh .` in the scratch copy (encoding modules unmodified, plus `tests-independent.l4`):

```
module                                    errors satisfied  failed  refused  expected
ito-credit-points-nouns.l4                     0         0       0        0         0
ito-credit-points-published-figures.l4         0         0       0        0         0
ito-credit-points-tests.l4                     0        58       0        0         0
ito-s33a-credit-point.l4                       0         0       0        0         0
ito-s34-s36-s36a-credits.l4                    0         0       0        0         0
tests-independent.l4                           0        78       0        0         0
TOTAL (6 modules)                              0       136       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`tests-independent.l4`: **0 errors, 78 satisfied, 0 failed, 0 refused.**
78 `#ASSERT` directives, 19 of them `#ASSERT REFUSED`, 10 of those pinning the reason with `BECAUSE`.
The only other diagnostic is the environment warning about a second copy of `prelude` in `~/.local/share/jl4/libraries/`.

**The harness can fail.** The negative-control probe used the same imports and four wrong assertions: a wrong number, a wrong refusal reason, a refusal expected where a value comes back, and a wrong allowance point.
`check.sh` reported `4 errors, 0 satisfied, 4 failed` for it, with messages `assertion failed`, `expected the refusal "a wrong reason", got "section 48 and the order made under it are not encoded in this model"`, and `expected a refusal, but the expression produced a value`.
The probe is not delivered.

## Failing assertions

**None.**
Every expectation I could express through the encoding's interface agreed with it, including the cells I had marked most likely to diverge:

- S04, the non-resident woman gets s 36A's half point (no residence limb in "בחישוב המס של אשה");
- S14/S15, a non-resident foreign worker gets 0 under ss 34/36 rather than a refusal (s 48A can only take away), while a foreign-worker woman's s 36A half point refuses;
- S10/S11, an Area resident who is not an Israeli citizen refuses ss 34/36 for the s 48 reason and still gets s 36A's half point if a woman;
- S24, 2.25 × 2,903 = 6,531.75 with no invented rounding; S35, 2,905 / 12 kept exact;
- S31, the set-off "המקוזז כנגד המס" floors the tax at 0, never negative;
- S37, the s 134A(2) aggregate excludes s 36A (9/4 for a woman, not 11/4).

Agreement here is two readers making the same choice, not proof that the choice is right: F1 (s 36A residence) and F2 (s 36 travel) are forks on which I independently took the encoder's reading.

## Expectations the interface cannot express

15 scenario rows cannot be expressed at all and 2 only in part.
They are sorted by what the encoding would do if a caller tried: the first group gets a confident wrong answer with no diagnostic; the second cannot refuse where I expect a refusal; the third is harmless or was my error.

### Silent: the encoding would answer, and the answer would be wrong

**S09a / S09b — an Israeli citizen who lives in the Area (Judea and Samaria) and is not an Israeli resident under s 1.**

- Provision: s 3A(f), line 471: "בכפוף להוראות סעיף זה, יחולו על אזרח ישראלי שהוא תושב אזור או פועל באזור, הוראות פקודה זו כאילו היה תושב ישראל". s 48 (line 1807) imports s 3A's definitions: "'אזור', 'תושב אזור' ו'אזרח ישראלי' – כהגדרתם בסעיף 3א".
- Expected: s 34 = 2, s 36 = 1/4, so 9/4 for a man and 11/4 for a woman.
- The encoding: no input distinguishes this person.
  The residence field's comment says it "carries the status as determined under s 1 for the tax year", so a caller following it enters `an Israeli resident in the tax year` = FALSE and `a resident of the Area who is not an Israeli citizen` = FALSE.
  The encoding then answers **0 for s 34 and 0 for s 36, with no refusal and no diagnostic.**
- Classification: **encoding gap, not recorded.** s 3A(f) appears nowhere in `NOTES.md`: not in the coverage table, the fork register, the answer table or the open questions.
  The s 48 row of the coverage table handles exactly the complementary case (non-citizens), which is the case s 48 exists for *because* s 3A(f) already covers citizens.
- Cheapest repair: say in the field's comment and in the `@export`'s `@desc` that an Israeli citizen in the s 3A(a) sense who is an Area resident is entered as resident by force of s 3A(f), and add a test; or add a field and route it.
  Note that s 3A(a)'s "אזרח ישראלי" is wider than citizenship: it includes (2) every Israeli resident and (3) a person entitled to immigrate under the Law of Return who is an Area resident.

A related small point on the same definitions: because s 48 takes "אזרח ישראלי" from s 3A(a), and s 3A(a)(2) makes every Israeli resident an "אזרח ישראלי", the encoder's fixture `a man resident in Israel who is also recorded as an Area resident and not a citizen` describes a combination that the statute's own definition rules out.
Its answer (2 points) is harmless; the nouns comment on `a resident of the Area who is not an Israeli citizen` should say that "Israeli citizen" carries the s 3A(a) meaning.

### Cannot refuse: the encoding has no input on which to refuse

**S40, S41, S42 — tax years whose text the bundle does not carry.**

- Provision: the section headers' amendment lists, s 34 "תשל״ה־2", s 36 "תשל״ז־4", s 36A "תשנ״ו", s 33A "תשס״ד־2"; the bundle is a single as-amended consolidation (BRIEF: "not a historical vintage").
- Expected: tax year 1970, s 34 and s 36 REFUSE; tax year 1990, s 36A REFUSE (s 34 = 2 and s 36 = 1/4); tax year 1960, everything REFUSE.
- The encoding: no rule takes a tax year, so it gives today's answer for any year a caller supplies a credit-point value for.
- Classification: **genuine scope issue, partly recorded.** `NOTES.md` §1 states, as "an assumption, not ruled", that the text "has stood since 5764" and that "the encoding answers any tax year since then for which the caller supplies the point value"; F10 notes that the s 48A refusal is undated.
  The note understates what the code does: the encoding answers *every* year, before 5764 as well, because it never asks the year.
  The sentence should say so, or the rules should take the year and refuse before the text's last amendment.
  My S41 split (s 34 answerable for 1990, s 36A not) rests on the same unverified amendment lists the encoder relied on; I marked it M.

**S16 — an individual resident for only part of the tax year.**

- Provision: s 34 "שהיה תושב ישראל בשנת המס"; s 36 "יחיד תושב ישראל"; no proration in either; contrast s 41 (line 1691), which prorates by months.
- Expected: REFUSE (M). The words do not say whether such a person "was a resident in the tax year" for the whole two points, was not, or takes a share.
- The encoding: residence is a BOOLEAN for the year, so a caller must choose TRUE (2 points) or FALSE (0), and either way receives a confident number.
- Classification: **genuine ambiguity, recorded** as fork F4 and open question Q3. The encoder chose to push the question to the caller; I would have refused. Both readings are visible in `NOTES.md`; this is a disagreement about where the refusal lives, not about the law.

### Harmless, by design, or my own error

| scenario | expected | why not expressible | classification |
| --- | --- | --- | --- |
| S17 non-registered spouse married part of the year (s 41) | REFUSE | no marital input | **my error on reflection.** s 41 consumes "נקודות הזיכוי לפי סעיפים 34, 36" as a quantity; the encoding's rules are that quantity, named as such and stated not to be a total (NOTES §1, coverage row s 41). |
| S18 woman inside her registered spouse's joint computation (ss 65, 66, 38) | REFUSE (L) | no input | **my error on reflection**, same reason; coverage rows s 38 and s 66 record it. |
| S44 kibbutz (s 57) | REFUSE | only one kind of body of persons | **my error on reflection.** s 57 applies ss 34–46A to the members in a hypothetical computation; the kibbutz itself gets 0, which is what the encoding answers for any body of persons. Coverage row s 57 records it. |
| S19 sex not stated | s 36A REFUSE | `a woman` is a required BOOLEAN | by design; a required input is a legitimate way to decline to guess. |
| S20 residence not stated | ss 34/36 REFUSE | required BOOLEAN | by design, as S19. |
| S27 credit-point value not supplied | REFUSE | required `GIVEN`, no default | by design, and what the brief requires. |
| S36 allowance-point base not supplied | REFUSE | required `GIVEN` | by design. |
| S38, S39 tax years 2026, 2024 | 9/4 | no year input | harmless: the encoding answers 9/4 for any year. |
| S31, second half: refund of the unused 2,986 | not answered | not exposed | harmless; F5 records the reading that the excess lapses. |
| S43, annual half: published annual figures for 2024, 2026, 2027 equal 2024's | equal (s 120B(e)(1)) | the annual figure refuses for every year but 2025 | harmless; the monthly half is asserted and passes (2024 = 2025 = 2026 = 242). |

## Minor, not tied to a scenario

- The `@export` says "the credit points an Israeli taxpayer **gets** under … ss 34, 36 and 36A alone".
  For a s 41 spouse or a joint-computation spouse the taxpayer does not "get" these points as such; the rule returns the per-section quantity that ss 41 and 66 then rework.
  An LLM caller reads the `@export` line and nothing else, so "the credit points under ss 34, 36 and 36A, before ss 41 and 66 apply" would be safer. Cosmetic.

## Summary

- Scenarios decided before opening the encoding: 45 rows.
- Assertions: 78, all satisfied; 0 failed; 0 refused; 0 errors.
- Not expressible: 15 rows wholly, 2 in part.
  One of them, **S09 (s 3A(f))**, is a silent wrong answer that `NOTES.md` does not record; it is the one finding I would act on first.
  The tax-year rows (S40–S42) are a scope issue the notes record as an assumption but state more narrowly than the code behaves.
  Part-year residence (S16) is a recorded fork.
- My own errors on reflection: S17, S18, S44, all three expectations of REFUSE that aimed at a person's final entitlement rather than at the per-section quantity this row claims to compute.
