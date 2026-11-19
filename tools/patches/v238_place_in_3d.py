"""v238: YOUR PLACE IN 3D for workbooks that have both maps (F1, item 1; his yes 11-19 10:05:
"i dont want any modifications made to the line map and its visuals - its perfect. I am open to the place mapping").
Before: a workbook with any written note on the line map never showed its place map in 3D; the place notes were left off.
Now: when both maps have notes, Pattern Analysis and Pattern Synthesis each get a closed fold, YOUR PLACE IN 3D,
under the line-map view. Opening it builds the place ground (Esri imagery on the real terrain, notes as pins,
areas as patches, the goal at the location), the same view a place-only workbook already gets.
The line map is untouched: gsmData() is unchanged, so every line-map view, reading, card, and way is built
from exactly the same data as v237. Usage: python3 v238_place_in_3d.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# 1. the place view can be asked for even when the line map has notes (only by the new fold)
rep('''  function gsmPlaceView() {
    var has = function (t) {
      return Array.isArray(t) && String(t[3] || "").trim();
    };
    if (C.m.some(has)) return null;''',
'''  function gsmPlaceView(force) {
    var has = function (t) {
      return Array.isArray(t) && String(t[3] || "").trim();
    };
    if (!force && C.m.some(has)) return null;''')
rep('''  window.gsmData = function () {
    var pv = gsmPlaceView();
    return { m: pv ? pv.m : C.m, a: Q(), goal: C.goal, place: pv ? pv.place : null };''',
'''  /* v238: the place map's own data, only for a workbook that has both maps (the line map keeps gsmData) */
  window.gsmPlaceData = function () {
    if (
      !C.m.some(function (t) {
        return Array.isArray(t) && String(t[3] || "").trim();
      })
    )
      return null;
    var pv = gsmPlaceView(1);
    return pv ? { m: pv.m, a: Q(), goal: C.goal, place: pv.place } : null;
  };
  window.gsmPlaceFold = function () {
    var pd = window.gsmPlaceData ? window.gsmPlaceData() : null;
    return pd
      ? '<details class="fold gtpl" style="margin:14px 0 18px"><summary>YOUR PLACE IN 3D</summary><div class="intsub" style="margin:4px 0 8px">The notes you placed on the place map' +
          (pd.place && pd.place.name ? ", at " + String(pd.place.name).replace(/&/g, "&amp;").replace(/</g, "&lt;") : "") +
          ', on the real land. The ground is the real terrain, true to scale; emotion shows only as color.</div><div class="gtplbox"></div></details>'
      : "";
  };
  document.addEventListener(
    "toggle",
    function (e) {
      var d = e.target;
      if (!d || !d.classList || !d.classList.contains("gtpl") || !d.open) return;
      var b = d.querySelector(".gtplbox");
      if (b && !b.firstChild) b.innerHTML = '<div class="gterr-host" data-an="1" data-pl="1"></div>';
    },
    true,
  );
  window.gsmData = function () {
    var pv = gsmPlaceView();
    return { m: pv ? pv.m : C.m, a: Q(), goal: C.goal, place: pv ? pv.place : null };''')

# 2. the fold on Pattern Analysis, under YOUR LANDSCAPE, ONE QUESTION AT A TIME
rep('''            ? '<div class="plab">YOUR LANDSCAPE, ONE QUESTION AT A TIME</div><div class="gterr-host" data-an="1"></div>'
            : "") +''',
'''            ? '<div class="plab">YOUR LANDSCAPE, ONE QUESTION AT A TIME</div><div class="gterr-host" data-an="1"></div>' +
              (window.gsmPlaceFold ? window.gsmPlaceFold() : "")
            : "") +''')

# 3. the fold on Pattern Synthesis, after the line-map view
rep('''                '<div class="gterr-host"></div><div class="gtold" style="display:none" aria-hidden="true">' +
                  ee(de.slice(0, qe), ge, Eo, de) +
                  "</div>")''',
'''                '<div class="gterr-host"></div><div class="gtold" style="display:none" aria-hidden="true">' +
                  ee(de.slice(0, qe), ge, Eo, de) +
                  "</div>" +
                  (window.gsmPlaceFold ? window.gsmPlaceFold() : ""))''')

# 4. the host in the fold mounts with the place data
rep('''        var dd = window.gsmData ? window.gsmData() : window.gsmTD || {};
        h.getAttribute("data-an") && (dd.an = 1);''',
'''        var dd = h.getAttribute("data-pl") && window.gsmPlaceData ? window.gsmPlaceData() || {} : window.gsmData ? window.gsmData() : window.gsmTD || {};
        h.getAttribute("data-an") && (dd.an = 1);''')

# 5. inside the fold, place notes are P1, P2, ... (as elsewhere in a both-maps workbook), never N1 (the line map's).
#    NP is "N" for every existing view, so the line map's labels are unchanged.
rep('''        h.getAttribute("data-an") && (dd.an = 1);''', '''        h.getAttribute("data-an") && (dd.an = 1);
        h.getAttribute("data-pl") && (dd.pl = 1);''')
a = s.index('  function mount(host, data) {\n    "use strict";\n')
b = s.index('  window.gsmTerrainMount = mount;')
body = s[a:b]
assert body.count('"N" +') == 42, body.count('"N" +')
body = body.replace('"N" +', 'NP +')
body = body.replace('  function mount(host, data) {\n    "use strict";\n',
                    '  function mount(host, data) {\n    "use strict";\n    var NP = data && data.pl ? "P" : "N";\n', 1)
def r1(x, y):
    global body
    assert body.count(x) == 1, (body.count(x), x); body = body.replace(x, y)
r1('if (m.id[0] === "N") {', 'if (m.id[0] === NP) {')
r1('supStep.replace(/N(\\d+)/g, function (m, k) {', 'supStep.replace(new RegExp(NP + "(\\\\d+)", "g"), function (m, k) {')
r1('.replace(/^(?:note\\s*)/i, "N");', '.replace(/^(?:note\\s*)/i, NP);')
r1('          goalText: GOALTEXT,\n          place: PLACE,\n        };', '          goalText: GOALTEXT,\n          place: PLACE,\n        };\n        NP !== "N" && (D.np = NP);')
s = s[:a] + body + s[b:]

rep('t.textContent = "v237"', 't.textContent = "v238"')
open(P, 'w').write(s)
print("v238 applied")
