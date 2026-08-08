# Directory conventions for `canon`

**Status (2026-08-05): PROPOSED as a document; its six questions are RULED.** Meng ruled
Q1–Q6 on 2026-08-05 (§10). Two rulings — Q3 (no primary encoding) and Q4 (pins only, no
mirroring) — overrule the first draft's recommendations, and they point the same way:
**canon is a registry, not a curator**. This revision carries that posture through the
whole document. The document remains proposed rather than adopted until §12's amendments to
the top-level [README](../README.md) land; nothing is filed under this tree yet.

This document is **SI-R9**'s concrete on-disk form ("canon as an index over GitHub",
proposed 2026-08-03 in l4-ide `specs/todo/single-instruction-demo/SPEC.md` §9). Per the Q6
ruling, R9 moves from PROPOSED to **ANSWERED, in the coexistence form** — canon holds
vendored encodings _and_ indexes external ones, through one row grammar. The edit recording
that in SPEC.md lands in l4-ide, not from this repository; §12 states it precisely.

The inside of an **encoding** — the subject-sidecar shape (descriptor, cases, projections,
registers, report, gates) ruled in SI-R1 and recorded in
[`subjects/README.md`](../subjects/README.md) — remains ruled input. The Q3 ruling
relocates it: the sidecar is now the shape of a vendored encoding **row**, one level below
the subject, and its descriptor splits into a subject-level and an encoding-level half
(§4.2); §12 records the `subjects/README.md` amendment this requires.

---

## 1. The tree at a glance

```
subjects/
  us/                       enacting authority: ISO 3166-1 alpha-2, lowercase
    regcf/                    17 CFR Part 227 — federal, so directly under us/
      subject.json              the LAW's identity: citation, extent, source facts
      source/                   the source text (license permitting) — shared by all rows
      encodings/
        legalese/               a vendored encoding row — the ruled sidecar shape
        example-firm.link.json  a pointer row — sha-pinned index entry, equal standing
    ca/                       ISO 3166-2 subdivision: California
      ccpa-2018/
  uk/
    bna-1981/                 British Nationality Act 1981 (extent: UK-wide — metadata)
    housing-act-1988/         a subject whose only row is a pointer
    sct/                      Acts of the Scottish Parliament
  eu/
    gdpr-2016/                supranational: eu is an ISO 3166-1 exceptionally-reserved code
    whistleblower-directive-2019/
  de/
    hinschg-2023/             transposes eu/whistleblower-directive-2019 — metadata cross-link
  jp/
    appi-2003/                non-Anglophone: ASCII slug; native-script title in subject.json
    13/                       ISO 3166-2 JP-13: Tōkyō-to
      youth-protection-ordinance-1964/
  contracts/
    GENRES.md                 the controlled genre vocabulary
    insurance/
    investment/
      yc-safe-postmoney/      a standard form
    leasing/
    lending/
      example-bank-facility-2024/   a bespoke instrument; its one row is a pointer
docs/
  directory-conventions.md    this document
```

Three rules generate everything above:

1. **A subject directory (a _leaf_ of the tree) is a directory containing `subject.json`** —
   the identity of the body of law itself: citation, extent, source facts. Everything above
   it is a grouping node.
2. **The path of a leaf below `subjects/` is the subject's canonical identifier**:
   `us/regcf`, `uk/bna-1981`, `contracts/investment/yc-safe-postmoney`. The first component
   selects the grammar — `contracts` opens the genre tree (§3); anything else must be a
   jurisdiction code and opens the authority tree (§2).
3. **Encodings of a subject are equal rows under `encodings/`** (Q3): each row is either a
   vendored directory in the ruled sidecar shape or a sha-pinned pointer file. **No row is
   primary**; canon records, and does not choose (§4).

---

## 2. Enacted law: the jurisdiction tree

### 2.1 Authority, not territory

The path component names the **enacting authority**, not the territory of application. This
is the design move that dissolves the hard cases, and it follows legislation.gov.uk, whose
document types (`ukpga`, `asp`, `wsi`, `nisr`) key on the legislature that made the
instrument, not on where it applies. Where an instrument applies — its extent — is a legal
question with legally interesting answers (the BNA 1981 extends UK-wide; the Housing Act
1988 extends to England and Wales), and it lives in `subject.json` as an `extent` field,
never in the path.

Consequences, case by case:

- **Federal systems.** Federal law sits directly under the country code; state or provincial
  law under a subdivision component. `us/regcf` (SEC, federal) beside `us/ca/ccpa-2018`
  (California legislature). Same subject legislated at two levels is two authorities, two
  leaves: `au/privacy-act-1988` and `au/nsw/pipa-1998` coexist without contortion, as do
  `ca/pipeda-2000` and `ca/qc/law-25-2021`.
