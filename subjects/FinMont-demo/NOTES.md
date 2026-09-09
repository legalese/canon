# FinMont-demo — encoding notes

This subject's idiosyncrasies, in prose, for humans. No script reads this file.

Read §3 before anyone relies on the refund or liability modules.

---

## 1. What this subject is

An L4 encoding of **Commission Delegated Regulation (EU) 2018/389** — the PSD2
regulatory technical standards on strong customer authentication and common and secure
open standards of communication ("the SCA-RTS") — built to answer three questions for
FinMont, a Berlin-based payment orchestration platform for the travel industry, operating
cross-border:

| question | answered by |
| --- | --- |
| Is SCA required, or is an exemption available? | `finmont-sca-orchestration.l4` → `is SCA required`, `SCA assessment for` |
| What are the refund obligation deadlines? | `psd2-refunds-and-liability.l4` → Arts 71, 73, 77 — **secondary source, see §3** |
| Where does chargeback liability shift? | `psd2-refunds-and-liability.l4` → Art 74(2) — **secondary source, see §3 and §6** |

Modules, in dependency order:

```
types.l4                          the nouns: types and records, no rules
chapter-i-general-provisions.l4   SCA-RTS Arts 2-3
chapter-ii-authentication.l4      SCA-RTS Arts 4-5
chapter-iii-exemptions.l4         SCA-RTS Arts 10-21 and the Annex
chapter-vi-final-provisions.l4    SCA-RTS Arts 37-38 — the law-time axis
psd2-refunds-and-liability.l4     PSD2 Arts 71-77, 89-92  ⚠ secondary source
finmont-sca-orchestration.l4      the firm-facing entry points and the scope gates
cases/finmont-travel-cases.l4     17 travel scenarios, machine-asserted
registers/source-bundle/          the extracted source text and its metadata
```

Module layout follows the convention the `western-australia` corpus uses: `types.l4` for
the shared ontology, one module per structural division of the instrument (Chapter here,
Part there), a flat directory, and the source text deposited under
`registers/source-bundle/`.

## 2. What is deliberately not encoded

**Chapters IV and V of the SCA-RTS** — Arts 22 to 27 (confidentiality and integrity of
personalised security credentials) and Arts 28 to 36 (common and secure open standards of
communication, dedicated interfaces, fallback, the eIDAS certificate requirements). These
impose narrative security and interface obligations with no computable eligibility test,
and none of FinMont's three questions reaches them. Art 30(3) and (5) are named in the
encoding only because Art 38(3) gives them their own application date.

**Articles 6 to 9** are encoded only as far as they are testable. Art 4(1)'s
"two or more elements" is a countable rule and is encoded; the requirements in Arts 6, 7,
8 and 9 that measures be "adopted" to "mitigate risk" are not propositions an engine can
evaluate, and are not faked into ones.

**Scheme chargeback rules.** See §6.

## 3. ⚠ The supplied source answers only one of the three questions

The document supplied with this job — `SG Acts - SSO/CommissionDelegatedRegulationEU.pdf`,
Commission Delegated Regulation (EU) 2018/389 — **contains no refund deadline and no
liability rule.** It is a regulatory technical standard about authentication and
communication. Reading it end to end: Chapter I general provisions, Chapter II security
measures for applying SCA, Chapter III exemptions, Chapter IV credential confidentiality,
Chapter V communication standards, Chapter VI final provisions, and one Annex of reference
fraud rates. Nothing about refunds. Nothing about who bears a loss.

Both of those live in the **parent instrument**, Directive (EU) 2015/2366 (PSD2):

- refund deadlines — Art 71 (13 months to notify), Art 73 (refund by end of the following
  business day), Arts 76 and 77 (8 weeks to request, 10 business days to refund or justify);
- the liability shift — Art 74(2).

**That text was not supplied.** `psd2-refunds-and-liability.l4` is therefore encoded from
the Directive as the encoder understands it, and every rule in it carries the marker

```
UNVERIFIED — no source text supplied for this Article
```

in its `@ref`. The same marker appears on three of the five scope gates in
`finmont-sca-orchestration.l4` (§4). This is why `subject.json` declares `status: "draft"`
and why the `gates/` directory is absent: no fidelity claim is made.

**To close this:** deposit the Directive text into `registers/source-bundle/` alongside the
RTS text already there, then re-verify each marked `@ref` against it and drop the marker.
`subject.json` already names the Directive under `secondary_sources` with
`"state": "not-deposited"`; flip that when it lands. Until that happens, treat the
refund and liability outputs as a structured hypothesis to check with counsel, not as an
answer.

## 4. Scope gates, and which of them are actually in the source

`finmont-sca-orchestration.l4` decides first whether the transaction is inside the SCA
obligation at all. Five gates; only two rest on the supplied document.

| gate | source | status |
| --- | --- | --- |
| Regulation not yet in application (before 14 Sep 2019) | SCA-RTS Art 38(2) | in the supplied source |
| anonymous payment instrument | SCA-RTS recital 8 | in the supplied source |
| mail order / telephone order | PSD2 Art 97(1) | **unverified** — AR-04 |
| merchant-initiated under a stored mandate | PSD2 Art 97(1) + EBA guidance | **unverified** — AR-06 |
| one leg outside the EEA | PSD2 Art 2 + EBA guidance | **unverified** — AR-07 |

