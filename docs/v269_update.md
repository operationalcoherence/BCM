# v269 · Pattern Synthesis retired

His decision 11-25 08:35–08:41 (`claude/pattern_synthesis_retired_2026-11-25.md` in the Claude project). Ackoff: analysis looks inward at structure; synthesis explains a thing by its role in a larger system it is part of. Nothing the engine reads without reading meaning is outside the situation, so the engine cannot do synthesis. The page's sections were analysis. Plus his note 08:46: WHAT THE GROUND SAYS "might be worth keeping, as a story, not a list".

## What changed
- **No Pattern Synthesis tab.** The tabs are Start Here, Mapping Context, Mapping Landscape, Pattern Analysis, In Parallel, Taking Action. A saved tab 3 opens Pattern Analysis.
- **Moved to the end of Pattern Analysis**, in their old order: THE LAY OF THE LAND (the 3D ground, WHAT THE GROUND SAYS, the tour, the patterns row, the legend, PATTERNS THAT RUN THROUGH IT), CAUSE AND EFFECT, NOW AND LATER, SCALE, ONE JUDGEMENT TWICE, IN YOUR ANSWERS, NOT ON THE MAP, OPEN QUESTIONS, WHAT IT RESTS ON, and WHAT YOU LINKED (each where the workbook has one).
- **Moved to Taking Action:** DOES THIS SERVE THE GOAL?, before MORE INFORMATION NEEDED. Saved answers (`goal|<id>`) unchanged.
- **Dropped:** HOW THIS MAP IS MADE, the graph blocks (WHAT CHANGED WHAT and the shape block), ABOUT WHAT YOU COLLECTED's text, WHAT IT MIGHT MEAN, WHAT TO PAY ATTENTION TO, and the "Put the two pictures together" card. The hidden old figure that In Parallel reads stays.
- **WHAT THE GROUND SAYS reads as a story**: one paragraph each for the high ground, the low ground, between them, and what keeps it this way, written from the same readings, with no note numbers. The numbered readings fold under it (THE READINGS, ONE BY ONE), because the numbers on the 3D map point to them. Main map only. Place maps get the same story from their own readings.
- **Parts renumbered:** 1 · LOOKING IN, 2 · THE TWO PICTURES TOGETHER, 3 · COURSES OF ACTION. The PDF's part 2 heading now says In Parallel (it said Pattern Synthesis), and part 3 says Taking Action (it already did, wrongly, for In Parallel).
- **Wording that pointed at Pattern Synthesis** now points at Pattern Analysis (Start here, the Mapping Landscape steps, In Parallel's figure and buttons, Taking Action's lines, WHAT YOU DID). The Synthesis instruction drop-down is gone; its paragraph on working with others joins the Analysis one. In Parallel's figure labels its lower half THE GROUND.
- In Parallel's "See it on the 3D map" scrolls to the ground on Pattern Analysis, and draws its lines there.

## Build
The graph modules (`tools/graph/`) are no longer bundled or called. Back to the one-file build:

    npx esbuild@0.24 gsm-readable.js --minify --outfile=gsm-preview.js

## Checks
- `matrix.py` on clinic, cause, big, questions, places_names, empty, goal-only, one, hostile, legacy, same: no page errors, no injection.
- Analysis plus what moved reads about 200 words shorter than Analysis and Synthesis did together (clinic 1,838 against 2,043).
- `agree.py` (In Parallel tap draws on the ground on Analysis), `tour.py` (the tour on the moved 3D).

## Not done (Claude's calls, for him to redirect)
- Pattern Analysis now has two 3D maps: YOUR LANDSCAPE, ONE QUESTION AT A TIME near the top and THE LAY OF THE LAND at the end. Merging them is the obvious next cut.
- The story is rule-written from the readings; the wording is Claude's (flagged for his end pass).
