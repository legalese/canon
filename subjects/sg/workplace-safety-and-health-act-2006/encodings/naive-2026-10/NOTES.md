# Workplace Safety and Health Act 2006 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/12/2025"), with amendments to Act 30 of 2024 (platform workers, in force 1 January
2025), Act 12 of 2020 (s 19(3), in force 1 October 2025) and S 754/2025 (in force
1 December 2025) shown.

**Checks:** one case file, 120 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes what an
employer, principal, worker or company officer actually meets: who counts as an
employee (s 6(2), (3)), who is outside the Act (s 3(2), s 62(1), Sixth Schedule), the
principal's duty to contractors (ss 14(2), 14A(4)), the protections in s 18, the
scene of a fatal accident (s 25), remedial and stop-work orders and appeals (ss 21,
22), the onus on the accused and on officers (ss 47, 48), the maximum penalties (ss
15, 18, 20, 21, 23, 25, 26, 46, 50, 51, 53), composition (s 56) and civil liability (s
60).

Not encoded: the content of the general duties in ss 11-17 (standards "so far as is
reasonably practicable", not tests), Part 7 management arrangements, the Council and
codes of practice, inspectors' powers, and the Schedules of dangerous occurrences,
diseases and machinery. Which offences are compoundable, and what must be notified
under s 27, is in regulations not retrieved.

## What the Act turns out to say

### 1. A reckless worker faces up to $200,000; a negligent one up to $30,000

s 15(4) gives an expressly lower penalty for a *negligent* act endangering safety:
$30,000 or 2 years. s 15(3), the *wilful or reckless* act, states no penalty at all,
so it falls to the s 50 general penalty: $200,000 or 2 years for a natural person,
$500,000 for a body corporate, plus a daily fine if it continues. Asserted.

### 2. Defying a stop-work order costs ten times defying a remedial order

s 21(6): a remedial order, $50,000 or 12 months plus $5,000 a day. s 21(7): a
stop-work order, $500,000 or 12 months plus $20,000 a day. And an appeal (within 14
days of service, s 22(1)) suspends a remedial order but not a stop-work order, which
must be obeyed pending the appeal (s 22(2), (3)). Asserted.

### 3. The burden is on the accused, twice over

s 47: where a duty is "so far as is reasonably practicable", it is for the accused to
prove that nothing more was reasonably practicable. s 48: when a company offends,
every officer is guilty unless the officer proves *both* no consent or connivance
*and* all due diligence. Proving one is not enough. Asserted.

### 4. A contract term does not discharge a principal's duty

s 14A(4): it is not a defence for a principal to rely "solely" on a contract term that
the contractor has complied or will comply. The s 14(1) duty to contractors' workers
applies only when they work under the principal's direction as to manner (s 14(2)).
Asserted.

### 5. A second death from the same offence lifts the fine cap

s 51: on a second conviction of the same offence causing death, the maximum fine
becomes $400,000 (natural person) or $1 million (body corporate). The text is not
limited to s 50 offences, so the encoding applies it to any offence; **this is an
inference**. Asserted.

### 6. Regular volunteers and interns are employees; the Government cannot be prosecuted

s 6(2): a volunteer working regularly, with the other person's knowledge or consent,
in connection with that person's business is treated as an employee; a one-off
volunteer is not. s 6(3): so is a person on the job for training or work experience.
s 3(2): the Act binds the Government but does not make it liable to prosecution, and
s 3(3) denies that immunity to its contractors. On-duty uniformed services and
self-contained international crews are outside the Act (Sixth Schedule). Asserted.

### 7. Smaller points

An employer may not charge employees for safety measures (s 18(1)) or dismiss them
for helping an inspector, reporting in good faith, committee work or complying with
an order, or proposing to (s 18(2)): $5,000 or 6 months. Records must be kept at
least 5 years (s 18(4)). Altering the scene of a *fatal* accident, dangerous
occurrence or occupational disease without consent is an offence unless for rescue
(s 25); a non-fatal accident is not covered by s 25(1). Composition is capped at the
lower of half the maximum fine and $5,000 (s 56). The Act confers no civil right of
action (s 60). Asserted.

## What would need doing before this is worth anything

- The regulations (which offences are compoundable, what is notifiable under s 27,
  any other record-keeping period under s 18(4)) were not retrieved.
- Imprisonment terms stated in offence sections are returned whether or not the
  offender is a body corporate; the text does not say how they apply to one.
- The second-conviction rate for s 15(5) and the s 51 repeat rule are modelled as
  flags on the facts, not derived from a conviction history.
- No sentencing decisions or case law were searched.
