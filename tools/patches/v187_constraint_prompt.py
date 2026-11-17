"""v187 (T5): on each Taking Action card, notes in the low ground (aggression, distrust, defiance) get his question,
"What constraint or rule keeps this note in the low ground, and how do we change it?", with a box for the answer.
Answers are saved in the workbook (asks["cons|<note id>"]) and carried when workbooks are combined."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("#gsm .copy a{color:#555}", "#gsm .copy a{color:#555}#gsm .ccons{margin:8px 0 2px}#gsm .ccq{display:block;font-size:13px;margin:3px 0 0;color:#222}#gsm .ccons textarea{display:block;width:100%;font:inherit;font-size:13.5px;border:1px solid #bbb;padding:6px 8px;margin:4px 0 10px;resize:vertical;background:#fff}#gsm .ccons textarea:focus{border-color:#222;outline:0}")

rep("""  function gsmSame(t) {""", """  document.addEventListener("input", function (ev) {
    var t = ev.target;
    if (!t || !t.getAttribute || null == t.getAttribute("data-cons")) return;
    (C.asks && "object" == typeof C.asks && !Array.isArray(C.asks)) || (C.asks = {});
    var id = t.getAttribute("data-cons"),
      k = "cons|" + id;
    t.value.trim() ? (C.asks[k] = t.value) : delete C.asks[k];
    document.querySelectorAll("textarea[data-cons]").forEach(function (o) {
      o !== t && o.getAttribute("data-cons") === id && (o.value = t.value);
    });
    try {
      localStorage.setItem(S, JSON.stringify(C));
    } catch (e) {}
  });
  function gsmSame(t) {""")

rep("""              u = (c.match(/class="cq"/g) || []).length + (c.match(/class="csl"/g) || []).length;
            return c
              ? (c.match(/class="cq"/g) || []).length <= 2
                ? l + c
                : l +""", """              u = (c.match(/class="cq"/g) || []).length + (c.match(/class="csl"/g) || []).length;
            l += (function (items) {
              var EN = ["aggression", "", "distrust", "", "defiance"],
                AK = C.asks || {},
                low = items
                  .filter(function (x) {
                    var r = x.line || x.place;
                    return r && String(r[3] || "").trim() && (0 === r[5] || 2 === r[5] || 4 === r[5]);
                  })
                  .slice(0, 4);
              if (!low.length) return "";
              return (
                '<div class="csec"><div class="csl">WHAT HOLDS IT IN THE LOW GROUND</div><div class="csn">The ways through it find the easiest path within things as they are. ' +
                (1 === low.length ? "This note sits" : "These notes sit") +
                " in the low ground. A different move is to change what holds " +
                (1 === low.length ? "it" : "them") +
                " there, which reshapes the ground itself.</div>" +
                low
                  .map(function (x) {
                    var r = x.line || x.place,
                      key = String(r[8] || x.id),
                      v = AK["cons|" + key] || "",
                      n = String(r[3] || "").replace(/\\s+/g, " ").trim();
                    return (
                      '<div class="ccons"><div class="cq"><span class="wh">' +
                      Gt(x.id) +
                      '</span> <i class="cqm">' +
                      EN[r[5]] +
                      "</i> \\u2014 \\u201c" +
                      Gt(n.length > 64 ? n.slice(0, 64).replace(/\\s+\\S*$/, "") + "\\u2026" : n) +
                      '\\u201d</div><label class="ccq">What constraint or rule keeps this note in the low ground, and how do we change it?<textarea data-cons="' +
                      Gt(key) +
                      '" rows="2" placeholder="The constraint or rule, and how to change it">' +
                      Gt(v) +
                      "</textarea></label></div>"
                    );
                  })
                  .join("") +
                '<div class="csn" style="font-size:12.5px;color:#666">A change you name here is a condition (Q.4), a redesign (Q.6) or something to reinforce (Q.7). Add it there too, so the rest of the method sees it. After Juarrero (2023).</div></div>'
              );
            })(s || []);
            return c
              ? (c.match(/class="cq"/g) || []).length <= 2
                ? l + c
                : l +""")
rep('t.textContent = "v186"', 't.textContent = "v187"')
open(P, "w").write(s)
