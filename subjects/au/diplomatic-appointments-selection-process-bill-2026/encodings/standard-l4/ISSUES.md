# Issues found in the Diplomatic Appointments (Selection Process) Bill 2026 (Cth)

Bill as introduced in the Senate (Senator Payman), 26S2721. Text: `../../sources/26S2721.txt`.

These are the problems that turned up while encoding the Bill in L4. The numbers match the `ISSUE n` comments in the `.l4` modules. Where a test in `tests.l4` pins the behaviour down, it is named. Those tests **pass**, because the encoding does what the Bill says, even where the result is a problem.

Severity:
- **High**: the Bill does not do what its outline says it does, or a safeguard can be got around.
- **Medium**: an ambiguity that changes the answer in realistic cases.
- **Low**: drafting.

| # | Severity | Provision | In one line |
|---|---|---|---|
| 1 | High | s 3, s 9(2) | The outline says a recommended person "must be appointed". No operative provision says so. |
| 2 | High | s 9(2), s 10(2)–(3) | A Committee can recommend someone who was never on the Minister's list, which gets around every limit in s 10(2). |
| 3 | High | s 9(3)(a)–(b), s 10(6) | Section 9(3) counts Committees from earlier vacancies: once a recommendation has ever been made, the route is closed for good, and old referrals can open it with no new Committee. |
| 4 | Medium | s 8(1), (2)(a) | "Within the last 10 years" has no reference point, so a person's status can change between the list and the appointment. |
| 5 | Medium | s 14(1), (3), (4), (6) | No one is named as making appointments or terminating them, and "as soon as practicable" sets no deadline. |
| 6 | Low | s 6, s 8(2)(b)(i) | "Minister" is defined as one particular Minister, then used in s 8(2)(b)(i) in its general sense. |
| 7 | Medium | s 8(2)(b) | Unclear whether the employer must have held the listed position at the time, and whether electorate staff count. "Shadow Minister" is undefined. |
| 8 | Medium | s 8(2)(c) | "Employed under a law of a State or Territory" and "equivalent or corresponds" are open-textured. |
| 9 | Low | s 8 | "Member" has no start or end point. |
| 10 | Medium | s 8(2)(d) | No time is fixed for "registered". State-registered parties are left out, and "officer" is undefined. |
| 11 | High | s 10(1), (3), (5), s 12(8), s 13(2) | A Committee that gets no list, or gives no notice, or loses a member, is never dissolved. That blocks every later Committee. |
| 12 | Medium | s 10(3), s 13(3) | "Agrees on a candidate" against majority voting, and "majority of the votes of the members". |
| 13 | Low | s 10(2)(b)–(c) | "May only propose 1" and "may only propose up to 2" are worded differently, and both are cast as permissions. |
| 14 | High | s 11 | Acting arrangements have no time limit, so an office can be filled indefinitely without any Committee. "Chargé d'affaires" is the wrong term for some of the offices. |
| 15 | Medium | s 9(4)–(5) | "Because the Minister is satisfied" is unclear when both of (c)(i) and (c)(ii) hold. Failing to table has no consequence. |
| 16 | Medium | s 14(1) | "In accordance with this Act" may or may not cover the s 10, 12 and 13 procedure. |
| 17 | Medium | s 15 | "The term of the appointment" and when it "starts" are undefined. Appointments made before commencement escape entirely. |
| 18 | Medium | s 15, s 11, s 14(4)–(6) | Section 15 speaks only of appointments, so it is unclear when the acting-arrangement rules start. |
| 19 | Low | s 6 | "Secretary" is defined and never used, and the definitions are out of alphabetical order. |
| 20 | Low | s 14(7), s 15, s 10(1) | Typographical errors. |
| 21 | Medium | s 9(3)(c)(i) | The Minister's subjective satisfaction replaces the objective test that applies everywhere else. |
| 22 | Medium | s 12 | Committee members face no independence or eligibility requirements. |
| 23 | Low | s 10(1), s 12(1), (4) | The 7-day clock runs from establishing the Committee, which can happen before it has any members. |

---

## 1. The outline promises a duty to appoint that the Bill does not contain (High)

Section 3 says that "any person so recommended by the Selection Committee **must be appointed**". No operative provision says that:
- s 9(1) is a restriction: a person "may be appointed ... **only if**";
- s 9(2) only makes a recommendation one of the two ways through it;
- s 10(3) and s 14 impose no duty on anyone to act on a recommendation.

As drafted, the Minister can sit on a recommendation, or establish another Committee. Once a recommendation has been made, the s 9(3) route is closed for that vacancy, because s 9(3)(a) requires that no recommendation "has been made" (and see issue 3). The vacancy then stays empty until a later Committee recommends someone acceptable. In the meantime it can be filled by an acting arrangement (issue 14).

