# Directory conventions for `canon`

**Status (2026-08-05): PROPOSED, not adopted.** Nothing is filed under this tree yet — the
repository holds zero subjects, which is exactly why the convention is being written now.
Adoption means: Meng rules on the open questions in §10 (answering by number is enough), and
the layout block in the top-level [README](../README.md) is amended per §12 in the same
change. Until then, this document describes a proposal, not the repository.

This document also discharges **SI-R9** ("canon as an index over GitHub", PROPOSED
2026-08-03 in l4-ide `specs/todo/single-instruction-demo/SPEC.md` §9): §4 is R9's concrete
on-disk form. §10 Q6 recommends moving R9 from PROPOSED to ANSWERED, in the coexistence
reading — canon holds a small curated set of vendored encodings _and_ indexes external ones,
through one leaf grammar.

What this document does **not** touch: the inside of a leaf. The subject-sidecar shape
(descriptor, cases, projections, registers, report, gates) was ruled in SI-R1, is recorded
in [`subjects/README.md`](../subjects/README.md), and is taken here as fixed input. This
document supplies the tree **above** the leaves, the pointer mechanism, and the naming rules.

---

## 1. The tree at a glance

```
subjects/
  us/                       enacting authority: ISO 3166-1 alpha-2, lowercase
    regcf/                    17 CFR Part 227 — federal, so directly under us/
    ca/                       ISO 3166-2 subdivision: California
      ccpa-2018/
  uk/
    bna-1981/                 British Nationality Act 1981 (extent: UK-wide — metadata)
    housing-act-1988/         a POINTER leaf: subject.link.json, no vendored content
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
      yc-safe-postmoney/      a standard form, vendored
    leasing/
    lending/
      example-bank-facility-2024/   a bespoke instrument, as a pointer leaf
docs/
  directory-conventions.md    this document
```

Two rules generate everything above:

1. **A leaf is a directory containing exactly one of `subject.json` (vendored encoding) or
   `subject.link.json` (pointer to an encoding hosted elsewhere).** Everything else in the
   tree is a grouping node.
2. **The path of a leaf below `subjects/` is its canonical identifier**: `us/regcf`,
   `uk/bna-1981`, `contracts/investment/yc-safe-postmoney`. The first component selects the
   grammar — `contracts` opens the genre tree (§3); anything else must be a jurisdiction
   code and opens the authority tree (§2).

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
- **The UK.** `uk/` is likewise an exceptionally-reserved ISO code, matches
  legislation.gov.uk's own usage, and is what everyone says (§10 Q2 offers strict-ISO `gb`
  as the alternative). Westminster legislation sits directly under `uk/` — including
  England-only measures, because England has no separate legislature; the devolved
  legislatures get subdivision components from ISO 3166-2:GB: `uk/sct/` (Acts of the
  Scottish Parliament), `uk/wls/` (Senedd), `uk/nir/` (NI Assembly). "Is Scotland a
  jurisdiction?" becomes a non-question: Scotland is an authority when the Scottish
  Parliament enacts, and an extent when Westminster legislates about it.
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
  `uk/sct`. Subdivisions **nest** as their own path component rather than Akoma Ntoso's
  single hyphenated component (`it-45`); §11 records the departure and §10 Q1 offers the
  AKN form as the alternative.
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
  `form_kind: "standard-form" | "bespoke"` field in the descriptor. Same tree, because a
  consumer browses by what the instrument _does_ (is there an encoded lease?) rather than by
  its provenance; a split tree would force every reader to look in two places. A **standard
  form** leaf names the form lineage — `yc-safe-postmoney`, `isda-master-2002` — and records
  the exact edition encoded in `subject.json` (`source.edition`); distinct instruments in a
  family (pre-money vs post-money SAFE) are distinct leaves. A **bespoke** instrument is
  admissible only if it is public, will usually live in its owner's repository, and
  therefore usually arrives as a pointer leaf (§4) under an author-qualified slug:
  `contracts/lending/example-bank-facility-2024/`.

---

## 4. Leaves are polymorphic: vendored or linked

This section is SI-R9's on-disk form. The model is the one this project already operates —
Claude Code plugin marketplaces, a thin index over GitHub, whose `marketplace.json` entries
carry a `source` of `{source: github, repo, path}` — extended with the pinning and
integrity fields a legal corpus needs and a plugin registry can afford to skimp on.

