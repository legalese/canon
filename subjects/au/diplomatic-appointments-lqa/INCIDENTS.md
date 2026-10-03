# Incidents: Diplomatic Appointments (Selection Process) Bill 2026 (Cth)

LQA steps 7A to 10A, 2 October 2026, against the first reading (Senate), introduced 7 September 2026 (file 26S2721). The machine-readable register is `incidents.json`; this file is its prose, one section per finding, in register order. Quotations from parliamentary material are cut to a few words; the full words are in `incidents.json` and are checked against the pinned copies.

Every finding was challenged on 2 October 2026 and re-pinned the same day. The re-pin could confirm only that no later print is held: aph.gov.au and ParlInfo refused scripted access (HTTP 403) and a web search found nothing on the Bill, so whether amendments have been circulated or a further print exists is not known (see REPORT.md, Re-pin).

## X-01: The simplified outline says a recommended person must be appointed; the operative words only permit it

- **Provision:** s 3; s 9(1), (2)
- **Category:** Extrinsic (also Style, Uncertainty)
- **Fork:** FORK-09 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity medium
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 3 says any person a Selection Committee recommends must be appointed, and EM para 18 says the Minister must accept the recommendation and appoint. Section 9(1)-(2) says only that a person may be appointed if a Committee recommends them: nothing obliges anyone to appoint the recommended person, or stops the appointer leaving the office to an acting arrangement, establishing further Committees until one recommends someone acceptable, or waiting. Acts Interpretation Act s 13 makes the outline part of the Act, and OPC Drafting Direction 1.3A paras 29-30 require every statement in an outline to have a substantive provision under it. The outline's 'This requirement applies in all cases' is also wider than the Act, which excludes acting arrangements (s 11(3)) and appointments within s 15.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT someone must appoint the person a Committee recommended for Japan appointment`
- assert, `cases.l4`: `#ASSERT someone must appoint the person a Committee recommended, reading B, for Japan appointment`
- quote, the Bill, s 3, third paragraph: "any person so recommended by the Selection Committee must be appointed"
- quote, the Bill, s 9(1): "A person may be appointed to a designated diplomatic office only if"
- quote, the explanatory memorandum, para 18: "The Minister must accept this recommendation and appoint the candidate that the ..."
- quote, OPC Drafting Direction 1.3A, para 30: "Everything in a simplified outline must have a substantive provision underlying it"
- quote, OPC Drafting Direction 3.4, para 27: "must be exercised in accordance with the recommendation or nomination"
- scenario in the console: "A Committee recommends Ellis, who is appointed Ambassador to Japan"
- simulation: seed 2, 365 days, default parameters

**Challenge.** Acts Interpretation Act s 13 (material from the first section to the end of the Act is part of the Act) makes s 3 part of the Act, so the conflict is within the Act itself. Section 15AB allows the EM to be used to confirm or determine meaning, but EM para 18 cannot supply a duty the operative words do not contain, and a court would be expected to prefer the operative provision over a simplified outline (OPC DD 1.3A para 34: an outline 'may be incomplete'). The second reading speech holds nothing on the point: Senator Payman sought leave to continue her remarks and the debate was adjourned (Senate Hansard, 7 September 2026, p. 60). Not answered.

**Suggested repair.** Decide the policy. If a recommended person is to be appointed, say so in an operative provision with a named actor (for example, the Minister must, within a stated period, advise the Governor-General to appoint the recommended person, unless the person declines or is no longer eligible), and say what happens if that does not occur. If not, amend s 3 and EM para 18 so they say only that a recommendation makes the appointment permissible.

## X-02: The outline states an objective bar; s 9(3)(c)(i) turns on the Minister's satisfaction

- **Provision:** s 3; s 9(3)(c)(i)
- **Category:** Extrinsic (also Uncertainty)
- **Fork:** FORK-10 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity medium
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** After two referrals, s 3 says 'the person appointed must not have a significant political affiliation' unless Parliament approves. Section 9(3)(c)(i) is met if 'the Minister is satisfied' the person has none. On the reading taken (FORK-10 A), a person who in fact has an affiliation (for example a former electorate officer to a Minister, FORK-02 A) may be appointed without either House on a satisfaction the Minister forms, and the appointment complies with s 14(1), so s 14(3) never requires it to be terminated. Only the s 9(4) statement of reasons, which carries no consequence, stands between the two.

**Evidence.**

- assert, `cases.l4`: `#ASSERT section 9(1) permits India appointment of Finley`
- assert, `cases.l4`: `#ASSERT NOT subparagraph 9(3)(c)(i) is met, reading B of FORK-10, for India appointment of Finley`
- quote, the Bill, s 3, fourth paragraph: "the person appointed must not have a significant political affiliation"
- quote, the Bill, s 9(3)(c)(i): "the Minister is satisfied the person does not have a significant political ..."
- quote, the explanatory memorandum, para 19: "Where the Minister is satisfied that the candidate does have a significant ..."
- scenario in the console: "After two referrals, the Minister is satisfied and appoints Finley, a Minister's electorate officer"

**Challenge.** A satisfaction formula is ordinarily read as a jurisdictional fact of opinion, reviewable only for legal unreasonableness, so FORK-10 A is the likely judicial reading; that confirms the gap with s 3 rather than closing it. Acts Interpretation Act s 13 makes s 3 part of the Act; s 15AB does not let EM paras 14 and 19 (which are themselves framed around what the Minister is satisfied of) displace the operative words. Not answered.

