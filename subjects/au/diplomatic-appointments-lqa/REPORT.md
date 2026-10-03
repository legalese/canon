# LQA report: Diplomatic Appointments (Selection Process) Bill 2026 (Cth)

**Instrument:** Diplomatic Appointments (Selection Process) Bill 2026, private Senator's Bill (Senator Payman).
**Print:** first reading (Senate), introduced 7 September 2026 (Parliament's file 26S2721).
**Legal engineer:** Claude (agent), for Legalese. Steps 7A to 11A run on 2 October 2026.
**Status of this report:** not yet released. Release (12H) needs a named person's signature for one recipient.

The Bill sets up Selection Committees for 15 named diplomatic posts, bars recent members of any Australian legislature from those posts, and limits appointments of people with other political ties. This report gives 30 findings: **23 OPEN** and **7 checked and found sound**. Of the OPEN findings, 8 are medium, 4 low-medium and 11 low. None is high.

The full prose of each finding is in `INCIDENTS.md`. The machine-readable register is `incidents.json`. The console scheme (`scheme.js`, id `dipl-appointments-lqa`) replays every finding. Quotations from the Bill, the explanatory memorandum (EM) and Hansard are held for internal analysis only and are kept to a few words here.

---

## 1. What needs a decision

Four of the medium findings come from the same cause: the Bill's description of itself (the s 3 outline and the EM) promises more than its operative words deliver.

- **X-01.** The outline says a recommended person must be appointed. EM para 18 says the Minister must appoint the recommended candidate. Section 9(2) only *permits* the appointment. Under Acts Interpretation Act s 13 the outline is part of the Act, so the Act contradicts itself on its central feature.
- **X-02.** The outline says the person appointed after two deadlocks must not have a significant political affiliation. Section 9(3)(c)(i) asks only whether the Minister *is satisfied* the person has none.
- **X-24.** EM paras 11, 15 and 34 describe a continuing bar: a person with an affiliation cannot hold or act in the office. Sections 14(1) and (4) test only the *making* of the appointment or arrangement.
- **P-03.** No one is named to appoint, to terminate, or to make or end an acting arrangement. The duty to terminate in s 14(3) and (6) is passive and is triggered by the Minister's awareness. The appointer is the Governor-General (Public Service Act s 39).

The other four medium findings concern the Committee process:

- **L-04.** A Committee that cannot muster all 3 members, or misses its 2 months, is never dissolved, and s 12(8) then bars any other Committee for that appointment.
- **P-05.** The Minister can revoke a Committee's establishing instrument before it reports (Acts Interpretation Act s 33(3)). The revoked Committee counts for nothing, so Committees can be replaced one after another until one recommends the preferred candidate. That is the result EM para 32 says s 12(8) is there to prevent.
- **U-16.** It is unclear whether "member of the staff of" a Minister or shadow Minister (s 8(2)(b)) includes electorate staff. It is also unclear how the phrase maps onto the Members of Parliament (Staff) Act's categories, past and present.
- **U-25.** Breaches of the list, membership and tabling duties (ss 9(4), 10, 12) have no stated consequence, unless s 14(1) takes them in. The Bill does not say whether it does.

---

## 2. Findings, by severity

Found-by codes: RD read, CMP compare, ENC encode, TST test. The test is explained in section 3. Under "Evidence", A is an assertion in L4, Sc a console scenario, Sim a generated simulation run, and Q a quotation from a pinned document.

### OPEN: medium

| ID | Finding | Provision | Found by | Evidence |
|---|---|---|---|---|
| X-01 | Outline says a recommended person must be appointed; s 9(2) only permits it | s 3; s 9(1), (2) | CMP | A, Q, Sc, Sim |
| X-02 | Outline states an objective bar; s 9(3)(c)(i) turns on the Minister's satisfaction | s 3; s 9(3)(c)(i) | CMP | A, Q, Sc |
| P-03 | No appointer, terminator or maker of acting arrangements is named | ss 9(1), 11, 14 | CMP | Q, Sc, Sim |
| L-04 | A stalled Committee is never dissolved, and blocks any other | ss 10(3), (5), 12(4), (8), 13(1), (2) | RD | A, Q, Sc, Sim |
| P-05 | The Minister may revoke a Committee before it reports; it then counts for nothing | s 12(1), (8); s 9(3) | CMP | Q, Sc |
| U-16 | Whose staff count under s 8(2)(b), under which MOP(S) Act (FORK-02) | s 8(2)(b) | CMP | A, Q, Sc, Sim |
| X-24 | EM describes a continuing bar; s 14 tests only the making (FORK-14) | ss 11(2), 14 | CMP | A, Q, Sc |
| U-25 | Process breaches have no consequence unless s 14(1) takes them in (FORK-16) | s 14(1), (3); ss 9(4), 10, 12 | ENC | A, Q, Sc, Sim |

### OPEN: low-medium

| ID | Finding | Provision | Found by | Evidence |
|---|---|---|---|---|
| U-08 | Does a 2-1 vote mean the Committee "agrees"? (FORK-08) | s 10(3)(a); s 13(3) | RD | A, Q, Sc, Sim |
| U-17 | Party "officer or employee" undefined; when must the party be registered? (FORK-03) | s 8(2)(d) | RD | A, Q, Sc, Sim |
| T-19 | Section 15 turns on when "the term of the appointment starts", which no law fixes | s 15 | ENC | A, Q, Sc, Sim |
| U-22 | Must the recommended candidate be on the Minister's list? (FORK-06) | s 10(1), (3)(a), (4) | ENC | A, Q, Sc |

### OPEN: low

| ID | Finding | Provision | Found by | Evidence |
|---|---|---|---|---|
| U-06 | Do Committees for an earlier vacancy count? (FORK-04) | s 9(3)(a), (b); s 10(6) | RD | A, Q, Sc, Sim |
| U-10 | From what day, and how, are "the last 10 years" counted? (FORK-01) | s 8(1), (2)(a) | RD | A, Q, Sc |
| U-20 | Does s 15's 12-month delay cover acting arrangements? (FORK-15) | s 15; s 11 | RD | A, Sc, Sim |
| R-21 | "within 5 sitting days of that House": s 9(5) names no House | s 9(4), (5) | RD | Q, Sc |
| U-23 | Must both Houses resolve before the appointment? (FORK-11) | s 9(3)(c)(ii) | ENC | A, Q, Sc |
| P-27 | Nothing requires a Committee ever to be established; acting has no time limit | ss 11(1), 12(1) | ENC | Q, Sc, Sim |

### Form and Style (OPEN, low)

| ID | Finding | Provision | Found by | Rule breached |
|---|---|---|---|---|
| S-13 | Section 6 definitions not in alphabetical order ("rules" last) | s 6 | RD | OPC Drafting Manual, "Definitions": defined terms in alphabetical order |
| S-28 | Declaratory provisions say "is to" | ss 12(2)-(4), 13(3) | CMP | Plain English Manual para 84 |
| S-29 | No simplified outlines for the Parts | Parts 1-4 | CMP | Drafting Direction 1.3A para 36 |
| F-14 | "Nothing in subsections (3) and (6) limit": verb does not agree | s 14(7) | RD | (none: a slip) |
| F-15 | "applies in relation an appointment": "to" missing (also in EM para 3) | s 15 | RD | (none: a slip) |

### Checked and found sound (VERIFIED-NO-DEFECT)

| ID | Question | What answered it |
|---|---|---|
| L-07 | Does the s 10(2)(b) cap reach a 2-or-3 list under s 10(6)? | s 10(2)(b) on its own terms: a list of 2 or 3 is a list of 2 to 4 (Bill) |
| U-09 | Majority of all members, or of votes cast? (FORK-07) | s 13(3) "of the members", confirmed by EM para 33 |
| D-11 | A long-serving member has both affiliations at once | ss 9(1)(a), 10(2)(a), 11(2): the disqualifying affiliation governs wherever both could matter (Bill) |
| D-12 | "Secretary" defined, never used | Legislation Act 2003 s 13(1)(b): rules under s 16 may use it with the Act's meaning |
| L-18 | A chargé d'affaires faces a stricter test than an appointee | Deliberate: EM para 28 |
| I-26 | Valid under s 14(2) but unable to take effect under PSA s 39(1) | Public Service Act 1999 s 39(1), (2)(a): different questions, with a route for non-APS appointees |
| S-30 | "Minister" defined by another Act, against DD 2.2 para 126 | Drafting Direction 2.2 paras 128-129 (a category 2 reference) |

---

## 3. How findings were found

Each finding records one method, set when it is first recorded: the first test that fits, in this order.

- **RD (read):** a *casual* reader of the provision would have caught it.
- **CMP (compare):** found by setting documents side by side.
- **ENC (encode):** writing the L4 or the console scheme forced the question.
- **TST (test):** a written case surfaced it.
- **SIM (simulate):** a generated run surfaced it.

The test is a casual reader, not a careful one. So it gives the L4 credit for what a careful reader might also have caught.

Leads noticed while reading at step 2A keep the method recorded then. Leads from `ENCODING-NOTES.md` keep the method by which they were noticed.

| Method | Count | Findings |
|---|---|---|
| RD | 13 | L-04, U-06, L-07, U-08, U-10, D-12, S-13, F-14, F-15, U-17, L-18, U-20, R-21 |
| CMP | 9 | X-01, X-02, P-03, P-05, U-16, X-24, S-28, S-29, S-30 |
| ENC | 7 | U-09, T-19, U-22, U-23, U-25, I-26, P-27 |
| TST | 1 | D-11 |
| CHK, SIM, EXT | 0 | |

By category: U 10, S 4, X 3, P 3, L 3, D 2, F 2, T 1, R 1, I 1. No finding has E, M or W as its primary category; E is a secondary category of P-03 and U-25, and W of L-04 and P-27.

**Evidence.** Every finding has machine-checked evidence, and none is opinion.

- **Assertions:** the findings that cite assertions use 227 in `cases.l4` (all satisfied) and 9 new ones in `lqa-evidence.l4` (all satisfied).
- **Quotations:** every quotation is checked against its pinned copy.
- **Scenarios:** 15 console scenarios cover every OPEN finding outside Form and Style.
- **Simulation:** one generated run (seed 2, 365 days, default parameters) records 11 of them: X-01, P-03, L-04, U-06, U-08, U-16, U-17, T-19, U-20, U-25 and P-27.

A finding that a simulation reaches is better evidenced than one a scenario sets up. A scenario can put the world into a state the rules could never reach on their own.

---

## 4. Forks and the readings taken

The encoding found 16 places where the text supports two readings. All 16 were reviewed at 6H, and reading A was confirmed for each. A fork is not a defect. It becomes a finding (category U, or recorded under X) only where the drafter left open a choice that changes an outcome.

| Fork | Provision | Reading taken (A) | Finding |
|---|---|---|---|
| FORK-01 | s 8(1), (2)(a) | the 10 years run back from the end of the day in question; an exact anniversary is outside | U-10 |
| FORK-02 | s 8(2)(b) | electorate employees of a listed position-holder count | U-16 |
| FORK-03 | s 8(2)(d) | the party must have been registered while the role was held | U-17 |
| FORK-04 | s 9(3)(a), (b); s 10(6) | only Committees for the current vacancy count | U-06 |
| FORK-05 | s 10(1) | the day of establishment is not one of the 7 days | none: not consequential |
| FORK-06 | s 10(3)(a) | the recommended candidate must be on the list | U-22 |
| FORK-07 | s 13(3) | majority of all 3 members | U-09 (sound) |
| FORK-08 | s 10(3)(a) | a 2-1 majority is agreement | U-08 |
| FORK-09 | s 9(2); s 3 | no duty to appoint the recommended person | X-01 |
| FORK-10 | s 9(3)(c)(i) | the Minister's satisfaction is the condition | X-02 |
| FORK-11 | s 9(3)(c)(ii) | both resolutions before the appointment | U-23 |
| FORK-12 | s 9(4) | statement needed even if both Houses also approved | none: not consequential |
| FORK-13 | s 9(5) | sitting days counted after the day of appointment | none: not consequential (see R-21) |
| FORK-14 | s 11(2); s 14(4), (6) | tested when the arrangement is made | X-24 |
| FORK-15 | s 15 | s 15 does not cover acting arrangements | U-20 |
| FORK-16 | s 14(1) | process breaches do not make the appointment non-compliant | U-25 |

FORK-05, FORK-12 and FORK-13 decide only the timing or existence of duties that carry no consequence (U-25). Choosing between their readings changes no outcome.

---

## 5. Probe record

Each of the 13 categories was run over all four Parts on 2 October 2026 (`registers/probe-record.json`). A probe that found nothing is still a result.

| Category | Candidates |
|---|---|
| D Definition | D-11, D-12 |
| R Reference | R-21 |
| L Logic | L-04, L-07, L-18 |
| T Time | T-19 |
| U Uncertainty | U-06, U-08, U-09, U-10, U-16, U-17, U-20, U-22, U-23, U-25 |
| P Power | P-03, P-05, P-27 |
| E Enforcement | none as primary category (see U-25, P-03) |
| M Amendment | none: the Bill amends nothing, and no consequential amendment or transitional provision was found missing |
| I Interaction | I-26 |
| X Extrinsic | X-01, X-02, X-24 |
| W Workability | none demonstrated as primary category (see L-04, P-27) |
| F Form | F-14, F-15 |
| S Style | S-13, S-28, S-29, S-30 |

**Two limits on the probe:**

- **No `l4 verify`.** The installed l4 has no `verify` command. Step 1 of the Logic procedure was replaced by `l4 check` on every module (all clean), by enumerating each decision's conditions by hand, and by running the console checker (it reported nothing).
- **Style paragraph numbers.** The Drafting Direction paragraph numbers cited come from the numbered paragraphs of the pinned Word files, because the text conversions drop them. The Drafting Manual has no paragraph numbers, so it is cited by heading.

---

## 6. Coverage and scope (as approved at 3H)

**Encoded:** the whole Bill, ss 1-16, one module per Part. The boundary modules cover Acts Interpretation Act time rules, the Members of Parliament (Staff) Act 1984 and Public Service Act 1999 s 39.

**Not encoded as rules:**

- the s 3 outline: read, and set against the operative words in category X;
- column 3 of the commencement table, the notes, the table of contents and the long title;
- the content of rules not yet made under s 16, and offices prescribed under s 7(2);
- s 10(4), s 12(6) and s 12(7), which have nothing to decide;
- the State and Territory staffing and legislature-membership laws, taken as facts;
- the Vienna Conventions, which the Bill does not cite.

---

## 7. Gates

| Step | Decision | By | Date |
|---|---|---|---|
| 0H Jurisdiction | Commonwealth reference set approved; Style runs against the pinned OPC documents | Michael Andrew Fairweather | 2 October 2026 |
| 3H Confirm | Pinned print and gathered set confirmed; scope approved | Michael Andrew Fairweather | 2 October 2026 |
| 6H Fidelity | Encoding certified; all 16 forks reviewed, reading A confirmed | Michael Andrew Fairweather | 2 October 2026 |
| 12H Release | Not yet signed | | |

The 6H signer is not the encoder, who was the agent. The 12H signer must confirm that the re-pin below is recent enough.

---

## 8. Re-pin (10A)

All 30 findings are stamped against the first reading print (Senate) of 7 September 2026, checked on 2 October 2026.

The agent running 10A could not reach the Bill's page (aph.gov.au refused scripted access). The orchestrating session then checked it in a browser on 2 October 2026: the Bill is still at **introduced and read a first time / second reading moved, 7 September 2026**; **no proposed amendments have been circulated**; there are no schedules of amendments and no committee referral. The first reading print is current.

---

## 9. What the reference set knowingly lacks

These gaps were recorded at 0H and 3H:

- Scrutiny of Bills comment and any Senate committee referral or report (aph.gov.au refuses automated access).
- The text of the Transparent and Quality Public Appointments Bill 2026 (Scamps).
- Members of Parliament (Staff) Act compilations before 2023. U-16 turns on these in part. They were not fetched, so the finding is left open on that point.
- DFAT material on head-of-mission appointment practice.
- State and Territory staffing and legislature-membership laws, and the Vienna Conventions.
- The remaining OPC Drafting Directions, the Scrutiny committees' guidelines and the Legislation Rules 2016.

Found at 7A:

- **The second reading speech says nothing.** The Hansard held for 7 September 2026 records that Senator Payman sought leave to continue her remarks and the debate was adjourned (p. 60). So there is no substantive speech to set against the Bill.
- **Nothing outside the sets answered a finding.** Every challenge was answered, or left unanswered, from the 0H and 3H sets.

---

## 10. Known limitations of this encoding

These are limitations of our work, not findings about the law:

- **State and Territory facts.** Membership and State or Territory staff employment are taken as facts. So is whether a party was registered, and whether a position "corresponds" under s 8(2)(c).
- **Earlier MOP(S) Act employment.** Employment under the MOP(S) Act is tested only against the Act as it now stands (ENCODING-NOTES E-08).
- **No appointer in the L4.** The appointing and terminating acts, and their maker, are inputs; the Bill names none (P-03). The console gives these acts to "the appointing authority".
- **No weekday in the console.** The console engine has no day of the week, so it does not carry a last day falling on a weekend or holiday forward (Acts Interpretation Act s 36(2)). The L4 does (E-20).
- **List contents summarised in the console.** The console records a candidate list as numbers, not as people (E-24), and offices are a fixed list (E-23).
- **Revocation and member vacancies not encoded.** Neither the L4 nor the certified scheme modelled revocation of a Committee or a vacancy in its membership. The console's "revoke" act and its rule were added at 8A to demonstrate P-05. They are not part of what 6H certified.
- **Boundary modules held twice.** The boundary modules are kept in two byte-identical copies, because the installed l4 cannot import from a subfolder (E-01).
- **Parliamentary material not cleared for publication.** The Bill, the EM and the Hansard are held for internal analysis only. They must not be bundled into a published console without clearance at 12H.
