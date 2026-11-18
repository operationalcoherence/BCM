# v218 update (2026-11-18)

His note (15:13): the pattern buttons "shouldn't disappear in full screen." Patch: `tools/patches/v218_fs_patterns.py` (engine, and the relief with `--relief`).

## What changes
Full screen on the Pattern Synthesis 3D carries the patterns row into the map, at the top left, clear of the legend drawer and the Play button. Closing full screen puts it back above the map. Tapping a pattern there draws it on the map as before. The row hides while the tour plays, so it doesn't crowd the captions, and comes back when the tour ends or pauses.

How: the relief calls `D.onFs(on, wrap)` when full screen opens or closes, and the engine moves the row into the map and back (`.fslay`). The relief tags the map `.touring` while the tour runs.

## Tests
- On 11-18 with the 3D: in full screen the row is inside the map (top left, 9 buttons); tapping "good fire" draws its loop; during the tour the row is hidden; after closing full screen it is back above the map. Screenshot checked.
- `tests/tour.py` on 11-18: unchanged behavior (full screen on Play, pause, resume, Escape ends, caption clears the legend); no page errors.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors. Builds reproduce; keys grep 0.
