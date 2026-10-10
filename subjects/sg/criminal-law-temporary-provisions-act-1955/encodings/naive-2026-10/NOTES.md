# Criminal Law (Temporary Provisions) Act 1955 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (SSO "Current version as
at 01 Oct 2026"), with amendments to Act 18 of 2024 (in force 21 October 2024)
shown, and an Act 3 of 2021 amendment to the Second Schedule in force 1 July 2025.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the rules
with decision content: how long the Act lasts (s 1(2)); illegal strikes and
lock-outs in essential services (ss 5 to 11, First Schedule Part 1); dispersal of
assemblies (s 13); the duty to report scheduled offences (s 16, Second Schedule);
penalties, arrestability and District Court limits (ss 18, 20, 21); consent to
body samples (ss 27, 27A); detention and supervision orders (ss 30, 31, 33(3),
35, Fourth Schedule); and holding a suspect pending enquiries (s 44). Search and
boarding, evidence and trial rules, retention of samples, advisory-committee
procedure, conditions of detention and the notice forms are not encoded.

## What the Act turns out to say

### 1. The Minister can detain without trial, with the Public Prosecutor's consent, and the decision is final

s 30(1): where the Minister is satisfied a person "has been associated with
activities of a criminal nature" (the Fourth Schedule: unlicensed moneylending,
drug trafficking, secret societies, human trafficking, robbery with firearms,
murder, gang rape, kidnapping, organised crime, and attempts or conspiracies), the
Minister may, with the Public Prosecutor's consent, order detention for up to 12
months or police supervision for up to 3 years. s 30(2): "Every decision of the
Minister ... is final." The order goes to an advisory committee within 28 days
(s 31(1)), and the President may confirm, vary or cancel it (s 31(3)) and extend it
12 months at a time (s 38). Robbery without firearms is not on the list. Asserted
(limits, list, 28 days).

### 2. A "temporary" Act, renewed in five-year periods

s 1(2) says the Act "continues in force for a period of 5 years starting on
21 October 2024" [Act 18 of 2024]. The encoding reads that as ending with
20 October 2029 (an inference about the end date). The long title still calls these
"temporary provisions" for an Act dated 1955. Asserted.

### 3. No notice can make a water, gas or electricity strike legal

s 6(1) and (3) ban strikes and lock-outs in those three services outright. In the
other 29 items of the First Schedule's 31 — banking, broadcasting,
newspapers, health, public transport, ports, postal and telecoms among them — a
strike needs at least 14 days' notice signed by at least 7 workmen or 7 union
representatives (s 6(2), (5)), may not start before the date in the notice, and may
not happen while conciliation, Industrial Arbitration Court or board-of-inquiry
proceedings are pending. Notices expire after 30 days (s 6(9)); treating a strike
begun on day 31 as un-noticed is an inference. Strikes outside essential services
are outside Part 3. Asserted.

### 4. Retaliation is legal, even in the banned services

s 8: a lock-out declared in consequence of an illegal strike, or a strike in
consequence of an illegal lock-out, "shall not be deemed to be illegal". On its face
this applies to water, gas and electricity too; the encoding follows the words.
Asserted.

### 5. The striker can get bail; the person who incited or funded the strike cannot

s 18 makes every offence under the Act arrestable and non-bailable "other than an
offence under section 9" — the workman in an illegal strike or the employer in an
illegal lock-out. Instigating (s 10) and knowingly funding (s 11) carry the same
$2,000 or 12 months, but are non-bailable. Asserted.

### 6. Knowing of a firearms or explosives offence and saying nothing carries 5 years, and the accused must prove the excuse

s 16: failing to report a Second Schedule offence (Arms Offences Act ss 3, 6, 7;
explosive-substance offences under ss 3 or 4 of the Corrosive and Explosive
Substances and Offensive Weapons Act) "at the earliest possible opportunity" is
punishable by 5 years. The burden of proving there was no opportunity, or that a
report was made, lies on the accused (s 16(2)). Privileged client communications
are excluded (s 16(3)). Corrosive-only offences are not on the list. Asserted.

### 7. A District Court cannot pass the full sentence for the 10-year offences

s 21 lets a District Court try any offence under the Act but caps its sentence at
$5,000 or 5 years. The supplies offence (s 3(1)) and the subversive-document offence
(s 4(1)) carry up to 10 years, so the full term is beyond it. Asserted.

### 8. Supervisees face a mandatory minimum and doubled maximums

s 33(3): breaching a supervision obligation carries "not less than one year and not
more than 3 years". s 35: a supervisee convicted of a Third Schedule offence committed
after the order is liable to twice the ordinary maximum term "and also to caning".
Asserted.

### 9. Blood needs consent; a mouth swab does not

s 27A(5): no blood (or prescribed invasive) sample without "appropriate consent" —
the person's own at 16 and over, both the person's and a parent's from 14 to 15, a
parent's below 14 (s 27). Hair, mouth swabs, photographs and finger impressions must
be submitted to, and reasonable force may be used (s 27A(3), (4)). Asserted.

### 10. A suspect can be held 24 hours, 48 with an ASP, then 14 more days

s 44(2), (3): 24 hours; up to 48 hours in all with an assistant superintendent's
authority; a further period up to 14 days with a superintendent's. The encoding adds
the 14 days to the 48 hours (384 hours), reading "additional" literally. Asserted.

## What would need doing before this is worth anything

- s 7 also makes illegal any strike in breach of "any other written law"; the
  Industrial Relations Act 1960 and Trade Unions Act were not read.
- Applying the general penalty in s 20 to offences that state none (s 14(4), s 24(2))
  is an inference.
- Only nine services are enumerated; the First Schedule's 31 items were not encoded.
- The s 13 offence assumes the 48-hour clock runs from the declaration; further
  declarations are not modelled.
- Rules under s 49, and any Gazette amendments to the Schedules under s 28, were not
  retrieved. No case law was searched.
