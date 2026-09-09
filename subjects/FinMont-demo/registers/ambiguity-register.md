# FinMont-demo — ambiguity register

Every interpretive choice the encoding makes, the competing reading it rejected, and what
turns on the difference. An entry here is not a defect; it is a place where the source text
admits more than one construction and the encoding had to pick one on its face.

Entries are cited from the `.l4` modules by id (`AR-01` and so on).

| id | site | status |
| --- | --- | --- |
| AR-01 | Arts 11 and 16 — the "(a) and (b); or (c)" conjunction | reading taken |
| AR-02 | Arts 13, 14 and 16 — inconsistent Article 2 conditioning | source silence preserved |
| AR-03 | Arts 11 and 16 — do the counters include the current transaction? | reading taken |
| AR-04 | PSD2 Art 97(1) — mail order and telephone order | unverified, outside supplied source |
| AR-05 | Art 14 — "the same amount" and variable travel instalments | reading taken |
| AR-06 | PSD2 Art 97(1) — merchant-initiated transactions | unverified, outside supplied source |
| AR-07 | PSD2 Art 2 — one leg outside the EEA | unverified, contested, highest risk |
| AR-08 | Chapter III and Annex — euro thresholds in a multi-currency book | source silence, input deferred |
| AR-09 | PSD2 Art 4(37) — "business day" | modelled approximately |
| AR-10 | PSD2 Art 89(1) — "without undue delay" | left unquantified |

---

## AR-01 — Articles 11 and 16: how the three conditions bind

**The text.** Article 11 reads:

> (a) the individual amount ... does not exceed EUR 50; **and**
> (b) the cumulative amount ... does not exceed EUR 150; **or**
> (c) the number of consecutive ... does not exceed five.

Article 16 has identical structure at EUR 30 / EUR 100 / five.

**The ambiguity.** Two readings are available on the face of the drafting:

1. `(a) AND ((b) OR (c))` — the individual ceiling always applies; the provider may run
   either the value counter or the count counter.
2. `((a) AND (b)) OR (c)` — the count limb stands alone, with no amount ceiling.

**Reading taken:** (1).

**Why.** Reading (2) would let a EUR 900 contactless tap ride limb (c) with no amount cap at
all, which the Article's heading ("Contactless payments at point of sale"), recital 9's
framing of exemptions as based on "the level of risk, amount, recurrence and the payment
channel", and the entire structure of Chapter III do not support. Reading (1) is also the
settled market and supervisory understanding.

**What turns on it.** Under reading (2) Art 11 would exempt arbitrarily large contactless
transactions for the first five taps after each authentication. Encoded in
`psd2-sca-rts.l4`, `article 11 exemption is available` and `article 16 exemption is available`.
Tested by Cases 7 and 8.

---

## AR-02 — Which exemptions are conditioned on Article 2, and which are not

**The text.** Articles 10, 11, 12 and 15 each say "subject to compliance with the
requirements laid down in Article 2". Articles 13(2) and 14(2) say "subject to compliance
with the general authentication requirements" — the same idea in different words, without
the cross-reference. **Article 16 says neither.** Article 17 says neither. Article 18
instead relies on Art 2 through its own paragraph 2(c).

**Reading taken.** Articles 13 and 14 are treated as conditioned on Article 2 ("the general
authentication requirements" being read as Article 2, which is the only place the
Regulation lays them down). **Article 16's silence is preserved, not repaired**: the
encoded Art 16 predicate takes no Article 2 argument.

**Why.** Repairing Art 16 would be legislating. The omission may well be a drafting
oversight — Art 21(1) requires monitoring in order to use *any* of the Arts 10 to 18
exemptions, which points the other way — but the encoding's job is to carry the text's own
shape, with the divergence recorded here where a reviewer can see it.

**What turns on it.** A provider without Article 2 transaction monitoring can, on the face
of this encoding, still take the Art 16 low-value exemption but not the Art 11 contactless
one. If FinMont wants the conservative behaviour, it should gate Art 16 on Article 2 in its
own policy layer rather than by editing the encoded Article.

---

## AR-03 — Do the Article 11 and 16 counters include the transaction being assessed?

**The text.** Art 11(b) counts "previous contactless electronic payment transactions
initiated ... from the date of the last application of strong customer authentication".
Art 16(b) counts "previous remote electronic payment transactions initiated by the payer
since the last application of strong customer authentication".

**Reading taken.** "Previous" excludes the transaction now being assessed. The
`Exemption Counters` fields are named accordingly
(`cumulative amount in euro of previous transactions since SCA was last applied`).

**What turns on it.** One transaction of headroom at every boundary. A payer whose previous
remote transactions total exactly EUR 100 may still take a further exempt transaction under
Art 16(b) on this reading, and may not on the other. FinMont's counter service must feed
these fields with pre-transaction figures; feeding post-transaction figures silently shifts
every boundary by one.

---

## AR-04 — Mail order and telephone order

**Status: unverified. The governing text was not supplied with this job.**

**The position taken.** A mail order or telephone order is not an electronic payment
transaction initiated by the payer, and does not engage Art 97(1) of Directive (EU)
2015/2366. It is therefore outside the SCA obligation entirely — not exempt from it.

