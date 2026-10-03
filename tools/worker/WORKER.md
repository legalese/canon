# Canon worker

A **worker** is a scheduled Claude Code run, typically hourly. When its owner's plan has spare
allowance, it does one small, bounded piece of the encoding project and lands it on `main`. Anyone
with push access and unused tokens can run one. Workers coordinate only through git: there is no
server, queue or shared state beyond this repository.

Files:

| File | Who edits it | What it is |
|---|---|---|
| `tools/worker/WORKER.md` | humans | this procedure; a worker follows it step by step |
| `tools/worker/config.json` | humans | policy: allowance ceilings, claim TTL, unit sizes, priority, per-jurisdiction licence and fetch status |
| `tools/worker/next-task.py` | humans | surveys the repo and names the unit a worker should claim; it never claims or writes anything |
| `tools/review-queue.py` | humans | the other side: what is waiting on a *human* |

## The hourly procedure

A worker does these steps in order and **stops at the first one that says stop**. Stopping is the
normal, expected outcome of most runs.

### 1. Gate: is there allowance to spare?

Read the plan usage (in the Claude desktop app, the `get_usage` tool: the "5-hour limit" and
"Weekly · all models" percentages). Stop if either is at or above the ceiling in
`config.json → gate`. The defaults are 80% weekly and 60% for the 5-hour window. A runner may set
**lower** ceilings in their own routine prompt, never higher.

If usage cannot be read, stop. A worker that can't see the allowance must not spend it.

### 2. Sync

```bash
git fetch origin
git switch main && git merge --ff-only origin/main
```

If the fast-forward fails (the local `main` has diverged, or there are uncommitted changes), stop
and leave a note. The working copy belongs to a human.

### 3. Survey and choose

```bash
python tools/worker/next-task.py --weekly-used <W> --five-hour-used <F>
```

This reads every target subject and the live `claim/*` branches on origin. It filters out work that
is claimed, licence-blocked, or has no way to fetch its source. It prints ranked candidates and the
one it **would** claim. The priority order is in `config.json → priority`:

1. **respond_to_review**: a human wrote `reviews/human-1.md` with `Verdict: changes requested`,
   and there is no `reviews/ai-2.md` yet. Answering people comes first.
2. **continue_own_claim**: this runner already holds a live claim. Finish that before taking another.
3. **encode_part**: the subject has open-licensed source text; encode the next Part, or a run of
   small Parts, as listed in `registers/encoding-plan.json`.
4. **fetch_source**: deposit the source text for a subject, but only where the jurisdiction's
   `fetch` is `ready` (a fetcher exists and is allowed).

If it names nothing, stop.

### 4. Claim (the lock)

A claim is a branch on origin named `claim/<jurisdiction>/<subject>`. Creating it is atomic: the
push succeeds only if the branch does not already exist.

```bash
git switch -c claim/<jurisdiction>/<subject> origin/main
git commit --allow-empty -m "claim: <unit> (runner: <name>, until <UTC time + ttl>)"
git push --force-with-lease=refs/heads/claim/<jurisdiction>/<subject>: origin HEAD:refs/heads/claim/<jurisdiction>/<subject>
```

The empty value after the colon in `--force-with-lease=<ref>:` means "only if this ref does not
exist". If the push is rejected, someone else holds the claim. Go back to step 3; `next-task.py`
will now see their branch.

**Expiry.** A claim branch whose newest commit is older than `claims.ttl_hours` (6) is stale. Another
runner may take it over. It pushes its own claim commit on top with
`--force-with-lease=refs/heads/<claim>:<the stale sha>`, so two takeovers cannot both succeed. It
also keeps any real work already on the branch.

**Heartbeat.** A worker that is still working after an hour commits its progress to the claim
branch. That refreshes the timestamp.

### 5. Work: one bounded unit

| Unit | What "done" means |
|---|---|
| encode_part | L4 for the Part(s) named in the unit, in the subject's own module files. `registers/encoding-plan.json` updated (the first unit for a subject writes the plan: every Part, its size, status `todo`). Incidents found go in `registers/incident-register.xlsx` and `NOTES.md` (numbered `#1`, `#2`, … per subject). |
| respond_to_review | `reviews/ai-2.md` answers each point in `reviews/human-1.md`: fixed (with the change made), disagreed (with the reason), or deferred (with an incident number). |
| fetch_source | Text plus a `.meta.json` in `registers/source-bundle/` (URL, retrieval date, as-at date, sha256). `SOURCE-LICENSE.md` records that text is now deposited. |