- **The EU.** `eu/` is a peer of the country codes — `EU` is an ISO 3166-1
  exceptionally-reserved code element, so one rule ("ISO 3166-1 alpha-2 including
  exceptionally-reserved codes") admits it without a special case. A **regulation** is one
  work: `eu/gdpr-2016`. A **directive** is a work of the EU, and each national
  **transposition is a different work by a different authority**: the directive lives at
  `eu/whistleblower-directive-2019`, the German transposition at `de/hinschg-2023`, whose
  `subject.json` carries `"transposes": "eu/whistleblower-directive-2019"`. The
  cross-reference is metadata, because the relationship is citational, not hierarchical —
  filing the HinSchG under `eu/` would misstate who enacted it.
- **The UK.** `uk/` is an exceptionally-reserved ISO code, matches legislation.gov.uk's own
  usage, and is what everyone says (ruled, §10 Q2). Westminster legislation sits directly
  under `uk/` — including England-only measures, because England has no separate
  legislature; the devolved legislatures get subdivision components from ISO 3166-2:GB:
  `uk/sct/` (Acts of the Scottish Parliament), `uk/wls/` (Senedd), `uk/nir/` (NI Assembly).
  "Is Scotland a jurisdiction?" becomes a non-question: Scotland is an authority when the
  Scottish Parliament enacts, and an extent when Westminster legislates about it.
  **England-and-Wales**, which is a legal system but not a legislature, never needs a path
  component — it appears only as an extent value.
- **Non-Anglophone jurisdictions and non-Latin scripts.** Path components are ASCII slugs
  (§7); the answer to "`de/` or `deutschland/`?" is `de/` — codes, not names, because codes
  are one mechanically-checkable list and names are an argument in every language. A
  Japanese statute romanizes its **official or customary abbreviation**: `jp/appi-2003` (Act
  on the Protection of Personal Information, Act No. 57 of 2003), with the native-script
  title in `subject.json` as `title_native`. A Tokyo Metropolitan ordinance sits under the
  prefecture's ISO 3166-2 suffix: `jp/13/youth-protection-ordinance-1964`. `jp/13` is
  admittedly opaque to humans — that is the price of a checkable list, and the derived index
  (§4.7) carries display names.

### 2.2 Codes, precisely

- **Country / supranational component**: ISO 3166-1 alpha-2, lowercase, **including
  exceptionally-reserved code elements** (`uk`, `eu`). One list, one linter check.
- **Subdivision component**: the suffix of the ISO 3166-2 code for that country, lowercase —
  `US-CA` → `us/ca`, `AU-NSW` → `au/nsw`, `CA-QC` → `ca/qc`, `JP-13` → `jp/13`, `GB-SCT` →
  `uk/sct`. Subdivisions **nest** as their own path component (ruled, §10 Q1) rather than
  Akoma Ntoso's single hyphenated component (`it-45`); §11 records the departure.
- **Jurisdictions whose subdivisions escape ISO 3166-2** (special administrative
  arrangements, municipal ordinances below the subdivision level): file under the nearest
  ISO-coded ancestor and record the precise authority in `subject.json`'s `authority` field.
  The path is a filing system, not an ontology; the descriptor is where precision lives.

### 2.3 Leaf slugs for enacted law

The leaf slug is a short lowercase slug, unique within its directory. Convention, not
enforcement: statutes take `<short-title-slug>-<year>` where the year is the **enactment
year** (`bna-1981`, `housing-act-1988`, `hinschg-2023`); regulations may use an established
nickname (`regcf`) or a citation slug (`ccpa-2018`). The enactment year is part of the
statute's _identity_ — like `ukpga/1981/61` — and is the **only** date a path may carry
(§5). The formal citation is required in `subject.json` regardless, so the slug can afford
to be memorable rather than exhaustive.

---

## 3. Contracts: the genre tree

Commercial instruments are categorically unlike legislation — no promulgating authority, no
official citation, often no jurisdiction at all until a governing-law clause supplies one —
so they get their own grammar under `subjects/contracts/<genre>/<leaf>/`.

- **Genre, not jurisdiction, is the path.** A SAFE under Delaware law and the same form
  adapted for Singapore are siblings, not residents of different countries; `governing_law`
  is a `subject.json` field. The contrast with §2 is principled: for enacted law the
  authority is constitutive of the work; for a contract the governing law is a term of the
  instrument, changeable by drafting.
- **The genre vocabulary is controlled**: seeded with `insurance/`, `investment/`,
  `leasing/`, `lending/`, recorded in `contracts/GENRES.md`, extended by PR to that file.
  A controlled list keeps genres mechanically checkable (§7) and prevents the
  `loans/`-vs-`lending/`-vs-`credit/` drift that free tagging produces.
- **Standard forms and bespoke instruments share the tree**, distinguished by a
  `form_kind: "standard-form" | "bespoke"` field in `subject.json`. Same tree, because a
  consumer browses by what the instrument _does_ (is there an encoded lease?) rather than by
  its provenance; a split tree would force every reader to look in two places. A **standard
  form** leaf names the form lineage — `yc-safe-postmoney`, `isda-master-2002` — with the
  form's known editions recorded in `subject.json` and the edition a given encoding covers
  recorded in that encoding's row; distinct instruments in a family (pre-money vs post-money
  SAFE) are distinct leaves. A **bespoke** instrument is admissible only if it is public,
  will usually live in its owner's repository, and therefore usually arrives as a subject
  whose only encoding row is a pointer (§4):
  `contracts/lending/example-bank-facility-2024/`.

