# NOTES — vn-msig-general-liability-2015, encoding row `legalese-2026-10-vn-09`

MSIG Insurance (Vietnam) Company Limited, **General Liability Insurance Policy** ("Revised General Liability Policy Form", the file dated 12 January 2015), the whole document, encoded in L4 by one agent in one session (run `VN-09-20261006`, agent `enc-vn-09`, 2026-10-06), from the brief in `BRIEF.md`.
Status: **draft**.
No domain expert has read it against the source; HG1 has not been sought.

`src:N` everywhere means line N of `../../source/raw/msig-cgl.txt`, the text rendering of `msig-cgl.pdf` (sha256 `cb17d805daa65afec62e78861fc2835a246d2d9fee306ea098b8d29c107d3814`, 14 pages, retrieved 2026-10-06 from msig.com.vn).
"Law" is the Law on Insurance Business 08/2022/QH15, read from the aid `../../../../../../.aids/law-08-2022-qh15.txt` and cited by article and aid line; that aid file stops at Article 130 (its last line says the gazette continues in the next issue), so the Law's transitional and final provisions were not available.

## 0. Build and run

Run on 2026-10-06 (23:32-23:51 SGT) with `/Users/mengwong/.local/bin/l4`, `JL4_LIBRARY_PATH` unset.
That path is a symlink to `~/.cabal/bin/l4`, a local cabal build in store entry `jl4-0.1-0ee0100b`, sha256 `64bbcb157dbef2ef1020a6a75589313bba0a2aeeb807c921c5e65e62e9eca118`.
The binary has no `--version`; no record beside it names the commit it was built from.

The command, from this directory:

```
L4=/Users/mengwong/.local/bin/l4 ./check.sh
```

Its totals: **0 errors, 285 assertions satisfied, 0 failed, 0 refused**, over 13 modules; exit 0 (the full output is §6).

Every module runs `IMPORT prelude` and `daydate`; each run also prints two Warnings that differing copies of those libraries exist under `~/.local/share/jl4/libraries/`. The binary uses its embedded copies, and the warnings are not errors.

**The harness can fail.** A scratch probe (in this session's scratch directory, not deposited) imported these modules and asserted three deliberately wrong values (the ultimate net loss off by one dong, a products claim "covered" under the CGL part, the Company's cancellation effective after nine days), one right value, and one `#ASSERT REFUSED` on a rule that answers. `l4 run` printed 3 `assertion failed`, 1 `assertion failed: expected a refusal, but the expression produced a value` and 1 `assertion satisfied`, with 4 `DiagnosticSeverity_Error`, and exited 0, which is why the exit code is not read.

**How the files were made.** The `.l4` modules were expanded from templates by a script in this session's scratch directory: every `-- src:N |` line is the output of `python3 -I tools/vnsrc.py quote ../../source/raw/msig-cgl.txt N M`, never typed; the 153 refusal arms and the fact list in `msig-cgl-record.l4` are generated from the enum `A fact` in `msig-cgl-nouns.l4`. The document prints no table, so there was no long test list to generate from the raw text; the figures it does print (US$250, US$25, S$250.00, S$25.00, ten days, three years, 120 months) are each tested on both sides of the edge (§5).

Wall time: one `check.sh` run takes about twenty minutes on this machine while the other encoders' runs share it, most of it in the three tests modules, each of which imports the whole stack.

## 1. What is encoded and what is not

**The source is English only.** It contains no Vietnamese, and no Vietnamese counterpart was found.
The `src:` comments therefore quote English; the bilingual deliverable is `GLOSSARY.md`, whose Vietnamese renderings are this encoder's and are marked `[translator]` on every line that carries one.

**Encoded: the whole document**, in the order printed:
the recital and agreement (as named text), COVERAGE, SUPPLEMENTARY PAYMENTS, APPLICABLE LAW (named text), JURISDICTION, all sixteen DEFINITIONS, CONDITIONS 1-10, the Comprehensive General Liability Insurance Coverage Part (I with exclusions (a)-(q), II, III, IV), the Products and Completed Operations Liability Insurance Coverage Part (I with exclusions (a)-(i), II, III, IV), every Special Condition, and the closing notice.

The three layers of the brief:

1. **Is the event covered?** `the answer under the CGL Coverage Part` and `the answer under the P&CO Coverage Part` (msig-cgl-answer.l4) return `covered`, or `not covered` with the clause that defeats the claim, asking the clauses in a stated order.
   The facts of a claim are FINDINGS on its record (msig-cgl-nouns.l4, `A fact`, 153 facts, each worded as the clause that reads it). A fact the record does not mention is never assumed: a rule that reaches it refuses, with the message "the record does not say whether …" (msig-cgl-record.l4). L4 is lazy, so a claim an earlier clause already decides needs no later fact.
