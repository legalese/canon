# Notaries Public Act 1959 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act, ss 1–8**, as printed by SSO, current version as at 05 Oct 2026 (2020 Revised Edition).
The Act was last amended by Act 20 of 2007, in force 1 June 2007, and s 7 carries its marker "[20/2007]". Earlier texts were not supplied, so **every rule that is about a day refuses for a day before 1 June 2007** rather than let today's text answer for it.

Not in the source, so not encoded: the powers and functions "ordinarily exercised by notaries public in England" (s 4(1)), and the Notaries Public Rules made under s 8 (which prescribe further powers under s 4(3)(c), and fees). Where an answer turns on them the encoding refuses, naming why.

## 2. Coverage table

| s | heading | disposition |
| --- | --- | --- |
| long title, 1 | | inert |
| 2 | Interpretation | encoded: "notary public" (fork F3); "Senate" is an office, not a rule |
| 3 | Appointment of notaries public | encoded: (1)–(4) the appointment decision with each refusal reason; (5) temporary appointment; (6) and (1) when an appointment has effect; (7) Gazette publication is an input |
| 4 | Privileges of notaries public | encoded: (2) and (3)(a)–(b); (1) and (3)(c) refuse (not in the source) |
| 5 | Misconduct of notaries public | encoded (a mandatory revocation) |
| 6 | Revocation on request | encoded (a power) |
| 7 | Penalty for unauthorised exercise | encoded: the offence, the $10,000 ceiling, the court |
| 8 | Rules | encoded: (1) who makes them; (2) when they come into force |

## 3. Fork register

| id | provision | the question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 3(5) "a period exceeding one month" | how is a month counted? | a calendar month: leaving 1 March and returning 1 April is one month, not more | The Act does not say, and a calendar month is the ordinary meaning. |
| F2 | s 3(1), (6) "a period not exceeding 12 months" | when does a 12-month appointment end? | the day before the same date 12 months on (1 Jan 2026 → 31 Dec 2026); an appointment stated for longer is read as running for 12 months | The period is of months, reckoned by the calendar. A longer stated period is beyond the power, and the encoding does not let it run on. |
| F3 | s 2 "notary public" | s 2 excludes only a person whose appointment "has been revoked under section 5". Does a revocation under s 6 (on request) end the status? | yes | s 6 "revoke[s] the appointment" in the same words; a revoked appointment that still made someone a notary would make s 6 do nothing. |

Smaller readings:
- **s 3(5)** does not repeat the 7-year requirement of s 3(2): a temporary appointee must be practising, nothing more. But **s 3(3)** ("any appointment under this section") does apply: the Council must be consulted for a temporary appointment too. That limb was missing from the first version and was added after the independent test pass found it.
- **The s 3(1) decision takes no date**, so the 1 June 2007 gate does not reach it. It states what the current text requires.
- **Gazette publication (s 3(7))** is recorded on an appointment and read by no rule, because the Act attaches no consequence to its absence.
- **s 4(2)** gives way to s 4(3) ("Except for the purposes of … subsection (3)"). So an affidavit proving due execution may be sworn before a notary even when it is for use in Singapore.
- **s 7**: the two ways of acting "otherwise than in accordance with the provisions of this Act" encoded are not being a notary public that day, and acting beyond s 4. Other departures from the Act, such as breaching the s 8 rules, are folded into the `within the s 4 powers` input.

## 4. Tests

`npa-tests.l4`, 51 assertions: s 3(2) at 6 and 7 years; each s 3 refusal reason; the 12-month limit; the temporary appointment at exactly one month and just over, and without the Council's consultation; when an appointment has effect, including revocation under s 5 and s 6 and lapse on the absent notary's return or death; s 2; each limb of s 4, including (2) giving way to (3) and the refusal where English practice decides; each limb of s 5; s 6; the s 7 offence in four situations and the 2007 date gate; and s 8.
`tests-independent.l4` (59 assertions) and `INDEPENDENT-TEST-REPORT.md` are the independent pass. A separate session wrote its expectations from the source before reading the encoding (`independent-expectations.md`). All 59 passed, and its notes found one gap, the s 3(3) consultation for temporary appointments, which was then fixed.

## 5. Checks

See `encoding.json` → `checks`.
