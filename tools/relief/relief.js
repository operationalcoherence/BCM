/* Pattern Synthesis relief model (approved 12 Nov 2026). Bundled with three.js into gsm-relief.js,
   loaded only when the Pattern Synthesis map mounts. window.gsmRelief.mount(el, D) -> {hl(i), dispose()} */
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

const CSS = `
.grel{position:relative;width:100%;background:#fff;border:1px solid #e4e4e4;overflow:hidden;touch-action:none}
.grel canvas{display:block}
.grel .lbs{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.grel .lb{position:absolute;left:0;top:0;white-space:nowrap}
.grel .nl{font:bold 12.5px Helvetica,Arial,sans-serif;color:#111;text-shadow:0 0 3px #fff,0 0 3px #fff,0 0 3px #fff}
.grel .ql{font:bold 12px Helvetica,Arial,sans-serif;background:#111;color:#fff;padding:2px 5px}
.grel .pl{font:bold 13px Helvetica,Arial,sans-serif;letter-spacing:.1em;color:#111;text-shadow:0 0 3px #fff,0 0 3px #fff,0 0 4px #fff}
.grel .side{font:bold 17.5px Helvetica,Arial,sans-serif;letter-spacing:.14em;color:#1f6f66;text-shadow:0 0 3px #fff,0 0 3px #fff}.grel .side.hd{color:#8a2a22}.grel .side.ax{color:#333}.grel .lb.hit{pointer-events:auto;cursor:pointer}.grel .tip{position:absolute;display:none;z-index:4;max-width:340px;max-height:60%;overflow:auto;background:#222;color:#fff;font:13px/1.45 Questrial,Helvetica,Arial,sans-serif;padding:8px 10px;border-radius:2px;box-shadow:0 2px 8px rgba(0,0,0,.3)}.grel .tip b{display:block;margin-bottom:3px}.grel .tip .sm{opacity:.75;font-size:12px;margin-top:4px}
.grel .rdm{font:bold 12px Helvetica,Arial,sans-serif;color:#fff;background:#111;width:22px;height:22px;line-height:20px;text-align:center;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.4)}
.grel .rdm.on{background:#7a1d12;transform:scale(1.25)}
.grel .wl{font:bold 14px Helvetica,Arial,sans-serif;width:26px;height:26px;line-height:22px;text-align:center;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.45)}.grel .bt{position:absolute;top:8px;background:#fff;border:1px solid #222;font:12px Questrial,Helvetica,Arial,sans-serif;padding:4px 9px;cursor:pointer;z-index:3}
.grel.fs{position:fixed;inset:0;z-index:2147483000;border:0}
.grel .busy{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#888;font:13px Questrial,Helvetica,Arial,sans-serif}
.grleg{margin:8px 0 2px;font-size:12.5px;line-height:1.45;color:#333}
.grleg .r{display:flex;gap:8px;align-items:flex-start;margin:3px 0}
.grleg i{flex:0 0 26px;height:12px;border-radius:2px;margin-top:2px;border:1px solid #ccc}
.grleg b{letter-spacing:.12em;font-size:11px;display:block;margin:6px 0 2px}`;

/* ---------- small helpers ---------- */
function hash(x, y) { let h = x * 374761393 + y * 668265263; h = (h ^ (h >>> 13)) * 1274126177; return ((h ^ (h >>> 16)) >>> 0) / 4294967295; }
function vn(x, y) { const i = Math.floor(x), j = Math.floor(y), u = x - i, v = y - j, su = u * u * (3 - 2 * u), sv = v * v * (3 - 2 * v);
  const a = hash(i, j), b = hash(i + 1, j), c = hash(i, j + 1), d = hash(i + 1, j + 1); return a + (b - a) * su + (c - a) * sv + (a - b - c + d) * su * sv; }
function fbm(x, y, o = 5) { let s = 0, a = 0.5, f = 1; for (let k = 0; k < o; k++) { s += a * vn(x * f, y * f); f *= 2.03; a *= 0.5; } return s; }
function ridged(x, y, o = 4) { let s = 0, a = 0.5, f = 1; for (let k = 0; k < o; k++) { const n = 1 - Math.abs(vn(x * f, y * f) * 2 - 1); s += a * n * n; f *= 2.1; a *= 0.5; } return s; }
const sstep = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const mix = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
function vivid(c) { let [r, g, b] = c.map(v => v / 255); const mx = Math.max(r, g, b), mn = Math.min(r, g, b); let l = (mx + mn) / 2, sa = 0, h = 0, d = mx - mn;
  if (d > 1e-6) { sa = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn); h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6; }
  sa = Math.min(1, sa * 1.5 + 0.08); l = Math.min(0.62, Math.max(0.42, l));
  const q = l < 0.5 ? l * (1 + sa) : l + sa - l * sa, p = 2 * l - q, f = t => { t = (t + 1) % 1; return t < 1 / 6 ? p + (q - p) * 6 * t : t < 0.5 ? q : t < 2 / 3 ? p + (q - p) * (2 / 3 - t) * 6 : p; };
  return [f(h + 1 / 3) * 255, f(h) * 255, f(h - 1 / 3) * 255]; }

