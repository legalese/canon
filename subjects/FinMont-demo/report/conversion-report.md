# FinMont-demo — conversion report

**Date:** 2026-09-09
**Subject:** `FinMont-demo`
**Status declared:** `draft` — the encoding exists; no claim of fidelity is made.

---

## 1. The job, and what the source could actually answer

FinMont asked for three things, and named one document:
`SG Acts - SSO/CommissionDelegatedRegulationEU.pdf`.

| asked for | in the supplied document? |
| --- | --- |
| Is SCA required / exempted? | **yes** — this is what the instrument is about |
| Refund obligation deadlines | **no** |
| Chargeback liability shifts | **no** |

The supplied PDF is Commission Delegated Regulation (EU) 2018/389, OJ L 69, 13.3.2018,
p. 23 — a regulatory technical standard on authentication and communication. Read end to
end: Chapter I general provisions (Arts 1–3), Chapter II security measures for applying SCA
(Arts 4–9), Chapter III exemptions (Arts 10–21), Chapter IV credential confidentiality
(Arts 22–27), Chapter V communication standards (Arts 28–36), Chapter VI final provisions
(Arts 37–38), and one Annex of reference fraud rates. **It contains no refund deadline and
no liability rule.**

Both live in the parent instrument, Directive (EU) 2015/2366 (PSD2) — Arts 71, 73, 76 and 77
for refunds, Art 74(2) for the liability shift — **which was not supplied**.

**Decision taken:** encode all three anyway, and carry the provenance split on the face of
the work rather than by quietly narrowing the deliverable or by quietly pretending the
second and third came from the same place as the first. Every rule sourced from the
Directive carries the marker `UNVERIFIED — no source text supplied for this Article` in its
`@ref`, lives in its own module, and is called out in `NOTES.md` §3. That is why the subject
is `draft` and not `adversarially-reviewed`.

## 2. What was encoded

| module | covers | lines |
| --- | --- | --- |
| `psd2-sca-domain.l4` | types and records only; no rules | 261 |
| `psd2-sca-rts.l4` | SCA-RTS Arts 2, 3, 4, 5, 10–21, 37, 38, Annex | 628 |
| `psd2-refunds-and-liability.l4` | PSD2 Arts 4(37), 71, 73, 74, 76, 77, 89, 90, 92 ⚠ | 371 |
| `finmont-sca-orchestration.l4` | scope gates, entry points, travel readings | 335 |
| `cases/finmont-travel-cases.l4` | 17 scenarios | 671 |

97 `@ref` citations. 82 `#ASSERT` directives. 2 `#EVAL` directives. 2 dated arms
(Art 38(2), Art 38(3)).

**The Annex table**, which is the commercially load-bearing part of the instrument and the
part most often got wrong, is encoded as two functions — `applicable exemption threshold
value in euro` (which band an amount falls in) and `reference fraud rate pct` (what fraud
rate that band demands, per transaction type) — plus `highest amount exemptible under
article 18 in euro`, which inverts it: given an acquirer's fraud rate, the largest amount it
may exempt. The inversion is what an orchestrator actually needs at routing time.

## 3. What was deliberately not encoded

- **Chapters IV and V** (Arts 22–36). Narrative security and interface obligations with no
  computable eligibility test; none of the three questions reaches them.
- **Arts 6, 7, 8, 9** beyond Art 4(1)'s countable "two or more elements". A requirement that
  measures be "adopted" to "mitigate risk" is not a proposition an engine can evaluate, and
  was not faked into one.
- **Card scheme chargeback rules.** Reason codes and presentment windows are Visa and
  Mastercard contract, not EU law, and vary by scheme, region and rulebook release. Nothing
  was invented. `NOTES.md` §6 documents the seam where FinMont plugs its own rulebook in
  above the statutory allocation.
- **"Without undue delay"** in PSD2 Art 89(1), left unquantified rather than encoded as an
  invented number of days (AR-10).

## 4. Interpretive choices

