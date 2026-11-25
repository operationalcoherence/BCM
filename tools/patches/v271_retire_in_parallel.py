# v271: In Parallel retired as a tab (his call, 25 Nov 2026 12:08). What was worth keeping moves
# into Pattern Analysis as one section, YOUR WORDS ON THE GROUND, placed right after THE LAY OF
# THE LAND: the agreement figure (lines from words to the ground), "Where to start", and WORTH A
# SECOND LOOK (PLACED ONE WAY, TIED THE OTHER; THE HIDDEN CHANNELS; TWO PEOPLE, TWO SIDES; and any
# others under "More patterns"). Dropped because Analysis already says it: ONE IDEA UNDER TWO NAMES
# (THE SAME THING?), the Emotion, Closest and farthest, and Voices readings (WHAT HOLDS..., WHERE IT
# CAN CROSS, RUNS TOGETHER, the one-voice lead), MORE FROM BOTH PICTURES, THE EARLIER 3D VIEW, and
# the no-notes fallback figures. Taking Action's WHERE THE READING SPLITS still reads every split.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:90])
    s = s.replace(old, new)

# 1. the section: heading, no part, no old 3D, no fallback figures
rep('(ut.textContent = "THE TWO PICTURES TOGETHER")', '(ut.textContent = "YOUR WORDS ON THE GROUND")')
i0 = s.index("? '<div class=\"agslot\"></div><details class=\"fold parold\"")
i1 = s.index("'<div class=\"intsub\">How everything ties to everything</div></div></div>') +", i0)
i1 += len("'<div class=\"intsub\">How everything ties to everything</div></div></div>')")
s = s[:i0] + "? '<div class=\"agslot\"></div>'\n                        : '')" + s[i1:]
rep('''                    a
                      ? (Rt.insertBefore(ct, a), Rt.insertBefore(ut, a), Rt.insertBefore(lt, a))
                      : (Rt.appendChild(ct), Rt.appendChild(ut), Rt.appendChild(lt)),''',
    '''                    gsmWGPlace(Rt, ut, lt, a),''')
rep('''                      PO && PB && lt.insertBefore(PO, PB);
                    })(),''', '''                      PO && PB && lt.insertBefore(PO, PB);
                      if (!AG && !lt.querySelector(".intrev")) {
                        ut.parentNode && ut.parentNode.removeChild(ut);
                        lt.parentNode && lt.parentNode.removeChild(lt);
                      }
                    })(),''')
rep('Rt.insertBefore(ht, ct));', 'void ht);')
rep('''                          "THE TWO PICTURES TOGETHER" === r ||''', '''                          "THE TWO PICTURES TOGETHER" === r ||
                          "YOUR WORDS ON THE GROUND" === r ||''')

# 2. place it right after THE LAY OF THE LAND (else at the end of Analysis)
rep('''  // v216: In Parallel under the figure''', '''  // v271: the In Parallel section now sits in Pattern Analysis, after THE LAY OF THE LAND
  function gsmWGPlace(Rt, ut, lt, a) {
    var kids = [].slice.call(Rt.children),
      at = a || null,
      k = -1;
    kids.forEach(function (x, i) {
      x.classList.contains("plab") && /^THE LAY OF THE LAND/.test(x.textContent.trim()) && (k = i);
    });
    if (k >= 0) {
      at = null;
      for (var i = k + 1; i < kids.length; i++)
        if (kids[i].classList.contains("plab") || kids[i].classList.contains("part")) {
          at = kids[i];
          break;
        }
    }
    Rt.insertBefore(ut, at);
    Rt.insertBefore(lt, at);
  }
  // v216: In Parallel under the figure''')

# 3. only Where to start and the second-look patterns remain
i0 = s.index('  function gsmIntOrder(E, f) {')
i1 = s.index('  // v213: THE TWO PICTURES, SIDE BY SIDE')
s = s[:i0] + '''  function gsmIntOrder(E, f) {
    var top = [],
      look = [];
    E.forEach(function (t) {
      "Where to start" === t[0]
        ? top.push(f(t))
        : "Patterns worth a second look" === t[0] && /class="rule"/.test(t[1]) &&
          look.push(f(t).replace("<b>Patterns worth a second look.</b> ", ""));
    });
    return (
      top.join("") +
      (look.length ? '<div class="intrev"><div class="intrevh">WORTH A SECOND LOOK</div>' + look.join("") + "</div>" : "")
    );
  }
''' + s[i1:]

