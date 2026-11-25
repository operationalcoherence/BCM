// The pass test for shape detection (tools/graph/shapes.js).
// Written BEFORE the module, from the hand runs and the frozen design in the Claude project:
//   claude/pattern_synthesis_loop_audit_2026-11-24.md      (three shapes; weakest arrow; shared nodes once)
//   claude/pattern_synthesis_architecture_attack_2026-11-24.md (amendments 6, 8, 9; the constructed cases)
//   claude/pattern_synthesis_minimal_page_2026-11-24.md    (11-20 block 2: the escalation)
//   claude/BCM_EPISTEMOLOGY.md                              (nothing from proximity; closures are hypotheses)
//
// "wording"  the hand run found it in the words or order of the notes: shapes should find it.
// "meaning"  the hand run found it by reading meaning, or it hangs on an arrow the graph can't
//            support: shapes are EXPECTED to miss it. Finding it would be suspect.
// "observe"  printed, not judged.
// Usage: node tests/shapes_pass.js
const path = require("path");
const fs = require("fs");
const G = require("../tools/graph/graph.js");
const S = require("../tools/graph/shapes.js");
const WB = (f) => JSON.parse(fs.readFileSync(path.join(__dirname, "graph_wb", f), "utf8")).data;

/* ---------- constructed workbooks (thought tests from the attack doc, made concrete) ---------- */
const note = (q, x, y, text, emo, id) => [q, x, y, text, null, emo, 0, "Mine", id];
// Technical constraint: "permit review trims acreage -> smaller units -> the same crew -> a later schedule".
// Technical writers state causes, so every step carries a cue.
const TECH = {
  goal: "Treat 400 acres of fuel breaks by June.",
  a: [],
  m: [
    note(2, 30, 180, "Permit review trims treatment acreage.", 2, "t1"),
    note(2, 110, 185, "Smaller treatment units due to permit review trimming acreage.", 3, "t2"),
    note(2, 190, 190, "The same crew works longer because of smaller treatment units.", 3, "t3"),
    note(2, 270, 185, "A later burn schedule driven by the same crew working longer.", 2, "t4"),
    note(7, 60, 40, "Contract crews from the neighboring district.", 1, "t5"),
  ],
  p: { m: [] }, voices: ["Mine"], links: [],
};
// Settlement: three different reasons, none naming another, each answered by one state.
const SETTLE = {
  goal: "Ten homeowners on the road complete home hardening this year.",
  a: [],
  m: [
    note(2, 40, 170, "Spending fire season away leads to no worry.", 3, "s1"),
    note(2, 55, 190, "Valuing the natural look leads to no cutting.", 0, "s2"),
    note(2, 70, 200, "Tight household budgets lead to no cost.", 0, "s3"),
    note(2, 250, 185, "The home stays as it is: no cutting, no cost, no worry.", 3, "s4"),
    note(3, 120, 40, "Neighbors on the next road chipped slash together.", 1, "s5"),
  ],
  p: { m: [] }, voices: ["Mine"], links: [],
};
// No resistance: "success breeds complacency" can be supposed about any goal; nothing may stand on it.
const NORES = {
  goal: "Every crew adopts the new briefing card this season.",
  a: [],
  m: [
    note(3, 40, 60, "Crew leads asked for the briefing card.", 1, "r1"),
    note(3, 150, 50, "Briefings run faster since the card arrived.", 1, "r2"),
    note(3, 260, 40, "Crews say the card is simply how briefings work now.", 1, "r3"),
  ],
  p: { m: [] }, voices: ["Mine"], links: [],
};
// Uncertainty: unknowns only.
const UNCERTAIN = {
  goal: "Decide on the treatment plan.",
  a: [],
  m: [
    note(2, 60, 170, "Unknown soil moisture.", 3, "u1"),
    note(2, 160, 180, "Unknown budget.", 3, "u2"),
    note(2, 240, 190, "Unknown staffing.", 3, "u3"),
  ],
  p: { m: [] }, voices: ["Mine"], links: [],
};
const EMPTY = { goal: "", a: [], m: [], p: { m: [] }, voices: ["Mine"], links: [] };
const GOALONLY = { goal: "Reduce structure loss.", a: [], m: [], p: { m: [] }, voices: ["Mine"], links: [] };

const RANK = { inferred: 1, placed: 2, stated: 3 };
let fails = 0;
const say = (tag, msg) => {
  if (tag === "FAIL" || tag === "SUSPECT") fails++;
  console.log("  " + tag.padEnd(13) + msg);
};
const ids = (g, labels) => labels.map((l) => g.byLabel[l] || l);
const has = (shape, list) => list.every((id) => shape.parts.includes(id));
const show = (g, s) =>
  s ? s.type + " [" + s.parts.map((id) => (g.nodes.find((n) => n.id === id) || { label: id }).label).join(", ") + "] " + s.grade + (s.given ? " given" : "") : "none";

