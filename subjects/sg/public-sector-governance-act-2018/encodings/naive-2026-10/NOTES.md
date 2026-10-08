# Public Sector (Governance) Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 August 2026.

**Checks:** three case files, 404 assertions satisfied, 0 errors, 0 warnings.

## Why this Act

A citation count across the 527 Singapore Acts deposited in this repository found
**70 Acts that cite the Public Sector (Governance) Act 2018**, excluding mentions in
legislative-history tables (which had made it look like 79). For an Act of only
84,000 characters that is the best ratio of reach to size among the unencoded Acts.
Most of the citations are to ss 4 and 5, the Minister's power to direct a statutory
board.

## Scope

The **whole Act**, bar s 1 (short title), s 3 (purposes), ss 43 and 44 (regulations
and their presentation) and the **contents** of the three Schedules.

| module | provisions |
|---|---|
| `psga-directions.l4` | Parts 1 and 2: the Groups, agencies, officers, control of information, ss 4–5 directions, s 6 sharing, the s 7 and s 8 offences, ss 9–11 |
| `psga-personnel-governance.l4` | Part 3 (chief executives, deemed public servants and officers) and Part 4 (conflicts of interest, meetings, resolutions, delegation) |
| `psga-finance.l4` | Part 5 (estimates, accounts, audit, reporting), s 42, s 45 |

**Which public body is in which Part of which Schedule is taken as a fact about each
body**, not enumerated: the Schedules list roughly a hundred. Group 1B is the Defence
Science and Technology Agency alone and Group 1C the People's Association alone, and
several findings below turn on that. The constitutional Acts of the listed bodies,
and the regulations, orders and prescribed circumstances the Act leaves open, were
not retrieved.

## What the Act turns out to say

### 1. Section 4 reaches every agency; section 5 reaches Group 1 only

s 4 lets the Minister direct "all Singapore public sector agencies" — Groups 1, 2
and 3, ministries, departments and Organs of State — to comply with a Government
policy on one of five pertinent subject matters, for one of seven purposes. s 5 lets
the responsible Minister give a Group 1 body directions "as to the performance by
the public body of its functions", with no confinement to purpose or subject matter.

So a Group 2 professional regulator or a Group 3 community body can be directed on
employment, records, finance, IT and data, and cannot be told how to perform its
functions. Asserted.

And s 45(1) treats every pre-2018 ministerial direction as if given under s 5. A
saved direction to a Group 2 or Group 3 body is therefore treated as made under a
power that body is outside, and the Act does not say what becomes of it. Asserted.

### 2. Group 2 and Group 3 carry a main-function test that 2A, 2B, 3A and 3B do not

"Group 2 public body" means a public body specified in the Second Schedule "being a
public body the main function of which is to regulate the practice and standards of
a profession". "Group 2A" means a public body specified in Part 1 of the Second
Schedule — no main-function condition. Group 3 and 3A/3B are parallel.

So a body in Part 1 of the Second Schedule whose main function is **not** regulating a
profession is a Group 2A public body and **not** a Group 2 public body. Parts 3, 4
and 5 apply to "every Group 1, every Group 2 and every Group 3", so such a body falls
outside all three, even though s 15 names Group 2A. Asserted at each Part.

### 3. Section 11(3): the Minister may direct a policy but not a person

s 11(3): Part 2 does not authorise a direction requiring "the performance or
non-performance of a particular act or the bringing about of a particular result, in
respect of a particular person or persons", or "the making of an employment decision
relating to a particular individual". s 11(5) defines "employment decision" to
include appointment, promotion, transfer, remuneration, termination and discipline.

