# LQA report: Cat Act 2011 (WA), Parts 1 and 2, with the Cat Regulations 2012 they depend on

**Instrument and print.** Cat Act 2011 (WA), No. 55 of 2011, compilation **00-l0-01, currency start
25 Sep 2025**; with the Cat Regulations 2012, compilation 02-b0-00 (currency start 24 Jul 2025).
Both confirmed current on the WA legislation website on 2 October 2026 (step 10A), as was the
Veterinary Practice Act 2021 (00-f0-01), on whose definitions two findings turn.

**Scope.** Part 1 (ss. 2-4) and Part 2 (ss. 5-25), and the provisions of the Cat Regulations 2012
that Part 2 depends on (rr. 4-19, Sch. 1 Forms 1-2, Sch. 3). Parts 3-7 and the Cat (Uniform Local
Provisions) Regulations 2013 are outside this run.

**Status.** Steps 0H-11A complete. **Not released**: release (12H) needs a named person's signature
for one recipient, and none has been given. Run by Claude (agent) for Legalese, 1-2 October 2026.

**Result.** 54 findings: **32 OPEN** (1 high, 2 medium-high, 5 medium, 9 low-medium, 12 low, and 3
Form findings at low) and **22 verified sound**. Every finding is evidenced: 104 `#ASSERT`s in
`lqa-evidence.l4` (all satisfied), 39 console scenarios, one generated year (seed 1, 365 days), and
quotations checked against the pinned texts. None is opinion.

---

## How "found by" is counted

Each finding records one discovery method, the first of these that fits: **RD** a *casual* reader of
the provision would have caught it; **CMP** found by setting documents side by side (the
explanatory memorandum, another Act, a regulation read as text), not through the L4; **ENC** writing
the L4 or the console scheme forced the question; **CHK** a tool reported it; **TST** a written case
surfaced it; **SIM** a generated run surfaced it; **EXT** someone else found it first. The test is a
casual reader on purpose: it credits the encoding with what a careful reader might have caught but a
casual one would not, and CMP keeps deliberate cross-reading from being credited to the L4.

| Method | All | OPEN | Verified sound |
|---|---|---|---|
| ENC | 37 | 21 | 16 |
| CMP | 8 | 4 | 4 |
| RD | 7 | 6 | 1 |
| TST | 2 | 1 | 1 |
| CHK, SIM, EXT | 0 | 0 | 0 |

No finding is CHK: `l4 verify` does not exist in the installed `l4` (its commands are run, check,
format, ast, batch, trace, state-graph), `l4 check` is clean, and the console checker reported
nothing. Simulation did not *find* anything, but a generated year records seven OPEN findings (D-01,
L-33, T-46, W-21, U-34, T-39, R-36), which is stronger evidence than a scenario.

---

## Open findings, by severity