---

## 4. Encodings: equal rows, vendored or linked

This section is SI-R9's on-disk form, revised to the Q3/Q4 rulings. The pointer model is
the one this project already operates — Claude Code plugin marketplaces, a thin index over
GitHub, whose `marketplace.json` entries carry a `source` of `{source: github, repo, path}` —
extended with the pinning and integrity fields a legal corpus needs and a plugin registry
can afford to skimp on. The registry posture is Meng's ruling: **every encoding of a
subject is an equal row, and canon takes no editorial position on which to use.**

### 4.1 The row grammar

A subject directory contains `subject.json` (the law's identity — citation, extent, source
facts), optionally `source/` (§6), and `encodings/`, whose entries are **rows**. Each row
is **exactly one** of:

- **a vendored row** — a directory `encodings/<encoder>/` holding the encoding in the ruled
  sidecar shape: `encoding.json` (the encoding-level descriptor, §4.2), `NOTES.md`,
  `SOURCE-LICENSE.md`, the `.l4`, `cases/`, `projections/`, `registers/`, `report/`,
  `gates/`;
- **a pointer row** — a file `encodings/<encoder>.link.json`: the encoding lives in someone
  else's repository, and this file is the complete index entry for it.

`<encoder>` is the row's identity — a slug in the standard charset (§7), by convention the
encoder's GitHub org or user name (`legalese`, `example-firm`), unique across both forms
within one subject (a directory `legalese/` and a file `legalese.link.json` may not
coexist). Exactly-one is structural and mechanically checkable — a row is a directory or a
file, distinguishable from a single contents-API listing — so "can an encoding be both
vendored and linked, and which wins?" never arises: one row, one form. When an encoding
moves upstream, one PR deletes the directory and adds the link (history keeps the old
content); the reverse deposit is likewise one PR, in the R8 fork-and-PR lane.

A consumer distinguishes everything **without cloning**: one `GET` of
`raw.githubusercontent.com/legalese/canon/main/subjects/<path>/subject.json` identifies the
subject; one directory listing of `encodings/` via the GitHub contents API returns the full
row set with each row's form (`dir` = vendored, `file` = pointer); one lookup in the
derived index (§4.7) does both at once.

### 4.2 Descriptors: the subject/encoding split

The Q3 ruling splits the old single descriptor in two:

- **`subject.json`** (subject level) carries facts about the **law**: `id` (the leaf slug),
  `display_name`, `citation`, `extent`, `authority` where the path is coarser than the
  enacting body, `title_native`, `transposes`, the source's URL and known versions, the
  source text's own license terms; for contracts, `form_kind` and `governing_law`. These
  are true regardless of who encodes, which is why no encoding row owns them.
- **`encoding.json`** (in each vendored row) carries facts about the **encoding**:
  `encoder`, `status` (`draft` / `adversarially-reviewed` / `reviewed`), `version` (semver),
  `versions_encoded` (which vintages of the text the dated arms cover), `license`,
  `maintainer`, corpus modules.

A **pointer row** carries the encoding-level facts plus the pin. Illustrated as
`subjects/uk/housing-act-1988/encodings/legalese.link.json`, for the Housing Act corpus
that today lives in l4-ide (`sha`/`tree_sha` values are illustrative zeros, not real pins):

```json
{
  "encoder": "legalese",
  "display_name": "Housing Act 1988, Sch. 2 — grounds for possession",
  "status": "draft",
  "status_checked": "2026-08-05",
  "version": "0.3.0",
  "source": {
    "source": "github",
    "repo": "legalese/l4-ide",
    "path": "jl4/experiments/housing-act",
    "ref": "housing-act-v1",
    "sha": "0000000000000000000000000000000000000000",
    "tree_sha": "0000000000000000000000000000000000000000"
  },
  "license": "Apache-2.0",
  "maintainer": { "name": "Legalese Pte. Ltd.", "github": "legalese" }
}
```

Field notes:

- `encoder`, `status`, `version` reuse `encoding.json`'s vocabulary exactly, so the derived
  index treats vendored and pointer rows uniformly. `status` states what the **upstream**
  encoding claims; `status_checked` records when canon last verified that claim against the
  pin. Indexed ≠ reviewed ≠ signed — three distinct claims (R9 cost 3) — and the fields
  keep them distinct: listing is the row's existence; review is `status`; the signature is
  the HG1 artifact in the **pointed-at** repository, where it binds to content and verifies
  with `ssh-keygen -Y verify` exactly as for a vendored row.
- `source` follows the marketplace shape, plus pins. `path` points at the encoding
  directory inside the source repo, which is expected to be in the sidecar shape.
- `license` is the license of the encoding. The **law's** citation and source terms are not
  duplicated here — they live in `subject.json`, one level up, once per subject.

### 4.3 Pinning: `sha` is mandatory, `ref` is a courtesy