function run(name, d, checks) {
  const g = G.buildGraph(d);
  const t0 = Date.now();
  const R = S.detectShapes(g);
  const ms = Date.now() - t0;
  const by = (t) => R.shapes.filter((s) => s.type === t).length;
  console.log("\n=== " + name + ": " + R.shapes.length + " shapes (" + by("loop") + " loops, " + by("settlement") + " settlements, " + by("chain") + " chains), " + ms + " ms" + (R.truncated ? ", TRUNCATED" : ""));
  console.log("  observe      strongest: " + show(g, R.strongest));
  checks(g, R);
  globalRules(g, R);
  return { g, R, ms };
}

function globalRules(g, R) {
  const inGraph = new Set(g.arrows.map((a) => a.from + "|" + a.to + "|" + a.kind));
  let bad = 0, badGrade = 0, allInf = 0, prox = 0, pat = 0, undirLoop = 0;
  R.shapes.forEach((s) => {
    s.arrows.forEach((a) => { if (!inGraph.has(a.from + "|" + a.to + "|" + a.kind)) bad++; });
    const min = Math.min.apply(null, s.arrows.map((a) => RANK[a.grade]));
    if (RANK[s.grade] !== min) badGrade++;
    if (s.arrows.every((a) => a.grade === "inferred")) allInf++;
    if (s.arrows.length && s.arrows.every((a) => (a.evidence || []).every((e) => e.type === "proximity"))) prox++;
    if (s.arrows.some((a) => (a.evidence || []).some((e) => e.src === "patterns"))) pat++;
    if (s.type === "loop" && s.arrows.length > 1 && s.arrows.every((a) => a.undirected) &&
        !(s.arrows.length === 1 || s.arrows.some((a) => (a.evidence || []).some((e) => e.type === "names-each-other")))) undirLoop++;
  });
  say(bad ? "FAIL" : "PASS", bad + " shape arrows not in the graph (candidates are never used)");
  say(badGrade ? "FAIL" : "PASS", badGrade + " shapes whose grade isn't their weakest arrow");
  say(allInf ? "FAIL" : "PASS", allInf + " shapes standing on inference alone");
  say(prox ? "FAIL" : "PASS", prox + " shapes on proximity alone");
  say(pat ? "FAIL" : "PASS", pat + " shapes using links Patterns made");
  say(undirLoop ? "FAIL" : "PASS", undirLoop + " loops with no direction anywhere (a cluster, not a loop)");
  // amendment 9: a given loop with nothing joining it never leads
  const top = R.strongest;
  const bad9 = top && top.given && !(top.joins || []).length && R.shapes.some((s) => !s.given);
  say(bad9 ? "FAIL" : "PASS", "a given shape with nothing joining it doesn't lead (amendment 9)");
  // deterministic
  const again = S.detectShapes(g).shapes.map((s) => s.key).join(";");
  say(again === R.shapes.map((s) => s.key).join(";") ? "PASS" : "FAIL", "same order on a second run");
}

/* ---------- the three real workbooks ---------- */
run("11-20 (g20.json)", WB("g20.json"), (g, R) => {
  const [n16, n38] = ids(g, ["N16", "N38"]);
  const esc = R.shapes.find((s) => s.type === "loop" && s.parts.length === 2 && has(s, [n16, n38]));
  say(esc && esc.grade === "placed" ? "PASS" : "FAIL", "K1 escalation N16 <-> N38 is a two-part loop, placed  (got " + show(g, esc) + ")");
  const [q2, n10, n11] = ids(g, ["Q.2", "N10", "N11"]);
  const set = R.shapes.find((s) => s.type === "settlement" && s.parts.includes(q2) && (s.parts.includes(n10) || s.parts.includes(n11)));
  say(set ? "SUSPECT" : "EXPECTED MISS", "L1 settlement on the reassurance (hangs on inferred Q.2 -> N10)  (got " + show(g, set) + ")");
  const [n19, n24] = ids(g, ["N19", "N24"]);
  const pl = R.shapes.find((s) => has(s, [n19, n24]));
  say(pl ? "SUSPECT" : "EXPECTED MISS", "L4 place loop N19 -> N24 (meaning only)  (got " + show(g, pl) + ")");
  const [n3, n7] = ids(g, ["N3", "N7"]);
  const r0 = R.shapes.find((s) => has(s, [n3, n7]));
  say("observe", "R0 (N3, N7) in a shape: " + show(g, r0));
});

