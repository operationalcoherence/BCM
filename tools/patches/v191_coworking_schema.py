"""v191 (A2): a coworking-ready workbook, additive and backward compatible.
- wid: an id for each workbook, made once.  sv: 2 (schema version).
- mt: {noteId: ISO} last edit of each note, kept by the edit log.  gone: {noteId: ISO} deletions.
- Combine: the same note edited by both people takes the newer version; a note the other person deleted from
  their own notes is removed; a note you deleted stays deleted unless they edited it after you deleted it.
- others[]: each perspective carries at (date combined) and wid (their workbook id)."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

# edit times and deletions, from the edit log
rep("""    Array.isArray(C.log) || (C.log = []);
    var s = C.log[C.log.length - 1];""", """    Array.isArray(C.log) || (C.log = []);
    if (e && /^note/.test(t)) {
      (C.mt && "object" == typeof C.mt) || (C.mt = {});
      (C.gone && "object" == typeof C.gone) || (C.gone = {});
      "note-" === t ? ((C.gone[e] = a), delete C.mt[e]) : ((C.mt[e] = a), delete C.gone[e]);
    }
    var s = C.log[C.log.length - 1];""")
# normalize on load
rep("""    Array.isArray(C.others) || (C.others = []),
    Array.isArray(C.log) || (C.log = []),""", """    Array.isArray(C.others) || (C.others = []),
    Array.isArray(C.log) || (C.log = []),
    ("string" == typeof C.wid && C.wid) || (C.wid = "w" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8)),
    (C.mt && "object" == typeof C.mt && !Array.isArray(C.mt)) || (C.mt = {}),
    (C.gone && "object" == typeof C.gone && !Array.isArray(C.gone)) || (C.gone = {}),
    (C.sv = 2),""")
# combine: newer edits win; deletions
rep("""                            var r = {},
                              i = [C.m.length, C.p.m.length, (C.links || []).length];""", """                            var r = {},
                              i = [C.m.length, C.p.m.length, (C.links || []).length],
                              TMT = t.mt && "object" == typeof t.mt ? t.mt : {},
                              TGO = t.gone && "object" == typeof t.gone ? t.gone : {},
                              UPD = 0,
                              DEL = 0,
                              ADD = [0, 0];
                            (C.mt && "object" == typeof C.mt) || (C.mt = {});
                            (C.gone && "object" == typeof C.gone) || (C.gone = {});""")
rep("""                                (a[8] || (a[8] = o + i + "-" + Math.random().toString(36).slice(2, 7)),
                                  r[a[8]] ||
                                    ((r[a[8]] = 1), a[9] || (a[9] = e), a[7] || (a[7] = a[9]), n.push(a)));""", """                                a[8] || (a[8] = o + i + "-" + Math.random().toString(36).slice(2, 7));
                                var id = a[8],
                                  tt = TMT[id];
                                if (r[id]) {
                                  if (tt && (!C.mt[id] || tt > C.mt[id]))
                                    for (var k = 0; k < n.length; k++)
                                      if (n[k] && n[k][8] === id) {
                                        (a[9] || (a[9] = n[k][9] || e), (n[k] = a), (C.mt[id] = tt), UPD++);
                                        break;
                                      }
                                  return;
                                }
                                if (C.gone[id] && (!tt || C.gone[id] >= tt)) return;
                                ((r[id] = 1), a[9] || (a[9] = e), a[7] || (a[7] = a[9]), n.push(a), ADD[n === C.m ? 0 : 1]++, tt && (C.mt[id] = tt), delete C.gone[id]);""")
rep("""                              s(t.m, C.m, e + "-L"),
                              s(t.p && t.p.m, C.p.m, e + "-P"),""", """                              s(t.m, C.m, e + "-L"),
                              s(t.p && t.p.m, C.p.m, e + "-P"),
                              [C.m, C.p.m].forEach(function (L) {
                                for (var k = L.length - 1; k >= 0; k--) {
                                  var id = L[k] && L[k][8];
                                  id &&
                                    TGO[id] &&
                                    L[k][9] === e &&
                                    (!C.mt[id] || TGO[id] > C.mt[id]) &&
                                    (L.splice(k, 1), (C.gone[id] = TGO[id]), delete C.mt[id], DEL++);
                                }
                              }),""")
rep("""                                ? C.others.forEach(function (n) {
                                    n.name === e &&
                                      ((n.goal = t.goal || ""), (n.a = (t.a || []).slice(0, 7)));
                                  })
                                : C.others.push({ name: e, goal: t.goal || "", a: (t.a || []).slice(0, 7) }),""", """                                ? C.others.forEach(function (n) {
                                    n.name === e &&
                                      ((n.goal = t.goal || ""), (n.a = (t.a || []).slice(0, 7)), (n.at = me()), (n.wid = t.wid || n.wid || null));
                                  })
                                : C.others.push({ name: e, goal: t.goal || "", a: (t.a || []).slice(0, 7), at: me(), wid: t.wid || null }),""")
rep("""                                links: (C.links || []).length - i[2],
                                upd: o,
                              }),""", """                                links: (C.links || []).length - i[2],
                                upd: o,
                                edits: UPD,

                                gone: DEL,
                              }),""")
rep("""                      (e.upd ? " Their earlier answers were replaced by the newer ones." : "") +""", """                      (e.upd ? " Their earlier answers were replaced by the newer ones." : "") +
                      (e.edits
                        ? " " + e.edits + (1 === e.edits ? " note they edited more recently now shows" : " notes they edited more recently now show") + " their version."
                        : "") +
                      (e.gone ? " " + e.gone + (1 === e.gone ? " note they deleted was" : " notes they deleted were") + " removed." : "") +""")
rep("""                                notes: C.m.length - i[0],
                                places: C.p.m.length - i[1],""", """                                notes: ADD[0],
                                places: ADD[1],""")
rep('t.textContent = "v190"', 't.textContent = "v191"')
open(P, "w").write(s)
