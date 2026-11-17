"""v173 batch 3b: U2, an explainer for each of the seven symbols (hover, tap or keyboard focus)."""
import sys, json
P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, n, a[:90])
    s = s.replace(a, b)


X = ["Q.1 · Within the community, why has the goal not already taken root? Place this where something already happening keeps the goal from taking root.",
     "Q.2 · Is there opposition to the goal? Place this where someone or something works against it.",
     "Q.3 · Is there support for the goal? Place this where someone or something already works for it.",
     "Q.4 · What conditions need to be established for the goal to take root and grow? Place this where a condition has to be met.",
     "Q.5 · What needs to be designed? Place this where something new has to be made.",
     "Q.6 · What needs to be redesigned? Place this where something that exists has to change.",
     "Q.7 · What needs to be reinforced? Place this where something that already works needs support to keep going."]
HINT = "Tap or hover a symbol to see what it marks."

rep('<div class="leg" id="gsm-leg"></div>', '<div class="leg" id="gsm-leg"></div><div class="symx" id="gsm-symx">' + HINT + '</div>')
rep('<div class="leg" id="gsm-pleg"></div>', '<div class="leg" id="gsm-pleg"></div><div class="symx" id="gsm-psymx">' + HINT + '</div>')
rep("#gsm .copy a{color:#555}", "#gsm .copy a{color:#555}#gsm .symx{font-size:13.5px;line-height:1.45;color:#333;background:#f4f4f2;border-left:3px solid #222;padding:6px 10px;margin:-4px 0 10px;min-height:2.9em}")
rep('''  var Y = document.getElementById("gsm-leg"),
    z = 0,
    V = "";''', '''  var SYX = %s;
  ["mouseover", "focusin", "click"].forEach(function (ev) {
    document.addEventListener(ev, function (x) {
      var c = x.target && x.target.closest ? x.target.closest("#gsm .leg .chip[data-k]") : null;
      if (!c) return;
      var box = c.parentNode.nextElementSibling;
      box && /\\bsymx\\b/.test(box.className) && (box.textContent = SYX[+c.getAttribute("data-k") - 1] || "");
    });
  });
  var Y = document.getElementById("gsm-leg"),
    z = 0,
    V = "";''' % json.dumps(X, ensure_ascii=False))
rep('''    V +=
      '<button type="button" class="chip" data-k="' +
      (e + 1) +
      '"><svg''', '''    V +=
      '<button type="button" class="chip" data-k="' +
      (e + 1) +
      '" title="' +
      Gt(SYX[e]) +
      '"><svg''')
rep('''        S +=
          '<button type="button" class="chip" data-k="' +
          (e + 1) +
          '"><svg''', '''        S +=
          '<button type="button" class="chip" data-k="' +
          (e + 1) +
          '" title="' +
          Gt(SYX[e]) +
          '"><svg''')
open(P, "w").write(s)
print("batch3b ok")