A bare branch pointer means the index silently changes meaning under you, so it is
prohibited: **`sha` (40-hex commit) is required**, `ref` is an optional human-readable
tag/branch name, and when both are present `sha` is the effective pin — the same semantics
Claude Code plugin sources use, where an entry with both installs the pinned commit even if
the named ref has since been deleted.

`tree_sha` is the integrity digest: the git tree object id of `<sha>:<path>`, computed and
verified with plain git (`git rev-parse <sha>:<path>` in a clone of the source), no bespoke
tooling. It answers a different question than `sha`: the commit pin says _which snapshot_,
the tree digest says _this exact content_, so a fetched copy — after a force-push, out of a
cache — can be checked against what was indexed. (Git tree ids are SHA-1; the strong
binding for reviewed encodings is the HG1 signature over its sha256 payload, which travels
with the content. `tree_sha` is a fetch-integrity check, not the trust anchor.)

### 4.4 No primary: what equal rows mean in practice

Two firms may encode the same statute and disagree; the project holds that
under-determination is a property of law, not a defect in an encoding, so competing
encodings are first-class (R9 fit b) — and by the Q3 ruling, **equally so**. There is no
curated encoding, no blessed row, no `alt/`: that directory existed in the first draft
precisely to mark second-class rows, so the name dissolves with the concept. The structure
itself now says "no endorsement": nothing sits above the rows for a reader to mistake for a
recommendation.

The namespace consequence (R9 cost 4): the **subject owns the path**, the **encoder
qualifies the row**. `uk/housing-act-1988` is nobody's exclusive name; `legalese` and
`example-firm` each hold a row under it, each with its own pin, status, and signature
story.

What a consumer asking "give me the L4 for Reg CF" gets: **the row set of
`subjects/us/regcf/encodings/`, and the metadata to choose on** — never a choice made for
them. The choice fields, all machine-readable per row: `status` (the strongest claim, and
for `reviewed` rows independently verifiable against the HG1 signature), `status_checked`
(how fresh canon's verification of that claim is), `versions_encoded` (law-time coverage —
does this encoding answer for the vintage you care about?), `version`, `maintainer`,
`license`, and the row's own fidelity reports and fork register. A consumer with a policy —
"reviewed rows only, widest law-time coverage, most recently checked" — can apply it
mechanically over the derived index (§4.7), which carries every one of these columns. A
registry that refuses to choose must make choosing cheap; that is what these fields are
for.

### 4.5 Rot: detectable, not survivable

Pointer rows rot: repos get deleted, made private, force-pushed. The convention's answer,
complete as ruled (Q4: **pins only, no mirroring**):

1. **Every pointer is pinned and digested** (§4.3), so rot is _detectable_ — a fetch either
   yields content matching `tree_sha` or it does not.
2. **A scheduled link-check** (CI cron) fetches every pointer; on failure it opens a PR
   adding `"unreachable_since": "<date>"` to the row. The row is never deleted for rot and
   never moves — consumers filter on the field, and a pointer that comes back gets the
   field removed the same way. A convention that deletes on 404 converts transient outages
   into permanent index damage.

That is the whole answer. **Rot is detectable but not survivable**: when an upstream
repository is truly gone, that encoding is simply gone from canon — the row remains as a
tombstone recording that it existed, what its pin and digest were, and since when it has
been unreachable, but the content is not recoverable from here. The Q3 and Q4 rulings
compound deliberately: with no curated vendored copy standing behind a pointer (Q3) and no
mirror (Q4), **an externally-hosted encoding has exactly one copy in the world**. That is
Meng's call (2026-08-05), recorded here as a stated consequence, not an objection. The one
durability path the convention offers is vendoring: an encoder who wants their work to
outlive their repository deposits it as a vendored row through the R8 fork-and-PR lane —
durability by the encoder's choice and the maintainer's acceptance, never by canon copying
unilaterally.

### 4.6 Rejected mechanisms, and why

- **Git submodules** — rejected. They pin by SHA (good) but drag content into every
  recursive clone, defeating the thin-index goal; a deleted or private upstream breaks
  `clone --recurse` for everyone rather than degrading one row; a submodule points at a
  whole repo, not an encoding subdirectory, so a multi-encoding source repo cannot be
  indexed at row granularity; and every addition touches the shared top-level
  `.gitmodules`, recreating the merge-conflict hotspot that per-row files exist to avoid.
- **Git subtree** — rejected. Subtree _vendors_ content wholesale: that is a monorepo with
  extra history, not an index, and it reintroduces exactly the R8 problem R9 dissolves —
  maintainer-side merges that touch contributed content and strand its HG1 signature.
- **A single hand-maintained top-level `index.json`** — rejected as the source of truth.
  One file every contributor edits is a permanent conflict hotspot; row-level review turns
  into diff archaeology; and a monolithic file cannot carry per-subject artifacts. It
  survives in derived form only (§4.7).