| ID | Finding | Provision | Severity | Found by |
|---|---|---|---|---|
| D-01 | After a transfer the registered owner remains "the owner"; the new keeper cannot register the cat | s. 4(1)(a); ss. 5, 6, 8(1), 24, 25 | high | ENC |
| D-05 | A cat chipped by a vet registered only in another State, or overseas, is not "microchipped" | s. 3(1); rr. 7, 8; VPA s. 22(1)(c) | medium-high | ENC |
| D-22 | A cat desexed by a vet registered only in another State, or overseas, is never "sterilised by a veterinarian" | s. 18(1); s. 3(1); VPA ss. 3, 22 | medium-high | ENC |
| L-09 | An owner who moves district is in breach of s. 5(1) at once, and r. 13's notice has no stated effect | s. 5(1); r. 13 | medium | ENC |
| D-10 | An owned cat at the vet, or boarding at an approved facility, must be refused registration | s. 9(2)(b); r. 9(2)(d), (e) | medium | CMP |
| P-15 | A refusal to consider an application carries no notice, reasons or review, and leaves the owner in breach | s. 9(6); ss. 13(2), 68 | medium | ENC |
| E-18 | If no s. 13 notice is given, the owner loses the objection and review rights | s. 13; ss. 69(1), 71(1) | medium | ENC |
| R-20 | Section 15 has no addressee until a database company has agreed to keep the cat's records | s. 15; s. 3(1) | medium | ENC |
| U-06 | "The person" in s. 5(2)(a): has a parent, or a business owner, kept the cat? (FORK-03) | s. 5(2)(a) | low-medium | ENC |
| U-27 | On a reclaim from a pound, who is the "seller"? (FORK-14) | s. 3(1) "transfer" (b); ss. 22-24 | low-medium | ENC |
| R-24 | Section 19 does not reach a false certificate of sterilisation | s. 19; r. 18(1) | low-medium | ENC |
| R-29 | Regulation 19's reference to r. 9 now exempts transfers to vet clinics and approved facilities from s. 23 | r. 19; r. 9 | low-medium | RD |
| D-31 | An offer for sale is a "transfer", so s. 24 requires notice of a purchaser who does not exist | s. 3(1); s. 24 | low-medium | TST |
| U-34 | Is a cat growing older a "change" the owner must notify? (FORK-15) | s. 25(b); r. 17(m) | low-medium | ENC |
| T-35 | Section 25's 7 days run from a change the owner may never learn of | s. 25; r. 17(c)-(e) | low-medium | ENC |
| U-38 | A "3-year" registration can last two years and a day (FORK-06) | r. 12(2)(a)(ii) | low-medium | ENC |
| W-21 | Section 16 requires the database company to keep information it was never given | s. 16 | low-medium | ENC |
| U-13 | "Within the previous 3 years": of the application or the decision? (FORK-11) | s. 9(2)(e) | low | ENC |
| R-17 | Section 13 notice goes to "the owner", and "the person's rights" has no antecedent | s. 13(1) | low | RD |
| U-19 | Does a certificate given before 6 months start to apply at 6 months? (FORK-13) | ss. 14(3), 18(3) | low | ENC |
| U-30 | Are the SAFE groups "set out in regulation 9" for r. 19? (FORK-08) | r. 19 | low | ENC |
| L-33 | Sections 24 and 25 both require the seller to report the same change | ss. 24, 25 | low | ENC |
| T-39 | Renewal outside the 21 days before 1 November, and an application after expiry, are not provided for | r. 12(2)(b) | low | ENC |
| T-46 | A one-year registration granted in late October lasts days | r. 12(2)(a)(i); Sch. 3 | low | CMP |
| R-36 | "Has effect from the period specified in the registration certificate", which specifies no period or start | r. 12(2)(a); Form 2 | low | RD |
| D-41 | The pensioner rate turns on "the owner", who may be several people | Sch. 3 cl. 1(3) | low | ENC |
| U-44 | Does IA s. 71(2) make a continuing failure to "ensure" a daily offence? (FORK-12) | ss. 5(1), 14(1), 18(1); IA s. 71(2) | low | ENC |
| X-47 | The explanatory memorandum presents s. 7 as dealing with forged tags; its words do not reach them | s. 7 | low | CMP |
| X-51 | Form 1 says the council "may refuse an application"; the Act's power is to refuse to consider it | Form 1 Part G; s. 9(6) | low | CMP |
| F-52 | Regulation 12(1) repeats "for" | r. 12(1) | low | RD |
| F-53 | Regulation 4: "each of the following bodies are prescribed" | r. 4 | low | RD |
| F-54 | Form 1 labels dates of birth "Age (dd/mm/yy)" | Form 1 Parts A, B | low | RD |

`INCIDENTS.md` gives each finding in full: provision, what, why it matters, evidence, the challenge,
status and a suggested repair. The most consequential, in brief:

**D-01 (high).** For a registered cat "owner" means only the registered owner (s. 4(1)(a)), and no
provision moves a registration to a purchaser: s. 24 requires notice of the purchaser's name, but
nothing then registers the cat in it. Until the registration ends -- never, under a lifetime
registration -- the seller keeps the owner's duties (tags, changes of details, registration in the
right district) for a cat it no longer has, and the person who keeps the cat may not apply to
register it (s. 8(1)). A generated year produces this in the ordinary course. *Repair:* make the
s. 24 notice transfer the registration, or end it, and let the keeper apply.

