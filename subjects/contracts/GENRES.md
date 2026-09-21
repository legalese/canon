# Genres

The controlled vocabulary for the second path component under `subjects/contracts/`.

`subjects/contracts/<genre>/<leaf>/` is the whole grammar. **Genre, not jurisdiction, is the
path**: a SAFE under Delaware law and the same form adapted for Singapore are siblings, and
`governing_law` is a `subject.json` field rather than a directory. The contrast with the
jurisdiction tree is principled — for enacted law the authority is constitutive of the work,
whereas for a contract the governing law is a term of the instrument, changeable by drafting.
See `docs/directory-conventions.md` §3, which seeded
this list, and §7 rule 3, which makes membership of it a lint condition: a grouping node in
the contracts tree must be a genre named here. That document is **not on this branch** — it
lives on `docs/directory-conventions`, which is why it is named rather than linked; read it
with `git show docs/directory-conventions:docs/directory-conventions.md`.

## The vocabulary

| genre        | what belongs                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `insurance/` | Policies, certificates and endorsements: the instrument prices a contingency and pays on the occurrence of an insured event.                                                                                              |
| `investment/`| Instruments by which capital is put into an enterprise for a return in equity or its equivalent: subscription and shareholders' agreements, convertible instruments, SAFEs, term sheets, side letters that vary them.      |
| `leasing/`   | Instruments conveying the use of an asset for a term against rent: real-property leases and licences, equipment and vehicle leases, charterparties.                                                                        |
| `lending/`   | Instruments creating an obligation to repay money advanced, and the security for it: facility and loan agreements, notes, guarantees, debentures, intercreditor and security documents.                                    |
| `payments/`  | Instruments governing a payment method's own terms, distinct from the credit or debt they may ride on: card, wallet and payment-network agreements, and the reward or loyalty programmes issued alongside them.          |

A genre says what the instrument **does**, not who wrote it and not whether it is a published
standard form or a one-off. Standard forms and bespoke instruments share the tree and are
distinguished by `form_kind` in `subject.json`, because a reader browses by function — *is
there an encoded lease?* — and a split tree would make them look in two places.

## Where an instrument sits between two genres

File it where its **operative obligation** sits, and record the other reading in the
subject's `NOTES.md`. A convertible note is `lending/` if the debt is real and repayment is
the default outcome, `investment/` if conversion is. Where the choice is genuinely arguable,
the argument belongs in `NOTES.md`, not in a second copy of the row: a subject has one path
(directory conventions §1 rule 2), and cross-references are metadata.

## Extending this list

By pull request **to this file**, in the same change as the first subject that needs the new
genre — a genre with no rows is a guess about the future. Say in the PR what the genre is
for and why an existing one does not hold the instrument. A controlled list is what keeps
genres mechanically checkable and heads off the `loans/`-vs-`lending/`-vs-`credit/` drift
that free tagging produces, so the cost of adding one is meant to be a conversation.

Reserved names may not be used as a genre: `encodings`, `cases`, `projections`, `registers`,
`report`, `gates`, `source`, `contracts`, `docs`, `index` (directory conventions §7 rule 7).

## Rows filed so far

| genre         | rows                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------- |
| `insurance/`  | none yet                                                                                          |
| `investment/` | [`yc-safe-postmoney`](investment/yc-safe-postmoney), [`yc-safe-premoney`](investment/yc-safe-premoney) |
| `leasing/`    | none yet                                                                                          |
| `lending/`    | none yet                                                                                          |
| `payments/`   | [`sg-miles-card`](payments/sg-miles-card)                                                        |

The three empty genres (`insurance`, `leasing`, `lending`) are kept because they are the
ruled seed vocabulary, not because a row is expected imminently. An empty genre directory is
not created until it has a row; the vocabulary lives in this table.

**`payments/` added 2026-09-21**, in the same change as its first subject,
`payments/sg-miles-card`: eight Singapore credit/debit cards' reward-programme terms. None
of the four seed genres holds it — the cards are not priced against a contingency
(`insurance/`), no capital changes hands (`investment/`), no asset is conveyed for a term
(`leasing/`), and while a credit card *is* a line of credit, the operative content encoded
here is the rewards programme riding on the card, not the credit facility itself (per this
document's own "file where the operative obligation sits" rule, the encoded obligation is
"how many miles does this transaction earn", not "must this balance be repaid"). This
decision has not been reviewed by anyone but the session that made it and Meng, who chose
the bundling shape (see the subject's own `NOTES.md` §1 for the one-subject-per-instrument
departure this genre choice sits beside); a maintainer who disagrees should feel free to
rename or fold it.
