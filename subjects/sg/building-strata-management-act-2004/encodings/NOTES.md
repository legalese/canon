# Building (Strata Management) Act 2004 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act** (Parts 1-8 and the First, Second and Fourth Schedules; Parts 3 and 7 are repealed, and the Third Schedule is omitted as having had effect), as printed in SSO's informal consolidation of the version in force from 1 October 2026. The Act was enacted as the Building Maintenance and Strata Management Act and has since been renamed. It is encoded from the text already deposited in this repository.

**Inputs.** These are taken as given rather than worked out:
- the discretions and findings of the Commissioner, the Minister, a Board and a court;
- prescribed matters: by-laws, fees, minimum insurance cover;
- valid-vote counts (s 2(8) applied before counting);
- public holidays (for "working day").

### The top-level goal

`the strata position for` a `Strata case` (`bsma-goal.l4`) answers: *for this strata development, is this matter validly decided by the management corporation; may this person sit on its council; and what does a proprietor in arrears now face?*

It returns:
- the resolution the matter needs;
- whether it is validly decided;
- whether a Board may make an order on it;
- the candidate's eligibility;
- when interest starts;
- whether the s 40(10) offence is committed;
- whether a charge may be lodged.

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Does the motion carry as the resolution the matter needs; was the meeting properly called, attended and voted? | `the motion is decided as`, `the resolution needed for`, `the matter is validly decided:`, `the general meeting may transact business…`, `the requisition obliges a meeting…`, `the most lots one proxy may represent…`, `the initial period ends…`, `the first AGM must be held by…`, `the next AGM is in time…` | s 2(2)-(8), ss 26, 27, 29(1)(d), 32-35, 37, 38(3A), 39, 41, 43, 50, 54, 59, 66, 67, 70, 71, 78, 84, 85, 85A; First Schedule | `bsma-meetings.l4` |
| 2 | May the developer sell; must it run maintenance funds and from when; what does it owe, and by when; what may the corporation not do in its initial period? | `the developer may make the disposal…`, `Division 1 applies to`, `the duty to establish maintenance funds arises on…`, `sold lots' charges are payable into the fund from…`, the s 17-26 dates, `the management corporation may do…`, `the developer is liable for the initial-period contravention…` | Parts 4, 5 Division 1; ss 23, 26(4), 49-52 | `bsma-developer.l4` |
| 3 | What does a proprietor owe; from when does it bear interest, become an offence, become a charge and allow sale; what must the corporation keep, give and lodge; may the proprietor do this to the lot? | `the lot's contribution…`, `the s 81 share…`, `interest runs on the contribution from`, `the proprietor commits the s 40(10) offence on`, `the corporation may lodge a charge for`, `the corporation may sell the charged lot,`, `the fund may pay for…`, `the by-law has effect…`, `the exterior window is part of the lot…`, `the proprietor may make the improvement…` | ss 2(9), 28-48, 62-65, 69-88 | `bsma-corporation.l4` |
| 4 | May this person stand for the council or an office; is the office vacated or may the member be removed; is the meeting quorate and the decision effective? | `eligible for election to the council`, `the threshold number…`, `the council's size…`, `the council member's office is vacated by`, `the corporation may remove the council member…`, `the council meeting is quorate…`, `the council's decision binds the corporation…` | ss 53-61, 80; Second Schedule | `bsma-council.l4` |
| 5 | May a Strata Titles Board hear and order this; when does its order take effect and how long does an interim order last? | `the Board is properly constituted…`, `the corporation is deemed to have refused…`, `a Board may order on a power exercised by`, `the interim order is in force,`, `the Board's order takes effect on…` | Part 6 | `bsma-boards-offences.l4` |
| 6 | Is this an offence, what is the most it can cost, may it be compounded, and when is a notice served? | `the maximum penalty for`, `the most that may be collected to compound`, `the notice is served on…`, `an emailed notice to a proprietor is served on…` | offence provisions throughout; ss 128, 129, 131, 136(4) | `bsma-boards-offences.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| long title, s 1 | carried as text |
| s 2(1) | read into the facts; "initial period" (Goal 1) and "working day" (Goal 6) are computed |
| s 2(2)-(8) | Goal 1 |
| s 2(9) | Goal 3 |
| ss 3, 4 | carried as text |
| Part 3 (ss 4A-9) | repealed |
| ss 10-14 | Goal 2 (s 14 penalty in Goal 6) |
| ss 15-22 | Goal 2 (penalties in Goal 6); powers carried as text |
| ss 23-25 | Goal 2 (s 23(4)-(5)); the rest carried as text |
| s 26 | Goal 1 (first AGM date, budget) and Goal 2 (s 26(4) documents); penalty in Goal 6 |
| s 27 | Goal 1 |
| ss 28-48 | Goal 3, and Goal 1 for the resolution each needs; the rest carried as text |
| ss 49-52 | Goal 2 |
| ss 53-61 | Goal 4 (penalties in Goal 6) |
| ss 62-65 | Goal 3 (s 65 periods); the rest carried as text |
| ss 66-68 | Goal 1 (resolutions); s 68 penalty in Goal 6; the rest carried as text |
| ss 69-75 | Goal 3 (ss 70, 73); the rest carried as text |
| ss 76-88 | Goal 3 (s 81 formula, ss 83, 85(3)); Goal 1 (resolutions); the rest carried as text |
| ss 89-120 | Goal 5; penalties (ss 96, 118, 120) in Goal 6; the order types carried as text |
| Part 7 (ss 121-122) | repealed |
| ss 123-139 | Goal 6 (ss 126, 127, 128, 129, 131, 134, 136(4)); the rest carried as text |
| First Schedule | Goal 1 |
| Second Schedule | Goal 4 |
| Third Schedule | omitted as having had effect |
| Fourth Schedule | carried as text (transitional) |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 49(3)(c)-(e) | (c), (d) and (e) are joined by "and", but (d) "not in a position to influence" and (e) "being in such a position, used all due diligence" cannot both hold | The defence is (c) and either (d) or (e) | It is the only reading under which the defence can ever succeed |
| F2 | First Schedule para 1A(1), (6) and s 2(2)-(7) | Does a special resolution shortening the meeting notice also shorten the 15 or 22 days s 2 requires for the motion? | No. The two tests are separate, and a motion is decided as a resolution only if s 2's notice is met | Para 1A(5) itself requires s 2's notice for special and stronger resolutions |
| F3 | s 40(10) "before the 14th day after the date of service" | Is payment on the 14th day in time? | No. It must be made by the 13th day after service | "before" the 14th day |
| F4 | s 43(1), (3) | When do 30 days and 6 weeks "after" expire? | At the end of service + 30 and publication + 42; the charge or sale is possible from the next day | Ordinary counting, excluding the first day |
| F5 | s 34A(1) | Which resolution does an EV-charger lease beyond 10 years need? | s 34(1)(b): a 90% resolution | s 34(2A) excludes only matters "falling within section 34A(1)" |
| F6 | First Schedule para 9(4) | "ignoring any fraction" | The value is rounded down | The text |
| F7 | s 101(6) | Which powers may a Board order on? | Those exercised by ordinary resolution or without a resolution. The function answers by resolution kind: any stronger kind is excluded | The text |

## 4. Tests

- **`bsma-tests.l4`: 249 assertions.** Expected values are worked from the source. They cover:
  - every resolution threshold and notice edge;
  - the resolution each matter needs;
  - quorum, proxies and requisitions;
  - the initial period, the first AGM and AGM timing;
  - each developer date and duty;
  - contributions, interest, the s 40(10) offence, the charge and sale;
  - funds, records and by-laws;
  - windows, improvements, entry and insurance;
  - council size, threshold number, eligibility, vacation, quorum and binding decisions;
  - Board constitution, deemed refusal and interim orders;
  - every penalty, composition and service rule;
  - whole cases through the top-level goal.
- **The independent pass.** The files are `tests-independent.l4` (288 assertions), `independent-expectations.md` (E01-E203, written before the encoding was read) and `INDEPENDENT-TEST-REPORT.md`. The first session was cut off by a usage limit; a second session completed it from the saved expectations.
  - **Result:** 286 pass and 2 fail. Both failures (E132 interest under s 40(6)(b), and E137 the charge under s 43(1)) are one-day-early expectations. The report itself concludes the encoding is right (fork F4): the 30 days end at the close of the 30th day. They are **expected failures**, and their expected values are left as written.
- **Changed after the independent pass:** the term of an exclusive-use by-law or a lease of common property is now named `term in years, with every renewal option`. Under ss 33(1)(b) and 34(2) the resolution turns on the aggregate term including options, so a 2-year term with a 2-year option must be entered as 4.
- **Simplifications the report lists, kept as they are:**
  - s 2(8) invalid votes are removed before the counts are entered;
  - the 12-week count is an input;
  - asking for more than 14 council seats returns 14 rather than refusing;
  - an appearance improvement under s 37(4) is authorised by the corporation with no stated resolution, so no matter is listed for it;
  - many First and Second Schedule meeting mechanics are carried as text (joint proprietors' votes, company representatives, proxies void when the appointer attends, election by one vote per lot, uncontested elections, council majority and notice, the managing agent's term, the minimum insurance cover).

## 5. Open questions

- s 49(3) (F1): which conjunction did Parliament intend?
- s 40(10) (F3): is the 14th day itself too late? The encoding says yes.

## 6. Checks

See `encoding.json` → `checks`.
