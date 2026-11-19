# v229: the way readings move to Evidence

2026-11-18. Patch: `tools/patches/v229_way_readings_evidence.py`.

His 21:46 "do it": the item v228 left open.

- **What moved:** the written readings the 3D adds to a card. On strategies: A/B/C why choose it, comparing the ways, why take the harder way, moves in order, and when to stop and readjust. On programs: what the ground says about it.
- **Where they go now:** the card's **Evidence**, under **HOW THE WAYS READ ON THE GROUND**.
- **What stays in "Why this action":** the map, the way buttons, and the chart, with one line pointing to the readings.
- **In full screen** the readings stay with the map, as before.
- **How:** the terrain module's `fillCourseBox()` writes the readings into `.taev > .taways` when the card is layered. It creates Evidence if the card has none, and refills it whenever the way changes.
- **The ground's own numbered readings** were already hidden on cards; they are unchanged.

Checked:
- With every card open on 11-18, each card's readings sit in Evidence and its chart in Why this action, with no page errors.
- `ta_flow.py` passes on 11-18 and Broadview; `matrix.py` shows no errors; the key check is 0.

Wording is Claude's: "HOW THE WAYS READ ON THE GROUND", "Read with the map and chart under Why this action: each letter is a way drawn there."
