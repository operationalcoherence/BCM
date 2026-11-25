// The pass test for the relationship graph (tools/graph/graph.js).
// Written from the hand-run docs in the Claude project BEFORE the module, so the
// module can't be tuned to it:
//   claude/pattern_synthesis_detectors_run_11-20_2026-11-24.md
//   claude/pattern_synthesis_architecture_attack_2026-11-24.md (amendments 1-7)
//   claude/pattern_synthesis_minimal_page_2026-11-24.md
// Note numbers follow file order (N1 = first note), as the hand-run docs do.
//
// "wording"  = the hand run found it in the words or order of the notes; the graph should too.
// "meaning"  = the hand run found it by reading meaning (no shared words, no cue);
//              the graph is EXPECTED to miss it. Finding it at stated/placed would be suspect.
// Usage: node tests/graph_pass.js
const path = require("path");
const fs = require("fs");
const G = require("../tools/graph/graph.js");
const WB = (f) => JSON.parse(fs.readFileSync(path.join(__dirname, "graph_wb", f), "utf8")).data;

const CASES = {
  "11-20 (g20.json)": {
    file: "g20.json",
    find: [
      { a: "N16", b: "N38", kind: "coupling", min: "placed", by: "wording", why: "K1: the two aggressions name each other" },
      { a: "N3", b: "N7", min: "stated", by: "wording", why: "R0: defiance holding stronger since the announcement" },
      { a: "N5", b: "N37", min: "stated", by: "wording", why: "C2: continued distrust of leadership" },
      { a: "N9", b: "N26", min: "stated", by: "wording", why: "C3: continued aggression toward the idea" },
      { a: "N31", b: "N16", min: "placed", by: "wording", why: "R1: sending supporters out feeds supporters' aggression" },
      { a: "Q.2", b: "N10", min: "inferred", max: "inferred", by: "wording", why: "the governing question's arrow: 'as it used to in a hierarchy' vs 'still in a hierarchy'" },
      { a: "N19", b: "N24", min: "placed", by: "meaning", why: "C5: fear about jobs becomes turnover" },
      { a: "N18", b: "N5", min: "placed", by: "meaning", why: "R2: constraint pen goes to leadership, whom N5 distrusts" },
    ],
    marks: [{ node: "N30", mark: "expects", why: "B1: 'likely to fail anyways'" }],
    rules: ["onlyOneMutualCoupling"],
  },
  "Good fire 11-13 (g13.json)": {
    file: "g13.json",
    find: [
      { a: "N28", b: "N28", min: "stated", by: "wording", why: "the fuel loop stated inside one note" },
      { a: "N30", b: "N30", min: "stated", by: "wording", why: "'reinforces itself' / 'positive feedback' inside one note" },
      { a: "N2", b: "N28", min: "inferred", by: "wording", why: "social half: politics answers public expectation (shared 'politic')" },
      { a: "Q.2", b: "N28", min: "inferred", by: "wording", why: "social half: public expectation of suppression (shared 'expect')" },
      { a: "N5", b: "N14", min: "placed", by: "meaning", why: "Recoil: simpler acquisition speeds tools as they are" },
    ],
    splits: [["N9", "N25"]],
    rules: [],
  },
  "Broadview 11-05 (g05.json)": {
    file: "g05.json",
    find: [
      { a: "nrcbyvg", b: "nve5zye", min: "placed", max: "placed", by: "wording", why: "user-drawn link" },
      { a: "nrcbyvg", b: "GOAL", min: "placed", max: "placed", by: "wording", why: "user-drawn link" },
    ],
    merged: [["ncgu0fz", "nk9xkyb", "nd7ohm0"]],
    rules: ["noPatternsLinks", "noOrderOnPlace", "proximityNeverAboveInferred"],
  },
};
const GLOBAL_RULES = ["inferredOnlyClosesOrBridges"];