So the Minister can direct a policy on dismissals (s 4(3)(a) lists "employment,
management and discipline of employees") and cannot direct one dismissal. Asserted.

**s 11(2) cuts a direction back; it does not strike it down.** A direction is "not
binding … to the extent (if any)" it would impede a statutorily independent function
or a quasi-judicial function in a particular matter. Asserted as valid-and-partly-
binding, separately from a direction that is inconsistent with an Act, which fails.

### 4. Section 6 overrides the common law of confidence and nothing else

s 6(1) authorises sharing under a data sharing direction "despite any obligation as
to confidentiality under the common law". s 6(2): this "does not override any
obligation as to confidentiality because of legal privilege or contract". s 6(3):
the Act is not intended to prevent sharing permitted by other law.

A **statutory secrecy provision in another Act** is not mentioned at all, and so is
untouched: the sharing is "authorised" by s 6 and the other Act's prohibition still
stands. Asserted as: authorisation exists, and the obstacle remains, for privilege,
contract and statutory secrecy alike; it falls away only for the common law duty.

A direction under s 5 is not a "data sharing direction" (defined as a direction
"given under section 4"), so authorises nothing under s 6.

### 5. The three offences are not alike, and the contractor's is the narrowest

| | s 7(1) disclosure | s 7(3) use | s 7(4) contractor's use | s 8(1) re-identification |
|---|---|---|---|---|
| who | relevant public official | relevant public official | contractor or its employee | relevant public official |
| needs gain/harm/loss? | **no** | **yes** | **yes** | **no** |
| personal data | covered | covered | **excluded** | anonymised data |
| authorisation tested | a data sharing direction | a data sharing direction | **the agency** | a data sharing direction |
| penalty | $5,000 / 24 months | same | same | same |

Three consequences, all asserted.

**A contractor's employee who passes government personal data to a third party commits
no offence under this Act.** s 7(1) is confined to a relevant public official, which a
contractor's employee is not; s 7(4) covers only "use", and only of information "other
than personal data".

**"Loss" in s 7(3) and (4) excludes what the offence is most often about.** The
definition "excludes, in relation to an individual, the loss of personal data about the
individual". An official who misuses someone's personal data and thereby causes them
only the loss of that data has caused no "loss"; they must have caused a gain, harm
(which includes harassment, alarm or distress), or a loss of something else.

**The defences reverse the burden for ordinary official work.** The offences are framed
against *data sharing directions*, so an official's routine disclosure or use that no
direction authorises satisfies the authorisation element, and it is for the official to
**prove**, on a balance of probabilities, that it was "permitted or required by or
under an Act or other law". The elements and the defence are asserted separately, so
the burden shows.

**s 8(2)(c) needs both halves.** A reasonable belief that the re-identification was
for a specified purpose is a defence only if the accused **also** notified the agency
or the Government Technology Agency as soon as practicable. Belief without notice,
and notice without belief, both fail. Asserted.

A person who has left is not a relevant public official "at the time of the
disclosure", however recently. Asserted.

### 6. Group 1B and Group 3A

Group 1B is the **Defence Science and Technology Agency**. It must prepare estimates,
keep accounts and report to its Minister (ss 34, 36, 41(1)). It is outside the audit
regime (ss 37–40) and outside the presentation of its annual report to Parliament
(s 41(2)), so nothing it produces is audited under this Act or laid before Parliament.

**Group 3A is not named in s 33(1) at all**, so Part 5 does not apply to it: no
estimates, no accounts duty, no audit. Group 3B is named. Both asserted.

### 7. The seconded chief executive is inside ss 15 and 16 and outside ss 17 and 18

s 15 and s 16 (appointment, removal) have no exception for a public officer on
secondment. s 17(2) and s 18(3) (discipline, promotion) do. So a seconded Group 1 chief
executive must be appointed with the Commission's concurrence, but may be disciplined
and promoted without it. Asserted.

**Group 2B is not named in s 15 or s 16**, so a Group 2B chief executive is subject to
no rule at all in that Division. A Group 3 chief executive needs the Minister's
approval and nothing else. Group 1 needs the Minister's approval, the Commission's
concurrence, and appointment by the body.

**A misconduct dismissal of a Group 1 chief executive needs only the Commission's
concurrence under s 17** (s 16(2)(b) lifts the s 16(1) requirement), where any other
removal needs both the Minister's approval and the Commission's concurrence. The same
dismissal of a Group 2A or Group 3 chief executive needs the Minister's approval,
because s 17 does not reach them. Asserted.

**s 45(2) and (3):** s 15 does not apply to a chief executive already in office on
1 April 2018, but ss 16 and 18 do. Asserted.

### 8. The People's Association's committees are public officers and not public servants

s 20(2) deems committee members public **servants** for the Penal Code where the
committee was formed by "a Group 1A, Group 1B, Group 2 or Group 3 public body" and is
delegated a function. Group 1C is omitted. s 21(1) deems "every member of a committee
which is formed by a Group 1C public body to carry out any of its functions" a public
**officer** for the Financial Procedure Act. So a delegated committee of the People's
Association — the only Group 1C body — gets the Financial Procedure Act consequences
and loses the Penal Code ones. Asserted.

A purely advisory committee is outside s 21(1) too, on the words "to carry out any of
its functions". That is a reading.

### 9. Section 23(5) has the Companies Act s 5B defect

s 23(5) defines a "wholly-owned subsidiary corporation of a public body" with the same
four limbs as Companies Act 1967 s 5B, including limb (c): a subsidiary of the public
body "being a subsidiary none of the members of which is a person other than that
public body or a nominee". In the chain **public body → S2 → S1 → C**, C's only member
is S1, whose only member is S2, so S1 fails limb (c) and C is not a wholly-owned
subsidiary corporation. A director of C is outside the s 23(3)(f) exception for
directors of wholly-owned subsidiaries, although every share is held by the one body.

This is the same finding as in the `companies-act-1967` row of this repository, here
reproduced in a second Act. The reason is that s 23(5) borrows its formula, and "subsidiary"
itself, from the Companies Act.

### 10. The associate chain has no length limit

s 23(4)(e): "a chain of relationships can be traced between them under one or more of the
above paragraphs". The paragraphs are close family; partnership; a company and its
director or manager; and **a private company and a shareholder in it** with no minimum
holding. A member with one share in a private company is an associate of the company,
so a company contracting with the public body is an associate who may derive a
financial benefit, and the member is interested — unless s 23(3)(h) (so remote or
insignificant that it cannot reasonably be regarded as likely to influence) removes it.
A shareholder in a **public** company is not caught. Asserted at five links.

**The seven "only because" exceptions in s 23(3)(a)–(g) each remove one ground, not the
interest.** A member who has an excepted ground **and** a financial benefit is still
interested. Asserted.

### 11. The disclosure ladder overlaps and has a gap

s 25(1)(b): an ordinary member discloses to (i) the chairperson; (ii) "if there is no
chairperson or the chairperson is interested, to a deputy chairperson"; or (iii) "if
there is neither a chairperson nor deputy chairperson or if the chairperson and every
deputy chairperson are interested, to the responsible Minister".

- **Overlap.** Where the chairperson **and every deputy** are interested, (ii) still
  says to disclose to a deputy, and (iii) says to the Minister. Both apply.
- **Gap.** Where there is **no chairperson** and an **interested deputy**, (ii) applies
  and (iii) does not ("the chairperson and every deputy chairperson are interested" is
  not satisfied when there is no chairperson to be interested), so the disclosure goes
  to an interested deputy.

All asserted.

### 12. An interested member can stop the body deciding, and nothing can be done about it

s 26(d): an interested member "must be disregarded for the purpose of forming a quorum
for that part of a meeting". With the quorum exactly met, **one** interested member
takes the body below it. The Act gives the responsible Minister no power to act in the
body's place and provides no other route. Asserted at 5 present, 1 interested, quorum 5.

### 13. The whole conflict regime has no sanction

A member who fails to disclose, or votes while interested, commits no offence — the
only offences in the Act are in ss 7, 8 and 38. The decision stands: s 27(2) says the
exercise of a power "is not affected merely because" a member failed to disclose or the
body failed to notify. The only consequence is a duty on the body to tell its Minister
(s 27(1)), a duty the Act also leaves unenforced, since a failure to notify likewise
does not affect the body's acts. Asserted.

### 14. A circular resolution needs a majority of those *entitled to vote*, with no quorum

s 31: a resolution is passed if all members are sent the document and "a majority of
those members who are entitled to vote on the matter" sign. An interested member is not
entitled to vote (s 26(a)), so is outside the denominator, but must still be *sent* the
document. There is no quorum and no requirement of discussion. A body with two entitled
members passes a resolution on two signatures and not on one; exactly half is not a
majority. Asserted.

### 15. The auditor is the Minister's choice, annually, and must be a person

s 37(1)(b): "another auditor appointed annually by the responsible Minister … in
consultation with the Auditor-General" — not by the body. s 37(2): the appointee must
be "a public accountant who is registered or deemed to be registered" — an individual.
Companies Act 1967 s 10 lets an accounting firm, corporation or limited liability
partnership be a company's auditor; this section does not. Asserted.

Even the auditor's direct line to the Minister (s 39(3)) runs "through the public body"
being audited. The offence in s 38(3) is open to "a person" and is a fine not exceeding
$1,000, one fifth of the s 7 level; limb (a) has a reasonable-cause escape, limb (b)
(hindering, obstructing or delaying) has none. Asserted.

### 16. Smaller things worth recording

**s 42(2):** the Minister may add, delete or replace any public body in any Schedule,
"however … nothing … authorises adding the Monetary Authority of Singapore". The one
body the Act contemplates keeping out of the framework is named.

**s 25(2):** disclosure must give the nature and monetary value if it can be quantified,
else the nature and extent. Asserted that giving the extent does not discharge it where
the value *can* be quantified.

**s 24(3):** a standing disclosure ends if the nature "materially alters" or the extent
"materially increases". A **decrease** in extent does not end it. Asserted.

**s 9(2) and s 10:** a direction "does not have legislative effect" and yet the agency
"must … comply" and compliance is "regarded as" one of the body's functions under
written law. A direction binds without being law.

## What was read into the text, and should be checked

- The treatment of a **Group 2A body failing the main-function test** as outside Parts 3,
  4 and 5 follows from reading "every Group 2" in ss 12, 22 and 33 as bearing the
  condition and "Group 2A" in s 15 as not. A court might read s 15's naming of Group 2A
  as bringing such a body in.
- The **advisory-committee** exclusion from s 21(1) (finding 8).
- The **overlap and gap** in s 25(1)(b) (finding 11) are readings of drafting that may
  have been intended differently.
- The **Group 2B** silence (finding 7) is read as no rule, not as an oversight to be
  filled.

## What would need doing before this is worth anything

- **Enumerate the Schedules.** The Act's practical reach is which bodies are in which
  Part, and this encoding takes that as a fact for each body.
- **No case law was searched.**
- The constitutional Acts of the listed public bodies are not retrieved, and many of the
  rules here are expressed to give way to them (ss 5(2), 33(2), 38(1)).
- Cross-referenced Acts are not followed: the Penal Code 1871 (public servant), the
  Financial Procedure Act 1966 s 20, the Government Contracts Act 1966, the Personal Data
  Protection Act 2012 (personal data; the Eleventh Schedule), the Accountants Act 2004
  and the Companies Act 1967 (private company; subsidiary).
