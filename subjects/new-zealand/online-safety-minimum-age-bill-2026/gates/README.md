# gates/ — human review grants

**State: HG1 prepared, not granted.** `HG1.payload.txt` exists; `HG1.payload.sig` does not,
and `allowed_signers` carries no key. `subject.json` therefore declares `status: draft`.

This is the first `gates/` directory in the corpus — no other subject has one yet — so the
mechanics below are written out in full. They follow the repository README's verification
command exactly; nothing here invents a new scheme.

## What HG1 means

Per the repository README's status vocabulary: *"a named domain expert has signed HG1: the
encoding is isomorphic to its source."* The statement the signer makes is written into
`HG1.payload.txt` itself, so that what was signed is not a matter of recollection. It covers
fidelity of the encoding to the Bill, and explicitly not the merits of the Bill.

HG2 is referenced in the repository README and in `subjects/README.md` but is not defined
anywhere in this repository. No HG2 artifact is prepared here.

## Why there is no signature

An agent prepared this payload. **Agents can verify signatures; they cannot make them** — the
repository README says so, and the point of the gate is that a person, not a process, put their
name to a reading of the Bill. A signature produced by the same process that wrote the encoding
would certify nothing.

The absence of `HG1.payload.sig` is therefore the correct state, not an omission to be tidied
away. Per the README, a waiver would equally be on the record: *"a waiver is a verdict with a
reason attached, never an absence."*

## Scope of the digest

The payload lists sha256 digests for 13 files: the nine `.l4` modules, `subject.json`,
`NOTES.md`, `SOURCE-LICENSE.md`, and the source XML the encoding was made from. Deliberately
out of scope are `registers/coverage-register.md`, `registers/incident-register.xlsx` and
`report/` — these are evidence *about* the encoding, and they will change as findings are
triaged, which would break a signature that covered them.

## To grant HG1

The reviewer reads each rule against the clause it cites — `registers/coverage-register.md`
gives the clause-to-module map, and `report/conversion-report.md` section 4 lists the
interpretation calls that need accepting or rejecting. Then, from the subject directory:

```bash
sha256sum -c <(sed -n '/^files (sha256):$/,/^$/p' gates/HG1.payload.txt | tail -n +2)
```

to confirm the payload still describes the files on disk, and then:

```bash
ssh-keygen -Y sign -f ~/.ssh/id_ed25519 -n l4-go-gate gates/HG1.payload.txt
```

which writes `gates/HG1.payload.txt.sig`. Rename it to `gates/HG1.payload.sig`, then add the
signer to `gates/allowed_signers` in the format:

```
reviewer@example.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA...
```

Finally set `"status": "reviewed"` in `subject.json` and commit all three changes together.

## To verify a granted HG1

```bash
ssh-keygen -Y verify -f gates/allowed_signers -I <signer> -n l4-go-gate \
  -s gates/HG1.payload.sig < gates/HG1.payload.txt
```

Edit any listed file and the digest changes, the signature stops verifying, and the grant is
visibly stale. That is the intended behaviour: the grant binds to content, not to a version
number.

## Before signing, know what is not yet done

`report/conversion-report.md` section 7 lists it: no independent fidelity pass has been made
over this encoding. Machine evaluation is clean — 64 of 64 assertions, 0 type errors — but a
rule can typecheck and still say something the Bill does not. HG1 is the assertion that it
does not, and that assertion has not yet been tested by anyone other than the encoder.
