"""v254: the whole 3D ground reads as rock, not coral (his note 11-24 10:00: "it looks more like corral than it looks
like rock"; the close-up was right, the whole map was not). The small, even bumps laid over the notes' shape are replaced:
steep ground steps down in bedded cliff bands that follow the slope, hard layers standing out over soft ones and fading
along their length; gentle ground rolls. One bedding coordinate drives both the ledges and the rock's color bands.
The shape from the notes (hRaw) is the same. Place maps are untouched.
Usage: python3 v254_rock_not_coral.py tools/relief/relief.js gsm-readable.js"""
import sys
R, G = sys.argv[1], sys.argv[2]
def patch(P, pairs):
    s = open(P).read()
    for a, b in pairs:
        c = s.count(a); assert c == 1, (P, c, a[:90]); s = s.replace(a, b)
    open(P, 'w').write(s)
PAIRS = [
[
"  const VRG = PL && PL.elev && PL.elev.hi > PL.elev.lo ? (PL.elev.hi - PL.elev.lo) / MPU : 0, VEX = VRG ? Math.max(1, Math.min(2.5, 140 / VRG)) : 2.5, VXT = VEX > 1.05 ? 'with heights exaggerated ' + (Math.round(VEX * 10) / 10) + '\u00d7 so its slopes and benches show' : 'true to scale';\n  function hAt(x, y) { if (PL) return PL.elev ? PL.elev(x, y) / MPU * VEX : 0; const e = 0.6, gx = (hRaw(x + e, y) - hRaw(x - e, y)) / (2 * e), gy = (hRaw(x, y + e) - hRaw(x, y - e)) / (2 * e), s = Math.hypot(gx, gy);",
"  const VRG = PL && PL.elev && PL.elev.hi > PL.elev.lo ? (PL.elev.hi - PL.elev.lo) / MPU : 0, VEX = VRG ? Math.max(1, Math.min(2.5, 140 / VRG)) : 2.5, VXT = VEX > 1.05 ? 'with heights exaggerated ' + (Math.round(VEX * 10) / 10) + '\u00d7 so its slopes and benches show' : 'true to scale';\n  function cell(x, y) { const i = Math.floor(x), j = Math.floor(y); let f1 = 9, f2 = 9, id = 0;\n    for (let a = -1; a <= 1; a++) for (let b = -1; b <= 1; b++) { const ci = i + a, cj = j + b, dx = ci + hash(ci, cj) - x, dy = cj + hash(cj + 71, ci + 13) - y, d = dx * dx + dy * dy;\n      if (d < f1) { f2 = f1; f1 = d; id = hash(ci + 5, cj + 3); } else if (d < f2) f2 = d; }\n    return [Math.sqrt(f1), Math.sqrt(f2), id]; }\n  /* v254: the rock's bedding, one coordinate shared by the ledges and the rock's color: a layer every LP units of height,\n     with a slight dip and a slow wander */\n  const LP = 6, layerAt = (x, y, hr) => { const L = hr / LP + x * 0.025 - y * 0.012 + (fbm(x * 0.05 + 11, y * 0.05, 3) - 0.5) * 1.8; return L + 0.3 * Math.sin(L * 2.1 + 1.3) + 0.12 * Math.sin(L * 4.7); };\n  function hAt(x, y) { if (PL) return PL.elev ? PL.elev(x, y) / MPU * VEX : 0; const e = 0.6, gx = (hRaw(x + e, y) - hRaw(x - e, y)) / (2 * e), gy = (hRaw(x, y + e) - hRaw(x, y - e)) / (2 * e), s = Math.hypot(gx, gy);"
],
[
"    const k = sstep(0.25, 1.1, s), ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);\n    const gul = (ridged(across * 0.18 + vn(x * 0.04, y * 0.04) * 2, along * 0.025, 3) - 0.4) * 2.4 * k;\n    return (hRaw(x, y) + gul + (ridged(x * 0.11 + 3, y * 0.11 + 7) - 0.35) * 0.9 * (1 - 0.6 * k) + (fbm(x * 0.35, y * 0.35, 3) - 0.5) * 0.5); }\n  const MX = 2 * VX - 1, MY = 2 * VY - 1, CK = landKey(D), CH = CACHE.get(CK) || {};",
"    const k = sstep(0.25, 1.1, s), ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);\n    const gul = (ridged(across * 0.18 + vn(x * 0.04, y * 0.04) * 2, along * 0.025, 3) - 0.4) * 1.6 * k, hr = hRaw(x, y);\n    /* v254: the surface detail reads as rock, not coral: steep ground steps down in ledges of bedded rock that follow the\n       slope (the layers of the Flatirons); gentle ground rolls. The shape from the notes (hRaw) is the same. */\n    /* hard layers stand out as cliff bands over soft ones; a band breaks off in places; the soft bumps step aside on rock */\n    const L = layerAt(x, y, hr), li = Math.floor(L), f = L - li, hard = 0.2 + 0.8 * sstep(0.55, 0.7, hash(li + 77, 31) * 0.6 + vn(x * 0.035 + li * 1.7, y * 0.035 - li * 0.9) * 0.7),\n      kt = sstep(0.5, 1.25, s) * sstep(0.2, 0.45, fbm(across * 0.07 + li * 3.7, along * 0.05 + 5, 3)),\n      ter = (sstep(0.68, 0.9, f) - f + 0.29) * LP * 0.95 * kt * hard;\n    return hr + gul * (1 - 0.5 * kt) + ter + (fbm(x * 0.08 + 3, y * 0.08 + 7, 4) - 0.5) * 1.1 * (1 - 0.8 * kt) + (fbm(x * 0.35, y * 0.35, 3) - 0.5) * 0.3 * (1 - 0.6 * kt); }\n  const MX = 2 * VX - 1, MY = 2 * VY - 1, CK = landKey(D), CH = CACHE.get(CK) || {};"
],
[
"  const ncv = PL ? null : (CH.ncv || document.createElement('canvas')); if (ncv && !CH.ncv) { ncv.width = TW; ncv.height = TH; }\n  function cell(x, y) { const i = Math.floor(x), j = Math.floor(y); let f1 = 9, f2 = 9, id = 0;\n    for (let a = -1; a <= 1; a++) for (let b = -1; b <= 1; b++) { const ci = i + a, cj = j + b, dx = ci + hash(ci, cj) - x, dy = cj + hash(cj + 71, ci + 13) - y, d = dx * dx + dy * dy;\n      if (d < f1) { f2 = f1; f1 = d; id = hash(ci + 5, cj + 3); } else if (d < f2) f2 = d; }\n    return [Math.sqrt(f1), Math.sqrt(f2), id]; }\n  /* how much of the sky each spot sees: 8 directions out to ~24 map units, on every other grid point */",
"  const ncv = PL ? null : (CH.ncv || document.createElement('canvas')); if (ncv && !CH.ncv) { ncv.width = TW; ncv.height = TH; }\n  /* how much of the sky each spot sees: 8 directions out to ~24 map units, on every other grid point */"
],
[
"          const ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);\n          const sb = h * 1.25 + x * 0.05 - y * 0.025 + (fbm(x * 0.045, y * 0.045, 3) - 0.5) * 5, lay = Math.floor(sb), band = sb - lay, lh = hash(lay + 300, 17);\n          const rc = lh < 0.42 ? mix(BUFF, GRAY, hash(lay + 9, 4) * 0.5) : lh < 0.75 ? mix(SALM, BUFF, hash(lay + 2, 8) * 0.6) : mix(GRAY, SALM, hash(lay + 5, 1) * 0.4);",
"          const ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);\n          const Lg = layerAt(x, y, hRaw(x, y)), sb = Lg * 3, lay = Math.floor(Lg), band = sb - Math.floor(sb), lh = hash(lay + 300, 17), riser = sstep(0.45, 0.6, Lg - lay) * (1 - sstep(0.9, 0.97, Lg - lay));\n          const rc = lh < 0.42 ? mix(BUFF, GRAY, hash(lay + 9, 4) * 0.5) : lh < 0.75 ? mix(SALM, BUFF, hash(lay + 2, 8) * 0.6) : mix(GRAY, SALM, hash(lay + 5, 1) * 0.4);"
],
[
"          const rough = fbm(x * 2.2, y * 2.2, 3) - 0.5;\n          rock = mix(mix(rc, LICH, lich), VARN, Math.max(streak, crack * 0.6, joint * 0.45, under * 0.35)).map(v => v * (1 + rough * 0.4) * (1 + lip * 0.08));\n          dR = -0.32 * under + 0.08 * lip - 0.45 * crack - 0.25 * joint + 0.36 * rough;",
"          const rough = fbm(x * 2.2, y * 2.2, 3) - 0.5;\n          rock = mix(mix(rc, LICH, lich), VARN, Math.max(streak, crack * 0.6, joint * 0.45, under * 0.35, riser * 0.22)).map(v => v * (1 + rough * 0.4) * (1 + lip * 0.08));\n          dR = -0.32 * under + 0.08 * lip - 0.45 * crack - 0.25 * joint + 0.36 * rough;"
]
]
patch(R, PAIRS)
patch(G, [('t && (t.textContent = "v253");', 't && (t.textContent = "v254");')])
