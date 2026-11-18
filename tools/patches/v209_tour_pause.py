"""v209: his notes on the tour (11-18).
1. Full screen: the legend drawer covered the caption. The caption now sits to the right of the drawer, as the
   labels and the map already do.
2. Pause and play instead of stop: the button reads Play the tour, then Pause, then Play. While paused the map
   can be turned and zoomed; Play flies back to the same stop and carries on. Reset view or Escape ends the tour;
   a click anywhere on the map (its labels included) pauses it.
3. Each stop sits nearer the middle of the frame (less empty sky in full screen).
5. No hover boxes while the tour plays; in full screen, hover boxes stay clear of the legend drawer.
6. A little slower: about 30 seconds for 12 stops (was 25), so each caption can be read.
Usage: python3 v209_tour_pause.py tools/relief/relief.js --relief   and   python3 v209_tour_pause.py gsm-readable.js"""
import sys

P = sys.argv[1]
RELIEF = "--relief" in sys.argv
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


if RELIEF:
    # 1: the caption clears the legend drawer in full screen
    rep(
        "lbs.style.left = pad + 'px'; attr.style.left = pad + 6 + 'px';",
        "lbs.style.left = pad + 'px'; attr.style.left = pad + 6 + 'px'; if (typeof cap !== 'undefined') cap.style.left = pad + 12 + 'px';",
    )
    # 2 + 3: pause and play
    rep(
        "  function stopTour() { if (!TOUR) return; TOUR = null; controls.enabled = true; cap.style.display = 'none'; bPlay.textContent = 'Play the tour';",
        "  function stopTour() { if (!TOUR) return; TOUR = null; controls.enabled = true; cap.style.display = 'none'; bPlay.textContent = 'Play the tour'; bPlay.title = '';",
    )
    rep(
        "  function startTour() { if (TOUR) return stopTour();",
        """  function pauseTour() { const T = TOUR; if (!T || T.paused != null) return; T.paused = (performance.now() - T.start) / 1000; controls.enabled = true; bPlay.textContent = 'Play'; dirty = true; }
  function resumeTour() { const T = TOUR; if (!T || T.paused == null) return; let l = T.legs[0]; for (const x of T.legs) if (T.paused >= x.t0) l = x;
    /* fly back from wherever the map was turned to, to the same stop, and carry on */
    l.a = [camera.position.clone(), controls.target.clone()]; T.start = performance.now() - l.t0 * 1000; T.paused = null; controls.enabled = false; bPlay.textContent = 'Pause'; pinned = null; hideTip(); dirty = true; }
  function startTour() { if (TOUR) return TOUR.paused != null ? resumeTour() : pauseTour();""",
    )
    rep(
        "const lk = t.clone().add(new THREE.Vector3(0, d * 0.16, 0));",
        "const lk = t.clone().add(new THREE.Vector3(0, d * 0.08, 0));",
    )
    rep(
        "per = Math.max(1.6, Math.min(2.6, 25 / n)) * SL,",
        "per = Math.max(1.8, Math.min(2.8, 30 / n)) * SL,",
    )
    rep(
        "TOUR = { legs, start: performance.now(), total: t0, cur: -2 }; controls.enabled = false; cap.style.display = 'block'; bPlay.textContent = 'Stop'; dirty = true; }",
        "TOUR = { legs, start: performance.now(), total: t0, cur: -2, paused: null }; controls.enabled = false; cap.style.display = 'block'; bPlay.textContent = 'Pause'; bPlay.title = 'Reset view or Escape ends the tour'; pinned = null; hideTip(); dirty = true; }",
    )
    rep(
        "  function stepTour(now) { const T = TOUR, s = (now - T.start) / 1000; if (s >= T.total) { stopTour(); return; }",
        "  function stepTour(now) { const T = TOUR; if (T.paused != null) { controls.update(); return; } const s = (now - T.start) / 1000; if (s >= T.total) { stopTour(); return; }",
    )
    rep(
        "  renderer.domElement.addEventListener('pointerdown', () => { if (TOUR) stopTour(); });",
        "  wrap.addEventListener('pointerdown', e => { if (TOUR && !(e.target.closest && e.target.closest('.bt,.grfs'))) pauseTour(); });",
    )
    rep(
        "  return { loops, focusQ, tour: startTour, touring() { return !!TOUR; }, hl(i) {",
        "  return { loops, focusQ, tour: startTour, touring() { return !!TOUR; }, paused() { return !!TOUR && TOUR.paused != null; }, hl(i) {",
    )
    # 5: no hover boxes while the tour plays; in full screen they stay clear of the legend drawer
    rep(
        "  function showTip(o, ev) { tip.innerHTML = '';",
        "  function showTip(o, ev) { if (TOUR && TOUR.paused == null) return; tip.innerHTML = '';",
    )
    rep(
        "tip.style.left = Math.max(4, Math.min(r.width - tip.offsetWidth - 4, x + 12)) + 'px';",
        "tip.style.left = Math.max(4 + (parseFloat(lbs.style.left) || 0), Math.min(r.width - tip.offsetWidth - 4, x + 12)) + 'px';",
    )
else:
    s = s.replace('t.textContent = "v208"', 't.textContent = "v209"')
    assert 't.textContent = "v209"' in s
open(P, "w").write(s)
