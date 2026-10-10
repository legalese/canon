# Corporate Service Providers Act 2024 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** the Act as enacted (No. 22 of 2024), deposited at
`../../registers/source-bundle/CSPA2024.txt`. It is not a 2020 Revised Edition
consolidation: the retrieval record calls it the SSO "Current version as at 01 Oct
2026", and no amendment annotations appear in the text. The commencement date is
left to Gazette notification (s 1) and is not in the deposit.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes what a
corporate service provider, a qualified individual or their client meets: what
counts as a corporate service (s 2), the ban on unregistered business and the
deemed registration of accounting entities (s 7), the transitional grace (s 42),
the renewal window and mandatory refusals (ss 8 to 11), the 14-day notice duty
(s 12), who must provide the service (s 14), nominee directors (s 16), customer due
diligence (s 17), regulatory action (ss 19, 21), appeals (s 23), the offence
penalties and composition (ss 7, 12, 16, 17, 25, 27). Administration, s 13
condition changes, deemed qualified individuals (s 15), the s 18 and s 20
cancellation grounds, s 22 procedure, interest and recovery (s 28), officers'
liability (ss 29, 30), the consequential amendments and the filing-agent
transitional rules (ss 43 to 45) are not encoded. Everything the Act leaves to
regulations (who is a "qualified individual", the prescribed course, the
fit-and-proper factors, the due diligence measures themselves) is a bare input.

## What the Act turns out to say

### 1. Skipping due diligence to avoid tipping off still means losing the customer

s 17(3) lets a provider "choose not to perform or complete" customer due diligence
where it suspects money laundering and believes the measures would tip off the
customer, unless a prescribed s 17(2) bar applies. But s 17(4) then applies
because it "chooses not to complete": it must decline or terminate the service,
decide whether to make a disclosure under the CDSA s 45 or the Terrorism
(Suppression of Financing) Act, and record why. The exception spares the
questions, not the customer. Asserted.

### 2. Only a section 19 cancellation bars reapplying for two years

s 9(1)(f) and s 11(1)(c) refuse an applicant whose previous registration was
cancelled under s 19(2) or (3) (s 21 for individuals) "less than 2 years before".
A cancellation under s 18 (for instance because a key appointment holder is not fit
and proper) is not in the list, though unfitness is separately a mandatory refusal
ground under s 9(1)(c). Asserted (12 months barred, 36 months not; 23 and 25 months
for an individual).

### 3. A listed company's nominee shareholder, and a bare tax return, are not corporate services

Paragraph (d) of "corporate service" excludes acting as nominee shareholder of a
corporation listed on an approved exchange. Paragraph (e) covers an accounting
service only where a "designated activity" (dealing in real estate, managing client
money or accounts, forming or running legal persons) is carried out, so preparing a
tax return is not, while managing client money in an accounting engagement is.
Foreign corporations count (s 2(2)). Asserted.

### 4. Accounting entities are registered without applying, but only for one service

s 7(2) treats an accounting entity as registered for "carrying out any designated
activity in relation to the provision of any accounting service by the accounting
entity", until suspended or cancelled. An accounting firm offering registered office
addresses has no such deeming and needs ordinary registration. s 7(4): $50,000 or
2 years, plus $2,500 a day after conviction. Asserted.

### 5. Regulatory action reaches only breaches that are not offences

s 19(1) and s 21(1) apply to breaches of registration conditions (not for a deemed
registrant) and of requirements "the contravention of or non-compliance with which
is not an offence". Offences go to court; the rest to the Registrar, who may cancel,
suspend up to 12 months, restrict the electronic transaction system, impose up to
$25,000 (provider) or $10,000 (individual) per contravention, or censure. s 14 (the
service must be provided by or under a registered qualified individual) creates no
offence, so by inference its breach is a s 19 matter. Asserted, except the s 14
inference.

### 6. Composition is capped at $20,000 whatever the fine

s 27(1): a prescribed compoundable offence may be compounded for at most the lower of
half the maximum fine and $20,000. For the $100,000 offences (ss 16, 17) the cap is a
fifth of the fine. Asserted for ss 7 and 12.

### 7. Smaller points

- Renewal may not be sought earlier than 60 days before expiry (ss 8(2), 10(2)).
  Asserted.
- A non-deemed registered person must notify changes in particulars within 14 days;
  $10,000 (s 12). Asserted.
- A provider arranging a nominee director must be satisfied the person is fit and
  proper, having taken reasonable steps to check disqualification (s 16); $100,000.
  Treating (2) as a condition of the satisfaction is an inference. Asserted.
- An appeal to the Minister is within 30 days, does not suspend the decision unless
  the Minister directs, and the Minister's decision is final (s 23). Asserted.
- An existing business that did not need filing-agent registration may continue for
  6 months after s 7 commences, or until its application made within that time is
  decided (s 42). Asserted.

## What would need doing before this is worth anything

- The regulations (qualified individual criteria, prescribed course, fit-and-proper
  factors, customer due diligence measures, compoundable offences, appeal period
  under s 23(1)) were not retrieved.
- s 23(1) refers to a "prescribed period" for appeal while s 23(2) says 30 days; the
  encoding uses the 30 days only.
- Deemed registration ending on cancellation (s 7(2)) is not modelled; only
  suspension is.
- The commencement date and whether any amendments have been made were not checked.
