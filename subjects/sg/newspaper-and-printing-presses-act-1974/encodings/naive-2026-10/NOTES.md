# Newspaper and Printing Presses Act 1974 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1 November 2022 (s 14 repealed by Act 31 of 2022 with effect from that date; S 26/2022
annotated at s 39).

**Checks:** one case file, 175 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**11 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
printer, a publisher, an investor in a newspaper company, a journalist or a seller of
foreign newspapers meets: the press licence and imprint (ss 3, 5, 6, 44(2)), who may
publish a weekly-or-more-frequent newspaper (ss 7, 8), management shares (s 10),
control thresholds (ss 11, 12), penalties and defences (s 17), foreign funding
(s 19), permits and foreign newspapers (ss 21, 23, 24, 25, 28), register fees (s 31),
the s 33 defence, the general penalty (s 35), consent to prosecute (s 37) and
composition (s 42). The Registrar and registers, the Minister's approval criteria and
objections as discretions, information powers, search and seizure powers, the
management-share issue price and appeals are not encoded.

## What the Act turns out to say

### 1. Management shares carry 200 votes each, but only on hiring and firing

s 10(11): a management share carries "200 votes" on any resolution "relating to the
appointment or dismissal of a director or any member of the staff", and otherwise
the same rights as an ordinary share. s 10(4) requires 1% of every share issue to be
management shares, and s 10(1)(c) lets them go only to holders the Minister has
approved in writing. If an ordinary share carries one vote (the articles decide, not
the Act), 1% of the capital in management shares (200 votes per 100 shares) outvotes
the other 99% (99 votes) on every appointment and dismissal. That is arithmetic, not
a statement in the Act. The encoding reads s 10(1)(c) ("citizens of Singapore or corporations who
or which have been granted the Minister's written approval") as requiring approval
even for citizens; that is an inference from the wording. Asserted.

### 2. The prison term turns on the kind of control, not its size

s 17(1): becoming a substantial shareholder or a 12% controller without approval is
punishable by a fine of up to $50,000 only. s 17(2): becoming an *indirect
controller* (one whose directions the directors follow, or who can determine policy,
s 12(5)) without approval adds up to 3 years' imprisonment. Both carry $5,000 a day
for a continuing offence. Asserted.

### 3. A family member's purchase can make you a controller, and there is a defence for exactly that

The 12% test counts holdings "together with the person's associates" (s 12(3)), and
associates include a spouse, parents, step-parents, ancestors, children,
stepchildren, issue and siblings (s 12(4)(c)(i)) but not cousins, uncles, aunts,
nephews, nieces or in-laws. s 17(4) gives a defence, for s 12(1) only, where the
contravention came from such a family associate's increase, there is no agreement to
act together, and the Minister was told within 14 days. Otherwise, lack of intent is
expressly no defence (s 17(5)). Asserted.

### 4. Any non-citizen is a "foreign source", even a resident

s 19(5)(c): "any person who is not a citizen of Singapore whether or not the person is
resident in Singapore". Receiving such funds for a weekly newspaper needs the
Minister's prior approval (s 19(1)), unsolicited funds must be reported within 3 days
(s 19(3)), and a journalist must report foreign-sourced payments to the managing
director within 7 days (s 19(8)); money from outside Singapore is presumed foreign
(s 19(9)). Dealings in quoted shares are carved out (s 19(6)). A Singapore company with a
foreign director is a foreign source only if the Minister gazettes it (s 19(5)(d)).
Asserted.

### 5. Six copies is a presumption of selling

ss 23(6) and 24(6): a person with "more than 5 copies of the same issue" of an
offshore or declared foreign newspaper is presumed to hold them for sale or
distribution. An "offshore newspaper" is a foreign-edited weekly-or-more-frequent
paper covering Southeast Asian politics, unless every issue circulates fewer than 300
copies here (s 23(7)). Subscribing to a declared foreign newspaper other than through
an authorised distributor is itself an offence, $5,000 or 6 months (s 28). Asserted.

### 6. Business cards and letterheads are outside the Act altogether

s 44(2): "Nothing in this Act extends to ... any visiting or business card, bill-head
or letter heading" or an engraving. Everything else printed in Singapore must carry
the printer's and publisher's names (s 5), and the printer must keep a copy for 6
months (s 6). Asserted.

### 7. Smaller points

- s 3 states no penalty for an unlicensed press; the s 35 general penalty
  ($50,000 or 2 years) would apply. That is an inference. The occupier of premises
  where a press is found is deemed to keep it until he proves otherwise (s 3(5)).
- Register searches cost $1, certified copies $2 (s 31).
- No prosecution without the Public Prosecutor's consent (s 37).
- A prescribed compoundable offence may be compounded for up to $1,000 where the
  maximum fine is $5,000 or less, otherwise up to $5,000 (s 42). Which offences are
  prescribed is left to rules. Asserted.

## What would need doing before this is worth anything

- "Substantial shareholder" is defined by s 81 of the Companies Act 1967, which was not
  read; it is an input here.
- The rules under ss 42 and 45 (compoundable offences, fees, forms) and any
  exemption orders under s 44 were not retrieved.
- The s 6 six-month period is counted in whole months; the boundary day is not
  modelled.
- No case law was searched.
