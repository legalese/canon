#!/usr/bin/env node
/* Bundle the Sim One console's data: the cradle-to-grave facts file and the requirement ledger,
   written as one JS file so index.html opens from disk with no server and no fetch.
   Run after either source changes:  node tools/society-sim/console/build.js  */
"use strict";
const fs = require("fs");
const path = require("path");

const here = __dirname;
const root = path.resolve(here, "..", "..", "..");
const factsPath = path.join(root, "subjects", "sg", "scenarios", "cradle-to-grave-simone", "facts.json");
const ledgerPath = path.join(root, "subjects", "sg", "requirements.jsonl");

const facts = JSON.parse(fs.readFileSync(factsPath, "utf8"));
const ledger = fs.readFileSync(ledgerPath, "utf8").split("\n").filter(l => l.trim() && !l.startsWith("#"))
  .map(l => JSON.parse(l));

// which encoding rows exist right now, so the console can say what the library held when it was built
const sg = path.join(root, "subjects", "sg");
const rows = {};
for (const slug of fs.readdirSync(sg)) {
  const enc = path.join(sg, slug, "encodings");
  if (!fs.existsSync(enc) || !fs.statSync(enc).isDirectory()) continue;
  const names = [];
  const walk = d => { for (const f of fs.readdirSync(d)) { const p = path.join(d, f);
    if (fs.statSync(p).isDirectory()) walk(p); else if (f === "encoding.json" || f.endsWith(".l4")) names.push(path.relative(enc, d) || "."); } };
  walk(enc);
  if (names.length) rows[slug] = [...new Set(names)];
}

const out = { built: new Date().toISOString().slice(0, 10), facts, ledger, rows };
fs.writeFileSync(path.join(here, "data.js"), "window.SIM_DATA = " + JSON.stringify(out) + ";\n");
console.log(`data.js: ${facts.events.length} events, ${ledger.length} ledger entries, ${Object.keys(rows).length} subjects with rows`);