- **One pointer file per row** — **adopted** (§4.2). Additions are conflict-free, review is
  per-row by construction, the pointer sits exactly where the vendored alternative would
  sit, and the row grammar (§4.1) stays a one-directory property. Prior art: Homebrew,
  where every formula is a per-leaf pointer file carrying `url` + `sha256` — the same shape
  at six-figure scale.
- **Mirroring at accept time** — proposed in the first draft, **rejected by ruling** (Q4).
  The Go module proxy's cache-immutably-at-first-sight model would have made rot survivable
  at the cost of org clutter, storage, and — decisively — mirroring being an act of
  redistribution. Pins-only is the ruled trade: §4.5 states what is given up.

### 4.7 The derived index

Machine consumers want one fetch, not a tree walk. A generated `index.json` — one entry per
**row**: subject path, encoder, kind (vendored/pointer), the subject's display name and
citation, and the row's status, `status_checked`, version, `versions_encoded`, license, and
pin — is **derived from the tree by CI and published as a release asset per tag** (ruled,
§10 Q5); it is never hand-edited and never committed, because a committed derivative drifts
from its sources the moment someone forgets a regeneration step. The tree is the database;
the index is a view.

---

## 5. Versioning: two axes, and what stays out of paths

The two axes are ruled (README, "Versioning") and restated here only to draw the path
consequence:

- **The law's own time axis** lives _inside_ the encoding: dated arms selected by
  `EVAL UNDER RULES EFFECTIVE AT`. Which vintages of the text an encoding covers is
  declared in its row (`versions_encoded` in `encoding.json`, §4.2 — the regcf corpus
  already records exactly this in `part227.versions.json`).
- **The encoding's revision** is semver in its row's `encoding.json`, advancing while the
  text stands still. Release tags, where used, are `<subject-path>/<encoder>/v<semver>`.

**Therefore: no dates or versions in paths.** A component like `bna-1981-as-amended-2009/`
or `regcf-v2/` conflates the axes in the reader's face and is banned by the linter (§7).
The one permitted year is the enactment year, which is identity, not version (§2.3).

In FRBR terms (the model under both Akoma Ntoso and ELI):

| FRBR level    | in canon                                                                     |
| ------------- | ---------------------------------------------------------------------------- |
| Work          | the subject directory — `subjects/uk/bna-1981`                               |
| Expression    | a dated arm inside the encoding, selected by `EVAL UNDER RULES EFFECTIVE AT` |
| Manifestation | a projection — DMN, BPMN, ladder SVG under a row's `projections/`            |
| Item          | the file in git, at a commit                                                 |

Equal rows sit comfortably here: competing encodings are multiple expressions of one work,
which FRBR models natively — another reason the subject, not any encoding, owns the path.

