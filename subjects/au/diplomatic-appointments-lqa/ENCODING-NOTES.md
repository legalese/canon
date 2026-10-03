# Encoding notes: Diplomatic Appointments (Selection Process) Bill 2026

Step 4A and 5A, 2 October 2026, against the first reading print (Senate) of 7 September 2026 (file 26S2721).

Each entry is one question the encoding forced, one choice it made, or one thing that looked wrong. Each gives the provision and how it was noticed. None is a finding yet: 7A decides which become candidates. Where the text supports two readings that change an outcome, the entry points to the fork register (`registers/fork-register.json`, FORK-01 to FORK-16).

"How noticed" uses these terms: **encoding the L4**, **writing the scheme**, **a failing case** (an `#ASSERT` in `cases.l4` that failed before the cause was understood), and **the compiler**.

---

## Tooling and layout

**E-01. The boundary modules exist twice.** Reference register (REF-01, -09, -10, -16, -20, -22, -23, -31).
The register names `boundary/aia-time.l4`, `boundary/mops-1984.l4` and `boundary/psa-1999-s39.l4`. The installed l4 cannot import from another folder: it looks for `IMPORT` targets only beside the importing file. Each boundary module is therefore kept twice, byte-identical: in the subject folder, where the Part modules import it, and at the path the register names, where it checks on its own. `cmp aia-time.l4 boundary/aia-time.l4` (and the same for the other two) must print nothing. Both copies are in the 6H digest.
*How noticed: the compiler (a test import from a subfolder failed).*

**E-02. `NOT` takes in the whole expression after it.** All modules.
In the installed l4, `NOT a OR b` means `NOT (a OR b)`, and `NOT FALSE AND FALSE` is `TRUE`. Every `NOT` in the modules is now bracketed, `(NOT x)`. This is a tool behaviour, not a question about the law. It is recorded here because it could have hidden a misencoding: the first full run of `cases.l4` failed s 10(2)(d) on a list that complied.
*How noticed: a failing case.*

**E-03. Section 15 lacks a word.** s 15.
The print reads "This Act applies in relation an appointment made on or after ...". "to" is missing after "in relation". EM para 3 quotes the same words. The encoding reads it as "in relation to".
*How noticed: encoding the L4.*

## Who acts

**E-04. The Bill names no appointer, no terminator and no maker of acting arrangements.** ss 9(1), 11, 14(3), (6), (7).
Section 9(1) is in the passive ("may be appointed"), and so are s 14(3) and (6) ("must be terminated"). Section 14(4) speaks of an arrangement "made", with no maker. Only the Minister's acts are given an actor: s 10(1), s 12(1) and (4), s 9(3)(c)(i), and s 9(4). The duty in s 14(3) and (6) therefore has no named holder, and s 14(7) speaks of "a power of the Commonwealth". The L4 takes the appointing act, and whether the Governor-General made it, as facts (REF-17, REF-30). The scheme gives these acts to an "appointing authority" (the Governor-General in Council), and the Minister only becomes aware.
*How noticed: writing the scheme (each act needs an actor).*

**E-09. "Secretary" is defined and never used.** s 6.
No operative provision mentions the Secretary. The definition is encoded as a pass-through and nothing reads it. REF-05 had anticipated this.
*How noticed: encoding the L4.*

## Section 8: affiliations

**E-05. "10 years" has no statutory measure.** s 8(1), (2)(a).
The Acts Interpretation Act defines "month" (s 2G) but not "year". The encoding reads 10 years as 120 months running back from the end of the day in question. The boundary is FORK-01. One edge was chosen: where the period would have to begin on a 29 February that does not exist, it begins on 1 March.
*How noticed: encoding the L4.*

**E-06. The day an affiliation is tested on is not stated for s 10(2).** ss 8, 9(1)(a), 10(2), 11(2).
Section 8 changes with time: 10 years run out, and new employment begins. Section 9(1)(a) is tested on the day of the appointment and s 11(2) on the day of the arrangement (see FORK-14). For s 10(2), the encoding tests on the day the list is given. A candidate who was compliant when listed may come to have an affiliation, or lose a disqualifying one, before the recommendation or the appointment. Section 9(1)(a) catches the first case only for a disqualifying affiliation.
*How noticed: encoding the L4.*

