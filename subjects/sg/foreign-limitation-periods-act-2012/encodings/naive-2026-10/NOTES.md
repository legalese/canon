# Foreign Limitation Periods Act 2012 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FLPA2012.txt`. It "incorporates all amendments up to
and including 1 December 2021 and comes into operation on 31 December 2021". The
Legislative History lists only Act 13 of 2012 (commenced 1 June 2012) and the 2013
Revised Edition; no amending Act is annotated.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0046**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to. No scenario has asked a sharper question yet. The Act has eight sections
and is encoded whole except s 1 (short title) and s 2 ("country" includes a State or
territory). It does not say which country's law governs a matter, and it contains no
limitation periods of its own. Both are inputs here.

## What the Act turns out to say

### 1. A claim with no foreign limitation period is never out of time in Singapore

s 6(1)(b): where the governing foreign law has no limitation period, the "law relating
to limitation" is "the rule that such proceedings may be brought within an indefinite
period", and s 3(1)(b) shuts out Singapore's own period. A foreign-law claim brought 30
years on is not time-barred, even though a Singapore period would have run long ago.
Asserted.

### 2. Whichever law governs the claim also sets the deadline, both longer and shorter

s 3(1): where a Singapore court must apply another country's law to a matter, that
country's limitation law applies and Singapore's "does not so apply". A foreign-law
claim with a 3-year foreign period, brought after 4 years, is barred even though the
6-year Singapore period used in the cases (an input, not a figure from this Act) would
allow it. A 10-year foreign period lets a claim brought after 8 years go ahead. s 3(2)
extends this to a foreign law "considered for the purpose of actionability under a
choice of law rule". Asserted.

### 3. Extensions for a party's absence from a country are struck out

s 4(3): any part of the foreign law that extends or interrupts the period because a
party is absent from a jurisdiction "is to be disregarded". Other foreign extensions
and interruptions do count (s 6(1)(a)), as does a foreign court's discretion, which a
Singapore court is to exercise as the foreign courts would in comparable cases (s 3(4)).
The absence extension comes back only where disregarding it would conflict with public
policy or cause undue hardship to a party (s 4(4)). Asserted.

### 4. Undue hardship to a party is a deemed breach of public policy

s 4(1) disapplies s 3 to the extent that it would conflict with public policy. s 4(2)
says applying it conflicts with public policy "to the extent that its application would
cause undue hardship" to a party or possible party. The encoding then applies Singapore's
period. That step is an INFERENCE: the Act does not say what applies instead. The "to
the extent" partial displacement is not modelled. Asserted.

### 5. Singapore law decides when proceedings were started

s 3(3): even under a foreign period, "the law of Singapore determines whether, and the
time at which, proceedings have been commenced". The elapsed time in every case is
measured that way. Whether a claim brought exactly on the last day is in time is not
in the Act. The encoding treats it as in time (elapsed time must exceed the period),
which is a modelling choice. Asserted.

### 6. Old claims stay under the old rule, and a foreign judgment on time is a judgment on the merits

s 8: the Act does not affect proceedings or arbitrations commenced before 1 June 2012.
It does not apply to a matter whose Singapore period had expired before that date, so a
longer foreign period does not revive it. s 5: a foreign court that decided a matter by
reference to a law relating to limitation is "deemed to have determined it on its
merits". s 7: the Act binds the Government, and s 3(5) excludes the foreign country's own
choice-of-law rules (so no referral back). Neither changes the result in the cases.
Asserted.

## What would need doing before this is worth anything

- The choice-of-law rules that decide when a foreign law governs a matter are outside the
  Act and were not encoded. They are the hard part of any real case.
- The Limitation Act 1959 periods were not read. The Singapore period in the cases is an
  input.
- What follows from s 5 (for example, whether a claim can be brought again after a
  foreign dismissal) depends on the law on recognising foreign judgments, which was not
  encoded.
- Partial displacement under s 4(1) ("to the extent") is all or nothing here.
- No case law on "undue hardship" or public policy was searched.
