// Headless check of the engine and every rule pack. Run after changing either:
//
//   node tools/comply4/check.js
//
// It lints each pack's structure, runs the engine's logic through its edge cases, and asserts the
// status of named duties on stated facts. Exit code 1 on any failure.

'use strict';
var fs = require('fs');
var path = require('path');
var C = require('./engine.js');
var packs = [require('./laws/acd.js')];

var failures = 0, passes = 0;
function ok(cond, what) {
  if (cond) { passes++; return; }
  failures++;
  console.log('  FAIL  ' + what);
}
function eq(got, want, what) { ok(got === want, what + ' — expected ' + want + ', got ' + got); }

// ---- engine: three-valued logic
(function () {
  var pack = { defs: {}, facts: [], duties: [] };
  function v(e, facts) { return C.evaluate(e, { pack: pack, facts: facts || {} }).v; }
  eq(v({ all: ['a', 'b'] }, { a: true }), null, 'all: true and unknown is unknown');
  eq(v({ all: ['a', 'b'] }, { a: false }), false, 'all: false and unknown is false');
  eq(v({ any: ['a', 'b'] }, { a: true }), true, 'any: true or unknown is true');
  eq(v({ any: ['a', 'b'] }, { a: false }), null, 'any: false or unknown is unknown');
  eq(v({ not: 'a' }, {}), null, 'not unknown is unknown');
  eq(v({ implies: ['a', 'b'] }, { a: false }), true, 'implies: false antecedent is true');
  eq(v({ implies: ['a', 'b'] }, { b: true }), true, 'implies: true consequent is true whatever the antecedent');
  eq(v({ lt: ['n', 30] }, { n: 30 }), false, 'lt: 30 is not less than 30');
  eq(v({ lt: ['n', 30] }, { n: 29 }), true, 'lt: 29 is less than 30');
  eq(v({ lt: ['n', 30] }, { n: '' }), null, 'lt: blank is unknown');
  eq(v({ is: ['e', 'x'] }, {}), null, 'is: unanswered is unknown');
  eq(v({ covers: ['m', 'n'] }, { m: ['A', 'B'], n: ['A'] }), false, 'covers: one missing');
  eq(v({ covers: ['m', 'n'] }, { m: ['A', 'B'], n: ['B', 'A', 'C'] }), true, 'covers: all present');
  eq(v({ covers: ['m', 'n'] }, { m: [], n: [] }), null, 'covers: nothing to cover is unknown, not met');
  eq(v({ covers: ['m', 'n'] }, { m: ['A'] }), null, 'covers: second list unanswered is unknown');
  eq(C.daysBetween('2026-10-02', '2026-12-01'), 60, 'daysBetween counts calendar days');
})();

// ---- packs
function statusOf(res, id) {
  var r = res.results.filter(function (x) { return x.duty.id === id; })[0];
  if (!r) throw new Error('no duty ' + id);
  return r.status;
}
function withFacts(base, change) {
  var f = JSON.parse(JSON.stringify(base));
  Object.keys(change).forEach(function (k) { if (change[k] === undefined) delete f[k]; else f[k] = change[k]; });
  return f;
}

packs.forEach(function (pack) {
  console.log(pack.title);
  var problems = C.lint(pack);
  problems.forEach(function (p) { failures++; console.log('  LINT  ' + p); });
  if (!problems.length) passes++;

  // No sample may leave a question it is asked unanswered, unless the product is outside the law.
  pack.samples.forEach(function (s) {
    var res = C.assess(pack, s.facts, '2026-10-02');
    if (res.verdict !== 'outside') ok(res.open.length === 0, 'sample "' + s.name + '" leaves questions open: ' + res.open.map(function (f) { return f.id; }).join(', '));
    ok(res.counts.unknown === 0 || res.verdict === 'outside', 'sample "' + s.name + '" has duties needing information');
  });
});