2. **How much is payable?** `the most the Company pays for the occurrence under …` applies the limits to the ultimate net loss (damages plus the supplementary sums), under the Combined Single Limit Endorsement or under III as printed; `what the Company pays under …` puts layers 1 and 2 together.
3. **What must each party do, and by when?** The duties are regulative rules (Condition 1 records, 3(a), 3(b), 3(c), 6, 9, Sistership 1); the periods the document states are date functions (Condition 2's three years, Condition 9's ten days, the Claim Series Clause's 120 months). No duty of the insured has a period in days: "as soon as practicable", "immediately" and "promptly" are standards, carried as findings (fork F12).

**Not encoded**, each because the document leaves it outside itself:

- the declarations, the schedule and the Company's manual: the named insured, the policy period, the limits, the Retroactive Date, the classification codes and the description of the territory are **inputs** with no default;
- the Company's "rules, rates, rating plans, premiums and minimum premiums" (Condition 1) and "the customary short rate table and procedure" (Condition 9): not in the document, so the premium and the refund on the named insured's own cancellation are **declined by name** (`REFUSE`);
- the Law on Insurance Business: read only to record where it fills or overrides the policy (forks tagged `LAW:`), never encoded.

No provision is out of scope and none is deferred (§2).

**What the brief's money convention meets here.** Money is a bare `NUMBER` in dong (brief rule 8). But the document states no currency for its limits, and its only printed figures are **US$250 and US$25** (src:28, 34) and **S$250.00 and S$25.00** (src:942, 949). Those caps are converted at rates the caller supplies (`Rates of exchange into dong`), because the document names no rate, date or source (fork F5; finding X4). No figure is read in the Vietnamese number format, because the document prints none: the four figures are written with a currency prefix and, for the Singapore ones, a decimal point (".00"), and are read as 250 and 25.

## 2. Coverage table

The source writes its headings in English; "heading as written" quotes them; the gloss is mine.
Disposition: `encoded` (a rule answers it), `inert` (carried as named text or a comment: it decides nothing a rule computes), `reached-and-refused` (a rule reaches it and declines by name, because what it points to is not in the document).
Totals: **139 rows: 119 encoded, 18 inert, 2 reached-and-refused, 0 out-of-scope, 0 deferred**.

| src | heading as written (the source is English) | English gloss | disposition | where in the L4 |
| --- | --- | --- | --- | --- |
| 1 | GENERAL LIABILITY INSURANCE POLICY | title | inert | general, `§ GENERAL LIABILITY INSURANCE POLICY` |
| 2-4 | WHEREAS ... | recital: proposal and declaration are the basis of the policy | inert (named text; consequences of a misstatement are the Law's, fork F31) | general, `the recital` |
| 6-7 | In consideration of ... | the agreement clause | inert (named text) | general, `the agreement` |
| 10-13 | COVERAGE | cover is by the coverage parts the declarations identify | encoded | general, `the declarations identify … as part of …`; answer, first arm |
| 16-18 | SUPPLEMENTARY PAYMENTS | sums paid inside the limit | encoded | general; answer, `the most the Company pays …` |
| 20-23 | SUPPLEMENTARY PAYMENTS (a) | defence expenses, costs, post-judgement interest | encoded | general, `Supplementary Payments (a)` |
| 25-28 | SUPPLEMENTARY PAYMENTS (b) | bond premiums; bail bonds up to US$250 each | encoded | general, `Supplementary Payments (b)` |
| 30-31 | SUPPLEMENTARY PAYMENTS (c) | first aid | encoded | general, `Supplementary Payments (c)` |
| 33-34 | SUPPLEMENTARY PAYMENTS (d) | the insured's expenses; earnings up to US$25 a day | encoded | general, `Supplementary Payments (d)` |
| 37-41 | APPLICABLE LAW | Vietnamese law, Vietnamese courts | inert (named text: chooses the law, adds no condition) | general, `the applicable law` |
| 44-49 | JURISDICTION | no cover for a judgement first given outside Vietnam | encoded | general, `the Jurisdiction clause takes the judgement outside the indemnity` |
| 52-54 | DEFINITIONS | chapeau | inert | definitions, `§ DEFINITIONS` |
| 56-57 | "automobile" | road vehicle, not mobile equipment | encoded | definitions, `the vehicle is an automobile` |
| 59-60 | "bodily injury" | injury, sickness, disease in the period; death resulting | encoded | definitions, `the harm is bodily injury`, `it occurs during the policy period of … on …` |
| 62-73 | "collapse hazard", "Structural property damage" | collapse from earthworks or underpinning, less three exceptions | encoded | definitions, `the property damage is included within the collapse hazard` |
| 74-78 | "completed operations hazard", "Operations" | harm from finished work away from the premises | encoded | definitions, `the harm is included within the completed operations hazard` |
| 80-87 | (1)-(3) deemed completed | three completion events | encoded | definitions, `the operations are deemed completed or abandoned` |
| 89-90 | further service ... deemed completed | work needing only service is complete | encoded | same |
| 92-100 | does not include (a)-(c) | transport, tools, "including completed operations" classifications | encoded | definitions, `the completed operations hazard does not include it` |
| 102-107 | "elevator" | hoisting device, less five kinds | encoded | definitions, `the device is an elevator` |
| 109-113 | "explosion hazard" | blasting or explosion, less four exceptions | encoded | definitions, `the property damage is included within the explosion hazard` |
| 115-118 | "incidental contract" | five written contracts | encoded | definitions, `that contract or agreement is an incidental contract` |
| 120-122 | "insured" | per Persons Insured; each insured separately; one set of limits | encoded (by the shape: one claim, one insured; limits per occurrence) | definitions, comment; nouns, `A claim against an insured` |
| 124-131 | "mobile equipment" | four kinds of land vehicle | encoded | definitions, `the vehicle is mobile equipment` |
| 133 | "named insured" | the person in Item 1 of the declarations | encoded (as a role) | nouns, `the named insured` |
| 135-137 | "named insured products" | goods of the named insured, not rented machines | encoded | definitions, `the harm arises out of the named insured's products` |
| 139-140 | "occurrence" | accident, neither expected nor intended | encoded | definitions, `the harm was caused by an occurrence` |
| 142-157 | "policy territory" | described territory; international waters; worldwide for products; suit in Vietnam | encoded | definitions, `the harm occurs within the policy territory` |
| 159-162 | "products hazard" | harm from products away from premises after possession given up | encoded | definitions, `the harm is included within the products hazard` |
| 164-166 | "property damage" | physical injury in the period; loss of use from an occurrence in the period | encoded | definitions, `the harm is property damage`, `the date the harm is dated by` |
| 168-175 | "underground property damage hazard" | buried services damaged by earthworks, less three exceptions | encoded | definitions, `the property damage is included within the underground property damage hazard` |
| 178 | CONDITIONS | chapeau | inert | conditions, `§ CONDITIONS` |
| 180-183 | 1. Premium: computed by the Company's rules | the rules are not in the document | reached-and-refused | conditions, `Condition 1 — the premium computed under the Company's rules, which are not in the document` |
| 185-190 | 1. Premium: advance premium, earned premium, return | deposit adjusted to earned premium | encoded | conditions, `Condition 1 — the adjustment of an earned premium of …` |
| 192-194 | 1. Premium: records | named insured sends records | encoded (duty, no period) | conditions, `Condition 1 — the named insured sends its premium records` |
| 196-201 | 2. Inspection and Audit: inspection | permitted, not obligated; no warranty | inert (named text) | conditions, `Condition 2 — inspection` |
| 203-205 | 2. Inspection and Audit: audit | during the period and three years after | encoded | conditions, `Condition 2 — the last day …`, `Condition 2 — the Company may examine and audit on …` |
| 207-212 | 3. Insured's Duties (a) | written notice of an occurrence as soon as practicable | encoded (content; duty with no period) | conditions, `Condition 3(a) — the notice has the content and route required`, `Condition 3(a) — notice of an occurrence` |
| 214-215 | 3. (b) | forward claims and process immediately | encoded (duty, no period) | conditions, `Condition 3(b) — forwarding of claims and process` |
| 217-221 | 3. (c) cooperate | cooperate and assist on request | encoded (as the finding Condition 4 reads, "full compliance") | conditions, comment; `Condition 4 — an action lies against the Company` |
| 226-227 | 3. (c) no voluntary payment | at the insured's own cost, except first aid | encoded (SHANT; such sums left out of the ultimate net loss) | conditions, `Condition 3(c) — …`; answer, ultimate net loss |
| 229-234 | 4. Action Against Company | full compliance and a final determination | encoded | conditions, `Condition 4 — an action lies against the Company` |
| 236-237 | 4. claimant's right to recover | after judgement or agreement | encoded | conditions, `Condition 4 — the claimant is entitled to recover under the Policy` |
| 237-241 | 4. no joinder; no impleading; insolvency | procedure | inert (comment: no answer computed turns on them) | conditions, comment |
| 243-252 | 5. Other Insurance | primary; not reduced by excess insurance; contribution on the same basis | encoded | conditions, `Condition 5 — the most of the loss the Company is liable for, …` |
| 254-259 | 5. (a) Contribution by Equal Shares | equal shares up to each limit | encoded | conditions, `Condition 5(a) — …` |
| 261-264 | 5. (b) Contribution by Limits | in proportion to limits | encoded | conditions, `Condition 5(b) — …` |
| 266-270 | 6. Subrogation | the Company takes the insured's rights; the insured secures them | encoded (duties) | conditions, `Condition 6 — the insured secures the rights of recovery` |
| 272-277 | 7. Changes | only a signed endorsement changes the policy | encoded | conditions, `Condition 7 — a waiver or change takes effect` |
| 279-281 | 8. Assignment | binds only with consent endorsed | encoded | conditions, `Condition 8 — an assignment of interest binds the Company` |
| 281-285 | 8. on death of the named insured | legal representative; custodian | encoded | conditions, `Condition 8 — on the named insured's death, …` |
| 287-290 | 9. Cancellation by the named insured | surrender or mailed notice | encoded (the effective date is the input `the policy period ends`) | nouns, `the policy period ends`; conditions, comment |
| 290-296 | 9. Cancellation by the Company | mailed notice, not less than ten days | encoded | conditions, `Condition 9 — the earliest date …`, `Condition 9 — the Company's notice, mailed on …` |
| 297 | 9. short rate | refund when the named insured cancels | reached-and-refused | conditions, `Condition 9 — the customary short rate table is not in the document` |
| 298 | 9. pro rata | refund when the Company cancels | encoded | conditions, `Condition 9 — the earned premium when the Company cancels, …` |
| 298-305 | 9. premium adjustment timing | at cancellation or as soon as practicable | encoded (duty, no period) | conditions, `Condition 9 — the Company returns the unearned premium` |
| 307-311 | 10. Declaration | statements are representations; entire agreement | inert (named text; fork F31) | conditions, `Condition 10 — the declaration` |
| 319 | COMPREHENSIVE GENERAL LIABILITY INSURANCE COVERAGE PART | heading | inert | part-cgl, `§` heading |
| 321-336 | I. COVERAGE A – BODILY INJURY LIABILITY; COVERAGE B – PROPERTY DAMAGE LIABILITY | the insuring agreement; defence; end on exhaustion | encoded | part-cgl, `CGL I — the insuring agreement reaches the claim`; answer, arms I; `the applicable limit is exhausted under …` |
| 332-335 | I. "may make such investigation and settlement ... as it deems expedient" | the Company's discretion to settle | inert (a discretion with no criteria; finding X23) | part-cgl, comment |
| 338-340 | Exclusions | chapeau | inert | part-cgl |
| 342-344 | (a) | contractual liability, except incidental contracts and warranties | encoded | part-cgl, `CGL exclusion (a) applies` |
| 346-354 | (b) | automobiles and aircraft of an insured; parking exception | encoded | part-cgl, `CGL exclusion (b) applies` |
| 356-359 | (c) | mobile equipment in contests; snowmobiles | encoded | part-cgl, `CGL exclusion (c) applies` |
| 361-362 | (d) | mobile equipment carried by an insured's automobile | encoded | part-cgl, `CGL exclusion (d) applies` |
| 364-371 | (e) | watercraft of an insured, except ashore on the premises | encoded | part-cgl, `CGL exclusion (e) applies` |
| 373-376 | (f) | pollution, except sudden and accidental | encoded | part-cgl, `CGL exclusion (f) applies` |
| 378-383 | (g) | war, for incidental contracts and first aid | encoded | part-cgl, `CGL exclusion (g) applies`, `CGL exclusion (g)(2) takes out the first aid expenses` |
| 385-403 | (h) | alcoholic beverages | encoded | part-cgl, `CGL exclusion (h) applies` |
| 405-406 | (i) | workmen's compensation and similar laws | encoded | part-cgl, `CGL exclusion (i) applies` |
| 408-410 | (j) | injury to employees, except incidental contracts | encoded | part-cgl, `CGL exclusion (j) applies` |
| 412-423 | (k) | property owned, used or controlled; sidetrack and elevator exceptions | encoded | part-cgl, `CGL exclusion (k) applies` |
| 425 | (l) | premises alienated | encoded | part-cgl, `CGL exclusion (l) applies` |
| 427-436 | (m) | loss of use from delay or failure; exception | encoded | part-cgl, `CGL exclusion (m) applies` |
| 438 | (n) | damage to the named insured's products | encoded | part-cgl, `CGL exclusion (n) applies` |
| 440-441 | (o) | damage to the named insured's work | encoded | part-cgl, `CGL exclusion (o) applies` |
| 443-446 | (p) | withdrawal of products or work | encoded | part-cgl, `CGL exclusion (p) applies` |
| 448-457 | (q) | explosion, collapse, underground hazards with x, c, u | encoded | part-cgl, `CGL exclusion (q) applies` |
| 460-473 | II. PERSONS INSURED (a)-(c) | by designation of the named insured | encoded | part-cgl, `Persons Insured (a)-(c) — …` |
| 475-479 | II. (d) | real estate manager | encoded | part-cgl, `CGL II — the person claimed against is an insured` |
| 481-497 | II. (e) and proviso | operators of registered mobile equipment on a highway | encoded | part-cgl, `Persons Insured (e) — …` |
| 498-499 | II. closing sentence | undesignated partnership or joint venture | encoded (fork F7) | part-cgl, `CGL II — the undesignated partnership or joint venture exclusion applies` |
| 502-506 | III. LIMITS OF LIABILITY | chapeau: regardless of number of insureds, claimants, claims | encoded (limits per occurrence) | answer, `the most the Company pays …` |
| 508-514 | III. Coverage A | each occurrence; aggregate for completed operations and products | encoded | part-cgl, `CGL III Coverage A — …`, `the cap of …` |
| 516-540 | III. Coverage B | each occurrence; aggregates (1)-(3), separately and per project | encoded (per category and project as the input `under the property damage aggregate that applies`) | part-cgl, `CGL III Coverage B — …` |
| 542-544 | III. Coverage A and B | continuous exposure is one occurrence | encoded | definitions, `the harms of … and of … count as one occurrence for the limits` |
| 547-549 | IV. POLICY TERRITORY | harm in the policy territory | encoded | part-cgl, `CGL IV — …` |
| 557 | PRODUCTS AND COMPLETED OPERATIONS LIABILITY INSURANCE COVERAGE PART | heading | inert | part-pco, `§` heading |
| 559-575 | I. COVERAGE A; COVERAGE B | insuring agreement, completed operations or products hazard only | encoded | part-pco, `P&CO I — …`; answer |
| 577-579 | Exclusions | chapeau | inert | part-pco |
| 581-583 | (a) | all contractual liability, except warranties | encoded | part-pco, `P&CO exclusion (a) applies` |
| 585-601 | (b) | alcoholic beverages | encoded | part-pco, `P&CO exclusion (b) applies` |
| 603-604 | (c) | workmen's compensation | encoded | part-pco, `P&CO exclusion (c) applies` |
| 606-607 | (d) | injury to employees | encoded | part-pco, `P&CO exclusion (d) applies` |
| 609-618 | (e) | loss of use from delay or failure | encoded | part-pco, `P&CO exclusion (e) applies` |
| 620 | (f) | damage to the products | encoded | part-pco, `P&CO exclusion (f) applies` |
| 622-623 | (g) | damage to the work | encoded | part-pco, `P&CO exclusion (g) applies` |
| 625-628 | (h) | withdrawal | encoded | part-pco, `P&CO exclusion (h) applies` |
| 630-637 | (i) | pollution | encoded | part-pco, `P&CO exclusion (i) applies` |
| 641-657 | II. PERSONS INSURED (a)-(d) | as the CGL part, without (e) | encoded | part-pco, `P&CO II — the person claimed against is an insured` |
| 659-660 | II. closing sentence | undesignated partnership or joint venture | encoded | part-pco, `P&CO II — the undesignated partnership or joint venture exclusion applies` |
| 663-683 | III. LIMITS OF LIABILITY | each occurrence; aggregate for all | encoded | part-pco, `P&CO III …`; answer |
| 685-687 | III. Coverage A and B | one occurrence | encoded | definitions (as 542-544) |
| 690-692 | IV. POLICY TERRITORY | harm in the policy territory | encoded | part-pco, `P&CO IV — …` |
| 700-703 | SPECIAL CONDITIONS | part of the Policy; supersede similar clauses | encoded (as the readings in forks F4, F10, F18) | special, header comment |
| 706 | Applicable to Comprehensive General Liability Insurance Coverage Part Only | scope heading | encoded (fork F18) | special, `§§` heading |
| 708-713 | COMPLETED OPERATIONS HAZARD AND PRODUCTS HAZARD EXCLUSION CLAUSE | CGL part: no products or completed operations | encoded | special, `the Completed Operations Hazard and Products Hazard Exclusion Clause applies` |
| 716 | Applicable to Products and Completed Operations Liability Insurance Coverage Part Only | scope heading | encoded (fork F18) | special, `§§` heading |
| 718-724 | BUSINESS RISK EXCLUSION | design failures, except active malfunction | encoded | special, `the Business Risk Exclusion applies` |
| 727-736 | CLAIMS MADE BASIS ENDORSEMENT 1 | claim in the period; after the Retroactive Date; immediate notice; knowledge proviso | encoded | special, `Claims Made Basis 1 — …` (four rules) |
| 738-741 | 2 | each claimant's claim is its own | encoded (by the shape: one claim record per claimant) | special, comment |
| 743-744 | 3 | nothing caused before the Retroactive Date | encoded | special, `Claims Made Basis 3 — …` |
| 746-752 | 4 | notice of circumstances deems a later claim made in the period | encoded | special, `Claims Made Basis 4 — …` |
| 754 | Retroactive Date: As stated in the Policy Schedule | from the schedule | encoded (input; refused by name where absent) | special, `the Retroactive Date of` |
| 757-760 | CLAIM SERIES CLAUSE | chapeau | inert | special |
| 762-763 | 1 | a series is dated by the rules below | encoded | answer, `the date the harm is taken to occur under …`; special, `Claims Made Basis 1 — the claim is made, or deemed made, …` |
| 765-766 | 2 | definition of a Claim Series Event | encoded | special, `Claim Series — the claim belongs to a Claim Series Event` |
| 768-773 | 3 | date of occurrence; date of claims-made | encoded | special, `Claim Series 3 — …` (two rules) |
| 772-773 | 3, last sentence | "the Company shall include each and every claim ..." | inert (comment: a rule of aggregation with no figure) | special, comment |
| 775-776 | 4 | 120 months | encoded | special, `Claim Series 4 — …` |
| 781 | Applicable to All Coverage Parts | scope heading | encoded | special, `§§` heading |
| 783-791 | ASBESTOS EXCLUSION | asbestos | encoded | special, `the Asbestos Exclusion applies` |
| 794-814 | COMBINED SINGLE LIMIT ENDORSEMENT | one limit for A and B; aggregate for products and completed operations | encoded (fork F10) | special, `Combined Single Limit — …` |
| 817-821 | CYBER LIABILITY EXCLUSION | business done online | encoded | special, `the Cyber Liability Exclusion applies` |
| 824-843 | DATE RECOGNITION EXCEPTION | date failures of devices | encoded | special, `the Date Recognition Exception applies` |
| 846-849 | ELECTROMAGNETIC FIELDS EXCLUSION | electromagnetic exposure | encoded | special, `the Electromagnetic Fields Exclusion applies` |
| 852-877 | INSTITUTE RADIOACTIVE CONTAMINATION, CHEMICAL, BIOLOGICAL, BIOCHEMICAL AND ELECTROMAGNETIC WEAPONS EXCLUSION CLAUSE | nuclear and weapons; isotopes exception | encoded | special, `the Institute Radioactive Contamination Exclusion Clause applies` |
| 880-883 | PROFESSIONAL LIABILITY EXCLUSION | professional duty or paid advice | encoded | special, `the Professional Liability Exclusion applies` |
| 886-889 | PUNITIVE DAMAGES EXCLUSION | fines, penalties, multiplied damages | encoded (as an amount) | special, `the Punitive Damages Exclusion takes out` |
| 892-897 | SANCTION LIMITATION AND EXCLUSION CLAUSE | sanctions | encoded | special, `the Sanction Limitation and Exclusion Clause applies` |
| 900-908 | SISTERSHIP EXCLUSION CLAUSE 1 | duty to withdraw, repair or replace | encoded (duty, no period) | special, `Sistership 1 — …` |
| 910-912 | 2 | later harm from the same cause excluded | encoded | special, `Sistership 2 — the exclusion applies` |
| 914-916 | 3 | cost of the measures not indemnified | encoded | special, `Sistership 3 — the expenses not indemnified` |
| 919-924 | ULTIMATE NET LOSS CLAUSE 1 | limits apply to the ultimate net loss | encoded | answer, `the most the Company pays …` |
| 926-949 | 2 (a)-(e) | what the ultimate net loss is | encoded | special, `Ultimate Net Loss 2(a)`-`2(e)`, `the ultimate net loss of … at …` |
| 952-975 | WAR & TERRORISM EXCLUSION (a)-(c) | war, terrorism, action against them | encoded | special, `the War and Terrorism Exclusion applies` |
| 976-977 | burden of proof | on the insured once alleged | encoded | same |
| 982-983 | IMPORTANT | read the Policy; return it for correction | inert (named text) | special, `the closing notice` |
| 69, 71, 147, 149, ... 989 | "Page N of 14", "Revised General Liability Policy Form" | page furniture | inert (not quoted) | — |

## 3. Fork register

Every ambiguity met, the readings, the one taken, and the text for each.
`LAW:` marks a place where the Law on Insurance Business fills or may override the policy; those are recorded and **not** resolved in the L4 unless the row says so.
Statements about Vietnamese law that cite no line of a text given to this session are marked "outside knowledge, unverified".

| # | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | "occurs during the policy period", src:59, 164, 731-732 | are the first and last stated days inside the period? | (i) both inclusive; (ii) the policy states hours elsewhere (src:293 "date and hour"), so time of day matters | **(i)**: the declarations give dates; no hour is stated for the period itself. Tests sit on 1 January and 31 December. |
| F2 | "policy territory" proviso, src:156-157; JURISDICTION, src:46-49 | does "provided the original suit ... is brought subject to the provisions of the Jurisdiction clause" qualify all three limbs or only (3)? what if no suit is brought? | (i) all limbs, and it bites only where a suit has been brought, which must be in a Vietnamese court; (ii) limb (3) only; (iii) it requires a Vietnamese suit even for a settlement | **(i)**: the proviso stands at the margin after (3), outside its indentation; a settlement brings no suit, and the Jurisdiction clause itself speaks only of judgements. Reading (ii) would let a foreign suit for an injury in Vietnam through. |
| F3 | "named insured products", src:135-137 | the definition defines "named insured products" and then uses "named insured's products", as do the clauses | (i) one term; (ii) the possessive form undefined | **(i)**: the definition's own last limb uses the possessive form to restrict itself. |
| F4 | Supplementary Payments (b), (d), src:28, 34; Ultimate Net Loss Clause 2(c), (e), src:942, 949 | the caps are US$250 and US$25 in one clause and S$250.00 and S$25.00 in the other | (i) the Ultimate Net Loss Clause: a Special Condition, which "shall supersede any other similar ... Clauses" (src:702-703) and opens "Notwithstanding any provision ... contrary" (src:921); (ii) Supplementary Payments, the general clause; (iii) **LAW:** Law Art. 24 (aid lines 588-591) reads an unclear clause in favour of the policyholder, which would take whichever cap is larger at the rates on the day | **(i)**, encoded as operative; (ii) is also encoded (`the Supplementary Payments, as printed with US dollar caps`) so the difference can be computed (finding X4). (iii) is not encoded. |
| F5 | the same four figures | at what rate, on what date, from what source are they converted to dong, the currency of the limits? | the document is silent | **input**: the caller supplies `Rates of exchange into dong`. The currency of the limits is not stated either; this row takes dong, the brief's convention. |
| F6 | "named insured" vs "insured" throughout | which insured is "the insured" in an exclusion? | (i) the insured against whom the claim is made, by the separate-application sentence (src:121-122); (ii) any insured | **(i)**. |
| F7 | Persons Insured, CGL part, src:498-499 | the closing sentence on undesignated partnerships is indented under (e) in the CGL part, at the margin in the P&CO part (src:659-660) | (i) applies to the whole part; (ii) applies to paragraph (e) only | **(i)**: the sentence is about any insured's partnership, not about mobile equipment, and the P&CO part prints the same words at the margin. |
| F8 | Persons Insured (e)(ii), src:486-489 | does "any person or organization legally responsible for such operation" need the same registration and permission? | (i) yes, "such operation" is the permitted operation of equipment registered to the named insured; (ii) any responsible person | **(i)**. |
| F9 | Persons Insured (a), src:465-466 | is the spouse an insured where the named insured is not an individual? | (i) no, "such a business" is the individual's sole proprietorship; (ii) yes | **(i)**. |
| F10 | III Limits of Liability, src:502-544, 663-687; Combined Single Limit Endorsement, src:794-814 | every Special Condition "shall form part of the Policy" (src:702), so the endorsement always rewrites III; but it refers to one "each occurrence" sum and one "aggregate", and a schedule may state separate bodily injury and property damage limits | (i) the endorsement governs where the schedule states one combined sum; III as printed governs where it states separate sums; (ii) the endorsement always governs, and a schedule with separate sums leaves its reference unresolved (decline); (iii) the endorsement applies only if the declarations list it | **(i)**: the schedule's shape is a fact of the policy (`The limits stated in the schedule`), and each text then has the sums it refers to. Under (ii) every separate-limits policy would be declined. |
| F11 | Supplementary Payments, src:18; III as printed | under separate limits, which coverage's limit absorbs the supplementary sums? | (i) the coverage of the damages, where there is one kind; the kind alleged, where there are no damages; declined where an occurrence causes both; (ii) pro rata to the damages; (iii) bodily injury first | **(i)**: the policy says "the applicable limit" and nothing more; (ii) and (iii) would invent a rule. Finding X5. |
| F12 | Condition 3(a), (b), src:212, 214; Sistership 1, src:904; Condition 9, src:298-304 | "as soon as practicable", "immediately", "promptly", "as soon as practicable after" | (i) standards, judged on the facts; (ii) a number of days | **(i)**: no period is stated, so none is invented (writing-l4-rules phrasebook 5.9); compliance enters as findings (Condition 4's "full compliance"; Claims Made Basis 1's "immediate notice"). |
| F13 | Condition 2, src:204 | "within three (3) years after the final termination" | (i) up to and including the same calendar date three years on (29 February goes to 28 February); (ii) 3 × 365 days | **(i)**, calendar years. |
| F14 | Condition 4, src:231-234 | "full compliance with all of the terms": any breach, however small, or only a material one? **LAW:** Law Art. 46(1)-(2) (aid lines 917-932) lets the insurer reduce the indemnity for late notice only by the damage it suffered, and only where the contract states the insured's responsibility for late notice; Law Art. 19(3) (aid lines 441-444) bars a late-notice exclusion where force majeure caused the delay | (i) literal: any breach bars the action; (ii) material breach only; (iii) the Law's proportional reduction | **(i)** as the text reads, with the conflict left open (finding X8). Whether "full compliance" is the contractual statement Art. 46(2) requires is not decided here. |
| F15 | Condition 5, src:245-252 | (1) other insurance on mixed bases; (2) this Policy excess or contingent while the other is on another basis | (1)(i) contribute only with insurance on the same basis; (2)(i) the text does not say | **(1)(i)**: the text speaks of insurance "on the same basis"; **(2) declined by name**. |
| F16 | Condition 9, src:292 | "not less than ten (10) days thereafter": calendar or working days; from mailing or from receipt? | (i) calendar days from mailing, the tenth day allowed; (ii) working days; (iii) from receipt | **(i)**: "the mailing of notice ... shall be sufficient proof of notice" (src:292-293). Finding X13. |
| F17 | Condition 9, src:298 | how pro rata is counted | (i) days elapsed over days in the period, each the difference of two dates; (ii) months | **(i)**. |
| F18 | Special Conditions headings, src:706, 716, 781 | which parts each Special Condition reaches | (i) by the heading above it: the Claims Made Basis Endorsement and the Claim Series Clause stand under the P&CO heading and before "Applicable to All Coverage Parts"; (ii) the claims-made endorsement reaches both parts | **(i)**: the layout, and the endorsement's own words "included within the completed operations hazard or the products hazard" (src:732-733), which the CGL part excludes anyway. |
| F19 | Completed Operations Hazard and Products Hazard Exclusion Clause, src:710-713 | "directly or indirectly arising out of or relating to or resulting from" the hazards | (i) harm within either hazard as defined; (ii) any loss "relating to" a product or finished work, including on the premises | **(i)**: the hazards are defined terms with their own limits (away from premises, possession given up). (ii) would also exclude an injury from a product on the named insured's own premises, which the definition leaves out of the hazard. |
| F20 | Claims Made Basis Endorsement 1, src:731-736, with the definitions, src:59, 164 | does the claims-made trigger replace the requirement that the harm occur in the period? | (i) no: the endorsement says cover applies "only in respect of" claims made in the period, which adds a condition; the definitions are untouched; (ii) yes: a claims-made form, the Retroactive Date governing the harm's date; **LAW:** Law Art. 24 (aid lines 588-591) | **(i)**, literal. Finding X1. **LAW:** Law Art. 58(1) (aid lines 1083-1086) ties the insurer's liability to a claim for damage done "during the insurance period", which reading (i) also satisfies. |
| F21 | Claims Made Basis Endorsement 1, src:733 | "sustained after the Retroactive Date": on the date itself? | (i) strictly after; (ii) on or after | **(i)**, "after". Tested on the day. |
| F22 | Claims Made Basis Endorsement 1, src:734-736 | "provided always that at the effective date of this policy any Insured did not know or could not reasonably have foreseen" | (i) as written: holds if no insured knew, or if it could not have been foreseen; fails only if an insured knew AND could have foreseen; (ii) "neither knew nor could have foreseen" | **(i)**, the words. (ii) is encoded beside it for comparison. Finding X6. "any Insured" is read as "no insured" (any insured who knew defeats it). |
| F23 | Claim Series Clause 4, src:775-776 | "within 120 months of the first claim" | (i) calendar months, the same day 120 months on included (`add months` clamps the day); (ii) 3,650 days | **(i)**. Tested on the day and the day after. |
| F24 | Claim Series Clause 3, src:768 | is the series' deemed date of occurrence also the date for "occurs during the policy period"? | (i) yes: "the date of occurrence of such 'A Claim Series Event' shall be deemed to be the date that the first loss of the series occurred"; (ii) only for claims-made purposes | **(i)**, in the P&CO part. |
| F25 | Claims Made Basis Endorsement 4, src:746-750 | when does the deeming apply? | (i) first awareness and written notice both in the period, and the claim arises out of the products the circumstances concern; (ii) notice alone | **(i)**, every word of the clause. Products only (finding X7). |
| F26 | War & Terrorism Exclusion, src:976-977 | the burden of proof | (i) once the Company alleges the exclusion, the loss is excluded unless the insured has proved the contrary, whatever else is found; (ii) the burden shifts only within a dispute over facts already found | **(i)**, as written. Finding X10. |
| F27 | Sanction clause, src:894-897 | "to the extent that" | (i) the whole claim, where the finding is made for it; (ii) a part of a claim | **(i)**: the record holds one finding per claim; a partial answer would need the amount, which the caller can split. |
| F28 | CGL exclusion (k), src:421 | "liability under a written sidetrack agreement" | (i) liability assumed under a written sidetrack agreement; (ii) any liability connected with one | **(i)**. |
| F29 | CGL exclusion (h) and P&CO (b), src:402-403, 600-601 | "part (ii) ... does not apply ... as an owner or lessor described in (2)" | (i) (1) is excluded under (i) or (ii); (2) under (i) only | **(i)**. |
| F30 | Sistership 2, src:911-912 | "arising from the same cause where the initial bodily injury or property damage occurs" | (i) "from the same cause as the initial injury or damage": later harm only; (ii) at the same place | **(i)**: the clause's paragraph 1 speaks of "the same or similar conditions where the initial ... occurred". |
| F31 | recital, src:2-4; Condition 10, src:309-311 | what follows from an untrue statement? **LAW:** Law Art. 22(2) (aid lines 543-553) lets the insurer rescind for a deliberately incomplete or false statement made to obtain the contract | the policy is silent | **not encoded**; the Law answers, and the misstatement is a fact outside the claim record. |
| F32 | definitions "automobile" and "mobile equipment", src:56-57, 124-131 | a road vehicle that is also, say, unregistered | (i) mobile equipment ("does not include mobile equipment") | **(i)**, the definition's own words. |
| F33 | Punitive Damages Exclusion, src:888-889 | a ground of no cover, or an amount? | (i) an amount: the fines and multiplied part leave the ultimate net loss; (ii) the whole claim | **(i)**: "shall not apply to fines, penalties, punitive damages ..." names sums, not claims. |
| F34 | Supplementary Payments (c), src:30-31 | first aid "for bodily injury to which this Policy applies" | (i) counted only for a covered claim | **(i)**: the amount layer runs only on a covered claim (`what the Company pays under …`). |
| F35 | Condition 9, src:289-292 | **LAW:** Law Art. 26 (aid lines 623-635) lists the cases in which either party may terminate unilaterally; the policy lets the Company cancel for any reason on ten days' notice | (i) the contract's ground stands; (ii) the Law's list is exhaustive | **not resolved**; whether parties may agree further grounds is outside knowledge, unverified. Finding X13. |
| F36 | the policy's silence on claim documents, the insurer's payment deadline and a time-bar | **LAW:** Law Art. 30 (aid lines 706-717): a claim dossier within one year, for a third-party claim counted from the third party's demand; Law Art. 31 (aid lines 718-729): payment within the agreed time or, failing one, 15 days from a complete dossier, with interest for delay | the Law fills the silence | **recorded, not encoded** (COMPARABLES "not stated"). Finding X21. |
| F37 | Condition 6, src:268-270 | **LAW:** Law Art. 54(3) (aid lines 1043-1049) bars recovery from the insured's parents, spouse or children unless they caused the loss intentionally; Art. 54 stands in the part of the Law on property and damage insurance (its heading at aid lines 890-892), and liability insurance has its own part (from aid line 1072) | (i) Art. 54(3) reaches this liability policy; (ii) it does not | **not resolved**. |
| F38 | Condition 4, src:236-239 | **LAW:** Law Art. 58(2) (aid lines 1087-1089): a third party has no direct claim on the insurer unless the law provides | the policy gives a claimant holding a judgement or agreement a right to recover "under this Policy" | **not resolved**: a contract granting more than the Law's default is not obviously barred (outside knowledge, unverified). |
| F39 | every exclusion | **LAW:** Law Art. 19(2) (aid lines 435-440): the insurer must explain the exclusions clearly and keep evidence that the policyholder understood them | whether that was done is a fact outside the document | **not encoded**; the consequence of failing to explain is not stated in the lines read. |
| F40 | Coverage parts and Special Conditions, src:12-13, 702 | is a Special Condition part of a policy whose declarations do not list it? | (i) yes, "shall form part of the Policy" | **(i)**. |

Where else I looked for ambiguity and found none worth a row: the elevator definition (the five excepted devices are each a finding), the explosion and underground hazard exceptions (read as printed), the order of the exclusions (no exclusion depends on another), and the two caps' per-bond and per-day application (each is plainly per unit).

## 4. Findings

Defects in the instrument as written, from a hostile pass as the policyholder's lawyer and as the insurer's.
"Evidence" names the assertion in `msig-cgl-tests-findings.l4` (section X*n*) or another tests module; "reading only" means the encoding cannot demonstrate it.
Every assertion named here passes: it shows the policy answering as its text makes it answer.

**X1. The P&CO part is claims-made AND occurrence-dated, so the Retroactive Date buys nothing and a claim made after the period falls between two policies.**
src:59-60, 164-166, 731-736, 754.
The definitions still require the bodily injury or property damage to occur during the policy period; the Claims Made Basis Endorsement adds that the claim must be made in it (fork F20).
Scenario: a product injures someone on 31 December 2026; the claim arrives on 1 January 2027. This policy: not covered, claim not made in the period. The 2027 renewal: not covered, injury not in that period. And an injury in November 2025, after the 2020 Retroactive Date, claimed in February 2026: not covered, injury not in the period, so the Retroactive Date never operates.
Evidence: X1, three assertions.

**X2. "Anywhere in the world" for products is cut back to suits brought in Vietnam.**
src:153-157, 46-49.
Scenario: a product sold for use in Vietnam injures a buyer abroad, who sues where injured. The place is inside the territory's limb (3), but the proviso requires the original suit to be brought subject to the Jurisdiction clause, and the Jurisdiction clause takes a foreign judgement out of the indemnity anyway. The same proviso reaches an injury in Vietnam sued on abroad (fork F2).
Evidence: X2.

**X3. The CGL part's own products and completed operations aggregates have nothing to apply to.**
src:512-514, 535-536, 710-713.
III gives the CGL part aggregates for the products and completed operations hazards; the Special Condition removes both hazards from the CGL part.
Evidence: X3 (the aggregate test is true for a products claim the CGL part does not cover).

**X4. The only printed figures are in two foreign currencies, which disagree, with no conversion rule.**
src:28, 34, 942, 949.
Supplementary Payments cap a bail bond at US$250 and a day's earnings at US$25; the Ultimate Net Loss Clause restates the same items with S$250.00 and S$25.00. Neither is dong, and no rate, date or source is given (forks F4, F5). At the hypothetical rates of the tests (26,000 and 19,000 dong), the same sums give 90,550,000 under one clause and 89,100,000 under the other.
Evidence: X4.

**X5. Under separate limits, nothing says which limit absorbs defence and the other sums when an occurrence causes both bodily injury and property damage.**
src:18, 504-540, 923-924.
They are "inclusive in the applicable limit", and there are two (fork F11).
Evidence: X5 (declined by name).

**X6. "Did not know or could not reasonably have foreseen" lets a foreseeable claim through.**
src:734-736.
As written, the proviso fails only if an insured both knew and could have foreseen; an objective test ("could reasonably have foreseen") joined by "or" to a subjective one does no work (fork F22).
Evidence: X6 (holds as written; fails on the "neither ... nor" reading).

**X7. Notice of circumstances saves a later products claim, not a completed operations claim.**
src:746-750.
Clause 4 speaks only of circumstances "by reason of the named insured's products", although the part covers both hazards.
Evidence: X7 (the same facts, products: covered; completed operations: not).

**X8. Any departure from any term bars the action, and a judgement must follow an actual trial.**
src:231-234, with 209-227.
"Full compliance with all of the terms" is a condition precedent, so late notice under Condition 3(a) bars the action entirely, however little it cost the Company; and a judgement on default or by consent is not "after actual trial", so only a three-way written agreement replaces a trial. **LAW:** Law Art. 46 and Art. 19(3) point the other way (fork F14).
Evidence: X8.

**X9. The Ultimate Net Loss Clause names coverages "Y" and "Z", which no part of the document defines.**
src:923.
Reading only (inert: no rule can reach a coverage that does not exist).

**X10. The War and Terrorism Exclusion applies on the Company's allegation alone, until the insured disproves it.**
src:976-977.
The allegation needs no stated ground: discretion with no criteria.
Evidence: X10 (no war or terrorism found; excluded).

**X11. The Cyber Liability Exclusion reaches any business done by e-mail or online.**
src:819-821.
"any claim or loss arising out of any activities and/or business conducted and/or transacted via ... the transmission of electronic mail": on a literal reading, a product ordered by e-mail that injures its buyer is excluded under both parts. For most businesses the cover is illusory to that extent.
Evidence: X11.

**X12. Three notice standards for one event.**
src:212, 214, 734.
Condition 3(a) asks for notice "as soon as practicable", 3(b) "immediately", and the Claims Made Basis Endorsement for "immediate notice ... in accordance with the Conditions", which the Conditions do not define. Reading only: the encoding takes each as a finding (fork F12).

**X13. The Company may cancel for any reason on ten days' notice that need never arrive.**
src:290-295.
Mailing is "sufficient proof of notice", so the ten days run from posting. **LAW:** Law Art. 26 lists the grounds for unilateral termination (fork F35). Reading only for the grounds; the ten days are tested (A14).

**X14. Defence and the other supplementary sums come out of the limit.**
src:18, 923-924.
Scenario: damages of 4,950,000,000 and the ordinary other sums of 89,100,000 against a 5,000,000,000 limit: the Company pays 5,000,000,000 and 39,100,000 of the damages are the insured's, because the defence was paid from the same limit.
Evidence: X14.

**X15. The named insured's employees are not insureds.**
src:462-499, 643-657.
Only paragraph (e) of the CGL part (operators of registered mobile equipment on a highway) reaches an employee; the P&CO part has no (e). An employee sued personally for a workplace accident is not covered.
Evidence: X15.

**X16. Under the combined single limit, the CGL part has no aggregate at all.**
src:808-810, 710-713.
The aggregate reaches only products and completed operations, which the CGL part excludes; every premises occurrence in the year has a fresh "each occurrence" limit. A finding for the insurer.
Evidence: X16.

**X17. A defined term used in a form it does not define.**
src:135-137.
"named insured products" is defined; "named insured's products" is used in it and everywhere else (fork F3). Reading only.

**X18. The refund on the named insured's own cancellation, and the premium, cannot be computed from the policy.**
src:182-183, 297.
Both depend on tables and rules not in the document.
Evidence: X18; A8.

**X19. The aggregate limit's period is not stated.**
src:514, 522, 675, 683, 809.
"aggregate" is never tied to the policy period or a year. Reading only; the encoding takes the caller's figure for what has already been paid out of it.

**X20. The Sistership clause obliges a recall at the insured's own cost on a mere expectation of harm, on pain of losing cover for later harm, with no criteria for a "justifiable reason".**
src:904-916.
Paragraph 1 is triggered where harm "is expected to occur"; paragraph 3 refuses the cost; paragraph 2 excludes later harm unless the failure had a "justifiable reason", which is undefined. Evidence of the mechanism: tests C10 (Sistership); the missing criteria are reading only.

**X21. The policy states no deadline for the claim documents, for the Company's assessment or payment, or for suit; and the Law's one year can run out while Condition 4 still waits for a trial.**
src:207-241.
**LAW:** Law Art. 30(3) counts the year for submitting a claim dossier from the third party's demand; Condition 4 withholds any action until the insured's obligation is fixed after actual trial. A policyholder who waits for the trial before filing may be out of time under the Law (fork F36). Reading only.

**X22. CGL exclusion (g) is surplus.**
src:378-383, 952-977.
The War and Terrorism Exclusion excludes all war loss in every part, so (g)'s limit to incidental contracts and first aid does no work. Reading only.

**X23. The Company may investigate and settle "as it deems expedient", with no criteria, while the excess over the limit stays with the insured.**
src:334, 572-573.
Read with X14: the Company controls a settlement that is paid from a limit which also pays its own defence costs. Reading only.

## 5. Answer table

The document has no fee or benefit table. Its answers are a matrix of which clause reaches which part, and the few figures it prints.

| clause | src | CGL part | P&CO part |
| --- | --- | --- | --- |
| insuring agreement | 325-336, 563-575 | harm occurring in the period | harm occurring in the period, within the products or completed operations hazard |
| claims made in the period | 731-736 | — | yes, and Retroactive Date, immediate notice, knowledge proviso |
| Claim Series Clause | 757-776 | — | yes |
| own exclusions | 342-457, 581-637 | (a)-(q), 17 | (a)-(i), 9 |
| contractual liability | 342-344, 581-583 | excluded except incidental contracts and warranties | excluded except warranties |
| injury to employees | 408-410, 606-607 | excluded except incidental contracts | excluded |
| Persons Insured (e), mobile equipment on a highway | 481-497 | yes | — |
| Completed Operations Hazard and Products Hazard Exclusion Clause | 708-713 | yes | — |
| Business Risk Exclusion | 718-724 | — | yes |
| Asbestos, Cyber, Date Recognition, Electromagnetic Fields, Radioactive, Professional, Punitive, Sanction, Sistership, War & Terrorism | 783-977 | yes | yes |
| Combined Single Limit aggregate | 808-810 | never applies (X3, X16) | always applies |

| figure | value | src | tested |
| --- | --- | --- | --- |
| bail bond cap (Supplementary Payments) | US$250 per bond | 28 | A2: at 6,500,000 and 6,500,001 dong |
| loss of earnings cap (Supplementary Payments) | US$25 per day | 34 | A2: 650,001 dong |
| bail bond cap (Ultimate Net Loss) | S$250.00 per bond | 942 | A1: at 4,750,000 and 4,750,001 dong |
| loss of earnings cap (Ultimate Net Loss) | S$25.00 per day | 949 | A1: at 475,000 and 475,001 dong |
| the Company's notice of cancellation | not less than 10 days after mailing | 292 | A14: the 10th and the 9th day |
| audit after final termination | 3 years | 204 | A9: the last day and the day after |
| later claims of a series | within 120 months of the first | 775-776 | C9: 10 May 2036 and 11 May 2036 |

## 6. What `check.sh` prints

```
module                                    errors satisfied  failed  refused  expected
msig-cgl-answer.l4                             0         0       0        0         0
msig-cgl-conditions.l4                         0         0       0        0         0
msig-cgl-definitions.l4                        0         0       0        0         0
msig-cgl-general.l4                            0         0       0        0         0
msig-cgl-nouns.l4                              0         0       0        0         0
msig-cgl-part-cgl.l4                           0         0       0        0         0
msig-cgl-part-pco.l4                           0         0       0        0         0
msig-cgl-record.l4                             0         0       0        0         0
msig-cgl-special.l4                            0         0       0        0         0
msig-cgl-tests-amounts.l4                      0        87       0        0         0
msig-cgl-tests-cover.l4                        0       176       0        0         0
msig-cgl-tests-findings.l4                     0        22       0        0         0
msig-cgl-tests-fixtures.l4                     0         0       0        0         0
TOTAL (13 modules)                             0       285       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

No failure or refusal is expected and none occurs, so `check.sh`'s `expected_failed` table is unchanged (every module 0).
The rule modules carry no assertions; the 285 are 176 in `msig-cgl-tests-cover.l4` (layer 1), 87 in `msig-cgl-tests-amounts.l4` (layers 2 and 3) and 22 in `msig-cgl-tests-findings.l4` (the evidence for §4).
Refusals that are part of the encoding are tested as such, with `#ASSERT REFUSED … BECAUSE "…"` (an empty record; a missing Retroactive Date; missing Claim Series dates; the premium under the Company's rules; the short rate table; a cancellation by someone other than the named insured or the Company; an excess policy against a primary one; separate limits with both kinds of harm and supplementary sums), so they count as satisfied, not refused.
`msig-cgl-tests-amounts.l4` also carries seven `#TRACE` directives over the duties (Conditions 1, 3(a), 3(c), 6, 9 and Sistership 1); they are not assertions and `check.sh` does not count them.

## 7. `vnsrc check`

The gate (every `.l4` and every `.md` in this directory except BRIEF.md, the lead's file), run on 2026-10-07:

```
python3 -I tools/vnsrc.py check ../../source/raw/msig-cgl.txt msig-cgl-*.l4 COMPARABLES.md GLOSSARY.md NOTES.md PROGRESS.md SOURCE-LICENSE.md
vnsrc check: 632 src: lines, 0 Vietnamese runs, 0 problems
```

The brief's literal command, `*.l4 *.md`, also reads BRIEF.md, and reports two problems, both in BRIEF.md (a Vietnamese word at its lines 46 and 50, which this English-only source does not contain). Its last line:

```
vnsrc check: 632 src: lines, 2 Vietnamese runs, 2 problems
```

The "0 Vietnamese runs" on my files is the expected count: the source has no Vietnamese, so every Vietnamese word in this deposit is a translation on a `[translator]` line, which the checker exempts.

## 8. Open questions for a domain expert

1. F20 and X1: does MSIG administer the P&CO part as a pure claims-made cover, the Retroactive Date governing when the harm may occur? If so, the definitions of "bodily injury" and "property damage" are not doing what the form says.
2. F4, F5 and X4: does MSIG issue this form in Vietnam with caps in dong, and which of US$ and S$ does it apply? Is there a Vietnamese text of the form?
3. F10: when the schedule states separate bodily injury and property damage limits, does MSIG treat the Combined Single Limit Endorsement as not applying?
4. F14 and X8: has a Vietnamese court read a "full compliance" condition precedent against Law Art. 46 and Art. 19(3)?
5. F35 and X13: may an insurer and policyholder agree grounds of unilateral termination beyond those of Law Art. 26?
6. F37: does Law Art. 54(3) reach a liability policy?
7. X21: how do insurers in practice reconcile the one-year dossier period of Law Art. 30 with a "judgement after actual trial" condition?
8. The Law's transitional provisions (beyond Article 130 of the aid) were not available: does the 2022 Law govern a policy on this 2015 form issued before 2023?