**Suggested repair.** If the bar is meant to be objective, make s 9(3)(c)(i) read 'the person does not have a significant political affiliation' (and keep the statement of reasons). If satisfaction is intended, amend s 3 to say so.

## P-03: No one is named to appoint, to terminate, or to make or end an acting arrangement

- **Provision:** ss 9(1), 11, 14(1)-(7)
- **Category:** Power (also Reference, Enforcement)
- **Status:** OPEN, severity medium
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** The Bill conditions appointments (s 9(1), 'may be appointed') and acting arrangements (s 14(4)) without naming who makes them, and requires termination (s 14(3), (6)) 'as soon as practicable after the Minister becomes aware' without naming who terminates or under what power. Heads of mission are appointed by the Governor-General (Public Service Act 1999 s 39(1)), acting heads are typically arranged within the Department, and EM para 28 says the Minister makes acting appointments. The duty is triggered by one office-holder's knowledge but owed, if by anyone, by another; s 14(7) assumes 'a power of the Commonwealth' to terminate that the Bill does not identify.

**Evidence.**

- quote, the Bill, s 14(3): "However, an appointment must be terminated as soon as practicable after the ..."
- quote, the Bill, s 14(7): "limit a power of the Commonwealth to terminate an appointment or arrangement ..."
- quote, the explanatory memorandum, para 28: "An acting appointment can be made without a Selection Committee or reference ..."
- quote, OPC Drafting Direction 3.4, para 2: "so as to make it clear who is to form the opinion, ..."
- scenario in the console: "A sitting MP is recommended and appointed, then the appointment is terminated"
- scenario in the console: "A Minister's electorate officer is made chargé d'affaires in London"
- simulation: seed 2, 365 days, default parameters

**Challenge.** Section 5 binds the Crown in right of the Commonwealth, so the conditions in s 9 bind whoever appoints, including the Governor-General acting on advice (Constitution ss 61, 64, 67). Acts Interpretation Act s 33(4) (a power to appoint includes a power to remove) does not apply because the Bill confers no power to appoint. Section 33A (acting appointments) likewise depends on a power to appoint conferred by an Act. A court would probably hold that the duty in s 14(3) falls on whoever holds the appointing power and that the Minister must advise termination, but that is construction, not text. Not answered.

**Suggested repair.** Name the actors: for example, 'the Minister must, as soon as practicable after becoming aware ..., advise the Governor-General to terminate the appointment', and 'the Minister must ensure that an arrangement ... is terminated'. Consider stating the power to terminate expressly.

## L-04: A Committee that cannot decide, or misses its 2 months, is never dissolved, and no other may be established

- **Provision:** s 10(3), (5); s 12(3), (4), (8); s 13(1), (2)
- **Category:** Logic (also Time, Workability)
- **Status:** OPEN, severity medium
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** A Committee is dissolved only 'after giving the Minister written notice as required by subsection (3)' (s 10(5)). It can decide, even to refer back, only at a meeting at which all 3 members are present (s 13(1), (2)). Members have no deadline to be appointed (s 12(4)), yet the 2 months run from receipt of the list (s 10(3)); the Bill has no provision for a member's vacancy, and resignation is left to rules (s 12(6)(g)). A Committee that misses the 2 months, or cannot muster all 3 members, therefore stays in existence, and s 12(8) bars any further Committee for the appointment. The process for that appointment can stall indefinitely, and with it s 9(2) and s 9(3) (which needs two referrals).

**Evidence.**

- assert, `lqa-evidence.l4`: `#ASSERT the Committee a Committee that never meets is in existence on (the day 2030 1 18)`
- assert, `lqa-evidence.l4`: `#ASSERT NOT section 12(8) allows a Committee to be established on (the day 2030 1 18) beside (LIST a Committee that never meets)`
- assert, `lqa-evidence.l4`: `#ASSERT NOT the Committee referred the matter back a two-member Committee`
- quote, the Bill, s 10(5): "The Selection Committee is dissolved after giving the Minister written notice as ..."
- quote, the Bill, s 13(2): "At a meeting of a Selection Committee, a quorum is constituted by ..."
- quote, the Bill, s 12(8): "No more than one Selection Committee for an appointment to a designated ..."
- scenario in the console: "The Japan Committee never meets, and the Minister cannot establish another"
- simulation: seed 2, 365 days, default parameters

**Challenge.** Acts Interpretation Act s 33(3) reads into s 12(1) a power to revoke the instrument establishing a Committee, and s 33(4) a power to remove and replace members, which offers a way out. But s 10(5) and s 12(6)(c) ('dissolution of Selection Committees (subject to subsection 10(5))') suggest the Bill means s 10(5) to be the way a Committee ends, which may show a contrary intention; OPC DD 3.4 para 17 warns against relying on s 33(3) without considering the instrument's nature. Even if revocation works, a revoked Committee counts neither as a recommendation nor as a referral, so the stall is relieved only by the device that P-05 describes. Answered only in part; severity kept at medium.

**Suggested repair.** Provide that a Committee that has not given its notice within the period is taken to have referred the matter back (or is dissolved), allow the Minister to fill a vacancy in the membership, and set a time for appointing members after establishment.

## P-05: The Minister may revoke a Committee before it reports, and the revoked Committee counts for nothing

