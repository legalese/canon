# Gambling Duties Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** the Act as enacted (No. 1 of 2022), which SSO labels "Current version
as at 01 Oct 2026". The only amendment annotation in the body is Act 14 of 2022
(with effect from 29 July 2022), in s 43. It is not a Revised Edition.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**5 of the 527 Singapore Acts** deposited here cite it. This row takes what is
taxable, the revenue the duty is worked out on, who pays, the time limits, penalty
tax, priority in insolvency, the offences and their penalties, and composition: ss 3,
5-11, 13, 14, 18, 19, 27-30 and 37. Assessment to best judgment, agents for recovery,
powers of entry and information, administration, liability of corporations and
partnerships, confidentiality, and the amendments to other Acts are not encoded.

## What the Act turns out to say

### 1. The Act sets no rate of duty at all

s 5(1) charges duty only on undertakings "that [are] prescribed"; s 6(1)(b) charges it
only on revenue that "is prescribed in Regulations"; s 6(2) applies "the rate of
gambling duty prescribed". Every number that decides how much duty is paid lives in
Regulations, which were not retrieved. The encoding takes the rate as an input. What
the Act does fix: GST is disregarded (s 6(4)), and revenue from an unlawful gaming
machine bears no duty (s 6(5)). Asserted.

### 2. Casinos are outside it, and so is unlawful gambling

The duty attaches to an *authorised* betting operator, an *authorised* lottery
promoter, an authorised person providing a gaming service, and gaming machines in
*non-casino* premises (s 5(1)). Each definition excludes a casino licence holder for
what the casino licence covers (ss 2(1), 3(5), 4(4)). Unlicensed betting is not
dutiable under s 5 because its operator is not authorised (this follows from the
definitions; the Act does not say it in terms). Asserted.

### 3. For gaming machines, the licensee pays, not the owner of the premises

s 7(3): duty on gaming machines is payable by the person licensed (or exempt) to keep
them "regardless that the person may not be the proprietor of those premises".
Liability survives ceasing to be authorised for as long as the duty is unpaid
(s 7(6)). Asserted.

### 4. Penalty tax climbs 5% a month to a 50% ceiling — on one reading

s 14(1): 5% of the unpaid duty; a further 5% if still unpaid a month later; a further
5% for every complete month after that. s 14(2): "the total additional penalty tax
must not exceed 50%". The encoding reads the ceiling as covering the whole penalty
(reached at nine complete months late). The word "additional" could instead mean
only the further amounts, which would allow 55% in all. This is a reading, not
something the text settles. Asserted on the first reading.

### 5. Five years, except for fraud — and the objection window is only 14 days

An assessment cannot be made more than 5 years after the period ends, but may be made
"at any time" for fraud or wilful default (s 9(5), (6)). A demand for a short levy must
come within 5 years of payment unless there was fraud or evasion (s 11(2)(c), (3)), and
amounts up to $200 may be waived (s 11(4)). A refund claim must be made within 5 years
of the overpayment (s 19(2)). An objection to a liability notice must be made within
14 days (s 10(2)(b)); an appeal to the Minister within 30 days (s 10(4)). The Minister's
decision is final (s 10(6)), and an appeal does not suspend the notice (s 10(8)).
Asserted.

### 6. Special fines of 2 and 4 times the duty, and a presumption of intent

A misleading return carries a special fine of twice the duty underpaid on top of the
ordinary fine ($5,000 or 2 years for an individual, $10,000 otherwise) (s 28(3), (4)).
Evasion carries four times the duty plus $12,500 or 5 years, or $25,000 (s 30(1),
(2)). Once a false entry is proved, intent to evade is presumed until the contrary is
proved (s 30(3)). A late return is a $5,000 offence only if the failure was
intentional or negligent (s 27). Asserted.

### 7. The non-possession defence is attached to giving false information

s 29(2) gives a defence, proved on a balance of probabilities, of not possessing the
document and having taken all reasonable steps to get it. The text attaches it to
"an offence under subsection (1)" (giving false or misleading information), not to the
failure-to-comply offence in s 29(4), which has its own "without reasonable excuse".
Encoded as the text reads. Asserted.

### 8. Composition is capped at the lower of half the maximum fine and $5,000

s 37(1), for offences prescribed as compoundable. Asserted.

## What would need doing before this is worth anything

- The Gambling Duties Regulations (the prescribed undertakings, revenue bases, rates,
  accounting periods and return deadlines) must be retrieved; without them nothing
  here computes a real duty.
- The reading of the 50% ceiling in s 14(2) needs checking against IRAS practice.
- Day counting (inclusive or exclusive) for the 14-, 15- and 30-day periods, and the
  boundary of "within 5 years starting the date of the overpayment", are not settled
  by the text; the encoding uses whole numbers and stays away from the edges in s 19.
- No IRAS guidance or case law was searched.