const RANK = { inferred: 1, placed: 2, stated: 3 };
// Changed after the first run (disclosed in the report): an expectation capped at "inferred"
// is looked up among g.candidates too. Amendment 6 keeps lone inferred arrows off the graph,
// but the question step needs them, so the graph now hands them over separately.
function findArrow(g, a, b, kind, inCandidates) {
  const ia = g.byLabel[a], ib = g.byLabel[b];
  if (!ia || !ib) return null;
  let best = null;
  g.arrows.concat(inCandidates ? g.candidates : []).forEach((r) => {
    const fwd = r.from === ia && r.to === ib, rev = r.undirected && r.from === ib && r.to === ia;
    if ((fwd || rev) && (!kind || r.kind === kind) && (!best || RANK[r.grade] > RANK[best.grade])) best = r;
  });
  return best;
}
const ruleFns = {
  onlyOneMutualCoupling: (g) => {
    const n = g.arrows.filter((r) => r.evidence.some((e) => e.type === "names-each-other")).length;
    return [n === 1, n + " coupling(s) where the notes name each other (hand run: exactly 1, K1)"];
  },
  noPatternsLinks: (g) => {
    const n = g.arrows.filter((r) => r.evidence.some((e) => e.type === "user-link" && e.src === "patterns")).length;
    return [n === 0, n + " arrows built from links Patterns made (must be 0)"];
  },
  noOrderOnPlace: (g) => {
    const n = g.arrows.filter((r) => r.evidence.some((e) => e.order)).length;
    return [n === 0, n + " arrows using order on a place map (must be 0)"];
  },
  proximityNeverAboveInferred: (g) => {
    const n = g.arrows.filter((r) => r.grade !== "inferred" && r.evidence.every((e) => e.type === "proximity")).length;
    return [n === 0, n + " arrows above inferred on proximity alone (must be 0)"];
  },
  inferredOnlyClosesOrBridges: (g) => {
    const n = g.arrows.filter((r) => r.grade === "inferred" && !r.role).length;
    return [n === 0, n + " inferred arrows standing alone (must be 0; amendment 6)"];
  },
};

let fails = 0;
for (const [name, C] of Object.entries(CASES)) {
  const g = G.buildGraph(WB(C.file));
  console.log("\n=== " + name + ": " + g.nodes.length + " nodes, " + g.arrows.length + " arrows (" +
    ["stated", "placed", "inferred"].map((k) => g.arrows.filter((r) => r.grade === k).length + " " + k).join(", ") + ")");
  C.find.forEach((f) => {
    const r = findArrow(g, f.a, f.b, f.kind, f.max === "inferred");
    const got = r ? r.grade : "none";
    let ok;
    if (f.by === "meaning") ok = !r || RANK[r.grade] <= RANK.inferred || "unexpected";
    else ok = !!r && RANK[r.grade] >= RANK[f.min] && (!f.max || RANK[r.grade] <= RANK[f.max]);
    const tag = f.by === "meaning" ? (ok === true ? "EXPECTED MISS" : "SUSPECT") : ok ? "PASS" : "FAIL";
    if (tag === "FAIL" || tag === "SUSPECT") fails++;
    console.log("  " + tag.padEnd(13) + f.a + " -> " + f.b + "  got " + got + (r ? " " + r.kind : "") + "  (" + f.why + ")");
  });
  (C.marks || []).forEach((m) => {
    const n = g.nodes.find((x) => x.label === m.node);
    const ok = n && n.marks && n.marks[m.mark];
    if (!ok) fails++;
    console.log("  " + (ok ? "PASS" : "FAIL").padEnd(13) + m.node + " marked " + m.mark + "  (" + m.why + ")");
  });
  (C.splits || []).forEach((s) => {
    const ids = s.map((l) => g.allLabels[l]);
    const ok = g.splits.some((sp) => s.every((l) => sp.labels.includes(l)));
    const arrowsOnThem = g.arrows.filter((r) => ids.includes(r.from) && ids.includes(r.to)).length;
    if (!ok || arrowsOnThem) fails++;
    console.log("  " + (ok && !arrowsOnThem ? "PASS" : "FAIL").padEnd(13) + s.join(" = ") + " read as a split reading, no arrow between them");
  });
  (C.merged || []).forEach((s) => {
    const ok = g.nodes.filter((n) => s.includes(n.id) || (n.aliases || []).some((a) => s.includes(a))).length === 1;
    if (!ok) fails++;
    console.log("  " + (ok ? "PASS" : "FAIL").padEnd(13) + s.length + " identical notes merged into one");
  });
  C.rules.concat(GLOBAL_RULES).forEach((k) => {
    const [ok, msg] = ruleFns[k](g);
    if (!ok) fails++;
    console.log("  " + (ok ? "PASS" : "FAIL").padEnd(13) + msg);
  });
}
console.log("\n" + (fails ? fails + " FAILED" : "ALL PASS"));
process.exit(fails ? 1 : 0);