Section 3 is a simplified outline and is not operative, so the outline is misleading rather than controlling. If a duty is intended, it needs an operative provision: who must appoint, and by when. Test: the `ISSUE 1` assertion in `tests.l4` § `s 9 — Appointments`.

## 2. A Committee may recommend someone who was not on the list (High)

Section 10(1)–(2) controls the Minister's list closely: 2 to 10 names, no disqualifying affiliations, a cap on significant affiliations, and reasons for each one. But:
- s 10(3)(a) lets the Committee recommend "**a** candidate", not "a proposed candidate";
- s 10(4) lets it seek input "from such persons as the Selection Committee determines";
- s 9(2) is satisfied by any recommendation of "the person's appointment".

Nothing confines the recommendation to the list. A Committee can therefore recommend a person with a significant political affiliation who is not on the list, even where the list's one significant slot is already used, and s 9(2) is satisfied. Only a broad reading of s 14(1) ("in accordance with this Act", issue 16) might catch it, and only after the appointment, with the appointment remaining valid (s 14(2)).

Tests: `Committee 1 recommends Drew, who is not on its list`. The s 9 route is `s 9(2)`, and only `s 14(1) — broad reading` returns FALSE.

## 3. Section 9(3) is not confined to the current vacancy (High)

Section 9(3)(a) requires that "no recommendation for an appointment to the office **has been made** by a Selection Committee established for the purpose of making such a recommendation". Section 9(3)(b) requires that "at least two such Selection Committees have ... referred the matter back". Neither is tied to the vacancy now being filled. Section 10(7) makes an old recommendation "of no effect" after an appointment, but it does not unmake the fact that a recommendation "has been made", and it says nothing about referrals. Section 10(6) has the same gap ("that particular appointment" is not defined).

Read literally, the Bill misfires in both directions:
- **Too strict.** Once any vacancy in an office has been filled on a recommendation, s 9(3)(a) can never be met for that office again. Test: `the second vacancy, after an earlier recommended appointment`. The literal reading gives no s 9(3) route; the vacancy-scoped reading gives one.
- **Too loose.** If an earlier vacancy was filled under s 9(3) after two referrals, those referrals still count. A later vacancy can then be filled under s 9(3)(c)(i) with **no Committee established for it at all**. Test: `the second vacancy, with no Committee of its own`.

The outline (s 3) says "Selection Committees established for making a recommendation in relation to **the same appointment**", which supports the vacancy-scoped reading. The operative text needs to say it. The encoding runs the literal reading and keeps the vacancy-scoped one beside it (`... vacancy-scoped reading`).

## 4. "Within the last 10 years": measured from when? (Medium)

Section 8(1) and s 8(2)(a) use "the last 10 years" with no reference point. The Bill tests affiliation at three different moments:
- when the list is given (s 10(2));
- when the appointment is made (s 9(1)(a), s 9(3)(c));
- when an acting arrangement is made or is running (s 11(2)).

A person's status changes as time passes. A former MP is "disqualifying" for 10 years and "significant" from then on. So a candidate lawfully left off a list can become appointable before the appointment, and the other way round. The Bill also does not say whether the boundary day is inside the window.

The encoding measures back from the day of each step, and includes the day exactly 10 years earlier (an anniversary on 29 February is kept as 29 February). Tests: `Ellis` and `Finley` (the boundary), and `Casey` changing category on 2029-03-24.

Two related points:
- s 8(2)(b)–(d) have no time limit at all. Ministerial staff work from 40 years ago still counts (test: `Drew` in 2068).
- The ss 8(1) and 8(2)(a) windows dovetail: every past member is one or the other, and the tests confirm there is no gap.

## 5. No one is named as appointing or terminating; no deadline to terminate (Medium)

- Section 14(1) ("An appointment ... must not be made") and s 14(3) ("an appointment must be terminated") are passive. Heads of mission are appointed by the Governor-General, or under the executive power, not by "the Minister" as defined. The Bill never says who makes the appointment, or who must terminate it.
- Section 14(4) and (6) have the same problem for acting arrangements.
- "As soon as practicable after the Minister becomes aware" sets no time and is triggered by the Minister's own awareness. In the encoding the s 14(3) duty has no deadline. A year's delay is not, by the clock alone, a breach (trace in `tests.l4`).
- Because s 14(2) and (5) preserve validity, the only consequence of non-compliance is a duty with no named bearer and no deadline.

## 6. "Minister" in s 8(2)(b)(i) clashes with the s 6 definition (Low)