The deliberate departure from Akoma Ntoso: AKN puts the expression in the identifier
(`/akn/sl/act/2004-02-13/2/eng@2004-07-21`) because an AKN document _is_ one expression. An
L4 encoding is expression-indexed internally — one artifact answers for many
points-in-time — so canon needs only work-level paths, and the expression axis is a query
parameter, not an address. This is the corpus-level echo of legislation.gov.uk's `/id/` vs
`/data/` split: the leaf path is the identifier URI (the work, "how it was, is, and will
be"); a projection at a law-date is a representation.

---

## 6. Inside a subject: committed vs generated

The sidecar shape itself is ruled ([`subjects/README.md`](../subjects/README.md)) and now
describes a vendored row (§4.1); this section adds only the committed/generated discipline,
from the regcf corpus as evidence and SI-R0 ("the execution is the exhibit") as the ruling
that forces the main call:

- **Committed, and CI-re-derived**: the executable projections (`projections/` — DMN, BPMN,
  with their fidelity reports), figures (ladder SVGs), and case expectations. R0 means the
  corpus DMN is expected to actually run; an exhibit that must be regenerated before it can
  be inspected is not an exhibit. The regcf discipline carries over: every committed derived
  artifact reproduces byte-for-byte from the corpus by a stated command, and CI regenerates
  and diffs (the golden pattern), so **committed never means stale** — drift fails the
  build.
- **Committed, authored**: `subject.json` at the subject level; per vendored row,
  `encoding.json`, `NOTES.md`, `SOURCE-LICENSE.md`, the `.l4` itself, registers, the
  report, gate artifacts.
- **Committed where license permits**: the source text, under `source/` **at the subject
  level** — the text is a fact about the law, shared by every row — with retrieval
  provenance (the regcf instance keeps the govinfo XML and a `versions.json`). Where the
  source terms do not permit redistribution, each row's `registers/source-bundle.json`
  carries URL, retrieval date, and digest instead — the text is then a pinned pointer, same
  philosophy as §4. `source/` is proposed here as an **optional subject-level directory**
  (§12); each row's source bundle still records what that encoding actually ingested.
- **Never committed**: scratch and run outputs — `*.actual`, anything under `out/` —
  gitignored globally.

How a reader tells: location. Everything under a row's `projections/` is derived and
carries a generator stamp where the format allows comments; descriptors, notes, and the
`.l4` are authored; `cases/` expectations are machine-evaluated, never hand-typed (already
the class contract).

---

## 7. Naming rules, lintable

Stated as a linter would enforce them. **Enforce first**: rules 1, 2, 5, and 6 — they
prevent the mistakes that are expensive to undo (bad charset and bad tree shape mean
renames; a missing pin means an index row whose meaning floats). The rest can arrive with
the linter's second pass.

1. **Charset.** Every path component matches `^[a-z0-9][a-z0-9-]*$`, at most 64
   characters. Files additionally take a single extension (`[a-z0-9-]+(\.[a-z0-9]+)+`).
   Lowercase ASCII only; no underscores, no spaces, no `@`. (Reserved sidecar filenames
   ruled before this document — `NOTES.md`, `SOURCE-LICENSE.md`, `GENRES.md` — are
   grandfathered uppercase, matching the repo's own README convention.)
2. **First component under `subjects/`** is `contracts` or a valid ISO 3166-1 alpha-2 code
   (including exceptionally-reserved elements), lowercase. No collision is possible: genre
   tree roots are words, country codes are two letters.
3. **Grouping vs leaf is decided by contents**: a directory with `subject.json` is a leaf;
   any other directory is a grouping node. In the jurisdiction tree a grouping node below a
   country must be a valid ISO 3166-2 suffix for that country; in the contracts tree it
   must be a genre listed in `contracts/GENRES.md`. A leaf slug directly under a country
   must not equal an ISO 3166-2 suffix of that country (so `us/ca` can never be ambiguous).
4. **No versions or dates in components**: nothing matching `-v[0-9]+$` or containing an
   ISO date (`[0-9]{4}-[0-9]{2}-[0-9]{2}`); a bare trailing `-[0-9]{4}` (enactment year) is
   permitted.
5. **The row grammar** (§4.1): a leaf contains `subject.json`, optionally `source/`, and
   `encodings/`; `encodings/` contains only rows — directories holding `encoding.json` (in
   the sidecar shape) or `<encoder>.link.json` files; an encoder slug appears at most once
   across both forms within a subject.
6. **Pointer validity**: `source.sha` present and 40-hex; `source.repo` matches
   `^[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+$`; `source.tree_sha` present; `license`
   present.
7. **Reserved names**, usable as neither leaf slugs nor genres nor encoder slugs:
   `encodings`, `cases`, `projections`, `registers`, `report`, `gates`, `source`,
   `contracts`, `docs`, `index`.

---

## 8. Worked examples

### 8.1 `subjects/us/regcf/` — two equal rows, US federal

SEC Regulation Crowdfunding, 17 CFR Part 227, today maintained in l4-ide at
`jl4/examples/legal/regcf/`; this is its target shape on deposit (an HG2 act, still gated),
demonstrating the equal-rows grammar — one vendored row, one pointer row, neither
privileged:

```
subjects/us/regcf/
  subject.json                        the LAW: citation 17 CFR Part 227 · extent · source URL + versions
  source/                             license permits: PD federal text, with provenance
    part227.govinfo-2025.xml
    part227.versions.json
  encodings/
    legalese/                         a vendored row — the ruled sidecar shape
      encoding.json                   encoder: legalese · status · version · versions_encoded
      NOTES.md
      SOURCE-LICENSE.md               US federal text: public domain, 17 U.S.C. § 105
      regcf.l4
      regcf-wizard.l4
      cases/
        2026-07-23-issuer-eligibility.json
        ...
      projections/
        regcf-corpus.dmn              committed; runs (R0); CI regenerates and diffs
        regcf-corpus.fidelity.txt
        regcf-advertising.bpmn
        figures/
          regcf-rule-100b.svg
          ...
      registers/
        fork-register.json
        external-modifications.json
        source-bundle.json
      report/
        2026-08-05-conversion-report.md
      gates/
        allowed_signers
        HG1.payload.txt
        HG1.payload.sig
    example-firm.link.json            a pointer row — equal standing, own pin and status
```

A consumer choosing between the two rows reads their `status`, `status_checked`,
`versions_encoded`, and fidelity artifacts (§4.4) — canon has not chosen for them.

### 8.2 `subjects/uk/bna-1981/` — one vendored row, UK (Westminster)

British Nationality Act 1981 (c. 61). Same grammar, one row
(`encodings/legalese/`); the differences are exactly the ones the metadata is for: the
row's `SOURCE-LICENSE.md` records OGL v3 and the attribution NOTICE requires;
`subject.json` says `extent: UK-wide`; the row's dated arms cover the consolidations listed
in its `versions_encoded`. Note what the path does **not** say: not `uk/eng/bna-1981`
(extent is not authority), and not `uk/bna-1981-as-amended-2009` (the law's time axis lives
inside the encoding, §5).

### 8.3 `subjects/uk/housing-act-1988/` — a subject whose only row is a pointer

```
subjects/uk/housing-act-1988/
  subject.json                 the LAW: citation, extent — true whoever encodes
  encodings/
    legalese.link.json         §4.2's pointer — the row is the entry
```

A consumer lists `uk/`, sees the leaf, fetches two small files raw, and knows: what the law
is (`subject.json`: citation, extent, source terms), who has encoded it (the row set),
where that encoding lives (`source.repo` + `path`), which exact content is indexed (`sha` +
`tree_sha`), and what is claimed for it (`status`, checked `status_checked`). Per §4.5,
this encoding exists in exactly one place — canon holds its pin, not its content.

### 8.4 `subjects/contracts/investment/yc-safe-postmoney/` — a standard form

```
subjects/contracts/investment/yc-safe-postmoney/
  subject.json          the FORM: form_kind: standard-form · governing_law: us-de
                        known editions · no citation — forms have publishers, not gazettes
  encodings/
    legalese/           a vendored row, sidecar shape as in §8.1
      encoding.json     which edition this encoding covers, status, version
      safe-postmoney.l4
      ...
```

A bespoke instrument in the same genre tree is a subject whose only row is a pointer:
`subjects/contracts/lending/example-bank-facility-2024/encodings/example-bank.link.json`,
with `form_kind: "bespoke"` in the subject descriptor — public one-off instruments live
with their owners, and canon indexes them.

---

## 9. Gates, moves, and merges

Three properties of this layout interact with the gate design (SI-R1/R8), and one is a
requirement on tooling:

1. **Directory reorganisation is signature-preserving — and must stay so.** The HG1/HG2
   payload binds _content_, not location: it lists corpus files by **basename** with their
   sha256 (`etc/go/phases/p0-preflight.sh` builds `corpus_sha_$(basename …)` entries), plus
   the producing repo's HEAD as provenance. No canon-relative path appears in any payload,
   so a merge that only moves a row — including adopting this very convention over
   already-deposited subjects — leaves every signature verifying. This document hardens the
   accident into a rule: **gate payloads must never embed canon paths**. (R8's
   merge-invalidation warning is about edits to file _contents_ during merge; moves are
   safe, edits are not.)
2. **Pointer rows dissolve R8's merge problem for external contributions** (R9's central
   claim, now concrete): accepting an external encoding merges an `<encoder>.link.json` — a
   row, not the content — so there is no maintainer edit that could strand the contributor's
   signature, which lives with the content upstream and verifies there indefinitely.
3. **Vendored rows keep R8's constraint**: content-preserving merges, or re-signature.
   Nothing here relaxes that; the row grammar just means it applies only to the rows that
   actually carry content.

---

## 10. Rulings (2026-08-05)

The first draft posed six numbered questions; Meng ruled all six on 2026-08-05. Q1, Q2, Q5
and Q6 confirmed the draft's recommendations. **Q3 and Q4 overruled them, in the same
direction: canon is a registry, not a curator** — it records encodings and the evidence
about them; it does not bless one, and it does not copy them. The original recommendations
and trade-offs are preserved below for the record.

- **Q1 — RULED: nested subdivisions** (`us/ca/ccpa-2018`), as recommended. The AKN-style
  single component (`us-ca/`) was the alternative: closer to the standard, no
  leaf/grouping disambiguation rule needed, at the cost of a flat, sprawling listing.
- **Q2 — RULED: `uk`**, as recommended (exceptionally-reserved ISO code, matches
  legislation.gov.uk and universal usage). Strict officially-assigned ISO (`gb`) was the
  alternative: purer as a ruleset, perpetually surprising to readers.
- **Q3 — RULED: no primary; every encoding an equal row** — overruling the draft's
  curated-primary-plus-`alt/` recommendation. Structural consequences, carried through this
  revision: `subject.json` lifts to the subject level as the descriptor of the **law**
  (§4.2); encodings sit as sibling rows under `encodings/`, vendored rows carrying the
  ruled sidecar shape with an `encoding.json` descriptor; `alt/` is dissolved — with no
  first-class rows there are no second-class ones, and the name goes with the concept; the
  exactly-one rule is restated at row level (§4.1); consumer choice is served by metadata,
  not editorial position (§4.4). The draft's argument for curation (a corpus named canon is
  curatorial on purpose) is overruled: the name now refers to the corpus, not to a blessing.
