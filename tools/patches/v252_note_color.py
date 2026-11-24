"""v252: every note brings its own emotion color to its own spot on the 3D ground (his screenshot 11-20 15:45:
"The acceptance emotion doesnt show up on hinder." "It didn't bring its color with it.").
Cause: the ground color is a blend of every note within reach, with each emotion's weight raised to the power 2.2,
so a lone note among many of another emotion (acceptance among the hinder side's aggression, distrust and defiance)
was outvoted at its own spot. Fix: each note also has a small patch of its own (radius about 8 map units).
Where that patch is stronger than the blend already shows, its emotion takes the spot; where the note's color already
wins, nothing changes. The rock face and the indifference band step aside inside the patch, so a lone note in
distant ground shows as a small patch ringed by rock. Heights are unchanged. Color only.
Usage: python3 v252_note_color.py tools/relief/relief.js gsm-readable.js"""
import sys
R, G = sys.argv[1], sys.argv[2]
def patch(P, pairs):
    s = open(P).read()
    for a, b in pairs:
        c = s.count(a); assert c == 1, (P, c, a[:90]); s = s.replace(a, b)
    open(P, 'w').write(s)
patch(R, [(
'''    let tot = 0, p = 0; for (let k = 0; k < K; k++) { const v = (ws[k] * (k === DEF ? 1.6 : 1)) ** 2.2; EF.a[o + k] = v; p += v; tot += ws[k]; }
    for (let k = 0; k < K; k++) EF.a[o + k] /= (p || 1);
    EF.a[o + K] = sstep(0.04, 0.5, tot); EF.a[o + K + 2] = RIB.length ? sstep(0.9, 2.0, ribAt(x, y)) : 0;
    const ord = [...ws.keys()].sort((u, v) => ws[v] - ws[u]), k1 = ord[0], k2 = ord[1], s1 = ws[k1], s2 = ws[k2];
    EF.a[o + K + 1] = (Math.abs(RANK[k1] - RANK[k2]) < 2 || RANK[k1] === 1 || RANK[k2] === 1 || s2 < 0.03) ? 0 : sstep(0.22, 0.42, s2 / (s1 + s2));''',
'''    let tot = 0, p = 0; for (let k = 0; k < K; k++) { const v = (ws[k] * (k === DEF ? 1.6 : 1)) ** 2.2; EF.a[o + k] = v; p += v; tot += ws[k]; }
    for (let k = 0; k < K; k++) EF.a[o + k] /= (p || 1);
    EF.a[o + K] = sstep(0.04, 0.5, tot); EF.a[o + K + 2] = RIB.length ? sstep(0.9, 2.0, ribAt(x, y)) : 0;
    const ord = [...ws.keys()].sort((u, v) => ws[v] - ws[u]), k1 = ord[0], k2 = ord[1], s1 = ws[k1], s2 = ws[k2];
    EF.a[o + K + 1] = (Math.abs(RANK[k1] - RANK[k2]) < 2 || RANK[k1] === 1 || RANK[k2] === 1 || s2 < 0.03) ? 0 : sstep(0.22, 0.42, s2 / (s1 + s2));
    /* v252: every note keeps its own color at its own spot, however many notes of other emotions are near */
    let kO = -1, wO = 0; EN.forEach(n => { const w = Math.exp(-((n.x - x) ** 2 + (n.y - y) ** 2) / (2 * 8 * 8)); if (w > wO) { wO = w; kO = n.e; } });
    if (kO >= 0) { const pw = sstep(0.25, 0.7, wO) * (1 - EF.a[o + kO]);
      if (pw > 0.001) { for (let k = 0; k < K; k++) EF.a[o + k] = EF.a[o + k] * (1 - pw) + (k === kO ? pw : 0);
        EF.a[o + K + 1] *= 1 - pw; if (kO !== IND) EF.a[o + K + 2] *= 1 - pw; EF.a[o + K] = Math.max(EF.a[o + K], pw); } }''')])
patch(G, [('t && (t.textContent = "v251");', 't && (t.textContent = "v252");')])