run("Good fire 11-13 (g13.json)", WB("g13.json"), (g, R) => {
  const [n28, n30, n2, q2] = ids(g, ["N28", "N30", "N2", "Q.2"]);
  const fuel = R.shapes.find((s) => s.type === "loop" && s.parts.length === 1 && s.parts[0] === n28);
  say(fuel && fuel.grade === "stated" && fuel.given ? "PASS" : "FAIL", "the fuel loop inside N28: a stated loop, given  (got " + show(g, fuel) + ")");
  const fb = R.shapes.find((s) => s.type === "loop" && s.parts.length === 1 && s.parts[0] === n30);
  say(fb && fb.grade === "stated" && fb.given ? "PASS" : "FAIL", "'positive feedback' inside N30: a stated loop, given  (got " + show(g, fb) + ")");
  const social = fuel && (fuel.joins || []).some((a) => a.from === n2 || a.to === n2 || a.from === q2 || a.to === q2);
  say(social ? "SUSPECT" : "EXPECTED MISS", "the fuel loop joined by its social half (N2, Q.2): the graph doesn't find those arrows");
  const [n9, n25] = ids(g, ["N9", "N25"]);
  say(n9 === n25 ? "PASS" : "FAIL", "N9 = N25 is one part (split reading), so no shape counts it twice");
});

run("Broadview 11-05 (g05.json)", WB("g05.json"), (g, R) => {
  const road = ["nrcbyvg", "n8ucdan", "nr45ycm", "n6618p1"];
  const set = R.shapes.find((s) => s.type === "settlement" && road.filter((id) => s.parts.includes(id)).length >= 3);
  say(set ? "SUSPECT" : "EXPECTED MISS", "the settlement on the resistant road (read from nearness and meaning)  (got " + show(g, set) + ")");
});

/* ---------- constructed ---------- */
run("Technical constraint (constructed)", TECH, (g, R) => {
  const ch = R.shapes.find((s) => s.type === "chain" && has(s, ["t1", "t2", "t3", "t4"]));
  say(ch && ch.grade === "stated" ? "PASS" : "FAIL", "permit -> units -> crew -> schedule is one stated chain  (got " + show(g, ch) + ")");
  say(R.strongest && R.strongest === ch ? "PASS" : "FAIL", "and it is the strongest shape");
  const order = ch ? ch.parts.join(",") === "t1,t2,t3,t4" : false;
  say(order ? "PASS" : "FAIL", "in the order the text gives");
});
run("Settlement (constructed)", SETTLE, (g, R) => {
  const st = R.shapes.find((s) => s.type === "settlement" && s.target === "s4");
  say(st && ["s1", "s2", "s3"].every((id) => st.sources.includes(id)) ? "PASS" : "FAIL", "three reasons end in one state (s4)  (got " + show(g, st) + ")");
  say(R.strongest && R.strongest.type === "settlement" ? "PASS" : "FAIL", "the settlement is the strongest shape");
  const loop = R.shapes.find((s) => s.type === "loop" && s.parts.includes("s4"));
  say(!loop ? "PASS" : "FAIL", "it isn't read as a loop (nothing feeds back)");
});
run("No resistance (constructed)", NORES, (g, R) => {
  say(!R.shapes.some((s) => s.arrows.some((a) => a.grade === "inferred" && !a.role)) ? "PASS" : "FAIL", "no shape carries an inferred arrow that only stands alone");
});
run("Uncertainty (constructed)", UNCERTAIN, (g, R) => {
  say(R.shapes.length === 0 ? "PASS" : "FAIL", "no shapes: unknowns aren't relationships");
});
run("Empty", EMPTY, (g, R) => say(R.shapes.length === 0 && R.strongest === null ? "PASS" : "FAIL", "no shapes, strongest is null"));
run("Goal only", GOALONLY, (g, R) => say(R.shapes.length === 0 ? "PASS" : "FAIL", "no shapes"));

/* ---------- scale ---------- */
const big = JSON.parse(fs.readFileSync(path.join(__dirname, "wb_big.json"), "utf8"));
const B = run("200-note synthetic (wb_big.json)", big.data || big, () => {});
say(B.ms < 3000 ? "PASS" : "FAIL", "shape detection under 3 s on 200 notes (" + B.ms + " ms)");

/* ---------- the question step will need these ---------- */
(function () {
  const g = G.buildGraph(WB("g20.json"));
  const c = g.candidates.find((r) => r.from === g.byLabel["Q.2"] && r.to === g.byLabel["N10"]);
  const yes = S.detectShapes(S.withArrow(g, c, "stated"));
  const no = S.detectShapes(S.withoutArrow(g, c));
  console.log("\n=== Yes/No pages for Q.2 -> N10 (what the question step will call)");
  console.log("  observe      yes: " + yes.shapes.length + " shapes, strongest " + show(g, yes.strongest));
  console.log("  observe      no:  " + no.shapes.length + " shapes, strongest " + show(g, no.strongest));
  say(c && yes && no ? "PASS" : "FAIL", "withArrow / withoutArrow run");
})();

console.log("\n" + (fails ? fails + " FAILED" : "ALL PASS"));
process.exit(fails ? 1 : 0);
