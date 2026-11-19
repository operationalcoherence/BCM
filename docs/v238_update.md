# v238 (preview only) — 2026-11-19

F1, item 1. His call (11-19 10:05): "i dont want any modifications made to the line map and its visuals - its perfect. I am open to the place mapping."

1. **YOUR PLACE IN 3D.** Before, a workbook with any written note on the line map never showed its place map in 3D, so its place notes were left off every 3D view. Now, when both maps have notes, Pattern Analysis (under YOUR LANDSCAPE, ONE QUESTION AT A TIME) and Pattern Synthesis (under the 3D view) each get a closed fold, YOUR PLACE IN 3D. Opening it builds the place ground: Esri imagery on the real terrain, notes as pins, areas as patches, and the goal at the location. It's the same view a place-only workbook already gets. Nothing is built until the fold is opened.
   - Intro line (Claude's wording): "The notes you placed on the place map, at [place name], on the real land. The ground is the real terrain, true to scale; emotion shows only as color."
2. **Place notes are P1, P2, and so on inside the fold.** The line map keeps N1, N2, and so on. The terrain module now carries one prefix (`NP`), which is "N" for every existing view and "P" only in the fold. The 3D labels read `D.np`, which is set only in the fold.

**The line map is untouched.** `gsmData()` is unchanged, so every line-map view, reading, card, and way is built from the same data as v237.

**How it works:** `gsmPlaceView(force)`; `window.gsmPlaceData()` returns the place data only when both maps have notes; `window.gsmPlaceFold()` writes the fold; a `toggle` listener puts a `.gterr-host[data-an][data-pl]` in the fold on first open; `scan()` mounts it with `gsmPlaceData()` and `pl`. It mounts in Analysis mode, so it never takes over `gsmSynRel` (the Synthesis line-map view keeps the In Parallel lines).

**Checked:**
- All four reading tabs (Analysis, Synthesis, In Parallel, Taking Action), with every fold open, on 12 workbooks (mkwb, plus a clinic workbook with a five-note place map, `wb_clinic_place.json`, built inline): text identical to v237, except the fold heading on the two both-maps workbooks.
- With the 3D loaded: the fold mounts on both tabs, the place legend shows, labels read P1 to P5, the Synthesis line-map view stays the main view, and there are no page errors. Matrix clean. Keys: none.

**Not checked:** real imagery and elevation (the sandbox can't reach Esri or AWS). Look at it on the preview with a both-maps workbook.

**Next:** v239, bare rock on place maps, shown as color (his yes, 11-19 10:06).