Follow the subject-sidecar conventions in `subjects/README.md`, with `subjects/new-zealand/online-safety-minimum-age-bill-2026/`
as the worked example. Stay within the one subject directory claimed.

### 6. Check

```bash
l4 check <every .l4 file touched>
l4 run   <every .l4 file touched>     # every #ASSERT holds, 0 errors
```

If the unit cannot be made clean, **do not land broken L4**. Commit what exists to the claim branch
with a note in `NOTES.md` saying where it stopped. Leave the claim to expire, so the next runner can
continue it.

If the subject has `gates/HG1.payload.txt`, regenerate it **last**, after every other change,
because its digests cover the other files.

### 7. Land

```bash
git rebase --no-keep-empty origin/main # onto the latest main, dropping the empty claim commit
git diff --stat origin/main..HEAD      # every path inside subjects/<jurisdiction>/<subject>/
git diff --diff-filter=DR origin/main..HEAD --name-only   # deleted or renamed files: must print nothing
git push origin HEAD:main              # plain push: rejected unless a fast-forward
git push origin --delete claim/<jurisdiction>/<subject>
```

If the push to `main` is rejected because someone else landed first, rebase and try again, at most
3 times. After that, leave the work on the claim branch and stop.

Commit message: `<Act short name>: <what was done>`, e.g. `Long Service Leave Act: encode Parts I-II`.

### 8. Report

End with a short summary: gate figures, what was claimed, what landed (commit sha), incidents
raised, and anything left on a claim branch.

## Never

- **Never sign a gate.** Workers may prepare `gates/*.payload.txt`. Only a human signs (HG1: domain
  expert fidelity; HG2: anything outward-facing).
- **Never deposit or quote statute text** in a subject whose jurisdiction `licence` in `config.json`
  is anything but `open` or `permission`. Victoria and Hong Kong are `not-open`, South Africa is
  `unclear`, and Canada, Ontario, NT and India are `conditional-pending`: these stay metadata-only
  until a human records a decision.
- **Never get around a bot check**, CAPTCHA, rate limit or access refusal. If a register says no,
  the fetch status is `script-blocked` and a human decides what to do.
- **Singapore:** workers do not fetch Singapore Statutes Online at all. The nightly harvester does,
  inside the 03:00-07:00 SGT window that SSO's terms allow.
- **Never touch another runner's claim branch** unless it has expired, and never edit files outside
  the claimed subject. That includes `tools/`, `subjects/README.md` and other subjects.
- **Never push anything to `main` that deletes or rewrites existing work.** Only additive
  fast-forwards. Never force-push `main`.
- **Never commit a human's uncommitted work** found in the working copy.

## How humans take part

- **Review.** `python tools/review-queue.py` lists subjects waiting on a person, oldest first. A
  review is `reviews/human-1.md`, first line `Verdict: approve` or `Verdict: changes requested`.
  Workers pick up "changes requested" before anything else.
- **Licence and fetch decisions.** Edit `config.json → jurisdictions`. Add `"decided_by"` and a date
  when clearing a licence, e.g.
  `"canada": {"licence": "open", "fetch": "not-built", "decided_by": "M Fairweather 2026-09-30"}`.
- **Steering.** Reorder `priority`, lower the gate, or set a jurisdiction's `fetch` back to
  `not-built` to pause work there.
- **Stopping a worker.** Delete its claim branch, or disable the routine.

## Installing a worker

Requirements: push access to `legalese/canon`, the `l4` CLI on `PATH`, Python 3, and a Claude
plan with spare allowance.

Create an hourly scheduled task (Claude desktop app → Code → scheduled tasks, or a Routine) whose
prompt is:

> In the canon repo at `<path>`, follow `tools/worker/WORKER.md` exactly, as runner `<your name>`.
> Use ceilings of at most `<W>`% weekly and `<F>`% 5-hour. Do one unit at most, then stop.

Run it once by hand first, and read what it did.

## Not yet decided

1. **Usage visibility in unattended runs.** `get_usage` works in an interactive desktop session.
   It has not been tested inside a scheduled task, a cloud routine, or someone else's setup. Rule 1
   says stop if it can't be read, so an unsupported setup does nothing rather than overspend.
2. **Local or cloud.** A local task needs the machine awake. A cloud run needs its own clone and
   push credentials.
3. **Agreement from the other maintainers** that `claim/*` branches and worker commits on `main` are
   welcome, and that `tools/` may be committed.
4. **The first fetchers.** Today only the Western Australian topic Acts have text; every other
   jurisdiction's `fetch` is `not-built` or blocked. Until fetchers exist, workers can only encode WA.
