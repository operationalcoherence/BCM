"""v194 (F4): the reflexive loop (map -> act -> re-map).
Each Taking Action card gets WHAT YOU DID under YOUR DECISION: write what you did and what happened, then Log it.
Logging stores the entry (acts: [{k: card, t, w, x, n: noteIds, l: labels}]) and flags the card's Q.1-Q.4 notes for
re-mapping (remap: {noteId: time}). Mapping Landscape then shows SINCE YOU ACTED with those notes until each is edited
(its mt is newer than the flag) or marked Done."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("#gsm .copy a{color:#555}", "#gsm .copy a{color:#555}#gsm .acted{margin:12px 0 0;padding-top:10px;border-top:1px solid #e4e4e4}#gsm .acted textarea{display:block;width:100%;font:inherit;font-size:13.5px;border:1px solid #bbb;padding:6px 8px;margin:6px 0;resize:vertical;background:#fff}#gsm .actr{font-size:13.5px;margin:6px 0 8px;line-height:1.45}#gsm .actr .ad{color:#666;font-size:12px;letter-spacing:.03em}#gsm .sincebox{border:1px solid #222;padding:10px 12px;margin:10px 0 14px;font-size:14px;line-height:1.5}#gsm .sincebox .sh{font-size:12px;letter-spacing:.14em;margin-bottom:4px}#gsm .sincebox .sr{margin:4px 0}#gsm .sincebox button{margin-left:6px}")

rep("""  function gsmPlaceView() {""", """  function gsmCardQ14(card) {
    var el = card.querySelector("[data-ids]"),
      out = [];
    if (!el) return out;
    String(el.getAttribute("data-ids") || "")
      .split(",")
      .forEach(function (x) {
        x = x.trim();
        var m = /^(?:note\\s*|N)?(\\d+)$/i.exec(x),
          pm = /^P(\\d+)$/i.exec(x),
          pl = !!pm,
          k = pm ? +pm[1] : m ? +m[1] : 0,
          r = k ? (pl ? C.p.m[k - 1] : C.m[k - 1]) : null;
        r &&
          r[8] &&
          r[0] >= 1 &&
          r[0] <= 4 &&
          !out.some(function (o) {
            return o.id === r[8];
          }) &&
          out.push({ id: String(r[8]), lab: p(pl, k - 1) });
      });
    return out;
  }
  function gsmSince() {
    var sp = N.querySelector('.sprog[data-tab="1"]');
    if (!sp) return;
    var bx = document.getElementById("gsm-since"),
      RM = C.remap && "object" == typeof C.remap ? C.remap : {},
      MT = C.mt || {},
      lab = {},
      txt = {};
    C.m.forEach(function (r, i) {
      r && r[8] && ((lab[r[8]] = p(0, i)), (txt[r[8]] = r[3]));
    });
    C.p.m.forEach(function (r, i) {
      r && r[8] && ((lab[r[8]] = p(1, i)), (txt[r[8]] = r[3]));
    });
    var ids = Object.keys(RM).filter(function (id) {
      var keep = lab[id] && !(MT[id] && MT[id] > RM[id]);
      keep || delete RM[id];
      return keep;
    });
    if (!ids.length) return void (bx && bx.parentNode.removeChild(bx));
    bx ||
      ((bx = document.createElement("div")),
      (bx.id = "gsm-since"),
      (bx.className = "sincebox" + (sp.classList.contains("tabhide") ? " tabhide" : "")),
      bx.setAttribute("data-tab", "1"),
      sp.parentNode.insertBefore(bx, sp.nextSibling),
      bx.addEventListener("click", function (ev) {
        var b = ev.target.closest && ev.target.closest("button[data-sd]");
        b && C.remap && (delete C.remap[b.getAttribute("data-sd")], P(), gsmSince());
      }));
    var acts = Array.isArray(C.acts) ? C.acts : [],
      last = acts[acts.length - 1];
    bx.innerHTML =
      '<div class="sh">SINCE YOU ACTED</div><div>' +
      (last ? "You logged " + Gt('"' + String(last.x).slice(0, 80) + (String(last.x).length > 80 ? "\\u2026" : "") + '"') + " (" + Gt(String(last.t).slice(0, 10)) + "). " : "") +
      "Check these notes on the map: has their emotion or place changed? Edit a note and it leaves this list. Then read Pattern Synthesis again.</div>" +
      ids
        .slice(0, 12)
        .map(function (id) {
          var t = String(txt[id] || "").replace(/\\s+/g, " ").trim();
          return (
            '<div class="sr"><b>' +
            Gt(lab[id]) +
            "</b> \\u2014 " +
            Gt(t.length > 70 ? t.slice(0, 70) + "\\u2026" : t) +
            '<button type="button" class="lnk sm" data-sd="' +
            Gt(id) +
            '">Done</button></div>'
          );
        })
        .join("");
  }
  function gsmActUI(card, key, bd) {
    if (card.querySelector(".acted")) return;
    Array.isArray(C.acts) || (C.acts = []);
    var w = document.createElement("div");
    w.className = "acted";
    w.innerHTML =
      '<span class="eml">WHAT YOU DID</span>' +
      C.acts
        .filter(function (a) {
          return a && a.k === key;
        })
        .map(function (a) {
          return (
            '<div class="actr"><span class="ad">' +
            Gt(String(a.t).slice(0, 10)) +
            (a.w ? " \\u00b7 " + Gt(a.w) : "") +
            "</span><br>" +
            Gt(a.x) +
            (a.l && a.l.length ? '<br><span class="ad">Flagged to check on the map: ' + Gt(a.l.join(", ")) + "</span>" : "") +
            "</div>"
          );
        })
        .join("") +
      '<textarea class="actx" rows="2" maxlength="600" placeholder="What you did, and what happened" aria-label="What you did, and what happened"></textarea><button type="button" class="ech actgo">Log it</button><div class="actmsg" style="font-size:13px;color:#555;margin-top:6px"></div>';
    bd.appendChild(w);
    w.querySelector(".actgo").addEventListener("click", function () {
      var tx = w.querySelector(".actx").value.trim(),
        msg = w.querySelector(".actmsg");
      if (!tx) return void (msg.textContent = "Write what you did first.");
      var now = new Date().toISOString(),
        fl = gsmCardQ14(card);
      C.acts.push({ k: key, t: now, w: (C.who || "").trim(), x: tx, n: fl.map(function (f) { return f.id; }), l: fl.map(function (f) { return f.lab; }) });
      (C.remap && "object" == typeof C.remap) || (C.remap = {});
      fl.forEach(function (f) {
        C.remap[f.id] = now;
      });
      R("act", key, tx.slice(0, 80));
      w.querySelector(".actx").value = "";
      msg.textContent = fl.length
        ? "Logged. " + fl.map(function (f) { return f.lab; }).join(", ") + " (Q.1\\u2013Q.4) are flagged on Mapping Landscape: check whether their emotion or place has changed, then read Pattern Synthesis again."
        : "Logged. When the map changes, read Pattern Synthesis again.";
      P();
      gsmSince();
    });
  }
  function gsmPlaceView() {""")
# card injection after the decision row
rep("""                      ((e.w = a.value), (t[o] = e), P(), se());
                    }),
                    n.appendChild(i));""", """                      ((e.w = a.value), (t[o] = e), P(), se());
                    }),
                    n.appendChild(i),
                    gsmActUI(e, o, n));""")
# show the list at start and keep it current
rep("""    (C.sv = 2),
    gsmEHrec(),""", """    (C.sv = 2),
    gsmEHrec(),
    Array.isArray(C.acts) || (C.acts = []),
    (C.remap && "object" == typeof C.remap && !Array.isArray(C.remap)) || (C.remap = {}),""")
rep("""  function P() {
    (B(), gsmEHrec(), clearTimeout(j),""", """  function P() {
    (B(), gsmEHrec(), setTimeout(gsmSince, 0), clearTimeout(j),""")
rep("""      function O(i) {
        ((r = i), N.classList.toggle("onstart", 5 === i), N.classList.toggle("onta", 4 === i));""", """      function O(i) {
        ((r = i), N.classList.toggle("onstart", 5 === i), N.classList.toggle("onta", 4 === i), gsmSince());""")
rep('t.textContent = "v193"', 't.textContent = "v194"')
open(P, "w").write(s)
