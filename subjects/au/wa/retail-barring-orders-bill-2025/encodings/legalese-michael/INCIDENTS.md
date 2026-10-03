# Incident register — Retail Barring Orders Bill 2025 (WA)

Findings from taking this subject through the L4 pipeline (P0–P10). Three classes,
kept apart because they are findings about different things:

- **H-nn — harness.** Defects in the pipeline itself (`legalese/l4-ide`). These are
  repo defects, in the sense `status-vocabulary.md` gives `BROKEN`: nothing in a run
  is a statement about the law until they are resolved.
- **C-nn — the corpus.** Defects in our own work on this subject — the deposits,
  the encoding, the provenance. Kept separate from B-nn because "the Bill is
  wrong" and "we encoded the wrong Bill" are not the same claim and do not have
  the same repair.
- **B-nn — the Bill.** Logical, clerical and drafting defects in the source text.
  Per `PIPELINE.md`, **every finding is traceable to a provision and reproducible by
  machine**: an incident that cannot be demonstrated by an assertion or a worked
  scenario is an opinion, not a finding. Findings that turn out to be sound drafting
  are kept and marked verified-no-defect, because knowing what was checked is part of
  the result.

Status vocabulary for this register: `OPEN`, `FIXED`, `WAIVED`, `VERIFIED-NO-DEFECT`.

---

## H-01 — `etc/go/lib/*.mjs` CLI entry guards never fire on Windows

- **Status:** OPEN (pre-existing; diagnosed 2026-09-09, reproduced 2026-09-23)
- **Severity:** blocking — no stage of the pipeline can run on this machine
- **Not discovered here.** `etc/go/subjects/dog-act-1976/NOTES.md:88-114` already
  records this defect and its root cause. This entry records that it **still
  reproduces at HEAD** (`b406191a`) and that it blocks this subject too.

**Symptom.** Every `go.sh` subcommand that needs a subject dies:

```
etc/go/go.sh: line 509: GO_S_ENCODING: unbound variable        (exit 1)
```

preceded by a dump of the entire environment (`declare -x …`).

**Root cause.** `etc/go/lib/subject.mjs:730` guards its CLI block with

```js
if (import.meta.url === `file://${process.argv[1]}`) { ... }
```

On Windows Node reports `process.argv[1]` as a backslashed path
(`C:\Users\micha\l4-ide\etc\go\lib\subject.mjs`) while `import.meta.url` is always
`file:///C:/Users/...`. The two can never be equal, so the CLI block never runs and
the process **exits 0 having printed nothing**.

**Reproduced, 2026-09-23:**

```
$ node etc/go/lib/subject.mjs --list      # expect 4 subjects
                                          # actual: no output
$ echo $?
0
```

Absolute paths in either slash style behave identically — this is not a path-form
problem, it is that the two values are never equal on Windows.

**Propagation.** `go.sh:479` does
`SUBJECT_ENV="$(node "$LIB/subject.mjs" "$SUBJECT" …)" || exit 2`. The command
succeeds and returns an empty string, so the `|| exit 2` never fires, `eval ""` is a
no-op, and no `GO_S_*` variable is ever set. Two consequences follow at `go.sh:481`
and `:509`:

1. `export "${!GO_S_@}"` expands to a **bare `export`**, which in bash prints every
   exported variable — the `declare -x` dump above is that, not a debug trace.
2. `GO_MODULES="${GO_S_ENCODING_MODULES:-$GO_S_ENCODING…}"` reads `GO_S_ENCODING`
   with no `:-` fallback of its own, and `set -u` aborts.

**Scope.** Nine CLI entry points carry the same guard, so each is a silent no-op on
Windows:

| file | what is lost |
| --- | --- |
| `etc/go/lib/subject.mjs` | subject resolution — blocks every subject-aware subcommand |
| `etc/go/lib/register-validate.mjs` | the P1/P2/P4 register oracle (SKILL.md step 9) |
| `etc/go/lib/denovo-diff.mjs` | the §8 acceptance comparator (SKILL.md step 10) |
| `etc/go/lib/canon-diff.mjs` | the DMN leg's canonicalisation |
| `etc/go/lib/assert-report.mjs` | `p6-tests` assertion reporting |
| `etc/go/lib/discover.mjs` | toolchain discovery |
| `etc/go/lib/probe.mjs` | `p0-preflight` probes |
| `etc/go/lib/split-digraphs.mjs` | the LTS leg's `digraph` count |
| `etc/check-bpmn-kie-baseline.mjs` | the BPMN baseline check |

**Why this one is worse than an ordinary break.** The failure mode is *silence plus
exit 0*. An oracle that prints nothing and returns 0 is indistinguishable, to a
caller that reads exit codes, from an oracle that ran and found nothing wrong —
which is the precise failure `status-vocabulary.md` cites from
`etc/kie-dmn-check/run.sh` ("a `javac` failure once called `skip()` and exited 0").
`subject.mjs` is the call site where it is loud, because `set -u` catches it two
lines later; `register-validate.mjs` is the call site where it would be quiet.

**Fix.** `import.meta.url === pathToFileURL(process.argv[1]).href`, using
`pathToFileURL` from `node:url` — already imported in `subject.mjs` for
`fileURLToPath`. Correct on both platforms, and the change is one line per file.

**Not yet applied.** `etc/go/lib/` is shared pipeline infrastructure in a different
repository; the dog-act note deferred it pending testing across all three of
`go.sh`'s `subject.mjs` call sites (`:411 --list`, `:454 --encodings`, `:479`
default). Awaiting a decision.

