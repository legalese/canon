# Cat Act 2011 (WA) and Cat Regulations 2012 — encoding notes (`legalese-aswathy`)

Read this first. `BRIEF.md` is the specification this encoding was written to; `inputs/PROVENANCE.md` says where every source came from.

## 1. What is encoded, and what is not

**Encoded: the whole of the Cat Act 2011** (consolidation 00-l0-01, in force from 25 September 2025 — ss 1–88, s 48 being deleted) **and the whole of the Cat Regulations 2012** (consolidation 02-b0-00, in force from 24 July 2025 — regs 1–30 and Schedules 1–3).
Every section and regulation has a row in the coverage table below, and none is `deferred`.

The encoding states the law **as in force from 25 September 2025**.
For any earlier date it refuses (`no source is encoded for a date before 25 September 2025 …`): earlier versions were not fetched, and the current text must not answer for a past date.
The one known future change, the *Evidence Act 2025* s 492(1) amendment of s 75(3) on 18 September 2027, swaps a cross-reference and changes no computed answer.

**Not encoded**, by the brief: the *Cat (Uniform Local Provisions) Regulations 2013* (read only to confirm what they prescribe under the Act — see §3), local laws, the *Cat Amendment (Local Laws) Bill 2026*, and the other Acts the Cat Act points to (Dog Act 1976, Animal Welfare Act 2002, Veterinary Practice Act 2021, Local Government Act 1995, Criminal Investigation Act 2006, Rates and Charges (Rebates and Deferments) Act 1992). Whatever those decide — that someone is a veterinarian, a pensioner, convicted under the Dog Act — is an input.

**Independence.** This row was written from the sources without opening the other encodings of this Act in canon (`../legalese-michael/`, `../../../cat-act-2011-lqa/`).
One file in the LQA directory was read, and it is a source, not an encoding: the as-passed text of the *Evidence Act 2025*, to see what its s 492(1) does to the Cat Act (`inputs/PROVENANCE.md`).

### How the encoding treats each kind of provision

| kind of provision | shape | example |
| --- | --- | --- |
| offence ("must …", "Penalty: a fine of $5 000") | a BOOLEAN test of whether facts contravene it, with its exemptions and defences, and the maximum fine as a separate constant (a ceiling, not an amount owed) | `s 5(1) is contravened on … by … as to …`, `s 5(1) — maximum fine` |
| a duty with a time limit | the same BOOLEAN on the calendar (Interpretation Act s 61), and a `DEONTIC` with `WITHIN` for `#TRACE` | ss 13, 15, 20, 24, 25, 40 |
| "must refuse … if, and only if" (s 9) | a total outcome type: must refuse (with the grounds), must grant, may refuse to consider | `Registration determination` |
| "may refuse … only if" (s 37) | a total outcome type that keeps the discretion: may refuse (with the grounds), is not to refuse, may defer, is to grant | `Breeding approval determination` |
| a power ("may seize", "may cancel") | a BOOLEAN that the power is available — never that it must be used | ss 10, 27, 34, 38, 49 |
| a list the source prints and nothing computes | a `LIST OF STRING`, quoted | reg 16, reg 17, s 52, s 75(1) |
| a judgement ("satisfied", "believes on reasonable grounds", "reasonable costs", "fit and proper") | an input field — the finding is someone's, not the encoding's | `Breeding application findings`, `Seizure` |

## 2. Coverage table