// ---- ASEAN Cosmetic Directive: stated facts, expected status
(function () {
  var pack = packs[0], TODAY = '2026-10-02';
  var S = {};
  pack.samples.forEach(function (s) { S[s.id] = s.facts; });
  function run(facts) { return C.assess(pack, facts, TODAY); }

  var sun = run(S.sunscreen), cream = run(S.daycream), drink = run(S.drink);

  // The three samples, whole.
  eq(sun.verdict, 'breach', 'sunscreen: verdict');
  var sunBreaches = sun.results.filter(function (r) { return r.status === 'breach'; }).map(function (r) { return r.duty.id; }).sort().join(' ');
  eq(sunBreaches, 'aCriteria fSafety lDate lSmall notify uv', 'sunscreen: exactly these duties are not met');
  eq(statusOf(sun, 'lBotanicals'), 'advice', 'sunscreen: a "should" not followed is advice, not a breach');
  eq(statusOf(sun, 'lBatch'), 'met', 'sunscreen: batch number on a leaflet is allowed for a small container (C.2)');
  eq(statusOf(sun, 'lSmall'), 'breach', 'sunscreen: but it must also be on the tube itself (C.2(b))');
  eq(statusOf(sun, 'colour'), 'na', 'sunscreen: no colouring agents, so the colour rules do not arise');

  eq(cream.verdict, 'due', 'day cream: verdict');
  eq(statusOf(cream, 'notify'), 'due', 'day cream: notification outstanding but the product is not yet on the market');
  var due = cream.results.filter(function (r) { return r.duty.id === 'notify'; })[0];
  eq(due.daysLeft, 60, 'day cream: 60 days to the planned market date');
  eq(cream.counts.breach, 0, 'day cream: nothing breached');
  eq(statusOf(cream, 'lDate'), 'met', 'day cream: 36 months durability, a manufacturing date is enough');

  eq(drink.verdict, 'outside', 'drink: a swallowed product is outside Art 2(1)');
  ok(drink.results.every(function (r) { return r.status === 'na'; }), 'drink: no duty arises');

  // Every stated case in laws/acd-cases.js.
  require('./laws/acd-cases.js').forEach(function (c) {
    var res = run(withFacts(S[c.from], c.change));
    Object.keys(c.expect || {}).forEach(function (id) { eq(statusOf(res, id), c.expect[id], c.name + ' [' + id + ']'); });
    if (c.verdict) eq(res.verdict, c.verdict, c.name + ' [verdict]');
  });

  // Reasons: a duty needing information names the question that would settle it.
  var open = run(withFacts(S.daycream, { colourListed: false })).results.filter(function (r) { return r.duty.id === 'colour'; })[0];
  eq(open.ask.join(' '), 'unlistedCover', 'the colour duty asks for exactly the cover question');
})();