---

---

## H-02 — a standard Windows git checkout silently invalidates every digest the pipeline takes

- **Status:** OPEN (new, 2026-09-23) · **Severity:** blocking, and **silent**
- **Found by:** running l4-ide's own `source-bundle.valid.json` fixture through its
  own validator. The fixture that is supposed to be clean reported a finding.

**Symptom.**

```
$ node rv.mjs source-bundle .../fixtures/source-bundle.valid.json
FINDINGS (1):
  assembled.sha256  recorded a84c2b52…913ac, file hashes 1f2d99d7…70e01
                    [assembled-digest-matches]
```

**The fixture is not wrong, and neither is the repo.** The bytes on disk are.

```
$ sha256sum      jl4/examples/legal/bna/source-s1.txt
1f2d99d77d7f005c07e79ec346269c2e0011f45eabc3226a2ff325ef30070e01
$ tr -d '\r' <   jl4/examples/legal/bna/source-s1.txt | sha256sum
a84c2b524dcf4b70900ecde967b656e99a9d4c5e896ea36eb3cced7e771913ac   <-- the recorded digest
```

Stripping carriage returns reproduces the recorded digest **exactly**. The cause:

```
$ git config --get core.autocrlf
true
$ find . -name .gitattributes        # nothing, anywhere in the repo
```

`core.autocrlf=true` is the default on a Git-for-Windows install. With no
`.gitattributes` to override it, git rewrites LF to CRLF on checkout for every file
it considers text. The committed bytes and the working-tree bytes differ, and
`git status` stays **clean**, because git normalises again on the way in. Nothing in
the repository looks wrong at any point.

**Scope — this is not about one fixture.** Measured on this worktree:

| file | on disk | as committed |
| --- | --- | --- |
| `jl4/examples/legal/bna/source-s1.txt` | `1f2d99d77d7f` | `a84c2b524dcf` |
| `etc/go/go.sh` | `6b411ba6fbcf` | `57fb559fbd92` |
| `specs/todo/single-instruction-demo/SPEC.md` | `50f82b4b0b20` | `18efeab74237` |

Corpus text, the driver itself, and the specification all differ. Every sha256 the
pipeline takes over a text file in a Windows working tree is a digest of different
bytes from the one a Linux or macOS working tree produces.

**What that reaches.** Nearly the whole evidence model, because the whole evidence
model is digests:

- **`p0-preflight`** records one digest per corpus module. All of them shift.
- **The HG1 gate payload** names each corpus file with its `shasum -a 256`
  (`gates.md`, "Why the signature binds to content"). A signature made on one
  platform can never verify on the other, over an identical commit. The gate reads
  this as *the encoding moved*, which is exactly the conclusion it is designed to
  draw and exactly the wrong one here.
- **Every stage's `--inputs` digest.** Nothing replays across platforms; every stage
  re-runs and the driver reports that an input moved when none did.
- **`go.sh verify`**, which re-hashes every artifact a receipt names, reports
  `CHANGED` for files nobody touched.
- **The object store.** Its witness key is `(stage, inputs_digest, rel)`, so
  `store diff` shows divergence between platforms for byte-identical work — and
  `references/phases.md` is explicit that a divergence *is the finding*. Here it
  would be a false one.
- **`readset` freshness**, which asks whether a newer version of a prerequisite
  exists. Cross-platform, everything reads stale forever.

