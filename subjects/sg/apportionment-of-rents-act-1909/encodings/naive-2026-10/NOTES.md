# Apportionment of Rents Act 1909 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/ARA1909.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31 December
2021". The latest amendment annotated in the text is [17/2001].

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers requirement **REQ-0040** in `subjects/sg/requirements.jsonl`. It is in
Tier 2 of the remaining Singapore Acts, which are ordered by how often they touch
everyday life. The requirement asks what the Act decides for a person or business it
applies to. No scenario has asked it anything more specific yet. The Act has only nine
sections, so this row covers ss 2 to 8 almost entirely. The following are left out: s 1;
s 9 (the Record of Apportionment of Rents, whose entries are prima facie evidence); the
seal and "under his hand" formalities; and how the Collector works out each
subdivision's rent. The Act gives no formula for that, so the determined amount is an
input to the encoding.

## What the Act turns out to say

### 1. A rent can only be rounded up, so subdividing can increase the total rent to the Government

s 3(3) says: "The minimum rent in respect of any subdivision shall be $1 and any fraction
of 50 cents shall count as 50 cents." Each subdivision's rent goes up to the next 50-cent
step and is never less than $1. Suppose a $1 lease rent is split three ways. Each share of
about 33 cents becomes $1, so the Government collects $3. The encoding reads "fraction of
50 cents" as "round up to the next 50 cents", which is an inference from the wording. The
three-way split is an illustration and was not computed as one case. Asserted: 30 cents
gives $1, 120 cents gives $1.50, 151 cents gives $2, 1001 cents gives $10.50, 2575 cents
gives $26.

### 2. Once the order is made, the seller can be free of the rent covenant, but only through duly registered deeds

s 8(b)(i) discharges the lessee's or grantee's covenant where they have "by duly
registered deeds assigned or conveyed the entirety of the land". If they keep part of the
land, s 8(b)(ii) limits the covenant to the rent apportioned to the part they keep. Some
cases fit neither limb, for example a transfer of the whole land by deeds that were not
duly registered. The encoding then leaves the covenant unchanged, which is an inference
from the Act's silence. Under s 8(c), any private covenant by a subdivision holder to pay
the lessee a share of the rent is discharged. Asserted.

### 3. The order binds people who were never served

s 7(3) makes the order "final and binding on every lessee or grantee and holder of a
subdivision, notwithstanding that notice may not have been served on all the persons
entitled". If a person cannot be found, s 5 allows service by posting the notice on the
land **and** at the Singapore Land Authority's office. Posting in only one of those places
is not good service. Asserted.

### 4. The duty to notify is short, has several parts, and covers only lessees and grantees

Under s 3(1), a lessee or grantee has **one month** after obtaining subdivision
permission to tell the Collector in writing. The notice must include the approved plan
and the beneficial owners' particulars. If any one of these is missing, or the notice is
late, the offence in s 3(5) is committed: a fine of up to $500, no imprisonment, and no
reasonable-excuse defence in the text. Under the s 2 definition, "lessee" includes an
assignee of the *entirety* of the land and the lessee's legal representatives. It does not
include an assignee of only part of the land, so the encoding treats that person as
outside the duty. That is a reading of the definition. Asserted.

### 5. If nobody notifies, the Collector can apportion anyway

s 4 allows the Collector to determine the rents of their own motion when land "has been
subdivided and no notification ... has been given". The rest of the procedure then runs
as if the owner had notified. Objections must be made in writing within one month of
service (s 6). The Collector must consider them (s 7(2)) and may not make the order until
one month after the *last* notice was served (s 7(1)). Once the order is made, any unpaid
rent for the current year is payable "forthwith" (s 8(a)(i)). Asserted.

## What would need doing before this is worth anything

- No search was made for case law or the Collector's practice on s 3(3) rounding or on
  how rents are apportioned.
- The Land Revenue Collection Act 1940 (the meaning of "Collector" and how rent is
  recovered under s 8(a)(iii)) and the Planning Act 1998 (subdivision permission) were not
  read.
- "Within one month" is modelled as a yes/no fact. The encoding does not calculate dates.