- **Provision:** s 12(1), (8); s 9(3)(a), (b); Acts Interpretation Act 1901 s 33(3)
- **Category:** Power (also Logic)
- **Status:** OPEN, severity medium
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 12(1) establishes Committees 'by written instrument'. Acts Interpretation Act s 33(3) construes a power to make an instrument of an administrative character as including a power to revoke it. A Minister who expects a Committee to recommend someone unwelcome, or to refer back, can revoke it before it gives its notice; it is then neither a recommendation nor a referral, s 12(8) no longer stands in the way, and a new Committee (with a fresh list of up to 10 under s 10(1)) can be established. EM para 32 says s 12(8) exists to stop Committees being set up concurrently to raise the chance of the government's preferred candidate being selected; serial revocation achieves the same thing sequentially. The Bill does not exclude s 33(3) or say what a revoked Committee counts as.

**Evidence.**

- quote, the Bill, s 12(1): "The Minister may, by written instrument, establish a committee for the purpose ..."
- quote, the explanatory memorandum, para 32: "a number of Selection Committees could be set up concurrently to increase ..."
- quote, OPC Drafting Direction 3.4, para 17: "You should not rely on subsection 33(3) of the Acts Interpretation Act ..."
- scenario in the console: "The Minister revokes the Netherlands Committee before it reports and establishes another"

**Challenge.** Section 33(3) applies to instruments 'of a legislative or administrative character', which an instrument under s 12(1) is (s 12(7) says only that it is not a legislative instrument). A contrary intention might be found in s 10(5) and s 12(6)(c), but that is uncertain (see L-04). Judicial review for improper purpose might restrain a revocation made to defeat a recommendation, but that is not something the Bill provides. Not answered.