Dispositions: **encoded** (a rule computes it), **inert** (carried as text or data; nothing to compute), **input** (the provision's content is a fact the caller supplies).
Module abbreviations: `P1` = `cat-part1-preliminary.l4`, `D1` = `cat-part2-div1-registration.l4`, `D23` = `cat-part2-div2-3-microchip-sterilise.l4`, `D45` = `cat-part2-div4-5-transfer.l4`, `P3` = `cat-part3-management.l4`, `P4` = `cat-part4-enforcement.l4`, `P57` = `cat-part5-7-subsidiary-misc.l4`, `S3` = `cat-regs-sch3-fees.l4`, `T` = `cat-time.l4`.

### Cat Act 2011

| s | heading | disposition | where |
| --- | --- | --- | --- |
| 1 | Short title | inert | P1 |
| 2 | Commencement | inert — every date is before 25 Sep 2025; s 2(c) carried as data and used by s 86 | P1, P57 |
| 3 | Terms used | encoded: authorised person, cat management facility, microchip, microchip database company, microchip implanter, microchipped, sterilised, registered, registered owner, approved cat breeder; "transfer", "premises", "public place", "veterinarian" are inputs or text; (2) noted (it does not carry "working day", fork F-01) | P1 |
| 4 | Term used: owner | encoded, (1)(a)–(c) and (2) | P1 |
| 5 | Cats to be registered | encoded, (1)–(2) | D1 |
| 6 | Cats to wear tags | encoded, (1)–(3) | D1 |
| 7 | Interference with tag | encoded | D1 |
| 8 | Application for registration | encoded (who may apply); (2) via regs 11 and Sch 3 | D1, S3 |
| 9 | Registration | encoded, (1)–(7) | D1, P1 (reg 12) |
| 10 | Cancellation of registration | encoded (a power) | D1 |
| 11 | Registration numbers, certificates and tags | encoded (tag colour, reg 15); the rest inert | D1 |
| 12 | Register of cats | inert; reg 16's list carried | D1 |
| 13 | Notice of decisions under Subdivision 2 | encoded (deadline, and `DEONTIC`) | D1 |
| 14 | Cats to be microchipped | encoded, (1)–(3) | D23 |
| 15 | Implanter to inform the database company | encoded (deadline, and `DEONTIC`); reg 17 carried | D23 |
| 16 | Microchip database company's obligations | encoded (the keeping is an input) | D23 |
| 17 | Interference with microchips | encoded | D23 |
| 18 | Cats to be sterilised | encoded, (1)–(3) | D23 |
| 19 | Identifying as sterilised a cat that is not | encoded, with reg 18 | D23 |
| 20 | Notice of sterilisation to the database company | encoded (deadline, and `DEONTIC`) | D23 |
| 21 | Certificate of sterilisation | encoded (no time fixed: Interpretation Act s 63; whether the time has passed is an input) | D23 |
| 22 | Terms used (purchaser, seller) | inert — the `Transfer` record names both | D45 |
| 23 | Transfer of ownership of cats | encoded, (1)–(3), with reg 19 | D45 |
| 24 | Notice of transfer | encoded (deadline; two concurrent `DEONTIC`s joined by `RAND`) | D45 |
| 25 | Notice of changes to recorded information | encoded | D45 |
| 26 | Cat control notice | encoded (power), (2) carried | P3 |
| 27 | Cats may be seized | encoded | P3 |
| 28 | Disposing of seized cats | encoded | P3 |
| 29 | Application of Division 3 | encoded | P3 |
| 30 | Obligation to identify owner | encoded, (1)–(2) | P3 |
| 31 | Owner liable for facility costs | encoded (sum of the reasonable costs, which are inputs); (2) inert | P3 |
| 32 | Notice to identified owner | encoded (what the notice lacks; the offence) | P3 |
| 33 | Facility may have the cat microchipped and sterilised | encoded (permissions; beliefs are inputs) | P3 |
| 34 | Unidentified and unclaimed cats | encoded, (1)–(2), working days | P3 |
| 35 | Only approved breeders may breed | encoded (1); (2)–(4) court orders inert | P3 |
| 36 | Application for approval to breed | encoded (who may apply); fee in S3 | P3, S3 |
| 37 | Approval to breed | encoded, (1)–(6), with regs 22–24 | P3 |
| 38 | Cancellation of approval | encoded (a power) | P3 |
| 39 | Certificate to approved breeder | inert (Form 4) | P3 |
| 40 | Notice of breeding decisions | encoded (deadline, and `DEONTIC`) | P3 |
| 41 | Cats not to be offered as prizes | encoded | P3 |
| 42 | Administration by local governments | inert | P4 |
| 43 | Places regarded as within district | (1) inert; (2) encoded | P4 |
| 44 | Delegation by local government | encoded | P4 |
| 45 | Delegation by CEO | encoded (1), (2), (6); (3)–(5) inert (conditions on the instrument) | P4 |
| 46 | Other matters about delegations | encoded (1)(a); rest inert | P4 |
| 47 | Register and review of delegations | encoded (2) (financial year); (1), (3) inert | P4 |
| 48 | [deleted: No. 16 of 2019 s 92] | inert — noted | P4 |
| 49 | Authorised person may cause destruction | encoded (1)–(2); (3) inert | P4 |
| 50 | Name on demand | encoded | P4 |
| 51 | Power to enter premises | encoded (1)–(3); (4)–(5) inert | P4 |
| 52 | General powers | inert — listed | P4 |
| 53 | Powers of police officers not derogated from | inert | P4 |
| 54 | Obstruction | encoded | P4 |
| 55 | Grounds for a search warrant | encoded (a power of the justice) | P4 |
| 56 | Grounds for a warrant to seize | encoded | P4 |
| 57 | Application for warrant | inert | P4 |
| 58 | Form of warrant | inert (Form 5, reg 26) | P4 |
| 59 | Effect of warrant | inert | P4 |
| 60 | Execution of warrant | encoded (1); (2) inert | P4 |
| 61 | Terms used (Div 4) | encoded — "prescribed" includes a local law (`Prescription for infringement`) | P4 |
| 62 | Giving an infringement notice | encoded, (1)–(3) | P4 |
| 63 | Content of infringement notice | encoded (1)(b), (2), (3); (1)(a), (c) inert | P4 |
| 64 | Extension of time | encoded (the extension is an input) | P4 |
| 65 | Withdrawal of notice | encoded | P4 |
| 66 | Benefit of paying | encoded (1)–(2); (3) inert | P4 |
| 67 | Application of penalties collected | inert | P4 |
| 68 | When Division 5 applies | encoded | P4 |
| 69 | Objection may be lodged | encoded | P4 |
| 70 | Dealing with objection | encoded (1)–(2); (3)–(5) inert, (4) listed | P4 |
| 71 | Review of decisions | encoded, (1)–(3) | P4 |
| 72 | Suspension of some decisions | encoded | P4 |
| 73 | Prosecutions | encoded (1); (2)–(3) inert | P4 |
| 74 | Additional court orders | encoded (when the court may order); orders listed | P4 |
| 75 | Evidentiary matters | inert — listed | P4 |
| 76 | General regulations | inert | P57 |
| 77 | Regulations operating as local laws | encoded (6); (1)–(5) inert | P57 |
| 78 | Provisions about regulations | encoded (b)–(c) ceilings; rest inert | P57 |
| 79 | Local laws | encoded (2); (1), (3) inert, (3) listed | P57 |
| 80 | Places outside district | encoded (1)–(3); (4) inert | P57 |
| 81 | Inconsistency with written laws | encoded | P57 |
| 82 | Local laws may adopt codes | inert | P57 |
| 83 | Model local laws | inert | P57 |
| 84 | Creating offences and penalties | encoded (1)–(2); (3)–(5) inert | P57 |
| 85 | False or misleading information | encoded | P57 |
| 86 | Review of Act | encoded (review points, report deadline) | P57 |
| 87 | Transitional — LG Legislation Amendment Act 2019 | encoded | P57 |
| 88 | Transitional — Stop Puppy Farming Act 2021 | encoded (3); commencement day is an input (not proclaimed) | P57 |

### Cat Regulations 2012

| reg | heading | disposition | where |
| --- | --- | --- | --- |
| 1 | Citation | inert | — |
| 2 | Commencement | inert — all before 25 Sep 2025 | — |
| 3 | Term used: Form | inert | — |
| 4 | Cat management facility operators | encoded | P1 |
| 5 | Microchip devices | encoded (1)–(3) | P1, D23 |
| 6 | Microchip database companies | encoded | P1 |
| 7 | Microchip implanters | encoded | P1 |
| 8 | Microchipping cat | encoded | P1 |
| 9 | Cats exempt from registration | encoded | D1 |
| 10 | Cats exempt from wearing tag | encoded | D1 |
| 11 | Application for registration | encoded (Form 1 parts listed); fee in S3 | D1 |
| 12 | Period of registration | encoded (1), (2)(a), (2)(b) | P1, D1 |
| 13 | Changes in registration | encoded | D1 |
| 14 | Registration certificate | inert (Form 2) | D1 |
| 15 | Registration tags | encoded (colour); (1)(a)–(b) inert | D1 |
| 16 | Information in the register | inert — listed | D1 |
| 17 | Information from implanter | inert — listed | D23 |
| 18 | Manner of identifying as sterilised | encoded | D23 |
| 19 | Transfer of exempt cats | encoded | D45 |
| 20 | Cat control notice | inert (Form 3) | P3 |
| 21 | Application for approval to breed | encoded (Form 1 parts listed); fee in S3 | P3 |
| 22 | Other refusal circumstances | encoded (1)–(2) | P3 |
| 23 | Person who may not be refused | encoded | P3 |
| 24 | Duration of approval | encoded | P3 |
| 25 | Breeder's certificate | inert (Form 4) | P3 |
| 26 | Warrant | inert (Form 5) | P4 |
| 27 | Infringement notice | inert (Form 6) | P4 |
| 28 | Withdrawal of infringement notice | inert (Form 7) | P4 |
| 29 | Objection | inert (Form 8) | P4 |
| 30 | Modified penalties | encoded, with Schedule 2 | P4 |
| Sch 1 | Forms 1–8 | inert — blanks to fill in. Form 1 Part A's "(Owner must be 18 years or older)" restates s 9(2)(a) | — |
| Sch 2 | Modified penalties, items 1–14 | encoded, every row | P4 |
| Sch 3 | Fees, cl 1 and items 1–4 | encoded, every row; cl 1(4) (reduce or waive) is a discretion left to the caller | S3 |

**Offence count, measured mechanically.** `grep -c 'Penalty: a fine' inputs/cat-act-2011.txt` prints 22: 21 sections, with s 23 carrying two. The Regulations carry two more (reg 5(2), (3)). The `Offence` type has exactly these 24 members, and `tests-part4-enforcement.l4` asserts the count.

## 3. Fork register

Each entry: the text, the readings, the one taken, and why. Nothing here has been settled by a court or the regulator that I found; I looked only at the instruments themselves, not at case law or departmental guidance.

| id | provision | the question | readings | taken | why |
| --- | --- | --- | --- | --- | --- |
| F-01 | ss 32(b), 34(1) "working days" | defined nowhere that reaches the Cat Act | (A) ordinary meaning: not a Saturday, Sunday or public holiday; (B) the Local Government Act 1995 Sch 4.1A cl 1 definition; (C) Interpretation Act s 61(2) "excluded day" in reverse | A | Cat Act s 3(2) imports LG Act definitions, but the LG Act defines "working day" only "In this Schedule", so it does not reach the Cat Act. All three readings give the same set of days once public, public-service and bank holidays are in the input list. |
| F-02 | ss 9(2)(e), 10(b), 37(2)(d), reg 22, reg 23(b): "within the previous 3 years", "within the period of 12 months before" | is an event on the anniversary inside? | (A) outside; (B) inside | A | Reckoned with Interpretation Act s 62(3): the period of n months that begins on the event day has ended by the anniversary. A one-day edge; a court could read it either way. |
| F-03 | reg 12(2)(a)(i) "the next 31 October" | for a registration taking effect on 31 October itself | (A) the following year's 31 October; (B) the same day | A | A one-year registration that expires the day it starts is absurd. |
| F-04 | reg 12(2)(a)(ii) "31 October in the final year of that period" | how are the 3 years counted? | (A) three registration years (1 Nov – 31 Oct), so the third 31 October; (B) three calendar years from the effective date, so 31 October of the calendar year in which the third anniversary falls (which can be after the anniversary) | A | Consistent with (i): a one-year registration ends at the first 31 October, so a 3-year one ends at the third. Reading B can end months after three years have run. **Worth a domain expert's view** (§6). |
| F-05 | s 4(1) "any of these persons" | a child keeper and their parent | (A) both are owners; (B) the parent replaces the child | A | "any of these persons" lists alternatives that can coexist; (c) adds a person rather than substituting one. The child is in any case refused registration (s 9(2)(a)). |
| F-06 | s 5(2)(a) "the cat has been kept by the person for less than 14 days" | how are days counted, and whose keeping counts for an owner who does not keep it (a parent, a database owner)? | counting: (A) whole days since the keeping began; (B) inclusive of both ends. Whose keeping: (A) the person's own, else the earliest current keeper's; (B) the exemption is unavailable to a non-keeper | A, A | Counting A follows s 61(1)(b) (the start day is not counted). For a non-keeping owner, the keeping that makes them an owner is the natural reference. |
| F-07 | ss 9(2)(e), 10(b), 37(2)(d), 74(1), reg 23(b): "an offence against this Act" | does an offence against regulations or a local law made under the Act count? | (A) no — the Act itself only; (B) yes | A | Interpretation Act s 5 defines "Act" apart from "subsidiary legislation"; Cat Act s 62(1) says "this Act or a regulation or local law made under this Act" when it means both, and s 77(5) extends "local law" to s 77 regulations expressly. The same reading is applied to the Dog Act and the Animal Welfare Act. |
| F-08 | s 9(2)(e), s 37(2)(d), reg 23(b): "within the previous 3 years" — of what day? | (A) the day the application is determined; (B) the day it is made | A | s 9(2) and s 37(2) turn on what the local government "is satisfied" of, which it is when it decides. |
| F-09 | s 9(2)(c), (d) | a kitten under 6 months that is not microchipped or not sterilised | (A) refusal is mandatory; (B) the age threshold of ss 14(1), 18(1) is read into s 9(2) | A | s 9(3)–(4) relieve only a cat "exempt … as referred to in section 14(2) / 18(2)", and a certificate "cannot apply" under 6 months (ss 14(3), 18(3)). Not being *required* to be microchipped is not being *exempt*. The text is clear; the result (a kitten cannot be voluntarily registered) may not be what was intended — **a question for a domain expert** (§6). |
| F-10 | Sch 3 item 1(a) "made after 31 May for registration until the next 31 October" | an application in November–December | (A) only June–October counts as "after 31 May"; (B) any date after 31 May in the calendar year | A | Under reading B a grant made on 15 December, which buys more than ten months, would get the half fee meant for the last five months of a registration year. |
| F-11 | Sch 3 cl 1(3) "if the owner of a cat is a pensioner" | owner or applicant? | (A) the applicant, who must be an owner (s 8(1)); (B) any owner | A | Only an owner may apply; where several people own the cat, which one's status counts is not said, and the applicant is the one in front of the local government. |
| F-12 | reg 19 "an organisation or person set out in regulation 9" | is a foster carer "set out"? | (A) no — the named bodies (including the SAFE entities of reg 9(1)) and the custodians of reg 9(2) only; (B) also foster care placed by those bodies | A | reg 9(3) describes a placement, not a person; no person is named. Reading B would exempt transfers into foster care from s 23. |
| F-13 | s 37(4), (5); reg 22(2) | when several apply: refuse to consider, "is not to refuse", "may defer" | order taken: refuse to consider → not to refuse → may defer → may refuse → grant | as listed | Refusing to *consider* is not refusing to *grant*, so s 37(5) does not bar it; reg 22 is headed "(s. 37(2)(f))", so "Despite subsection (2)" in s 37(5) is read to override its deferral power too. |
| F-14 | s 38 "the things set out in section 37(2)" | on which day, and how does reg 22(1)'s "prior to the application" read for a cancellation? | (A) tested on the day of cancellation, 12 months counted back from it; (B) reg 22(1) does not reach s 38 at all | A | s 38 incorporates all of s 37(2), which includes (f); a cancellation has no application, so the day of cancellation stands in for it. |
| F-15 | reg 22(1) "issued to, and paid by, the applicant within the 12 months prior" | which must fall within the 12 months — issue or payment? | (A) issue; (B) both | A | The payment date is not in the inputs; "issued … within the 12 months" is the natural reading of the sentence's structure. |
| F-16 | s 71(1)(a), (3) and example (a) | when does the right to apply for review arise without an objection? | (A) when notice of the decision is given; (B) on the decision, as the example says | A | s 71(1) gives the right only to "A person who has been given notice under section 13 or 40". The two agree when notice is given on the day of the decision. |

Two smaller readings, recorded here so they are not silent:

- **s 9(5)–(6) and s 37(3)–(4).** A request for documents that allowed *more* than 21 days is not a requirement under (5), so failing to meet it gives no power to refuse to consider.
- **s 32(d) "where relevant".** Read as: (i) is relevant when the operator believes the cat is not microchipped, and (ii) when it believes it is not sterilised — the beliefs that open s 33.

## 4. Answer tables

### Schedule 3 — fees (Cat Regulations 2012 Sch 3 cl 1)

| application | fee | pensioner (cl 1(3)) | source |
| --- | --- | --- | --- |
| registration, one year — a **grant** applied for 1 June – 31 October (fork F-10) | $10.00 | $5.00 | item 1(a) |
| registration, one year — any other grant, and every renewal | $20.00 | $10.00 | item 1(b) |
| registration, 3 years | $42.50 | $21.25 | item 2 |
| registration, life of the cat | $100.00 | $50.00 | item 3 |
| approval to breed, grant or renewal | $100.00 per breeding cat | **$100.00 per breeding cat** — cl 1(3) covers registration only | item 4 |

A local government "may reduce or waive" any of these (cl 1(4)); the figures are the most that can be charged.

### Schedule 2 — modified penalties (reg 30)

| item | offence | modified penalty | maximum fine | ≤ 10%? (s 63(3)) |
| --- | --- | --- | --- | --- |
| 1 | s 5(1) unregistered cat | $200 | $5 000 | yes |
| 2 | s 6(1) not wearing tag in public | $200 | $5 000 | yes |
| 3 | s 7 interfering with tag | $200 | $5 000 | yes |
| 4 | s 14(1) not microchipped | $200 | $5 000 | yes |
| 5 | s 17 interfering with microchip | $200 | $5 000 | yes |
| 6 | s 18(1) not sterilised | $200 | $5 000 | yes |
| 7 | s 19 identifying as sterilised a cat that is not | $200 | $5 000 | yes |
| 8 | s 23(1) transferring an unchipped cat | $200 | $5 000 | yes |
| 9 | s 23(2) transferring an entire cat | $200 | $5 000 | yes |
| 10 | s 24 no notice of new owner | $200 | $5 000 | yes |
| 11 | s 25 no notice of change of details | $200 | $5 000 | yes |
| 12 | s 35(1) breeding without approval | $200 | $5 000 | yes |
| 13 | s 41 cat as a prize | $200 | $5 000 | yes |
| 14 | s 50(2) refusing name on request | $200 | $5 000 | yes |

The other ten offences (ss 15, 16, 20, 21, 30(1), 32, 54, 85; regs 5(2), 5(3)) are not prescribed by these Regulations. Under s 61 a local law may prescribe an offence against the Act, so the encoding says "not prescribed by the Cat Regulations 2012; a local law may prescribe it" rather than "not prescribed".

### Registration periods (reg 12(2)(a))

| term | takes effect | last day of effect |
| --- | --- | --- |
| one year | 1 Nov 2025 | 31 Oct 2026 |
| one year | 15 Mar 2026 | 31 Oct 2026 |
| one year | 31 Oct 2025 | 31 Oct 2026 (fork F-03) |
| 3 years | 1 Nov 2025 | 31 Oct 2028 (fork F-04) |
| life | any | the death of the cat (or cancellation) |

A renewal may take effect from 1 November if made in the 21 days before it, 11–31 October (reg 12(2)(b) with Interpretation Act s 61(1)(c)).

## 5. What `check.sh` prints

Run with `L4=~/.local/bin/l4 ./check.sh`, on `l4` built from `legalese/l4-ide` `unstable` at `7768812fa` (2 October 2026). Recorded on 2026-10-05, after the independent test pass's repairs:

```
module                                    errors satisfied  failed
cat-domain.l4                                  0         0       0
cat-part1-preliminary.l4                       0         0       0
cat-part2-div1-registration.l4                 0         0       0
cat-part2-div2-3-microchip-sterilise.l4        0         0       0
cat-part2-div4-5-transfer.l4                   0         0       0
cat-part3-management.l4                        0         0       0
cat-part4-enforcement.l4                       0         0       0
cat-part5-7-subsidiary-misc.l4                 0         0       0
cat-regs-sch3-fees.l4                          0         0       0
cat-time.l4                                    0         0       0
tests-fixtures.l4                              0         0       0
tests-independent.l4                           0       212       0
tests-part1-time.l4                            0        71       0
tests-part2-identification-transfer.l4         0        57       0
tests-part2-registration.l4                    0        77       0
tests-part3-management.l4                      0        69       0
tests-part4-enforcement.l4                     0       115       0
tests-part5-7.l4                               0        29       0
tests-sch3-fees.l4                             0        16       0
TOTAL (19 modules)                             0       646       0
```

**No assertion is expected to fail.** There is no "expected red" file: the source has no worked examples or draft-stage expectations that the enacted text fails to meet.

**One finding the tests made.** On its first run `tests-part2-identification-transfer.l4` failed one assertion: a plain transfer of an unchipped kitten did not contravene s 23(1). The cause was layout. The rule wrote the inert label `"unless … satisfied that a … certificate applies"` after `NOT` on one line and its operand on the next. The parser attached the operand to the enclosing `AND` chain instead of to the `NOT`, so the rule *required* the seller to be satisfied, which inverts s 23(1). The fix put label and operand on one line; the assertion now passes, and a search found no other `NOT "…"` label with its operand on a following line. The checker separately caught three places where `NOT` would have swallowed an `OR` (`cat-part3-management.l4`, s 32), all fixed with brackets before any test ran.

### The independent test pass (2026-10-05)

A separate session read only `BRIEF.md` and `inputs/`, wrote its expected answers down **before** opening any `.l4` file (`independent-expectations.md`, kept here as the record), then wrote `tests-independent.l4` against the encoding's names.
First run: **212 assertions, 204 satisfied, 8 failed.** Every failure was triaged against the source, and every one was an **encoding error**. None was a test-author error or a genuine ambiguity:

| # | failure | cause | repair |
| --- | --- | --- | --- |
| 1–7 | s 65(1), s 66, s 69, s 71, reg 12(2)(b), reg 24 and s 74 answered for dates before 25 September 2025 instead of refusing, as the brief requires | those rules never read the date gate in `cat-time.l4` | the gate was added to them, and also to the rules the tester named but had not probed: reg 12(2)(a) expiry, s 34(2), s 46, s 47, s 51(3), the s 63/64 payment deadline, s 72 and s 88 |
| 8 | s 65(1): a notice given Fri 2 Oct 2026 could not be withdrawn on Mon 4 Oct 2027, although its year ended on Sat 2 Oct | the rule did not apply Interpretation Act s 61(1)(e), which every other time limit in the encoding applies | s 65(1) now takes the holiday list and applies s 61(1)(e). `tests-part4-enforcement.l4` has the case on both sides. |

After the repairs: **212 of 212 satisfied.** No expected value in `tests-independent.l4` was changed. Only the four s 65 call sites gained the new holiday argument.

Things the tester could not express against the encoding's names, kept so they are not lost:
- the s 63(3) cap at an arbitrary amount ($500 against $501), because the rule reads Schedule 2;
- the date gate on rules that take no date (ss 6(3), 7, 16, 17, 19, 41, the Schedule 2 lookup);
- s 71(1)(a) with the decision and the notice on different days (fork F-16);
- a mid-year 3-year registration (fork F-04).

**s 86 deliberately answers before 25 September 2025.** Its review points (1 Nov 2018, 2023, 2028, …) are dates the current text itself fixes from s 2(c). They are not the law as it stood on a past day, so they are not gated.

## 6. Open questions for a domain expert

1. **Kittens and voluntary registration (F-09).** s 9(2)(c)–(d) appear to make refusal mandatory for any unchipped or entire cat under 6 months, even though the owner is not yet required to register, chip or sterilise it. Is that how local governments apply it?
2. **3-year registrations (F-04).** Does a 3-year registration granted in, say, March 2026 run to 31 October 2028 or 31 October 2029 in practice? Registration certificates (Form 2) state an expiry date — a few real certificates would settle it.
3. **Item 1(a) (F-10).** Is the $10 rate applied only to grants made June–October?
4. **Working days (F-01).** Which holidays do facilities treat as non-working days — State-wide public holidays only, or also regional ones (s 61(2) speaks of "that part of the State which is relevant")?
5. **reg 19 and foster carers (F-12).** Do the Cat Haven and RSPCA foster programmes treat a transfer into foster care as exempt from s 23?
6. **The uncommenced Stop Puppy Farming amendments (Dog Amendment (Stop Puppy Farming) Act 2021 ss 50–61).** When proclaimed they will change the Cat Act's registration machinery (s 88 anticipates a centralised registration system). They were not fetched; this encoding will need a new vintage then.

## 7. Files

| file | what |
| --- | --- |
| `BRIEF.md` | the specification |
| `inputs/` | the source texts, mechanically extracted, and `PROVENANCE.md` |
| `cat-domain.l4` | every noun |
| `cat-time.l4` | Interpretation Act ss 61–62, working days, the in-force gate |
| `cat-part1-preliminary.l4` | Part 1; regs 4–8; reg 12(2)(a) |
| `cat-part2-div1-registration.l4` | ss 5–13; regs 9–16 |
| `cat-part2-div2-3-microchip-sterilise.l4` | ss 14–21; regs 5, 17, 18 |
| `cat-part2-div4-5-transfer.l4` | ss 22–25; reg 19 |
| `cat-part3-management.l4` | ss 26–41; regs 20–25 |
| `cat-part4-enforcement.l4` | ss 42–75; regs 26–30; Sch 2 |
| `cat-part5-7-subsidiary-misc.l4` | ss 76–88 |
| `cat-regs-sch3-fees.l4` | Sch 3 |
| `tests-*.l4` | tests, from the source; `tests-fixtures.l4` holds shared people, cats and the holiday list |
| `tests-independent.l4` | the independent test pass (§5) |
| `independent-expectations.md` | that pass's expected answers, written before it read the encoding |
| `check.sh` | the self-check |
