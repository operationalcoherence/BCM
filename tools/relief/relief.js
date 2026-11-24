/* Pattern Synthesis relief model (approved 12 Nov 2026). Bundled with three.js into gsm-relief.js,
   loaded only when the Pattern Synthesis map mounts. window.gsmRelief.mount(el, D) -> {hl(i), dispose()} */
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

const CSS = `
.grel{position:relative;width:100%;background:#fff;border:1px solid #e4e4e4;overflow:hidden;touch-action:none}
.grel canvas{display:block}
.grel .lbs{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.grel .lb{position:absolute;left:0;top:0;white-space:nowrap}
.grel .ldr{position:absolute;left:0;top:0;height:1px;background:rgba(20,20,20,.75);box-shadow:0 0 0 1px rgba(255,255,255,.55);transform-origin:0 50%;pointer-events:none;display:none}
.grel .nl{font:bold 12.5px Helvetica,Arial,sans-serif;color:#111;text-shadow:0 0 3px #fff,0 0 3px #fff,0 0 3px #fff}
.grel .lb.on,.grel .lb:hover,.grel .lb.tfoc{filter:none!important}.grel .lb.tfoc{background:#fff;border-radius:5px;padding:1px 4px;box-shadow:0 0 0 2px #fff,0 0 12px 4px rgba(255,255,255,.95);z-index:5}
.grel .tourbar .tpn{font:14px Questrial,Helvetica,Arial,sans-serif;padding:8px 14px;border-radius:20px;background:#fff;border:1px solid #222;display:none}
.grel .ql{font:bold 12px Helvetica,Arial,sans-serif;background:#111;color:#fff;padding:2px 5px}
.grel .pl{font:bold 13px Helvetica,Arial,sans-serif;letter-spacing:.1em;color:#111;text-shadow:0 0 3px #fff,0 0 3px #fff,0 0 4px #fff}
.grel .side{font:bold 17.5px Helvetica,Arial,sans-serif;letter-spacing:.14em;color:#1f6f66;text-shadow:0 0 3px #fff,0 0 3px #fff}.grel .side.hd{color:#8a2a22}.grel .side.ax{color:#333}.grel .lb.hit{pointer-events:auto;cursor:pointer}.grel .tip{position:absolute;display:none;z-index:4;max-width:340px;max-height:60%;overflow:auto;background:#222;color:#fff;font:13px/1.45 Questrial,Helvetica,Arial,sans-serif;padding:8px 10px;border-radius:2px;box-shadow:0 2px 8px rgba(0,0,0,.3)}.grel .tip b{display:block;margin-bottom:3px}.grel .tip .sm{opacity:.75;font-size:12px;margin-top:4px}
.grel .rdm{font:bold 12px Helvetica,Arial,sans-serif;color:#fff;background:#111;width:22px;height:22px;line-height:20px;text-align:center;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.4)}
.grel .rdm.on{background:#7a1d12;transform:scale(1.25)}
.grel .wn{font:bold 11px Helvetica,Arial,sans-serif;min-width:18px;height:18px;line-height:15px;padding:0 3px;text-align:center;border-radius:9px;border:1.5px solid #fff;box-shadow:0 1px 2px rgba(0,0,0,.45)}.grel .wl{font:bold 14px Helvetica,Arial,sans-serif;width:26px;height:26px;line-height:22px;text-align:center;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.45)}.grel .bt{position:absolute;top:8px;background:#fff;border:1px solid #222;font:12px Questrial,Helvetica,Arial,sans-serif;padding:4px 9px;cursor:pointer;z-index:3}
.grel.fs{position:fixed;inset:0;z-index:2147483000;border:0}.grel .grfs{display:none!important}.grel.fs .grfs,.grel.cfs .grfs{display:block!important}.grel .fsleg{position:absolute;top:0;bottom:0;left:0;width:min(340px,86vw);background:rgba(255,255,255,.82);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border-right:1px solid #ddd;padding:52px 14px 14px;overflow:auto;z-index:4;transform:translateX(0);transition:transform .2s}.grel .fsleg.shut{transform:translateX(-100%)}.grel .fsleg .grleg{margin:0}.grel .fslb{position:absolute;top:8px;left:8px;z-index:5;background:#fff;border:1px solid #222;font:12px Questrial,Helvetica,Arial,sans-serif;padding:4px 9px;cursor:pointer}.grel .brand{position:absolute;top:auto;left:auto;width:auto;height:auto;pointer-events:none;right:12px;bottom:10px;z-index:3;font:12px Questrial,Helvetica,Arial,sans-serif;letter-spacing:.12em;color:#333;background:rgba(255,255,255,.75);padding:3px 8px}.grel .brand b{font-weight:700}
.grel .tourcap{position:absolute;left:12px;right:12px;top:48px;z-index:3;max-width:640px;background:rgba(255,255,255,.96);border:1px solid #222;box-shadow:0 2px 10px rgba(0,0,0,.25);padding:12px 16px 12px;font:17px/1.5 Questrial,Helvetica,Arial,sans-serif;color:#111;display:none;pointer-events:none}.grel .tourcap .ta{font-size:12.5px;letter-spacing:.14em;font-weight:700;color:#555}.grel .tourcap .tm{font-size:15px;line-height:1.45;color:#333;margin:4px 0 8px;padding:0 0 8px;border-bottom:1px solid #ddd}.grel .tourcap .tt{font-weight:700;font-size:20px;line-height:1.3;margin:3px 0 4px}.grel .tourcap .tp{height:4px;background:#e4e1d8;margin-top:10px}.grel .fslay{position:absolute;top:46px;z-index:4;margin:0!important;padding:8px 10px;background:rgba(255,255,255,.88);border:1px solid #ccc;display:flex;flex-wrap:wrap;gap:6px;align-items:center}.grel .fslay .lhelp{display:none}.grel.touring .fslay{display:none!important}.grel .tourbar{position:absolute;bottom:44px;left:50%;transform:translateX(-50%);z-index:4;display:flex;gap:10px;align-items:center}.grel .tourbar .bt{position:static}.grel .tourbar .tpb{font:bold 17px Questrial,Helvetica,Arial,sans-serif;padding:11px 24px 11px 20px;background:#111;color:#fff;border:2px solid #fff;border-radius:28px;box-shadow:0 2px 10px rgba(0,0,0,.35);letter-spacing:.02em}.grel .tourbar .tpb::before{content:'\\25B6';display:inline-block;margin-right:10px;font-size:14px}.grel .tourbar .tpb[data-st=pause]::before{content:'\\275A\\275A';font-size:12px;letter-spacing:-2px}.grel .tourbar .tpb:hover{background:#7a1d12}.grel .tourbar .tpe{font:14px Questrial,Helvetica,Arial,sans-serif;padding:8px 14px;border-radius:20px;background:#fff;border:1px solid #222;display:none}.grel .tourcap .tp i{display:block;height:3px;background:#111;width:0}
.grel .walkbar{display:flex;gap:8px;align-items:center;margin-top:9px}
.grel .walkbar .bt{position:static;font:14px Questrial,Helvetica,Arial,sans-serif;padding:7px 14px;border-radius:18px;background:#fff;border:1px solid #222}
.grel .walkbar .bt.wnx{background:#111;color:#fff;border-color:#fff;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,.3)}
.grel .walkbar .bt:disabled{opacity:.35;cursor:default}
.grel .bt.wgo{font-weight:700;background:#111;color:#fff;border-color:#111}
.grel.walking .tourcap{display:block!important;pointer-events:auto;z-index:6;top:44px;max-width:min(620px,calc(100% - 24px));font-size:15px;padding:9px 13px}
.grel.walking .tourcap .tt{font-size:17px}
.grel.walking .tourcap .tx{font-size:14px;line-height:1.4;color:#333;max-height:4.3em;overflow:hidden}
.grel .tourcap .wk{display:flex;flex-wrap:wrap;gap:3px 2px;margin-top:8px;padding-top:7px;border-top:1px solid #ddd;font:12px/1.2 Helvetica,Arial,sans-serif}
.grel .tourcap .wk span{cursor:pointer;padding:2px 5px;border-radius:9px;border:1px solid #bbb;color:#888;background:#fff;white-space:nowrap}
.grel .tourcap .wk span.dn{color:#111;border-color:#111}
.grel .tourcap .wk span.at{color:#111;background:#f2b400;border-color:#111;font-weight:700}
.grel .tourcap .wk span.fr{color:#fff;background:#111;border-color:#111;font-weight:700}
.grel .tourcap .wk i{color:#999;font-style:normal;padding:2px 0}
.grbrand{text-align:right;margin:5px 2px 0;font:12px Questrial,Helvetica,Arial,sans-serif;letter-spacing:.12em;color:#333}.grbrand b{font-weight:700}
.grel .attr{position:absolute;left:6px;bottom:4px;z-index:3;font:10px Helvetica,Arial,sans-serif;color:#333;background:rgba(255,255,255,.75);padding:1px 6px;pointer-events:none}.grel .busy{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#888;font:13px Questrial,Helvetica,Arial,sans-serif}
.grleg{margin:8px 0 2px;font-size:12.5px;line-height:1.45;color:#333}
.grleg .r{display:flex;gap:8px;align-items:flex-start;margin:3px 0}
.grleg i{flex:0 0 26px;height:12px;border-radius:2px;margin-top:2px;border:1px solid #ccc}
.grleg b{letter-spacing:.12em;font-size:11px;display:block;margin:6px 0 2px}
.grleg .grlf>summary{cursor:pointer;font-size:12.5px;color:#666;text-decoration:underline;margin:2px 0}`;

/* ---------- small helpers ---------- */
function hash(x, y) { let h = x * 374761393 + y * 668265263; h = (h ^ (h >>> 13)) * 1274126177; return ((h ^ (h >>> 16)) >>> 0) / 4294967295; }
function vn(x, y) { const i = Math.floor(x), j = Math.floor(y), u = x - i, v = y - j, su = u * u * (3 - 2 * u), sv = v * v * (3 - 2 * v);
  const a = hash(i, j), b = hash(i + 1, j), c = hash(i, j + 1), d = hash(i + 1, j + 1); return a + (b - a) * su + (c - a) * sv + (a - b - c + d) * su * sv; }
function fbm(x, y, o = 5) { let s = 0, a = 0.5, f = 1; for (let k = 0; k < o; k++) { s += a * vn(x * f, y * f); f *= 2.03; a *= 0.5; } return s; }
function ridged(x, y, o = 4) { let s = 0, a = 0.5, f = 1; for (let k = 0; k < o; k++) { const n = 1 - Math.abs(vn(x * f, y * f) * 2 - 1); s += a * n * n; f *= 2.1; a *= 0.5; } return s; }
const sstep = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const mix = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
function vivid(c, deep) { let [r, g, b] = c.map(v => v / 255); const mx = Math.max(r, g, b), mn = Math.min(r, g, b); let l = (mx + mn) / 2, sa = 0, h = 0, d = mx - mn;
  if (d > 1e-6) { sa = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn); h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6; }
  sa = Math.min(1, sa * 1.5 + 0.08); l = deep ? Math.min(0.36, Math.max(0.24, l)) : Math.min(0.62, Math.max(0.42, l));
  const q = l < 0.5 ? l * (1 + sa) : l + sa - l * sa, p = 2 * l - q, f = t => { t = (t + 1) % 1; return t < 1 / 6 ? p + (q - p) * 6 * t : t < 0.5 ? q : t < 2 / 3 ? p + (q - p) * (2 / 3 - t) * 6 : p; };
  return [f(h + 1 / 3) * 255, f(h) * 255, f(h - 1 / 3) * 255]; }

