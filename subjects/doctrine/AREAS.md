# Areas

The controlled vocabulary for the second path component under `subjects/doctrine/`.

`subjects/doctrine/<area>/<leaf>/` is the whole grammar, and it mirrors the contracts tree
exactly — see [`../contracts/GENRES.md`](../contracts/GENRES.md), which this file is modelled on.

## What the doctrine tree is for, and why it is not the jurisdiction tree

`docs/directory-conventions.md` gives two grammars. §2 files **enacted law by the authority that
enacted it**, because for a statute the authority is constitutive of the work. §3 files
**commercial instruments by genre**, because a contract has no promulgating authority at all.

**A doctrine of judge-made law, encoded across authorities, fits neither.** Filing it under one
jurisdiction would make the comparators trespassers and would misdescribe the subject, which is
the *question* rather than any one court's answer to it. Filing four sibling subjects would put
the comparison nowhere, because a delta has no home in either operand.

So: for enacted law the **authority** is constitutive; for a commercial instrument the **genre**
is what a reader browses by; for a doctrine under comparison the **question** is constitutive and
the authorities are its variants. The authorities a leaf reaches are listed in `extent` in
`subject.json`, exactly as §2.1 puts extent in the descriptor rather than in the path.

**This grammar is a proposal, not a ruling.** `docs/directory-conventions.md` §12 owns the
rewrite, and no row here has amended it. That document is **not on this branch** — read it with
`git show docs/directory-conventions:docs/directory-conventions.md`. A reviewer who thinks the
doctrine tree is wrong should move its rows and say why in that document.

## The vocabulary

Seeded by the first row to land. Extend it by PR to this file, as the genre list is extended.

| area        | what belongs                                                                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contract/` | Doctrines governing the formation, validity, content and discharge of agreements: mistake, misrepresentation, duress and undue influence, frustration, penalties, construction. |

## When a leaf belongs here rather than under a jurisdiction

Ask what the encoding is **of**. If it is one authority's rule, stated for that authority, it is
that authority's — a single-jurisdiction doctrine is not obliged to move here merely because it is
judge-made. A leaf belongs here when the subject is the doctrine itself and the point of the
encoding is that the authorities answer differently, which is a fact about none of them
individually.

The first row is the worked example: `doctrine/contract/unilateral-mistake` exists because
Singapore's equitable limb is only visible as distinctive when England's, Australia's and the
American rule are computed on the same facts beside it.

## What a leaf here owes that a statute leaf does not

- **`authority_note` in `subject.json`**, per authority, saying how each was retrieved and how far
  it can be relied on. A comparative row will almost always have one primary source read in full
  and comparators read at second hand, and that asymmetry has to be on the record rather than in
  someone's head.
- **`law_kind`**, so a consumer can tell a judgment from an enactment without parsing a citation.
- **A statement of what the encoding cannot say.** A doctrine leaf has no in-force date, no revised
  edition and no amendment markers, so several of the registers' completeness joins cannot run at
  all. Say which, and why.
