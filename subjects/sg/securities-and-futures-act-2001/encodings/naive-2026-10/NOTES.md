# Securities and Futures Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 25 of
2021 shown in force).

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**36 of the 527 Singapore Acts** deposited here cite it, the most of any Act not yet
encoded. The deposit is about 1.8 million characters. This row takes Part 12 market
misconduct only: false trading (s 197), false statements (s 199), continuous
disclosure (s 203), insider trading (ss 214-231), and the penalties and civil
liability that follow (ss 204, 221, 232-234). Licensing, prospectuses, collective
investment schemes, takeovers, benchmarks and the Division 5 corporate-liability
provisions are not encoded.

## What the Act turns out to say

### 1. Insiders: a director can be negligent; anyone else must know

s 218 catches a **connected** person (officer, substantial shareholder, adviser) who
"knows or ought reasonably to know" the information is inside information, and
s 218(4) **presumes** that knowledge once possession is proved. s 219 catches
everyone else only if they actually **know**. There is no "ought to know" and no
presumption. A director who should have realised is liable; a dinner guest who
should have realised, but did not, is not. Asserted.

### 2. A negligent false announcement contravenes s 199

s 199(e): "knows or ought reasonably to have known". A careless market announcement
contravenes Part 12 just as a deliberate one does. Asserted.

### 3. Negligent non-disclosure is a contravention but not a crime

s 203(1) forbids failing to disclose "intentionally, recklessly or negligently".
s 203(3) then says it is not an **offence** unless it was intentional or reckless. A
negligent failure is open to a civil penalty and to investor claims, but not to
prosecution. Asserted.

### 4. Investors against an insider share the insider's profit; investors misled by a statement get their loss

s 234(1) gives traders who dealt contemporaneously with an insider a claim only if
the insider made a profit or avoided a loss, and s 234(2) and (6) cap each claim at
the profit, less what other claimants have already been awarded. An insider who made
$10,000 owes $10,000 between all of them, however much they lost.

s 234(1A), added in 2012, makes a person who made a false statement liable "whether
or not" they profited, to anyone who dealt **in reliance** on it. Under (2A)(b) that
claim has no profit cap. A company that made nothing from a misleading announcement
owes every relying investor their whole loss. Asserted.

### 5. Civil penalty and prosecution are alternatives

Under s 232 the civil penalty is up to the greater of 3 times the profit and $2
million, with a floor of $50,000 (individuals) or $100,000 (corporations). Under
ss 204(2) and 221(2), a civil penalty order or agreement bars prosecution. Under
s 233(2), a conviction or an acquittal on the merits bars a civil penalty. Asserted.

### 6. Smaller things worth recording

- **s 197(3):** a wash trade or matched orders raise a rebuttable presumption of a
  false-appearance purpose.
- **s 220:** no need to prove intention to use the inside information.
- **s 228:** knowing only your own plan to deal is not inside information.
- **s 231:** parity defence: the counterparty knew, or ought reasonably to have known.

## What would need doing before this is worth anything

- **No case law was searched.** "Generally available", "material effect" and
  "contemporaneously" are judge-made in practice.
- s 234(5)'s factors for "contemporaneous" are reduced to a flag.
- Division 5 (corporate liability for employees' contraventions) and s 236
  (claims after conviction) are not encoded.

## Source refreshed after encoding (10 Oct 2026)

This row was encoded against the deposit as it stood before the source refresh: the SSO consolidation current at the
earlier retrieval, still in git at commit da331074. The deposit has since been replaced by the consolidation current as at
9 October 2026, whose text differs. **The row has not been re-checked against the refreshed text.** Its assertions do not
read the source, so they still pass; whether the encoded provisions changed is an open question.
