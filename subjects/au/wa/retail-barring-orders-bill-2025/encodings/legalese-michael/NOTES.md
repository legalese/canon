# retail-barring-orders-bill-2025 — notes

Free prose. Nothing here is read by a script; it is the place for the things
about this subject that do not fit a schema, and that a later reader would
otherwise have to rediscover.

## This is a Bill, and it is still moving

Not an Act. As at 2026-09-23 it has passed the Legislative Assembly (Consideration
in Detail and Third Reading, both 2026-03-12) and been agreed at second reading in
the Legislative Council (2026-09-15), with eleven Supplementary Notice Papers
issued. Clause 2 commences Part 1 on Royal Assent and the rest on proclamation, so
even assent would not bring the operative Parts into force.

Nothing in this directory should be quoted as law.

## The text we hold is the *as introduced* print

Read **C-01** in `INCIDENTS.md` before doing anything with the encoding. In short:
the file is named `Bill+47-1.002.pdf`, which is the Parliament's filename for the
Bill *as passed by the originating House*, but its sha256 is byte-identical to the
Internet Archive's capture of the *as introduced* print. Every finding here is a
finding about the as-introduced text, and Consideration in Detail is exactly the
stage at which the drafting defects B-01 and B-02 would have been repaired if
anyone noticed them.

The as-passed print could not be retrieved: `parliament.wa.gov.au` answers an
Azure WAF JavaScript challenge to `curl`, the in-app browser turns the link into a
save dialog, and the Internet Archive has no capture of that file.

## Running anything here

This subject is a **corpus**, not a pipeline run. `etc/go/subjects/retail-barring-orders-bill-2025/`
exists in l4-ide as a sidecar, but no stage has ever run over it and no receipt
exists, for two reasons recorded as H-01 and H-02:

- `go.sh` cannot resolve any subject on Windows (`GO_S_ENCODING: unbound variable`),
  because every `etc/go/lib/*.mjs` CLI entry guard compares `import.meta.url`
  against `` `file://${process.argv[1]}` ``, which is never true there;
- and `core.autocrlf=true` with no `.gitattributes` means every digest the pipeline
  would take is a digest of different bytes than the ones committed.

So the artifacts here were produced and checked **outside** the driver: `l4 check`
and `l4 run` directly for the encoding, and `tools/rv.mjs` — a read-only wrapper
that imports l4-ide's own `validateInstance` — for the registers. That is an inner
loop, not evidence. There is no journal, no receipt and no verdict, and none of
this has been through HG1.

## The encoding has no library imports, deliberately

The `l4` on this machine ships no standard library (H-04), and an unresolvable
`IMPORT` typechecks clean and exits 0 (H-03) — so an `IMPORT prelude` line would be
a claim the file cannot cash. Everything is written against compiler builtins.

The cost is in `rbo-domain.l4`'s date helpers: `drafting-patterns.md` builds date
windows with `daydate`'s `YMD` / `Date` / `Day`, and those are unavailable, so the
s 8(2) twelve-month window is computed by comparing `DATE_YEAR` / `DATE_MONTH` /
`DATE_DAY` components with the year incremented. The leap edge is worked out in a
comment at the site. **Rewrite both helpers against `daydate` once the library is
installed** — that is the house style and this is not.

`REFUSE` and `TBD` are also absent (H-05), which is why `rbo-cases.l4` falls back
to `FALSE` on the unreachable `NOTHING` arms of its `TODATE` unwrapping instead of
refusing.

## Where the two high-severity findings live

Both are reproduced by assertion in `rbo-cases.l4`, and both have a fork entry
recording the interpretive question underneath them — which is the distinction
worth keeping: *the Bill is ambiguous here* and *the Bill has a gap here* are
different findings with different repairs.

| finding | encoded in | fork |
| --- | --- | --- |
| B-01 — s 39(2) has no power to dismiss | `rbo-part3-varying-or-cancelling.l4` | F-4 |
| B-02 — the s 63 firearms chain breaks on six of nine service routes | `rbo-part5-service-and-firearms.l4` | F-3 |

## What was not done

- The eleven Supplementary Notice Papers, both Explanatory Memoranda, both second
  reading speeches and the Consideration in Detail Hansard were **not read**. The
  coverage notes in `registers/external-modifications.json` say so in the register's
  own terms.
- Parts 4, 6 and 7 of the Bill, and much of Part 2 Divisions 4–6, are **not
  encoded**. The encoding covers what the two findings needed plus enough of the
  spine (ss 5, 6, 8, 10, 11, 21, 39, 54–57, 63) to make them meaningful. A coverage
  register would be the next artifact.
- No `#TRACE` and no regulative rules. The Bill is full of duties — ss 18, 19, 22,
  43, 59, 60, 63 — and none is encoded as `PARTY … MUST … WITHIN`. That is the
  obvious next piece of work and the one most likely to surface further findings,
  because the notification duties are where B-04 and B-05 already live.