- **Q4 — RULED: pins only; no mirroring** — overruling the draft's
  mirror-fork-at-accept-time recommendation. Consequence stated plainly in §4.5: rot is
  detectable (pins + digests + link-check) but **not survivable**; a deleted upstream means
  that encoding is gone from canon, its row remaining as a tombstone. Combined with Q3,
  an externally-hosted encoding has exactly one copy in the world — deliberate, and
  recorded as a consequence rather than an objection. Durability remains available to any
  encoder by vendoring through the R8 lane.
- **Q5 — RULED: derived index as a release asset per tag**, as recommended. The committed
  `index.json`-with-drift-check alternative was one raw URL closer for consumers but put a
  derivative in the tree, and derivatives in trees drift.
- **Q6 — RULED: SI-R9 moves from PROPOSED to ANSWERED, in the coexistence form**, as
  recommended — canon holds vendored rows _and_ indexes external ones, through one row
  grammar; R8 (fork-and-PR) remains the vendored lane's mechanism, its standing
  yield-to-Thomas instruction untouched. R9's five named costs, honestly accounted under
  the rulings: **availability is only partially answered** — pins make rot detectable, but
  Q4 rules out mirroring, so survivability is deliberately not provided (an accepted
  residual, not an open question); fetch-time verification → `tree_sha` (§4.3);
  indexed≠reviewed≠signed → the field separation in §4.2; namespace → subject-owned paths
  with encoder-qualified rows (§4.4); supply chain → pins make the trust decision explicit
  and auditable. The edit recording R9 as ANSWERED lands in l4-ide's SPEC.md — §12 states
  it precisely; it is applied there, not from this repository.

