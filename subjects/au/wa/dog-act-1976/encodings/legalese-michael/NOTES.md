# Dog Act 1976 (WA) — dog attacks and dangerous dogs — notes

## Provenance of this deposit

This subject was originally created here (2026-09-07) by a bulk ingest sweep of Western
Australian legislation that fetched the raw Act text with no encoding produced —
`corpus_modules: []`, `status: "draft"`. On 2026-09-09 the same underlying document was used to
produce a scoped encoding (s. 3 extract + Part VI Division 1 s. 33D / Division 2 ss 33E-33M) in
the `legalese/l4-ide` development repository, under `etc/go/subjects/dog-act-1976/` (the
pipeline sidecar) and `jl4/examples/legal/dog-act-1976/` (the corpus). This directory is a
mirrored copy of that work, kept here because `dog-act-1976` was already registered as a canon
subject. **`l4-ide`'s copy, not this one, is under the pipeline's own version control and
machine checks** (`l4 check`, `l4 run`, `etc/go/lib/register-validate.mjs`); treat this copy as
current as of 2026-09-09 and re-sync it if the `l4-ide` side is later revised.

## No human gate has been granted

Neither HG1 (domain-expert review of the encoding) nor HG2 (sign-off on anything outward-facing)
has been sought or granted for this deposit. `status: "draft"` reflects that. This is a working
copy in a local clone of `legalese/canon`; it has not been committed or pushed to that repo's
remote, and doing so is exactly the kind of outward-facing act HG2 exists to gate.

## Scope discipline

**Superseded 2026-09-09, same day.** The paragraph below described the first-pass scope; the user
then asked "is this the entire Dog Act?", was told no, and asked to parallelize the rest. This
subject now covers the **whole Act** — 18 modules, 654 assertions — via a 16-way parallel Workflow
run in `l4-ide` (`wf_9ecfc05c-79c`). See README.md's Modules table, History section, and ambiguity
register for the current state.

<details><summary>Original scope note (2026-09-09, first pass, no longer current)</summary>

The Dog Act 1976 runs to roughly 120 sections across ten Parts (registration, microchipping,
kennels, general dog control, pet-shop/dog-supply regulation, enforcement, civil remedies, local
laws, and miscellaneous provisions). This deposit encodes none of that outside Division 1 s. 33D
and Division 2 (ss 33E-33M) — a deliberately bounded scope, on the precedent of the BNA smoke
corpus (British Nationality Act 1981, s. 1 only) rather than an attempt at the whole Act.

</details>

## The restricted-breed regulations

The Act names no restricted breeds. s. 3 defines a dangerous dog (restricted breed) as one "of a
breed prescribed by the regulations to be a restricted breed", or a mix including one.
`registers/source-bundle/` now holds **Dog (Restricted Breeds) Regulations (No. 2) 2002**,
version `01-00-00`: Reprint 1, **as at 1 May 2008**, supplied by Michael on 2026-09-30. Its r. 3
lists dogo Argentino, fila Brasileiro, Japanese tosa, American pit bull terrier, pit bull
terrier, and any breed whose import the Commonwealth prohibits absolutely, plus a mix that
"visibly contains" one of them. The scheme console's Dog Act model uses that list.

**Currency is unconfirmed, and there are signs this is not the instrument doing the prescribing
today.** The reprint predates the 2013 amendments that put the restricted-breed rules into the
Act (ss. 33GA-33GC). Its r. 3 defines "restricted breed dog" for its own purposes rather than
prescribing breeds "to be a restricted breed" as s. 3 now requires. Its r. 8A exempts dogs
"under the age of 6 months" from sterilisation, where s. 33GB(1) now bites at 3 months. And its
mixed-breed test ("visibly contains") is narrower than s. 3(b) ("a mix of 2 or more breeds, one
being…"). Before relying on the list, find the current prescribing instrument on
legislation.wa.gov.au and record its version here. The encoding treats the breed as a supplied
fact, so nothing in the L4 depends on this document.

## Toolchain

Checked and run against `l4` prerelease `unstable-20260907-9d6536a` (commit
`9d6536a94fda175138e5a8dc5fbcd47bd9dd9a68`), from `legalese/prereleases`, downloaded and
sha256-verified 2026-09-09. Full detail, including a platform bug found (and not fixed, as
out-of-scope shared infrastructure) while wiring the `l4-ide` sidecar up on Windows, is in that
repository's `etc/go/subjects/dog-act-1976/NOTES.md`.
