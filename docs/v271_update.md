# v271 · In Parallel retired; what's worth keeping moves to Pattern Analysis

His call, 25 Nov 2026 12:08: "let us remove In Parallel. But first, let us move anything from In Parallel to analysis that is worth keeping." Since v269, both of In Parallel's two pictures already lived on Pattern Analysis, so the separate tab only repeated that comparison. The tab as it was is archived in `docs/archive/in_parallel_v270/`.

## What changed
- **No In Parallel tab.** The tabs are Start Here, Mapping Context, Mapping Landscape, Pattern Analysis, and Taking Action. A saved In Parallel tab opens Pattern Analysis.
- **New section on Pattern Analysis, YOUR WORDS ON THE GROUND**, right after THE LAY OF THE LAND (or at the end of Analysis when there is no 3D):
  - the agreement figure (words in a column, lines to their notes on the ground; solid black = the ground agrees, dashed red = the ground raises a question). Tapping a word still draws its lines on the 3D map above it. The column is labelled YOUR WORDS.
  - "Where to start."
  - WORTH A SECOND LOOK: PLACED ONE WAY, TIED THE OTHER; THE HIDDEN CHANNELS; TWO PEOPLE, TWO SIDES; and the rest under "More patterns" (e.g. NEVER IN THE SAME PLACE), each with its own wording, which Analysis's meaning pass leaves alone.
- **Dropped, because Analysis already says it:** ONE IDEA UNDER TWO NAMES (THE SAME THING?), the Emotion, Closest and farthest, and Voices readings (WHAT HOLDS THE SITUATION IN PLACE, WHERE IT CAN CROSS, RUNS TOGETHER, the one-voice lead), MORE FROM BOTH PICTURES, THE EARLIER 3D VIEW, and the no-notes fallback figures (AROUND THE GOAL, HOW IT HANGS TOGETHER).
- **Taking Action is unchanged.** WHERE THE READING SPLITS still reads every split, ONE IDEA UNDER TWO NAMES included; its wording now says Pattern Analysis found them.
- **Parts renumbered:** 1 · LOOKING IN, 2 · COURSES OF ACTION. The PDF's part 2 is Taking Action.
- Wording that named In Parallel or "both pictures" now names the ground, Patterns, or Pattern Analysis.

## Checks
- `matrix.py` on w18, clinic, cause, big, questions, places_names, empty, goal-only, one, hostile, legacy, same: no page errors, no injection.
- Analysis plus In Parallel together are shorter: w18 3,344 → 2,865 words; clinic 2,520 → 2,138; big 3,068 → 2,669.
- `agree.py`: the figure is on Analysis, and tapping "good fire" draws 8 line segments on THE LAY OF THE LAND.

## Not done (Claude's calls, for him to redirect)
- Analysis still has two 3D maps (YOUR LANDSCAPE near the top, THE LAY OF THE LAND at the end).
- TWO PEOPLE, TWO SIDES can read oddly when both groups carry the same emotion ("…it carries aggression; in the notes from Other wildfire professionals, aggression."). That wording is from before this version.
