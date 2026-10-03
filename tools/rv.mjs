#!/usr/bin/env node
// rv.mjs -- a read-only wrapper around l4-ide's register validator.
//
// WHY THIS EXISTS. `etc/go/lib/register-validate.mjs` guards its CLI block with
//     if (import.meta.url === `file://${process.argv[1]}`)
// which is never true on Windows, so the script exits 0 having printed nothing
// (incident H-01). The VALIDATION LOGIC is fine -- only the entry point is
// unreachable. This wrapper imports the module's own exported
// `validateInstance` and calls it directly, so the oracle that runs is
// l4-ide's, byte for byte, and nothing in l4-ide is modified.
//
// It is deliberately NOT a substitute for the stage. `p1-ingest` and friends
// write a RECEIPT, and the receipt is the fact; this prints a verdict to a
// terminal and nothing records it. Treat its output as an inner-loop check,
// never as evidence.
//
// Usage:
//   node rv.mjs <schema-name> <file> [peer-file ...]
//   node rv.mjs --rules <schema-name>
//   node rv.mjs --names
//
// Schema names: source-bundle | external-modifications | fork-register
// Peers are identified by their own `kind` field, matching the way the real
// CLI pairs them, so the cross-file joins actually run.
//
// Exit: 0 clean, 1 findings, 2 usage/IO error.

import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

const L4_IDE = process.env.L4_IDE_ROOT ?? "C:/Users/micha/l4-ide";
const MOD = pathToFileURL(
  resolve(L4_IDE, "etc/go/lib/register-validate.mjs"),
).href;
const SCHEMA_DIR = resolve(L4_IDE, "specs/todo/single-instruction-demo/schemas");

const { validateInstance, SCHEMA_NAMES } = await import(MOD);

function die(msg) {
  process.stderr.write(`rv: ${msg}\n`);
  process.exit(2);
}

function readJson(p) {
  try {
    return JSON.parse(readFileSync(p, "utf8"));
  } catch (e) {
    die(`${p}: ${e.message}`);
  }
}

const argv = process.argv.slice(2);
if (argv.length === 0) die("usage: rv.mjs <schema> <file> [peer ...]");

if (argv[0] === "--names") {
  process.stdout.write(SCHEMA_NAMES.join("\n") + "\n");
  process.exit(0);
}

if (argv[0] === "--rules") {
  const name = argv[1] ?? die("--rules needs a schema name");
  const schema = readJson(resolve(SCHEMA_DIR, `${name}.schema.json`));
  for (const r of schema["x-rules"] ?? [])
    process.stdout.write(
      `${r.id}\t${r.peer ? `[peer:${r.peer}] ` : ""}${r.description ?? ""}\n`,
    );
  process.exit(0);
}

const [name, file, ...peerFiles] = argv;
if (!SCHEMA_NAMES.includes(name))
  die(`unknown schema '${name}'; known: ${SCHEMA_NAMES.join(", ")}`);
if (!file) die("no instance file given");

const doc = readJson(file);

// Pair each peer by its own declared `kind`. Withholding a peer is legitimate
// -- the joins that needed it then report `skip` with a reason, which is the
// behaviour the real validator has and the reason it is worth preserving.
const peers = {};
for (const p of peerFiles) {
  const pdoc = readJson(p);
  const kind = pdoc.kind ?? null;
  if (!kind) die(`${p} has no 'kind' field, so it cannot be paired as a peer`);
  if (!SCHEMA_NAMES.includes(kind)) die(`${p}: unknown kind '${kind}'`);
  peers[kind] = { path: p, doc: pdoc };
}

const { findings, skips, rulesRun, structuralOnly } = validateInstance(
  name,
  doc,
  file,
  peers,
);

const w = (s) => process.stdout.write(s + "\n");

w(`schema:   ${name}`);
w(`instance: ${file}`);
if (Object.keys(peers).length)
  w(`peers:    ${Object.entries(peers).map(([k, v]) => `${k}=${v.path}`).join(", ")}`);
else w(`peers:    (none given -- peer joins will skip)`);
w("");

if (findings.length) {
  w(structuralOnly
    ? `STRUCTURAL FINDINGS (${findings.length}) -- x-rules not run, because a shape`
      + ` the rules assume is wrong and running them would bury this:`
    : `FINDINGS (${findings.length}):`);
  for (const f of findings)
    w(`  ${f.path || "(root)"}  ${f.message}${f.rule ? `   [${f.rule}]` : ""}`);
  w("");
}

if (skips.length) {
  w(`SKIPPED RULES (${skips.length}) -- these checked NOTHING:`);
  for (const s of skips) w(`  ${s.rule}: ${s.why}`);
  w("");
}

w(`rules run: ${rulesRun}`);
w(findings.length ? "VERDICT: FINDINGS" : "VERDICT: CLEAN");
process.exit(findings.length ? 1 : 0);
