"""v239: Taking Action shows each strategy's and program's 3D map by default (his ask 11-19 10:26:
"keep taking action 98% of the way it is, but show the 3D maps of the strategies/programs by default.
Keep everything else compacted, but show the 3d maps").
Before: THE WAY THROUGH IT (the card's map) sat inside the closed "Why this action" fold.
Now: it sits open, right under the decision strip; Why this action and Evidence stay closed with everything else.
Cards folded under MORE ... FROM THE WORDS YOU USE stay folded (their maps show when opened).
Usage: python3 v239_ta_maps_open.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep('''    w.innerHTML = "<summary>Why this action</summary>";
    L2.forEach(function (x) {
      w.appendChild(x[1]);
    });
    bd.insertBefore(sp, bd.firstChild);
    h ? sp.parentNode.insertBefore(w, sp.nextSibling) : (sp.parentNode.removeChild(sp), bd.insertBefore(w, bd.firstChild));''',
'''    w.innerHTML = "<summary>Why this action</summary>";
    /* v239: the card's map (THE WAY THROUGH IT) stays open, under the decision strip */
    var mapSec = null;
    L2.forEach(function (x) {
      8 === x[0] && !mapSec ? (mapSec = x[1]) : w.appendChild(x[1]);
    });
    bd.insertBefore(sp, bd.firstChild);
    h ? sp.parentNode.insertBefore(w, sp.nextSibling) : (sp.parentNode.removeChild(sp), bd.insertBefore(w, bd.firstChild));
    mapSec && (mapSec.classList.add("tamap"), w.parentNode.insertBefore(mapSec, w));''')

# the note under the map pointed to "the map and chart under Why this action"; the map is no longer there
rep('nt.textContent = "Read with the map and chart under Why this action: each letter is a way drawn there.";',
    'nt.textContent = "Each letter on the map is a way; its reading is under Evidence.";')
# "Named above, not on the map" read only the text above the map; with the map moved up it read only the strip.
# On a layered card it now reads what used to sit above the map inside Why this action (the same text as before), and says "on this card".
rep('''              for (var r = "", i = 0; i < n.children.length && n.children[i] !== e; i++)
                r += " " + n.children[i].textContent;''',
'''              for (var r = "", i = 0; i < n.children.length && n.children[i] !== e; i++)
                r += " " + n.children[i].textContent;
              /* v239: the map now sits above Why this action, so read what used to sit above it there */
              var tamap = e.classList.contains("tamap");
              tamap &&
                [].forEach.call(n.querySelectorAll(":scope > .tawhy > :not(summary)"), function (x) {
                  var l = x.querySelector(":scope > .csl");
                  (l && "WHAT HOLDS IT IN THE LOW GROUND" === l.textContent.trim()) || (r += " " + x.textContent);
                });''')
rep('''c.appendChild(document.createTextNode("Named above, not on the map: ")),''',
'''c.appendChild(document.createTextNode(tamap ? "Named on this card, not on the map: " : "Named above, not on the map: ")),''')
rep('t.textContent = "v238"', 't.textContent = "v239"')
open(P, 'w').write(s)
print("v239 applied")
# The 3D part (tools/relief/relief.js, edited directly as in earlier versions): on a card (D.card) the legend is
# a closed <details class="grlf"> "Legend"; the full-screen drawer opens its copy.
