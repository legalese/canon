// Comply4 engine. Names no law: a rule pack supplies the facts, the duties and the wording.
//
// Three-valued throughout. A fact nobody has answered is unknown (null), not false, and the
// connectives are Kleene's: `all` is false as soon as one limb is false, true only when every
// limb is true, and otherwise unknown. So a duty reports "needs information" exactly when the
// facts given so far cannot settle it, and names the questions that would.

(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.Comply4 = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var T = true, F = false, U = null;

  function isSet(x) { return x !== undefined && x !== null && x !== ''; }

  // An expression is one of:
  //   true | false
  //   "factId"                    a yes/no fact
  //   {def: "name"}               a named condition from pack.defs
  //   {not: e} {all: [e…]} {any: [e…]} {implies: [a, b]}
  //   {is: [factId, value]}       an option fact equals value
  //   {in: [factId, [values]]}    an option fact is one of values
  //   {lt: [factId, n]} {gte: [factId, n]}
  //   {covers: [listFact, listFact]}   every member of the first list is in the second
  // The result is a node {v, …} that keeps its children, so the reasons can be read back.
  function evaluate(expr, ctx) {
    var facts = ctx.facts, pack = ctx.pack;

    if (expr === true || expr === false) return { op: 'const', v: expr };

    if (typeof expr === 'string') {
      var a = facts[expr];
      return { op: 'fact', fact: expr, v: a === true ? T : a === false ? F : U };
    }

    if (expr.def) {
      if (!pack.defs || !(expr.def in pack.defs)) throw new Error('no such definition: ' + expr.def);
      var inner = evaluate(pack.defs[expr.def], ctx);
      return { op: 'def', def: expr.def, v: inner.v, kids: [inner] };
    }

    if ('not' in expr) {
      var k = evaluate(expr.not, ctx);
      return { op: 'not', v: k.v === U ? U : !k.v, kids: [k] };
    }

    if (expr.all || expr.any) {
      var isAll = !!expr.all;
      var kids = (expr.all || expr.any).map(function (e) { return evaluate(e, ctx); });
      var decisive = isAll ? F : T;
      var v = kids.some(function (c) { return c.v === decisive; }) ? decisive
        : kids.some(function (c) { return c.v === U; }) ? U
          : !decisive;
      return { op: isAll ? 'all' : 'any', v: v, kids: kids };
    }

    if (expr.implies) return evaluate({ any: [{ not: expr.implies[0] }, expr.implies[1]] }, ctx);

    if (expr.is || expr['in']) {
      var id = (expr.is || expr['in'])[0];
      var wanted = expr.is ? [expr.is[1]] : expr['in'][1];
      var got = facts[id];
      return { op: 'is', fact: id, wanted: wanted, v: isSet(got) ? wanted.indexOf(got) >= 0 : U };
    }

    if (expr.lt || expr.gte) {
      var pair = expr.lt || expr.gte;
      var n = facts[pair[0]];
      var known = isSet(n) && !isNaN(Number(n));
      return {
        op: expr.lt ? 'lt' : 'gte', fact: pair[0], bound: pair[1],
        v: !known ? U : expr.lt ? Number(n) < pair[1] : Number(n) >= pair[1]
      };
    }

    if (expr.covers) {
      var need = facts[expr.covers[0]], have = facts[expr.covers[1]];
      if (!Array.isArray(need) || need.length === 0) {
        return { op: 'covers', fact: expr.covers[0], other: expr.covers[1], v: U, missing: [] };
      }
      if (!Array.isArray(have)) {
        return { op: 'covers', fact: expr.covers[1], other: expr.covers[0], v: U, missing: need.slice() };
      }
      var missing = need.filter(function (x) { return have.indexOf(x) < 0; });
      return { op: 'covers', fact: expr.covers[1], other: expr.covers[0], v: missing.length === 0, missing: missing };
    }

    throw new Error('unknown expression: ' + JSON.stringify(expr));
  }

  // The leaves that decide a node's value. For a false `all` those are its false limbs; for an
  // unknown one, the limbs still unknown (false is impossible there and true limbs do not
  // matter). `any` is the mirror image.
  function reasons(node, out) {
    out = out || [];
    if (!node.kids) { if (node.op !== 'const') out.push(node); return out; }
    if (node.op === 'all' || node.op === 'any') {
      var decisive = node.op === 'all' ? F : T;
      var pick = node.v === decisive ? decisive : node.v === U ? U : !decisive;
      node.kids.forEach(function (c) { if (c.v === pick) reasons(c, out); });
      return out;
    }
    node.kids.forEach(function (c) { reasons(c, out); });
    return out;
  }

  function uniqueFacts(nodes) {
    var seen = {}, list = [];
    nodes.forEach(function (n) {
      if (n.fact && !seen[n.fact]) { seen[n.fact] = true; list.push(n.fact); }
    });
    return list;
  }

  function daysBetween(fromIso, toIso) {
    var a = Date.parse(fromIso + 'T00:00:00Z'), b = Date.parse(toIso + 'T00:00:00Z');
    if (isNaN(a) || isNaN(b)) return null;
    return Math.round((b - a) / 86400000);
  }

  // One duty against the facts.
  //   na       the duty does not arise on these facts
  //   unknown  the facts given cannot settle it; `ask` lists what would
  //   met
  //   due      not yet done, and the time for doing it has not passed
  //   breach   not met
  //   advice   a "should" in the text that is not followed (never counted as a breach)
  function assessDuty(duty, ctx) {
    var pack = ctx.pack;
    var applies = evaluate({ all: [pack.scope || true, duty.appliesWhen === undefined ? true : duty.appliesWhen] }, ctx);
    var res = { duty: duty, applies: applies, status: null, why: [], ask: [] };

    if (applies.v === F) { res.status = 'na'; res.why = reasons(applies); return res; }
    if (applies.v === U) { res.status = 'unknown'; res.ask = uniqueFacts(reasons(applies)); return res; }

    var met = evaluate(duty.metWhen, ctx);
    res.met = met;
    res.why = reasons(met);

    if (met.v === T) { res.status = 'met'; return res; }
    if (met.v === U) { res.status = 'unknown'; res.ask = uniqueFacts(res.why); return res; }

    if (duty.pendingWhen !== undefined) {
      var pending = evaluate(duty.pendingWhen, ctx);
      if (pending.v === U) { res.status = 'unknown'; res.ask = uniqueFacts(reasons(pending)); return res; }
      if (pending.v === T) {
        res.status = 'due';
        var date = duty.deadlineFact && ctx.facts[duty.deadlineFact];
        if (isSet(date)) { res.deadline = date; res.daysLeft = daysBetween(ctx.today, date); }
        return res;
      }
    }
    res.status = duty.advisory ? 'advice' : 'breach';
    return res;
  }

  function isAsked(fact, ctx) {
    if (fact.askWhen === undefined) return true;
    return evaluate(fact.askWhen, ctx).v === T;
  }

  function isAnswered(fact, facts) {
    var a = facts[fact.id];
    if (fact.type === 'multi') return Array.isArray(a);
    return isSet(a);
  }

  function assess(pack, facts, today) {
    var ctx = { pack: pack, facts: facts || {}, today: today || new Date().toISOString().slice(0, 10) };
    var scope = evaluate(pack.scope || true, ctx);
    var results = pack.duties.map(function (d) { return assessDuty(d, ctx); });
    var counts = { met: 0, breach: 0, due: 0, unknown: 0, na: 0, advice: 0 };
    results.forEach(function (r) { counts[r.status]++; });

    var asked = pack.facts.filter(function (f) { return isAsked(f, ctx); });
    var open = asked.filter(function (f) { return !f.optional && !isAnswered(f, ctx.facts); });

    var verdict =
      scope.v === F ? 'outside'
        : counts.breach > 0 ? 'breach'
          : counts.unknown > 0 ? 'incomplete'
            : counts.due > 0 ? 'due'
              : 'clear';

    return {
      ctx: ctx, scope: scope, scopeWhy: reasons(scope), results: results, counts: counts,
      asked: asked, open: open, verdict: verdict
    };
  }

  // Structural check of a pack: every reference resolves, every fact is used, every duty can be
  // reached. Returns a list of problems; empty means the pack is well formed.
  function lint(pack) {
    var problems = [];
    var factIds = {}, used = {};
    pack.facts.forEach(function (f) {
      if (factIds[f.id]) problems.push('fact declared twice: ' + f.id);
      factIds[f.id] = f;
      if ((f.type === 'enum' || f.type === 'multi') && !(f.options && f.options.length)) {
        problems.push('fact ' + f.id + ' has no options');
      }
    });
    var groups = {};
    (pack.groups || []).forEach(function (g) { groups[g.id] = true; });
    pack.facts.forEach(function (f) { if (!groups[f.group]) problems.push('fact ' + f.id + ' is in no known group'); });

    function walk(e, where) {
      if (e === true || e === false || e === undefined) return;
      if (typeof e === 'string') { ref(e, where, 'bool'); return; }
      if (e.def) { if (!pack.defs || !(e.def in pack.defs)) problems.push(where + ': no definition ' + e.def); return; }
      if ('not' in e) return walk(e.not, where);
      if (e.all || e.any) return (e.all || e.any).forEach(function (x) { walk(x, where); });
      if (e.implies) return e.implies.forEach(function (x) { walk(x, where); });
      if (e.is || e['in']) {
        var id = (e.is || e['in'])[0], vals = e.is ? [e.is[1]] : e['in'][1];
        ref(id, where, 'enum');
        var f = factIds[id];
        if (f && f.options) vals.forEach(function (v) {
          if (!f.options.some(function (o) { return o.v === v; })) problems.push(where + ': ' + id + ' has no option ' + v);
        });
        return;
      }
      if (e.lt || e.gte) return ref((e.lt || e.gte)[0], where, 'number');
      if (e.covers) return e.covers.forEach(function (x) { ref(x, where, 'multi'); });
      problems.push(where + ': unknown expression ' + JSON.stringify(e));
    }
    function ref(id, where, type) {
      used[id] = true;
      if (!factIds[id]) problems.push(where + ': no fact ' + id);
      else if (factIds[id].type !== type) problems.push(where + ': ' + id + ' is ' + factIds[id].type + ', used as ' + type);
    }

    Object.keys(pack.defs || {}).forEach(function (k) { walk(pack.defs[k], 'def ' + k); });
    walk(pack.scope, 'scope');
    pack.facts.forEach(function (f) { walk(f.askWhen, 'fact ' + f.id + ' askWhen'); });

    var parts = {}, dutyIds = {};
    (pack.parts || []).forEach(function (p) { parts[p.id] = true; });
    pack.duties.forEach(function (d) {
      if (dutyIds[d.id]) problems.push('duty declared twice: ' + d.id);
      dutyIds[d.id] = true;
      if (!parts[d.part]) problems.push('duty ' + d.id + ' is in no known part');
      if (!d.ref) problems.push('duty ' + d.id + ' cites no provision');
      if (d.metWhen === undefined) problems.push('duty ' + d.id + ' has no metWhen');
      walk(d.appliesWhen, 'duty ' + d.id + ' appliesWhen');
      walk(d.metWhen, 'duty ' + d.id + ' metWhen');
      walk(d.pendingWhen, 'duty ' + d.id + ' pendingWhen');
      if (d.deadlineFact) { used[d.deadlineFact] = true; if (!factIds[d.deadlineFact]) problems.push('duty ' + d.id + ': no fact ' + d.deadlineFact); }
    });
    pack.facts.forEach(function (f) { if (!used[f.id]) problems.push('fact ' + f.id + ' is asked but no rule reads it'); });
    return problems;
  }

  return {
    evaluate: evaluate, reasons: reasons, assess: assess, assessDuty: assessDuty,
    isAsked: isAsked, isAnswered: isAnswered, lint: lint, daysBetween: daysBetween
  };
});