**E-07. A person can have both affiliations at once.** s 8(1), (2)(a).
A person whose membership began more than 10 years ago and ended less than 10 years ago is "a member ... within the last 10 years" (s 8(1)). The same person has also been a member "at any time other than within the last 10 years" (s 8(2)(a)). The encoding gives that person both affiliations. No outcome found so far turns on the overlap, because a disqualifying affiliation bars the person under s 9(1)(a), s 10(2)(a) and s 11(2). EM para 12 describes s 8(2)(a) as "10 years ago or longer", which suggests that only past members were meant.
*How noticed: a failing case (Casey, member 2016 to 2020, was expected not to meet s 8(2)(a)).*

**E-08. Employment under the MOP(S) Act is tested only against the Act as it now stands.** s 8(2)(b); MOP(S) Act ss 3, 4, 11.
The L4 asks whether current s 11 authorised each engagement. Employment before the 2023 amendments, under the former Parts III and IV, is not mapped (REF-11; the earlier compilations are knowingly missing at 3H). A "shadow Minister" has no statutory office. The shadow Minister's personal staff count only if a s 4 determination is in force. Whether the shadow Minister's electorate staff count is FORK-02.
*How noticed: encoding the L4 (the boundary module).*

## Sections 9 and 10: the selection process

**E-10. Every office in s 7(1) is treated as the head of a mission.** s 7(1); Public Service Act 1999 ss 7, 39.
The L4 treats each s 7(1) office as heading an Australian diplomatic or consular mission: an embassy, high commission, consulate-general or permanent mission. A Public Service Act s 39 Head of Mission is the head of such a mission. For an office prescribed under s 7(2), whether it heads a mission is a fact. Whether a Consul-General heads a "consular mission", and whether a Permanent Representative heads a "diplomatic mission", is assumed, not decided.
*How noticed: encoding the L4 (the boundary module).*

**E-11. Section 14(2) and Public Service Act s 39(1) are set side by side.** s 14(2); Public Service Act 1999 s 39(1).
Under s 14(2), a non-compliant appointment is still valid. Under s 39(1), a Governor-General's appointment of a Head of Mission "cannot take effect" unless the person is an APS employee. The encoding keeps the two apart: one rule says whether the appointment is invalid under s 14 (never), and another says whether it can take effect under s 39(1). For a person from outside the APS, s 39(2)(a) directions are the route in.
*How noticed: encoding the L4 (the boundary module).*

**E-12. A Committee can be left unable to decide, and nothing ends it.** ss 10(3), (5), 12(3), (8), 13(2).
A Committee is dissolved only by giving its s 10(3) notice (s 10(5)). It can decide only at a meeting at which all 3 members are present (s 13(2)). If it lacks members or never meets, it is never dissolved, and s 12(8) bars a further Committee for that appointment. A member might resign (the rules may provide for that, s 12(6)(g)), be absent, or never be appointed. Nothing in the Bill closes a Committee that misses the 2 months. Acts Interpretation Act s 33(3), revoking the establishing instrument, may be an answer (REF-27). The scheme logs the overrun and its effect on s 12(8).
*How noticed: writing the scheme.*

**E-13. The list is taken as received on the day it is given.** s 10(1), (3).
Section 10(1) runs from establishing the Committee and requires the Minister to "give" the list. Section 10(3) runs from "receiving the list". The encoding counts both from one day, the day the list is given (REF-24; Acts Interpretation Act s 28A on service is not encoded).
*How noticed: encoding the L4.*

**E-14. When a Committee ceases to exist, and the s 12(8) edge.** ss 10(5), 12(8).
A Committee is "dissolved after giving the Minister written notice". The encoding treats it as gone on the day of its notice, so a further Committee may be established that day. The encoded s 12(8) looks only at Committees established before the day in question. Two Committees established on the same day are therefore not caught.
*How noticed: encoding the L4.*

