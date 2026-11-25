# v273: THE LAY OF THE LAND retired (his call, 25 Nov 2026 13:48, option 1). Its numbered readings move onto
# YOUR LANDSCAPE, ONE QUESTION AT A TIME (the map with the notes), with their list folded under that map.
# Its patterns row, PATTERNS THAT RUN THROUGH IT, the old 2D controls and its own tour go with it.
# THE BARE LANDSCAPE stays bare. Place maps are unchanged.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:90])
    s = s.replace(old, new)

# 0. v272's BARE flag clashed with the engine's own BARE color ([238, 235, 227], declared later in the same
#    function), so every Pattern Analysis map behaved as the bare one. The flag is BAREH from here on.
import re
lines = s.split('\n')
for i, L in enumerate(lines):
    if 'THE BARE' in L or 'BARE ROCK' in L:
        continue
    lines[i] = re.sub(r'\bBARE\b(?!\s*\[|\.join|\s*=\s*\[)', 'BAREH', L)
s = '\n'.join(lines)

# 1. the section goes from the page
rep('''      if ("ABOUT WHAT YOU COLLECTED" === t) {
        /* its text goes; its fold now heads the ground (THE LAY OF THE LAND) and the hidden old figure it holds */
        var sp0 = k.querySelector("span");
        sp0 ? (sp0.textContent = "THE LAY OF THE LAND") : (k.textContent = "THE LAY OF THE LAND");
        for (var c = k.nextElementSibling; c && !c.classList.contains("plab") && !c.classList.contains("part"); ) {
          var c2 = c.nextElementSibling;
          /^(meta|msub|metal)$/.test(String(c.getAttribute("class") || "")) && c.remove();
          c = c2;
        }
        sb && sb.classList.remove("closed");''', '''      if ("ABOUT WHAT YOU COLLECTED" === t) {
        /* v273: THE LAY OF THE LAND is retired; its numbered readings are on YOUR LANDSCAPE */
        for (var c = k.nextElementSibling; c && !c.classList.contains("plab") && !c.classList.contains("part"); ) {
          var c2 = c.nextElementSibling;
          /* the hidden old figure stays (hidden): Taking Action's WHERE THE READING SPLITS is read from it */
          if (c.matches(".pnet") || c.querySelector(".pnet")) {
            c.querySelectorAll(".gterr-host").forEach(function (h) {
              h.parentNode.removeChild(h);
            });
            c.classList.remove("secb", "closed");
            c.style.display = "none";
            c.setAttribute("aria-hidden", "true");
          } else c.remove();
          c = c2;
        }
        k.remove();''')

# 2. YOUR LANDSCAPE carries the numbers (line maps only; the bare map stays bare)
rep('''        } else if (ANH && !PAR) {
          D.read = [];''', '''        } else if (ANH && !PAR) {
          D.read =
            BAREH || PLACE
              ? []
              : READ.map(function (r) {
                  return { at: r.at, title: r.title, text: r.short + (r.more ? " " + r.more : ""), grp: r.grp, cap: r.short };
                });
          D.read.length && (D.groups = GROUPS);''')
rep('''              BAREH && BAREAFTER && BAREAFTER(box);''', '''              BAREH && BAREAFTER && BAREAFTER(box);
              ANH &&
                !BAREH &&
                !PAR &&
                box.querySelectorAll(".grleg .r span").forEach(function (sp) {
                  /^Numbered: what the ground says/.test(sp.textContent) &&
                    (sp.textContent = "Numbered: what the ground says. Hover or tap a number to read it; the list is under the map.");
                  /^A brown line: a pattern you ticked/.test(sp.textContent) && sp.parentNode.parentNode.removeChild(sp.parentNode);
                });''')
rep('''        return t + " Tap a question above the map to see only its notes. With all notes shown, tap the ground to read what gathers there.";''',
    '''        return (
          t +
          " Tap a question above the map to see only its notes. With all notes shown, tap the ground to read what gathers there." +
          (READ.length && !PLACE ? " The numbers mark what stands out on the ground; tap one, or open the list under the map." : "")
        );''')

# 3. the list of what the numbers say, folded under that map (made once READ is filled)
rep('''    function fillReadings() {
      var el = $("readings");
      el.innerHTML = "";''', '''    function fillReadings() {
      var el = $("readings");
      el.innerHTML = "";
      if (ANH && !BAREH && !PAR && !PLACE && READ.length && !host._rdf) {
        host._rdf = document.createElement("details");
        host._rdf.className = "gfold";
        host._rdf.innerHTML = '<summary><span class="sec">WHAT THE NUMBERS ON THE MAP SAY</span></summary>';
        el.style.display = "";
        host._rdf.appendChild(el);
        host.appendChild(host._rdf);
      }''')

# 4. wording that pointed to the retired section
rep('(THE LAY OF THE LAND, Pattern Analysis)', '(YOUR LANDSCAPE, Pattern Analysis)')
rep('cap: cost + " THE LAY OF THE LAND, below, reads this ground in full.", at: null', 'cap: cost + " The numbers on this map read this ground in full.", at: null')

open(p, 'w', encoding='utf-8').write(s)
print('v273 patched')
