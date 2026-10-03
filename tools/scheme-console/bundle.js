/* ===========================================================================
   Packs each corpus law's text and L4 encoding into corpus/<scheme id>.json,
   which the console's Discussion mode reads so Claude can answer from the text and
   the encoding as well as the scheme.

     node tools/scheme-console/bundle.js

   Run it after an encoding or a source text changes, and before publishing.
   A text is bundled only when its licence is recorded below: the published
   console is shared by link, so bundling a text is publishing it.
   =========================================================================== */
var fs = require("fs"), path = require("path");
var root = path.join(__dirname, "..", "..");
var out = path.join(__dirname, "corpus");

var SUBJECTS = [
  {
    scheme: "dog-act",
    dir: "subjects/western-australia/dog-act-1976",
    l4: ["."],
    texts: [
      { file: "registers/source-bundle/mrdoc_47983.txt", title: "Dog Act 1976 (WA), compilation 08-b0-00 (28 Nov 2024)",
        licence: "Sourced from the Western Australian Legislation website at 2026-09-07: “Dog Act 1976”, State of Western Australia, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)." }
    ]
  },
  {
    scheme: "cat-act",
    dir: "subjects/western-australia/cat-act-2011",
    l4: ["."],
    texts: [
      { file: "sources/cat-act-2011-00-l0-01.txt", title: "Cat Act 2011 (WA), compilation 00-l0-01 (from 25 Sep 2025)",
        licence: "Sourced from the Western Australian Legislation website at 2026-09-30: “Cat Act 2011”, State of Western Australia, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)." },
      { file: "sources/cat-regulations-2012.txt", title: "Cat Regulations 2012 (WA), version 02-b0-00",
        licence: "© State of Western Australia 2025, licensed under CC BY 4.0, as the compilation itself states. Sourced from the Western Australian Legislation website." },
      { file: "sources/em-cat-bill-2011-extract.txt", title: "Explanatory Memorandum, Cat Bill 2011 (extract)", licence: null }
    ]
  },
  {
    scheme: "rbo-bill",
    dir: "subjects/western-australia/retail-barring-orders-bill-2025",
    l4: ["."],
    texts: [
      { file: "sources/bill-47-1.txt", title: "Retail Barring Orders Bill 2025 (WA), print 47-1, as introduced (superseded; see the subject’s source-bundle.json)",
        licence: null }
    ]
  },
  {
    scheme: "rta-rent-cap",
    dir: "subjects/western-australia/residential-tenancies-act",
    l4: ["LQA", "."],
    texts: [
      { file: "LQA/sources/bill-70-1.txt", title: "Residential Tenancies Amendment (Rent Cap) Bill 2026 (WA), print 70-1", licence: null },
      { file: "LQA/sources/act-rta-1997-r84-part5-excerpt.txt", title: "Residential Tenancies Act 1987 (WA), Part V excerpt", licence: null },
      { file: "LQA/sources/em.txt", title: "Explanatory Memorandum to the Rent Cap Bill", licence: null }
    ]
  }
];

/* the section numbers a piece of text mentions, and how often: "s. 29(8)", "ss. 7, 15",
   "s.31AA", "cl. 4", "r. 3". The count lets the module that encodes s. 29 outrank one that
   merely cites it. */
function citedSections(txt) {
  var found = {}, re = /\b(?:ss?|sections?|cl|clauses?|r|regs?)\.?\s*(\d+[A-Z]{0,3})((?:\s*(?:,|and|to|–|-)\s*\d+[A-Z]{0,3})*)/g, m;
  while ((m = re.exec(txt))) {
    found[m[1]] = (found[m[1]] || 0) + 1;
    (m[2].match(/\d+[A-Z]{0,3}/g) || []).forEach(function (x) { found[x] = (found[x] || 0) + 1; });
  }
  return found;
}

/* split a law's text at its section headings; text with none is one piece */
function sections(txt) {
  var lines = txt.split(/\r?\n/), chunks = [], cur = { sec: "", body: [] };
  lines.forEach(function (ln) {
    var m = /^\s{0,8}(\d+[A-Z]{0,3})\.\s+\S/.exec(ln);
    if (m) { if (cur.body.length) chunks.push(cur); cur = { sec: m[1], body: [] }; }
    cur.body.push(ln);
  });
  if (cur.body.length) chunks.push(cur);
  return chunks.map(function (c) { return { sec: c.sec, body: c.body.join("\n") }; });
}

if (!fs.existsSync(out)) fs.mkdirSync(out);
SUBJECTS.forEach(function (s) {
  var base = path.join(root, s.dir), mods = [];
  s.l4.forEach(function (sub) {
    var d = path.join(base, sub);
    fs.readdirSync(d).filter(function (f) { return /\.l4$/.test(f); }).sort().forEach(function (f) {
      var content = fs.readFileSync(path.join(d, f), "utf8");
      mods.push({ file: path.posix.join(sub === "." ? "" : sub, f), sections: citedSections(content), content: content });
    });
  });
  var texts = s.texts.map(function (t) {
    var p = path.join(base, t.file);
    if (!t.licence) return { title: t.title, bundled: false, why: "Its licence is not recorded in the subject, so the text is not published with the console." };
    return { title: t.title, bundled: true, licence: t.licence, chunks: sections(fs.readFileSync(p, "utf8")) };
  });
  var data = { scheme: s.scheme, subject: s.dir, built: new Date().toISOString().slice(0, 10), texts: texts, l4: mods };
  var file = path.join(out, s.scheme + ".json");
  fs.writeFileSync(file, JSON.stringify(data));
  var tChars = texts.reduce(function (n, t) { return n + (t.chunks || []).reduce(function (m, c) { return m + c.body.length; }, 0); }, 0);
  console.log(s.scheme + ": " + mods.length + " L4 modules (" +
    mods.reduce(function (n, m) { return n + m.content.length; }, 0).toLocaleString("en-AU") + " chars), text " +
    texts.filter(function (t) { return t.bundled; }).length + " of " + texts.length + " bundled (" +
    tChars.toLocaleString("en-AU") + " chars) -> corpus/" + s.scheme + ".json");
});
