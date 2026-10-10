# Hotels Act 1954 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited as `HA1954.txt`. The deposit says it
"incorporates all amendments up to and including 1 December 2021 and comes into
operation on 31 December 2021"; the retrieval record calls it the current version
as at 1 October 2026. No later amendment is annotated; the last amending Act in the
legislative history is Act 7 of 1996. The arrangement of sections at the top of the
deposit is out of step by one with the body; the body's numbers are used throughout.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0061**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. The Act has 17
sections, so the row takes almost everything an operator, owner or guest meets: the
definition of hotel (s 2) and the presumption in a prosecution (s 14), registration
(ss 5, 6), the manager's licence (s 7), suspension and cancellation (ss 8, 9), appeal
(s 11), exemption (s 12), liability for staff (s 13), entry and inspection (s 15), and
the offences and penalties (s 16). Not encoded: the Board and its officers (ss 3, 4),
reclassification (s 10) beyond its absence from the appeal list, the regulation-making
power (s 17), and the regulations themselves (fees, forms, classes, prescribed licence
conditions, exemptions), which were not retrieved.

## What the Act turns out to say

### 1. Short lets are presumed to be hotels, whatever their size

s 2 defines a hotel (beyond boarding houses, lodging houses and guesthouses) as
premises with "not less than 4 rooms or cubicles" where people lodge for hire and
"any domestic service is provided". But s 14 presumes, in any prosecution, that
premises whose rooms are let "for periods of less than one week constitute a hotel",
until the contrary is proved. The presumption names no room count and no service. A
two-room flat let by the night with no service is not a hotel under s 2, yet a court
treats it as one unless the defence proves otherwise. Asserted.

### 2. A licence lasts until 31 December, however late it is granted

s 7(5)(b): every licence is granted "on or after 1 January in every year and shall
expire on 31 December next following the date of grant". There is no fixed term: a
licence granted on 1 January runs 365 days, one granted on 15 December runs 17.
Asserted.

### 3. The Board can always say no, without reasons, and the Minister has the last word

The s 6 conditions (not a disorderly house, structurally adapted, sanitation,
situation, standard for the class) and the s 7(6) conditions (not a disorderly house,
good character, fit and proper) are only preconditions: ss 5(4) and 7(7) let the Board
refuse "without assigning any reason therefor". The encoding states that no applicant
is ever entitled to registration. Appeal lies to the Minister within 10 days, "whose
decision shall be final and conclusive" (s 11). Asserted.

### 4. Not every adverse decision can be appealed

s 11 lists refusal to register, refusal to grant or renew a licence, and suspension or
cancellation "under section 8". It does not list the mandatory cancellation on a
conviction under Part 11 of the Women's Charter 1961 (s 9, where the Board "shall"
cancel both licence and certificate) or reclassification to a lower class (s 10).
Asserted.

### 5. A s 8 sanction waits 10 days, and an appeal holds it until the Minister confirms

s 8(4): no s 8 suspension or cancellation takes effect "until the expiration of 10
days"; s 8(5): if appealed within those 10 days it waits until the appeal is determined
"and the Minister confirms". For an insanitary hotel the remedy period in the notice
must be "not being less than one month" (s 8(2)). Counting the 10 days from the day
after the decision is an inference; the cases avoid the boundary day. Asserted.

### 6. Making a false statement needs no knowledge; using one does

s 16(6) punishes anyone who "makes any declaration or statement which is false in any
material particular or knowingly utters, produces, or makes use of" one. On the words,
"knowingly" governs only uttering, producing and using. Asserted (a court may read
mens rea into making; that is not in the text).

### 7. A first offence carries a fine only

s 16(7): a fine not exceeding $2,000; only for a "second or subsequent offence" is
imprisonment of up to 6 months available. The court may also cancel or suspend the
certificate and cancel the licence (s 16(8)). Asserted.

### 8. The licensee answers for anyone who appears to work there

s 13(2) deems "every person who appears to be employed in any hotel registered under
this Act" to be the licensee's servant, so the licensee bears the same pecuniary
penalty for their acts; the servant stays liable (s 13(3)). Inspectors may enter "at
any time of the day or night without previous notice" (s 15(1)), but only the
chairman, a Board member or someone the chairman authorised in writing. Asserted.

## What would need doing before this is worth anything

- The regulations (fees, classes, prescribed licence conditions and exemptions) were
  not retrieved; s 12 exemptions and s 16(5) licence conditions are bare booleans.
- Whether the 4-room, hire and service qualifiers in s 2 also govern boarding houses,
  lodging houses and guesthouses is a reading; the encoding treats the named kinds as
  hotels in their own right.
- The relation to the Women's Charter Part 11 offences and to short-term rental rules
  elsewhere (planning law) was not read. No case law was searched.
