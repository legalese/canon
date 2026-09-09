# FinMont-demo

**PSD2 strong customer authentication, encoded in L4 for a travel payment orchestrator.**

Commission Delegated Regulation (EU) 2018/389 — the SCA-RTS — encoded to answer, at
authorisation time and with a citation behind every answer:

- **Is SCA required, or is an exemption available?**
- **What are the refund obligation deadlines?** *(secondary source — see below)*
- **Where does chargeback liability shift?** *(secondary source — see below)*

Built for FinMont, a Berlin-based payment orchestration platform for the travel industry,
for cross-border regulatory compliance.

> **Status: `draft`.** The encoding exists; no claim of fidelity is made, and no human gate
> has been granted. Read [`NOTES.md`](NOTES.md) §3 before relying on the refund or liability
> answers — the document supplied for this job answers only the first of the three
> questions.

## Layout

Follows the subject-sidecar shape used by the [`western-australia`](../western-australia/)
corpus: `types.l4` for the shared ontology, one module per structural division of the
instrument, a flat directory, and the source text deposited under `registers/source-bundle/`.

```
subject.json                            the descriptor
NOTES.md                                idiosyncrasies and divergences        ← read §3
SOURCE-LICENSE.md                       the terms the quoted legal text carries
types.l4                                the nouns: types and records, no rules
chapter-i-general-provisions.l4         SCA-RTS Arts 2-3
chapter-ii-authentication.l4            SCA-RTS Arts 4-5
chapter-iii-exemptions.l4               SCA-RTS Arts 10-21 and the Annex
chapter-vi-final-provisions.l4          SCA-RTS Arts 37-38 — the law-time axis
psd2-refunds-and-liability.l4           PSD2 Arts 71-77, 89-92       ⚠ secondary source
finmont-sca-orchestration.l4            the firm-facing entry points and the scope gates
cases/finmont-travel-cases.l4           17 travel scenarios, machine-asserted
registers/source-bundle/                the extracted source text and its metadata
registers/ambiguity-register.md         every interpretive choice, and what turns on it
report/conversion-report.md             what was encoded, what was not, what to fix first
```

## The three entry points

All in `finmont-sca-orchestration.l4`, all taking one `Assessment Input` bundle:

| call | returns | use |
| --- | --- | --- |
| `is SCA required` | `BOOLEAN` | the authorisation gate |
| `SCA assessment for` | outcome + every available exemption + a reason string | the decision log |
| `exemptions available for` | `LIST OF SCA Exemption`, in Article order | exemption-preference policy |

```
#EVAL `SCA assessment for` `case 1`
```

## Three things to know before wiring it in

**1. "Exempt" is a power, not a permission slip.** Every Chapter III Article is drafted as
*"payment service providers shall be allowed not to apply strong customer authentication"* —
a power of the payment service provider, not a right of a merchant. `SCA exempt` means *an
exemption is available on these facts*. On a card transaction it travels to the issuer as an
acquirer **request**; the issuer decides and may soft-decline. Always be able to step up.
(`NOTES.md` §5.)

**2. Article 18 depends on your acquirer, not on the transaction.** It is the only exemption
in the Regulation that turns on the acquirer's fraud book, through the Annex table. The same
EUR 480 flight is exemptible through an acquirer at 0.008 % (Case 1), not through one at
0.09 % (Case 13), and not through one in an Article 20 cessation (Case 12). And **no
acquirer, at any fraud rate, can exempt a transaction above EUR 500** (Case 2) — that
ceiling, not a risk score, is the binding constraint on an airline's authentication rate.

**3. Chargeback is scheme law; only the liability allocation is EU law.** Visa and
Mastercard rulebook windows and reason codes — including the long delayed-delivery windows
travel depends on — are contractual and are **not encoded here**. What is encoded is PSD2
Art 74(2), the statutory allocation those rules operationalise. FinMont plugs its own
rulebook in above this, from its own scheme documentation. (`NOTES.md` §6.)

## Travel shapes the cases cover

| case | shape | answer |
| --- | --- | --- |
| 1 | EUR 480 online flight, clean acquirer | exempt — Art 18 |
| 2 | the same at EUR 620 | **required** — above every Annex band |
| 3 | EUR 25 seat selection, counters intact | exempt — Arts 16 *and* 18 |
| 4 | call-centre booking | out of scope — MOTO ⚠ |
| 5 | post-ticketing change fee | out of scope — merchant-initiated ⚠ |
| 6 | rail ticket machine, EUR 220 | exempt — Art 12, no ceiling at all |
| 7 | contactless at the gate, EUR 35 | exempt — Art 11 |
| 8 | the same with both counters exhausted | **required** |
| 9 | non-EEA airline acquirer | out of scope — one leg out ⚠ **contested** |
| 10 | corporate lodge card, EUR 4,000 | exempt — Art 17, no ceiling |
| 11 | traveller stores a card on file | **required** — Art 13(1) beats an available Art 18 |
| 12 | Case 1 through an acquirer in cessation | **required** — Art 20(2) |
| 13 | Case 1 through a 0.09 % acquirer | **required** — its Art 18 ceiling is EUR 100 |
| 14 | Case 1 with an abnormal payer location | **required** — Art 18(2)(c)(v) |
| 15 | Case 1 under the rules effective June 2019 | out of scope — Art 38(2) dated arm |
| 16 | disputed EUR 900 booking, payee refused SCA | liability shifts to the payee side ⚠ |
| 17 | tour operator's variable balance | Art 76 refund due ⚠ |

⚠ = rests on the Directive or on supervisory guidance, neither supplied with this job. See
[`registers/ambiguity-register.md`](registers/ambiguity-register.md).

## Before this goes near production

In order, from [`report/conversion-report.md`](report/conversion-report.md):

1. Deposit the Directive (EU) 2015/2366 text and discharge the `UNVERIFIED` markers.
2. Run the toolchain — nothing here has been machine-evaluated; no jl4 CLI was available in
   the environment this was built in — and raise the `checks` floors in `subject.json` from
   a real run.
3. Get local advice on **AR-07** (one leg outside the EEA) per market, and make that gate
   configurable rather than fixed.
4. Have a domain expert sign HG1 over the content digest.