**E-15. A referral is a decision at a quorate meeting, but needs no majority.** ss 10(3)(b), 13(1)-(3).
Under s 13(1), "A decision of a Selection Committee under subsection 10(3)" must be made at a meeting, and a referral is such a decision. Section 13(3) requires a majority on "a question". The encoding requires a quorate meeting for a referral but no majority, because a referral is what follows "otherwise". On a strict reading, a Committee split three ways could reach no decision, not even to refer.
*How noticed: encoding the L4.*

**E-17. One Committee decision, one question.** ss 10(3), 13(3).
Each Committee record carries a single vote count: the vote on the question its notice reports. A Committee that votes on several candidates in turn is not modelled. Nor is a vote that recommends nobody but does not refer.
*How noticed: encoding the L4.*

**E-18. Tabling on a day the House does not sit.** s 9(4), (5); Acts Interpretation Act ss 2M, 34B.
The encoding counts the sitting days, which are facts, between the appointment and the day the statement is tabled. It does not model presentation to a House that is not sitting (s 34B, REF-21). A statement "tabled" on a non-sitting day after the 5th sitting day would count as in time if no further sitting intervened.
*How noticed: encoding the L4.*

**E-19. A "recommendation has been made" closes s 9(3) for the vacancy.** s 9(2), (3)(a), 10(7).
After a Committee for a vacancy recommends someone, s 9(3)(a) can no longer be met for that vacancy, even if the recommended person is never appointed (declines, dies, or is not chosen). Section 9(2) then permits that one person, and a further Committee may recommend another. If no Committee ever agrees again, the only routes left are more Committees.
*How noticed: encoding the L4.*

## Sections 11, 14 and 15

**E-16. An acting arrangement on no s 11(1) occasion.** ss 11(1), 14(4).
Section 11 applies only to a person acting "during a vacancy" or during an appointee's absence or inability. An arrangement to act at any other time meets no requirement of the Act, so it breaches none. The encoding treats it as in accordance with the Act. The scheme logs it as a warning.
*How noticed: encoding the L4.*

**E-21. "The term of the appointment starts" is a fact.** s 15.
No law states a term for these appointments. The day the term starts is taken as a fact separate from the day the appointment is made. An appointment made after commencement with a term starting in the first 12 months is outside the Act whoever is appointed, a sitting member included (`cases.l4`, the Casey cases). Committees may be established from commencement.
*How noticed: encoding the L4.*

**E-22. "As soon as practicable" and "becomes aware" are facts.** s 14(3), (6).
The encoding takes as facts whether the Minister knows the facts of a failure and whether a termination came as soon as practicable. Awareness of the facts is treated as awareness of the failure. Whether the Minister must also know that the facts amount to a failure is not decided.
*How noticed: encoding the L4.*

## The console scheme

**E-20. The console does not apply Acts Interpretation Act s 36(2).** ss 10(1), (3).
The console engine has no day of the week. So a last day that falls on a Saturday, Sunday or holiday is not carried to the next working day for the 7 days or the 2 months. The L4 applies s 36(2), with a list of holidays given as facts. The scheme's logs cite this.
*How noticed: writing the scheme.*

**E-23. Offices are a fixed list in the console's acts.** Scheme only.
The engine's acts take one target. So appointing a person, arranging for a person to act, and resolving to approve an appointment each name the office through a choice of the 16 offices in the opening cast. An office added in God mode, such as one prescribed under s 7(2), cannot be chosen.
*How noticed: writing the scheme.*

**E-24. The console summarises the list.** s 10(1), (2); scheme only.
A list is given in the console as numbers: how many candidates, how many with a significant affiliation, whether one is disqualified, and whether reasons are set out. Whether a recommended candidate was on the list is a tick-box. The L4 works from the actual candidates and tests each one under s 8.
*How noticed: writing the scheme.*

**E-25. In generated runs, an act's parameters are evaluated with the actor as `$self`.** Scheme only.
In the console engine, an act's parameters are evaluated after `$self` has been rebound to the actor, so they cannot read the generating actor. The first simulation runs showed appointments to no office. The generators now reach offices through `$target` or through an `officeId` the office records on itself. This is a tool behaviour, not a question about the law.
*How noticed: writing the scheme (a simulation run).*