---

## 11. Prior art: followed and departed

| source                        | followed                                                                                               | departed                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Akoma Ntoso naming convention | ISO 3166-1/-2 jurisdiction codes; FRBR levels; work-level identity                                     | no expression (`@date`) in identifiers — L4 internalises the expression axis (§5); subdivisions nest rather than hyphenate (Q1)                 |
| ELI                           | FRBR alignment; jurisdiction as leading component; metadata over path for what paths can't say cleanly | no document-type component (`/act/`, `/reg/`): at canon's scale the slug + citation metadata carry it; revisit if a country node grows unwieldy |
| legislation.gov.uk            | authority-not-territory typing; identifier/representation split echoed as leaf-path vs projections     | no year/number path grammar — citation lives in the descriptor                                                                                  |
| Claude Code marketplaces      | pointer shape `{source: github, repo, path}`; ref/sha semantics with sha as effective pin              | added `tree_sha`, `status_checked`, license split — integrity and claim-separation a plugin registry can skip and a legal corpus cannot         |
| Homebrew                      | per-leaf pointer file with integrity digest (formula = url + sha256); conflict-free additions          | —                                                                                                                                               |
| Terraform registry            | thin index over GitHub; author-namespaced identity for competing publishers — now every row (Q3)       | encoders qualify rows inside a subject directory rather than leading the path — the subject, not the vendor, owns the address                   |
| Go modules / module proxy     | digest database (`go.sum` → `tree_sha`)                                                                | no immutable mirror (Q4: pins only) — availability deliberately weaker than the proxy's cache-at-first-sight model; §4.5 states the cost        |

---

## 12. Changes to existing files, if adopted

- **`README.md`** — the layout block, `subjects/<subject-id>/…`, becomes
  `subjects/<jurisdiction…>/<subject-id>/` with `subject.json` + `encodings/` rows beneath,
  and a pointer to this document. (The link in the prose lands with this proposal; the
  block amendment lands with adoption, so the README never describes an unadopted tree as
  current.)
- **`subjects/README.md`** — gains the first-component grammar (§1) and the Q3 split: the
  class table's `subject.json` row becomes `encoding.json` (the encoding-level half of the
  old descriptor, §4.2); a new subject-level `subject.json` is described above the table;
  the sidecar shape is stated to live per vendored row under `encodings/`; `source/` is
  added as an optional subject-level directory (§6).
- **`NOTICE`** — **landed 2026-08-08, ahead of adoption**, on Meng's instruction. It named
  `subjects/<subject-id>/SOURCE-LICENSE.md`, the pre-Q3 path, and now names the row-level
  one (§4.1) and states that a pointer row records no terms here. This bullet was missing
  from the first draft of this list: `NOTICE` hardcodes a path, so the Q3 split reaches it
  the same way it reaches `subjects/README.md`. Unlike the README layout block, this edit
  did not wait for adoption — a file that misdirects a reader looking for licence terms is
  a different risk from one that describes an unadopted tree.
- **l4-ide `specs/todo/single-instruction-demo/SPEC.md` §9, R9** — to be applied **in
  l4-ide, not from this repository** (the team lead is handling l4-ide edits): (1) the
  bullet's opening changes from "**PROPOSED 2026-08-03 (Meng); not yet ruled**" to
  "**ANSWERED 2026-08-05 (Meng), in the coexistence form** — concrete on-disk shape in
  legalese/canon `docs/directory-conventions.md` (§4), ruled via its §10"; (2) record the
  three sub-rulings: pins mandatory (`sha` + `tree_sha`), **no mirroring** (rot detectable,
  not survivable — cost 1 "availability" is thereby only partially answered, the residual
  accepted deliberately), and **no curated primary** (every encoding an equal row, cost 4
  resolved by subject-owned paths with encoder-qualified rows); (3) the closing "**Open for
  Meng**" paragraph's three opens are ruled — coexist / pin-by-SHA yes / mirror no — so
  "Until ruled, R8 stands" becomes "R8 stands for the vendored lane", its standing
  yield-to-Thomas instruction untouched.
- **`etc/go` sidecars (l4-ide)** — no change to the pipeline sidecar itself; at deposit
  time its single descriptor maps onto the §4.2 split (subject-level facts to
  `subject.json`, encoding-level facts to `encoding.json`) — a deposit-tooling mapping, not
  a sidecar change.
- **Nothing else** — zero subjects are filed, so there is no migration; that is the point
  of ruling now.
