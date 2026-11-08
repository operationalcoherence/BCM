# Bear Canyon Method v101 (preview) - update

Written 2026-11-08. Follows v100. Corrects a claim in `v100_update.md`.

## What changed

**The place map's note hover now appears at all.** One guard added to a
document-level listener.

v100 added the author's name to the hover heading and the update doc said it
worked the same on the line map and the place map, because both call the same
function (`tt`). The first half was right and the second was wrong in effect:
on the place map the heading was built correctly and then wiped about a
millisecond later, so nothing was ever visible.

The cause: `document.addEventListener("mouseover", ...)` resolves the target
with `at()`, which only matches note and question references
(`a.ref`, `[data-hid]`, `circle[data-ref]`). A Leaflet marker matches none of
them, so `at()` returned null and the listener called `Z(null)`, hiding the
tooltip. The marker's own handler fires first, further down the bubble path, so
it set the tooltip and the document listener cleared it.

The line map escaped this because its figure also has a `pointermove` handler
that re-shows the tooltip on the next cursor movement. The place map has no
equivalent, so the tooltip stayed hidden.

Fix: the document listener no longer clears the tooltip when the pointer is
inside a `.leaflet-marker-icon`. Reference tooltips, the goal tooltip and the
line map are untouched — only the "nothing here, clear it" branch changed.

This was a pre-existing bug, not something v100 introduced. Place-map note
hovers have never worked.

## Verified

Leaflet was served to the test harness from a local copy (`node_modules`), so
the place map renders for the first time in testing. Tiles are still blocked;
markers do not need them.

- Broadview (place map, 14 notes), name typed as Greg: markers read
  `N1 · Q2 opposition · Greg`, and so on.
- Broadview exactly as saved, where no name has been typed: markers read
  `N1 · Q2 opposition`, with no trailing separator.
- Real workbook (line map), two notes given a second author: `N1`/`N6` read
  Greg, `N2`/`N4` read Sam. Unchanged from v100.
- Both workbooks, all reading tabs, every fold open: no page errors.
- Key check: `grep -c 'AAPK\|AIza'` is 0 in both files.

## Still not verified

- Touch devices, where hover does not exist.
- A real combine of two workbooks. Both tests write the second author into the
  file rather than combining.

## Note for the next session

`tests/placehover.py` is how the place map was tested: it routes the Leaflet
CDN URLs to a local copy and hovers each marker. The handoff's standing
instruction to run a place-map workbook every time can now be followed for
anything hover-related, not just page rendering.

## Wording

No new on-screen wording.
