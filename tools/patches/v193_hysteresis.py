"""v193 (F6): hysteresis. The workbook now keeps each note's emotion history (eh: {noteId: [[ISO|null, emotion], ...]}),
seeded from the edit log for existing notes. Opposition (distrust, aggression, defiance) that has held a long time, or came
back after changing, weighs more in the friction of the ways that cross it: weight = 1 + 0.5 x min(1, days held / 180)
+ 0.25 x min(2, times it came back). Each way's reading names the entrenched notes it meets."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("""  function gsmPlaceView() {""", """  function gsmEHrec() {
    (C.eh && "object" == typeof C.eh && !Array.isArray(C.eh)) || (C.eh = {});
    var now = new Date().toISOString(),
      LT = null;
    C.m.concat((C.p && C.p.m) || []).forEach(function (r) {
      if (!Array.isArray(r) || !r[8]) return;
      var id = String(r[8]),
        e = null != r[5] ? r[5] : null,
        H = C.eh[id];
      if (!Array.isArray(H) || !H.length) {
        LT ||
          ((LT = {}),
          (C.log || []).forEach(function (l) {
            l && l.i && ("note+" === l.k || "noteemo" === l.k) && (LT[l.i] = l.t);
          }));
        C.eh[id] = [[LT[id] || null, e]];
        return;
      }
      H[H.length - 1][1] !== e && H.push([now, e]);
    });
  }
  window.gsmHy = function (id) {
    var H = C.eh && C.eh[id];
    if (!Array.isArray(H) || !H.length) return null;
    var hard = function (e) {
        return 0 === e || 2 === e || 4 === e;
      },
      cur = H[H.length - 1][1];
    if (!hard(cur)) return { hy: 1 };
    var i = H.length - 1;
    for (; i > 0 && H[i - 1][1] === cur; ) i--;
    var since = H[i][0],
      days = since ? Math.max(0, (Date.now() - Date.parse(since)) / 864e5) : 0,
      back = 0,
      seen = !1,
      soft = !1;
    H.forEach(function (h) {
      hard(h[1]) ? (seen && soft && back++, (seen = !0), (soft = !1)) : seen && (soft = !0);
    });
    return { hy: 1 + 0.5 * Math.min(1, days / 180) + 0.25 * Math.min(2, back), since: since, back: back, days: days, e: cur };
  };
  function gsmPlaceView() {""")
rep("""  function P() {
    (B(), clearTimeout(j),""", """  function P() {
    (B(), gsmEHrec(), clearTimeout(j),""")
rep("""    (C.sv = 2),""", """    (C.sv = 2),
    gsmEHrec(),""")
# module: carry id and hysteresis
rep("""          v: n[7] ? String(n[7]) : "",
          hd: null != n.hd ? !!n.hd : y > 118,
        });""", """          v: n[7] ? String(n[7]) : "",
          hd: null != n.hd ? !!n.hd : y > 118,
          id: n[8] ? String(n[8]) : "",
          hyi: n[8] && window.gsmHy ? window.gsmHy(String(n[8])) : null,
        });""")
rep("""            d2 < 10816 && (ws[n.e] += Math.exp(-d2 / 1352));""", """            d2 < 10816 && (ws[n.e] += Math.exp(-d2 / 1352) * (n.hyi && n.hyi.hy ? n.hyi.hy : 1));""")
rep("""                    " without passing indifference first, so pushing there can turn people further against the goal."
                  : "");""", """                    " without passing indifference first, so pushing there can turn people further against the goal."
                  : "") +
                (function () {
                  var ent = (S.hard || [])
                    .map(function (k) {
                      return NSK[k];
                    })
                    .filter(function (n) {
                      return n && n.hyi && n.hyi.hy > 1.05;
                    })
                    .sort(function (a, b) {
                      return b.hyi.hy - a.hyi.hy;
                    })
                    .slice(0, 3);
                  return ent.length
                    ? " Entrenched: " +
                        ent
                          .map(function (n) {
                            var h = n.hyi;
                            return (
                              "N" +
                              n.k +
                              " has held " +
                              en3(n.e) +
                              (h.since ? " since " + String(h.since).slice(0, 10) : "") +
                              (h.back ? (h.since ? " and " : " and ") + "came back " + (1 === h.back ? "once" : "twice") + " after changing" : "")
                            );
                          })
                          .join("; ") +
                        ". Opposition held this long costs more to cross."
                    : "";
                })();""")
rep("""                              s(t.p && t.p.m, C.p.m, e + "-P"),""", """                              s(t.p && t.p.m, C.p.m, e + "-P"),
                              t.eh &&
                                "object" == typeof t.eh &&
                                ((C.eh && "object" == typeof C.eh) || (C.eh = {}),
                                Object.keys(t.eh).forEach(function (id) {
                                  var a = C.eh[id],
                                    b = t.eh[id];
                                  Array.isArray(b) && b.length && (!Array.isArray(a) || b.length > a.length) && (C.eh[id] = b);
                                })),""")
rep('t.textContent = "v192"', 't.textContent = "v193"')
open(P, "w").write(s)
