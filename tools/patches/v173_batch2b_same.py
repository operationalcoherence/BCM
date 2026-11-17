"""v172 batch 2b: E3, words the person says mean the same are read as one (asked, never assumed)."""
import sys
P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, n, a[:90])
    s = s.replace(a, b)


# tokenizer: apply the person's own "same" declarations (asks key "same|<word>|<word it means>" = "y")
rep('''  function Ht(t) {
    var e = { k: {}, b: {}, seq: [] },
      n = (t || "")''', '''  function Ht(t) {
    var e = { k: {}, b: {}, seq: [] },
      n = gsmSame(t || "")''')
rep('''  function P() {''', '''  function gsmSame(t) {
    var A = (C && C.asks) || {};
    Object.keys(A).forEach(function (k) {
      if (0 !== k.indexOf("same|") || "y" !== A[k]) return;
      var w = k.split("|");
      if (w.length < 3 || !/^[a-z][a-z-]*$/.test(w[1]) || !/^[a-z][a-z-]*$/.test(w[2])) return;
      t = t.replace(new RegExp("\\\\b" + w[1] + "(s?)\\\\b", "gi"), function (m, pl) {
        return w[2] + pl;
      });
    });
    return t;
  }
  function P() {''')

# the question, under ONE WORD, SEVERAL MEANINGS: two medium words, one inside the other (fire / wildfire)
rep('''          Object.keys(window.gsmMED || {})
            .sort(function (x, y) {''', '''          (function () {
            var MW = Object.keys(window.gsmMED || {}).map(function (w) {
                return jt(w).toLowerCase();
              }),
              A = C.asks || {},
              pr = null;
            MW.forEach(function (a) {
              MW.forEach(function (b) {
                !pr &&
                  a !== b &&
                  a.length > b.length &&
                  (a.slice(-b.length) === b || a.slice(0, b.length) === b) &&
                  null == A["same|" + a + "|" + b] &&
                  (pr = [a, b]);
              });
            });
            var done = Object.keys(A).filter(function (k) {
              return 0 === k.indexOf("same|") && "y" === A[k];
            });
            window.gsmAskSame = function (a, b, v) {
              ((C.asks && "object" == typeof C.asks) || (C.asks = {}), (C.asks["same|" + a + "|" + b] = v), P());
            };
            pr &&
              c(
                "THE SAME THING?",
                "Do <b>“" +
                  Gt(pr[0]) +
                  "”</b> and <b>“" +
                  Gt(pr[1]) +
                  "”</b> mean the same thing to you? Patterns keeps your words apart unless you say they are one, because merging two things you mean differently would hide a distinction. If you say yes, it reads “" +
                  Gt(pr[0]) +
                  "” as “" +
                  Gt(pr[1]) +
                  "” everywhere." +
                  '<div class="emo"><button type="button" class="ech" onclick="gsmAskSame(\\'' +
                  pr[0] +
                  "','" +
                  pr[1] +
                  '\\',\\'y\\')">Yes, the same</button><button type="button" class="ech" onclick="gsmAskSame(\\'' +
                  pr[0] +
                  "','" +
                  pr[1] +
                  "','n')\\">No, different</button></div>",
                [],
                null,
              );
            done.length &&
              c(
                "READ AS ONE",
                done
                  .map(function (k) {
                    var w = k.split("|");
                    return (
                      "You said <b>“" +
                      Gt(w[1]) +
                      "”</b> and <b>“" +
                      Gt(w[2]) +
                      "”</b> mean the same thing, so Patterns reads them as one word. " +
                      '<button type="button" class="ech" onclick="gsmAskSame(\\'' +
                      w[1] +
                      "','" +
                      w[2] +
                      "','n')\\">Read them apart again</button>"
                    );
                  })
                  .join("<br>"),
                [],
                null,
              );
          })();
          Object.keys(window.gsmMED || {})
            .sort(function (x, y) {''')
open(P, "w").write(s)
print("batch2b ok")
