"""v207: card titles carry their context in plain sight.
1. Every Taking Action card title shows the sentence it comes from in small gray text after it
   ("good fire: “…” (N16)"), instead of only on hover, which did not work for him.
2. Thread cards pick that sentence better. They took the first sentence that happened to carry the phrase
   (for "wildfire management": N12, agency administrators). Now every sentence that uses the phrase is
   weighed, and the one that shares the most words with the others (the phrase's common ground) is shown.
Usage: python3 v207_title_context.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


# 1: phBest keeps every sentence that carries each phrase (ranking unchanged)
rep(
    """              "goal" === it.src && (ex[key].g = 1);""",
    """              "goal" === it.src && (ex[key].g = 1);
              (ex[key].all = ex[key].all || []).push({ s: sen, src: it.src });""",
)
rep(
    """              if (seen[key]) continue;
              seen[key] = 1;""",
    """              if (seen[key]) continue;
              seen[key] = 1;
              ex[key] && (ex[key].all = ex[key].all || []).push({ s: sen, src: it.src });""",
)
# the second push covers later sentences; the first only the sentence that created the entry
rep(
    """              "goal" === it.src && (ex[key].g = 1);
              (ex[key].all = ex[key].all || []).push({ s: sen, src: it.src });""",
    """              "goal" === it.src && (ex[key].g = 1);
              ex[key].all || (ex[key].all = [{ s: sen, src: it.src }]);""",
)

# 2: the phrase's most central sentence
rep(
    """  // a card's title from the clause it came from
  function gsmPhClauseTitle(stems, text) {""",
    """  // the sentence that best carries a phrase: the one sharing the most words with its other sentences
  function phCentral(b, stems) {
    var A = (b.all || []).filter(function (x, i, z) {
      return (
        z.findIndex(function (y) {
          return y.s === x.s;
        }) === i
      );
    });
    if (A.length < 2) return A[0] || { s: b.sent, src: b.src };
    var S = phSet(stems),
      MED = window.gsmMED || {},
      bags = A.map(function (x) {
        var g = {};
        phToks(x.s).forEach(function (o) {
          o.c &&
            o.st.forEach(function (k) {
              S[k] || MED[k] || (g[k] = 1);
            });
        });
        return g;
      }),
      best = 0,
      bs = -1;
    bags.forEach(function (g, i) {
      var ks = Object.keys(g),
        sc = 0;
      ks.forEach(function (k) {
        bags.forEach(function (h, j) {
          j !== i && h[k] && sc++;
        });
      });
      var nw = A[i].s.split(/\\s+/).length;
      sc = (sc + 0.5) / Math.sqrt(ks.length + 1) - (nw < 6 ? 1 : 0) - ("goal" === A[i].src ? 0.25 : 0);
      sc > bs && ((bs = sc), (best = i));
    });
    return A[best];
  }
  // a card title with its context in small gray text after it (v207: hover did not work for him)
  function gsmHdT(title, sent, src) {
    sent = String(sent || "").replace(/\\s+/g, " ").trim();
    return (
      '<div class="hdt"><b>' +
      Gt(title) +
      "</b>" +
      (sent
        ? '<span class="phctx">: “' + Gt(sent) + "”" + (src ? " (" + ("goal" === src ? "the goal" : src) + ")" : "") + "</span>"
        : "") +
      "</div>"
    );
  }
  // a card's title from the clause it came from
  function gsmPhClauseTitle(stems, text) {""",
)
rep(
    """      return L[0] ? ((PhUsed[L[0].ph.toLowerCase()] = 1), L[0]) : null;""",
    """      L[0] && (L[0].ctx = phCentral(L[0], stems));
      return L[0] ? ((PhUsed[L[0].ph.toLowerCase()] = 1), L[0]) : null;""",
)

# 3: the three card headers
rep(
    """                    '<div class="coa"><div class="hd"><b' +
                    (PT ? ' title="' + phAttr(PT.sent) + '"' : "") +
                    ">" +
                    Gt(PT ? PT.ph : jt(t)) +
                    '</b><span class="mode' +""",
    """                    '<div class="coa"><div class="hd">' +
                    gsmHdT(PT ? PT.ph : jt(t), PT ? (PT.ctx || {}).s || PT.sent : "", PT ? (PT.ctx || {}).src || PT.src : "") +
                    '<span class="mode' +""",
)
rep(
    """                  '<div class="coa"><div class="hd"><b' +
                  (CT ? ' title="' + phAttr(CT.sent) + '"' : "") +
                  ">" +
                  Gt(e) +
                  '</b><span class="mode">PROGRAM</span></div><div class="bd">' +""",
    """                  '<div class="coa"><div class="hd">' +
                  gsmHdT(e, CT ? CT.sent : "", t.src) +
                  '<span class="mode">PROGRAM</span></div><div class="bd">' +""",
)
rep(
    """                    '<div class="coa"><div class="hd"><b' +
                    (CT ? ' title="' + phAttr(CT.sent) + '"' : "") +
                    ">" +
                    Gt(l) +
                    '</b><span class="mode' +""",
    """                    '<div class="coa"><div class="hd">' +
                    gsmHdT(l, CT ? CT.sent : "", CT ? "Q." + (t + 1) : "") +
                    '<span class="mode' +""",
)
rep(
    "#gsm .coa .hd{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-bottom:1px solid #ddd}",
    "#gsm .coa .hd{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-bottom:1px solid #ddd}"
    "#gsm .coa .hdt{flex:1;min-width:0}#gsm .coa .phctx{color:#777;font-size:13px;font-weight:400;line-height:1.4}",
)

s = s.replace('t.textContent = "v206"', 't.textContent = "v207"')
assert 't.textContent = "v207"' in s
open(P, "w").write(s)