The last three carry a great deal of FinMont's traffic — call-centre bookings, post-ticketing
ancillaries, and non-EEA airline acquirers respectively — which is why they are here rather
than omitted. They are also the first three things to re-verify, and **AR-07 in particular
should not ship without local advice**: the one-leg-out position is guidance-based,
contested, and varies by market.

## 5. "Exempt" is a power, not a permission slip

Every Article in Chapter III is drafted as *"payment service providers **shall be allowed
not to apply** strong customer authentication"*. It confers a power on the payment service
provider. It does not confer a right on a merchant, an orchestrator, or a traveller.

So `SCA exempt` in this encoding means **an exemption is available on these facts**. It does
not mean no authentication will happen. On a card transaction the exemption FinMont
identifies travels to the issuer as an acquirer *request*; the issuer applies its own
Art 18 analysis and may soft-decline. FinMont must treat every returned outcome as a
request and must always be able to step up.

Two further consequences the encoding makes visible on purpose:

- `exemptions available for` returns **every** applicable exemption, not a winner. Which to
  request is commercial policy — an acquirer will usually prefer Art 18 over Art 16 to keep
  the low-value counters intact for later ancillaries — and policy does not belong in an
  encoding of law. Case 3 is the two-exemption case.
- Arts 13(1) and 14(1) are **duties**, not exemptions, and they outrank an available
  exemption on the same transaction. Case 11 is that collision: Art 18 is available and
  SCA is still required.

## 6. Chargeback is scheme law, not EU law

FinMont asked for "chargeback liability shifts". Precision matters here, because two
different systems are involved and only one of them is legislation.

**Chargeback** is a card scheme mechanism — the Visa and Mastercard rulebooks. Reason codes,
presentment windows, evidence requirements, and the long delayed-delivery windows the travel
industry depends on (a flight bought in January and flown in October) are **contractual**.
They vary by scheme, by region, and by rulebook release.

**EU law supplies the liability allocation** that those scheme rules operationalise. That is
PSD2 Art 74(2), encoded here as two distinct movements which are frequently conflated:

1. *issuer side* — where the payer's provider did not require SCA, the payer bears no loss
   unless it acted fraudulently;
2. *acceptance side* — where the payee or the payee's provider failed to accept SCA, **that
   party refunds the financial damage to the payer's provider**.

Limb 2 can bite where limb 1 does not.

**No scheme rule is encoded here, and none should be invented.** `psd2-refunds-and-liability.l4`
stops at the statutory allocation. FinMont plugs its own rulebook windows in above it, from
its own scheme documentation, as a separate module with its own citations. The seam is
deliberate: statute and rulebook change on different clocks and are owned by different people.

## 7. Currency

The SCA-RTS states every threshold in **euro** — EUR 50 and EUR 150 (Art 11), EUR 30 and
EUR 100 (Art 16), EUR 100 / 250 / 500 (Annex). FinMont settles in many currencies. The
encoding takes the euro equivalent as an input (`amount in euro`) and does no conversion:
which rate, and as at what moment, is a question the SCA-RTS does not answer. See AR-08.

## 8. Article 18 is the only provider-dependent exemption

Worth stating plainly because it drives FinMont's economics. Every other exemption in
Chapter III turns on facts about the transaction. Article 18 turns on facts about the
**acquirer's fraud book**, through the Annex table. The same EUR 480 flight is exemptible
through an acquirer at 0.008 % (Case 1), not exemptible through one at 0.09 % (Case 13), and
not exemptible through one in an Art 20 cessation however clean its current quarter
(Case 12). And no acquirer, at any fraud rate, can exempt a transaction above **EUR 500**
(Case 2) — that ceiling, not a risk score, is the binding constraint on an airline's
authentication rate.

## 9. Divergences from the subject-sidecar class

Recorded here rather than by forking the template, per the repository README.

- **Two instruments in one subject.** The class assumes one body of law. This subject
  encodes the SCA-RTS (primary, supplied) and parts of PSD2 (secondary, not supplied),
  because FinMont's three questions straddle both and separating them into two subjects
  would hide the dependency rather than record it. `subject.json` carries the second in a
  `secondary_sources` key, which the `western-australia` descriptors have no need of and
  therefore do not define; the provenance split is otherwise carried by the `UNVERIFIED`
  markers and by §3.
- **`projections/` and `gates/` are absent**, as they are throughout `western-australia`.
  No DMN or BPMN projection has been emitted and no human gate has been granted. An absent
  gate directory is an honest statement that nobody has signed; a stub would not be.
- **`cases/` and `report/` are present**, where no `western-australia` subject yet has
  either. Both are in the class contract in `subjects/README.md`; WA simply has not reached
  them. They hold real content here and were not dropped for the sake of matching a
  scaffold.
- **A per-subject `README.md`**, which the class contract does not list and WA does not
  use. Additive, for FinMont's engineers; nothing reads it.
- **Not under a jurisdiction directory.** `western-australia` subjects sit at
  `subjects/<jurisdiction>/<subject-id>/`. This one sits at `subjects/FinMont-demo/`,
  where it was asked for. If the corpus later regularises on jurisdiction folders it
  belongs at `subjects/european-union/`, and `git mv` is the whole migration.
- **A `FinMont-demo` subject id, not a law id.** Named for the firm rather than the
  instrument because the orchestration module and the scenario cases are firm-specific.
  The five law modules are firm-neutral and could be lifted into a `psd2-sca-rts` subject
  of their own unchanged if the corpus ever wants one.
