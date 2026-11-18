# v204 update (2026-11-18)

Read against his 11-18 workbook (`bear-canyon-workbook-2026-11-18.json`, 35 notes; it adds N32–N35, all aggression, all on the help side). Patch: `tools/patches/v204_ground_wording.py` (engine only).

## What his new notes do on Taking Action (v202, confirmed on his workbook)
Each patch of aggression among acceptance now forms its own strategy card: N32 and N33 together, N34, and N35.

## What v204 changes
1. **Ground cards no longer decide what the emotion is aimed at.** v202 said the aggression "stands in the goal's way". He places these notes on the help side on purpose: N32 is aggression toward full suppression where it isn't warranted, and N34 is the push for good fire. The card now says "You placed it where things help the goal. Keep it working for the goal without letting the aggression spread into the acceptance around it (…)". The reason reads "acceptance and aggression side by side is a high-risk mix, whatever the aggression is aimed at: aggression can tip toward defiance, the most severe emotion (Vigneaux, 2026)". The second first move asks what the emotion is aimed at, and whom it reaches.
2. **The line under FIRST MOVES for a way names the emotions** ("meets aggression, distrust, or defiance at N34 and N35") instead of calling them "what resists the goal".
3. **Up to three ground cards** (was two), so N35 gets its card.

## Wording that is Claude's (flagged)
All of the above.

## Not a code problem
The failed deploy he saw (11-18, build 861bf89, v201) was GitHub Pages returning 502 Server Error. The next deploys succeeded, and the preview carries every version.

## Tests
- `tests/matrix.py` on his 11-18 workbook, 11-13, Broadview, clinic, 200 notes, hostile, legacy, and empty: no page errors, no script injection.
- `tests/switch.py` and `tests/waymoves.py` on his 11-18 workbook.
- `grep -c 'AAPK\|AIza'` = 0.