**Why this is worse than H-01.** H-01 fails loudly: exit 1, a named unbound
variable, nothing proceeds. H-02 fails **quietly and plausibly** — it produces
well-formed digests of the wrong bytes, and every consumer treats them as good
evidence. The one place it surfaces is as a *finding against the corpus*, which is
the worst possible place, because the honest reading of that finding ("the recorded
digest does not match the file") is indistinguishable from the dishonest one.

**Relation to what `gates.md` already admits.** That file carefully states two things
the signature does not cover — the `l4` binary and the L4 standard library — and
records the measurement that forced the stdlib into the toolchain section. Line-ending
normalisation is a third, and it is not mentioned anywhere in the skills, the
references, or `SPEC.md`. It differs from the other two in kind: the binary and the
stdlib are inputs that were *not declared*, whereas here the **declared** input is
read as different bytes than the ones that were signed.

**Suggested repair,** cheapest first:

1. **Commit a `.gitattributes`** at the repo root pinning the digest-bearing paths to
   LF — at minimum `*.l4`, `*.json`, `*.txt`, `*.md`, `*.sh`, `*.golden`. This makes
   the working tree byte-identical across platforms and costs nothing at runtime.
   `* text=auto eol=lf` is the blunt version.
2. **Have `p0-preflight` record the `core.autocrlf` and `.gitattributes` state** in
   `probes.json`, the way it already records the binary and the clock. A run whose
   digests cannot be compared to another platform's should say so on the record
   rather than leaving it to be discovered as a corpus finding.
3. Optionally, **normalise before digesting** in `digest()` for known-text
   extensions. This is the most invasive and the least honest — it makes the digest
   stop being a digest of the file — and is listed only to be argued against.

**Note on the wrapper's own verdict.** With this understood, the wrapper's run over
the six committed fixtures is a clean bill for the validator itself: the three
`invalid` fixtures produced 11, 17 and 23 findings; the `external-modifications` and
`fork-register` `valid` fixtures were CLEAN; and the one finding against
`source-bundle.valid` is H-02, not a defect in the fixture. 43 x-rules ran in total.
The checker can be shown to go red and to go green, which is the condition
`references/phases.md` sets for trusting it.

---

---

## H-03 — an unresolvable `IMPORT` is a check ERROR that still exits 0 and prints "Check succeeded"

- **Status:** OPEN (new, 2026-09-23) · **Severity:** high, and **silent**

**Reproduced.**

```
$ printf 'IMPORT `no-such-library-at-all`\n' > p5.l4
$ l4 check p5.l4
  Severity: DiagnosticSeverity_Error
  Message:  I could not find a module with this name: no-such-library-at-all
            (searched C:\Users\micha\AppData\Roaming\jl4\libraries\...,
                      C:\Users\micha\AppData\Local\Programs\l4\..\..\libraries\...)
Check succeeded.
$ echo $?
0
```

The compiler **knows** the module is missing, says so at `Error` severity, names
both paths it searched — and then reports success.

**The control.** A genuine type error behaves correctly, which is what makes this a
finding about imports specifically rather than about `l4 check` generally:

```
$ printf 'GIVETH A NUMBER\nf MEANS "not a number"\n' > p9.l4
$ l4 check p9.l4 ; echo $?
... STRING ...        # no "Check succeeded"
1
```

**Consequence for the pipeline, and it is not small.** `references/phases.md` says
of `p3-encode`: "`l4 check` over every deposited module. That is all it is: the
compiler's own verdict that the deposit is L4 the toolchain accepts." A deposited
module whose every `IMPORT` silently resolves to nothing therefore earns a **green
`PASS`** from `p3-encode`. The stage's oracle is the exit code, and the exit code is
0.

This is the same failure shape as H-01 — work not done, reported as success — but
one layer down, in the compiler rather than in the driver.

**What it cost here.** `rbo-domain.l4` reported `Check succeeded` on its first run
while both of its imports (`prelude`, `daydate`) had resolved to nothing. The
encoding looked validated and was not. The failure only surfaced two modules later,
as `I could not find a definition for the identifier Day` — pointing at the **use
site**, in a different file, with no mention of the import that should have supplied
it.

**Suggested repair.** An unresolved module should fail the check. If there is a
reason to keep it non-fatal, `check` must not print "Check succeeded" while an
`Error`-severity diagnostic is outstanding, because that line is what a human reads
and what a phase script's exit code agrees with.

---

## H-04 — the installed `l4` has no standard library, so every documented library is unavailable

- **Status:** OPEN (new, 2026-09-23) · **Severity:** medium (environment), but it is
  what makes H-03 bite

**Measured.**

```
$ ls C:/Users/micha/AppData/Local/Programs/l4/
l4.exe                       # the binary, and nothing else

$ printf 'IMPORT prelude\n#EVAL sum (LIST 1, 2, 3)\n' > p4.l4 && l4 run p4.l4
    I could not find a definition for the identifier
      sum
```

The search paths the compiler reports are `%APPDATA%\jl4\libraries\` and
`<binary>\..\..\libraries\`. Neither is populated. All twenty-two libraries
`references/builtins.md` documents — `prelude`, `daydate`, `math`, `hierarchy`,
`negation-as-failure`, the six `actus-*` files and the rest — are therefore absent
on this machine, although `IMPORT prelude` and `IMPORT daydate` both report success
(H-03).

They **do** exist in the l4-ide checkout, at `jl4-core/libraries/` (23 files). So
this is a packaging or installation gap, not a missing artifact. Setting
`JL4_LIBRARY_PATH` to that directory did not change the result — the variable does
not appear among the paths the compiler reports searching, so either this build does
not consult it or it expects a different layout.

**What still works without a library.** Measured, so the encoding could proceed:
`LIST` literals, `EQUALS` over enum constructors, records and `CONSIDER`, and the
core coercions. `DATE_DAY` / `DATE_MONTH` / `DATE_YEAR` are compiler builtins rather
than `daydate` names and are available. What is **not** available is everything
`daydate` supplies — `YMD`, `Date`, `Day`, `add months`, `is leap year` — and every
prelude aggregate.

**Effect on this encoding.** The modules are written with **no library imports at
all**, and date comparisons are done on `DATE_YEAR` / `DATE_MONTH` / `DATE_DAY`
components rather than on `daydate`'s day counts. That is a real cost and it is
recorded rather than hidden: `references/drafting-patterns.md` prescribes building
date windows from the calendar via `daydate`, and the component arithmetic used here
is the workaround, not the house style. It should be rewritten against `daydate`
once the library is installed.

**Suggested repair.** Ship the libraries with the installer, or populate
`%APPDATA%\jl4\libraries\` from `jl4-core/libraries/`. Until then, H-03 means a file
that depends on any of them typechecks clean and fails only at the use site.

---

---

## H-05 — `REFUSE` and `TBD` are not in this build, and a whole phrasebook area is built on them

- **Status:** OPEN (new, 2026-09-23) · **Severity:** medium · **Class:** doc/build drift

**Measured.**

```
#EVAL TBD                  ->  I could not find a definition for the identifier
... THEN REFUSE "not a date"  ->  I could not find a definition for the identifier / REFUSE
```

`references/source-patterns.md` lists `REFUSE "message"` under **"New in this
release"** and devotes the whole of area 11 — ten entries,
`11-when-the-encoding-cannot-answer.md`, 870 lines — to it, describing `TBD` as
"the refusal that means 'not written yet'". Neither name resolves in the `l4` on
this machine.

**Consequence for an encoder following the skill.** Area 11's governing
distinction — "'the law does not apply' is the law's own answer and stays a value;
'the model does not cover this' is the encoder's answer and is a refusal" — has no
expressible second half here. Every case the phrasebook routes to `REFUSE` has to
be re-modelled as an ordinary value, which is exactly the conflation the area
exists to prevent.

**What it cost here.** `rbo-cases.l4` needs a total function returning a `DATE`
from `TODATE`'s `MAYBE DATE`. The natural spelling is
`WHEN NOTHING THEN REFUSE "…"`. Unavailable, so the fallback is `FALSE` on the
boolean at the assertion site, with a comment saying why. That is weaker: a
refusal would name the unreachable arm as unreachable, and `FALSE` merely makes it
fail loudly if it is ever reached.

**Note this is drift, not necessarily a bug.** The skill may be describing a newer
L4 than the installed binary, or an older one. Either way an encoder cannot tell
which from the documentation, because H-03 means a file using an absent construct
does not fail the check — it fails at the use site with "could not find the
identifier", which reads like a typo.

---

## H-06 — a mixfix call cannot span lines, and `gotchas.md` does not say so

- **Status:** OPEN (new, 2026-09-23) · **Severity:** low · **Class:** documentation gap

**Minimal reproduction.**

```l4
GIVEN a IS A NUMBER
      b IS A NUMBER
GIVETH A BOOLEAN
DECIDE a `beats` b IF a GREATER THAN b

GIVETH A BOOLEAN
f MEANS
    3
        `beats` 2
```

```
9 |         `beats` 2
  |         ^^^^^^^
unexpected `beats`
expecting %, &&, *, +, -, .., ..., /, ;, <, <=, =, =>, >, >=, ABOVE, AND, AT,
BELOW, DIVIDED, EQUALS, FOLLOWED, GREATER, IMPLIES, LESS, MINUS, MODULO, OR,
PLUS, RAND, ROR, TIMES, UNLESS, WHERE, end of input, space token, or ||
```

`3 `beats` 2` on one line checks clean. The error message enumerates every infix
operator that may open a continuation line and no mixfix segment is among them.

**Why it matters more than it looks.** The house style pushes towards long
backticked names that read like prose, and L4 is layout-sensitive, so wrapping is
the normal way to keep a line readable. A mixfix call is the one construct that
cannot be wrapped, which means the most prose-like calls are the ones forced onto
the longest single lines. Two call sites in this encoding run past 120 characters
for exactly this reason.

**`gotchas.md` documents two mixfix traps and not this one.** It has the `--`
trap and the one-argument-trailing-segment trap, both with probe names. This is a
third, and the second one nearly hides it: the arity error a wrapped call produces
("The function … is applied to …", plus "could not find the identifier" for the
orphaned segment) is the *same* error the trailing-segment trap produces, so a
reader who knows `gotchas.md` will look for the wrong cause.

**Also measured, same family.** A head segment followed by a keyword segment and
exactly one argument —
`` `the firearms RBO against Dale` `coming into force on` d `` — registers the head
at arity 1 and leaves `coming into force on` undefined. That one *is* the
documented trailing-segment trap wearing different clothes; it is recorded here
only because the fix is not obvious from the error text, which names the head
rather than the orphan.


---

---

## H-07 — `register-validate.mjs` resolves `local_path` against the l4-ide repo, so a canon corpus can never have its digests checked

- **Status:** OPEN (new, 2026-09-23) · **Severity:** medium

**The code.** `etc/go/lib/register-validate.mjs` sets

```js
const HERE = dirname(fileURLToPath(import.meta.url));   // etc/go/lib
const REPO = resolve(HERE, "../../..");                  // the l4-ide root
```

and both digest rules resolve against it — `digest-matches-local-file` and
`assembled-digest-matches` each do `resolve(REPO, …local_path)`.

**Why that is the wrong root here.** `PIPELINE.md` is explicit that the two
repositories divide the work: l4-ide holds the pipeline, and
`legalese/canon`'s `subjects/<jurisdiction>/<subject>/` holds "the corpus side:
source bundle, L4 modules, registers, reports". So for every canon subject the
register is written about files the validator cannot see. Measured on this
subject:

```
SKIPPED RULES (2) -- these checked NOTHING:
  digest-matches-local-file: subjects/.../Bill+47-1.002.pdf is not on this branch
  assembled-digest-matches: subjects/.../sources/bill-47-1.txt is not on this branch
```

**It fails in the safe direction, which is why it is medium and not high.** The
rules report `skip` with the path named, rather than passing. Nobody is misled
into thinking a digest was checked. What is lost is the check itself — on a
corpus-side subject, the one rule that would catch a register whose digests have
drifted from its files never runs.

**Demonstrated to be only about the root.** Rewriting the same register with
absolute `local_path`s makes both rules fire and pass, and corrupting one digit of
the assembled digest turns it red:

```
  assembled.sha256  recorded 024a9d85…, file hashes 124a9d85…   [assembled-digest-matches]
```

So the digests recorded here are correct; it is the path resolution that cannot
reach them.

**Suggested repair.** Resolve `local_path` against the register file's own
directory, or against a root the caller passes (`--root`, the way
`L4_GO_SCHEMA_DIR` already overrides the schema root for the selftest). The
register-relative option is the better of the two: a register is about files near
itself, and it makes the deposit portable between the two repositories.

---

---

## H-08 — `l4 batch` strips the backticks off every identifier it re-emits, so it cannot run a rule written in house style

- **Status:** OPEN (new, 2026-09-23) · **Severity:** high for deployment · **Class:** toolchain

**What `l4 batch` is for.** It is the one deployment path that needs no server:
"evaluate an `@export` function against many rows, streaming NDJSON output (one
object per row)". It works by generating a synthetic wrapper module per row —
`<file>.batchN.l4` — that applies the exported function to the row's values.

**The defect.** That generated wrapper re-emits the exported function's name and
its `GIVEN` parameter names **unquoted**. Any identifier that needed backticks in
the source is then a syntax or scope error in a file the user never wrote and
cannot edit.

**Three measurements, isolating it.**

1. **Backticked parameter name** — `` `days since the incident` IS A NUMBER ``:

   ```
   14 | , days since the incident IS NUMBER
      |        ^^^^^
   unexpected since / expecting IS or space token
   ```

   The wrapper's own line 14 shows the name with its backticks gone.

2. **Backticked function name**, parameters single-word — ``DECIDE `may apply` IF``:

   ```
   I could not find a definition for the identifier   may
     which I have inferred to be of type: FUNCTION FROM apply28 AND Cap AND NUMBER TO A34
   I could not find a definition for the identifier   apply
   ```

   `may apply` has been split into `may` applied to `apply`.

3. **Control — no identifier needs backticks.** `DECIDE mayApply IF`, parameters
   `capacity` and `days`:

   ```
   success | {"capacity": "the employer", "days": 30}  -> result True
   success | {"capacity": "someone else", "days": 30}  -> result False
   success | {"capacity": "the employer", "days": 400} -> result False
   ```

   Three rows, three correct answers. So `batch` itself works; it is the
   re-quoting that does not.

Enum **values** containing spaces are unaffected — `"the employer"` travels as a
JSON string and never has to be re-emitted as an identifier.

**Why this matters more than an ordinary bug.** It breaks precisely the
convention the house style mandates. `SKILL.md`, under "Writing for legal
audiences": "**Use backtick identifiers liberally.** `` `the applicant` `` not
`applicant`. `` `has valid identification` `` not `hasValidID`." An encoding that
follows that instruction cannot be batch-evaluated; an encoding that can be
batch-evaluated has abandoned it. Every rule in this subject's encoding uses
multi-word backticked names, so **none of them is batch-runnable as written**.

**Scope, and what is not established.** This was measured on `l4 batch` only.
Whether `jl4-service`'s REST and MCP surfaces share the defect was **not tested**,
because no service is running here and `JL4_GO_SERVICE_URL` is unset. They may
well not: the service compiles the bundle and dispatches by sanitised name
(`SKILL.md`, "Name sanitization": spaced identifiers are hyphenated for JSON and
URL use, and the API accepts both forms), which is a different mechanism from
generating a wrapper module. So the deployment story may be intact on the server
path and broken only on the local one. That is worth establishing before either
is relied on.

**Suggested repair.** Re-quote in the wrapper generator: emit any identifier that
is not a bare alphanumeric token inside backticks. A regression fixture with a
multi-word function name and a multi-word parameter would hold it.

**Workaround, and its cost.** Give an `@export`ed rule a single-token name and
single-token parameters, and take the case as ONE record parameter so there is
only one name to sanitise — which the skill already prefers for other reasons
("A record as one `GIVEN` parameter … One parameter, one shape to document, one
JSON object at the boundary"). The cost is that the entry point stops reading
like the statute exactly where a lawyer would be looking at it.


---

# Findings in the corpus

Defects in **our own** work on this subject — the deposits, the encoding, the
provenance — as distinct from defects in the Bill (B-nn) or in the pipeline
(H-nn).

---

## C-01 — the file we encoded is the Bill *as introduced*, not the print its filename claims

- **Status:** OPEN · **Severity:** high · **Class:** provenance
- **Consequence:** every finding in this register is a finding about a text that
  was superseded on 2026-03-12.

**What was found.** The file in the subject directory is named
`Bill+47-1.002.pdf`. On the Parliament of Western Australia's own bill page,
`Bill+47-1.002.pdf` is the target of the link **"Download the Bill as passed by
originating House"**, while `Bill+47-1.pdf` is **"Download the Bill as
Introduced"**. The name therefore asserts that we hold the as-passed text.

We do not. Measured:

```
local  Bill+47-1.002.pdf                    bc504a511cac03e9…602f9fb73
Wayback 20251231144400 of Bill+47-1.pdf     bc504a511cac03e9…602f9fb73
```

The Internet Archive's capture of the **as-introduced** print, taken 2025-12-31 —
after introduction on 2025-12-03 and more than two months before the Assembly's
Consideration in Detail on 2026-03-12 — is byte-identical to the file we hold.

**What that means, stated carefully.** One of two things is true, and this session
could not distinguish them:

1. the local file was saved from the "as Introduced" link and stored under the
   other link's filename; or
2. the Parliament serves identical bytes from both links.

Direct retrieval of `Bill+47-1.002.pdf` is refused by an Azure WAF JavaScript
challenge, and the Internet Archive holds no capture of it, so neither could be
confirmed. What **is** confirmed is that the bytes we encoded are the
as-introduced bytes.

**Why it matters more than a filename usually would.** The Bill has moved a long
way since that print: Consideration in Detail and Third Reading in the Assembly on
2026-03-12, introduction and second reading in the Council, second reading agreed
2026-09-15, and eleven Supplementary Notice Papers. Consideration in Detail is the
stage at which amendments are moved. So B-01 and B-02 — both high-severity
findings about drafting — may already have been repaired, and this register cannot
say. Entry EM-1 of the external-modifications register carries the same point in
the sweep's own terms.

**What does not change.** The encoding, the assertions and the validated registers
are all correct *about the as-introduced print*, and the print is a real,
digest-pinned, independently corroborated text. Nothing has to be rebuilt; the
diff has to be done.

**Repair, in order.**

1. Obtain `Bill+47-1.002.pdf` — via the browser's save dialog, or from the
   Parliament by another route — and diff it against `sources/bill-47-1.txt`.
2. If the prints differ, re-run the findings against the later text before
   reporting any of them outward. Re-pin `registers/source-bundle.json` to the new
   document and close EM-1.
3. If they do not differ, rename the local file to match its contents and record
   that the Assembly passed the Bill unamended — which is itself the answer EM-1
   is asking for.
4. Either way, read SNP 47-11 before treating any finding as current.


---

# Findings in the Bill

Source: `sources/bill-47-1.txt`, extracted with `pdftotext -layout` from
`Bill+47-1.002.pdf` (sha256 `bc504a51…f9fb73`). Line numbers below are lines of
that extract; section numbers are the Bill's own.

Each finding states a **worked scenario** — the facts on which the provision gives
the wrong answer or no answer. Where the scenario is mechanisable it is marked
*(assertion pending)*: the L4 encoding will carry an `#ASSERT` that demonstrates it,
and until that assertion exists the finding is argued rather than reproduced.

---

## B-01 — s. 39(2): no power to dismiss a cancellation application heard in the respondent's absence

- **Status:** OPEN · **Class:** logical gap · **Severity:** high · **REPRODUCED** — `rbo-cases.l4`, § `B-01`

**Provisions.** s. 34(3), s. 38(1), s. 39(1)–(2), s. 41(1).

Section 39 confers the court's powers on an application to vary or cancel, and it
splits them by which section fixed the hearing:

> **39(1)** At a hearing fixed under section 37 the court may make an order —
> (a) dismissing the application to vary or cancel the RBO; or (b) subject to
> subsection (4), varying the RBO; or (c) cancelling the RBO.
>
> **39(2)** At a hearing fixed under section 38(1)(a) the court may make an order
> cancelling the RBO.

A s. 38 hearing is the one route the Bill provides for a cancellation application
that the RBO applicant has asked (under s. 34(3)) to have heard **in the absence of
the person who is bound**. At that hearing the only order s. 39 authorises is
cancellation. **There is no power to dismiss the application.**

**Worked scenario.** A retail employer obtains an RBO, then applies to cancel it
under s. 33(a) and specifies under s. 34(3) that it be heard in the person's
absence. A registrar fixes a hearing under s. 38(1)(a) and does not summons the
person bound (s. 38(1)(b) is discretionary). At the hearing the court is **not**
satisfied the RBO should be cancelled — say the s. 39(3) matters (ss. 12–14 applied
as if the court were considering making the RBO) still point to a real risk to other
retail workers on the premises. The court declines to cancel. The application is now
undetermined and s. 39 gives the court nothing to do with it.

**Why this is not answered elsewhere.** Section 41(1) supplies a dismissal power for
a hearing fixed under s. 37 **or 38(1)(a)**, but only where the applicant *does not
attend*. So the Bill expressly contemplates dismissal at a s. 38 hearing, and
supplies it only for non-attendance — which makes the omission on the merits look
like an oversight rather than a deliberate restriction. `grep` confirms s. 38 is
referred to exactly twice in the Bill, at s. 39(2) and s. 41(1) (lines 1886, 1945).

**Contrast.** The parallel provision for a s. 37 hearing, s. 39(1)(a), has the
dismissal power. The two subsections were plainly drafted together; (2) is (1) with
the variation limb and the dismissal limb both removed, and only the removal of the
variation limb has an evident purpose (a s. 38 hearing arises only on a
*cancellation* application).

**Possible cure, and why it does not close the finding.** Section 45 applies the
Magistrates Court (Civil Proceedings) Act 2004 practice and procedure, which may
supply a general power to dispose of an application; and "may make an order
cancelling" implies a discretion not to. Neither tells the court what becomes of the
application when the discretion is exercised against cancellation. Section 35(2)(a)
shows the drafter's own vocabulary for this — "or the application to vary is
otherwise determined" — and no equivalent appears for s. 38.

**Suggested repair.** Give s. 39(2) the same two limbs as s. 39(1): "may make an
order — (a) dismissing the application to cancel the RBO; or (b) cancelling the RBO."

---

## B-02 — s. 63: the firearms notification chain fails unless a police officer serves the order

- **Status:** OPEN · **Class:** coverage gap · **Severity:** high · **REPRODUCED** — `rbo-cases.l4`, § `B-02`

**Provisions.** s. 54(2), s. 55(2), s. 57(6), s. 63(2), s. 63(4)–(6).

Section 63 is the public-safety mechanism for an RBO that prohibits possession of a
firearm item. It works in three steps: a police officer asks the restrained person
the s. 63(2)(a) questions and completes the **police copy** of the order; the
Commissioner of Police, **on receipt of the police copy**, notifies the responsible
person and any co-licensee (s. 63(4)); and those people then commit offences under
s. 63(5) and (6) if they allow the restrained person access to a firearm item.

Every step after the first is conditioned on the first. But s. 63(2) binds only:

> A **police officer** who serves a firearms RBO **personally** or effects
> substituted service of a firearms RBO under section 56(3) or 57(5) **orally** …

Three routes of lawful service fall outside it.

**Worked scenario A — personal service by a non-police officer.** Section 55(2)
permits personal service of a relevant order by a registrar of the court, a person
authorised by a registrar, a **custodial officer** or a **prison officer**, as well
as by a police officer. Suppose the person bound is in custody and a prison officer
effects personal service of a firearms RBO. Service is good (s. 55(2)(e)). No
s. 63(2)(a) questions are asked, because a prison officer is not a police officer.
No police copy is completed, so nothing reaches the Commissioner under s. 63(4), so
the responsible person and co-licensee are never notified, so neither can commit the
s. 63(5) or (6) offence. The restrained person's employer — who may hold the
firearms authorisation for the firearm the person uses at work — is never told.

**Worked scenario B — substituted service other than orally.** Section 57(6) lets
the regulations prescribe substituted service (a) orally, (b) by post, or (c) by
email, text message or other electronic means. A senior police officer approves
substituted service by post under s. 57(1). A police officer posts the order. Service
is effective (s. 57(5)). Section 63(2) does not bite, because it reaches substituted
service only where effected **orally**. Same consequence as scenario A.

**Worked scenario C — service deemed by presence in court.** Under s. 54(2), where
the person bound is present in court when the order is made, the order is taken to
have been served personally on them when it is made. There is no server at all, so
no one is under a s. 63(2) duty. This is the commonest case for an RBO made at a
hearing the respondent attends, and it is the case in which the person is most
plainly identified and most easily questioned.

**Why this is a finding and not a policy choice.** The Bill makes the s. 63(5)/(6)
offences turn on notification "under subsection (4)", and s. 63(4) turns on "receipt
of the police copy". A gap in the first step is therefore not a gap in paperwork; it
silently disables two offence provisions and the safety purpose behind them.

**Suggested repair.** Attach the s. 63(2) duty to whoever effects service of a
firearms RBO, not to police officers alone; and extend it to every form of
substituted service, with a mechanism for the questions to be put where service is by
post or electronic means, and where s. 54(2) deems service in court, put the
questions to the person in court.

---

## B-03 — s. 63(1): `corresponding law` is defined for States and Territories and then used for the Commonwealth

- **Status:** OPEN · **Class:** clerical / definitional · **Severity:** medium

**Provision.** s. 63(1), lines 2811 and 2858.

The definition:

> **corresponding law**, in relation to **another State or a Territory**, means a
> law of that State or Territory that empowers a court of that State or Territory to
> make orders (however described) having an effect that is the same as or similar to
> the effect of restraining orders made under the Restraining Orders Act 1997;

The sole use, inside the definition of `responsible person` in the same subsection:

> (b) if the restrained person is otherwise employed or engaged by an employing
> authority, as defined in the Public Sector Management Act 1994, (or an equivalent
> body for the purposes of a **corresponding law of another State, a Territory or
> the Commonwealth**) — that employing authority (or equivalent body);

**Worked scenario.** The restrained person is a Commonwealth employee — say an
Australian Border Force officer who uses a firearm in the course of their usual
occupation. To identify the `responsible person`, the reader must find "an
equivalent body for the purposes of a corresponding law of … the Commonwealth". The
defined term has no operation in relation to the Commonwealth, because the definition
is expressly framed "in relation to another State or a Territory". The reader is left
either to apply a defined term outside its stated domain or to read "corresponding
law" in its undefined ordinary sense in the one place it appears. Neither is what
the Bill says.

**A second, independent oddity in the same definition.** `Restraining Orders
Act 1997` appears exactly once in the whole Bill — here (line 2819). Equivalence is
therefore measured against *restraining orders*, not against RBOs, in an Act whose
entire subject is RBOs. A State or Territory law that makes RBO-equivalent orders but
has no restraining-order analogue would not be a corresponding law. The most likely
explanation is that s. 63 was adapted from the firearms-notification provisions of
the Restraining Orders Act 1997 and this definition was carried across unrevised —
which, if right, is worth checking across the rest of s. 63 as well.

**Suggested repair.** Either widen the definition ("in relation to another State, a
Territory or the Commonwealth, means a law of that jurisdiction …") or narrow the
use. And confirm whether the intended comparator is restraining orders or retail
barring orders.

---

## B-04 — no duty to notify the Commissioner of Police when an RBO is made

- **Status:** OPEN · **Class:** coverage gap · **Severity:** medium

**Provisions.** s. 19, s. 32(2)(c), s. 43(1)(c)(ii), s. 43(2)(b), s. 63(4),
s. 70(2)(i).

The Bill imposes a duty to notify the Commissioner of Police at every later point in
an RBO's life:

| event | provision | line |
| --- | --- | --- |
| set-aside order made | s. 32(2)(c) | 1653 |
| RBO varied | s. 43(1)(c)(ii) | 2009 |
| RBO cancelled | s. 43(2)(b) | 2017 |

It imposes none when the RBO is **made**. Section 19 requires a registrar only to
prepare the order and cause it to be served. The only route by which the Commissioner
learns of a new RBO is s. 70(2)(i) — a matter the rules of court **may** provide for,
not a statutory duty.

**Worked scenario.** A firearms RBO is made and served. Section 63(4) obliges the
Commissioner to notify the responsible person and co-licensee "on receipt of the
police copy" — but no provision requires the police copy to reach the Commissioner
unless rules of court are made under s. 70(2)(i). If the rules are silent or delayed,
the Commissioner's own duty has no trigger, and the notification chain in B-02 fails
for a second, independent reason.

**The asymmetry is the argument.** A drafter who thought the Commissioner did not
need to know about RBOs would not have written three separate notification duties for
variation, cancellation and set-aside. The likeliest reading is that the making case
was assumed to be covered by the rules of court, and the assumption was not written
down as a duty.

---

## B-05 — s. 39(3) applies s. 14 to variation and cancellation, but nothing tells the Commissioner a hearing is on foot

- **Status:** OPEN · **Class:** coverage gap · **Severity:** low–medium

**Provisions.** s. 14(1), s. 39(3).

Section 39(3) provides that when the court is considering whether to vary or cancel
an RBO, "sections 12 to 14 apply as if the court were considering whether to make the
RBO". Section 14(1) therefore obliges the Commissioner of Police to give the court,
where practicable, any criminal record of the person.

**Worked scenario.** The person bound applies to vary the RBO, is granted leave under
s. 36(2)(a), and a hearing is fixed under s. 37(2) summonsing the RBO applicant. The
Commissioner is not a party, is not summonsed, and no provision requires anyone to
notify the Commissioner that a variation hearing has been fixed. The s. 14 duty, as
applied by s. 39(3), has no trigger. "Where practicable" carries the weight: a duty
the duty-holder cannot know has arisen is never practicable to perform.

Compare s. 32(2)(c), which *does* require the Commissioner to be notified when a
set-aside order is made — the one place the Bill anticipates that the Commissioner
needs to know a rehearing is coming.

---

## B-06 — s. 29(4)(b) summonses the applicant but omits the person on whose behalf the application was made

- **Status:** OPEN · **Class:** clerical inconsistency · **Severity:** low

**Provisions.** s. 28(2)(b)–(c), s. 29(4)(b), s. 31(2)(a), s. 31(3), s. 32(1)(a).

Section 28(2) allows a set aside application to be made **on behalf of** the person
who was the respondent — by a responsible adult where that person is a child
(s. 28(2)(b)), or by a guardian appointed under the Guardianship and Administration
Act 1990 (s. 28(2)(c)).

Every later provision in Division 6 carries both limbs of that distinction:

> **31(2)(a)** … the person who made the set aside application, **or on whose behalf
> the application is made** …
>
> **31(3)** … the person who made the set aside application, **or on whose behalf the
> application is made**, had a reasonable excuse …
>
> **32(1)(a)** … the person who made the set aside application, **or on whose behalf
> the application is made** …

Section 29(4)(b) does not:

> (4) If a set aside application is made, a registrar must — (a) fix a hearing; and
> (b) summons **the person who made the application** to attend the hearing.

**Worked scenario.** A responsible adult makes a set aside application on behalf of a
14-year-old. The registrar summonses the responsible adult. The child — whose RBO it
is, and whose "reasonable cause not to attend" the court must assess under
s. 31(2)(a) — is not summonsed to the hearing at which that assessment is made.

**Severity.** Low, because s. 47 separately requires a responsible adult to attend
child-related RBO proceedings and the practical effect may be the same. It is
recorded because the phrase "or on whose behalf the application is made" appears
three times in the four sections that surround s. 29(4)(b), and its absence there is
more likely an omission than a choice.

---

# Verified — no defect

Checked because they look wrong, and are not. Recorded because knowing what was
checked is part of the result.

## V-01 — s. 29(1)(a) vs s. 30: a set aside application in the Magistrates Court over a Children's Court decision

Section 29(1) routes a set aside application to the Children's Court "if the person
who was the respondent to the RBO application **is** a child" and otherwise to the
Magistrates Court. Section 30 then addresses the case where the application is made
to the **Magistrates** Court but the **Children's** Court made the decision — which
looks impossible on s. 29(1).

It is not. Section 29(1)(a) is in the present tense, and s. 27's application period
runs 21 days from service of the RBO, with s. 31(3) contemplating applications made
outside it. A respondent who was 17 when the RBO was made and is 18 when the set
aside application is made is no longer "a child", so the application goes to the
Magistrates Court while the Children's Court holds the record. Section 30 is exactly
the transfer provision that case needs, and s. 48 handles the mirror case — the
person turning 18 while an application is still pending.

## V-02 — s. 51(9) protects against s. 49 only, not s. 50

Section 51(5) permits a person acquitted of persistent breach to be found guilty of
offences against s. 49 **or 50**; s. 51(9) bars that route for s. 49 where the
persistent-breach prosecution began after the s. 49 limitation period had run, and
says nothing about s. 50.

The asymmetry is correct. Section 49 creates a simple offence, subject to the
Criminal Procedure Act 2004 limitation on commencing a prosecution. Section 50(2)
creates a **crime**, for which no such limitation runs. There is no s. 50 limitation
period for s. 51(9) to protect against.

## V-03 — s. 35 does not apply to an RBO with no specified period

Section 35 extends an RBO pending determination of an extension application, but only
where the RBO "specifies its duration". An RBO with no specified period appears to be
left out.

It is correctly left out. Under s. 21(3)(b)–(c) an RBO with no specified period runs
for the statutory maximum — 2 years for an adult, 1 year for a child — and s. 40(2)
caps the total period of a varied RBO at those same figures. Such an RBO is already
at the ceiling and cannot be extended at all, so there is nothing for s. 35 to
preserve.