**Basis.** PSD2 Art 97(1) and recital 95; long-standing supervisory understanding.

**What turns on it.** Every call-centre booking FinMont processes. If the position is wrong,
those transactions need SCA and there is no exemption in Chapter III that fits them.
Encoded as `out of scope because the order is mail order or telephone order`. Case 4.

---

## AR-05 — Article 14: "with the same amount"

**The text.** Art 14(1): "a series of recurring transactions **with the same amount and with
the same payee**".

**Reading taken.** Both conditions are load-bearing. A series whose instalments vary in
amount is not an Art 14 series at all, and the Art 14(2) exemption is unavailable to it.

**Why it matters in travel specifically.** Two very common travel shapes fail this test:

- **deposit then balance** — by construction two different amounts;
- **instalment plans priced in a currency other than the billing currency** — the amount
  moves with the exchange rate.

Both fall to be analysed as merchant-initiated instead (AR-06), which is a *different legal
route to a similar operational outcome* and must be documented as such, because it rests on
weaker ground.

Encoded as `the instalment plan can be an article 14 series` in
`finmont-sca-orchestration.l4`.

---

## AR-06 — Merchant-initiated transactions

**Status: unverified. The governing text was not supplied with this job.**

**The position taken.** A transaction the merchant raises later under a mandate already
established with SCA is not an action carried out *by the payer*, so Art 97(1) PSD2 does not
engage and the transaction is outside the SCA obligation.

**Basis.** PSD2 Art 97(1) read with EBA guidance on merchant-initiated transactions.

**The distinction that must not be blurred.** This is **not** the Article 14 exemption.
Article 14 is a Chapter III exemption requiring the same amount and the same payee.
Merchant-initiated is an argument that the obligation never arose. They reach a similar
operational result by entirely different routes, they rest on different sources, and one of
them is unverified. Conflating them is the commonest modelling error in travel payment
orchestration, and the encoding keeps them in separate functions in separate modules so the
conflation cannot happen silently. Case 5 asserts both halves.

**What turns on it.** Post-ticketing ancillaries: change fees, no-show fees,
excess-baggage charges, hotel incidentals billed after check-out.

---

## AR-07 — One leg outside the EEA · **highest-risk entry in this register**

**Status: unverified, contested, and jurisdiction-sensitive. Do not ship without local
advice.**

**The position taken.** Where either the payer's or the payee's payment service provider is
established outside the EEA, SCA is not *required*; the EEA-side provider applies it on a
best-efforts basis.

**Basis.** PSD2 Art 2 (territorial scope) read with the EBA Opinion on the elements of
strong customer authentication. Neither was supplied with this job.

**Why it is the riskiest entry.** It is the one gate that is (i) guidance-based rather than
text-based, (ii) genuinely contested, (iii) applied differently across markets, and (iv)
carries the largest share of FinMont's traffic by value, since cross-border travel is
precisely the case where one leg is routinely outside the EEA. It is also the gate whose
failure mode is the worst: getting it wrong in the permissive direction means systematically
under-authenticating cross-border transactions across the whole book.

**What turns on it.** An EEA cardholder buying from a non-EEA airline acquirer, and a
non-EEA cardholder buying from an EEA merchant. Encoded as
`out of scope because only one leg is in the EEA`. Case 9.

**Recommended treatment.** Make this gate configurable per market in FinMont's policy layer
rather than fixed in the encoding, and default it to the conservative setting (SCA required)
in any market where local advice has not been obtained.

---

## AR-08 — Euro thresholds against a multi-currency book

**The silence.** The SCA-RTS states every threshold in euro and says nothing about how a
transaction denominated in another currency is measured against them — which rate, sourced
from where, as at what moment.

**Treatment.** Deferred to the caller. `amount in euro` is an input; the encoding performs
no conversion and asserts nothing about how the figure was produced.

**What turns on it.** A transaction near a boundary — EUR 30, EUR 50, EUR 100, EUR 250,
EUR 500 — can fall on either side depending on the rate and the timestamp chosen. FinMont
should fix a documented convention and record the rate used alongside each decision, because
the decision is only auditable if the figure it turned on is reproducible.

---

## AR-09 — "Business day"

**Status: unverified source; modelled approximately.**

PSD2 Art 4(37) defines a business day by whether the relevant provider "is open for business
as required for the execution of a payment transaction" — provider-specific and
calendar-specific.

**Modelled here** as Monday to Friday. **Public holidays are not modelled.** A deadline
computed by `business days after` is therefore the *earliest possible* one; a real calendar
can only push it later. That direction is deliberate: an encoding that errs should err
towards the tighter deadline, not the looser one.

Affects Art 73(1) (end of the following business day), Art 77(2) (10 business days) and
Art 90(2).

---

## AR-10 — "Without undue delay"

PSD2 Art 89(1) requires a refund "without undue delay". This is a standard, not a period. It
is **deliberately left unquantified** rather than encoded as some invented number of days.
`the payer payment service provider is liable for correct execution` decides liability;
nothing in the encoding computes a deadline from Art 89.

Contrast Arts 73(1), 77(1), 77(2) and 90(2), which state countable periods and are encoded
as dates.
