# Control of Vectors and Pesticides Act 1998 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, labelled in the deposit
"version in force from 1/7/2026", with amendments to Act 15 of 2026 (in force
1 July 2026, to the definition of "owner" in s 2) shown.

**Checks:** one case file, 51 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes what a
householder, landowner, pesticide seller or pest-control firm meets: the
registration and labelling rule for pesticides and repellents (s 5), the offence of
creating conditions favourable to vectors and its presumption (s 15), permission to
breed vectors (s 16), clearing vegetation near water (s 19), who must be registered,
licensed or certified (ss 24-27), validity periods (s 30), appeal periods and whether a
decision bites pending appeal (ss 12, 13, 17, 32), entry into a dwelling-house
(s 35(3)), maximum penalties (ss 14, 23, 34, 37, 38, 45, 48), officers' liability
(s 49) and the time limit for a complaint (s 50). The registration procedure,
cancellation grounds, sampling powers, the Director-General's self-help powers, costs
recovery, arrest, composition, evidence, exemptions and regulations are not encoded.

## What the Act turns out to say

### 1. A pest-control licence survives a timely appeal; a pesticide cancellation does not

s 32(3): if a suspended or cancelled operator, technician or worker gives due notice of
appeal, the suspension or cancellation "does not take effect unless it is confirmed by
the Minister or the appeal is for any reason dismissed". The cancellation of a
pesticide's registration, by contrast, takes effect on the Director-General's date
"unless the Minister otherwise directs" (s 12(2)), and so does an order under s 17
(s 17(10)). Asserted.

### 2. Three days to appeal an order against vectors

An order under s 17 to carry out vector control work, cover tanks, drain land or stop
work may be appealed to the Minister only "within 3 days of the order" (s 17(9)). Every
other appeal in the Act runs 14 days (ss 12, 13(3), 32). Asserted.

### 3. The owner or occupier is presumed to have created the breeding condition

s 15(4): once a condition favourable to vectors is shown on premises, it is presumed,
"unless the contrary is proved", that the owner or occupier created or permitted it.
The penalty under s 23(b) is $5,000 or 3 months, then $10,000 or 6 months; failing to
obey a s 17 order carries the higher $20,000 / $50,000 scale (s 23(a)). Asserted.

### 4. Registration bites on advertising, sale and supply; the label rule only on sale

s 5(1) forbids advertising, selling or supplying an unregistered pesticide for vector
control, or an unregistered repellent. s 5(2), the approved-label rule, speaks only of
selling; reading it as not reaching a free supply is an inference from the words. s 5(3)
forbids operators, technicians and workers using unregistered pesticides, but s 5 does
not reach a householder using one at home. Asserted.

### 5. A 6-metre buffer around water that could be shaded

s 19 forbids clearing undergrowth or vegetation "within 6 metres" of a stream, seepage
or standing water that vegetation could shade, without prior approval. Treating exactly
6 metres as within the buffer is an inference. Asserted.

### 6. Provisional authorisations last 9 months, full ones 3 years

s 30: an operator's registration, a technician's licence and a worker's certificate
last 3 years; a provisional licence or certificate (granted while training, s 29(6))
lasts 9 months. A business needs full registration (s 24); technicians and workers may
work on a provisional licence or certificate (ss 25, 26). Asserted.

### 7. Smaller points

- Entry into a dwelling-house under s 35 needs the occupier's consent or at least 12
  hours' notice (s 35(3)). Asserted.
- Directors and similar officers are guilty of a body's offence unless they prove both
  absence of consent or connivance and due diligence (s 49). Asserted.
- A complaint must be made within 12 months, unless injury or danger to health still
  subsists at the date of complaint (s 50). Asserted.
- The two works offences (ss 37, 38) carry only a $10,000 fine, with no imprisonment
  and no higher repeat penalty. Asserted.
- Compoundable offences may be compounded for up to $5,000 (s 53); regulations may
  create offences up to $10,000 and $500 a day (s 60(3)). Not asserted.

## What would need doing before this is worth anything

- The regulations (prescribed standards, labels, qualifications, compoundable offences)
  were not retrieved.
- "Within 12 months" and "within 6 metres" are tested only away from day-level and
  centimetre-level edges.
- No case law was searched, including on what amounts to "proving the contrary" under
  s 15(4).