### 4.1 The exactly-one rule

A leaf directory contains **exactly one** of:

- `subject.json` — the encoding is **vendored**: the `.l4`, cases, projections, registers,
  report, and gates are in this repository, in the ruled sidecar shape.
- `subject.link.json` — the leaf is a **pointer**: the encoding lives in someone else's
  repository, and this file is the complete index entry for it.

Exactly-one is structural, CI-enforced, and answers "can a subject be both, and which
wins?" — it cannot be both, so nothing needs to win. When a vendored subject moves to
upstream maintenance, one PR deletes the content and adds the link (history keeps the old
content); the reverse deposit is likewise one PR. A consumer distinguishes the two **without
cloning**: one `GET` of
`raw.githubusercontent.com/legalese/canon/main/subjects/<path>/subject.link.json` — a 200
is a pointer, a 404 with `subject.json` present is vendored — or one directory listing via
the GitHub contents API, or one lookup in the derived index (§4.7), which carries a `kind`
column.

### 4.2 The pointer file

`subject.link.json`, illustrated with the Housing Act 1988 corpus that today lives in
l4-ide (`sha`/`tree_sha` values here are illustrative zeros, not real pins):

```json
{
  "id": "housing-act-1988",
  "display_name": "Housing Act 1988, Schedule 2 — grounds for possession",
  "citation": "Housing Act 1988 c. 50, Sch. 2",
  "status": "draft",
  "status_checked": "2026-08-05",
  "source": {
    "source": "github",
    "repo": "legalese/l4-ide",
    "path": "jl4/experiments/housing-act",
    "ref": "housing-act-v1",
    "sha": "0000000000000000000000000000000000000000",
    "tree_sha": "0000000000000000000000000000000000000000"
  },
  "license": "Apache-2.0",
  "source_license": "OGL-3.0",
  "maintainer": { "name": "Legalese Pte. Ltd.", "github": "legalese" }
}
```

Field notes:

- `id`, `display_name`, `citation`, `status` reuse `subject.json`'s vocabulary exactly, so
  the derived index treats vendored and linked rows uniformly. `status` carries the same
  three-value vocabulary (`draft` / `adversarially-reviewed` / `reviewed`) and states what
  the **upstream** encoding claims; `status_checked` records when canon last verified that
  claim against the pin. Indexed ≠ reviewed ≠ signed — three distinct claims (R9 cost 3) —
  and the fields keep them distinct: listing is `id` + `source`; review is `status`; the
  signature is the HG1 artifact in the **pointed-at** repository, where it binds to content
  and verifies with `ssh-keygen -Y verify` exactly as for a vendored subject.
- `source` follows the marketplace shape, plus pins. `path` points at the subject directory
  inside the source repo, which is expected to be in the sidecar shape.
- `license` is the license of the encoding; `source_license` the terms of the quoted legal
  text — the same split the vendored layout makes with `LICENSE`/`SOURCE-LICENSE.md`.

### 4.3 Pinning: `sha` is mandatory, `ref` is a courtesy

A bare branch pointer means the index silently changes meaning under you, so it is
prohibited: **`sha` (40-hex commit) is required**, `ref` is an optional human-readable
tag/branch name, and when both are present `sha` is the effective pin — the same semantics
Claude Code plugin sources use, where an entry with both installs the pinned commit even if
the named ref has since been deleted.

`tree_sha` is the integrity digest: the git tree object id of `<sha>:<path>`, computed and
verified with plain git (`git rev-parse <sha>:<path>` in a clone of the source), no bespoke
tooling. It answers a different question than `sha`: the commit pin says _which snapshot_,
the tree digest says _this exact content_, so a fetched copy — from a mirror, after a
force-push, out of a cache — can be checked against what was indexed. (Git tree ids are
SHA-1; the strong binding for reviewed subjects is the HG1 signature over its sha256
payload, which travels with the content. `tree_sha` is a fetch-integrity check, not the
trust anchor.)

### 4.4 Competing encodings: `alt/`

Two firms may encode the same statute and disagree; the project holds that
under-determination is a property of law, not a defect in an encoding, so competing
encodings are first-class (R9 fit b). The grammar: the leaf root holds the **curated**
encoding (vendored or linked); additional encodings are pointer files under `alt/`,
author-qualified by filename:

```
subjects/us/regcf/
  subject.json                    the curated encoding (vendored)
  alt/
    example-firm.link.json        a competing encoding, indexed
```

`alt/` entries are always pointers — a competitor's content lives in the competitor's
repository, which is R9's whole point — and carry the full §4.2 schema, so each competing
row has its own pin, status, and signature story. This keeps the jurisdiction tree free of
author-qualified directory names (R9 cost 4: names cannot be exclusive, so identity is
path + author, with the path owned by the _subject_ and the author qualification carried by
the row). The curated/alt distinction is an endorsement decision by the canon maintainer;
§10 Q3 offers the flatter no-primary alternative.

### 4.5 Rot

Pointers rot: repos get deleted, made private, force-pushed. The convention's answers, in
increasing strength:

1. **Every pointer is pinned and digested** (§4.3), so rot is _detectable_ — a fetch either
   yields content matching `tree_sha` or it does not.
2. **A scheduled link-check** (CI cron) fetches every pointer; on failure it opens a PR
   adding `"unreachable_since": "<date>"` to the pointer file. The leaf is never deleted for
   rot and never moves — consumers filter on the field, and a pointer that comes back gets
   the field removed the same way. A convention that deletes on 404 converts transient
   outages into permanent index damage.
3. **Mirroring** (recommended, §10 Q4): at accept time, canon's org takes a mirror fork of
   the source repository. GitHub forks retain objects when the upstream vanishes, so the
   pinned `sha` stays fetchable — the Go module proxy's insight (cache immutably at first
   sight) implemented with zero custom infrastructure. Mirroring is redistribution, so it is
   only available where `license` permits it; a pointer whose license forbids mirroring is
   accepted pins-only, eyes open.

### 4.6 Rejected mechanisms, and why

- **Git submodules** — rejected. They pin by SHA (good) but drag content into every
  recursive clone, defeating the thin-index goal; a deleted or private upstream breaks
  `clone --recurse` for everyone rather than degrading one row; a submodule points at a
  whole repo, not a subject subdirectory, so a multi-subject source repo cannot be indexed
  at subject granularity; and every addition touches the shared top-level `.gitmodules`,
  recreating the merge-conflict hotspot that per-leaf files exist to avoid.
- **Git subtree** — rejected. Subtree _vendors_ content wholesale: that is a monorepo with
  extra history, not an index, and it reintroduces exactly the R8 problem R9 dissolves —
  maintainer-side merges that touch contributed content and strand its HG1 signature.
- **A single hand-maintained top-level `index.json`** — rejected as the source of truth.
  One file every contributor edits is a permanent conflict hotspot; row-level review turns
  into diff archaeology; and a monolithic file cannot carry per-subject artifacts. It
  survives in derived form only (§4.7).
- **One pointer file per leaf** — **adopted** (§4.2). Additions are conflict-free, review is
  per-row by construction, the pointer sits exactly where the vendored alternative would
  sit, and the polymorphism rule (§4.1) stays a one-directory property. Prior art:
  Homebrew, where every formula is a per-leaf pointer file carrying `url` + `sha256` — the
  same shape at six-figure scale.

### 4.7 The derived index

Machine consumers want one fetch, not a tree walk. A generated `index.json` — every leaf's
id, path, kind (vendored/linked), display name, citation, status, license, and pin —
is **derived from the leaves by CI and published as a release asset per tag**; it is never
hand-edited and (recommendation, §10 Q5) never committed, because a committed derivative
drifts from its sources the moment someone forgets a regeneration step. The leaves are the
database; the index is a view.

---

## 5. Versioning: two axes, and what stays out of paths

The two axes are ruled (README, "Versioning") and restated here only to draw the path
consequence:

- **The law's own time axis** lives _inside_ the encoding: dated arms selected by
  `EVAL UNDER RULES EFFECTIVE AT`. Which vintages of the text an encoding covers is
  declared in `subject.json` (`source.versions_encoded`, a list of consolidation dates
  with retrieval provenance — the regcf corpus already records exactly this in
  `part227.versions.json`).
- **The encoding's revision** is semver in `subject.json`, advancing while the text stands
  still. Release tags, where used, are `<subject-path>/v<semver>`.

**Therefore: no dates or versions in paths.** A component like `bna-1981-as-amended-2009/`
or `regcf-v2/` conflates the axes in the reader's face and is banned by the linter (§7).
The one permitted year is the enactment year, which is identity, not version (§2.3).

