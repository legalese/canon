# The encoding pipeline: stages, gates and what each one certifies

This is the process an encoding passes through, and what a human is attesting to when they let it
move. It is written down here, once, because until now it lived in one subject's `gates/README.md`
and in people's heads.

The repository README defines the *status vocabulary* (`draft`, `adversarially-reviewed`,
`reviewed`) and the *signature mechanics*. This file defines the *stages*, the artifacts each
stage produces, and the two human gates. Where this file and the repository README disagree, the
README wins and this file is wrong and should be fixed.

## The five stages

| # | Stage | Who | Artifact that proves it happened |
|---|---|---|---|
| 1 | **Indexed** | agent | `subject.json`, `SOURCE-LICENSE.md`, `registers/source-bundle/*.meta.json` |
| 2 | **AI pass #1** | agent | the `.l4` modules, `registers/coverage-register.md`, `registers/incident-register.xlsx`, `report/conversion-report.md`, `report/machine-evaluation.md` |
| 3 | **Human pass #1** | person | `reviews/human-1.md` |
| 4 | **AI pass #2** | agent | `reviews/ai-2.md` |
| 5 | **Human pass #2** | person | `gates/HG1.payload.sig` (or a recorded waiver) |

`tools/review-queue.py` derives a subject's stage from exactly these files, so a stage that leaves
no artifact did not happen.

Source text must be deposited before stage 2, and only where the jurisdiction's licence permits it
(`tools/worker/config.json` holds the decision). Metadata-only subjects stop after stage 1.

### `reviews/human-1.md`

First line, exactly one of:

```
Verdict: approve
Verdict: changes requested
```

Then the reviewer's points, numbered. Each point should name the module and the rule or the section
of the source it concerns. A reviewer may raise a point without proposing a fix: identifying the
problem is the job.

### `reviews/ai-2.md`

Answers every numbered point in `human-1.md`, in order, as one of:

- **fixed** — with the change made, and the rule or file it touched;
- **disagreed** — with the reason, in terms of the source text;
- **deferred** — with the incident number it was recorded as.

An agent may not close a point by asserting the reviewer is mistaken without citing the source.

## The two gates

A gate is a statement a **named person** makes, signed with their own key over a digest of specific
files. The signature binds to content: edit a covered file and the grant visibly stops verifying.
**Agents may prepare a payload; agents never sign.** A signature made by the process that produced
the work certifies nothing.

A waiver is a verdict with a reason attached, never an absence. A waiver is recorded in the same
directory as `HG1.waiver.md` or `HG2.waiver.md`, is signed the same way, and says what was not
checked and why that was acceptable.

### HG1 — fidelity

**The statement:** *the encoding is isomorphic to its source: each rule says what the provision it
cites says, and the encoding neither adds nor omits legal effect.*

HG1 is about fidelity, never about the merits of the law. A signer who thinks the law is bad policy
still signs HG1 if the encoding is faithful; that is what makes the encoding usable for quality
assurance at all.

- **Who may sign:** someone who can read the source in its authoritative language and knows the
  field. Their key goes in `gates/allowed_signers`.
- **Covered by the digest:** the `.l4` modules, `subject.json`, `NOTES.md`, `SOURCE-LICENSE.md`,
  and the deposited source text the encoding was made from.
- **Deliberately not covered:** `registers/incident-register.xlsx`, `registers/coverage-register.md`
  and `report/` — they are evidence *about* the encoding and change as findings are triaged, which
  would break the signature for no reason.
- **Effect:** `subject.json` may be set to `status: reviewed`.

**Translated sources.** Where the authoritative text is not in the language the encoders worked in,
the payload must name the chain — authoritative text → any consolidation → any translation → L4 —
and the signer must attest to reading the **authoritative** text. Certifying an encoding against a
working translation certifies the translation, not the law. (Israel is the live case: Hebrew
governs, the consolidation is unofficial, and the English translation is an aid.)

### HG2 — outward-facing release

**The statement:** *this material is fit to go outside the project under the project's name: its
claims are supported by the encoding and the source, its limits are stated, and the people named in
it are correctly described.*

HG2 gates publication, not encoding. It is required before: sending findings to a legislature, a
ministry, a regulator or a drafting office; publishing a report, a page or a paper; making any
public claim that a law contains a defect; and any outward use of the corpus that names a
jurisdiction's drafting.

- **Who may sign:** the person accountable for the project's external communications. For
  `legalese/canon` today that is the repository owner or a maintainer they name.
- **Covered by the digest:** the artifact being released, plus the incident register and conversion
  report at the moment of release — because those are what the claims rest on.
- **Not implied by HG1:** a faithful encoding can still support an overstated claim. The two gates
  answer different questions and are signed separately.
- **HG2 may be granted where HG1 was not**, provided the release says so. Publishing "we encoded
  this and found these candidate defects, unreviewed" is honest; publishing it as verified is not.

**Findings about a real Bill or Act name a real drafting office.** Say what was checked, what was
not, and the date and version of the text. An incident is a candidate defect until a person has
agreed with it: the register's severity and status columns carry that distinction, and a release
must not collapse it.

## Granting a gate

From the subject directory, confirm the payload still describes the files on disk:

```bash
sha256sum -c <(sed -n '/^files (sha256):$/,/^$/p' gates/HG1.payload.txt | tail -n +2 | sed '/^$/d')
```

Sign it, with the namespace `l4-go-gate`:

```bash
ssh-keygen -Y sign -f ~/.ssh/id_ed25519 -n l4-go-gate gates/HG1.payload.txt
mv gates/HG1.payload.txt.sig gates/HG1.payload.sig
```

Add the signer to `gates/allowed_signers`, one line, `<identity> <keytype> <base64 public key>`.
Then set `subject.json` `status` and commit the signature, the signers file and the status together.

Verify any grant, which anyone may do, including agents:

```bash
ssh-keygen -Y verify -f gates/allowed_signers -I <signer-identity> -n l4-go-gate \
  -s gates/HG1.payload.sig < gates/HG1.payload.txt
```

`gates/README.md` in each subject records that subject's state. The mechanics above were smoke
tested on 2026-09-23 with a disposable key: signing, verification, rejection of a tampered payload,
rejection of a signer absent from `allowed_signers`, rejection of a wrong namespace, and a failing
digest check after a covered file was edited all behaved as described. No agent has ever
held a signing key for this corpus, and none should.

## Quality assurance on a Bill or a live Act

Legislative quality assurance is the pipeline plus one discipline: **every finding is traceable to a
provision and reproducible by machine.** An incident that cannot be demonstrated by an assertion or
a worked scenario is an opinion, and belongs in the conversation, not the register.

The register carries, per incident: an id (`#1`, `#2`, … per subject), the provision, what the
drafting says, what it appears to mean, why that is a defect, the severity, whether it is confirmed
or a candidate, and the scenario or assertion that demonstrates it. Findings that turn out to be
correct drafting are kept, marked as verified-no-defect: knowing what was checked and found sound is
part of the result.

Release of any of that is an HG2 act.
