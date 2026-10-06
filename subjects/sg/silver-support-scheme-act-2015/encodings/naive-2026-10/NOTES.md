# Silver Support Scheme Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 December 2025.

**Checks:** `l4 run sss-cases.l4` and `l4 run sss-administration-cases.l4` —
102 assertions satisfied, 0 errors, 0 warnings.

**No `daydate`.** The `l4` on this machine imports `prelude` but not `daydate`,
so there is no `DATE` type. A date is carried as its three components and
compared as a single ordered number (`yyyymmdd`). That is enough here, because
every rule in s 6(2) is about *calendar components* rather than elapsed time —
but it would not be enough for an Act that counted days.

## The one thing to know before using this

**This Act decides almost nothing about who gets Silver Support.** s 6(1) has
three limbs, and the third is "satisfies all other eligibility criteria that may
be prescribed". Citizenship and age are the only criteria in the Act itself.
Everything that actually determines whether a person receives the payment —
income, housing type, lifetime CPF contributions, household support — is in
regulations, and those were not retrieved.

So a system built on this encoding alone cannot answer "am I eligible?". It can
answer "have I attained 65 for the purposes of this Act?", which is a real
question with a surprisingly intricate answer, and it can answer the recovery
and offence questions. The eligibility rule is carried as a supplied fact and
the encoding says so rather than pretending otherwise.

## Three observations on s 6(2)

**1. The 29 February rule is never a fallback — it is the only rule that can
ever apply.** s 6(2)(b) deems the 65th anniversary of a 29 February birth to
occur on 1 March. One might read that as a tidy-up for the years when
29 February does not exist. It is more than that: **65 years after a leap year
is never itself a leap year**, because 65 leaves a remainder of 1 on division by
4. So a 29 February birthday has *no* 65th anniversary in the ordinary sense,
ever, and s 6(2)(b) is doing all the work in every single case. Asserted for
1956, 1960 and 1964 → 2021, 2025 and 2029, none of them leap years.

The consequence for a person: someone born on 29 February 1960 and someone born
the next day, 1 March 1960, attain 65 **on the same day**. The leap-day person
is a day older and waits no less long. Asserted directly as an equality of the
two anniversary dates.

**2. The deeming rules have no stated order, and the order changes the answer.**
Where the month cannot be ascertained but the day is recorded as 29, (d) deems
the person born in January, so the deemed date is 29 January and (b) never
engages. Had (b) been applied to a *recorded* 29 February instead, the answer
would be 1 March. The Act does not say whether (b) reads the actual date or the
deemed one, and the two readings differ by over a month for anyone in that
position.

The encoding applies the deeming first and then tests for 29 February, which is
the reading on which (c) and (d) do their work before (b) looks at anything.
That is a choice, and it is asserted at
`born in 1960, month unknown, day 29`, so a change of reading cannot pass
silently. How many people are affected is unknown — probably very few, and all
of them elderly people with incomplete birth records, which is precisely the
population this Act exists for.

**3. The deeming is in the claimant's favour, and consistently so.** An
unascertainable day moves the birthday to the first of the month; an
unascertainable month moves it to January. Both make the person eligible
*earlier* than a known later date would. Asserted as the pair against a known
15 June birthday.

## One observation on s 10

s 10(1) and s 10(2) are different recovery routes and only one of them reads
s 6. Under s 10(1) the question is whether the recipient was eligible and
whether the amount was right. Under s 10(2) the question is whether the benefit
was obtained by a false statement or document, and it applies "whether or not an
eligible individual" — so a fully eligible person paid exactly the right amount
is still liable to repay the whole of it if they lied to get it. Asserted on
`a correct payment obtained by a lie`, which is recoverable under (2) and not
under (1).

## What would need doing before this is worth anything

- The regulations under s 20 carry the whole of the real eligibility test and
  every benefit amount. They were not retrieved. This is the gap that matters.
- No case law was searched.
- The three observations above are observations. The second in particular needs
  someone who can say how the Central Provident Fund Board actually applies the
  deeming rules in practice.


---

# Added with sections 8, 9 and 13 to 19

## The information regime is the interesting half

The Scheme pays people **without their applying**. That only works if the
Government can assemble means information about them from other departments, and
ss 8 and 9 are where that is arranged. They decide the privacy of every
recipient, and they are more consequential than anything in the eligibility
sections.

**s 8 compels disclosure, and an existing duty of confidence is no answer.** A
department directed under s 8 must comply "**despite any other written law, and
whether or not it is under any obligation ... not to disclose**". Three
safeguards are built in and all three are conditions rather than discretions: a
**written** ministerial certificate of necessity, a limit to "**so much ... as is
necessary**", and a stated purpose. Asserted as a pair on the
duty-of-confidence fact, where the answer deliberately does not move.

**s 9(5) is an opt-out, not an opt-in.** Reports about an individual flow to
other prescribed public schemes unless that individual opts out "in the manner
determined by the Commissioner". The burden is on the person to discover that
the reports exist and that they may be stopped. Nothing in the Act requires
anyone to tell them.

## The penalty ranking

Set the four maxima side by side:

| offence | maximum fine |
|---|---|
| s 15 obstructing the Commissioner or an investigator | **$20,000** |
| s 14(4) failing to produce information or a document | $10,000 |
| s 9(7) misusing a recipient's private information | $5,000 |
| s 11 dishonestly obtaining a benefit | $5,000 |

Obstructing the investigation is worth four times as much as misusing the
information the investigation gathered, and four times as much as the fraud the
Act exists to prevent. That is a choice, and the Act does not explain it.
Asserted directly.

## Two smaller observations

**s 17's half-the-fine limb can never bite.** Composition is capped at "the
lower of (a) one half of the maximum fine ... (b) $1,000". The half-limb only
governs where the maximum fine is $2,000 or less, and **the Act creates no such
offence** — its lowest maximum is $5,000. So limb (a) is inoperative on the
Act's own offences as it stands. It would come alive only for an offence created
by regulations with a maximum under $2,000.

**Neglect alone makes an officer personally guilty.** s 16 attributes a body's
offence to an officer either on "consent or connivance" **or** on neglect. No
knowledge is needed for the second limb. The same two limbs reach members
managing a body corporate, partners, and officers of unincorporated
associations.

## What would still need doing

- ss 1–5, s 18 and s 20.
- The regulations under s 20, which carry the whole of the real eligibility test
  and every benefit amount. This remains the gap that matters most.
- No case law was searched, and no human gate has been sought.
