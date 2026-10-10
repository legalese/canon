# Public Defenders Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 23 of 2022, informal consolidation, "version in force from
1/5/2026". The deposit annotates amendments by Act 32 of 2024 (wef 25/11/2024),
Act 31 of 2023 (wef 01/12/2025) and, the latest, S 247/2026 (wef 01/05/2026).

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it decides whether a person of limited
means who is charged with a crime in Singapore gets a state-funded defence lawyer.
This row takes what an accused person and his or her family meet: who counts as a
minor and a guardian (s 2), which offences aid cannot cover (s 8 and the Schedule)
and when it can cover them anyway (s 12(8)), repeat applications (s 9(3), (4)),
turning 21 mid-case (s 10(3) to (5)), the conditions for a Grant of Aid and a
provisional grant (s 12(1) to (4), (7)), who pays contributions (s 17(2)),
discharging the assigned solicitor (s 18), costs against the aided person (s 19),
aid for an appeal (s 20), privilege (s 22(1), (4)) and the false-statement offence
(s 23).

Not encoded: the appointments (s 3), solicitor panels, removal and fees (ss 4 to 6),
personal immunity (s 7), the inquiry powers (s 11), who acts and notice to the court
(s 13), co-accused (s 14), variation and cancellation (ss 15, 16), contribution
amounts and recovery, costs against the Office (s 21), rules and regulations
(ss 24, 25) and the consequential amendments (ss 26 to 28).

## What the Act turns out to say

### 1. The means test is not in the Act

s 12(1)(a) requires the applicant to satisfy "the prescribed means criteria". The
Act sets no income or asset figure; the criteria, the prescribed offences and the
prescribed times are all left to subsidiary legislation, which was not retrieved.
The encoding takes them as yes/no inputs. For an unmarried minor, **both** the minor
and the guardian who applied must satisfy them. The Minister may direct a grant
"even though" the means criteria are not met (s 12(7)(b)). Asserted.

### 2. How the case is started can decide whether aid is available

Under the Schedule, Part 1, an offence under one of the 39 Part 3 Acts (among them
the Road Traffic Act 1961, the Employment of Foreign Manpower Act 1990 and the
Immigration Act 1959) is excluded only if "the accused person is served a notice to
attend court or a summons". The same drink-driving offence is within scope after an
arrest and excluded when begun by a summons. Any offence begun by a summons from an
officer of a statutory body, and any private prosecution, is excluded whatever the
Act. Asserted.

### 3. Capital charges are excluded, unless they come with others

Offences "punishable by death" are excluded (Schedule para 1), as are offences under
the Part 2 Acts (gambling, casino, massage establishment, organised crime and
terrorism laws). But s 12(8) lets a grant "extend to" an excluded offence where the
applicant faces 2 or more charges, one or more excluded. The encoding reads s 12(8)
with s 12(1)(b)(i), which points back to proceedings for a non-excluded offence, so
at least one charge must be non-excluded: two excluded charges alone do not qualify.
That reading is an inference, not words of the Act. Asserted.

### 4. Not every case gets the Chief Public Defender's own call on merits

Where the application concerns only prescribed offences, the Chief Public Defender
decides merits. Otherwise a board of the Chief Public Defender "and at least 2
solicitors" must find merit "by the majority of its members" (s 12(1)(c), as amended
by Act 32 of 2024). Merit includes needing a lawyer "to plead guilty". In weighing
whether a grant is appropriate, the benefit or detriment "must not be determined by
whether the interests of the applicant are ... adverse to" the prosecution or the
investigating agency (s 12(3)). Asserted.

### 5. Only citizens and permanent residents

s 8(1) limits aid to "a citizen or permanent resident of Singapore", and s 12(1)(b)
repeats it. The Minister's power to authorise a grant "in the interests of justice"
(s 12(7)(a)) is expressed "despite this section", meaning s 12, not s 8; and s 12(8)
treats grants under (7) as otherwise bound by s 8(1). The encoding therefore does not
let a Ministerial grant reach a foreigner. That is an inference. Asserted.

### 6. Aid is not continuous: turning 21, and appealing, need fresh steps

A minor (below 21, s 2) whose case is still running at 21 must give written consent
within the prescribed time to keep the aid, and is deemed to have made a fresh
application "in his or her own right" (s 10(3) to (5)). After trial, an appeal needs
a fresh application within the prescribed time, though a late one may still be
considered if the notice of appeal was filed first or there are extenuating
circumstances (s 20). Asserted.

### 7. What you tell the Office about your means is not privileged

Solicitor-client privilege attaches to dealings with public defenders and assigned
solicitors (s 22(1)), but not to "information ... concerning the means and other
circumstances of the applicant" (s 22(4)). Failing to disclose means fully, or to
report a change that may make one ineligible, is an offence carrying up to $5,000 or
6 months or both (s 23); only the false-statement limb says "knowingly". Asserted.

### 8. The aided person cannot simply fire the lawyer

s 18(1): an aided accused person "must not discharge" the assigned solicitor without
the Chief Public Defender's permission. A court may order the aided person to pay
the defence's costs where the grant was obtained by fraud or misrepresentation or he
or she "acted improperly" in the proceedings, even after cancellation (s 19).
Asserted.

## What would need doing before this is worth anything

- The regulations prescribing the means criteria, the prescribed offences and the
  prescribed times, and the circumstances for variation and cancellation, were not
  retrieved; without them the encoding cannot say whether any real person qualifies.
- The two inferences (findings 3 and 5) need checking against the regulations,
  practice of the Public Defender's Office, or a decision.
- Only a sample of the Schedule's Part 2 and Part 3 Acts is enumerated.
- No case law was searched.