In FRBR terms (the model under both Akoma Ntoso and ELI):

| FRBR level    | in canon                                                                     |
| ------------- | ---------------------------------------------------------------------------- |
| Work          | the leaf directory — `subjects/uk/bna-1981`                                  |
| Expression    | a dated arm inside the encoding, selected by `EVAL UNDER RULES EFFECTIVE AT` |
| Manifestation | a projection — DMN, BPMN, ladder SVG under `projections/`                    |
| Item          | the file in git, at a commit                                                 |

The deliberate departure from Akoma Ntoso: AKN puts the expression in the identifier
(`/akn/sl/act/2004-02-13/2/eng@2004-07-21`) because an AKN document _is_ one expression. An
L4 encoding is expression-indexed internally — one artifact answers for many
points-in-time — so canon needs only work-level paths, and the expression axis is a query
parameter, not an address. This is the corpus-level echo of legislation.gov.uk's `/id/` vs
`/data/` split: the leaf path is the identifier URI (the work, "how it was, is, and will
be"); a projection at a law-date is a representation.

---

## 6. Inside a leaf: committed vs generated

The sidecar shape itself is ruled ([`subjects/README.md`](../subjects/README.md)); this
section adds only the committed/generated discipline, from the regcf corpus as evidence and
SI-R0 ("the execution is the exhibit") as the ruling that forces the main call:

- **Committed, and CI-re-derived**: the executable projections (`projections/` — DMN, BPMN,
  with their fidelity reports), figures (ladder SVGs), and case expectations. R0 means the
  corpus DMN is expected to actually run; an exhibit that must be regenerated before it can
  be inspected is not an exhibit. The regcf discipline carries over: every committed derived
  artifact reproduces byte-for-byte from the corpus by a stated command, and CI regenerates
  and diffs (the golden pattern), so **committed never means stale** — drift fails the
  build.
- **Committed, authored**: `subject.json`, `NOTES.md`, `SOURCE-LICENSE.md`, the `.l4`
  itself, registers, the report, gate artifacts.
- **Committed where license permits**: the source text, under `source/`, with retrieval
  provenance (the regcf instance keeps the govinfo XML and a `versions.json`). Where the
  source terms do not permit redistribution, `registers/source-bundle.json` carries URL,
  retrieval date, and digest instead — the text is then a pinned pointer, same philosophy
  as §4. `source/` is proposed here as an **optional class directory** (an additive
  amendment to the ruled sidecar table, §12).
- **Never committed**: scratch and run outputs — `*.actual`, anything under `out/` —
  gitignored globally.

How a reader tells: location. Everything under `projections/` is derived and carries a
generator stamp where the format allows comments; everything at the leaf root is authored;
`cases/` expectations are machine-evaluated, never hand-typed (already the class contract).

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
3. **Grouping vs leaf is decided by contents**: a directory with `subject.json` or
   `subject.link.json` is a leaf; any other directory is a grouping node. In the
   jurisdiction tree a grouping node below a country must be a valid ISO 3166-2 suffix for
   that country; in the contracts tree it must be a genre listed in `contracts/GENRES.md`.
   A leaf slug directly under a country must not equal an ISO 3166-2 suffix of that country
   (so `us/ca` can never be ambiguous).
4. **No versions or dates in components**: nothing matching `-v[0-9]+$` or containing an
   ISO date (`[0-9]{4}-[0-9]{2}-[0-9]{2}`); a bare trailing `-[0-9]{4}` (enactment year) is
   permitted.
5. **Exactly-one** of `subject.json` / `subject.link.json` per leaf (§4.1); `alt/`, if
   present, contains only `*.link.json` files.
6. **Pointer validity**: `source.sha` present and 40-hex; `source.repo` matches
   `^[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+$`; `source.tree_sha` present; `license`
   present.
7. **Reserved names**, usable as neither leaf slugs nor genres: `alt`, `cases`,
   `projections`, `registers`, `report`, `gates`, `source`, `contracts`, `docs`, `index`.

---

## 8. Worked examples

### 8.1 `subjects/us/regcf/` — vendored, US federal

SEC Regulation Crowdfunding, 17 CFR Part 227, today maintained in l4-ide at
`jl4/examples/legal/regcf/`; this is its target shape on deposit (an HG2 act, still gated):

```
subjects/us/regcf/
  subject.json                      id: regcf · citation: 17 CFR Part 227 · extent: US
  NOTES.md
  SOURCE-LICENSE.md                 US federal text: public domain, 17 U.S.C. § 105
  regcf.l4
  regcf-wizard.l4
  cases/
    2026-07-23-issuer-eligibility.json
    ...
  projections/
    regcf-corpus.dmn                committed; runs (R0); CI regenerates and diffs
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
  source/                           license permits: PD federal text, with provenance
    part227.govinfo-2025.xml
    part227.versions.json
  alt/
    example-firm.link.json          a competing encoding, indexed per §4.4
```

### 8.2 `subjects/uk/bna-1981/` — vendored, UK (Westminster)

British Nationality Act 1981 (c. 61). Same shape; the differences are exactly the ones the
metadata is for: `SOURCE-LICENSE.md` records OGL v3 and the attribution NOTICE requires;
`subject.json` says `extent: UK-wide`; the encoding's dated arms cover the consolidations
listed in `source.versions_encoded`. Note what the path does **not** say: not
`uk/eng/bna-1981` (extent is not authority), and not `uk/bna-1981-as-amended-2009` (the law's
time axis lives inside the encoding, §5).

### 8.3 `subjects/uk/housing-act-1988/` — a pointer leaf

The directory contains `subject.link.json` (contents in §4.2) and nothing else. A consumer
lists `uk/`, sees the leaf, fetches one file raw, and knows: what it is (`citation`), where
it lives (`source.repo` + `path`), which exact content is indexed (`sha` + `tree_sha`),
what is claimed for it (`status`, checked `status_checked`), and on what terms (`license`,
`source_license`).

### 8.4 `subjects/contracts/investment/yc-safe-postmoney/` — a standard form

```
subjects/contracts/investment/yc-safe-postmoney/
  subject.json          form_kind: standard-form · source.edition: "post-money v1.2"
                        governing_law: us-de · no citation — forms have publishers, not gazettes
  NOTES.md
  SOURCE-LICENSE.md     the form's own distribution terms
  safe-postmoney.l4
  cases/
  projections/
  registers/
  report/
  gates/
```

A bespoke instrument in the same genre tree arrives as a pointer:
`subjects/contracts/lending/example-bank-facility-2024/subject.link.json`, with
`form_kind: "bespoke"` — public one-off instruments live with their owners, and canon
indexes them.

---

## 9. Gates, moves, and merges

Three properties of this layout interact with the gate design (SI-R1/R8), and one is a
requirement on tooling:

1. **Directory reorganisation is signature-preserving — and must stay so.** The HG1/HG2
   payload binds _content_, not location: it lists corpus files by **basename** with their
   sha256 (`etc/go/phases/p0-preflight.sh` builds `corpus_sha_$(basename …)` entries), plus
   the producing repo's HEAD as provenance. No canon-relative path appears in any payload,
   so a merge that only moves a leaf — including adopting this very convention over
   already-deposited subjects — leaves every signature verifying. This document hardens the
   accident into a rule: **gate payloads must never embed canon paths**. (R8's
   merge-invalidation warning is about edits to file _contents_ during merge; moves are
   safe, edits are not.)
2. **Pointer leaves dissolve R8's merge problem for external contributions** (R9's central
   claim, now concrete): accepting an external encoding merges a `subject.link.json` — a
   row, not the content — so there is no maintainer edit that could strand the contributor's
   signature, which lives with the content upstream and verifies there indefinitely.
