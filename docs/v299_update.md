# v299 — no vague Taking Action titles on place maps

His handoff, 26 Nov 2026 07:00: fix Broadview's two vague titles.

Cause: the titles for "what holds the situation" and "the opportunity" are built from the card's notes, but the
helper only read line notes ("note 5"). On a place map the ids are P5, so it found nothing and fell back to the
generic title.

Fix (gsm-readable.js, gsmTAGists and gsmTAAction):
- Place notes are read too, labelled the way the page labels them (N5; "N5, line" / "N5, place" when a workbook has both maps).
- WHAT HOLDS THE SITUATION IN PLACE now names the part its first move starts with:
  "Change what keeps “plainly uninterested” (N1) in place".

Broadview:
- "Change what holds the situation in place" → "Change what keeps “plainly uninterested” (N1) in place"
- "Scale the alternative that already exists" → "Scale what already works, starting with property owner removed beetle-killed trees by themselves (N5), and 3 more"

Checks: tests/vague_titles.py passes on Broadview, w20, and the made-up workbooks. Every other title is unchanged from
v298 except wb_places_names, which now counts its place note too ("…(N2, line), and 1 more"). No page errors.