Section 6 defines "Minister" as "the Minister administering the Diplomatic and Consular Missions Act 1978". Section 8(2)(b)(i) then says "a Minister (including the Prime Minister)", which only makes sense in the ordinary sense of any Minister of State. The indefinite article and the context probably displace the definition, but the Bill should say "a Minister of State" or carve the paragraph out of the definition. The same applies to "a shadow Minister" in (vi).

## 7. Section 8(2)(b): which staff, and when? (Medium)

"Employed under the Members of Parliament (Staff) Act 1984 as a member of the staff of a person occupying any of the following positions" leaves three questions open:
- **Timing.** Must the employer have held the listed position **during** the employment? For example, someone who worked for a backbencher who later became a Minister. The encoding takes the position the employer held during the engagement.
- **Which staff.** A Minister's electorate officers are employed under the MOP(S) Act in the Minister's capacity as a member, not as a Minister. Read literally, they are still staff "of a person occupying" the position of Minister.
- **Undefined positions.** "Shadow Minister" (and shadow assistant ministers) has no statutory definition. Whether Assistant Ministers and Parliamentary Secretaries are "a Minister" is also unclear.

## 8. Section 8(2)(c): State and Territory staff (Medium)

- Not every State or Territory employs political staff "under a law". Some use executive arrangements or common-law contracts. Such staff fall outside (c) entirely. Test: `Morgan` has no significant affiliation; `Logan` does.
- "Equivalent or corresponds to a position mentioned in ... (b)(i) to (vi)" cannot be applied mechanically. Queensland, the ACT and the NT have unicameral legislatures, so there is no "Leader of the Opposition in the Senate" to correspond to.
- The encoding takes both limbs as facts supplied by the caller.

## 9. When is a person a "member"? (Low)

Section 8 turns on being "a member of the Parliament of the Commonwealth, the Parliament of a State or the legislature of a Territory". It does not say whether membership starts at the election, the return of the writ, the start of the term or the oath, or when it ends. Senators-elect waiting for their term to start are the obvious case. The encoding takes membership dates as input. A membership that has not yet begun counts for nothing (test: `Harper`).

## 10. Section 8(2)(d): registered when, and which parties? (Medium)

- **Timing.** "A registered political party (within the meaning of the Commonwealth Electoral Act 1918)": registered at the time of the role, or now? A party since deregistered, or not yet registered, is unclear.
- **State parties.** A party registered only under State law is outside (d) (test: `Taylor`).
- **"Officer".** Undefined. It may reach unpaid branch office-bearers.
- Mere membership of a party is not caught (test: `Sage`). That looks deliberate, but it is a large gap beside (b) and (c).

## 11. A Committee can stall the process indefinitely (High)

- A Committee is dissolved only "after giving the Minister written notice as required by subsection (3)" (s 10(5)).
- The 2-month clock in s 10(3) runs from "receiving the list". If the Minister gives no list (s 10(1)), the Committee's clock never starts.
- Neither the 7-day nor the 2-month deadline has a consequence.
- A quorum is "all 3 members" (s 13(2)). If a member resigns, dies or is conflicted out, no decision can be made (test: a meeting with 2 present is not quorate).

In each case the Committee is never dissolved, and s 12(8) ("No more than one Selection Committee for an appointment ... at any one time") then stops the Minister establishing another. Test: `Committee 1` with no notice blocks a new Committee a year later.

Rules under s 12(6)(c), (g) and (h) could fill the gap, but the Bill does not require them. The default of no rules leaves a deadlock, and with it, by s 9(1)(b), no lawful appointment at all.

## 12. "Agrees on a candidate" and "a majority of the votes of the members" (Medium)

- Section 10(3)(a) speaks of the Committee "agree[ing] on a candidate", and the outline speaks of Committees that "fail to agree". Section 13(3) decides questions "by a majority of the votes of the members". It is unclear whether a 2–1 vote is "agreement" or whether consensus is required.
- "A majority of the votes of the members" may mean a majority of all 3 members (2 votes), or of the votes cast. The difference shows when members abstain. The encoding takes 2 of 3; under the other reading, a single vote with two abstentions would carry (test: the `ISSUE 12` meeting refers the matter back).
- A three-way split has no majority, so "otherwise" in s 10(3)(b) applies. The encoding follows that.

## 13. "May only propose 1" and "may only propose up to 2" (Low)

Paragraphs (b) and (c) of s 10(2) express the same kind of ceiling in two forms. "May only propose 1" could be misread as requiring exactly one. Both are also framed as permissions ("may only"), while (a) and (d) are duties ("must not", "must"). The encoding reads both as ceilings: at most 1 for a list of 2–4 (including the 2-or-3 list under s 10(6)), and at most 2 for a list of 5–10.

## 14. Acting arrangements bypass the selection process; "chargé d'affaires" (High)

Section 11 sets an eligibility bar for an acting appointee, stricter than s 9 (no significant affiliation either), but:
- it puts no limit on duration;
- it requires no Committee;
- it does not require that a selection process be under way.