const CACHE = new Map();
function landKey(D) { let s = 0; for (let q = 0; q < D.hn.length; q += 97) s += D.hn[q] * (q + 1); return D.VX + ',' + D.VY + ',' + D.notes.length + ',' + s.toFixed(4) + ',' + D.notes.map(n => n.k + ':' + n.e + ':' + Math.round(n.x) + ':' + Math.round(n.y)).join(';'); }
function mount(host, D) {
  if (!document.getElementById('gsm-relcss')) { const s = document.createElement('style'); s.id = 'gsm-relcss'; s.textContent = CSS; document.head.appendChild(s); }
  const VX = D.VX, VY = D.VY, CX = D.CX, CY = D.CY, W = (VX - 1) * CX, H = (VY - 1) * CY, HS = 58, ALPHA = 0.6, PL = D.place || null;
  const wrap = document.createElement('div'); wrap.className = 'grel pnet'; host.appendChild(wrap);
  const lbs = document.createElement('div'); lbs.className = 'lbs'; wrap.appendChild(lbs);
  const attr = document.createElement('div'); attr.className = 'attr'; attr.style.display = 'none'; attr.textContent = 'Imagery © Esri, Maxar, Earthstar Geographics, and the GIS User Community · Powered by Esri'; wrap.appendChild(attr);
  const busy = document.createElement('div'); busy.className = 'busy'; busy.textContent = 'Building the land…'; wrap.appendChild(busy);
  const foot = document.createElement('div'); foot.className = 'grbrand'; foot.innerHTML = '<b>THE BEAR CANYON METHOD</b> · BY OPERATIONAL COHERENCE'; host.appendChild(foot);
  const leg = document.createElement('div'); leg.className = 'grleg'; host.appendChild(leg);

  /* ---------- heights ---------- */
  function bil(arr, x, y) { const fx = Math.max(0, Math.min(VX - 1.001, x / CX)), fy = Math.max(0, Math.min(VY - 1.001, y / CY)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
    const g = (ii, jj) => arr[jj * VX + ii]; return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; }
  const hRaw = (x, y) => bil(D.hn, x, y) * HS;
  /* a place: the ground is the real terrain (meters per map unit), heights x VEX so benches and slopes show (v242); emotion shows only as color */
  const MPU = PL ? 156543.03392 * Math.cos(Math.atan(Math.sinh(Math.PI * (1 - 2 * (PL.Y0 + H / 2 / PL.k) / 256)))) / PL.k : 1;
  /* v242: up to 2.5x, never below true scale; v243: capped at ~140 units of rise (was 70) */
  const VRG = PL && PL.elev && PL.elev.hi > PL.elev.lo ? (PL.elev.hi - PL.elev.lo) / MPU : 0, VEX = VRG ? Math.max(1, Math.min(2.5, 140 / VRG)) : 2.5, VXT = VEX > 1.05 ? 'with heights exaggerated ' + (Math.round(VEX * 10) / 10) + '× so its slopes and benches show' : 'true to scale';
  function cell(x, y) { const i = Math.floor(x), j = Math.floor(y); let f1 = 9, f2 = 9, id = 0;
    for (let a = -1; a <= 1; a++) for (let b = -1; b <= 1; b++) { const ci = i + a, cj = j + b, dx = ci + hash(ci, cj) - x, dy = cj + hash(cj + 71, ci + 13) - y, d = dx * dx + dy * dy;
      if (d < f1) { f2 = f1; f1 = d; id = hash(ci + 5, cj + 3); } else if (d < f2) f2 = d; }
    return [Math.sqrt(f1), Math.sqrt(f2), id]; }
  /* v254: the rock's bedding, one coordinate shared by the ledges and the rock's color: a layer every LP units of height,
     with a slight dip and a slow wander */
  const LP = 6, layerAt = (x, y, hr) => { const L = hr / LP + x * 0.025 - y * 0.012 + (fbm(x * 0.05 + 11, y * 0.05, 3) - 0.5) * 1.8; return L + 0.3 * Math.sin(L * 2.1 + 1.3) + 0.12 * Math.sin(L * 4.7); };
  function hAt(x, y) { if (PL) return PL.elev ? PL.elev(x, y) / MPU * VEX : 0; const e = 0.6, gx = (hRaw(x + e, y) - hRaw(x - e, y)) / (2 * e), gy = (hRaw(x, y + e) - hRaw(x, y - e)) / (2 * e), s = Math.hypot(gx, gy);
    const k = sstep(0.25, 1.1, s), ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);
    const gul = (ridged(across * 0.18 + vn(x * 0.04, y * 0.04) * 2, along * 0.025, 3) - 0.4) * 1.6 * k, hr = hRaw(x, y);
    /* v254: the surface detail reads as rock, not coral: steep ground steps down in ledges of bedded rock that follow the
       slope (the layers of the Flatirons); gentle ground rolls. The shape from the notes (hRaw) is the same. */
    /* hard layers stand out as cliff bands over soft ones; a band breaks off in places; the soft bumps step aside on rock */
    const L = layerAt(x, y, hr), li = Math.floor(L), f = L - li, hard = 0.2 + 0.8 * sstep(0.55, 0.7, hash(li + 77, 31) * 0.6 + vn(x * 0.035 + li * 1.7, y * 0.035 - li * 0.9) * 0.7),
      kt = sstep(0.5, 1.25, s) * sstep(0.2, 0.45, fbm(across * 0.07 + li * 3.7, along * 0.05 + 5, 3)),
      ter = (sstep(0.68, 0.9, f) - f + 0.29) * LP * 0.95 * kt * hard;
    return hr + gul * (1 - 0.5 * kt) + ter + (fbm(x * 0.08 + 3, y * 0.08 + 7, 4) - 0.5) * 1.1 * (1 - 0.8 * kt) + (fbm(x * 0.35, y * 0.35, 3) - 0.5) * 0.3 * (1 - 0.6 * kt); }
  const RS = PL ? 2 : 3, MX = RS * (VX - 1) + 1, MY = RS * (VY - 1) + 1, CK = landKey(D), CH = CACHE.get(CK) || {};
  const hGrid = CH.hGrid || new Float32Array(MX * MY); let hMin = 1e9;
  if (!CH.hGrid) for (let j = 0; j < MY; j++) for (let i = 0; i < MX; i++) { const h = hAt(i / (MX - 1) * W, j / (MY - 1) * H); hGrid[j * MX + i] = h; }
  for (let q = 0; q < hGrid.length; q++) if (hGrid[q] < hMin) hMin = hGrid[q];
  CH.hGrid = hGrid; CACHE.set(CK, CH);
  const BASE = hMin - 7;
  function gH(x, y) { const fx = Math.max(0, Math.min(MX - 1.001, x / W * (MX - 1))), fy = Math.max(0, Math.min(MY - 1.001, y / H * (MY - 1))), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
    const g = (a, b) => hGrid[b * MX + a]; return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; }

  /* ---------- emotion field from the notes; rock face where distant emotions meet ---------- */
  const K = D.emo.length;
  const RANK = D.emo.map(e => /accept/i.test(e[0]) ? 0 : /indiff/i.test(e[0]) ? 1 : /distrust/i.test(e[0]) ? 2 : /aggress/i.test(e[0]) ? 3 : 4);
  const DEF = RANK.indexOf(4), EN = D.notes.filter(n => n.e != null), EMOC = D.emo.map((e, k) => vivid(e[1], k === DEF));
  /* indifference reads as one band: its notes are joined (shortest links first, none longer than 95), and the yellow
     runs along each join at full strength, through other emotions' ground. Color only; line maps only. */
  const IND = RANK.indexOf(1), RIB = [];
  if (IND >= 0 && !PL) { const P = EN.filter(n => n.e === IND), par = P.map((_, i) => i), top = i => par[i] === i ? i : (par[i] = top(par[i])), E = [];
    for (let i = 0; i < P.length; i++) for (let j = i + 1; j < P.length; j++) E.push([Math.hypot(P[i].x - P[j].x, P[i].y - P[j].y), i, j]);
    E.sort((a, b) => a[0] - b[0]).forEach(([d, i, j]) => { if (d > 95 || top(i) === top(j)) return; par[top(i)] = top(j); RIB.push([P[i].x, P[i].y, P[j].x, P[j].y]); }); }
  const ribAt = (x, y) => { let w = 0; RIB.forEach(([ax, ay, bx, by]) => { const dx = bx - ax, dy = by - ay, t = Math.max(0, Math.min(1, ((x - ax) * dx + (y - ay) * dy) / (dx * dx + dy * dy || 1))), d2 = (ax + t * dx - x) ** 2 + (ay + t * dy - y) ** 2; w += 2.4 * Math.exp(-d2 / (2 * 8 * 8)); }); return w; };
  const EF = { w: 150 }; EF.h = Math.round(EF.w * H / W); EF.a = new Float32Array(EF.w * EF.h * (K + 3));
  for (let j = 0; j < EF.h; j++) for (let i = 0; i < EF.w; i++) {
    const x = i / (EF.w - 1) * W, y = j / (EF.h - 1) * H, ws = new Float32Array(K), o = (j * EF.w + i) * (K + 3);
    EN.forEach(n => { ws[n.e] += Math.exp(-((n.x - x) ** 2 + (n.y - y) ** 2) / (2 * 26 * 26)); }); if (RIB.length) ws[IND] += ribAt(x, y);
    let tot = 0, p = 0; for (let k = 0; k < K; k++) { const v = (ws[k] * (k === DEF ? 1.6 : 1)) ** 2.2; EF.a[o + k] = v; p += v; tot += ws[k]; }
    for (let k = 0; k < K; k++) EF.a[o + k] /= (p || 1);
    EF.a[o + K] = sstep(0.04, 0.5, tot); EF.a[o + K + 2] = RIB.length ? sstep(0.9, 2.0, ribAt(x, y)) : 0;
    const ord = [...ws.keys()].sort((u, v) => ws[v] - ws[u]), k1 = ord[0], k2 = ord[1], s1 = ws[k1], s2 = ws[k2];
    EF.a[o + K + 1] = (Math.abs(RANK[k1] - RANK[k2]) < 2 || RANK[k1] === 1 || RANK[k2] === 1 || s2 < 0.03) ? 0 : sstep(0.22, 0.42, s2 / (s1 + s2));
    /* v252: every note keeps its own color at its own spot, however many notes of other emotions are near */
    let kO = -1, wO = 0; EN.forEach(n => { const w = Math.exp(-((n.x - x) ** 2 + (n.y - y) ** 2) / (2 * 8 * 8)); if (w > wO) { wO = w; kO = n.e; } });
    if (kO >= 0) { const pw = sstep(0.25, 0.7, wO) * (1 - EF.a[o + kO]);
      if (pw > 0.001) { for (let k = 0; k < K; k++) EF.a[o + k] = EF.a[o + k] * (1 - pw) + (k === kO ? pw : 0);
        EF.a[o + K + 1] *= 1 - pw; if (kO !== IND) EF.a[o + K + 2] *= 1 - pw; EF.a[o + K] = Math.max(EF.a[o + K], pw); } }
  }
  function emoMix(x, y) { const fx = Math.min(EF.w - 1.001, x / W * (EF.w - 1)), fy = Math.min(EF.h - 1.001, y / H * (EF.h - 1)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
    const g = (ii, jj, k) => EF.a[(jj * EF.w + ii) * (K + 3) + k], b = k => g(i, j, k) * (1 - u) * (1 - v) + g(i + 1, j, k) * u * (1 - v) + g(i, j + 1, k) * (1 - u) * v + g(i + 1, j + 1, k) * u * v;
    let c = [0, 0, 0]; for (let k = 0; k < K; k++) { const w = b(k); c = [c[0] + EMOC[k][0] * w, c[1] + EMOC[k][1] * w, c[2] + EMOC[k][2] * w]; } return [c, b(K), b(K + 1), b(K + 2)]; }

  /* ---------- ground texture: grass, soil, rock by slope; emotion hue at 60% ---------- */
  /* v253 (his photos of Bear Canyon, 11-24): quality and realism only. On line maps the rock gets sandstone bedding,
     joints, lichen and dark streaks; the soil gets its red and its stones; the grass gets dry tufts and low shrubs; a fine
     relief map carries that detail into the light; the land's own horizon gives the shading in hollows and under rock.
     Heights, where rock sits, how far it reaches, and every color's meaning are unchanged. A place keeps its imagery. */
  const TW = PL ? 2560 : 1600, TH = Math.round(TW * H / W), tcv = CH.tcv || document.createElement('canvas'); if (!CH.tcv) { tcv.width = TW; tcv.height = TH; }
  const ncv = PL ? null : (CH.ncv || document.createElement('canvas')); if (ncv && !CH.ncv) { ncv.width = TW; ncv.height = TH; }
  const mcv = PL ? null : (CH.mcv || document.createElement('canvas')); if (mcv && !CH.mcv) { mcv.width = TW; mcv.height = TH; }
  /* how much of the sky each spot sees: 8 directions out to ~24 map units, on every other grid point */
  const AOS = RS, AOW = Math.floor((MX - 1) / AOS) + 1, AOH = Math.floor((MY - 1) / AOS) + 1, HAO = CH.hao || new Float32Array(AOW * AOH);
  if (!PL && !CH.hao) for (let j = 0; j < AOH; j++) for (let i = 0; i < AOW; i++) {
    const x = Math.min(W, i * AOS / (MX - 1) * W), y = Math.min(H, j * AOS / (MY - 1) * H), h0 = gH(x, y); let occ = 0;
    for (let k = 0; k < 8; k++) { const a = k * Math.PI / 4 + 0.3, dx = Math.cos(a), dy = Math.sin(a); let t = 0;
      for (const r of [1.5, 3, 5, 8, 12, 17, 24]) { const xx = x + dx * r, yy = y + dy * r; if (xx < 0 || yy < 0 || xx > W || yy > H) break; t = Math.max(t, (gH(xx, yy) - h0) / r); }
      occ += t / Math.sqrt(1 + t * t); }
    HAO[j * AOW + i] = occ / 8; }
  if (!PL) CH.hao = HAO;
  const aoAt = (x, y) => { const fx = Math.max(0, Math.min(AOW - 1.001, x / W * (MX - 1) / AOS)), fy = Math.max(0, Math.min(AOH - 1.001, y / H * (MY - 1) / AOS)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j, g = (a, b) => HAO[b * AOW + a];
    return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; };
  function paint(base) {
    const ctx = tcv.getContext('2d'), img = ctx.createImageData(TW, TH), px = img.data, bp = base && base.data, DT = ncv ? new Float32Array(TW * TH) : null, RW = ncv ? new Uint8Array(TW * TH) : null;
    const GR = [98, 108, 62], GR2 = [140, 134, 86], SO = [124, 96, 66], SO2 = [86, 68, 50], RK = [122, 118, 112], RK2 = [168, 160, 148], lum = q => 0.3 * q[0] + 0.59 * q[1] + 0.11 * q[2];
    /* v253 palette, read from his photos; the means stay near the old ones so the legend's swatches still hold */
    const BUFF = [184, 170, 150], SALM = [176, 144, 126], GRAY = [150, 146, 140], LICH = [158, 156, 108], VARN = [104, 96, 88],
      DRY = [150, 138, 94], GRN = [100, 112, 64], SHRB = [66, 80, 50], RED = [142, 98, 70], RED2 = [100, 74, 56], STN = [170, 156, 138];
    for (let py = 0; py < TH; py++) for (let pxx = 0; pxx < TW; pxx++) {
      const x = pxx / (TW - 1) * W, y = py / (TH - 1) * H, e = W / TW * 1.5;
      const h = gH(x, y), gx = (gH(x + e, y) - gH(x - e, y)) / (2 * e), gy = (gH(x, y + e) - gH(x, y - e)) / (2 * e), s = Math.hypot(gx, gy);
      const lap = gH(x + 3 * e, y) + gH(x - 3 * e, y) + gH(x, y + 3 * e) + gH(x, y - 3 * e) - 4 * h;
      const n1 = fbm(x * 0.08, y * 0.08, 4), n2 = vn(x * 1.7, y * 1.7), sp = hash(pxx, py);
      const fg = fbm(x * 0.05 + 9, y * 0.05, 4), tR = sstep(0.55, 1.15, s + (n1 - 0.5) * 0.5), tS = sstep(0.25, 0.55, s + (n1 - 0.5) * 0.6) * (1 - tR);
      let [em, st, gap, rb] = emoMix(x, y); if (PL) gap = 0;
      let grass, soil, rock, dR = 0, dG = 0;
      if (PL) { grass = mix(GR, GR2, sstep(0.35, 0.75, fg)); soil = mix(SO, SO2, sstep(-0.2, -0.9, h / HS) * 0.8); rock = mix(RK, RK2, n2 * 0.7).map(v => v * (0.92 + 0.08 * vn(x * 0.6, y * 0.6))); }
      else {
        /* each material is worked out only where it shows */
        const rw = Math.max(tR, gap), sw = Math.min(1, tS + sstep(-0.4, -1.0, h / HS) * 0.5 * (1 - tR));
        rock = soil = grass = [0, 0, 0];
        if (rw > 0.003) {
          /* sandstone: layers that follow the contours with a slight dip, each its own tone; a lip on top, an undercut below */
          const ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);
          const Lg = layerAt(x, y, hRaw(x, y)), sb = Lg * 3, lay = Math.floor(Lg), band = sb - Math.floor(sb), lh = hash(lay + 300, 17), riser = sstep(0.45, 0.6, Lg - lay) * (1 - sstep(0.9, 0.97, Lg - lay));
          const rc = lh < 0.42 ? mix(BUFF, GRAY, hash(lay + 9, 4) * 0.5) : lh < 0.75 ? mix(SALM, BUFF, hash(lay + 2, 8) * 0.6) : mix(GRAY, SALM, hash(lay + 5, 1) * 0.4);
          const under = sstep(0.78, 0.98, band), lip = 1 - sstep(0, 0.07, band);
          /* joints: blocks broken along cracks, and thin joints across the bedding */
          const [f1, f2] = cell(across * 0.42 + sb * 0.35, sb * 0.9 + across * 0.05), crack = 1 - sstep(0.015, 0.09, f2 - f1);
          const joint = (1 - sstep(0.0, 0.06, Math.abs(Math.sin(across * 0.55 + (vn(x * 0.2, y * 0.2) - 0.5) * 4)))) * sstep(0.55, 0.75, hash(lay + 40, 2));
          const lich = sstep(0.62, 0.72, fbm(x * 0.22 + 40, y * 0.22, 3)) * (1 - crack) * 0.4, streak = sstep(0.62, 0.82, vn(across * 1.1, along * 0.07 + lay * 0.3)) * 0.3;
          const rough = fbm(x * 2.2, y * 2.2, 3) - 0.5;
          rock = mix(mix(rc, LICH, lich), VARN, Math.max(streak, crack * 0.2, joint * 0.15, under * 0.2, riser * 0.22)).map(v => v * (1 + rough * 0.1) * (1 + lip * 0.04));
          dR = (-0.32 * under + 0.08 * lip - 0.45 * crack - 0.25 * joint + 0.36 * rough) * 0.3;
        }
        /* soil: red decomposed granite with stones; grass: dry grass with green patches */
        if (sw > 0.003 && tR < 0.997) { const [p1, , pid] = cell(x * 1.6, y * 1.6), stone = sstep(0.3, 0.16, p1) * sstep(0.62, 0.75, pid);
          soil = mix(mix(RED, RED2, sstep(-0.2, -0.9, h / HS) * 0.8 + (vn(x * 0.3, y * 0.3) - 0.5) * 0.5), STN.map(v => v * (0.8 + 0.25 * pid)), stone * 0.55); dG += 0.1 * stone * sw; }
        if (sw < 0.997 && tR < 0.997) { const tuft = vn(x * 6.5, y * 6.5) * 0.65 + vn(x * 13.1, y * 13.1) * 0.35, patch = fbm(x * 0.6 + 7, y * 0.6 - 3, 2);
          grass = mix(mix(GRN, DRY, sstep(0.3, 0.7, fg)), SHRB, sstep(0.55, 0.85, patch) * 0.3).map(v => v * (0.94 + 0.12 * tuft)); dG += (0.06 * (tuft - 0.5) + 0.08 * (patch - 0.5)) * (1 - sw); }
      }
      const o0 = (py * TW + pxx) * 4;
      let c = bp ? [bp[o0], bp[o0 + 1], bp[o0 + 2]] : mix(mix(grass, soil, tS + sstep(-0.4, -1.0, h / HS) * 0.5 * (1 - tR)), rock, tR); const kk = bp ? 1 : PL ? 0.93 + 0.14 * sp : 0.96 + 0.08 * sp; c = c.map(v => v * kk);
      let ao = Math.max(-0.28, Math.min(0.18, -lap * (PL ? 0.5 : 0.11))); if (!PL) { ao = Math.max(-0.42, ao * 0.7 - aoAt(x, y) * 0.5); const l1 = gH(x + e, y) + gH(x - e, y) + gH(x, y + e) + gH(x, y - e) - 4 * h; ao += Math.min(0.1, Math.max(0, -l1 - 0.02) * 0.6) * sstep(0.15, 0.5, s); } c = c.map(v => v * (1 + ao));
      /* v243: a place gets a hillshade over its imagery (light from the northwest, 45° up) so benches and slopes read */
      if (PL) { const gx = (gH(x + e, y) - gH(x - e, y)) / (2 * e), gy = (gH(x, y + e) - gH(x, y - e)) / (2 * e), nl = Math.hypot(gx, gy, 1), sh = ((gx + gy) * 0.7071 + 1) * 0.7071 / nl / 0.7071 - 1; c = c.map(v => Math.min(255, v * (1 + Math.max(-0.45, Math.min(0.3, sh * 0.9))))); }
      if (gap > 0.01) c = mix(c, rock.map(v => v * (1 + ao)), gap * 0.85);
      const ls = lum(c), le = lum(em) || 1; c = mix(c, PL ? em : em.map(v => Math.min(255, v * ls / le * 1.05)), (PL ? 0.42 : ALPHA) * st * (1 - gap));
      if (rb > 0.01) c = mix(c, EMOC[IND].map(v => v * (0.9 + 0.1 * (1 + ao))), 0.8 * rb);
      const o = (py * TW + pxx) * 4; px[o] = c[0]; px[o + 1] = c[1]; px[o + 2] = c[2]; px[o + 3] = 255;
      if (DT) { const rw = Math.max(tR, gap); DT[py * TW + pxx] = dG * (1 - rw) + dR * rw; RW[py * TW + pxx] = rw * 255; }
    }
    ctx.putImageData(img, 0, 0);
    /* the fine relief as a normal map: the detail's slope, in the texture's own frame (u along x, v against y) */
    if (DT) { const nctx = ncv.getContext('2d'), ni = nctx.createImageData(TW, TH), nd = ni.data, k = 0.5 / (W / TW);
      for (let j = 0; j < TH; j++) for (let i = 0; i < TW; i++) { const a = DT[j * TW + Math.max(0, i - 1)], b = DT[j * TW + Math.min(TW - 1, i + 1)], c2 = DT[Math.max(0, j - 1) * TW + i], d2 = DT[Math.min(TH - 1, j + 1) * TW + i];
        let nx = -(b - a) / 2 * k, ny = (d2 - c2) / 2 * k; const l = Math.hypot(nx, ny, 1), o = (j * TW + i) * 4;
        nd[o] = (nx / l * 0.5 + 0.5) * 255; nd[o + 1] = (ny / l * 0.5 + 0.5) * 255; nd[o + 2] = (1 / l * 0.5 + 0.5) * 255; nd[o + 3] = 255; }
      nctx.putImageData(ni, 0, 0);
      const mctx = mcv.getContext('2d'), mi = mctx.createImageData(TW, TH), md = mi.data; for (let q = 0; q < RW.length; q++) { md[4 * q] = md[4 * q + 1] = md[4 * q + 2] = RW[q]; md[4 * q + 3] = 255; } mctx.putImageData(mi, 0, 0); }
  }
  if (!CH.tcv) paint(null);
  CH.tcv = tcv; if (ncv) { CH.ncv = ncv; CH.mcv = mcv; }
  /* a place: Esri imagery, roads and place names under the emotion color; areas drawn as shaded patches */
  function placeGround() {
    if (!PL) return; if (CH.placed) { attr.style.display = ''; return; }
    const span = W / PL.k; let z = Math.max(1, Math.min(18, Math.round(Math.log2(TW * 1.3 / span))));
    let a, b, c, d; const rng = () => { const n = 2 ** z; a = Math.floor(PL.X0 * n / 256); b = Math.floor((PL.X0 + span) * n / 256); c = Math.floor(PL.Y0 * n / 256); d = Math.floor((PL.Y0 + H / PL.k) * n / 256); };
    rng(); while ((b - a + 1) * (d - c + 1) > 64 && z > 1) { z--; rng(); }
    const n = 2 ** z, fx = TW / (span * n), fy = TH / (H / PL.k * n);
    const layer = (url, opq) => new Promise(res => { const cv = document.createElement('canvas'); cv.width = TW; cv.height = TH; const cx = cv.getContext('2d');
      if (opq) { cx.fillStyle = '#c9c4b8'; cx.fillRect(0, 0, TW, TH); }
      let left = (b - a + 1) * (d - c + 1), ok = 0; const done = () => { if (--left === 0) res(ok ? cv : null); };
      setTimeout(() => { left = 1; done(); }, 20000);
      for (let tx = a; tx <= b; tx++) for (let ty = c; ty <= d; ty++) { const im = new Image(); im.crossOrigin = 'anonymous';
        im.onload = () => { try { cx.drawImage(im, (tx * 256 - PL.X0 * n) * fx, (ty * 256 - PL.Y0 * n) * fy, 256 * fx + 1, 256 * fy + 1); ok++; } catch (e) {} done(); };
        im.onerror = done; im.src = url.replace('{z}', z).replace('{y}', ty).replace('{x}', tx); } });
    const E = 'https://server.arcgisonline.com/ArcGIS/rest/services/';
    Promise.all([layer(E + 'World_Imagery/MapServer/tile/{z}/{y}/{x}', 1), layer(E + 'Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}'), layer(E + 'Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}')]).then(([im, rd, nm]) => {
      if (!alive) return; let base = null; try { base = im && im.getContext('2d').getImageData(0, 0, TW, TH); } catch (e) { base = null; }
      if (base) paint(base);
      const ctx = tcv.getContext('2d'); [rd, nm].forEach(L => { if (L) try { ctx.drawImage(L, 0, 0); } catch (e) {} });
      (PL.areas || []).forEach(A => { if (!A.pts || A.pts.length < 3) return; ctx.beginPath(); A.pts.forEach((p, i) => ctx[i ? 'lineTo' : 'moveTo'](p[0] / W * TW, p[1] / H * TH)); ctx.closePath();
        const col = A.e == null ? [255, 255, 255] : EMOC[A.e]; ctx.fillStyle = `rgba(${col.map(v => v | 0).join(',')},0.5)`; ctx.fill(); ctx.lineJoin = 'round'; ctx.lineWidth = 10; ctx.strokeStyle = 'rgba(255,255,255,0.9)'; ctx.stroke(); ctx.lineWidth = 5; ctx.strokeStyle = `rgb(${col.map(v => v * 0.7 | 0).join(',')})`; ctx.stroke(); });
      if (base) { CH.placed = 1; attr.style.display = ''; } tex.needsUpdate = true; dirty = true; });
  }

  /* ---------- scene ---------- */
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = PL ? THREE.PCFShadowMap : THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.3;
  wrap.insertBefore(renderer.domElement, lbs); busy.remove();
  const scene = new THREE.Scene(); scene.background = new THREE.Color('#ffffff');
  const camera = new THREE.PerspectiveCamera(30, 1.6, 1, 5000), controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.maxPolarAngle = Math.PI * 0.47; controls.minDistance = 120; controls.maxDistance = 1400;
  /* v253: on line maps a sky that is a little blue and a ground that bounces warm, and a lower, warmer sun from the same side */
  scene.add(PL ? new THREE.HemisphereLight(0xffffff, 0x9a9384, 1.0) : new THREE.HemisphereLight(0xe2ebf5, 0x8f7c66, 0.85));
  const sun = new THREE.DirectionalLight(PL ? 0xfff6ea : 0xfff0dc, 3.3); if (PL) sun.position.set(-260, 260, -160); else sun.position.set(-290, 215, -175); sun.castShadow = true;
  sun.shadow.mapSize.set(PL ? 2048 : 4096, PL ? 2048 : 4096); sun.shadow.bias = -0.0006; sun.shadow.normalBias = 0.6;
  Object.assign(sun.shadow.camera, { left: -260, right: 260, top: 200, bottom: -200, near: 10, far: 900 }); scene.add(sun);
  const fill = new THREE.DirectionalLight(0xffffff, 0.9); fill.position.set(120, 90, 400); scene.add(fill);
  /* v255: on line maps the light also comes from the whole sky (blue above, warm ground below), as outdoors */
  if (!PL) { const sk = new THREE.Scene(), sg = new THREE.SphereGeometry(10, 32, 16), sm = new THREE.ShaderMaterial({ side: THREE.BackSide, vertexShader: 'varying vec3 d; void main(){ d = position; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
      fragmentShader: 'varying vec3 d; void main(){ float y = normalize(d).y; vec3 c = y > 0.0 ? mix(vec3(0.95, 0.93, 0.88), vec3(0.55, 0.68, 0.88), pow(y, 0.6)) : mix(vec3(0.62, 0.52, 0.42), vec3(0.32, 0.27, 0.22), -y); gl_FragColor = vec4(c * 1.4, 1.0); }' });
    sk.add(new THREE.Mesh(sg, sm)); const pm = new THREE.PMREMGenerator(renderer); scene.environment = pm.fromScene(sk, 0.02).texture; scene.environmentIntensity = 0.3; pm.dispose(); }
  const HAZE = { n: { value: 1e5 }, f: { value: 2e5 } };
  const draw = () => { if (!PL) { const d = camera.position.distanceTo(controls.target); HAZE.n.value = d * 0.9; HAZE.f.value = d * 1.5; } renderer.render(scene, camera); };
  const X = x => x - W / 2, Z = y => y - H / 2;
  const geo = new THREE.PlaneGeometry(W, H, MX - 1, MY - 1); geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position; for (let q = 0; q < MX * MY; q++) pos.setY(q, hGrid[q]); geo.computeVertexNormals();
  const tex = new THREE.CanvasTexture(tcv); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  const tmat = new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95 }); if (ncv) { const nt = new THREE.CanvasTexture(ncv); nt.anisotropy = 8; tmat.normalMap = nt; tmat.normalScale.set(1, 1); }
  /* v255: the rock's fine detail is drawn on the graphics card from each point's real position in 3D (layers by height,
     grain, cracks), so it stays sharp at any zoom and wraps cliff faces instead of stretching down them. It shows only
     where the painted ground is already rock (the mask), so where rock sits is unchanged. Finer than a pixel fades out. */
  if (mcv) { const mt = new THREE.CanvasTexture(mcv); tmat.onBeforeCompile = sh => { sh.uniforms.rockMask = { value: mt };
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nvarying vec3 vWP;').replace('#include <worldpos_vertex>', '#include <worldpos_vertex>\nvWP = (modelMatrix * vec4(transformed, 1.0)).xyz;');
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', `#include <common>
varying vec3 vWP; uniform sampler2D rockMask;
float h3(vec3 p){ p = fract(p * 0.1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }
float n3(vec3 x){ vec3 i = floor(x), f = fract(x); f = f * f * (3.0 - 2.0 * f);
  return mix(mix(mix(h3(i), h3(i + vec3(1,0,0)), f.x), mix(h3(i + vec3(0,1,0)), h3(i + vec3(1,1,0)), f.x), f.y),
             mix(mix(h3(i + vec3(0,0,1)), h3(i + vec3(1,0,1)), f.x), mix(h3(i + vec3(0,1,1)), h3(i + vec3(1,1,1)), f.x), f.y), f.z); }
float rockH(vec3 p, float fw, out float tone){
  float s = p.y * 1.7 + p.x * 0.06 + (n3(p * 0.25) - 0.5) * 2.4, lay = floor(s), b = s - lay;
  tone = h3(vec3(lay, 3.0, 7.0));
  float h = smoothstep(0.72, 0.9, b) * 0.3 * smoothstep(0.5, 0.18, fw * 1.7);
  float a = 0.55, f = 1.1;
  for (int k = 0; k < 3; k++) { h += a * (n3(p * f + float(k) * 7.1) - 0.5) * smoothstep(0.45, 0.15, fw * f); f *= 2.15; a *= 0.5; }
  return h; }
vec3 bumpN(vec3 sp, vec3 n, float h){ vec3 dx = dFdx(sp), dy = dFdy(sp), r1 = cross(dy, n), r2 = cross(n, dx); float det = dot(dx, r1);
  vec3 g = sign(det) * (dFdx(h) * r1 + dFdy(h) * r2); return normalize(abs(det) * n - g); }
float rkM; float rkH; float rkT;`)
      .replace('#include <map_fragment>', `#include <map_fragment>
rkM = texture2D(rockMask, vMapUv).r; { float fw = length(fwidth(vWP)); rkH = rockH(vWP, fw, rkT); }
diffuseColor.rgb *= mix(1.0, (0.86 + 0.28 * rkT) * (1.0 + rkH * 0.55), rkM);`)
      .replace('#include <normal_fragment_maps>', `#include <normal_fragment_maps>
normal = bumpN(-vViewPosition, normal, rkH * rkM * 0.9);`)
      /* v262: distance haze, after the ground's color is final */
      .replace('#include <fog_fragment>', `#include <fog_fragment>
{ float hz = clamp((length(vViewPosition) - hazeN) / max(1.0, hazeF - hazeN), 0.0, 1.0); gl_FragColor.rgb = mix(gl_FragColor.rgb, vec3(0.86, 0.89, 0.93), hz * 0.2); }`)
      .replace('uniform sampler2D rockMask;', 'uniform sampler2D rockMask; uniform float hazeN; uniform float hazeF;');
    sh.uniforms.hazeN = HAZE.n; sh.uniforms.hazeF = HAZE.f; }; }
  const terrain = new THREE.Mesh(geo, tmat); terrain.castShadow = terrain.receiveShadow = true; scene.add(terrain);
  // block sides
  function wallStrip(pts) { const g = new THREE.BufferGeometry(), v = [], idx = [];
    pts.forEach(p => { v.push(X(p[0]), gH(p[0], p[1]), Z(p[1]), X(p[0]), BASE, Z(p[1])); });
    for (let k = 0; k < pts.length - 1; k++) { const a = 2 * k; idx.push(a, a + 1, a + 2, a + 2, a + 1, a + 3); }
    g.setAttribute('position', new THREE.Float32BufferAttribute(v, 3)); g.setIndex(idx); g.computeVertexNormals(); return g; }
  const sideMat = new THREE.MeshStandardMaterial({ color: 0x1d1c1a, roughness: 1, side: THREE.DoubleSide }), N = 200, ed = { s: [], n: [], w: [], e: [] };
  for (let k = 0; k <= N; k++) { const t = k / N; ed.s.push([t * W, H]); ed.n.push([W - t * W, 0]); ed.w.push([0, t * H]); ed.e.push([W, H - t * H]); }
  Object.values(ed).forEach(p => { const m = new THREE.Mesh(wallStrip(p), sideMat); m.receiveShadow = true; scene.add(m); });
  /* v265: the attribution, lettered on the front face of the block, below the lowest point of its top edge */
  { let top = 1e9; ed.s.forEach(p => { top = Math.min(top, gH(p[0], p[1])); }); const room = top - BASE;
    if (room > 1.5) { const cv = document.createElement('canvas'); cv.width = 2048; cv.height = 96; const g = cv.getContext('2d');
      g.fillStyle = '#d8d4cc'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = '600 52px Helvetica, Arial, sans-serif';
      const T = 'The Bear Canyon Method by Operational Coherence'; if ('letterSpacing' in g) g.letterSpacing = '4px'; g.fillText(T, 1024, 50);
      const tw = Math.min(2040, g.measureText(T).width + 40), th = Math.min(room * 0.42, 9), pw = th * cv.width / cv.height * 0.98;
      const tt = new THREE.CanvasTexture(cv); tt.colorSpace = THREE.SRGBColorSpace; tt.anisotropy = 8;
      const sign = new THREE.Mesh(new THREE.PlaneGeometry(Math.min(pw, W * 0.9), th), new THREE.MeshBasicMaterial({ map: tt, transparent: true, opacity: 0.85, depthWrite: false }));
      if (pw > W * 0.9) sign.scale.y = W * 0.9 / pw; sign.position.set(0, BASE + room * 0.5, H / 2 + 0.25); if (th >= 4) scene.add(sign); }
    /* where the front face is too low to letter (flat or gentle ground, as on many place maps), the line lies on the base in front of it */
    if (!(room > 1.5) || Math.min(room * 0.42, 9) < 4) { const cv = document.createElement('canvas'); cv.width = 2048; cv.height = 96; const g = cv.getContext('2d');
      g.fillStyle = '#55524c'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = '600 52px Helvetica, Arial, sans-serif'; if ('letterSpacing' in g) g.letterSpacing = '4px';
      g.fillText('The Bear Canyon Method by Operational Coherence', 1024, 50); const tt = new THREE.CanvasTexture(cv); tt.colorSpace = THREE.SRGBColorSpace; tt.anisotropy = 8;
      const th = 7, pw = Math.min(th * cv.width / cv.height * 0.98, W * 0.9), mat = new THREE.MeshBasicMaterial({ map: tt, transparent: true, opacity: 0.85, depthWrite: false });
      const flat = new THREE.Mesh(new THREE.PlaneGeometry(pw, th * pw / (th * cv.width / cv.height * 0.98)), mat); flat.rotation.x = -Math.PI / 2; flat.position.set(0, BASE + 0.05, H / 2 + 8); scene.add(flat); } }

  const slab = new THREE.Mesh(new THREE.BoxGeometry(W + 30, 4, H + 30), new THREE.MeshStandardMaterial({ color: 0xeeeeec, roughness: 0.9 })); slab.position.y = BASE - 2; slab.receiveShadow = true; scene.add(slab);

  /* ---------- notes, questions, goal, things to notice ---------- */
  const L = [], blk = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.6 });
  function lab(text, cls, x, y, lift, pri, ax, ay, info) { const el = document.createElement('div'); el.className = 'lb ' + cls + (info ? ' hit' : ''); el.textContent = text; lbs.appendChild(el); const o = { el, v: new THREE.Vector3(X(x), gH(x, y) + lift, Z(y)), pri, ax: ax || 0, ay: ay || 0, info }; L.push(o);
    if (info) { el.addEventListener('mouseenter', ev => { if (!pinned) showTip(o, ev); }); el.addEventListener('mouseleave', () => { if (!pinned) hideTip(); }); el.addEventListener('click', ev => { ev.stopPropagation(); pinned = pinned === o ? null : o; pinned ? showTip(o, ev) : hideTip(); }); } return o; }
  const NOBJ = [], spokeMat = new THREE.LineBasicMaterial({ color: 0x222222, transparent: true, opacity: 0.55 });
  D.notes.forEach(n => { const h = gH(n.x, n.y);
    const st = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 10, 6), blk); st.position.set(X(n.x), h + 5, Z(n.y)); st.castShadow = true; scene.add(st);
    const hd = new THREE.Mesh(new THREE.SphereGeometry(2.8, 18, 12), new THREE.MeshStandardMaterial({ color: n.e == null ? 0xffffff : new THREE.Color(`rgb(${D.emo[n.e][1].join(',')})`), roughness: 0.5 }));
    hd.position.set(X(n.x), h + 11, Z(n.y)); hd.castShadow = true; scene.add(hd);
    const lo = lab((D.np || 'N') + n.k, 'nl', n.x, n.y, 11, 1, 6, -8, { head: (D.np || 'N') + n.k + ' · ' + (n.e == null ? 'no emotion marked' : D.emo[n.e][0].toUpperCase()) + (n.q ? ' · Q.' + n.q : ''), body: n.t || '' }); let sp = null; if (D.spokes && n.q) { const Q = (D.qpos || []).find(z => z && z.q === n.q); if (Q) { const P = []; for (let k = 0; k <= 24; k++) { const t = k / 24, x = Q.x + (n.x - Q.x) * t, y = Q.y + (n.y - Q.y) * t; P.push(new THREE.Vector3(X(x), gH(x, y) + 1.4, Z(y))); } sp = new THREE.Line(new THREE.BufferGeometry().setFromPoints(P), spokeMat); scene.add(sp); } }
    lo.head = hd.position; lo.isN = 1; NOBJ.push({ q: n.q, st, hd, lo, sp }); });
  D.qpos.forEach(Q => { if (!Q) return; const h = gH(Q.x, Q.y), st = new THREE.Mesh(new THREE.CylinderGeometry(0.55, 0.55, 18, 6), blk); st.position.set(X(Q.x), h + 9, Z(Q.y)); st.castShadow = true; scene.add(st);
    const fl = new THREE.Mesh(new THREE.BoxGeometry(7, 4.2, 0.6), blk); fl.position.set(X(Q.x) + 3.2, h + 16.4, Z(Q.y)); fl.castShadow = true; scene.add(fl); lab('Q.' + Q.q, 'ql', Q.x, Q.y, 16.4, 2, -4, -10, { head: 'Q.' + Q.q + (Q.title ? ' · ' + Q.title : ''), body: Q.ans || 'No answer written yet.', sm: Q.n ? 'Placed at the middle of its ' + Q.n + ' note' + (Q.n > 1 ? 's' : '') + '.' : 'No notes yet; placed on the line between present and goal.' }); });
  { const s = D.START, h = gH(s.x, s.y), p = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 22, 6), blk); p.position.set(X(s.x), h + 11, Z(s.y)); p.castShadow = true; scene.add(p);
    const f = new THREE.Mesh(new THREE.BoxGeometry(0.5, 7, 11), new THREE.MeshStandardMaterial({ color: 0x2e9b45, roughness: 0.55 })); f.position.set(X(s.x), h + 18.5, Z(s.y) + 5.5); f.castShadow = true; scene.add(f);
    lab(PL ? 'START' : 'PRESENT', 'pl', s.x, s.y, 24, 3, -30, -24, PL ? { head: 'START', body: 'The note farthest from the goal. The ways run from here to the goal.' } : { head: 'PRESENT', body: 'Where things stand now. The ground runs from here toward the goal.' }); }
  const ringAt = (cx, cy, r) => { const p = []; for (let k = 0; k <= 64; k++) { const a = k / 64 * Math.PI * 2, x = cx + Math.cos(a) * r, y = cy + Math.sin(a) * r; p.push(new THREE.Vector3(X(x), gH(x, y) + 0.5, Z(y))); } return p; };
  const RINGP = []; [22, 14, 6].forEach(r => { const q = ringAt(D.GOAL.x, D.GOAL.y, r); for (let k = 0; k < 64; k += (r > 10 ? 2 : 4)) RINGP.push(q[k]); });
  [22, 14, 6].forEach(r => { const c = new THREE.CatmullRomCurve3(ringAt(D.GOAL.x, D.GOAL.y, r), true); scene.add(new THREE.Mesh(new THREE.TubeGeometry(c, 80, 1.0, 6, true), new THREE.MeshStandardMaterial({ color: 0xffffff }))); scene.add(new THREE.Mesh(new THREE.TubeGeometry(c, 80, 0.5, 6, true), blk)); });
  { const g = D.GOAL, hh = gH(g.x, g.y), pole = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 16, 6), blk); pole.position.set(X(g.x), hh + 8, Z(g.y)); scene.add(pole);
    pole.scale.y = 1.5; pole.position.y = hh + 12;
    const ck = document.createElement('canvas'); ck.width = 96; ck.height = 64; { const c = ck.getContext('2d'); for (let i = 0; i < 6; i++) for (let j = 0; j < 4; j++) { c.fillStyle = (i + j) % 2 ? '#111111' : '#ffffff'; c.fillRect(i * 16, j * 16, 16, 16); } }
    const ctex = new THREE.CanvasTexture(ck); ctex.colorSpace = THREE.SRGBColorSpace; ctex.magFilter = THREE.NearestFilter;
    const st = new THREE.Mesh(new THREE.BoxGeometry(0.5, 8, 12), new THREE.MeshStandardMaterial({ map: ctex, roughness: 0.6 })); st.position.set(X(g.x), hh + 20, Z(g.y) + 6); st.castShadow = true; scene.add(st); lab('GOAL', 'pl', g.x, g.y, 25, 3, -22, -22, { head: 'GOAL', body: D.goalText || 'No goal written yet.' }); }
  if (!PL) { let nm = -1e9; for (let k = 0; k <= 60; k++) nm = Math.max(nm, gH(0, k / 60 * 20)); const o = lab('↑ HELP', 'side', 0, 2, 0, 4, -104, -10); o.v.set(X(-6), nm + 4, Z(2));
    const o2 = lab('↓ HINDER', 'side hd', 0, H - 2, 0, 4, -128, -10); o2.v.set(X(-6), (gH(0, H - 2) + BASE) / 2, Z(H));
    const o3 = lab('← PRESENT', 'side ax', 0, H, 0, 4, 0, 10); o3.v.set(X(0), BASE, Z(H) + 4);
    const o4 = lab('FUTURE →', 'side ax', W, H, 0, 4, -120, 10); o4.v.set(X(W), BASE, Z(H) + 4); }
  const RD = (D.read || []).map((r, i) => { const o = lab(String(i + 1), 'rdm', r.at[0], r.at[1], 21, 5, -11, -11, { head: (i + 1) + ' · ' + (r.title || ''), body: r.text || '', rd: i }); const h = gH(r.at[0], r.at[1]);
    const st = new THREE.Mesh(new THREE.CylinderGeometry(0.35, 0.35, 20, 6), blk); st.position.set(X(r.at[0]), h + 10, Z(r.at[1])); st.castShadow = true; scene.add(st);
    const bl = new THREE.Mesh(new THREE.SphereGeometry(2.6, 16, 12), blk); bl.position.set(X(r.at[0]), h + 21, Z(r.at[1])); bl.castShadow = true; scene.add(bl);
    const rim = new THREE.Mesh(new THREE.TorusGeometry(2.7, 0.35, 6, 24), new THREE.MeshStandardMaterial({ color: 0xffffff })); rim.position.copy(bl.position); scene.add(rim); o.rim = rim; o.head = bl.position; return o; });

  const tip = document.createElement('div'); tip.className = 'tip'; wrap.appendChild(tip); let pinned = null;
  function showTip(o, ev) { if (TOUR && TOUR.paused == null) return; tip.innerHTML = ''; const b = document.createElement('b'); b.textContent = o.info.head; tip.appendChild(b); const bd = String(o.info.body || ''); tip.appendChild(document.createTextNode(bd.length > (o.info.long ? 900 : 420) ? bd.slice(0, 400).replace(/\s+\S*$/, '') + '\u2026' : bd));
    if (o.info.sm) { const d = document.createElement('div'); d.className = 'sm'; d.textContent = o.info.sm; tip.appendChild(d); }
    dirty = true; tip.style.display = 'block'; const r = wrap.getBoundingClientRect(), x = (ev ? ev.clientX : r.left) - r.left, y = (ev ? ev.clientY : r.top) - r.top;
    tip.style.left = Math.max(4 + (parseFloat(lbs.style.left) || 0), Math.min(r.width - tip.offsetWidth - 4, x + 12)) + 'px'; tip.style.top = Math.max(4, y - 10 - tip.offsetHeight) + 'px';
    RD.forEach((q, k) => q.el.classList.toggle('on', k === o.info.rd)); if (D.onHL) D.onHL(o.info.rd == null ? null : o.info.rd); if (o.info.way) hoverWay(o.info.way); }
  function hideTip() { dirty = true; if (!pinned) hoverWay(null); tip.style.display = 'none'; RD.forEach(q => q.el.classList.remove('on')); if (D.onHL) D.onHL(null); }
  function nearest(ev) { const r = renderer.domElement.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top; let best = null, bd = 20;
    L.forEach(o => { if (!o.info || o.sx == null || o.off) return; const d = Math.hypot(o.sx - x, o.sy - y); if (d < bd) { bd = d; best = o; } }); return best; }
  const offClick = ev => { if (pinned && !wrap.contains(ev.target)) { pinned = null; hoverWay(null); hideTip(); } }; document.addEventListener('click', offClick, true);
  let downAt = null;
  renderer.domElement.addEventListener('pointermove', ev => { if (ev.buttons || pinned) return; const o = nearest(ev); if (o) { showTip(o, ev); return; }
    const k = wayAt(ev); hoverWay(k); if (k) { const R = D.routes.find(q => q.key === k); showTip({ info: { head: k + ' · ' + R.name, body: R.text || '' } }, ev); } else if (tip.style.display !== 'none') hideTip(); });
  renderer.domElement.addEventListener('pointerdown', ev => { downAt = [ev.clientX, ev.clientY]; });
  renderer.domElement.addEventListener('pointerup', ev => { if (!downAt || Math.hypot(ev.clientX - downAt[0], ev.clientY - downAt[1]) > 5) return; const o = nearest(ev);
    if (o) { pinned = o; showTip(o, ev); return; } const k = wayAt(ev); if (k) { const R = D.routes.find(q => q.key === k); pinned = { info: { head: k + ' · ' + R.name, body: R.text || '' } }; hoverWay(k); showTip(pinned, ev); } else { const g = D.onGround && groundAt(ev), gi = g && D.onGround(g[0], g[1]); if (gi) { pinned = { info: gi }; hoverWay(null); showTip(pinned, ev); } else { pinned = null; hoverWay(null); hideTip(); } } });
  renderer.domElement.addEventListener('pointerleave', () => { if (!pinned) { hoverWay(null); if (tip.style.display !== 'none') hideTip(); } });
  const RC = { A: '#111111', B: '#f4f4f4', C: '#e0007a' }, WAYS = {}, PICK = [];
  /* v261: a band laid on the ground along a curve: width w, lifted by lift, n steps; t0..t1 a part of the curve; tip narrows it to a point */
  function ribbon(c, w, lift, n, t0, t1, tip) { t0 = t0 || 0; t1 = t1 == null ? 1 : t1; n = n || Math.max(60, Math.min(1400, Math.ceil(c.getLength() * (t1 - t0) / 0.7))); const P = [], pos = [], idx = [];
    for (let i = 0; i <= n; i++) P.push(c.getPointAt(t0 + (t1 - t0) * i / n));
    const hy = (x, z) => gH(x + W / 2, z + H / 2);
    for (let i = 0; i <= n; i++) { const a = P[Math.max(0, i - 1)], b = P[Math.min(n, i + 1)], dx = b.x - a.x, dz = b.z - a.z, l = Math.hypot(dx, dz) || 1, nx = -dz / l, nz = dx / l, ww = tip ? w * (1 - i / n) : w, y0 = hy(P[i].x, P[i].z);
      for (const sd of [-1, 1]) { const x = P[i].x + nx * ww / 2 * sd, z = P[i].z + nz * ww / 2 * sd; pos.push(x, Math.max(hy(x, z), y0, hy((x + P[i].x) / 2, (z + P[i].z) / 2)) + lift, z); } }
    for (let i = 0; i < n; i++) { const a = 2 * i; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals(); return g; }
  const onGround = (m, o) => { m.side = THREE.DoubleSide; m.transparent = true; m.depthWrite = false; m.polygonOffset = true; m.polygonOffsetFactor = -o; m.polygonOffsetUnits = -o * 2; return m; };
  const NR = (D.routes || []).length, BADGE = [];
  const nearOther = (x, y, ri) => { let m = 1e9; (D.routes || []).forEach((Q, qi) => { if (qi === ri) return; for (let k = 0; k < Q.pts.length; k += 2) m = Math.min(m, Math.hypot(Q.pts[k][0] - x, Q.pts[k][1] - y)); }); return m; };
  (D.routes || []).forEach((R, ri) => {
    const off = (ri - (NR - 1) / 2) * 2.6, rp = R.pts.map((p, k, a) => { const p0 = a[Math.max(0, k - 2)], p1 = a[Math.min(a.length - 1, k + 2)], dx = p1[0] - p0[0], dy = p1[1] - p0[1], l = Math.hypot(dx, dy) || 1;
      return nearOther(p[0], p[1], ri) < 4 ? [p[0] - dy / l * off, p[1] + dx / l * off] : p; });
    const pts = rp.filter((p, k) => k % 2 === 0 || k === rp.length - 1).map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 1.6 + ri * 0.4, Z(p[1])));
    if (pts.length < 2) return; const c = new THREE.CatmullRomCurve3(pts);
    const mat = new THREE.MeshStandardMaterial({ color: RC[R.key] || '#111', roughness: 0.45, emissive: R.key === 'B' ? '#ffffff' : '#000000', emissiveIntensity: R.key === 'B' ? 0.35 : 0, transparent: true });
    mat.roughness = 0.8; onGround(mat, 4 + ri);
    const tube = new THREE.Mesh(ribbon(c, 3.4, 1.1 + ri * 0.2), mat); tube.receiveShadow = true; tube.renderOrder = 3 + ri * 2; scene.add(tube);
    const edge = new THREE.Mesh(ribbon(c, 4.6, 0.9 + ri * 0.2), onGround(new THREE.MeshStandardMaterial({ color: R.key === 'B' ? '#222' : '#f3efe6', roughness: 0.9, transparent: true, opacity: 0.8 }), 3 + ri)); edge.receiveShadow = true; edge.renderOrder = 2 + ri * 2; scene.add(edge);
    const fat = new THREE.Mesh(new THREE.TubeGeometry(c, 200, 5, 6), new THREE.MeshBasicMaterial({ transparent: true, opacity: 0, depthWrite: false })); fat.userData.key = R.key; scene.add(fat); PICK.push(fat);
    const info = { head: R.key + ' · ' + R.name, body: R.text || '', way: R.key };
    let bi = Math.floor(rp.length / 2), bs = -1;
    for (let f = 0.2; f <= 0.8; f += 0.04) { const k = Math.floor(rp.length * f), p = rp[k], sc = Math.min(nearOther(p[0], p[1], ri), 40) + Math.min(40, ...BADGE.map(b => Math.hypot(b[0] - p[0], b[1] - p[1])), 40) - Math.abs(f - 0.5) * 10; if (sc > bs) { bs = sc; bi = k; } }
    BADGE.push(rp[bi]);
    const badges = [rp[bi]].map(p => { const o = lab(R.key, 'wl', p[0], p[1], 5, 6, -13, -13, info);
      o.el.style.background = RC[R.key]; o.el.style.color = R.key === 'B' ? '#111' : '#fff'; o.el.style.borderColor = R.key === 'B' ? '#111' : '#fff'; return o; });
    /* v240: arrowheads along the way, pointing the way it goes (from the present to the goal) */
    const shell = onGround(new THREE.MeshBasicMaterial({ color: R.key === 'B' ? '#222222' : '#ffffff', transparent: true, opacity: 0.95 }), 3 + ri), arrows = [], len = c.getLength(), na = Math.max(2, Math.min(14, Math.round(len / 42))), up = new THREE.Vector3(0, 1, 0), bp = new THREE.Vector3(X(rp[bi][0]), 0, Z(rp[bi][1]));
    for (let i = 0; i < na; i++) { const t = (i + 0.5) / na, at = c.getPointAt(t), tg = c.getTangentAt(t).normalize();
      if (Math.hypot(at.x - bp.x, at.z - bp.z) < 9) continue;
      const dt = 11 / len, ta = Math.max(0, t - dt * 0.4), tb = Math.min(1, t + dt * 0.6);
      const cone = new THREE.Mesh(ribbon(c, 9, 1.5 + ri * 0.2, 16, ta, tb, true), mat); cone.renderOrder = 4 + ri * 2; scene.add(cone); arrows.push(cone);
      const ce = new THREE.Mesh(ribbon(c, 12.5, 1.5 + ri * 0.2, 16, Math.max(0, ta - dt * 0.12), Math.min(1, tb + dt * 0.12), true), shell); ce.renderOrder = 3 + ri * 2; scene.add(ce); arrows.push(ce); }
    /* v241: the stops in order, numbered 1, 2, 3 ... (START and GOAL keep their flags); shown on the selected way */
    const nums = []; let prev = null;
    (R.stops || []).slice(1, -1).forEach(sp => { if (prev && Math.hypot(sp[0] - prev[0], sp[1] - prev[1]) < 3) return; prev = sp;
      let bk = 0, bd = 1e9; rp.forEach((p, k) => { const d = Math.hypot(p[0] - sp[0], p[1] - sp[1]); if (d < bd) { bd = d; bk = k; } });
      const o = lab(String(nums.length + 1), 'wn', rp[bk][0], rp[bk][1], 4, 7, -9, -9, null); o.el.style.background = RC[R.key]; o.el.style.color = R.key === 'B' ? '#111' : '#fff'; o.el.style.borderColor = R.key === 'B' ? '#111' : '#fff'; o.hid = R.key !== 'A'; nums.push(o); });
    WAYS[R.key] = { tube, edge, badges, mat, arrows, shell, nums, rp, ri, stops: R.stops || null, name: R.name };
  });
  const LOOPS = new THREE.Group(); scene.add(LOOPS); let loopKey = '';
  const loopMat = new THREE.MeshStandardMaterial({ color: 0x3a1f0c, roughness: 0.5, emissive: 0x2a1205, emissiveIntensity: 0.4 }), haloMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.8 });
  function loops(list) { const key = (list || []).map(t => t.w).join('|'); if (key === loopKey) return; loopKey = key;
    while (LOOPS.children.length) { const m = LOOPS.children.pop(); m.geometry.dispose(); }
    (list || []).forEach(t => (t.lines || []).forEach(L => { if (!L || L.length < 2) return;
      const pts = L.map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 1.2, Z(p[1]))); const c = new THREE.CatmullRomCurve3(pts);
      const n = Math.max(24, pts.length * 3); LOOPS.add(new THREE.Mesh(new THREE.TubeGeometry(c, n, 1.05, 6), haloMat)); LOOPS.add(new THREE.Mesh(new THREE.TubeGeometry(c, n, 0.9, 6), loopMat)); }));
    dirty = true; }
  /* v213: a word's hoses from the agreement figure, drawn as the ways are (black: the ground agrees; white: it asks) */
  const HOSES = new THREE.Group(); scene.add(HOSES); let hoseN = 0;
  function hoses(h) { while (HOSES.children.length) { const m = HOSES.children.pop(); m.geometry.dispose(); m.material.dispose(); } hoseN = 0;
    if (h && h.pts && h.pts.length > 1) { const P = h.pts, white = !!h.ask;
      for (let i = 1; i < P.length; i++) { const a = P[i - 1], b = P[i], n = Math.max(8, Math.ceil(Math.hypot(b[0] - a[0], b[1] - a[1]) / 3)), pts = [];
        for (let k = 0; k <= n; k++) { const t = k / n, x = a[0] + (b[0] - a[0]) * t, y = a[1] + (b[1] - a[1]) * t; pts.push(new THREE.Vector3(X(x), gH(x, y) + 2 + Math.sin(Math.PI * t) * 4, Z(y))); }
        /* v214: thin lines; a question is dashed red */
        const c = new THREE.CatmullRomCurve3(pts), segs = white ? Math.max(4, Math.round(c.getLength() / 6)) : 1;
        for (let q = 0; q < segs; q += white ? 2 : 1) { const sp = []; for (let k = 0; k <= 8; k++) sp.push(c.getPoint((q + k / 8) / segs));
          HOSES.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(sp), white ? 8 : n * 4, 0.85, 6), new THREE.MeshStandardMaterial({ color: white ? '#b3261e' : '#111111', roughness: 0.5, emissive: white ? '#5a0d08' : '#000000', emissiveIntensity: white ? 0.35 : 0 }))); }
        hoseN++; } }
    dirty = true; }
  let selWay = null, hovWay = null;
  function showWays() { if (typeof WALK !== 'undefined' && WALK) return; const k = hovWay || selWay; Object.keys(WAYS).forEach(q => { const w = WAYS[q], on = !k || q === k; w.mat.opacity = on ? 1 : 0.15; if (w.edge) w.edge.material.opacity = on ? 0.9 : 0.1; if (w.shell) w.shell.opacity = on ? 0.95 : 0.12; (w.nums || []).forEach(o => { o.hid = !(k ? q === k : q === 'A'); }); w.badges.forEach(b => { b.el.style.opacity = on ? 1 : 0.25; }); }); dirty = true; }
  const ray = new THREE.Raycaster(), mv = new THREE.Vector2();
  function wayAt(ev) { if (!PICK.length) return null; const r = renderer.domElement.getBoundingClientRect(); mv.set((ev.clientX - r.left) / r.width * 2 - 1, -(ev.clientY - r.top) / r.height * 2 + 1); ray.setFromCamera(mv, camera); const hit = ray.intersectObjects(PICK, false)[0]; return hit ? hit.object.userData.key : null; }
  /* v233: where a tap lands on the ground, in the engine's own coordinates */
  function groundAt(ev) { const r = renderer.domElement.getBoundingClientRect(); mv.set((ev.clientX - r.left) / r.width * 2 - 1, -(ev.clientY - r.top) / r.height * 2 + 1); ray.setFromCamera(mv, camera); const hit = ray.intersectObject(terrain, false)[0]; return hit ? [hit.point.x + W / 2, hit.point.z + H / 2] : null; }
  function hoverWay(k) { if (k === hovWay) return; hovWay = k; showWays(); if (D.onWay) D.onWay(k); }
  /* ---------- legend ---------- */
  const sw = c => `rgb(${c.map(v => v | 0).join(',')})`, order = [[0, 'the highest ground'], [1, 'a ridge'], [2, 'low ground'], [3, 'lower ground'], [4, 'the lowest ground']];
  leg.innerHTML = '<b>LEGEND</b>' + order.map(([rk, t]) => { const k = RANK.indexOf(rk); return k < 0 ? '' : `<div class="r"><i style="background:${sw(EMOC[k])}"></i><span>${D.emo[k][0]}${PL ? '' : ': ' + t}</span></div>`; }).join('') + (PL ? '<div class="r"><i style="background:linear-gradient(#cfc8b8,#7d7566)"></i><span>The ground is the real terrain, ' + VXT + '. Emotion shows only as color.</span></div>' : '') +
    (PL ? '<div class="r"><i style="background:rgba(120,160,120,.45);border:2px solid #2a9d8f"></i><span>Shaded patches: areas you drew on the place map, in their emotion’s color.</span></div><div class="r"><i style="background:#8a8577"></i><span>Satellite image without color: no notes nearby, so no information here.</span></div>' : '<div class="r"><i style="background:rgb(140,135,127)"></i><span>Bare rock face: two distant emotions meet with no ridge of indifference between them, so getting across is a climb. A big move takes energy either way; most moves go through indifference.</span></div>' +
    '<div class="r"><i style="background:rgb(116,122,74)"></i><span>Plain grass, soil or rock, no color: no notes nearby, so no information here.</span></div>') +
    (D.routes && D.routes.length ? D.routes.map(R => `<div class="r"><i style="background:${RC[R.key]};border-color:#111;height:6px;margin-top:5px"></i><span><b style="display:inline;letter-spacing:0;font-size:12.5px">${R.key}</b> · ${R.name.replace(/[<>&]/g, '')}</span></div>`).join('') : '') +
    (D.spokes ? '<div class="r"><i style="background:#222;height:2px;margin-top:7px"></i><span>Thin lines: from each question’s flag to its notes.</span></div>' : '') + ((D.read || []).length ? '<div class="r"><i style="background:#111;border-radius:50%"></i><span>Numbered: what the ground says' + (D.spokes ? ' (from Pattern Synthesis). Hover or tap a number to read it.' : ', read above the map.') + '</span></div><div class="r"><i style="background:#3a1f0c;height:6px;margin-top:5px;border:1px solid #fff;box-shadow:0 0 0 1px #bbb"></i><span>A brown line: a pattern you ticked under PATTERNS THAT RUN THROUGH IT.</span></div>' : '') +
    (PL ? '<div class="r"><i style="background:#111;border-radius:50%"></i><span>Pins are notes in their emotion’s color, where you placed them; black flags are questions. The green flag (START) is the note farthest from the goal; the checkered flag is the goal, at ' + (PL.name ? PL.name.replace(/[<>&]/g, '') : 'your location') + '. North is at the back.</span></div>' : '<div class="r"><i style="background:#111;border-radius:50%"></i><span>Pins are notes in their emotion’s color; black flags are questions. The green flag is the present; the checkered flag is the goal. ← PRESENT and FUTURE → run along the front; ↑ HELP and ↓ HINDER run back to front.</span></div>') +
    '<div class="r"><span style="color:#666">Drag to turn, scroll or pinch to zoom. Hover or tap a note, question, the goal, a number, or a way to read it.</span></div>';

  /* v239: on a Taking Action card the legend is folded (Legend, closed); full screen still shows it open */
  if (D.card) leg.innerHTML = '<details class="grlf"><summary>Legend</summary>' + leg.innerHTML.replace('<b>LEGEND</b>', '') + '</details>';
  /* ---------- full screen: legend drawer and the method's name ---------- */
  const fsl = document.createElement('div'); fsl.className = 'grfs fsleg'; const fsb = document.createElement('button'); fsb.type = 'button'; fsb.className = 'grfs fslb'; fsb.textContent = 'Hide legend';
  const brand = document.createElement('div'); brand.className = 'grfs brand'; brand.innerHTML = '<b>THE BEAR CANYON METHOD</b> · BY OPERATIONAL COHERENCE';
  fsb.onclick = ev => { ev.stopPropagation(); const shut = !fsl.classList.contains('shut'); fsl.classList.toggle('shut', shut); fsb.textContent = shut ? 'Legend' : 'Hide legend'; moved = false; size(); };
  [fsl, fsb, brand].forEach(e => wrap.appendChild(e)); const fillFsl = () => { fsl.innerHTML = ''; const c = leg.cloneNode(true); c.style.display = ''; c.querySelectorAll('details').forEach(d => { d.open = true; }); fsl.appendChild(c); };
  /* ---------- buttons ---------- */
  const bReset = document.createElement('button'), bFs = document.createElement('button');
  bReset.className = bFs.className = 'bt'; bReset.textContent = 'Reset view'; bFs.textContent = 'Full screen';
  const bPlay = document.createElement('button'); bPlay.className = 'bt tpb'; bPlay.textContent = 'Play the tour'; bPlay.dataset.st = 'play';
  const bEnd = document.createElement('button'); bEnd.className = 'bt tpe'; bEnd.textContent = 'End tour';
  const bPrev = document.createElement('button'), bNext = document.createElement('button'); bPrev.className = bNext.className = 'bt tpn'; bPrev.textContent = '‹ Back'; bNext.textContent = 'Next ›'; bPrev.title = 'The stop before'; bNext.title = 'The next stop';
  const tbar = document.createElement('div'); tbar.className = 'tourbar'; tbar.appendChild(bPrev); tbar.appendChild(bPlay); tbar.appendChild(bNext); tbar.appendChild(bEnd); wrap.appendChild(tbar);
  const TL = (D.intro || []).concat(D.read || []), NI = (D.intro || []).length;
  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); });
  const barW = bar;
  if (D.card || TL.length < 2) tbar.style.display = 'none'; if (D.card) bFs.style.display = 'none'; wrap.appendChild(bar);
  let hMax = -1e9; for (let q = 0; q < hGrid.length; q++) if (hGrid[q] > hMax) hMax = hGrid[q];
  const corners = []; [-W / 2 - 16, W / 2].forEach(x => [BASE - 30, hMax + 14].forEach(y => [-H / 2, H / 2].forEach(z => corners.push(new THREE.Vector3(x, y, z)))));
  function home() { const tgt = new THREE.Vector3(0, (BASE + hMax) / 2 - 6, 8), dir = new THREE.Vector3(0, 290, 330).normalize(); let d = 440;
    for (let it = 0; it < 6; it++) { camera.position.copy(tgt).addScaledVector(dir, d); camera.lookAt(tgt); camera.updateMatrixWorld(); let m = 0;
      corners.forEach(c => { const q = c.clone().project(camera); m = Math.max(m, Math.abs(q.x), Math.abs(q.y)); }); d *= m / 0.99; }
    camera.position.copy(tgt).addScaledVector(dir, d); camera.lookAt(tgt); camera.updateMatrixWorld();
    // centre the block in the frame
    let y0 = 1, y1 = -1, x0 = 1, x1 = -1; corners.forEach(c => { const q = c.clone().project(camera); y0 = Math.min(y0, q.y); y1 = Math.max(y1, q.y); x0 = Math.min(x0, q.x); x1 = Math.max(x1, q.x); });
    const up = new THREE.Vector3(0, 1, 0).applyQuaternion(camera.quaternion), rt = new THREE.Vector3(1, 0, 0).applyQuaternion(camera.quaternion), th = Math.tan(camera.fov * Math.PI / 360) * d;
    const sh = up.multiplyScalar((y0 + y1) / 2 * th).add(rt.multiplyScalar((x0 + x1) / 2 * th * camera.aspect)); tgt.add(sh);
    camera.position.copy(tgt).addScaledVector(dir, d); controls.target.copy(tgt); controls.update(); dirty = true; }
  /* ---------- the guided tour of the ground (v208) ---------- */
  const cap = document.createElement('div'); cap.className = 'tourcap'; cap.setAttribute('aria-live', 'polite'); wrap.appendChild(cap);
  let TOUR = null;
  /* v246: what the tour is talking about glows: a white ring on the ground around the spot (an outline, so the colors
     inside stay visible), drawn over the land so a hill never hides it, and the notes the caption names light up */
  const spotM1 = new THREE.MeshBasicMaterial({ color: '#ffffff', transparent: true, opacity: 0.95, depthTest: false, depthWrite: false }),
    spotM2 = new THREE.MeshBasicMaterial({ color: '#ffffff', transparent: true, opacity: 0.3, depthTest: false, depthWrite: false }),
    spot = new THREE.Group(), sr1 = new THREE.Mesh(new THREE.TorusGeometry(16, 0.9, 8, 72), spotM1), sr2 = new THREE.Mesh(new THREE.TorusGeometry(16, 3.4, 8, 72), spotM2);
  [sr1, sr2].forEach(m => { m.rotation.x = -Math.PI / 2; m.renderOrder = 999; spot.add(m); }); spot.visible = false; scene.add(spot);
  function setSpot(r) { L.forEach(o => o.el.classList.remove('tfoc')); if (!r || !r.at) { spot.visible = false; dirty = true; return; }
    spot.position.set(X(r.at[0]), gH(r.at[0], r.at[1]) + 2, Z(r.at[1])); spot.visible = true;
    const nm = {}; (String((r.title || '') + ' ' + (r.cap || r.text || '')).match(/\b[NP]\d+\b/g) || []).forEach(k => { nm[k] = 1; });
    L.forEach(o => { if (/\bnl\b/.test(o.el.className) && nm[o.el.textContent.trim()]) o.el.classList.add('tfoc'); }); dirty = true; }
  function pulse(now) { if (!spot.visible) return; const w = Math.sin(now / 280); spot.scale.setScalar(1 + 0.07 * w); spotM2.opacity = 0.26 + 0.14 * w; }
  const ease = t => t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
  function homePose() { const p = camera.position.clone(), t = controls.target.clone(); home(); const hp = camera.position.clone(), ht = controls.target.clone(); camera.position.copy(p); controls.target.copy(t); camera.lookAt(t); return [hp, ht]; }
  /* v234: the first stop of each act opens with what the act means */
  function actOpen(i) { const r = TL[i]; if (i < NI || !r || r.grp == null || !D.actMean) return ''; const p = TL[i - 1]; return (i === NI || !p || p.grp !== r.grp) ? (D.actMean[r.grp] || '') : ''; }
  function capFor(i) { const r = TL[i], G = D.groups || [];
    cap.innerHTML = '<div class="ta"></div><div class="tm"></div><div class="tt"></div><div class="tx"></div><div class="tp"><i></i></div>'; const am = actOpen(i); cap.querySelector('.tm').textContent = am; cap.querySelector('.tm').style.display = am ? '' : 'none';
    cap.querySelector('.ta').textContent = r.act || G[r.grp] || ''; cap.querySelector('.tt').textContent = (i < NI ? '' : (i - NI + 1) + ' · ') + (r.title || ''); cap.querySelector('.tx').textContent = String(r.cap || r.text || '').replace(/\s*\(\s*(?:after\s+)?Vigneaux,?\s*2026\s*\)/g, '').replace(/\s+in Vigneaux \(2026\)/g, ''); }
  let autoFs = false;
  function stopTour() { if (!TOUR) return; TOUR = null; setSpot(null); wrap.classList.remove('touring'); controls.enabled = true; cap.style.display = 'none'; bPlay.textContent = 'Play the tour'; bPlay.dataset.st = 'play'; bPlay.title = ''; bEnd.style.display = bPrev.style.display = bNext.style.display = 'none';
    if (autoFs) { autoFs = false; if (wrap.classList.contains('fs')) bFs.onclick(); }
    RD.forEach(q => q.el.classList.remove('on')); if (D.onHL) D.onHL(null); moved = false; home(); dirty = true; }
  function pauseTour() { const T = TOUR; if (!T || T.paused != null) return; T.paused = (performance.now() - T.start) / 1000; controls.enabled = true; bPlay.textContent = 'Play'; bPlay.dataset.st = 'play'; dirty = true; }
  function resumeTour() { const T = TOUR; if (!T || T.paused == null) return; let l = T.legs[0]; for (const x of T.legs) if (T.paused >= x.t0) l = x;
    /* fly back from wherever the map was turned to, to the same stop, and carry on */
    l.a = [camera.position.clone(), controls.target.clone()]; T.start = performance.now() - l.t0 * 1000; T.paused = null; controls.enabled = false; bPlay.textContent = 'Pause'; bPlay.dataset.st = 'pause'; pinned = null; hideTip(); dirty = true; }
  function startTour() { if (TOUR) return TOUR.paused != null ? resumeTour() : pauseTour();
    if (!D.card && !wrap.classList.contains('fs')) { autoFs = true; bFs.onclick(); }
    const [hp, ht] = homePose(), dH = hp.distanceTo(ht), n = TL.length, SL = +window.gsmTourSlow || 1, fly = 1.2 * SL, legs = [];
    const hold = (r, i) => (Math.max(2.4, Math.min(6, String((r.title || '') + ' ' + (r.cap || r.text || '')).split(/\s+/).length / 3.3)) + Math.min(5, actOpen(i).split(/\s+/).filter(Boolean).length / 3.6)) * SL;
    let from = [camera.position.clone(), controls.target.clone()];
    TL.forEach((r, i) => { if (!r.at) { legs.push({ i, a: from, b: [hp.clone(), ht.clone()], fly, hold: hold(r, i) }); from = [hp.clone(), ht.clone()]; return; } const t = new THREE.Vector3(X(r.at[0]), gH(r.at[0], r.at[1]), Z(r.at[1])), az = -0.55 + 1.1 * (n > 1 ? i / (n - 1) : 0.5), po = 0.74, d = Math.max(controls.minDistance + 10, dH * 0.55);
      const p = t.clone().add(new THREE.Vector3(Math.sin(po) * Math.sin(az), Math.cos(po), Math.sin(po) * Math.cos(az)).multiplyScalar(d));
      const lk = t.clone().add(new THREE.Vector3(0, d * 0.08, 0)); legs.push({ i, a: from, b: [p, lk], fly, hold: hold(r, i) }); from = [p, lk]; });
    legs.push({ i: -1, a: from, b: [hp, ht], fly: 1.4 * SL, hold: 0 });
    let t0 = 0; legs.forEach(l => { l.t0 = t0; t0 += l.fly + l.hold; });
    wrap.classList.add('touring'); TOUR = { legs, start: performance.now(), total: t0, cur: -2, paused: null }; controls.enabled = false; cap.style.display = 'block'; bPlay.textContent = 'Pause'; bPlay.dataset.st = 'pause'; bPlay.title = 'Escape also ends the tour'; bEnd.style.display = bPrev.style.display = bNext.style.display = 'inline-block'; pinned = null; hideTip(); dirty = true; }
  /* v246: Back and Next jump to the stop before or after, and play on from there */
  function jumpTour(d) { const T = TOUR; if (!T) return; let k = T.legs.findIndex(l => l.i === T.cur); if (k < 0) k = 0; const j = Math.max(0, Math.min(T.legs.length - 1, k + d)); if (j === T.legs.length - 1 && d > 0 && k === T.legs.length - 2) { stopTour(); return; }
    const l = T.legs[j]; l.a = [camera.position.clone(), controls.target.clone()]; T.start = performance.now() - l.t0 * 1000; T.paused = null; T.cur = -2; controls.enabled = false; bPlay.textContent = 'Pause'; bPlay.dataset.st = 'pause'; pinned = null; hideTip(); dirty = true; }
  bPrev.onclick = ev => { ev.stopPropagation(); jumpTour(-1); }; bNext.onclick = ev => { ev.stopPropagation(); jumpTour(1); };
  function stepTour(now) { const T = TOUR; if (T.paused != null) { controls.update(); return; } const s = (now - T.start) / 1000; if (s >= T.total) { stopTour(); return; }
    let l = T.legs[0]; for (const x of T.legs) if (s >= x.t0) l = x;
    pulse(now); if (l.i !== T.cur) { T.cur = l.i; setSpot(l.i >= 0 ? TL[l.i] : null); if (l.i >= 0) { capFor(l.i); const ri = l.i - NI; RD.forEach((q, k) => q.el.classList.toggle('on', k === ri)); if (D.onHL) D.onHL(ri >= 0 ? ri : null); } else { cap.style.display = 'none'; RD.forEach(q => q.el.classList.remove('on')); if (D.onHL) D.onHL(null); } }
    const u = ease(Math.min(1, (s - l.t0) / l.fly));
    camera.position.lerpVectors(l.a[0], l.b[0], u); controls.target.lerpVectors(l.a[1], l.b[1], u); camera.lookAt(controls.target);
    const pi = cap.querySelector('.tp i'); if (pi) pi.style.width = (100 * s / T.total).toFixed(1) + '%'; dirty = true; }
  /* v259: walk a way, one leg at a time (Taking Action cards). Only where the way has been, the leg it is on, and
     the stop it is heading to are shown; a strip lists every stop in order and any stop can be tapped. */
  var WALK = null; const WG = new THREE.Group(); scene.add(WG);
  const legMat = new THREE.MeshStandardMaterial({ color: '#f2b400', roughness: 0.4, emissive: '#5a3c00', emissiveIntensity: 0.35 }), legEdge = new THREE.MeshBasicMaterial({ color: '#111111' }); onGround(legMat, 9); onGround(legEdge, 8); const legGhost = new THREE.MeshBasicMaterial({ color: '#f2b400', transparent: true, opacity: 0.5, depthTest: false, depthWrite: false, side: THREE.DoubleSide });
  const stopName = (sp, i, n) => { if (i === 0) return PL ? 'START' : 'PRESENT'; if (i === n - 1) return 'GOAL'; let b = null, bd = 4.5; D.notes.forEach(q => { const d = Math.hypot(q.x - sp[0], q.y - sp[1]); if (d < bd) { bd = d; b = q; } }); return b ? { k: (D.np || 'N') + b.k, n: b } : { k: 'a turn', n: null }; };
  function walkData(k) { const w = WAYS[k]; if (!w || !w.stops || w.stops.length < 3) return null; const rp = w.rp, st = [], idx = []; let from = 0;
    const extra = {}; w.stops.forEach((sp, i) => { if (i && Math.hypot(sp[0] - w.stops[i - 1][0], sp[1] - w.stops[i - 1][1]) < 3 && i < w.stops.length - 1) { (extra[st.length - 1] = extra[st.length - 1] || []).push(sp); return; } let bk = -1, bd = 1e9;
      for (let q = from; q < rp.length; q++) { const d = Math.hypot(rp[q][0] - sp[0], rp[q][1] - sp[1]); if (d < 4.5) { bk = q; break; } if (d < bd) { bd = d; bk = q; } }
      if (i === w.stops.length - 1) bk = rp.length - 1; if (i === 0) bk = 0; from = bk; st.push(sp); idx.push(bk); });
    const names = st.map((sp, i) => { const a = stopName(sp, i, st.length); if (typeof a === 'string' || !extra[i]) return a; const ks = [a.k]; extra[i].forEach(e => { const z = stopName(e, 1, 3); if (typeof z !== 'string' && z.n && ks.indexOf(z.k) < 0) ks.push(z.k); }); return { k: ks.join(' + '), n: a.n, all: ks }; });
    return { k, w, st, idx, names }; }
  const tube3 = (pts2, ri, r) => { const P = pts2.filter((p, q) => q % 2 === 0 || q === pts2.length - 1).map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 2 + ri * 0.4, Z(p[1]))); if (P.length < 2) return null; if (P.length === 2) P.splice(1, 0, P[0].clone().lerp(P[1], 0.5)); const c = new THREE.CatmullRomCurve3(P); return { c, g: ribbon(c, r * 2.4, r > 2.5 ? 1.6 : r > 1.5 ? 1.8 : 1.6) }; };
  function walkClear() { while (WG.children.length) { const m = WG.children.pop(); m.geometry.dispose(); if (m.material !== legMat && m.material !== legEdge && m.material !== legGhost) m.material.dispose(); } }
  function walkShow(i) { const Wk = WALK; if (!Wk) return; const n = Wk.st.length; i = Math.max(1, Math.min(n - 1, i)); Wk.i = i; walkClear();
    const ri = Wk.w.ri, a = Wk.idx[i - 1], b = Wk.idx[i];
    if (a > 0) { const t = tube3(Wk.w.rp.slice(0, a + 1), ri, 0.9); if (t) WG.add(new THREE.Mesh(t.g, onGround(new THREE.MeshStandardMaterial({ color: Wk.k === 'B' ? '#666666' : (RC[Wk.k] || '#111'), roughness: 0.8 }), 7))); }
    const t = tube3(Wk.w.rp.slice(a, Math.max(a + 2, b + 1)), ri, 2.1);
    if (t) { WG.add(new THREE.Mesh(t.g, legMat)); WG.add(new THREE.Mesh(t.g.clone(), legGhost)); const e = tube3(Wk.w.rp.slice(a, Math.max(a + 2, b + 1)), ri, 3.6); if (e) WG.add(new THREE.Mesh(e.g, legEdge));
      const at = t.c.getPointAt(0.97), tg = t.c.getTangentAt(0.97).normalize(), q = new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0, 1, 0), tg);
      const ll = t.c.getLength(), ta = Math.max(0, 1 - 13 / ll);
      WG.add(new THREE.Mesh(ribbon(t.c, 11, 1.9, 16, ta, 1, true), legMat)); WG.add(new THREE.Mesh(ribbon(t.c, 14.5, 1.8, 16, Math.max(0, ta - 1.5 / ll), 1, true), legEdge)); }
    WG.children.forEach(m => { m.renderOrder = m.material === legMat ? 22 : m.material === legEdge ? 21 : m.material === legGhost ? 19 : 20; });
    const nm = Wk.names, to = nm[i], fr = nm[i - 1], lbl = z => typeof z === 'string' ? z : z.k;
    setSpot({ at: Wk.st[i], title: [fr, to].map(z => typeof z === 'string' ? '' : z.k).join(' ') });
    cap.innerHTML = '<div class="ta"></div><div class="tt"></div><div class="tx"></div><div class="wk"></div>'; cap.appendChild(wbar);
    cap.querySelector('.ta').textContent = 'WAY ' + Wk.k + ' · STEP ' + i + ' OF ' + (n - 1);
    cap.querySelector('.tt').textContent = 'From ' + lbl(fr) + ' to ' + lbl(to);
    const tn = typeof to === 'string' ? null : to.n, tx = to === 'GOAL' ? (D.goalText || 'The goal.') : tn ? (tn.e == null ? '' : D.emo[tn.e][0][0].toUpperCase() + D.emo[tn.e][0].slice(1) + '. ') + String(tn.t || '') : (typeof to === 'string' ? '' : 'The way turns here, between notes.');
    cap.querySelector('.tx').textContent = tx.length > 220 ? tx.slice(0, 217).replace(/\s+\S*$/, '') + '…' : tx;
    const wk = cap.querySelector('.wk'); nm.forEach((z, q) => { if (q) { const s2 = document.createElement('i'); s2.textContent = '›'; wk.appendChild(s2); } const sp = document.createElement('span'); sp.textContent = lbl(z); sp.className = q === i ? 'at' : q === i - 1 ? 'fr' : q < i ? 'dn' : ''; sp.title = q ? 'Go to step ' + q : 'The start'; sp.onclick = ev => { ev.stopPropagation(); walkShow(Math.max(1, q)); }; wk.appendChild(sp); });
    wPrev.disabled = i <= 1; wNext.textContent = i >= n - 1 ? 'Done' : 'Next ›'; walkCap(); dirty = true; }
  /* the caption keeps off the leg it describes: top left, else bottom left, bottom right, top right */
  const wv = new THREE.Vector3();
  function walkCap() { const Wk = WALK; if (!Wk) return; const cw = renderer.domElement.clientWidth, ch = renderer.domElement.clientHeight, pad = parseFloat(renderer.domElement.style.marginLeft) || 0, a = Wk.idx[Wk.i - 1], b = Wk.idx[Wk.i], P = [];
    for (let q = a; q <= b; q += Math.max(1, Math.floor((b - a) / 12))) P.push(Wk.w.rp[q]); P.push(Wk.w.rp[b]);
    const S = P.map(p => { wv.set(X(p[0]), gH(p[0], p[1]) + 2, Z(p[1])).project(camera); return [pad + (wv.x * 0.5 + 0.5) * cw, (-wv.y * 0.5 + 0.5) * ch]; });
    const w = cap.offsetWidth, h = cap.offsetHeight, W2 = wrap.clientWidth, H2 = wrap.clientHeight, m = 18;
    const C = [[pad + 12, 44], [pad + 12, H2 - h - 12], [W2 - w - 12, H2 - h - 12], [W2 - w - 12, 44]];
    let best = C[0], bn = 1e9; C.forEach(([x, y]) => { const n = S.filter(([sx, sy]) => sx > x - m && sx < x + w + m && sy > y - m && sy < y + h + m).length; if (n < bn) { bn = n; best = [x, y]; } });
    cap.style.left = Math.max(pad + 4, best[0]) + 'px'; cap.style.right = 'auto'; cap.style.top = Math.max(4, best[1]) + 'px'; }
  /* on a card shown in the page, the walk opens the card's full screen (as the tour does), and closes it again after */
  let walkFs = false; const cardFs = () => { const c = host.closest('.coa'); return c ? c.querySelector('.gtfsb') : null; };
  function walkStart(k) { if (TOUR) stopTour(); const Wk = walkData(k || selWay || 'A'); if (!Wk) return; WALK = Wk; wrap.classList.add('walking'); pinned = null; hideTip();
    const fb = cardFs(); if (D.card && fb && !host.closest('.gtfs-on')) { walkFs = true; fb.click(); setTimeout(() => { try { wrap.scrollIntoView({ block: 'nearest' }); } catch (e) {} }, 60); }
    Object.keys(WAYS).forEach(q => { const w = WAYS[q]; w.mat.opacity = q === Wk.k ? 0.22 : 0.06; if (w.edge) w.edge.material.opacity = q === Wk.k ? 0.15 : 0.05; if (w.shell) w.shell.opacity = 0.05; (w.nums || []).forEach(o => { o.hid = true; }); w.badges.forEach(b => { b.el.style.opacity = 0.2; }); });
    walkShow(1); }
  controls.addEventListener('end', () => { if (WALK) walkCap(); });
  function walkEnd() { if (!WALK) return; WALK = null; walkClear(); setSpot(null); wrap.classList.remove('walking'); cap.style.display = 'none'; cap.innerHTML = ''; cap.style.top = ''; cap.style.right = ''; showWays(); walkBtn();
    if (walkFs) { walkFs = false; const fb = cardFs(); if (fb && host.closest('.gtfs-on')) fb.click(); } dirty = true; }
  const wbar = document.createElement('div'); wbar.className = 'walkbar'; const wPrev = document.createElement('button'), wNext = document.createElement('button'), wEnd = document.createElement('button');
  wPrev.className = wEnd.className = 'bt'; wNext.className = 'bt wnx'; wPrev.textContent = '‹ Back'; wNext.textContent = 'Next ›'; wEnd.textContent = 'Stop walking'; [wPrev, wNext, wEnd].forEach(b2 => { b2.type = 'button'; wbar.appendChild(b2); });
  wPrev.onclick = ev => { ev.stopPropagation(); if (WALK) walkShow(WALK.i - 1); }; wNext.onclick = ev => { ev.stopPropagation(); if (!WALK) return; if (WALK.i >= WALK.st.length - 1) walkEnd(); else walkShow(WALK.i + 1); }; wEnd.onclick = ev => { ev.stopPropagation(); walkEnd(); };
  const bWalk = document.createElement('button'); bWalk.type = 'button'; bWalk.className = 'bt wgo'; bWalk.style.position = 'static';
  function walkBtn() { const k = selWay || 'A', d = WAYS[k] && WAYS[k].stops && WAYS[k].stops.length >= 3; bWalk.style.display = D.card && d ? '' : 'none'; bWalk.textContent = 'Walk way ' + k + ', step by step'; bWalk.title = 'Follow way ' + k + ' one leg at a time, in order'; }
  bWalk.onclick = ev => { ev.stopPropagation(); WALK ? walkEnd() : walkStart(); };
  document.addEventListener('keydown', e => { if (!WALK || !host.isConnected) return; if (e.key === 'ArrowRight') { e.preventDefault(); wNext.onclick(e); } else if (e.key === 'ArrowLeft') { e.preventDefault(); wPrev.onclick(e); } else if (e.key === 'Escape') walkEnd(); });
  barW.insertBefore(bWalk, barW.firstChild); walkBtn();
  bPlay.onclick = ev => { ev.stopPropagation(); startTour(); }; bEnd.onclick = ev => { ev.stopPropagation(); stopTour(); };
  wrap.addEventListener('pointerdown', e => { if (TOUR && !(e.target.closest && e.target.closest('.bt,.grfs'))) pauseTour(); });
  bReset.onclick = () => { if (TOUR) stopTour(); moved = false; home(); };
  bFs.onclick = () => { const on = !wrap.classList.contains('fs'); if (on) fillFsl(); moved = false; wrap.classList.toggle('fs', on); if (D.onFs) D.onFs(on, wrap); bFs.textContent = on ? 'Close full screen' : 'Full screen'; document.documentElement.style.overflow = on ? 'hidden' : ''; size(); };
  const onKey = e => { if (e.key !== 'Escape') return; if (TOUR) stopTour(); else if (wrap.classList.contains('fs')) bFs.onclick(); const on = wrap.classList.contains('fs'); if ((bFs.textContent === 'Close full screen') !== on) { bFs.textContent = on ? 'Close full screen' : 'Full screen'; if (!on) document.documentElement.style.overflow = ''; moved = false; size(); } }; document.addEventListener('keydown', onKey);

  /* ---------- sizing, labels, loop ---------- */
  let dirty = true, alive = true, lastW = 0, lastCfs = false;
  function size() { const fs = wrap.classList.contains('fs'), w = fs ? window.innerWidth : wrap.clientWidth; if (!w) return; const cfs = D.card && host.closest('.gtfs-on'), h = fs ? window.innerHeight : cfs ? Math.round(Math.max(420, window.innerHeight * 0.78)) : Math.round(Math.max(300, Math.min(D.card ? 520 : 620, w * (D.card ? 0.62 : 0.56))));
    /* a strategy card in full screen gets the same legend drawer and name as the full-screen Pattern Synthesis map */
    wrap.classList.toggle('cfs', !!cfs); if (cfs) fillFsl(); leg.style.display = foot.style.display = cfs ? 'none' : '';
    const pad = (fs || cfs) && !fsl.classList.contains('shut') ? Math.min(340, Math.round(w * 0.86)) : 0, vw = Math.max(200, w - pad);
    wrap.style.height = fs ? '' : h + 'px'; renderer.setSize(vw, h); renderer.domElement.style.marginLeft = pad + 'px'; lbs.style.left = pad + 'px'; attr.style.left = pad + 6 + 'px'; if (typeof cap !== 'undefined') cap.style.left = pad + 12 + 'px'; if (typeof tbar !== 'undefined') tbar.style.left = pad + vw / 2 + 'px'; const fl = wrap.querySelector('.fslay'); if (fl) { fl.style.left = pad + 12 + 'px'; fl.style.maxWidth = Math.max(220, vw * 0.62) + 'px'; } camera.aspect = vw / h;
    // keep the whole block in frame
    camera.fov = 30; camera.updateProjectionMatrix(); lastW = w; if (typeof home === 'function' && !moved) home(); dirty = true; }
  const ro = window.ResizeObserver ? new ResizeObserver(size) : null; if (ro) ro.observe(wrap); window.addEventListener('resize', size);
  let moved = false; controls.addEventListener('start', () => { moved = true; }); controls.addEventListener('change', () => { dirty = true; if (!pinned) tip.style.display = 'none'; });
  const v = new THREE.Vector3();
  /* v258: labels look for free ground around their own pin, and a moved label gets a leader line back to it */
  const hv = new THREE.Vector3(), hv2 = new THREE.Vector3();
  function place() { const w = renderer.domElement.clientWidth, h = renderer.domElement.clientHeight, boxes = [], heads = [];
    const up = new THREE.Vector3(0, 1, 0).applyQuaternion(camera.quaternion);
    L.forEach(o => { if (!o.head || o.hid || o.off) return; hv.copy(o.head).project(camera); if (hv.z > 1) return; hv2.copy(o.head).addScaledVector(up, 2.8).project(camera);
      const r = 1.5 * Math.max(3, Math.hypot((hv2.x - hv.x) * 0.5 * w, (hv2.y - hv.y) * 0.5 * h)); heads.push({ o, x: (hv.x * 0.5 + 0.5) * w, y: (-hv.y * 0.5 + 0.5) * h, r }); });
    const rings = []; RINGP.forEach(q => { hv.copy(q).project(camera); if (hv.z <= 1) rings.push([(hv.x * 0.5 + 0.5) * w, (-hv.y * 0.5 + 0.5) * h]); });
    const hitR = (o, x, y, bw, bh) => { if (o.el.textContent === 'GOAL') return 0; let n = 0; for (const r of rings) if (r[0] > x - 3 && r[0] < x + bw + 3 && r[1] > y - 3 && r[1] < y + bh + 3) n += 30; return n; };
    const hitB = (x, y, bw, bh) => { let n = 0; for (const b of boxes) if (x < b[0] + b[2] && x + bw > b[0] && y < b[1] + b[3] && y + bh > b[1]) n += Math.min(x + bw, b[0] + b[2]) - Math.max(x, b[0]) + 1; return n; };
    const hitH = (o, x, y, bw, bh) => { let n = 0; if (!o.isN) return 0; for (const q of heads) { if (q.o === o) continue; const cx = Math.max(x, Math.min(q.x, x + bw)), cy = Math.max(y, Math.min(q.y, y + bh)); if ((cx - q.x) ** 2 + (cy - q.y) ** 2 < (q.r + 1) ** 2) n += 40 + q.r; } return n; };
    L.map(o => { v.copy(o.v).project(camera); o.sx = (v.x * 0.5 + 0.5) * w; o.sy = (-v.y * 0.5 + 0.5) * h; return { o, x: o.sx + o.ax, y: o.sy + o.ay, off: v.z > 1 }; })
     .sort((a, b) => b.o.pri - a.o.pri || a.o.sy - b.o.sy)
     .forEach(p => { const o = p.o; if (o.hid || p.off || p.x < -24 || p.x > w + 24 || p.y < -24 || p.y > h + 24) { o.el.style.display = 'none'; if (o.ld) o.ld.style.display = 'none'; return; } o.el.style.display = '';
       const bw = o.el.offsetWidth || 30, bh = o.el.offsetHeight || 16; let x = p.x, y = p.y;
       /* the side and axis words keep their places; everything else may move off a crowded spot */
       if (!/\bside\b/.test(o.el.className) && (hitB(x, y, bw, bh) || hitH(o, x, y, bw, bh) || hitR(o, x, y, bw, bh))) {
         const ax = o.sx, ay = o.sy, g = 4, C = [];
         [0, 1, 2, 3].forEach(k => { const d = k * (bh + 2);
           C.push([p.x, p.y - d - (k ? 0 : 0)], [ax + g + d, ay - bh / 2], [ax - g - bw - d, ay - bh / 2], [ax - bw / 2, ay - g - bh - d], [ax - bw / 2, ay + g + d], [ax + g + d * 0.7, ay - g - bh - d * 0.7], [ax - g - bw - d * 0.7, ay - g - bh - d * 0.7], [ax + g + d * 0.7, ay + g + d * 0.7], [ax - g - bw - d * 0.7, ay + g + d * 0.7]); });
         let best = null, bs = 1e9;
         for (let i = 0; i < C.length; i++) { const [cx, cy] = C[i]; if (cx < 2 || cx + bw > w - 2 || cy < 2 || cy + bh > h - 2) continue; const sc = hitB(cx, cy, bw, bh) * 20 + hitH(o, cx, cy, bw, bh) * 20 + hitR(o, cx, cy, bw, bh) * 20 + i; if (sc < bs) { bs = sc; best = C[i]; } if (sc === i) break; }
         if (best) { x = best[0]; y = best[1]; } }
       if (o.isN) { const dd = camera.position.distanceTo(o.v), d0 = camera.position.distanceTo(controls.target), fz = Math.max(0, Math.min(1, (dd - d0 * 0.95) / (d0 * 0.4))), fo = (1 - 0.35 * fz).toFixed(2); o.el.style.filter = fo === '1.00' ? '' : 'opacity(' + fo + ')'; }
       x = Math.max(2, Math.min(w - bw - 2, x)); boxes.push([x, y, bw, bh]); o.el.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px)`;
       /* a leader line when the label has left its pin */
       const ex = Math.max(x, Math.min(o.sx, x + bw)), ey = Math.max(y, Math.min(o.sy, y + bh)), dl = Math.hypot(ex - o.sx, ey - o.sy), far = Math.hypot(x - p.x, y - p.y) > 3;
       if (far && dl > 7) { if (!o.ld) { o.ld = document.createElement('div'); o.ld.className = 'ldr'; lbs.insertBefore(o.ld, lbs.firstChild); }
         const r0 = 3.5, L0 = dl - r0; o.ld.style.display = 'block'; o.ld.style.width = L0.toFixed(1) + 'px'; const an = Math.atan2(ey - o.sy, ex - o.sx); o.ld.style.transform = `translate(${(o.sx + Math.cos(an) * r0).toFixed(1)}px,${(o.sy + Math.sin(an) * r0).toFixed(1)}px) rotate(${an.toFixed(3)}rad)`; o.ld.style.opacity = o.el.style.opacity || ''; }
       else if (o.ld) o.ld.style.display = 'none'; }); }
  function loop() { if (!alive) return; if (!host.isConnected) { dispose(); return; } if (TOUR) stepTour(performance.now()); else controls.update();
    if (!!(D.card && host.closest('.gtfs-on')) !== lastCfs) dirty = true;
    if (dirty && wrap.clientWidth) { RD.forEach(o => o.rim && o.rim.quaternion.copy(camera.quaternion)); if ((wrap.clientWidth !== lastW || !!(D.card && host.closest('.gtfs-on')) !== lastCfs) && !wrap.classList.contains('fs')) { lastCfs = !!(D.card && host.closest('.gtfs-on')); size(); } draw(); place(); dirty = false; } requestAnimationFrame(loop); }
  function dispose() { if (!alive) return; alive = false; if (ro) ro.disconnect(); window.removeEventListener('resize', size); document.removeEventListener('keydown', onKey); document.removeEventListener('click', offClick, true); renderer.dispose(); try { renderer.forceContextLoss(); } catch (e) {} }
  size(); home(); loop(); placeGround();
  function focusQ(q) { NOBJ.forEach(o => { const on = !q || o.q === q; o.st.visible = o.hd.visible = on; if (o.sp) o.sp.visible = on; o.lo.off = !on; o.lo.el.style.opacity = on ? '' : '0'; o.lo.el.style.pointerEvents = on ? '' : 'none'; }); dirty = true; }
  return { loops, hoses, hoseCount() { return hoseN; }, focusQ, tour: startTour, touring() { return !!TOUR; }, paused() { return !!TOUR && TOUR.paused != null; }, hl(i) { if (!pinned) RD.forEach((o, k) => o.el.classList.toggle('on', k === i)); }, setWay(k) { if (k !== selWay) { selWay = k; if (WALK) walkEnd(); showWays(); walkBtn(); } }, walk(k) { walkStart(k); }, walking() { return WALK ? { k: WALK.k, i: WALK.i, n: WALK.st.length - 1, names: WALK.names.map(z => typeof z === 'string' ? z : z.k) } : null; }, walkStep(i) { walkShow(i); }, walkEnd() { walkEnd(); }, hoverWay(k) { hoverWay(k); },
    snap() { draw(); return renderer.domElement.toDataURL('image/jpeg', 0.85); }, height() { return wrap.offsetHeight; }, dispose };
}

