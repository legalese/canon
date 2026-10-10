# Human Organ Transplant Act 1987 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/HOTA1987.txt`. The cover says it incorporates
amendments "up to and including 1 December 2021", but the body also carries later
annotations: Act 11 of 2023 (in force 1 May 2023), Act 31 of 2023 (in force
1 December 2025, s 4(3)) and Act 19 of 2025 (in force 5 December 2025, the definition
of "licensee"). Section numbers follow the body (1 to 32). The bracketed numbers in
the deposit ([4], [15A] and so on) look like the earlier numbering; that is an
inference.

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the rules a
donor, a family, a hospital or a would-be buyer or broker meets: which organs the Act
reaches (s 2 and the Schedules), removal after death (ss 4, 5), recipient priority
(s 11), the trading ban (s 13), living donor transplants and their committees
(ss 15, 16, 17) and confidentiality (s 28). The register machinery (ss 8-10), the
selection committee (s 12), directions (s 18), enforcement and informers (ss 19-25),
the s 26 carve-outs, body-corporate liability (s 29), composition (s 30),
advertising (s 14) and regulations are not encoded.

## What the Act turns out to say

### 1. Removal after death is the default; the family is asked only for minors and the mentally disordered

s 4(1) lets a hospital's designated officer authorise removal of an organ from anyone
who died in the hospital. The bars in s 4(2) are: a registered objection, not being a
citizen or permanent resident, being under 21, or being believed mentally disordered;
and for the last two, a parent's or guardian's consent lifts the bar. Nothing in s 4
asks the family of an adult citizen who did not object. Where the Coroner has
jurisdiction, the Coroner's consent is also needed (s 5). Asserted.

### 2. Objecting costs you priority as a recipient, and withdrawing takes two years to restore it

s 11: a person who has not objected has priority over one who has, for organs removed
under s 4. Someone who withdraws an objection regains equal priority only "at the
expiry of 2 years" from the Director-General's receipt of the withdrawal, and only if
they have not objected again. Asserted.

### 3. Selling your own organ is a $10,000 offence; brokering someone else's is $100,000 or 10 years

Any contract to supply an organ or blood for valuable consideration is void
(s 13(1)) and every party commits an offence carrying $10,000 or 12 months (s 13(2)).
The heavier offence in s 13(3), $100,000 or 10 years, is written around organs "from
the body of another person", and paragraphs (a) and (d) exclude buying or negotiating
"for the purpose of transplantation to his or her body". So the donor who sells their
own organ and the patient who buys one for their own transplant meet only s 13(2);
the third-party buyer, the middleman, the seller of another's organ and the manager of
a brokering body meet s 13(3). Asserted.

### 4. Reimbursement, donor benefits and paired exchange are not "valuable consideration"

s 13(4) takes reimbursement of reasonable costs (removal, transport, storage, travel,
accommodation, domestic help, child care, lost earnings, medical care and insurance)
and Government donor-benefit schemes out of the ban. s 13(8) does the same for a
living donor who donates in return for a donation, or priority, for a recipient of
their choice, but only "if the donors have given their consent and the provisions of
Part 4A ... are complied with". The Minister may also declare classes of processed
products outside the ban (s 13(5)). Asserted.

### 5. A living donor has no minimum age, but the Part 4A rules reach only kidneys and liver

The transplant ethics committee must be satisfied the donor consented, is not mentally
disordered and, "despite the person's age", understands the procedure; and that the
consent was not bought or obtained by fraud, duress or undue influence (s 15(2)).
No age floor appears. A "living donor organ transplant" is defined (s 2) by reference
to a "specified organ", and the Second Schedule lists only the kidney and any part of
the liver. Inference, not stated in the text: living donation of any other organ is
outside s 15 altogether. The Minister may amend the Second Schedule by order (s 31).
Asserted (the lawfulness rule treats a non-specified organ as outside s 15).

### 6. A suspended committee stops all transplants, even ones already authorised

When the Director-General directs a committee under s 17(1), no authorised living donor
transplant may proceed in that hospital until the direction is complied with, unless
the Director-General allows it (s 17(2)); yet the existing authorisations "remain
valid unless rescinded" (s 17(3)). A committee needs at least 3 members, including an
outside doctor and a lay person (s 16(2)). Asserted.

### 7. Identifying a donor or recipient publicly is an offence

s 28 forbids disclosing anything by which a donor's or recipient's identity "may become
publicly known", except for enforcement, a complaint about a medical practitioner,
court orders, hospital administration or bona fide research, with consent, or where
privileged. $10,000 or 12 months. Asserted.

## What would need doing before this is worth anything

- The regulations (forms, prescribed considerations for committees under s 15(3),
  compoundable offences under s 30) were not retrieved.
- Whether "the liver" in the First Schedule includes a part of a liver is not settled
  by the text; the encoding uses one value for both.
- The s 13(3) roles are modelled as exclusive categories; a real person may fall in
  several, and the encoding does not combine them.
- No case law or Ministry guidance was searched.
