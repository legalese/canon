# Holidays Act 1998 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/HA1998.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021". Its legislative history lists no
amending Act after Act 8 of 1998 (commenced 10 April 1998); the last entry is the 1999
Revised Edition.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore: it is the
Act that makes the public holidays. It is nine sections and a one-page Schedule, so
the whole operative text is encoded: ss 2, 4-9 and the Schedule. s 1 (short title) and
s 3 ("This Act binds the Government") are noted only. The Employment Act 1968
provisions that s 9 preserves are not encoded here.

Days are whole numbers with day 0 a Sunday, because no calendar library worked with
the local `l4`. That is an encoding convention, and the test years are hypothetical,
not real calendars.

## What the Act turns out to say

### 1. The Act gives no one a day off or holiday pay

Nothing in the nine sections confers a day off or pay on anyone. The Act declares
which days are public holidays (s 4(1)), and s 9 says it "does not affect the
operation of any of the provisions of the Employment Act 1968 relating to rest days,
hours of work, shift workers, holidays and other conditions of service". What a worker
is owed for a public holiday comes from elsewhere. Asserted (s 9 rule).

### 2. The Act contains no dates at all

The Schedule lists ten names and eleven days ("Chinese New Year (2 days)") and gives
no date for any of them, fixed or movable. Where the dates come from each year the Act
does not say; that they are fixed by Gazette notification is an inference, not
something the text states. Asserted (11 days).

### 3. A Sunday holiday moves to Monday; a Saturday holiday does not move

s 4(2): "if any day specified in the Schedule falls on a Sunday, the day next
following not being itself a public holiday is declared a public holiday". There is
no Saturday rule. A Schedule day on a Saturday yields no extra day unless the
President gazettes one under s 5(1). Asserted.

### 4. The Monday is skipped if it is already a holiday

"Not being itself a public holiday": if the first day of Chinese New Year falls on a
Sunday, Monday is already the second day, so the extra day is Tuesday. A Sunday
holiday whose Monday has been gazetted likewise pushes the extra day to Tuesday.
Asserted.

### 5. Two holidays on the same day get no automatic extra day

s 5(2): where "2 public holidays fall on the same day, the President **may**, by
notification in the Gazette, declare" an additional day. It is a power, not an
entitlement. If the two coincide on a Sunday, s 4(2) produces a single "day next
following" -- the encoding (on its stated simplification) gives both the same Monday,
so one day is lost unless s 5(2) is used. That reading of how ss 4(2) and 5(2) fit is
an inference. Asserted.

### 6. Only the Gazette makes a holiday; an agreed day off is not a public holiday

s 5 works "by notification in the Gazette". An employer-employee agreement giving a
different day in place of a public holiday is sheltered by s 6 ("Nothing in this Act
prevents or affects the validity of any agreement"), but it does not make that day a
public holiday under s 2. Asserted.

### 7. Nothing is invalid merely because it was done on a holiday

s 7: subject to other written law, nothing in the Act invalidates an act, judicial
proceeding, transaction or instrument done on a Sunday or public holiday. s 8 declares
the same retrospectively for anything done before 10 April 1998. Asserted.

## What would need doing before this is worth anything

- The s 4(2) rule tests "already a public holiday" against the Schedule and gazetted
  days given, not against other s 4(2) days. So two Schedule days on the same Sunday
  both point at the same Monday (finding 5); whether the second should instead move
  on to Tuesday, because Monday has become "itself a public holiday", is a reading
  this row has not settled.
- No Gazette notifications of holiday dates, no s 5 declarations, and no Employment
  Act 1968 holiday provisions were retrieved or read.
- No case law was searched.
