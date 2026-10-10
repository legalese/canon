# Corruption, Drug Trafficking and Other Serious Crimes (Confiscation of Benefits) Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation marked "version in force from 17/8/2026", deposited at
`../../registers/source-bundle/CDTOSCCBA1992.txt`. The latest amendment annotated is
S 556/2026 wef 17 August 2026 (Second Schedule); the latest amending Act annotated is
Act 21 of 2025 wef 30 December 2025.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0052** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The Act is long (85 sections and four Schedules, the Second listing hundreds of
predicate offences). This row takes what an ordinary person or business meets: the
duty to report a suspicion met at work (s 45), laundering benefits from criminal
conduct (ss 51, 54), possessing suspicious property (s 55), the payment-account
offences (s 55A), tipping-off (s 57), cash carried across the border or received from
abroad (ss 60, 62, 64) and the composition caps (s 81). Not encoded: confiscation
orders and the assessment of benefits (Parts 2 to 4A), restraint and charging orders,
production orders and search powers, financial institutions' record-keeping (ss 43,
44), the drug-dealing twins ss 50 and 53, cash transaction reports (Part 6B), and the
Schedules other than the Fourth.

## What the Act turns out to say

### 1. Laundering a scammer's money can now earn up to 12 strokes of the cane, and the burden is on you

From 30 December 2025 (Act 21 of 2025), an individual convicted on the knowing limb
of s 51(1) or s 54(1), (2) or (3) is also liable to caning of not more than 12 strokes
if the property was the benefits of a "serious scam offence" (Fourth Schedule: an
offence under s 420(2) of the Penal Code 1871) — unless, for another person's money,
the individual proves "he or she had taken reasonable steps". For one's own scam
proceeds (s 54(1)) no such escape is written. No one need have been convicted of the
scam (ss 51(10), 54(9)). The rash and negligent limbs carry no caning. Asserted.

### 2. Letting someone use your bank account is an offence even without proof you knew

s 55A (from 8 February 2024) makes it an offence to let another person "access,
operate or control a payment account" you control, to move money through your account,
or to pay or receive money for someone, without taking "reasonable steps" to find out
the purpose, the source or destination, or the other person's identity and physical
location — or where the sums are "disproportionate to A's known sources of income".
The only defence is to prove you did not know and had no reasonable ground to believe
the money was criminal benefits. Up to $50,000 or 3 years for an individual. Taking
reasonable steps defeats every circumstance except the disproportionate-income one;
the encoding reads it that way. Asserted.

### 3. Negligence is enough for a laundering offence

ss 51(1A) and 54(3A) (from 8 February 2024) add "rashly" and "negligently" limbs:
$250,000 or 5 years for rashness, $150,000 or 3 years for negligence, against $500,000
or 10 years where the person knew or had reasonable grounds to believe. A company
faces $1 million or twice the value of the benefits, whichever is higher, on any limb.
Laundering one's own benefits (s 54(1)) has no written mental element at all. Asserted.

### 4. Anyone who suspects at work must report — and a good report protects

s 45(1) binds every person, not only banks: knowledge or reasonable suspicion that came
to the person "in the course of the person's trade, profession, business or employment"
must be disclosed to a Suspicious Transaction Reporting Officer "as soon as is reasonably
practicable", whether or not the transaction completed (s 45(2)). Failure costs an
individual up to $250,000 or 3 years, others $500,000. Lawyers keep legal privilege and
arbitrators keep what they learnt in the arbitration (s 45(5)); a reasonable excuse
(s 45(6)) or a report through the employer's procedure (s 45(8)) is a defence. For
s 51, disclosure before the act counts only if the act is then done "with the consent
of the authorised officer"; disclosure after counts only if it is made "on the person's
initiative and as soon as it is reasonable" (s 51(3)). Asserted.

### 5. The border cash threshold is not in the Act

ss 60 and 62 turn on cash exceeding "the prescribed amount", which is set by
regulations that were not deposited; the encoding takes it as a parameter and the tests
use an assumed $20,000 (labelled as an assumption). Carrying more than that amount
without a report, or failing to report cash received from abroad within 5 business days
beginning on the day of receipt, costs up to $50,000 or 3 years; on conviction the
court may confiscate the part above the prescribed amount (s 64). Cash exactly at the
amount does not "exceed" it. These two offences may be compounded for up to $20,000;
other prescribed offences for up to $5,000 (s 81). Asserted.

### 6. Tipping-off has one fine for everyone

s 57 fixes $250,000 or 3 years for disclosing information likely to prejudice an
investigation or a report; unlike ss 45, 51, 54, 55 and 55A, no separate figure is
written for a person who is not an individual. Lawyers advising a client are excepted
unless furthering an illegal purpose. Asserted.

## What would need doing before this is worth anything

- The regulations fixing the prescribed amount, the compoundable offences and the
  form and timing of reports were not retrieved.
- s 46 (a prompt s 45 report means the person is "taken ... not to have been in
  possession of that information" for ss 50, 51, 53, 54 and 55A) is quoted but not
  wired into the offences.
- s 55A(2)(ii) is confined to the acquiring, possessing or using case; not modelled.
- The drug-dealing offences (ss 50, 53) and the Second Schedule's list of serious
  offences were not encoded; no case law on "reasonable steps" or "negligently" was
  searched.
