# v301: Broadview visual checks (v293 to v300)

Handoff item, 26 Nov 2026: Broadview visual checks on v293 to v300. Pattern Analysis and Taking Action at desktop and
phone width, every fold open, the 3D loaded. No page errors and nothing wider than the phone screen before or after.
Patch: tools/patches/v301_place_ground_words.py.

Found and fixed:

1. **Garbled loading text, every workbook.** A card map that was still loading read "Building the land" plus a broken
   character: a CSS escape lost its backslash inside the JS string. Now "Building the land…".
2. **Red, underlined story text, every workbook.** Opening "Your story in greater detail" or "The whole workbook read
   as one story" showed the text underlined, the second in dark red: the style for small "read more" links also caught
   these folds. They now read as plain text.
3. **Ground words on a place-only workbook.** v300 fixed the cards; these were left:
   - THE BARE LANDSCAPE: "the ridge of indifference… The ridge holds" → "indifference… Indifference holds";
     "Your plans sit on higher ground" → "Your plans carry less resistance".
   - THE OPPORTUNITY: "the high ground of acceptance" → "already stands in acceptance, the emotion with the most promise".
   - YOUR LANDSCAPE, WHAT THIS SUGGESTS: "The high ground / The lowest ground belongs to" → "Acceptance / Aggression and
     defiance belong mostly to"; "N3 carries indifference: the ridge" → "the step most moves pass through".
   - Its legend: emotion names only, and no bare rock row (his rule: no bare rock on place maps).
   - Taking Action summary and the story's "On Taking Action" line: "stands on high ground" → "already stands in
     acceptance"; "through the ridge" → "through indifference"; "Most shifts happen on the ridge of indifference" →
     "Most shifts pass through indifference".
4. **Double period, every workbook.** DOES THIS ANSWER THE GOAL? read `“Perceptions of wildfire risk.”.`; the quote now
   drops its own final period.

While fixing 3, the terrain block (a separate scope) could not see the place-only check, and the error was swallowed:
the bare landscape went blank and AT A GLANCE lost WHAT THE SYSTEM IS DOING. Caught by diffing against v300 before
shipping; the check is now shared with that block.

Checks: Broadview text diff against v300 shows only the lines above. w20, wb_cause, wb_clinic, wb_places_names (both
maps): Pattern Analysis identical; Taking Action identical except the double-period fix. No page errors at 1200 or 420
wide.
