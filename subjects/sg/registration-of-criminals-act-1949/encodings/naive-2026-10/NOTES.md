# Registration of Criminals Act 1949 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to
S 608/2026 (in force 15 September 2026) shown.

**Checks:** one case file, 110 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**19 of the 527 Singapore Acts** deposited here cite it. Most of the Act is
police machinery: the register, the identification and DNA databases, the powers
to take fingerprints and body samples, removal and a Reviewing Tribunal. The part
an ordinary person meets is Part 2A, spent records. This row takes Part 2A
(ss 7A-7F, the Third Schedule as a test), the s 8 consent rule, the refusal
offences (ss 16, 27) and removal at death or age 100 (s 33). The powers in
ss 9-15 and 17-26, the court's inferences (s 28), the databases, removal on
acquittal, the Tribunal appeal and the First Schedule list of registrable crimes
are not encoded.

## What the Act turns out to say

### 1. A second conviction on the same occasion bars the record from ever lapsing

s 7C(f) disqualifies anyone with "records in the register of more than one
conviction, whether or not those convictions arise from the same particular
occasion". Two charges from one night out are enough. So is (g): any earlier
record already spent or treated as spent. A first spent record is a one-time
benefit; the second offender must apply to the Commissioner of Police under s 7D.
Asserted.

### 2. The thresholds are small, and imprisonment in default of a fine does not count

s 7C(b): imprisonment "exceeding 3 months" or a fine "exceeding $2,000"
disqualifies. A $2,000 fine or exactly 3 months does not; $2,001 or 4 months does.
s 7A(1) excludes imprisonment "in default of payment of a fine or penalty" from
"term of imprisonment", so six months in default of a $1,000 fine still leaves the
record capable of lapsing. Asserted.

### 3. A community sentence overrides everything

s 7DA(1): "Despite any provision in this Part", the record becomes spent on the
date the community sentence is completed, with no five-year wait. The same for
the Youth Court orders in s 7DA(2). This encoding reads "despite any provision"
as overriding s 7C disqualification too, so a record with a $5,000 fine (as
constructed in the fixture) becomes spent on completion; that reading is an
inference. Asserted.

### 4. Spent means you may say you have no record, except where it matters most

s 7E(1)(a): it is lawful to answer a question about one's record "as if he or she
had no record of that conviction". s 7E(2) withdraws that for investigations,
prosecutions, court proceedings (including giving evidence) and applications to
an office or profession the law bars convicted persons from. s 7E(3) restores it
for a child or young person in all four settings. Asserted.

### 5. The clock runs from release, not conviction

s 7B(4): the five years run from the "relevant date": the date of sentence for a
non-custodial sentence, the date of release from legal custody where the sentence
includes imprisonment, and the date of remission where the imprisonment was wholly
remitted or commuted. Home detention counts as legal custody (s 7A(2)). A spent
record is "not revived" by a later conviction after the period (s 7B(3)).
Asserted (the relevant date and the five-year boundary; revival is not modelled).

### 6. Children of 14 and 15 and their parents can each commit the refusal offence

s 8 "appropriate consent": 16 and over, the individual alone; 14-15, both the
individual and a parent or guardian; under 14, a parent or guardian alone.
s 27(3) makes both the 14-15 year old and the parent who refuse consent to an
invasive sample guilty; s 27(4) makes the parent of an under-14 guilty. The
penalty for refusal offences under ss 16 and 27 is a fine up to $1,000,
imprisonment up to one month, or both, and s 16(3) says the offence is committed
even if the fingerprints were taken anyway by reasonable force. Asserted.

### 7. Records go at death or age 100

s 33: the Registrar must remove all identifying information, records and DNA
information when the death is registered or the Registrar is satisfied the
individual has reached 100. Asserted.

## What would need doing before this is worth anything

- The Third Schedule is represented by seven sample offences only. Part 1B of the
  deposited Schedule is a two-column PDF table whose offence names and section
  numbers are out of step in the `.txt`; it was not used.
- Which offences are registrable crimes at all (First Schedule) is assumed, not
  tested.
- s 7B(4)'s "no longer subject to appeal" condition and s 7B(3) non-revival are
  not modelled; dates are bare numbers of years.
- The individual of 16 or over who refuses consent to an invasive sample is
  treated as committing the s 27(2) offence by inference; that case is not
  asserted.
- No police guidance, Commissioner decisions under s 7D, or case law was searched.
