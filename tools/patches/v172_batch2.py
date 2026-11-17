"""v172 batch 2: the word engine. E1 saturation filter, E2 sub-phrase reading, E4 low-meaning words.
Run on the readable source after v171: python3 batch2.py src.js"""
import sys
P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, n, a[:90])
    s = s.replace(a, b)


# ---- E4: words that carry no meaning of their own are never findings
rep('''  var Lt =
      "a about above''', '''  var Lt =
      "involved necessary a about above''')

# ---- E1: a word that runs through 40% or more of the answers and notes, and that the person splits
# into two or more recurring phrases, is the medium, not a signal. It stops counting as a recurring word,
# so findings name its phrases instead ("good fire", "prescribed fire") and never the bare word.
rep('''        h.length < 2 && !C.m.length && !C.p.m.length)
      )
        Rt.innerHTML =''', '''        (function () {
          var MED = {};
          h.length >= 10 &&
            Object.keys(g).forEach(function (w) {
              if (w.indexOf(" ") >= 0 || g[w] / h.length < 0.4) return;
              var subs = Object.keys(p).filter(function (b) {
                return p[b] >= 2 && b.split(" ").indexOf(w) >= 0;
              });
              var cnt = {};
              subs.forEach(function (b) {
                cnt[b] = p[b];
              });
              subs.length >= 2 && (MED[w] = { n: g[w], of: h.length, subs: subs, cnt: cnt });
            });
          Object.keys(MED).forEach(function (w) {
            g[w] = 1;
          });
          window.gsmMED = MED;
        })(),
        h.length < 2 && !C.m.length && !C.p.m.length)
      )
        Rt.innerHTML =''')

# ---- E2: say what the medium word means, phrase by phrase, by which side of the line each phrase sits on
rep('''          var E = Object.keys(r.k).filter(function (t) {
            return (
              !k[t] &&''', '''          Object.keys(window.gsmMED || {})
            .sort(function (x, y) {
              return window.gsmMED[y].n - window.gsmMED[x].n;
            })
            .slice(0, 3)
            .forEach(function (w, wi) {
            var M = window.gsmMED[w],
              rows = M.subs
                .map(function (b) {
                  var up = 0,
                    dn = 0,
                    tot = 0;
                  n.forEach(function (pc) {
                    if (!pc.t || !pc.t.b || !pc.t.b[b] || "GOAL" === pc.id) return;
                    tot++;
                    var sd =
                      null != pc.ys ? (pc.ys < 118 ? 1 : -1) : null != pc.q ? Pt[pc.q] : pc.nk ? Wt[pc.nk - 1] : 0;
                    sd > 0 ? up++ : sd < 0 && dn++;
                  });
                  return { b: b, n: M.cnt[b], side: up > dn ? 1 : dn > up ? -1 : 0, tot: tot };
                })
                .sort(function (x, y) {
                  return y.n - x.n;
                }),
              say = function (sd) {
                var r = rows.filter(function (x) {
                  return x.side === sd;
                });
                if (!r.length) return "";
                var t = r.slice(0, 4).map(function (x) {
                  return "<b>" + Gt(jt(x.b)) + "</b> (" + x.n + ")";
                });
                return t.length > 1 ? t.slice(0, -1).join(", ") + " and " + t[t.length - 1] : t[0];
              },
              hp = say(1),
              hn = say(-1),
              bo2 = say(0);
            c(
              "ONE WORD, SEVERAL MEANINGS",
              "<b>“" +
                Gt(jt(w)) +
                "”</b> is in " +
                M.n +
                " of your " +
                M.of +
                " answers and notes, so on its own it says little" +
                (wi
                  ? ". It is part of what the workbook is about, not a finding in it."
                  : ": like the water a fish swims in, it is what the whole workbook is about.") +
                " What it means changes with the words beside it." +
                (hp ? " Where things help, you write " + hp + "." : "") +
                (hn ? " Where things hinder, you write " + hn + "." : "") +
                (bo2 ? " On both sides of the line: " + bo2 + "." : "") +
                (wi
                  ? ""
                  : " Patterns reads these as separate ideas from here on and no longer reports the bare word by itself. If two of them are the same thing to you, or a kind you mean is missing, say so in your notes.") ,
              M.subs,
              null,
            );
          });
          var E = Object.keys(r.k).filter(function (t) {
            return (
              !k[t] &&''')

open(P, "w").write(s)
print("batch2 ok")