Ten, all recorded in `registers/ambiguity-register.md` with the competing reading and what
turns on the difference. The three that matter most:

- **AR-01** — Arts 11 and 16 read as `(a) AND ((b) OR (c))`. The rejected reading would
  exempt an arbitrarily large contactless transaction on the count limb alone.
- **AR-02** — Art 16's silence on Article 2 conditioning is **preserved, not repaired**.
  Arts 10, 11, 12 and 15 are expressly conditioned on Art 2; Arts 13(2) and 14(2) are
  conditioned on "the general authentication requirements"; Art 16 says neither. Repairing
  it would be legislating. FinMont should gate Art 16 in its policy layer if it wants the
  conservative behaviour.
- **AR-07** — one leg outside the EEA. **The highest-risk entry in this encoding**:
  guidance-based, contested, jurisdiction-varying, and carrying the largest share of
  FinMont's traffic by value. Recommended to be made configurable per market and defaulted
  to "SCA required" wherever local advice has not been obtained.

## 5. Two distinctions the encoding keeps structurally separate

Both are conflations that cause real production defects, and both are held apart by putting
the two halves in different functions in different modules rather than by a comment.

**Merchant-initiated is not Article 14.** Art 14 is a Chapter III exemption requiring the
*same amount* and the *same payee*. Merchant-initiated is an argument that the SCA
obligation never arose at all. They reach a similar operational result by different routes,
from different sources, and one of them is unverified. A travel deposit-then-balance
booking, and any instalment plan that moves with an exchange rate, fail Art 14 on the "same
amount" limb and fall to the weaker route (AR-05, AR-06). Case 5 asserts both halves.

**Out of scope is not exempt.** For an authorisation gate they are the same instruction, and
`is SCA required` returns `FALSE` for both. For Article 21(1)(c) reporting — the number of
transactions on which each exemption was applied — they are different facts, and a decision
log that cannot tell them apart will misreport. `SCA assessment for` keeps them distinct;
Case 4 asserts that an out-of-scope transaction reports **no** exemptions.

## 6. Verification status — what has and has not been checked

| | |
| --- | --- |
| Source text read in full | ✅ all 38 Articles and the Annex, from the supplied PDF |
| Annex table cross-checked | ✅ against the PDF, whose column layout the text extractor mangled; values re-read from the source layout |
| Citations placed on every rule | ✅ 97 `@ref` |
| Scenario assertions written | ✅ 82 |
| **Assertions machine-evaluated** | ❌ **no** |
| **Modules type-checked** | ❌ **no** |
| Directive text verified | ❌ not supplied |
| Human gate signed | ❌ none |

**No jl4 CLI was available in the environment this was built in** — the tree carries
`jl4-lsp.exe` (a language server, stdio only) and no batch runner, and no Haskell toolchain.
The L4 was therefore written against the syntax of the existing corpus modules in this
repository rather than validated by the compiler. **Expect to fix syntax on the first run.**
`subject.json` keeps `min_dated_arms` and `min_assertions` at 0 for this reason: a floor
must be a measured figure from `l4 run --json`, and none has been earned. The counts in §2
are what a first run should be reconciled against, not floors.

## 7. What to fix first

1. **Run the toolchain.** Type-check the five modules and evaluate the 82 assertions. Fix
   what breaks; raise the `checks` floors in `subject.json` from the real run.
2. **Deposit Directive (EU) 2015/2366** as a source bundle in `registers/` and discharge
   every `UNVERIFIED` marker against it — 45 occurrences, all in
   `psd2-refunds-and-liability.l4` and in three scope gates in
   `finmont-sca-orchestration.l4`.
3. **Get local advice on AR-07** per market, and make that gate configurable rather than
   fixed in the encoding.
4. **Decide AR-08** — the euro-conversion convention for a multi-currency book, and record
   the rate used alongside each decision so that boundary cases are reproducible.
5. **Sign HG1** over the content digest, once 1 and 2 are done.

Nothing in steps 1 to 5 is optional before this informs a production authorisation decision.