3. **Vendored deposits keep R8's constraint**: content-preserving merges, or re-signature.
   Nothing here relaxes that; the exactly-one rule just means it applies only to the leaves
   that actually carry content.

---

## 10. Open questions for Meng

Numbered so they can be answered by number. Each carries a recommendation and the trade-off
that made it a question.

- **Q1 — Subdivision components: nested (`us/ca/ccpa-2018`) or AKN-style single component
  (`us-ca/ccpa-2018`)?** Recommendation: **nested**. Nesting groups a country's federal and
  state law under one browsable node and keeps components on one list each; the AKN form is
  closer to the standard and avoids needing rule §7.3's leaf/grouping disambiguation, at the
  cost of a flat, sprawling `subjects/` listing.
- **Q2 — `uk` or `gb`?** Recommendation: **`uk`** (exceptionally-reserved ISO code, matches
  legislation.gov.uk and universal usage). The alternative is strict officially-assigned
  ISO (`gb`), which is purer as a ruleset but perpetually surprising to readers.
- **Q3 — Curated-primary-plus-`alt/` (§4.4), or no primary (every encoding an equal row)?**
  Recommendation: **curated primary**. Placing one encoding at the leaf root is an
  endorsement, which is deliberate — a corpus named canon is curatorial on purpose, and the
  status fields keep listing/review/signature claims distinct. The flat alternative is more
  neutral and closer to a pure registry, at the cost of every consumer re-deciding which
  encoding to use.