// ---- intake: Claude's reply is checked against the pack, and merged without trampling the user
(function () {
  var I = require('./intake.js'), pack = packs[0];
  var prompt = I.buildPrompt(pack, { name: 'label.jpg', how: 'a photo', images: 1 });
  ok(pack.facts.every(function (f) { return prompt.indexOf('- ' + f.id + ' (') >= 0; }), 'the prompt lists every question');
  ok(prompt.length < 60000, 'the prompt without content stays small (' + prompt.length + ' chars)');
  var long = I.buildPrompt(pack, { name: 'x.txt', how: 'a text file', text: new Array(100001).join('a') });
  ok(long.length < 60000 + I.MAX_TEXT && /first 60000 characters of 100000/.test(long), 'long content is cut and says so');

  var v = I.validate(pack, {
    kind: 'label', title: 'Front of tube', product: 'Sun lotion', productType: 'sunscreen', summary: 's', notes: ['n', 7, ''],
    answers: [
      { id: 'lblName', value: 'pack', evidence: 'name printed on the front', confidence: 'high' },
      { id: 'hasUV', value: true, evidence: 'lists a UV filter', confidence: 'certain' },
      { id: 'durability', value: 24, evidence: 'best before 24 months', confidence: 'medium' },
      { id: 'markets', value: ['SG', 'SG', 'MY'], evidence: 'ships to Singapore and Malaysia', confidence: 'medium' },
      { id: 'nonsense', value: true, evidence: 'x' },
      { id: 'lblBatch', value: 'on the tube', evidence: 'x' },
      { id: 'hasColour', value: 'yes', evidence: 'x' },
      { id: 'contentsUnits', value: 'metric' },
      { id: 'lblName', value: 'none', evidence: 'again' },
      { id: 'marketDate', value: '2026-13-40', evidence: 'x' }
    ]
  });
  eq(v.answers.map(function (a) { return a.id; }).join(' '), 'lblName hasUV durability markets', 'validate keeps only well-formed answers');
  eq(v.dropped.length, 6, 'validate reports what it dropped');
  eq(v.answers[1].confidence, 'low', 'an unknown confidence is treated as low');
  eq(v.answers[3].value.join(','), 'SG,MY', 'duplicate list members are removed');
  eq(v.notes.length, 1, 'notes that are not text are dropped');
  eq(v.kindLabel, 'Label or packaging', 'the kind is named from the pack');
  eq(I.validate(pack, 'not json').answers.length, 0, 'a reply that is not an object yields nothing');

  var facts = { lblName: 'none', hasUV: true }, src = {};
  var r = I.apply(facts, src, 'a', v.answers);
  eq(r.conflicts.map(function (a) { return a.id; }).join(' '), 'lblName', 'a hand-given answer that differs becomes a conflict');
  eq(facts.lblName, 'none', 'and is not overwritten');
  ok(!src.hasUV, 'a hand-given answer that agrees stays the user\'s own');
  eq(facts.durability, 24, 'an unanswered question takes the reading');
  eq(src.durability.item, 'a', 'and records where it came from');
  var r2 = I.apply(facts, src, 'b', [{ id: 'durability', value: 36, evidence: 'e', confidence: 'high' }]);
  eq(facts.durability + ' ' + src.durability.item + ' ' + r2.conflicts.length, '24 a 1', 'other content that disagrees with an earlier reading is a conflict, not an overwrite');
  I.apply(facts, src, 'a', [{ id: 'durability', value: 30, evidence: 'e', confidence: 'high' }]);
  eq(facts.durability, 30, 're-reading the same item replaces what it said before');
  I.accept(facts, src, 'b', r2.conflicts[0]);
  eq(facts.durability + ' ' + src.durability.item, '36 b', 'accepting the conflict moves the answer to the other item');
  I.accept(facts, src, 'a', r.conflicts[0]);
  eq(facts.lblName + ' ' + src.lblName.item, 'pack a', 'accepting a conflict takes the content\'s reading');
  eq(I.removeItem(facts, src, 'a').sort().join(' '), 'lblName markets', 'removing content removes only the answers resting on it');
  ok(facts.hasUV === true && facts.durability === 36 && !('lblName' in facts), 'everything else stays');

  // End to end: a reading that makes the product not a cosmetic puts it outside the law.
  var soup = I.validate(pack, { kind: 'formula', answers: [
    { id: 'site', value: 'other', evidence: 'a soup, eaten', confidence: 'high' },
    { id: 'mainPurpose', value: false, evidence: 'a food', confidence: 'high' }] });
  var f2 = {}, s2 = {};
  I.apply(f2, s2, 'x', soup.answers);
  eq(C.assess(pack, f2, '2026-10-02').verdict, 'outside', 'a recipe for soup is outside the Directive');
})();

// ---- the L4: regenerate the cases and run them, if an `l4` is installed
(function () {
  var cp = require('child_process');
  cp.execFileSync(process.execPath, [path.join(__dirname, 'build.js')], { stdio: 'inherit' });
  packs.forEach(function (pack) {
    var r = cp.spawnSync('l4', ['run', pack.id + '-cases.l4'], { cwd: path.join(__dirname, 'laws'), encoding: 'utf8', maxBuffer: 1 << 28 });
    if (r.error) { console.log('  l4 is not on the PATH: the L4 assertions were NOT run'); return; }
    // `l4 run` exits 0 whatever the assertions do and prints each diagnostic twice, so count
    // distinct source ranges by outcome.
    var seen = { satisfied: {}, failed: {} }, m;
    var re = /Range:\s+(\S+)[\s\S]*?Message:\s+assertion (satisfied|failed)/g;
    var text = (r.stdout || '') + (r.stderr || '');
    while ((m = re.exec(text))) seen[m[2]][m[1]] = true;
    var good = Object.keys(seen.satisfied).length, bad = Object.keys(seen.failed).length;
    var want = (fs.readFileSync(path.join(__dirname, 'laws', pack.id + '-cases.l4'), 'utf8').match(/^#ASSERT /gm) || []).length;
    console.log('  l4: ' + good + ' of ' + want + ' assertions satisfied, ' + bad + ' failed');
    ok(bad === 0, bad + ' L4 assertions failed at ' + Object.keys(seen.failed).slice(0, 5).join(', '));
    ok(good === want, 'l4 reported ' + good + ' satisfied assertions, the cases file has ' + want);
  });
})();

console.log('');
console.log(passes + ' passed, ' + failures + ' failed');
process.exit(failures ? 1 : 0);
