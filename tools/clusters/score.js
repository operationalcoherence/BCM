// node tools/clusters/score.js <combined.json> <answer_key.json>: how well gsmClusters finds the planted groups
var fs = require("fs"), gsmClusters = require("./clusters.js");
var W = JSON.parse(fs.readFileSync(process.argv[2], "utf8")).data, K = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
var notes = W.m.map(function (n) { return { id: n[8], t: n[3], e: n[5], q: n[0], x: n[1], y: n[2], who: n[9], voice: n[7] }; });
var t0 = Date.now(), R = gsmClusters(notes, W.goal, W.links), ms = Date.now() - t0;
var truth = {}; K.forEach(function (k) { truth[k.note] = k; });
var HOW = ["", "same words", "similar words", "placed together"];
console.log("found " + R.clusters.length + " clusters, " + R.threads.length + " threads, in " + ms + " ms\n");
var hitBy = {};
R.clusters.concat(R.threads).forEach(function (c, ci) {
  var kind = ci < R.clusters.length ? "CLUSTER" : "thread";
  var tally = {};
  c.notes.forEach(function (n) { var g = truth[n.t].group; tally[g] = (tally[g] || 0) + 1; });
  var main = Object.keys(tally).sort(function (a, b) { return tally[b] - tally[a]; })[0];
  console.log(kind + " · " + c.emotion + " about \"" + c.about + "\" · " + c.people + " people, " + c.notes.length + " notes · mostly " + main);
  c.notes.forEach(function (n) {
    var k = truth[n.t], ok = k.group === main ? " " : (k.group === "loose" ? "✗" : "?");
    console.log("   " + ok + " [" + k.group + "/" + k.should_match_by + "] by " + HOW[n.how || 0] + " · " + n.t.slice(0, 70));
  });
  (hitBy[main] = hitBy[main] || []).push({ kind: kind, c: c });
});
console.log("\nPLANTED GROUPS");
var groups = {}; K.forEach(function (k) { if (k.group !== "loose") (groups[k.group] = groups[k.group] || []).push(k); });
Object.keys(groups).sort().forEach(function (g) {
  var want = groups[g], found = (hitBy[g] || []);
  var got = {}; found.forEach(function (f) { f.c.notes.forEach(function (n) { truth[n.t].group === g && (got[n.t] = 1); }); });
  var miss = want.filter(function (k) { return !got[k.note]; });
  console.log(g + ": " + (found.length ? found.map(function (f) { return f.kind; }).join("+") : "NOT FOUND") + " · " + Object.keys(got).length + "/" + want.length + " notes" +
    (miss.length ? " · missed: " + miss.map(function (k) { return k.should_match_by; }).join(", ") : ""));
});