An office can therefore be filled indefinitely by an acting arrangement, with no Selection Committee ever established. That defeats Parts 2–3 for any candidate without an affiliation the Government prefers to keep out of the Committee process.

Separately, "chargé d'affaires" is a term of diplomatic law (chargé d'affaires ad interim, Vienna Convention on Diplomatic Relations art 19) for the acting head of a diplomatic mission. It does not fit the acting head of a consular post (s 7(1)(b), Consuls-General) or a permanent mission to an international organisation (s 7(1)(k), (o)). It is used here as a defined label, which is harmless, but confusing.

## 15. Tabling under s 9(4)–(5) (Medium)

- **Which ground.** The duty arises where the person is appointed "because the Minister is satisfied in accordance with subparagraph (3)(c)(i)". If both Houses have also approved the appointment ((c)(ii)), it is unclear whether the duty still applies. The encoding reports route (c)(i) and the duty.
- **No consequence.** Failure to table has none. The appointment is made before the duty arises, so it is hard to see how a later failure makes the appointment one not made "in accordance with this Act" (s 14(1)).
- **Two clocks.** "5 sitting days of that House" runs separately for each House. The encoding models one duty per House, joined (traces in `tests.l4`).

## 16. What does "in accordance with this Act" cover? (Medium)

Section 14(1) prohibits an appointment made "otherwise than in accordance with this Act", and s 14(3) attaches the duty to terminate to that. The Bill does not say whether a failure in the procedure behind a s 9(2) recommendation makes the appointment non-compliant. Such failures include:
- a list that breaches s 10(2);
- a list given late (s 10(1));
- a Committee of the wrong size (s 12(3));
- a decision not made at a quorate meeting (s 13);
- a late notice (s 10(3));
- a recommended person not on the list (issue 2).

The narrow reading (s 9 only) is operative in the encoding, and `s 14(1) — broad reading` is encoded beside it. The difference decides whether the appointee must be terminated.

## 17. Section 15: "the term of the appointment" (Medium)

- **No defined term.** The Act applies only "if the term of the appointment starts at least 12 months after" commencement. Head-of-mission appointments are not made for a statutory term. It is unclear whether the "term" starts on appointment, on arrival or on presentation of credentials.
- **Pre-commencement appointments escape.** The Act applies only to appointments "made on or after the commencement". An appointment made the day before commencement, for a term starting years later, is outside the Act altogether (test).
- **The first year is open.** Appointments made after commencement whose terms start within 12 months are also outside the Act. That is presumably a deliberate transition, but it is a 12-month window in which any appointment may be made.

## 18. Does s 15 limit the acting-arrangement rules? (Medium)

Section 15 says the Act applies "in relation [to] an appointment" meeting its conditions. Acting arrangements (s 11, s 14(4)–(6)) are not appointments, so s 15 seems not to reach them. They would then be regulated from commencement, including arrangements already in place, while substantive appointments wait at least 12 months. The encoding applies s 15 to appointments only.

## 19. Unused definition; ordering (Low)

"Secretary" is defined in s 6 and never used. The definitions are also out of alphabetical order: "rules" comes after "significant political affiliation".

## 20. Typographical errors (Low)

- s 15: "This Act applies in relation an appointment": "to" is missing.
- s 14(7): "Nothing in subsections (3) and (6) limit": should be "limits".
- s 10(1): "within 7 days **of** establishing": the usual Commonwealth form is "after". "Of" is ambiguous about whether the day of establishment counts. The encoding follows Acts Interpretation Act 1901 s 36(1).

## 21. The Minister's satisfaction replaces the objective test (Medium)

Everywhere else, affiliation is an objective fact (s 8): in s 9(1)(a), s 10(2) and s 11(2). Under s 9(3)(c)(i), though, the test is that the Minister "is satisfied the person does not have a significant political affiliation". A person who in fact has one can be appointed if the Minister is so satisfied. The only check is the tabled statement of reasons, which has no consequence (issue 15). The encoding takes the Minister's satisfaction as an input.

## 22. No independence requirement for Committee members (Medium)

Section 12 requires 3 members with "an appropriate balance of expertise" (s 12(5)). It imposes no eligibility or independence requirement. Members may themselves have disqualifying or significant political affiliations, may be departmental officers answerable to the Minister, and may even be candidates. Disclosure of interests is left to optional rules (s 12(6)(f)).

## 23. The 7-day clock can run before the Committee has members (Low)

The list is due "within 7 days of establishing" the Committee (s 10(1)). But establishing the Committee (s 12(1)) and appointing its members (s 12(4)) are separate instruments. The list can fall due, and be given, to a Committee with no members.
