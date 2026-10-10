# Cybersecurity Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill conventions and nothing else. No pipeline, no coverage table, no independent
test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021,
in operation 31 December 2021), retrieved 1 October 2026 as the current version,
with amendments by Act 19 of 2024 (with effect from 31 October 2025) annotated
throughout. Deposited at `../../registers/source-bundle/CA2018.txt`. The arrangement
of sections at the top of the deposit numbers the saving and transitional section 48;
the body numbers it 49. The body was followed.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0065**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet.

Most of the Act governs a small number of designated operators. This row takes the
parts an ordinary business or individual meets: whether a cybersecurity firm needs a
licence, and what follows if it has none (s 2, Second Schedule, Part 5); what the
Commissioner can demand of anyone while investigating an incident (ss 19, 20); and
the core duties of an owner of provider-owned critical information infrastructure
(ss 14 to 16). Not encoded: designation of CII (ss 7 to 13), Parts 3A to 3D
(third-party-owned CII, systems of temporary cybersecurity concern and the 2024
additions), emergency measures (s 23), codes of practice, Part 6 procedure, and the
transitional s 49. The periods for s 14 reports are "prescribed" and the regulations
were not retrieved.

## What the Act turns out to say

### 1. Only two services need a licence

A "cybersecurity service" is broad: forensics, incident response, threat hunting and
even selling or installing cybersecurity solutions (s 2(1)(a) to (e)). But the
Second Schedule makes only two of them licensable: managed security operations centre
(SOC) monitoring and penetration testing, the latter expressly including social
engineering tests. A forensic examiner or firewall installer is providing a
cybersecurity service and needs no licence. Asserted.

### 2. An unlicensed tester cannot sue for its fee, even where s 24 lets it work

s 24(3) exempts a company providing a cybersecurity service to its related company
from the licence requirement. s 31 bars "any person who provides any licensable
cybersecurity service" from suing for a fee unless licensed when providing it, and
carries no related-company exception. On the words, an unlicensed group company may
test its sister company lawfully but could not sue it for the fee. That is a literal
reading of two sections side by side, not something either says. Asserted for s 31
alone; s 24 is asserted separately.

### 3. A contract is no excuse for staying silent; privilege is

When an incident response officer requires information under s 19, a person need not
disclose what is protected by a right, privilege or obligation "by or under any law or
rules of professional conduct", but "the performance of a contractual obligation is
not an excuse" (s 19(6)), and good-faith disclosure is not a breach of contract
(s 19(7)). Refusal costs up to $5,000 or 6 months; in a serious-incident investigation
under s 20 it rises to $25,000 or 2 years. Asserted.

### 4. Your computer can be taken without your consent, but only through four gates

s 20(2)(h) allows an officer to take possession of a computer "with the owner's
consent". Without it, the Commissioner must be satisfied it is necessary, that there
is no less disruptive method, and that after consulting the owner the benefit
outweighs the detriment, and must issue a written authorisation (s 20(5)). These wider
powers need a threat meeting the severity threshold of s 20(3), which can be met by
scale alone, "whether or not" the computers are critical infrastructure. Asserted.

### 5. Licensing discipline: caps, notice periods, and appeals that do not always suspend

Financial penalties are capped at $10,000 a contravention and $50,000 in aggregate
(s 32(2)), after at least 21 days' notice (s 33(3)). A revocation or suspension takes
effect at once if the order says continuing is undesirable in the public interest,
otherwise 14 days after service (s 30(6)). An appeal to the Minister, within 14 days
or a longer period the Minister allows, does not suspend the decision, except a
14-day order under s 30(6)(b) or a financial penalty (s 35(6)). Records are kept at
least 3 years (s 29(1)(b)); a licence runs at most 5 years (s 28). Asserted.

### 6. CII owners must report incidents in their suppliers' systems

s 14(1)(bb), annotated as from Act 19 of 2024, extends the reporting duty to prescribed incidents in a
supplier's systems that are interconnected with, or communicate with, the CII, and
(ba) to the owner's other systems even if not interconnected. A supplier's stand-alone
system is not listed. Failing to report: $100,000 or 2 years. Audits are due at least
every 2 years and risk assessments yearly (s 15(1)), with reports within 30 days of
completion (s 15(2)); continuing failures add $5,000 or $2,500 a day after conviction
(s 15(7), (8)). Asserted.

### 7. The renewal window has an edge the text leaves open

s 26(1)(c) requires renewal "not later than one month ... before the expiry" (the
"renewal period"); s 26(6) keeps the licence alive pending decision only if the
application is made "before the start of the renewal period". Read literally, an
application made exactly one month before expiry is in time but does not keep the
licence alive. The encoding counts the period in days, which a month is not. This is
an inference from the wording. Asserted as encoded.

## What would need doing before this is worth anything

- The regulations under s 48, including any for service providers and CII,
  which prescribe fees, renewal periods and the s 14 reporting periods,
  were not retrieved.
- Parts 3A to 3D, much of them new in 2024, are untouched.
- Finding 2 (s 24(3) against s 31) wants a lawyer's view.
- No guidance from the Cyber Security Agency or case law was searched.
