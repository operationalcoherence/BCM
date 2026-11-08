# Bear Canyon Method v100 (preview) - update

Written 2026-11-08. Supersedes nothing; follows v99.

## What changed

One change. Hovering a symbol on the map in Mapping Change now shows who made it, at the end of the heading:

    N2 · Q2 opposition · Sam

- Works the same on the line map and the place map: both use the same tooltip function (tt).
- The name is the note's author. A note with no author (every note in a workbook saved before combining) shows the workbook owner's name instead.
- Notes that Patterns refers to by name (the note references with the dotted underline) use the same tooltip, so they show the name too.
- If no one has typed a name, nothing is added.

The version label reads v100.

## Verified

Your 2026-11-07 workbook on the line map, with two notes given a second author: N1 and N6 read "Greg", N2 and N4 read "Sam". All tabs render with no page errors. Key check: grep 'AAPK\|AIza' returns 0 in both files.

## Not verified

- Place-map hover: Leaflet tiles are blocked in the test harness. It uses the same function, but it was not seen.
- A real combine of two workbooks (tested with authors written into the file).
- Touch devices (hover does not exist there).

## Wording

No new on-screen wording. Only a name appended to the heading.

## Files

gsm-preview.js and gsm-readable.js (regenerated with prettier). Not pushed.