**D-05 and D-22 (medium-high).** Since the Veterinary Practice Act 2021 replaced the definition of
"veterinarian" (2022), an interstate vet is a "veterinarian" only if registered under that Act's
s. 22, which requires that the person practise in WA. A cat chipped in another State or overseas is
"not microchipped" (r. 8: only a microchip implanter's implant counts), so its owner is in breach of
s. 14(1) from arrival and registration must be refused; a cat desexed there can never be "sterilised
by a veterinarian" (s. 18(1)), though s. 9(2)(d) lets it be registered. *Repair:* make both turn on
the state of the cat (a compliant, recorded chip; sterilised), or recognise practitioners elsewhere.

**L-09, D-10 (medium).** An owner who moves within WA is in breach of s. 5(1) on the day of the move,
and r. 13's notice "to continue that period of registration with the new local government" has no
stated effect. And because r. 9(2) exempts from registration any cat in the custody of veterinary
premises or a cat management facility (which includes any facility a local government has approved),
s. 9(2)(b) obliges a local government to refuse a renewal decided while the cat is at the vet or
boarding.

**P-15, E-18 (medium).** A refusal to consider (s. 9(6)) is neither a grant nor a refusal: no notice,
reasons or review, and the owner stays in breach of s. 5(1). And because objection and review
(ss. 69, 71) are open only to "a person who has been given notice under section 13", a local
government that gives no notice removes the review.

**R-20 (medium).** The implanter must notify "the microchip database company for that cat", which
exists only once a company has agreed to keep the records (s. 3(1)). An implanter who arranges
nothing commits no offence, and the chip identifies nobody.

**Three repairs already enacted and not commenced.** The Dog Amendment (Stop Puppy Farming) Act 2021
(assented 22 December 2021) amends Part 2, and its ss. 50-61 are still "to be proclaimed" at this
print. Three would repair findings here: s. 50(4) deletes "offer for sale" from "transfer" (D-31,
though that also takes offers out of s. 23); s. 53 limits s. 16 to information "that has been given
to it" (W-21); and s. 55 runs the s. 25 clock from when the owner "becomes aware of the change"
(T-35). Commencing them would close or narrow three OPEN findings. None of them touches D-01, D-05,
D-22 or R-20.

---

## Findings verified sound, and what answered them

| ID | Candidate | Answered by |
|---|---|---|
| D-02 | The s. 4(2) presumption gives no day on which keeping began | Cat Act s. 4(2) ("in the absence of evidence to the contrary") |
| U-03 | The day a cat reaches 6 months (FORK-01) | Interpretation Act s. 62 |
| U-04 | A child keeper and the parent both owners (FORK-02) | Cat Act s. 4(1) ("any of these persons") |
| U-07 | Counting "less than 14 days" (FORK-04) | Interpretation Act s. 61(1)(b), (g) |
| U-08 | Does s. 5(2)(b) exempt a person never resident? (FORK-09) | Interpretation Act s. 18 |
| L-11 | An unsterilised kitten must be refused registration | Cat Act s. 5(1) (no duty before 6 months) |
| U-12 | "2 or more offences against any of" three Acts (FORK-10) | LC Supplementary Notice Paper 197-2, amendment 13/9 |
| P-14 | A s. 9(5) requirement allowing more than 21 days | Cat Act s. 9(5), (6) |
| L-16 | "If, and only if" and an application without the fee | Cat Act s. 9(1) with s. 8(2) |
| T-23 | Section 21 fixes no time | Interpretation Act s. 63 |
| D-25 | Section 18(2)(b) with several owners | Cat Act s. 18(2) ("A cat is exempt") |
| L-26 | No class prescribed as exempt from sterilisation (lead from 2A) | Cat Act s. 76(1) (permitted, not required) |
| L-28 | An unchipped kitten cannot lawfully be transferred | Cat Bill 2011 EM, overview and cl. 23 |
| R-32 | Section 24 for a cat neither registered nor recorded | Cat Act s. 24(a), (b) |
| U-37 | "The next 31 October" on 31 October (FORK-05) | Cat Regulations r. 12(1)(a) ("one year") |
| U-40 | The $10 fee "after 31 May" (FORK-07) | Cat Regulations Sch. 3 item 1(a) |
| T-42 | Foster care for "a total of 12 weeks" | Cat Regulations r. 9(3)(b) |
| P-43 | Regulation 10 exempts an owner, not a class | Cat Regulations r. 10(1)-(2), under ss. 6(2), 76(1) |
| T-45 | Exemptions commenced a year before the duties | Cat Act s. 2(b), (c), with s. 9(3)-(4) |
| X-48 | EM describes refusal for one conviction | LC Supplementary Notice Paper 197-2, amendment 13/9 |
| X-49 | EM limits the voucher to young cats | Interpretation Act s. 19(1) |
| X-50 | EM says s. 8 requires an application | Cat Act s. 5(1) |

---

## Forks and the readings taken

Fifteen forks, all recorded at 5A and each reviewed and confirmed (reading A) by Michael Andrew
Fairweather at 6H. Both readings are asserted for every fork except FORK-01's reading C. Eight left a
consequential choice open and are OPEN Uncertainty findings; seven were closed at 9A.

| Fork | Question | Reading taken | Finding |
|---|---|---|---|
| FORK-01 | When a cat "reaches 6 months" | numerically corresponding day (IA s. 62) | U-03, sound |
| FORK-02 | Child keeper and parent | both owners | U-04, sound |
| FORK-03 | "The person" in s. 5(2)(a) for an owner through another's keeping | keeping attributed | U-06, OPEN |
| FORK-04 | Counting 14 days | first day excluded | U-07, sound |
| FORK-05 | "The next 31 October" on 31 October | a year later | U-37, sound |
| FORK-06 | "31 October in the final year" of 3 years | 31 October in the last 12 months | U-38, OPEN |
| FORK-07 | $10 fee "after 31 May" | June-October | U-40, sound |
| FORK-08 | SAFE entities "set out in regulation 9" | yes | U-30, OPEN |
| FORK-09 | s. 5(2)(b) and non-residents | does not reach them | U-08, sound |
| FORK-10 | "2 or more offences against any of" | counted together | U-12, sound |
| FORK-11 | "Within the previous 3 years" | before the decision | U-13, OPEN |
| FORK-12 | IA s. 71(2) and duties to "ensure" | reaches them | U-44, OPEN |
| FORK-13 | Certificate given before 6 months | applies from 6 months | U-19, OPEN |
| FORK-14 | Who transfers on a reclaim | the facility's operator | U-27, OPEN |
| FORK-15 | A cat's age as a "change" | no | U-34, OPEN |

---

## Probe record

Every one of the thirteen categories was run over each of the seven Parts in `coverage.json`: 91 runs,
recorded in `registers/probe-record.json` with what each found, including the runs that found nothing.

- **Style (S) did not run.** Each S run is recorded "not run: no 0H manual (0H confirmation)": the
  WA Parliamentary Counsel's Office publishes no drafting manual, and the 0H confirmation decided
  that S does not run for WA and that no stand-in manual is adopted.
- **Logic (L).** The procedure's first step, `l4 verify`, could not run: the command does not exist
  in the installed `l4`. `l4 check` is clean over all eleven modules, and the console checker's
  conferred-fact and observation checks returned nothing. Decisions were enumerated by hand.
- **Amendment (M).** The print is a compilation, not an amending Bill. Every uncommenced instruction
  touching Parts 1-2 (Stop Puppy Farming Act ss. 50-55; Animal Welfare Amendment (Chief Animal
  Protection Officer) Bill 2025 (No. 40-1) cl. 20) was applied to the print and applies exactly once.
- **Runs that found nothing** are recorded as such: among them E over Parts 1, 2 Div. 3-5 and the
  regulations; W everywhere but Division 2; F everywhere but the regulations; I over Divisions 1, 2,
  4 and 5; M everywhere but Division 3 and the regulations.
- ENCODING-NOTES entries that are encoding choices rather than questions about the law (N-12, N-19,
  N-26, N-34), about the Interpretation Act rather than this instrument (N-53), or about the tools
  (N-01 to N-07, N-56) were not made candidates; the probe record says which run considered each.
  N-51 (the r. 15(3) tag-colour Gazette notice) is a 3H gap, not a demonstrated impossibility.

**A lead outside scope.** The Animal Welfare Amendment (Chief Animal Protection Officer) Bill 2025
cl. 21 inserts a s. 86A ("Report for Chief Animal Protection Officer") after s. 86, and the
uncommenced Stop Puppy Farming Act s. 61 inserts a different s. 86A ("Delegation by Department CEO")
at the end of Part 6. Whichever commences second produces two sections numbered 86A. It is not
recorded as a finding because it is in Part 6, outside this run's scope (Parts 1-2), and because the
defect is in another instrument (Bill No. 40-1, a Bill before the Legislative Council), not in the
pinned print. It belongs to an LQA run of that Bill. (Editorial renumbering under the Legislation Act
2021 Part 3 may be available to the Parliamentary Counsel; that was not checked.)

---

## Coverage

Encoded (`coverage.json`): s. 2; s. 3(1) definitions of cat, cat management facility, microchip,
microchip database company, microchip implanter, microchipped, owner, registered, registered owner,
sterilised, transfer; s. 4; ss. 5-11, 12(3), 13; ss. 14-17; ss. 18-21; ss. 22-24; s. 25; Cat
Regulations rr. 4, 5(1), 6-10, 11(1), 12-14 (Form 2's fields), 15-19, and Sch. 3 cl. 1(1)-(4) and
items 1-3; Interpretation Act 1984 ss. 5, 61, 62, 71, 72.

Not encoded, with reasons recorded in `coverage.json`: s. 1; the s. 3(1) terms Part 2 uses only as
facts (approved cat breeder, public place, veterinarian) or not at all; s. 3(2); s. 11 as duties and
s. 12(1), (2), (4); s. 88; Parts 3-7; the uncommenced amendments; rr. 1-3, 5(2)-(3), 11(2)-(3),
15(3), Forms 1 (content) and 3-8, Sch. 2, rr. 20-30; the Uniform Local Provisions Regulations; IA
s. 63; Criminal Code Chapter V, Criminal Procedure Act, Sentencing Act. Several findings were
challenged against provisions outside the encoding (IA ss. 10, 16, 18, 19, 32, 43, 63; Criminal Code
ss. 23A, 24, 29, 36; Cat Act ss. 29, 40, 68-71, 76, 85), read as text from the 0H and 3H sets.

---

## Known limitations of this encoding

Released with these stated, by decision at release (12H). They are limits of our encoding, not
defects in the Act, and no finding below depends on them.

- **Section 18(2)(b), a cat with several owners** (ENCODING-NOTES N-33). The encoding tests the
  approved-breeder exemption against the owner whose duty is in question, not against every owner.
  Where one co-owner is an approved breeder and another is not, the encoding treats the non-breeder
  as liable. D-25 states the law correctly (the exemption attaches to the cat: "A cat is exempt"),
  and is verified sound on that basis; the console and the L4 diverge from it in this one case.
- **The pensioner rate, Sch. 3 cl. 1(3)** (ENCODING-NOTES N-49). The encoding applies the pensioner
  test to the applicant. D-41 records that the clause turns on "the owner", who may be several
  people; the encoding takes one reading of an open question.
- **Gaps in the reference sets, found at Challenge (9A).** The State Administrative Tribunal Act 2004
  is not in the WA reference set, though E-18 turns on review in the Tribunal; Interpretation Act
  s. 63 is not in the reference register; and the 2011 explanatory memorandum is held as a PDF only,
  so quotations from it are cited by clause rather than machine-checked.

## Gates

| Step | Decision | By | Date |
|---|---|---|---|
| 0H Jurisdiction | confirmed: WA reference set; Style does not run; no stand-in manual | Michael Andrew Fairweather | 2026-10-01 |
| 3H Confirm | confirmed: print 00-l0-01 and the gathered set; parliamentary documents internal only | Michael Andrew Fairweather | 2026-10-01 |
| 6H Fidelity | certified: Parts 1-2 and the regulations; all 15 forks, reading A | Michael Andrew Fairweather | 2026-10-01 (recorded twice, the second under the corrected fingerprint) |
| 12H Release | not started | -- | -- |

No gate was waived. The same person signed 0H, 3H and 6H; the encoding was written by the agent.

---

## What the reference set knowingly lacks

From the 0H confirmation: a WA drafting manual (none exists; Style does not run); the Joint Standing
Committee on Delegated Legislation's terms of reference and practice; WALGA model local laws; the
Commonwealth Constitution and Australia Act 1986; copies of "How to read legislation" and the
local-laws operational guideline (held by link); regulations under the Interpretation, Criminal
Procedure and Fines Enforcement Acts.

From the 3H confirmation: the second-reading speeches for the Cat Bill 2011 and Bills 53 and 40
(Hansard refuses automated access); Delegated Legislation Committee reports from the 41st Parliament
and earlier; the amending regulations as made, 2013-2022 (unavailable; their effect is in the
compilation -- R-29 and U-30 turn on what the 2018 and 2022 amendments were meant to do); the 2022
Stop Puppy Farming commencement proclamation; the Minister's Gazette notice of tag colours (r. 15(3));
the Cat Bill 2011 as introduced and the second EM of each amending Bill; a copy of the 2019 statutory
review; Australian Standards AS 5018 and 5019.

Found at 9A, for repair at 0H or 3H:

- **State Administrative Tribunal Act 2004.** E-18 turns on whether a person never given s. 13 notice
  has any route to review; the SAT Act is in neither set.
- **The Cat Bill 2011 explanatory memorandum** is pinned as a PDF whose source-bundle note says it
  has no usable text layer. It has one (`pdftotext` extracts it), and the clause notes were read for
  X-47 to X-50 and cited by clause. Because the pinned copy is the PDF, quotations from it cannot be
  checked by `tools/lqa/check.js`, so none is used as quote evidence; a pinned text conversion would
  allow it.
- **Interpretation Act s. 63** answers T-23 but is not named in the reference register (as
  ENCODING-NOTES N-07 and N-31 noted at 4A); it is in the 0H set.

---

## Files

`incidents.json` (the register), `INCIDENTS.md` (each finding in full), `lqa-evidence.l4` (the 104
assertions, not part of the certified encoding), `scheme.js` (console scheme `cat-act-lqa`: one
observation per finding, with `ref` and `foundBy`; 39 scenarios; simulation parameters with
defaults), `registers/probe-record.json`. Run `node tools/lqa/check.js
subjects/western-australia/cat-act-2011-lqa --l4` to re-check every step.
