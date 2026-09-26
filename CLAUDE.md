# CLAUDE.md — `legalese/canon`

Notes for a coding assistant working in this repository.
It holds **law**: sources, and L4 encodings of them.
The tools — the L4 language, the `l4` binary, the pipeline — live in [`legalese/l4-ide`](https://github.com/legalese/l4-ide).

## Before you encode anything

**Load the L4 skills.** They do not live in this repository, so a session started here has neither unless the L4 plugin is installed:

```
/plugin marketplace add legalese/l4-plugin
/plugin install l4-computational-law@legalese
```

It carries two skills:

- **`encoding-a-subject`** — the workflow for encoding a whole Act, regulation or contract and filing it here: the brief, a coverage table, nouns before rules, tests taken from the source, a self-check, an independent test pass, and this repository's layout.
  **Start here for any request to "encode" something.**
- **`writing-l4-rules`** — the language itself.

If `/skills` does not list `encoding-a-subject`, the installed plugin predates it; read it at [`skills/encoding-a-subject/`](https://github.com/legalese/l4-ide/tree/unstable/skills/encoding-a-subject) in l4-ide.

**Get a current `l4`.** The plugin's `scripts/install-l4.sh` installs the release it was built against; otherwise take the newest archive from [`legalese/prereleases`](https://github.com/legalese/prereleases/releases).
`l4` has no `--version`; the archive's `BUILD-INFO.txt` names the commit.
A binary older than the skills rejects constructs the skills tell you exist, and the error reads like your mistake.
Leave `JL4_LIBRARY_PATH` unset.

## Where things go

The layout is ruled in `docs/directory-conventions.md` (rulings of 2026-08-05), which is on the `docs/directory-conventions` branch and not yet on `main`:

```bash
git show origin/docs/directory-conventions:docs/directory-conventions.md
```

In short: `subjects/<jurisdiction>/<slug>/` for the law, with `<jurisdiction>` an ISO 3166 code in lowercase (`sg`, `il`, `us/ca`); `subjects/contracts/<genre>/<slug>/` for contract forms; and each encoding as its own row at `encodings/<row>/`, with an `encoding.json`, a `NOTES.md` and a `SOURCE-LICENSE.md` beside the `.l4`.
The `encoding-a-subject` skill's `references/canon-deposit.md` walks through it.

**`main` does not follow that layout everywhere yet.** Much of it uses full jurisdiction names (`subjects/israel/`, `subjects/western-australia/`) with the `.l4` directly in the subject directory.
If the law you are about to encode already has a directory under the other spelling, ask before creating a second one.

**Encodings go on your own drafts branch, `<github-username>/drafts`, not `main`.**
The l4-ide pipeline's publish stage refuses `main` for the same reason: an encoding stays on a drafts shelf until the licence terms of the source text it quotes are settled.

## Worked examples to read first

On the `mengwong/drafts` branch:

- `subjects/il/hvac-work-licensing-2025/encodings/legalese/` — a Law and its fee regulations in three vintages, with a scope statement, a fork register, a table of every fee in each vintage, and a test file that is meant to fail and says how many times.
- `subjects/sg/child-support/` — a subject whose primary source is an announcement rather than a statute, and says so.

```bash
git show origin/mengwong/drafts:subjects/il/hvac-work-licensing-2025/encodings/legalese/encoding.json
```

## When the encoding exists

[`PIPELINE.md`](PIPELINE.md) describes the l4-ide pipeline that takes a finished encoding to its projections (DMN, BPMN, a web wizard) and the two human gates.
You do not need it to produce a good encoding.