/* real elevation for a place map: AWS Terrain Tiles (Terrarium PNG, USGS 3DEP in the US), decoded to meters
   above the lowest point in the frame. Fetched before the scene is built; flat if they cannot be loaded. */
const ELC = new Map();
function prep(P) {
  if (!P || P.elev !== undefined) return Promise.resolve();
  const key = [P.X0, P.Y0, P.k].map(v => (+v).toFixed(7)).join('|');
  if (!ELC.has(key)) ELC.set(key, loadElev(P));
  return ELC.get(key).then(f => { P.elev = f; }, () => { P.elev = null; });
}
function loadElev(P) {
  const FW = 340, FH = 230, span = FW / P.k;
  let z = Math.max(1, Math.min(15, Math.round(Math.log2(640 / span)))), a, b, c, d;
  const rng = () => { const n = 2 ** z; a = Math.floor(P.X0 * n / 256); b = Math.floor((P.X0 + span) * n / 256); c = Math.floor(P.Y0 * n / 256); d = Math.floor((P.Y0 + FH / P.k) * n / 256); };
  rng(); while ((b - a + 1) * (d - c + 1) > 36 && z > 1) { z--; rng(); }
  const n = 2 ** z, cw = (b - a + 1) * 256, chh = (d - c + 1) * 256, cv = document.createElement('canvas'); cv.width = cw; cv.height = chh;
  const cx = cv.getContext('2d', { willReadFrequently: true }), total = (b - a + 1) * (d - c + 1);
  return new Promise(res => {
    let left = total, ok = 0, fin = false;
    const finish = () => { if (fin) return; fin = true;
      if (ok < total) return res(null);
      let px; try { px = cx.getImageData(0, 0, cw, chh).data; } catch (e) { return res(null); }
      const el = new Float32Array(cw * chh); for (let q = 0, o = 0; q < el.length; q++, o += 4) el[q] = px[o] * 256 + px[o + 1] + px[o + 2] / 256 - 32768;
      const at = (fx, fy) => { const X = Math.max(0, Math.min(cw - 1.001, (P.X0 + fx / P.k) * n - a * 256)), Y = Math.max(0, Math.min(chh - 1.001, (P.Y0 + fy / P.k) * n - c * 256)), i = X | 0, j = Y | 0, u = X - i, v = Y - j, g = (p, q) => el[q * cw + p];
        return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; };
      let lo = 1e9, hi = -1e9; for (let j = 0; j <= 40; j++) for (let i = 0; i <= 60; i++) { const h = at(i / 60 * FW, j / 40 * FH); lo = Math.min(lo, h); hi = Math.max(hi, h); }
      if (!isFinite(lo) || hi - lo > 9000) return res(null);
      const f = (fx, fy) => at(fx, fy) - lo; f.lo = lo; f.hi = hi; res(f); };
    setTimeout(finish, 12000);
    for (let tx = a; tx <= b; tx++) for (let ty = c; ty <= d; ty++) { const im = new Image(); im.crossOrigin = 'anonymous';
      im.onload = () => { try { cx.drawImage(im, (tx - a) * 256, (ty - c) * 256); ok++; } catch (e) {} if (--left === 0) finish(); };
      im.onerror = () => { if (--left === 0) finish(); };
      im.src = 'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/' + z + '/' + tx + '/' + ty + '.png'; }
  });
}
window.gsmRelief = { mount, prep, version: 'r2' };
