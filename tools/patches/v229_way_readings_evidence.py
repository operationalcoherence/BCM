"""v229: the written readings of a card's ways (A: why choose it, comparing the ways, why take the harder way,
moves in order, when to stop and readjust; on programs, what the ground says) move from "Why this action" into
the card's Evidence, under "HOW THE WAYS READ ON THE GROUND". The map and the chart stay in layer 2. In full screen
the readings stay with the map, as before. Usage: python3 v229_way_readings_evidence.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
rep('''      box.appendChild(hd);
      courseReadings(COURSE).forEach(function (r) {''', '''      var EVH = null;
      if (CARDH && !isFull() && el.closest) {
        var card = el.closest(".coa"),
          bd = card && card.querySelector(":scope > .bd"),
          wy = bd && bd.querySelector(":scope > .tawhy");
        if (wy) {
          var ev = bd.querySelector(":scope > .taev");
          if (!ev) {
            ev = document.createElement("details");
            ev.className = "taev";
            ev.innerHTML = "<summary>Evidence</summary>";
            wy.parentNode.insertBefore(ev, wy.nextSibling);
          }
          EVH = ev.querySelector(":scope > .taways");
          if (!EVH) {
            EVH = document.createElement("div");
            EVH.className = "taways";
            ev.insertBefore(EVH, ev.firstElementChild ? ev.firstElementChild.nextSibling : null);
          }
          EVH.innerHTML = "";
          hd.textContent = "HOW THE WAYS READ ON THE GROUND";
          EVH.appendChild(hd);
        }
      }
      EVH || box.appendChild(hd);
      courseReadings(COURSE).forEach(function (r) {''')
rep('''        d.appendChild(b);
        box.appendChild(d);
      });
      cd.mode === "STRATEGY" && waysChart(box);''', '''        d.appendChild(b);
        (EVH || box).appendChild(d);
      });
      if (EVH) {
        var nt = document.createElement("div");
        nt.className = "small";
        nt.style.margin = "2px 0 8px";
        nt.textContent = "Read with the map and chart under Why this action: each letter is a way drawn there.";
        box.appendChild(nt);
      }
      cd.mode === "STRATEGY" && waysChart(box);''')
rep('''t.textContent = "v228"''', '''t.textContent = "v229"''')
open(P, "w").write(s)
print("ok")
