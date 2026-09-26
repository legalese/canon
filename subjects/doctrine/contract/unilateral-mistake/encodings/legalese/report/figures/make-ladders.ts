/** SCRATCH — ladder SVGs for the unilateral-mistake canon row. Delete after running. */
import { layout, estimateMetrics, defaultViewSpec } from "../src/index.js";
import type { FunDecl, IRExpr, NodeId, UBoolValue } from "../src/index.js";
import { sceneToSvg } from "../../ladder-svg/src/index.js";
import { writeFileSync, mkdirSync } from "node:fs";

type V = UBoolValue;
const T: V = "TrueV", F: V = "FalseV";

/** Each builder returns the tree plus the valuation it implies, so leaf values and
 *  node ids can never drift apart. */
function build(spec: (b: B) => IRExpr, name: string): [FunDecl, Map<NodeId, V>] {
  let n = 0;
  const val = new Map<NodeId, V>();
  const b: B = {
    leaf: (label, v) => { const id = n++; if (v) val.set(id, v);
      return { $type: "UBoolVar", id, label, atomId: label } as IRExpr; },
    inert: (text, context) => ({ $type: "InertE", id: n++, text, context }) as IRExpr,
    and: (...args) => ({ $type: "And", id: n++, args }) as IRExpr,
    or: (...args) => ({ $type: "Or", id: n++, args }) as IRExpr,
    not: (negand) => ({ $type: "Not", id: n++, negand }) as IRExpr,
  };
  const body = spec(b);
  return [{ id: n++, name, params: [], body }, val];
}
interface B {
  leaf(label: string, v?: V): IRExpr;
  inert(text: string, context: "InertAnd" | "InertOr"): IRExpr;
  and(...args: IRExpr[]): IRExpr;
  or(...args: IRExpr[]): IRExpr;
  not(negand: IRExpr): IRExpr;
}

/* ---- the circuits, transcribed from the L4 modules ---- */

const sgEquity = (k: Record<string, V>) => build((b) => b.and(
  b.not(b.leaf("void at common law", k.voidCL)),
  b.leaf("a mistake as to a term", k.term),
  b.leaf("the mistake was fundamental", k.fundamental),
  b.leaf("constructive knowledge", k.suspected),
  b.or(
    b.inert("an additional element of impropriety", "InertOr"),
    b.leaf("a conscious omission to disabuse", k.omission),
    b.leaf("deliberate steps to prevent discovery", k.deliberate),
  ),
), "Singapore — the equity door");

const usS153 = (k: Record<string, V>) => build((b) => b.and(
  b.leaf("material adverse effect", k.material),
  b.not(b.leaf("the mistaken party bears the risk", k.risk)),
  b.or(
    b.inert("either limb suffices", "InertOr"),
    b.leaf("enforcement would be unconscionable", k.unconscionable),
    b.leaf("the other party had reason to know", k.reason),
    b.leaf("the other party's fault caused it", k.fault),
  ),
), "Restatement (Second) § 153");

const auTaylor = (k: Record<string, V>) => build((b) => b.and(
  b.leaf("a mistake as to a term", k.term),
  b.leaf("the mistake was fundamental", k.fundamental),
  b.leaf("knew or had reason to know", k.suspected),
  b.leaf("deliberately set out to prevent discovery", k.deliberate),
), "Australia — Taylor v Johnson");

const panels: Array<[string, [FunDecl, Map<NodeId, V>]]> = [
  ["donovan-sg", sgEquity({ voidCL: F, term: T, fundamental: T, suspected: F, omission: F, deliberate: F })],
  ["donovan-us", usS153({ material: T, risk: F, unconscionable: T, reason: F, fault: F })],
  ["dm2-sg",     sgEquity({ voidCL: F, term: T, fundamental: T, suspected: T, omission: T, deliberate: F })],
  ["dm2-au",     auTaylor({ term: T, fundamental: T, suspected: T, deliberate: F })],
];

mkdirSync("/tmp/ladder-out", { recursive: true });
for (const [name, [fn, valuation]] of panels) {
  for (const theme of ["screen", "ink"] as const) {
    const vs = defaultViewSpec({ showCurrent: true, theme, valuation, scale: "full", orient: "LR" });
    const scene = layout(fn, vs, estimateMetrics);
    writeFileSync(`/tmp/ladder-out/${name}.${theme}.svg`, sceneToSvg(scene, theme));
    if (theme === "screen")
      console.log(name.padEnd(12), scene.size.w.toFixed(0) + "x" + scene.size.h.toFixed(0),
                  "complete=" + scene.complete, "prims=" + scene.prims.length);
  }
}