const CACHE = new Map();
function landKey(D) { let s = 0; for (let q = 0; q < D.hn.length; q += 97) s += D.hn[q] * (q + 1); return D.VX + ',' + D.VY + ',' + D.notes.length + ',' + s.toFixed(4) + ',' + D.notes.map(n => n.k + ':' + n.e + ':' + Math.round(n.x) + ':' + Math.round(n.y)).join(';'); }
function mount(host, D) {
  if (!document.getElementById('gsm-relcss')) { const s = document.createElement('style'); s.id = 'gsm-relcss'; s.textContent = CSS; document.head.appendChild(s); }
  const VX = D.VX, VY = D.VY, CX = D.CX, CY = D.CY, W = (VX - 1) * CX, H = (VY - 1) * CY, HS = 58, ALPHA = 0.6;
  const wrap = document.createElement('div'); wrap.className = 'grel pnet'; host.appendChild(wrap);
  const lbs = document.createElement('div'); lbs.className = 'lbs'; wrap.appendChild(lbs);
  const busy = document.createElement('div'); busy.className = 'busy'; busy.textContent = 'Building the land…'; wrap.appendChild(busy);
  const leg = document.createElement('div'); leg.className = 'grleg'; host.appendChild(leg);

  /* ---------- heights ---------- */
  function bil(arr, x, y) { const fx = Math.max(0, Math.min(VX - 1.001, x / CX)), fy = Math.max(0, Math.min(VY - 1.001, y / CY)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
    const g = (ii, jj) => arr[jj * VX + ii]; return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; }
  const hRaw = (x, y) => bil(D.hn, x, y) * HS;
  function hAt(x, y) { const e = 0.6, gx = (hRaw(x + e, y) - hRaw(x - e, y)) / (2 * e), gy = (hRaw(x, y + e) - hRaw(x, y - e)) / (2 * e), s = Math.hypot(gx, gy);
    const k = sstep(0.25, 1.1, s), ux = s > 1e-4 ? -gy / s : 1, uy = s > 1e-4 ? gx / s : 0, across = x * ux + y * uy, along = (x * gx + y * gy) / (s || 1);
    const gul = (ridged(across * 0.18 + vn(x * 0.04, y * 0.04) * 2, along * 0.025, 3) - 0.4) * 2.4 * k;
    return hRaw(x, y) + gul + (ridged(x * 0.11 + 3, y * 0.11 + 7) - 0.35) * 0.9 * (1 - 0.6 * k) + (fbm(x * 0.35, y * 0.35, 3) - 0.5) * 0.5; }
  const MX = 2 * VX - 1, MY = 2 * VY - 1, CK = landKey(D), CH = CACHE.get(CK) || {};
  const hGrid = CH.hGrid || new Float32Array(MX * MY); let hMin = 1e9;
  if (!CH.hGrid) for (let j = 0; j < MY; j++) for (let i = 0; i < MX; i++) { const h = hAt(i / (MX - 1) * W, j / (MY - 1) * H); hGrid[j * MX + i] = h; }
  for (let q = 0; q < hGrid.length; q++) if (hGrid[q] < hMin) hMin = hGrid[q];
  CH.hGrid = hGrid; CACHE.set(CK, CH);
  const BASE = hMin - 7;
  function gH(x, y) { const fx = Math.max(0, Math.min(MX - 1.001, x / W * (MX - 1))), fy = Math.max(0, Math.min(MY - 1.001, y / H * (MY - 1))), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
    const g = (a, b) => hGrid[b * MX + a]; return g(i, j) * (1 - u) * (1 - v) + g(i + 1, j) * u * (1 - v) + g(i, j + 1) * (1 - u) * v + g(i + 1, j + 1) * u * v; }

  /* ---------- emotion field from the notes; rock face where distant emotions meet ---------- */
  const EMOC = D.emo.map(e => vivid(e[1])), K = D.emo.length;
  const RANK = D.emo.map(e => /accept/i.test(e[0]) ? 0 : /indiff/i.test(e[0]) ? 1 : /distrust/i.test(e[0]) ? 2 : /aggress/i.test(e[0]) ? 3 : 4);
  const DEF = RANK.indexOf(4), EN = D.notes.filter(n => n.e != null);
  const EF = { w: 96 }; EF.h = Math.round(EF.w * H / W); EF.a = new Float32Array(EF.w * EF.h * (K + 2));
  for (let j = 0; j < EF.h; j++) for (let i = 0; i < EF.w; i++) {
    const x = i / (EF.w - 1) * W, y = j / (EF.h - 1) * H, ws = new Float32Array(K), o = (j * EF.w + i) * (K + 2);
    EN.forEach(n => { ws[n.e] += Math.exp(-((n.x - x) ** 2 + (n.y - y) ** 2) / (2 * 26 * 26)); });
    let tot = 0, p = 0; for (let k = 0; k < K; k++) { const v = (ws[k] * (k === DEF ? 1.6 : 1)) ** 2.2; EF.a[o + k] = v; p += v; tot += ws[k]; }
    for (let k = 0; k < K; k++) EF.a[o + k] /= (p || 1);
    EF.a[o + K] = sstep(0.04, 0.5, tot);
    const ord = [...ws.keys()].sort((u, v) => ws[v] - ws[u]), k1 = ord[0], k2 = ord[1], s1 = ws[k1], s2 = ws[k2];
    EF.a[o + K + 1] = (Math.abs(RANK[k1] - RANK[k2]) < 2 || RANK[k1] === 1 || RANK[k2] === 1 || s2 < 0.03) ? 0 : sstep(0.22, 0.42, s2 / (s1 + s2));
  }
  function emoMix(x, y) { const fx = Math.min(EF.w - 1.001, x / W * (EF.w - 1)), fy = Math.min(EF.h - 1.001, y / H * (EF.h - 1)), i = fx | 0, j = fy | 0, u = fx - i, v = fy - j;
    const g = (ii, jj, k) => EF.a[(jj * EF.w + ii) * (K + 2) + k], b = k => g(i, j, k) * (1 - u) * (1 - v) + g(i + 1, j, k) * u * (1 - v) + g(i, j + 1, k) * (1 - u) * v + g(i + 1, j + 1, k) * u * v;
    let c = [0, 0, 0]; for (let k = 0; k < K; k++) { const w = b(k); c = [c[0] + EMOC[k][0] * w, c[1] + EMOC[k][1] * w, c[2] + EMOC[k][2] * w]; } return [c, b(K), b(K + 1)]; }

  /* ---------- ground texture: grass, soil, rock by slope; emotion hue at 60% ---------- */
  const TW = 1600, TH = Math.round(TW * H / W), tcv = CH.tcv || document.createElement('canvas'); if (!CH.tcv) { tcv.width = TW; tcv.height = TH; }
  if (!CH.tcv) (function paint() {
    const ctx = tcv.getContext('2d'), img = ctx.createImageData(TW, TH), px = img.data;
    const GR = [98, 108, 62], GR2 = [140, 134, 86], SO = [124, 96, 66], SO2 = [86, 68, 50], RK = [122, 118, 112], RK2 = [168, 160, 148], lum = q => 0.3 * q[0] + 0.59 * q[1] + 0.11 * q[2];
    for (let py = 0; py < TH; py++) for (let pxx = 0; pxx < TW; pxx++) {
      const x = pxx / (TW - 1) * W, y = py / (TH - 1) * H, e = W / TW * 1.5;
      const h = gH(x, y), s = Math.hypot(gH(x + e, y) - gH(x - e, y), gH(x, y + e) - gH(x, y - e)) / (2 * e);
      const lap = gH(x + 3 * e, y) + gH(x - 3 * e, y) + gH(x, y + 3 * e) + gH(x, y - 3 * e) - 4 * h;
      const n1 = fbm(x * 0.08, y * 0.08, 4), n2 = vn(x * 1.7, y * 1.7), sp = hash(pxx, py);
      const grass = mix(GR, GR2, sstep(0.35, 0.75, fbm(x * 0.05 + 9, y * 0.05, 4))), soil = mix(SO, SO2, sstep(-0.2, -0.9, h / HS) * 0.8);
      const rock = mix(RK, RK2, n2 * 0.7).map(v => v * (0.92 + 0.08 * vn(x * 0.6, y * 0.6)));
      const tR = sstep(0.55, 1.15, s + (n1 - 0.5) * 0.5), tS = sstep(0.25, 0.55, s + (n1 - 0.5) * 0.6) * (1 - tR);
      let c = mix(mix(grass, soil, tS + sstep(-0.4, -1.0, h / HS) * 0.5 * (1 - tR)), rock, tR); const kk = 0.93 + 0.14 * sp; c = c.map(v => v * kk);
      const ao = Math.max(-0.28, Math.min(0.18, -lap * 0.11)); c = c.map(v => v * (1 + ao));
      const [em, st, gap] = emoMix(x, y);
      if (gap > 0.01) c = mix(c, rock.map(v => v * (1 + ao)), gap * 0.85);
      const ls = lum(c), le = lum(em) || 1; c = mix(c, em.map(v => Math.min(255, v * ls / le * 1.05)), ALPHA * st * (1 - gap));
      const o = (py * TW + pxx) * 4; px[o] = c[0]; px[o + 1] = c[1]; px[o + 2] = c[2]; px[o + 3] = 255;
    }
    ctx.putImageData(img, 0, 0);
  })();
  CH.tcv = tcv;

  /* ---------- scene ---------- */
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.3;
  wrap.insertBefore(renderer.domElement, lbs); busy.remove();
  const scene = new THREE.Scene(); scene.background = new THREE.Color('#ffffff');
  const camera = new THREE.PerspectiveCamera(30, 1.6, 1, 5000), controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.maxPolarAngle = Math.PI * 0.47; controls.minDistance = 120; controls.maxDistance = 1400;
  scene.add(new THREE.HemisphereLight(0xffffff, 0x9a9384, 1.0));
  const sun = new THREE.DirectionalLight(0xfff6ea, 3.3); sun.position.set(-260, 260, -160); sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048); sun.shadow.bias = -0.0006; sun.shadow.normalBias = 0.6;
  Object.assign(sun.shadow.camera, { left: -260, right: 260, top: 200, bottom: -200, near: 10, far: 900 }); scene.add(sun);
  const fill = new THREE.DirectionalLight(0xffffff, 0.9); fill.position.set(120, 90, 400); scene.add(fill);
  const X = x => x - W / 2, Z = y => y - H / 2;
  const geo = new THREE.PlaneGeometry(W, H, MX - 1, MY - 1); geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position; for (let q = 0; q < MX * MY; q++) pos.setY(q, hGrid[q]); geo.computeVertexNormals();
  const tex = new THREE.CanvasTexture(tcv); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  const terrain = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95 })); terrain.castShadow = terrain.receiveShadow = true; scene.add(terrain);
  // block sides
  function wallStrip(pts) { const g = new THREE.BufferGeometry(), v = [], idx = [];
    pts.forEach(p => { v.push(X(p[0]), gH(p[0], p[1]), Z(p[1]), X(p[0]), BASE, Z(p[1])); });
    for (let k = 0; k < pts.length - 1; k++) { const a = 2 * k; idx.push(a, a + 1, a + 2, a + 2, a + 1, a + 3); }
    g.setAttribute('position', new THREE.Float32BufferAttribute(v, 3)); g.setIndex(idx); g.computeVertexNormals(); return g; }
  const sideMat = new THREE.MeshStandardMaterial({ color: 0x1d1c1a, roughness: 1, side: THREE.DoubleSide }), N = 200, ed = { s: [], n: [], w: [], e: [] };
  for (let k = 0; k <= N; k++) { const t = k / N; ed.s.push([t * W, H]); ed.n.push([W - t * W, 0]); ed.w.push([0, t * H]); ed.e.push([W, H - t * H]); }
  Object.values(ed).forEach(p => { const m = new THREE.Mesh(wallStrip(p), sideMat); m.receiveShadow = true; scene.add(m); });

  const slab = new THREE.Mesh(new THREE.BoxGeometry(W + 30, 4, H + 30), new THREE.MeshStandardMaterial({ color: 0xeeeeec, roughness: 0.9 })); slab.position.y = BASE - 2; slab.receiveShadow = true; scene.add(slab);

  /* ---------- notes, questions, goal, things to notice ---------- */
  const L = [], blk = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.6 });
  function lab(text, cls, x, y, lift, pri, ax, ay, info) { const el = document.createElement('div'); el.className = 'lb ' + cls + (info ? ' hit' : ''); el.textContent = text; lbs.appendChild(el); const o = { el, v: new THREE.Vector3(X(x), gH(x, y) + lift, Z(y)), pri, ax: ax || 0, ay: ay || 0, info }; L.push(o);
    if (info) { el.addEventListener('mouseenter', ev => { if (!pinned) showTip(o, ev); }); el.addEventListener('mouseleave', () => { if (!pinned) hideTip(); }); el.addEventListener('click', ev => { ev.stopPropagation(); pinned = pinned === o ? null : o; pinned ? showTip(o, ev) : hideTip(); }); } return o; }
  D.notes.forEach(n => { const h = gH(n.x, n.y);
    const st = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 10, 6), blk); st.position.set(X(n.x), h + 5, Z(n.y)); st.castShadow = true; scene.add(st);
    const hd = new THREE.Mesh(new THREE.SphereGeometry(2.8, 18, 12), new THREE.MeshStandardMaterial({ color: n.e == null ? 0xffffff : new THREE.Color(`rgb(${D.emo[n.e][1].join(',')})`), roughness: 0.5 }));
    hd.position.set(X(n.x), h + 11, Z(n.y)); hd.castShadow = true; scene.add(hd);
    lab('N' + n.k, 'nl', n.x, n.y, 11, 1, 6, -8, { head: 'N' + n.k + ' · ' + (n.e == null ? 'no emotion marked' : D.emo[n.e][0].toUpperCase()) + (n.q ? ' · Q.' + n.q : ''), body: n.t || '' }); });
  D.qpos.forEach(Q => { if (!Q) return; const h = gH(Q.x, Q.y), st = new THREE.Mesh(new THREE.CylinderGeometry(0.55, 0.55, 18, 6), blk); st.position.set(X(Q.x), h + 9, Z(Q.y)); st.castShadow = true; scene.add(st);
    const fl = new THREE.Mesh(new THREE.BoxGeometry(7, 4.2, 0.6), blk); fl.position.set(X(Q.x) + 3.2, h + 16.4, Z(Q.y)); fl.castShadow = true; scene.add(fl); lab('Q.' + Q.q, 'ql', Q.x, Q.y, 16.4, 2, -4, -10, { head: 'Q.' + Q.q + (Q.title ? ' · ' + Q.title : ''), body: Q.ans || 'No answer written yet.', sm: Q.n ? 'Placed at the middle of its ' + Q.n + ' note' + (Q.n > 1 ? 's' : '') + '.' : 'No notes yet; placed on the line between present and goal.' }); });
  { const s = D.START, h = gH(s.x, s.y), p = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 22, 6), blk); p.position.set(X(s.x), h + 11, Z(s.y)); p.castShadow = true; scene.add(p);
    const f = new THREE.Mesh(new THREE.BoxGeometry(0.5, 7, 11), blk); f.position.set(X(s.x), h + 18.5, Z(s.y) + 5.5); scene.add(f); }
  const ringAt = (cx, cy, r) => { const p = []; for (let k = 0; k <= 64; k++) { const a = k / 64 * Math.PI * 2, x = cx + Math.cos(a) * r, y = cy + Math.sin(a) * r; p.push(new THREE.Vector3(X(x), gH(x, y) + 0.5, Z(y))); } return p; };
  [22, 14, 6].forEach(r => { const c = new THREE.CatmullRomCurve3(ringAt(D.GOAL.x, D.GOAL.y, r), true); scene.add(new THREE.Mesh(new THREE.TubeGeometry(c, 80, 1.0, 6, true), new THREE.MeshStandardMaterial({ color: 0xffffff }))); scene.add(new THREE.Mesh(new THREE.TubeGeometry(c, 80, 0.5, 6, true), blk)); });
  { const g = D.GOAL, hh = gH(g.x, g.y), pole = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 16, 6), blk); pole.position.set(X(g.x), hh + 8, Z(g.y)); scene.add(pole);
    const st = new THREE.Mesh(new THREE.OctahedronGeometry(4), blk); st.position.set(X(g.x), hh + 17, Z(g.y)); st.castShadow = true; scene.add(st); lab('GOAL', 'pl', g.x, g.y, 18, 3, -22, -22, { head: 'GOAL', body: D.goalText || 'No goal written yet.' }); }
  { let nm = -1e9; for (let k = 0; k <= 60; k++) nm = Math.max(nm, gH(0, k / 60 * 20)); const o = lab('↑ HELP', 'side', 0, 2, 0, 4, -104, -10); o.v.set(X(-6), nm + 4, Z(2));
    const o2 = lab('↓ HINDER', 'side hd', 0, H - 2, 0, 4, -128, -10); o2.v.set(X(-6), (gH(0, H - 2) + BASE) / 2, Z(H));
    const o3 = lab('← PRESENT', 'side ax', 0, H, 0, 4, 0, 10); o3.v.set(X(0), BASE, Z(H) + 4);
    const o4 = lab('FUTURE →', 'side ax', W, H, 0, 4, -120, 10); o4.v.set(X(W), BASE, Z(H) + 4); }
  const RD = (D.read || []).map((r, i) => { const o = lab(String(i + 1), 'rdm', r.at[0], r.at[1], 21, 5, -11, -11, { head: (i + 1) + ' · ' + (r.title || ''), body: r.text || '', rd: i }); const h = gH(r.at[0], r.at[1]);
    const st = new THREE.Mesh(new THREE.CylinderGeometry(0.35, 0.35, 20, 6), blk); st.position.set(X(r.at[0]), h + 10, Z(r.at[1])); st.castShadow = true; scene.add(st);
    const bl = new THREE.Mesh(new THREE.SphereGeometry(2.6, 16, 12), blk); bl.position.set(X(r.at[0]), h + 21, Z(r.at[1])); bl.castShadow = true; scene.add(bl);
    const rim = new THREE.Mesh(new THREE.TorusGeometry(2.7, 0.35, 6, 24), new THREE.MeshStandardMaterial({ color: 0xffffff })); rim.position.copy(bl.position); scene.add(rim); o.rim = rim; return o; });

  const tip = document.createElement('div'); tip.className = 'tip'; wrap.appendChild(tip); let pinned = null;
  function showTip(o, ev) { tip.innerHTML = ''; const b = document.createElement('b'); b.textContent = o.info.head; tip.appendChild(b); const bd = String(o.info.body || ''); tip.appendChild(document.createTextNode(bd.length > 420 ? bd.slice(0, 400).replace(/\s+\S*$/, '') + '\u2026' : bd));
    if (o.info.sm) { const d = document.createElement('div'); d.className = 'sm'; d.textContent = o.info.sm; tip.appendChild(d); }
    dirty = true; tip.style.display = 'block'; const r = wrap.getBoundingClientRect(), x = (ev ? ev.clientX : r.left) - r.left, y = (ev ? ev.clientY : r.top) - r.top;
    tip.style.left = Math.max(4, Math.min(r.width - tip.offsetWidth - 4, x + 12)) + 'px'; tip.style.top = Math.max(4, y - 10 - tip.offsetHeight) + 'px';
    RD.forEach((q, k) => q.el.classList.toggle('on', k === o.info.rd)); if (D.onHL) D.onHL(o.info.rd == null ? null : o.info.rd); if (o.info.way) hoverWay(o.info.way); }
  function hideTip() { dirty = true; if (!pinned) hoverWay(null); tip.style.display = 'none'; RD.forEach(q => q.el.classList.remove('on')); if (D.onHL) D.onHL(null); }
  function nearest(ev) { const r = wrap.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top; let best = null, bd = 20;
    L.forEach(o => { if (!o.info || o.sx == null) return; const d = Math.hypot(o.sx - x, o.sy - y); if (d < bd) { bd = d; best = o; } }); return best; }
  const offClick = ev => { if (pinned && !wrap.contains(ev.target)) { pinned = null; hoverWay(null); hideTip(); } }; document.addEventListener('click', offClick, true);
  let downAt = null;
  renderer.domElement.addEventListener('pointermove', ev => { if (ev.buttons || pinned) return; const o = nearest(ev); if (o) { showTip(o, ev); return; }
    const k = wayAt(ev); hoverWay(k); if (k) { const R = D.routes.find(q => q.key === k); showTip({ info: { head: k + ' · ' + R.name, body: R.text || '' } }, ev); } else if (tip.style.display !== 'none') hideTip(); });
  renderer.domElement.addEventListener('pointerdown', ev => { downAt = [ev.clientX, ev.clientY]; });
  renderer.domElement.addEventListener('pointerup', ev => { if (!downAt || Math.hypot(ev.clientX - downAt[0], ev.clientY - downAt[1]) > 5) return; const o = nearest(ev);
    if (o) { pinned = o; showTip(o, ev); return; } const k = wayAt(ev); if (k) { const R = D.routes.find(q => q.key === k); pinned = { info: { head: k + ' · ' + R.name, body: R.text || '' } }; hoverWay(k); showTip(pinned, ev); } else { pinned = null; hoverWay(null); hideTip(); } });
  renderer.domElement.addEventListener('pointerleave', () => { if (!pinned) { hoverWay(null); if (tip.style.display !== 'none') hideTip(); } });
  const RC = { A: '#111111', B: '#f4f4f4', C: '#e0007a' }, WAYS = {}, PICK = [];
  (D.routes || []).forEach((R, ri) => {
    const pts = R.pts.filter((p, k) => k % 2 === 0 || k === R.pts.length - 1).map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 1.6 + ri * 0.4, Z(p[1])));
    if (pts.length < 2) return; const c = new THREE.CatmullRomCurve3(pts);
    const mat = new THREE.MeshStandardMaterial({ color: RC[R.key] || '#111', roughness: 0.45, emissive: R.key === 'B' ? '#ffffff' : '#000000', emissiveIntensity: R.key === 'B' ? 0.35 : 0, transparent: true });
    const tube = new THREE.Mesh(new THREE.TubeGeometry(c, 700, 1.5, 8), mat); tube.castShadow = true; scene.add(tube);
    const edge = R.key === 'B' ? new THREE.Mesh(new THREE.TubeGeometry(c, 700, 1.9, 8), new THREE.MeshStandardMaterial({ color: '#222', transparent: true, opacity: 0.9, side: THREE.BackSide })) : null; if (edge) scene.add(edge);
    const fat = new THREE.Mesh(new THREE.TubeGeometry(c, 200, 5, 6), new THREE.MeshBasicMaterial({ transparent: true, opacity: 0, depthWrite: false })); fat.userData.key = R.key; scene.add(fat); PICK.push(fat);
    const info = { head: R.key + ' · ' + R.name, body: R.text || '', way: R.key };
    const badges = [0.22, 0.58].map(f => { const p = R.pts[Math.min(R.pts.length - 1, Math.floor(R.pts.length * (f + ri * 0.06)))]; const o = lab(R.key, 'wl', p[0], p[1], 5, 6, -13, -13, info);
      o.el.style.background = RC[R.key]; o.el.style.color = R.key === 'B' ? '#111' : '#fff'; o.el.style.borderColor = R.key === 'B' ? '#111' : '#fff'; return o; });
    WAYS[R.key] = { tube, edge, badges, mat };
  });
  let selWay = null, hovWay = null;
  function showWays() { const k = hovWay || selWay; Object.keys(WAYS).forEach(q => { const w = WAYS[q], on = !k || q === k; w.mat.opacity = on ? 1 : 0.15; if (w.edge) w.edge.material.opacity = on ? 0.9 : 0.1; w.badges.forEach(b => { b.el.style.opacity = on ? 1 : 0.25; }); }); dirty = true; }
  const ray = new THREE.Raycaster(), mv = new THREE.Vector2();
  function wayAt(ev) { if (!PICK.length) return null; const r = renderer.domElement.getBoundingClientRect(); mv.set((ev.clientX - r.left) / r.width * 2 - 1, -(ev.clientY - r.top) / r.height * 2 + 1); ray.setFromCamera(mv, camera); const hit = ray.intersectObjects(PICK, false)[0]; return hit ? hit.object.userData.key : null; }
  function hoverWay(k) { if (k === hovWay) return; hovWay = k; showWays(); if (D.onWay) D.onWay(k); }
  /* ---------- legend ---------- */
  const sw = c => `rgb(${c.map(v => v | 0).join(',')})`, order = [[0, 'the highest ground'], [1, 'a ridge'], [2, 'low ground'], [3, 'lower ground'], [4, 'the lowest ground']];
  leg.innerHTML = '<b>LEGEND</b>' + order.map(([rk, t]) => { const k = RANK.indexOf(rk); return k < 0 ? '' : `<div class="r"><i style="background:${sw(EMOC[k])}"></i><span>${D.emo[k][0]}: ${t}</span></div>`; }).join('') +
    '<div class="r"><i style="background:rgb(140,135,127)"></i><span>Bare rock face: two distant emotions meet with no ridge of indifference between them, so getting across is a climb. A big move takes energy either way; most moves go through indifference.</span></div>' +
    '<div class="r"><i style="background:rgb(116,122,74)"></i><span>Plain grass, soil or rock, no color: no notes nearby, so no information here.</span></div>' +
    (D.routes && D.routes.length ? D.routes.map(R => `<div class="r"><i style="background:${RC[R.key]};border-color:#111;height:6px;margin-top:5px"></i><span><b style="display:inline;letter-spacing:0;font-size:12.5px">${R.key}</b> · ${R.name.replace(/[<>&]/g, '')}</span></div>`).join('') : '') +
    ((D.read || []).length ? '<div class="r"><i style="background:#111;border-radius:50%"></i><span>Numbered: what stands out, read below.</span></div>' : '') +
    '<div class="r"><i style="background:#111;border-radius:50%"></i><span>Pins are notes in their emotion’s color; black flags are questions. ← PRESENT and FUTURE → run along the front; ↑ HELP and ↓ HINDER run back to front.</span></div>' +
    '<div class="r"><span style="color:#666">Drag to turn, scroll or pinch to zoom. Hover or tap a note, question, the goal, a number or a way to read it.</span></div>';

  /* ---------- buttons ---------- */
  const bReset = document.createElement('button'), bFs = document.createElement('button');
  bReset.className = bFs.className = 'bt'; bReset.textContent = 'Reset view'; bFs.textContent = 'Full screen';
  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); }); if (D.card) bFs.style.display = 'none'; wrap.appendChild(bar);
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
  bReset.onclick = () => { moved = false; home(); };
  bFs.onclick = () => { const on = !wrap.classList.contains('fs'); wrap.classList.toggle('fs', on); bFs.textContent = on ? 'Close full screen' : 'Full screen'; document.documentElement.style.overflow = on ? 'hidden' : ''; size(); };
  const onKey = e => { if (e.key === 'Escape' && wrap.classList.contains('fs')) bFs.onclick(); }; document.addEventListener('keydown', onKey);

  /* ---------- sizing, labels, loop ---------- */
  let dirty = true, alive = true, lastW = 0, lastCfs = false;
  function size() { const fs = wrap.classList.contains('fs'), w = fs ? window.innerWidth : wrap.clientWidth; if (!w) return; const cfs = D.card && host.closest('.gtfs-on'), h = fs ? window.innerHeight : cfs ? Math.round(Math.max(420, window.innerHeight * 0.78)) : Math.round(Math.max(300, Math.min(D.card ? 520 : 620, w * (D.card ? 0.62 : 0.56))));
    wrap.style.height = fs ? '' : h + 'px'; renderer.setSize(w, h); camera.aspect = w / h;
    // keep the whole block in frame
    camera.fov = 30; camera.updateProjectionMatrix(); lastW = w; if (typeof home === 'function' && !moved) home(); dirty = true; }
  const ro = window.ResizeObserver ? new ResizeObserver(size) : null; if (ro) ro.observe(wrap); window.addEventListener('resize', size);
  let moved = false; controls.addEventListener('start', () => { moved = true; }); controls.addEventListener('change', () => { dirty = true; if (!pinned) tip.style.display = 'none'; });
  const v = new THREE.Vector3();
  function place() { const w = renderer.domElement.clientWidth, h = renderer.domElement.clientHeight, boxes = [];
    L.map(o => { v.copy(o.v).project(camera); o.sx = (v.x * 0.5 + 0.5) * w; o.sy = (-v.y * 0.5 + 0.5) * h; return { o, x: o.sx + o.ax, y: o.sy + o.ay, off: v.z > 1 }; })
     .sort((a, b) => b.o.pri - a.o.pri)
     .forEach(p => { if (p.off) { p.o.el.style.display = 'none'; return; } p.o.el.style.display = '';
       const bw = p.o.el.offsetWidth || 30, bh = p.o.el.offsetHeight || 16; let y = p.y;
       let x = p.x; const tries = [[0, 0], [bw * 0.7, 0], [-bw * 0.7, 0], [0, -bh - 2], [bw * 0.7, -bh - 2], [-bw * 0.7, -bh - 2]];
       for (const [dx, dy] of tries) { const hit = boxes.some(b => p.x + dx < b[0] + b[2] && p.x + dx + bw > b[0] && p.y + dy < b[1] + b[3] && p.y + dy + bh > b[1]); x = p.x + dx; y = p.y + dy; if (!hit) break; }
       x = Math.max(2, Math.min(w - bw - 2, x)); boxes.push([x, y, bw, bh]); p.o.el.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px)`; }); }
  function loop() { if (!alive) return; if (!host.isConnected) { dispose(); return; } controls.update();
    if (dirty && wrap.clientWidth) { RD.forEach(o => o.rim && o.rim.quaternion.copy(camera.quaternion)); if ((wrap.clientWidth !== lastW || !!(D.card && host.closest('.gtfs-on')) !== lastCfs) && !wrap.classList.contains('fs')) { lastCfs = !!(D.card && host.closest('.gtfs-on')); size(); } renderer.render(scene, camera); place(); dirty = false; } requestAnimationFrame(loop); }
  function dispose() { if (!alive) return; alive = false; if (ro) ro.disconnect(); window.removeEventListener('resize', size); document.removeEventListener('keydown', onKey); document.removeEventListener('click', offClick, true); renderer.dispose(); try { renderer.forceContextLoss(); } catch (e) {} }
  size(); home(); loop();
  return { hl(i) { if (!pinned) RD.forEach((o, k) => o.el.classList.toggle('on', k === i)); }, setWay(k) { if (k !== selWay) { selWay = k; showWays(); } }, hoverWay(k) { hoverWay(k); },
    snap() { renderer.render(scene, camera); return renderer.domElement.toDataURL('image/jpeg', 0.85); }, height() { return wrap.offsetHeight; }, dispose };
}

window.gsmRelief = { mount, version: 'r1' };