- **Q4 — Mirror against rot (§4.5.3), or pins-only?** Recommendation: **mirror-fork at
  accept time where the license permits**. Costs: org clutter, storage, and mirroring is
  itself redistribution — an outward-facing act with license implications, which is why
  this is a Meng call and not a default.
- **Q5 — Derived index: release asset per tag (recommended), or committed `index.json` with
  a CI drift check?** Committed is one raw URL away for consumers but is a derivative in
  the tree, and derivatives in trees drift; the drift check mitigates but adds a failure
  mode to every PR.
- **Q6 — Move SI-R9 from PROPOSED to ANSWERED, in the coexistence form?** Recommendation:
  **yes**. This document is the concrete shape R9 lacked: canon holds curated vendored
  subjects _and_ indexes external ones, through one leaf grammar, with R9's five named
  costs answered in §4 (availability → pins + mirroring Q4; fetch-time verification →
  `tree_sha`; indexed≠reviewed≠signed → §4.2's field separation; namespace →
  subject-owned paths with author-qualified `alt/` rows; supply chain → pins make the
  trust decision explicit and auditable). If adopted, R8 (fork-and-PR) remains the vendored
  lane's mechanism, per R9's own "coexist" option — and R8's standing instruction (yields
  to Thomas's better model) is inherited untouched.

---

## 11. Prior art: followed and departed

| source                        | followed                                                                                               | departed                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Akoma Ntoso naming convention | ISO 3166-1/-2 jurisdiction codes; FRBR levels; work-level identity                                     | no expression (`@date`) in identifiers — L4 internalises the expression axis (§5); subdivisions nest rather than hyphenate (Q1)                 |
| ELI                           | FRBR alignment; jurisdiction as leading component; metadata over path for what paths can't say cleanly | no document-type component (`/act/`, `/reg/`): at canon's scale the slug + citation metadata carry it; revisit if a country node grows unwieldy |
| legislation.gov.uk            | authority-not-territory typing; identifier/representation split echoed as leaf-path vs projections     | no year/number path grammar — citation lives in the descriptor                                                                                  |
| Claude Code marketplaces      | pointer shape `{source: github, repo, path}`; ref/sha semantics with sha as effective pin              | added `tree_sha`, `status_checked`, license split — integrity and claim-separation a plugin registry can skip and a legal corpus cannot         |
| Homebrew                      | per-leaf pointer file with integrity digest (formula = url + sha256); conflict-free additions          | —                                                                                                                                               |
| Terraform registry            | thin index over GitHub; author-namespaced identity for competing providers                             | author qualification only on `alt/` rows, not in every path — subjects, unlike providers, have one canonical referent                           |
| Go modules / module proxy     | digest database (`go.sum` → `tree_sha`); immutable mirror-at-first-sight (→ Q4)                        | no custom proxy protocol — GitHub raw + forks suffice at this scale                                                                             |

---

## 12. Changes to existing files, if adopted

- **`README.md`** — the layout block's first line, `subjects/<subject-id>/`, becomes
  `subjects/<jurisdiction…>/<subject-id>/` with a pointer to this document. (The link in
  the prose lands with this proposal; the block amendment lands with adoption, so the
  README never describes an unadopted tree as current.)
- **`subjects/README.md`** — gains the first-component grammar (§1) and, if the `source/`
  amendment is accepted, one additive row in the class table (§6).
- **`etc/go` sidecars (l4-ide)** — none required: `subject.json` `id` stays the leaf slug;
  the canon path is carried by location, not duplicated into the descriptor.
- **Nothing else** — zero subjects are filed, so there is no migration; that is the point
  of ruling now.