# 4. ONE IDEA UNDER TWO NAMES is THE SAME THING? on Analysis: not shown twice (Taking Action still reads it)
rep('''                        return "PLACED ONE WAY, TIED THE OTHER" === t.lab || "THE HIDDEN CHANNELS" === t.lab;
                      },
                      ot = R.filter(PRI).concat(
                        R.filter(function (t) {''', '''                        return "PLACED ONE WAY, TIED THE OTHER" === t.lab || "THE HIDDEN CHANNELS" === t.lab;
                      },
                      R2 = R.filter(function (t) {
                        return "ONE IDEA UNDER TWO NAMES" !== t.lab;
                      }),
                      ot = R2.filter(PRI).concat(
                        R2.filter(function (t) {''')
rep('''                      rt = R.filter(function (t) {
                        return ot.indexOf(t) < 0;''', '''                      rt = R2.filter(function (t) {
                        return ot.indexOf(t) < 0;''')
rep('''                    R.forEach(function (t) {
                      KIND[t.lab] && kinds.indexOf(KIND[t.lab]) < 0''', '''                    R2.forEach(function (t) {
                      KIND[t.lab] && kinds.indexOf(KIND[t.lab]) < 0''')

# 5. no In Parallel tab; a saved In Parallel tab opens Pattern Analysis
rep('''<button type="button" data-v="2">Pattern Analysis</button><button type="button" data-v="6">' +
          n +
          '</button><button type="button" data-v="4">Taking Action</button>''',
    '''<button type="button" data-v="2">Pattern Analysis</button><button type="button" data-v="4">Taking Action</button>''')
rep('        3 === i && (i = 2);', '        (3 === i || 6 === i) && (i = 2);')

# 6. parts renumbered; the PDF's part 2 is Taking Action
rep('<div class="part">3 · COURSES OF ACTION', '<div class="part">2 · COURSES OF ACTION')
rep('''                                      (H(),
                                      z("In Parallel"),''', '''                                      (H(),
                                      z("Taking Action"),''')

# 7. wording that named In Parallel or the two pictures
rep('In Parallel found nothing that splits the reading of these cards.', 'Pattern Analysis found nothing that splits the reading of these cards.')
rep('What In Parallel found under this card’s notes', 'What Pattern Analysis found under this card’s notes')
rep('Pattern Analysis keeps its own column; a line runs from each of its words to every note on the ground that carries it.',
    'Your words keep their own column; a line runs from each to every note on the ground that carries it.')
rep('the ground agrees with what Analysis found.', 'the ground agrees with what your words say.', 2)
rep('Tap a word to follow it here and on the 3D map in Pattern Analysis, under THE LAY OF THE LAND.', 'Tap a word to follow it here and on the 3D map above.')
rep('"aria-label": "Pattern Analysis words in a column', '"aria-label": "Your words in a column')
rep('t0.textContent = "PATTERN ANALYSIS";', 't0.textContent = "YOUR WORDS";')
rep('"Tap a word to read what both pictures say about it."', '"Tap a word to read what the ground says about it."', 2)
rep('or read differently by the two pictures</span>', 'or read differently by your words and the ground</span>')
rep('ft.textContent = "THE TWO PICTURES, SIDE BY SIDE";', 'ft.textContent = "YOUR WORDS ON THE GROUND";')
rep('bt.textContent = "See it on the 3D map in Pattern Analysis";', 'bt.textContent = "See it on the 3D map";')
rep('so what both pictures say about them rests on little', 'so what Patterns says about them rests on little', 2)
rep('your thinnest voice, so what both pictures say about it rests on little.', 'your thinnest voice, so what Patterns says about it rests on little.')
rep('"the least expected thing in the two pictures may be "', '"the least expected thing in your workbook may be "')

# 8. the second-look readings carry their own wording; Analysis's meaning pass leaves them alone
rep('''    sec.querySelectorAll(".rule").forEach(function (r) {
      if (r.getAttribute("data-mp")) return;''', '''    sec.querySelectorAll(".rule").forEach(function (r) {
      if (r.getAttribute("data-mp") || r.closest(".intrev")) return;''')

rep('" ONE WORD, SEVERAL MEANINGS on Pattern Analysis shows the phrases each side uses."', '" ONE WORD, SEVERAL MEANINGS, above, shows the phrases each side uses."')

s = s.replace('t.textContent = "v270"', 't.textContent = "v271"')
assert 't.textContent = "v271"' in s
open(p, 'w', encoding='utf-8').write(s)
print('ok')