**Suggested repair.** Either exclude revocation (except on grounds stated, such as a member's death) or provide that a Committee whose establishing instrument is revoked before it gives notice is taken to have referred the matter back, and require the revocation and its reasons to be tabled.

## U-06: Do Committees for an earlier vacancy count towards s 9(3) and s 10(6)?

- **Provision:** s 9(3)(a), (b); s 10(6), (7)
- **Category:** Uncertainty (also Reference)
- **Fork:** FORK-04 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity low
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 9(3)(a) asks whether any recommendation for an appointment to the office 'has been made', and (b) whether two Committees have referred the matter back; s 10(6) speaks of 'that particular appointment'. None is confined to the current vacancy. Section 10(7) deals only with the effect of a recommendation after an appointment is made. On reading B, referrals for a vacancy filled years ago open s 9(3) for the next one, and a single past recommendation closes s 9(3)(a) for the office for good.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT paragraphs 9(3)(a) and (b) are met for Italy appointment`
- assert, `cases.l4`: `#ASSERT paragraphs 9(3)(a) and (b) are met, reading B of FORK-04, for Italy appointment`
- quote, the Bill, s 9(3)(a): "no recommendation for an appointment to the office has been made by ..."
- scenario in the console: "Italy: referrals for an earlier vacancy, then a new vacancy and a list of five"
- simulation: seed 2, 365 days, default parameters

**Challenge.** Section 10(7), its note ('historical recommendations cannot be relied on for subsequent appointments') and EM para 27 point strongly to reading A, and reading B produces results (a permanently closed s 9(3)(a)) a court would avoid. The words still do not say it, and the note does not reach referrals. Kept OPEN at low severity.

**Suggested repair.** In s 9(3)(a) and (b), and s 10(6), refer to Committees established for the appointment since the office was last filled (or 'for the current vacancy').

## L-07: Does the s 10(2)(b) cap apply to a list of 2 or 3 under s 10(6)?

- **Provision:** s 10(2)(b), (6)
- **Category:** Logic
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 10(6) modifies only s 10(1). The question was whether s 10(2)(b) (a list of 2 to 4 may propose only 1 candidate with a significant political affiliation) still governs a 2-or-3 list. It does, on its own terms: such a list is a list of between 2 and 4.

**Evidence.**

- assert, `lqa-evidence.l4`: `#ASSERT the list for India second Committee with two affiliated after India Committees has a permitted number of candidates`
- assert, `lqa-evidence.l4`: `#ASSERT NOT s 10(2)(b) and (c) are met by the list for India second Committee with two affiliated`
- quote, the Bill, s 10(6): "subsection (1) has effect in relation to the second or subsequent Committee"

**Challenge.** Answered by the text of s 10(2)(b). Answered by: s 10(2)(b): 'if the list proposes between 2 and 4 candidates (inclusive)' covers every list of 2 or 3 (bill-26S2721).

## U-08: Does a Committee 'agree on' a candidate by a 2-1 majority?

- **Provision:** s 10(3)(a); s 13(3)
- **Category:** Uncertainty
- **Fork:** FORK-08 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity low-medium
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 10(3)(a) applies 'if the Selection Committee agrees on a candidate'; otherwise it must refer the matter back (s 10(3)(b)). Section 13(3) decides 'a question arising at a meeting' by majority. On the reading taken a 2-1 vote is agreement; on the ordinary meaning of 'agrees' it is not, and a split Committee must refer back, moving the appointment towards s 9(3).

**Evidence.**

- assert, `cases.l4`: `#ASSERT the Committee Japan Committee agrees on the candidate named "Alex"`
- assert, `cases.l4`: `#ASSERT NOT the Committee Japan Committee agrees, reading B of FORK-08, on the candidate named "Alex"`
- quote, the Bill, s 10(3)(a): "if the Selection Committee agrees on a candidate for the appointment"
- scenario in the console: "A Committee recommends Ellis, who is appointed Ambassador to Japan"
- simulation: seed 2, 365 days, default parameters

**Challenge.** Section 13(1) makes the s 10(3) decision a decision at a meeting, s 13(3) gives the rule for questions at meetings, and EM para 23 says at least two members must concur; together these make reading A likely. Nothing in the 0H or 3H set makes reading B untenable, and the outcome (recommend or refer) is the Bill's central decision. Kept OPEN, low-medium.

**Suggested repair.** In s 10(3)(a), say 'if a majority of the members of the Selection Committee agree on a candidate' (or require unanimity expressly).

## U-09: Is s 13(3) a majority of all members or of votes cast?

- **Provision:** s 13(3)
- **Category:** Uncertainty
- **Fork:** FORK-07 (reading A taken; confirmed at 6H)
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC, encode (writing the L4 or the scheme forced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** With abstentions, a majority of votes cast and a majority of the members' votes part. The words 'a majority of the votes of the members' (not 'of the members present and voting'), with the quorum of all 3, mean at least 2 of 3.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT the question was carried an abstaining Committee`
- assert, `cases.l4`: `#ASSERT the question was carried, reading B an abstaining Committee`
- quote, the Bill, s 13(3): "A question arising at a meeting of the Selection Committee is to ..."
- quote, the explanatory memorandum, para 33: "questions can only be resolved with two or more votes in favour ..."

**Challenge.** Answered by the text, confirmed by EM para 33 under Acts Interpretation Act s 15AB(1)(a). Answered by: s 13(3) ('of the members'), confirmed by EM para 33 (em-26S2721).

## U-10: From what day, and how, are 'the last 10 years' counted?

- **Provision:** s 8(1), (2)(a); s 10(2)
- **Category:** Uncertainty (also Time)
- **Fork:** FORK-01 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity low
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 8 does not say on what day 'the last 10 years' end. For s 9(1)(a) and s 11(2) the context points to the day of appointment or arrangement; for s 10(2) the list could be tested when given, when the Committee decides, or at appointment, and a candidate can cross the line in between. The Acts Interpretation Act defines a month (s 2G) but not a year, so whether a last day of membership exactly 10 years earlier is inside the period is open (FORK-01).

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT has a disqualifying political affiliation on Blair the test day`
- assert, `cases.l4`: `#ASSERT has a disqualifying political affiliation, reading B, on Blair the test day`
- quote, the Bill, s 8(1): "is, or has been at any time within the last 10 years, ..."
- scenario in the console: "Ten years pass for Blair, a former federal member"

**Challenge.** Acts Interpretation Act s 2G (months) and s 36 (calculating time) do not cover a period of years running back from an unstated day. The boundary affects one day; the unstated test day for s 10(2) matters more. Kept OPEN, low.

**Suggested repair.** Say 'within the 10 years ending on the day [the appointment is made / the list is given]' and, if precision matters, 'the period of 10 years ending at the end of that day'.

## D-11: A long-serving member has both a disqualifying and a significant affiliation

- **Provision:** s 8(1), (2)(a)
- **Category:** Definition
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** TST, test (a written case surfaced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 8(2)(a) ('has been, at any time other than within the last 10 years, a member') also catches a sitting member, or a recent former member, whose membership began more than 10 years ago, so such a person has both affiliations; EM para 12 describes (2)(a) as membership '10 years ago or longer'. Nothing turns on the overlap, because the disqualifying affiliation bars the person under ss 9(1)(a), 10(2)(a) and 11(2) wherever the significant one would matter.

**Evidence.**

- assert, `cases.l4`: `#ASSERT has a disqualifying political affiliation on Casey the test day`
- assert, `cases.l4`: `#ASSERT paragraph 8(2)(a) applies to Casey on the test day`
- quote, the explanatory memorandum, para 12: "10 years ago or longer"

**Challenge.** Answered by ss 9(1)(a), 10(2)(a) and 11(2), which give the disqualifying affiliation priority in every provision that reads the significant one. Answered by: ss 9(1)(a), 10(2)(a), 11(2) (bill-26S2721).

## D-12: 'Secretary' is defined and not used

- **Provision:** s 6
- **Category:** Definition (also Style)
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 6 defines 'Secretary'; no provision of the Bill uses it. Rules under s 16 may (for example on Committee procedure under s 12(6)), and expressions in a legislative instrument have the meaning they have in the enabling Act.

**Evidence.**

- quote, the Bill, s 6: "Secretary means the Secretary of the Department administered by the Minister."

**Challenge.** Answered by Legislation Act 2003 s 13(1)(b). OPC practice tolerates definitions provided for instruments under the Act. Answered by: Legislation Act 2003 s 13(1)(b): expressions used in an instrument have the same meaning as in the enabling legislation (cth-legislation-act-2003).

## S-13: Section 6 definitions are not in alphabetical order

- **Provision:** s 6
- **Category:** Style (also Form)
- **Status:** OPEN, severity low
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** 'rules' is listed last, after 'significant political affiliation'; it belongs before 'Secretary'. The OPC Drafting Manual says defined terms are listed in alphabetical order.

**Evidence.**

- quote, the Bill, s 6: "significant political affiliation: see subsection 8(2)."
- quote, the Bill, s 6, last definition: "rules means rules made under section 16."
- quote, the OPC Drafting Manual, Components of Bills, 'Definitions': "We list the defined terms in alphabetical order."

**Challenge.** No exception in the Drafting Manual or DD 1.5 applies.

**Suggested repair.** Move the definition of 'rules' to follow 'Minister'.

## F-14: 'Nothing in subsections (3) and (6) limit': the verb does not agree

- **Provision:** s 14(7)
- **Category:** Form
- **Status:** OPEN, severity low
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** 'Nothing' takes a singular verb.

**Evidence.**

- quote, the Bill, s 14(7): "Nothing in subsections (3) and (6) limit a power of the Commonwealth"

**Challenge.** A slip a court would read past; recorded at low severity.

**Suggested repair.** 'Nothing in subsection (3) or (6) limits a power of the Commonwealth ...'.

## F-15: 'applies in relation an appointment': a word is missing

- **Provision:** s 15
- **Category:** Form
- **Status:** OPEN, severity low
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** 'to' is missing after 'in relation'. EM para 3 quotes the clause with the same slip.

**Evidence.**

- quote, the Bill, s 15: "This Act applies in relation an appointment made on or after the ..."
- quote, the explanatory memorandum, para 3: "This Act applies in relation an appointment made on or after the ..."

**Challenge.** A slip a court would read past; recorded at low severity.

**Suggested repair.** 'This Act applies in relation to an appointment ...'.

## U-16: Whose staff count under s 8(2)(b), and under which version of the MOP(S) Act?

- **Provision:** s 8(2)(b); Members of Parliament (Staff) Act 1984 ss 3, 4, 11
- **Category:** Uncertainty (also Definition, Reference)
- **Fork:** FORK-02 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity medium
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 8(2)(b) speaks of employment under the MOP(S) Act 'as a member of the staff of a person occupying' a listed position. The MOP(S) Act employs people as electorate employees or personal employees (Ministerial or non-Ministerial) of a parliamentarian; it has no category matching the words. Whether a Minister's or shadow Minister's electorate officer is caught is open (FORK-02), and decides whether a large class of former staff need the s 10(2) reasons and caps. A 'shadow Minister' holds no office under the MOP(S) Act and can employ personal staff only under a s 4 determination. 'Is or has been employed under' the Act reaches employment under its earlier versions (former Parts III and IV), which the set does not hold (3H gap).

**Evidence.**

- assert, `cases.l4`: `#ASSERT has a significant political affiliation on Finley the test day`
- assert, `cases.l4`: `#ASSERT NOT has a significant political affiliation, reading B of FORK-02, on Finley the test day`
- quote, the Bill, s 8(2)(b): "employed under the Members of Parliament (Staff) Act 1984 as a member ..."
- quote, the explanatory memorandum, para 12: "The person has worked (or works) for a federal, state or territory ..."
- scenario in the console: "A Minister's electorate officer is made chargé d'affaires in London"
- simulation: seed 2, 365 days, default parameters

**Challenge.** MOP(S) Act s 3AA makes the parliamentarian the employing individual for electorate employees too, and EM para 12 ('worked ... for a ... minister or shadow minister') is consistent with reading A, so A is the likely reading. Still, the words leave a consequential choice open, and their fit with the pre-2023 Act cannot be checked from the set (the earlier compilations are a recorded 3H gap). Not answered.

**Suggested repair.** Use the MOP(S) Act's own terms: 'employed under the Members of Parliament (Staff) Act 1984 (as an electorate employee or a personal employee) by a person who, at the time, occupied any of the following positions', and say whether earlier versions of that Act are included.

## U-17: Party 'officer or employee' is undefined, and when must the party be registered?

- **Provision:** s 8(2)(d); Commonwealth Electoral Act 1918 s 4(1)
- **Category:** Uncertainty (also Definition)
- **Fork:** FORK-03 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity low-medium
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Neither the Bill nor the Commonwealth Electoral Act defines an 'officer' of a political party: a branch secretary, a delegate, a campaign volunteer with a title? The Bill also does not say whether the party must have been registered while the person held the role (FORK-03 A) or must be registered when the question is asked (B), so a party's later registration or deregistration can change a person's affiliation.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT has a significant political affiliation on Jordan the test day`
- assert, `cases.l4`: `#ASSERT has a significant political affiliation, reading B of FORK-03, on Jordan the test day`
- quote, the Bill, s 8(2)(d): "the person is or has been an officer or employee of a ..."
- scenario in the console: "Alex acts in London, then becomes a party officer"
- simulation: seed 2, 365 days, default parameters

**Challenge.** Commonwealth Electoral Act s 4(1) defines 'registered political party' (registered under Part XI) but not 'officer'. EM para 12 ('employed by or holds an office within') suggests holding any office in the party, which is wide. Not answered.

**Suggested repair.** Define 'officer' (for example, a person who holds an office under the party's constitution, or is a member of its executive at any level) and say 'a political party that was a registered political party ... at the time'.

## L-18: A chargé d'affaires is held to a stricter test than an appointee

- **Provision:** s 9(1); s 11(2)
- **Category:** Logic
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** A person with a significant (not disqualifying) affiliation may be appointed on a Committee's recommendation but may not act in the same office, even for a day. It looked like an inconsistency between ss 9 and 11.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT section 11(2) is met for Finley acts in Japan`
- quote, the Bill, s 11(2): "The chargé d’affaires must not have a disqualifying political affiliation or a ..."
- quote, the explanatory memorandum, para 28: "An acting appointment can be made without a Selection Committee or reference ..."

**Challenge.** Answered: deliberate, and explained in EM para 28 (acting arrangements skip the Committee and so exclude significant affiliations). Answered by: EM para 28 (em-26S2721).

## T-19: Section 15 turns on when 'the term of the appointment starts', which no law fixes

- **Provision:** s 15
- **Category:** Time (also Definition)
- **Status:** OPEN, severity low-medium
- **Found by:** ENC, encode (writing the L4 or the scheme forced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** The Act applies to an appointment made after commencement only 'if the term of the appointment starts at least 12 months after that commencement'. No statute gives heads of mission a term or says when it starts; the start is whatever the appointing instrument or practice says (arrival at post, presentation of credentials, a stated date). The same appointment of a sitting member, made in the first year, is outside the Act with a term from day 365 and inside it with a term from day 366, and the appointer chooses which.

**Evidence.**

- assert, `lqa-evidence.l4`: `#ASSERT the appointment Drew, term from 1 March 2028 was made in accordance with this Act, in the world`
- assert, `lqa-evidence.l4`: `#ASSERT NOT the appointment Drew, term from 2 March 2028 was made in accordance with this Act, in the world`
- quote, the Bill, s 15: "if the term of the appointment starts at least 12 months after ..."
- quote, the explanatory memorandum, para 35: "only affects appointments with a term which starts 12 months after the ..."
- scenario in the console: "In the first year, a sitting MP is appointed with a term starting at once"
- simulation: seed 2, 365 days, default parameters

**Challenge.** EM para 35 gives the purpose (time to prepare), which explains a delay but not the choice of the term start as the test. Nothing in the 0H or 3H set defines the term of a head of mission's appointment (Public Service Act s 39 does not). Not answered.

**Suggested repair.** Key s 15 to a day the Bill controls: 'an appointment made on or after [the day 12 months after commencement]', with a separate rule for appointments made earlier whose terms start later, if that is wanted.

## U-20: Does s 15's 12-month delay cover acting arrangements?

- **Provision:** s 15; s 11; s 14(4)
- **Category:** Uncertainty
- **Fork:** FORK-15 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity low
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 15 limits the Act's application to appointments whose terms start 12 months after commencement; it says nothing of acting arrangements. On the reading taken, s 11(2) and s 14(4)-(6) apply to every arrangement made from commencement, while appointments get a year's grace; on the other, 'appointment' in s 15 includes an acting appointment (the word EM para 28 uses).

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT the arrangement Finley acts in Japan in 2027 was made in accordance with this Act, in the world`
- assert, `cases.l4`: `#ASSERT the arrangement Finley acts in Japan in 2027 was made in accordance with this Act, reading B of FORK-15, in the world`
- scenario in the console: "A Minister's electorate officer is made chargé d'affaires in London"
- simulation: seed 2, 365 days, default parameters

**Challenge.** The Bill distinguishes 'appointment' from 'arrangement for a person to act' throughout s 14, which favours reading A; EM para 28's 'acting appointment' and EM para 35's purpose leave B arguable. Kept OPEN, low.

**Suggested repair.** State expressly whether s 15 applies to acting arrangements (for example, 'This Act applies in relation to an arrangement for a person to act ... made on or after the commencement of this section').

## R-21: 'Within 5 sitting days of that House': s 9(5) names no House

- **Provision:** s 9(4), (5)
- **Category:** Reference (also Time)
- **Status:** OPEN, severity low
- **Found by:** RD, read (a casual reader would catch it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 9(5) refers to 'that House', but no House is mentioned in s 9(5); the antecedent is 'each House' in s 9(4). The intended distributive reading (each House's own sitting days) is clear enough, but the usual Commonwealth form names it. Whether a sitting on the day of the appointment counts is a separate fork (FORK-13) with no consequence, since a late statement has none.

**Evidence.**

- quote, the Bill, s 9(5): "The statement must be tabled within 5 sitting days of that House ..."
- quote, the Bill, s 9(4): "the Minister must table in each House of the Parliament a statement ..."
- scenario in the console: "Two Committees refer the matter back; the Minister appoints Alex, satisfied"

**Challenge.** Acts Interpretation Act s 2M defines a sitting day of a House but does not supply the antecedent. A court would read past it; low severity.

**Suggested repair.** Combine s 9(4) and (5): '... must cause a statement ... to be tabled in each House of the Parliament within 5 sitting days of that House after the day the appointment is made'.

## U-22: Must the candidate a Committee recommends be on the Minister's list?

- **Provision:** s 10(1), (3)(a), (4)
- **Category:** Uncertainty
- **Fork:** FORK-06 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity low-medium
- **Found by:** ENC, encode (writing the L4 or the scheme forced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 10(3)(a) speaks of 'a candidate for the appointment', not a candidate on the list, and s 10(4) lets the Committee seek input from anyone. If a Committee may recommend someone off the list, the list's limits in s 10(2) (no disqualified candidate; the affiliated-candidate caps; reasons) are bypassed, and s 9(2) applies to that person.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT the Committee an off-list Committee agrees on the candidate named "Zed"`
- assert, `cases.l4`: `#ASSERT the Committee an off-list Committee agrees, reading B of FORK-06, on the candidate named "Zed"`
- quote, the Bill, s 10(4): "seek assistance, input or information from such persons as the Selection Committee ..."
- quote, the explanatory memorandum, para 23: "identify a candidate from that list which it recommends for appointment"
- scenario in the console: "A Committee recommends Kai, who was not on the Minister's list"

**Challenge.** EM para 23 and the purpose of s 10(2) favour reading A, but nothing in the operative words says so. Kept OPEN.

**Suggested repair.** In s 10(3)(a), say 'agrees on a candidate proposed in the list'.

## U-23: Must both Houses resolve before the appointment is made?

- **Provision:** s 9(1), (3)(c)(ii)
- **Category:** Uncertainty
- **Fork:** FORK-11 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity low
- **Found by:** ENC, encode (writing the L4 or the scheme forced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 9(3)(c)(ii) applies if 'both Houses of Parliament pass a resolution approving the person's appointment'. The present tense and 'approving' fit approval after the event as well as before. On the reading taken an appointment made before the second resolution is not in accordance with the Act, and later resolutions do not cure it.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT subparagraph 9(3)(c)(ii) is met for India appointment of Blair, approved late`
- assert, `cases.l4`: `#ASSERT subparagraph 9(3)(c)(ii) is met, reading B of FORK-11, for India appointment of Blair, approved late`
- quote, the Bill, s 9(3)(c)(ii): "both Houses of Parliament pass a resolution approving the person’s appointment to ..."
- scenario in the console: "Blair is appointed after two referrals, and both Houses approve afterwards"

**Challenge.** Section 9(1) is a condition on making the appointment, and EM para 19 says the Minister cannot make the appointment until both Houses have resolved: reading A is likely. Kept OPEN, low.

**Suggested repair.** 'both Houses of the Parliament have, before the appointment is made, passed a resolution approving ...'.

## X-24: The EM describes a continuing bar; ss 14(1) and (4) test only the making

- **Provision:** s 11(2); s 14(1), (3), (4), (6)
- **Category:** Extrinsic (also Uncertainty)
- **Fork:** FORK-14 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity medium
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** EM paras 11, 15 and 34 say a person with a disqualifying affiliation cannot hold or act in a designated office, and that when the Minister becomes aware that an office-holder or chargé has such an affiliation (or, for a chargé, a significant one) the appointment or arrangement must be terminated. The Bill's duties to terminate (s 14(3), (6)) are engaged only by a failure to comply with s 14(1) or (4), which speak of an appointment or arrangement being 'made'. A head of mission who later becomes a party officer, or a chargé who joins a Minister's staff while acting, is not caught on the reading taken (FORK-14 A).

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT the arrangement Morgan acts in Japan must be terminated under s 14(6), in the world`
- assert, `cases.l4`: `#ASSERT the arrangement Morgan acts in Japan must be terminated under s 14(6), reading B of FORK-14, in the world on (the day 2028 6 1)`
- quote, the Bill, s 14(4): "An arrangement for a person to act in a designated diplomatic office ..."
- quote, the explanatory memorandum, para 15: "when the Minister becomes aware that a person acting in a designated ..."
- quote, the explanatory memorandum, para 34: "a person with a disqualifying political affiliation cannot be appointed to, hold ..."
- scenario in the console: "Alex acts in London, then becomes a party officer"

**Challenge.** Acts Interpretation Act s 15AB allows the EM to be used where the meaning is ambiguous, and s 11(2) ('must not have', present tense) gives EM para 15 some purchase for acting arrangements; for appointments there is no textual hook at all. The words of s 14(1) and (4) ('must not be made') are not ambiguous on the point. Not answered.

**Suggested repair.** Decide the policy. If the bar is continuing, add: 'If a person appointed to, or acting in, a designated diplomatic office comes to have [an affiliation], the appointment or arrangement must be terminated as soon as practicable after the Minister becomes aware of it'; otherwise correct EM paras 11, 15 and 34.

## U-25: Breaches of the process in ss 9(4), 10 and 12 have no consequence, unless s 14(1) takes them in

- **Provision:** s 14(1), (3); s 9(4), (5); s 10(1)-(3); s 12(5), (8)
- **Category:** Uncertainty (also Enforcement)
- **Fork:** FORK-16 (reading A taken; confirmed at 6H)
- **Status:** OPEN, severity medium
- **Found by:** ENC, encode (writing the L4 or the scheme forced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** The Minister's duties to give the list within 7 days and within its caps and with reasons (s 10(1), (2)), to ensure a balanced membership (s 12(5)), and to table reasons (s 9(4), (5)), and the Committee's 2-month duty (s 10(3)), have no stated consequence. Whether an appointment that follows such a breach is made 'otherwise than in accordance with this Act' (s 14(1)), and so must be terminated, is open (FORK-16). On the reading taken, a recommendation from a Committee given a late, over-cap list supports a compliant appointment; on the other, the appointment must be terminated.

**Evidence.**

- assert, `cases.l4`: `#ASSERT the appointment Canada appointment was made in accordance with this Act, in the world`
- assert, `cases.l4`: `#ASSERT the appointment Canada appointment must be terminated under s 14(3), reading B of FORK-16, in the world`
- quote, the Bill, s 14(1): "An appointment to a designated diplomatic office must not be made otherwise ..."
- scenario in the console: "Canada: a late list over its cap, a recommendation, an appointment"
- simulation: seed 2, 365 days, default parameters

**Challenge.** No general offence or consequence provision in the 0H set (Crimes Act Part IA, Criminal Code, Regulatory Powers Act) attaches to these duties; s 16(2)(a) forbids rules creating offences or civil penalties. Judicial review could in principle set aside a recommendation, but the Bill says nothing. Not answered.

**Suggested repair.** Say whether a breach of ss 10 or 12 affects the recommendation or the appointment (for example, 'a failure to comply with section 10 or 12 does not affect the validity of a recommendation' or the reverse), and consider a consequence for failing to table under s 9(4).

## I-26: Valid under s 14(2), but unable to take effect under Public Service Act s 39(1)

- **Provision:** s 14(2); Public Service Act 1999 s 39
- **Category:** Interaction
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC, encode (writing the L4 or the scheme forced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Section 14(2) says a non-compliant appointment remains valid; Public Service Act s 39(1) says a Governor-General's appointment of a Head of Mission cannot take effect unless the person is an APS employee. A Committee may recommend someone outside the APS. The two looked as if they might conflict.

**Evidence.**

- assert, `cases.l4`: `#ASSERT NOT the Public Service Act 1999 s 39(1) lets take effect the appointment Japan appointment of Ellis`
- assert, `cases.l4`: `#ASSERT NOT the appointment Japan appointment of Ellis is invalid because of a failure to comply with s 14(1), in the world`
- quote, the Bill, s 14(2): "A failure to comply with subsection (1) does not affect the validity ..."

**Challenge.** Answered: they address different questions (validity under the Bill; taking effect under the Public Service Act), and s 39(2)(a) lets the Agency Minister direct that a non-APS appointee be engaged so the appointment can take effect. Answered by: Public Service Act 1999 s 39(1), (2)(a) (cth-psa-1999).

## P-27: Nothing requires a Committee ever to be established, and acting has no time limit

- **Provision:** s 11(1); s 12(1)
- **Category:** Power (also Workability)
- **Status:** OPEN, severity low
- **Found by:** ENC, encode (writing the L4 or the scheme forced it)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** The Minister 'may' establish a Committee (s 12(1)); nothing requires one to be established for a vacancy, or within any time. Section 11 lets a person act during a vacancy for any period. A designated office can therefore be run indefinitely by a chargé d'affaires chosen without the selection process (though without a political affiliation, s 11(2)). Found while working through the scheme's acts for category P: every step of the process is the Minister's option.

**Evidence.**

- quote, the Bill, s 12(1): "The Minister may, by written instrument, establish a committee"
- quote, the Bill, s 11(1)(a): "during a vacancy in the office"
- scenario in the console: "Alex acts in London, then becomes a party officer"
- simulation: seed 2, 365 days, default parameters

**Challenge.** EM para 28 says it is not feasible to leave a post vacant while a Committee deliberates, which explains acting arrangements but not an unlimited one. Nothing in the 0H or 3H set limits the period. Not answered; low because s 11(2) keeps political appointees out of the acting role.

**Suggested repair.** Require a Committee to be established within a stated period after a vacancy arises (or after an acting arrangement begins), or limit the period a person may act during a vacancy.

## S-28: Declaratory provisions say 'is to' instead of the present tense

- **Provision:** s 12(2), (3), (4); s 13(3)
- **Category:** Style
- **Status:** OPEN, severity low
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** 'is to be known as' (s 12(2)), 'is to consist of 3 members' (s 12(3)), 'are to be appointed by the Minister' (s 12(4)), 'is to be determined by a majority' (s 13(3)). The Plain English Manual para 84 says declarations of the law are expressed in the present tense ('The Authority consists of 10 members'). Section 12(4) would be clearer as a conferral: 'The Minister must appoint the members ... by written instrument'.

**Evidence.**

- quote, the Bill, s 12(3): "A Selection Committee is to consist of 3 members."
- quote, the Bill, s 12(4): "The members of a Selection Committee are to be appointed by the ..."
- quote, the OPC Plain English Manual, para 84: "These are neither imperatives nor statements about the future, they are declarations ..."
- quote, the OPC Plain English Manual, para 84, example: "The Authority consists of 10 members."

**Challenge.** Para 83 allows 'is to' as a gentler imperative, but these provisions declare the law rather than impose an obligation. Drafting Direction 2.1 gives the Plain English Manual the status of a Drafting Direction.

**Suggested repair.** '... is known as ...'; 'A Selection Committee consists of 3 members.'; 'The Minister must appoint the members ... by written instrument.'; 'A question ... is determined by a majority ...'.

## S-29: No simplified outlines for the Parts

- **Provision:** Parts 1-4
- **Category:** Style
- **Status:** OPEN, severity low
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** The Bill has a simplified outline for the Act (s 3) and none for any Part or Division. Drafting Direction 1.3A para 36 says that where an Act has simplified outlines there should also be outlines for at least one level of unit.

**Evidence.**

- quote, OPC Drafting Direction 1.3A, para 36: "In addition to the simplified outline for an Act, there should also ..."

**Challenge.** A short Bill may justify less, and DD 1.3A para 37 leaves the level to judgement; it does not dispense with the rule. Low.

**Suggested repair.** Either add short Part outlines or, given the Bill's length, rely on s 3 and record the departure; in either case correct s 3 (X-01, X-02).

## S-30: 'Minister' is defined by reference to another Act

- **Provision:** s 6
- **Category:** Style
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** CMP, compare (documents set side by side)
- **Print:** first reading (Senate), introduced 7 September 2026 (checked 2026-10-02)

**What, and why it matters.** Drafting Direction 2.2 para 126 says that for the Minister administering the provision, drafters should simply say 'the Minister' and rely on Acts Interpretation Act s 19. Section 6 instead defines the Minister as the Minister administering the Diplomatic and Consular Missions Act 1978.

**Evidence.**

- quote, the Bill, s 6: "Minister means the Minister administering the Diplomatic and Consular Missions Act 1978."
- quote, OPC Drafting Direction 2.2, para 126: "rely on sections 19 and 19A of the Acts Interpretation Act 1901 ..."
- quote, OPC Drafting Direction 2.2, para 129: "identify a key piece of legislation administered by that Minister, and to ..."

**Challenge.** Answered: the Bill means the Foreign Minister whichever Minister is allotted the new Act, and para 129 endorses identifying a Minister through a key Act that Minister administers (the AAO allots the DCMA to DFAT's Minister). The choice of the DCMA, an Act about false claims of diplomatic status, is apt enough. Answered by: OPC Drafting Direction 2.2 paras 128-129 (category 2 references) (cth-opc-dd-2-2).
