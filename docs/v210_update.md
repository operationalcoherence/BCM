# v210 update (2026-11-18)

His notes on the v209 tour: make it go full screen on Play; introduce bare rock and transitions (their cost and feasibility); make Pause/Play easier to find; make the caption box and text bigger; edit WHAT THE GROUND SAYS as the tour shows it; and should Analysis have its own tour? Patch: `tools/patches/v210_tour_read.py`, run on the engine and, with `--relief`, on `tools/relief/relief.js`.

## Decided: two tours, different jobs
Pattern Analysis is where people first meet the 3D, so it gets a short tour of how to read the map, on their own notes. Pattern Synthesis keeps the tour of the ground in his four acts, opened by two stops on reading the ground. Moving the one tour to Analysis would put the reading of the ground ahead of the page it belongs to. He can redirect this.

## What changes
1. **Full screen on Play.** Play takes the map full screen; the tour's end, End tour, or Escape brings it back (only if Play opened it).
2. **One large button** at the bottom center of the map: ▶ Play the tour, then ❚❚ Pause, then ▶ Play. End tour sits beside it while the tour runs. It stays centered on the map, clear of the full-screen legend.
3. **Larger caption:** 17 px text and a 20 px title (were 12.5 px), in a wider box with a shadow. Each stop is held as long as its caption takes to read (3.3 words a second, 2.4 to 6 s), so the Synthesis tour now runs about 1.5 minutes on 11-18 (was about 30 s). Pause is right there.
4. **READING THE GROUND opens the Synthesis tour:** what color and height mean (the order in Vigneaux, 2026); what a move costs (climbing far more than falling; more the farther apart the emotions are; most moves go through indifference); which moves are feasible now (from acceptance and indifference, change can start now; from distrust, aggression, and defiance, it is unlikely in the short or medium term, after Vigneaux, 2026); and what gray bare rock is.
5. **Bare rock gets its own reading** under BETWEEN THEM, at the largest rock face (found with the same rule the 3D uses to lay the rock): which emotions meet there, how many steps apart they are, that the climb up is the hard one, that the feasible way goes around through indifference (it names the nearest indifference note), and what share of the colored ground is bare rock. When the largest face is the pair already read under "Where it is easiest to fall from", that reading says the ground between them is bare rock instead. On 11-18 the rock reading is N5 (acceptance) against N9 (defiance) by the goal. WHAT THE GROUND SAYS can now hold 13 readings (was 12).
6. **WHAT THE GROUND SAYS, edited:** readings start with what the ground does, not with a list of notes:
   - Low ground: "32% of the ground slopes down into this hollow of distrust, defiance, and aggression, around N16, N18, N19, N20, and N25." (was "N16, N18, N19, N20, N25. About 32% of the ground slopes down into here.")
   - High ground: "High ground of acceptance around N6, N7, and N11." (was "N6, N7, N11.")
   - Phrases: the reading comes first. "Until you answer the question below, N15 counts as supporting it." moves to the end; it said "standing for it," which the buttons stopped saying in v198.
   - The loop: "N14 and N30 name what leads to suppression, and Q.1 names what suppression leads to in turn." (was "… leads on to something else.")
7. **The Pattern Analysis tour** (about 45 s): how to read this ground; the high ground (the highest acceptance note); the ridge (the indifference notes); bare rock (the largest face); the deepest ground; and what a move costs. On place maps it says the ground is the real terrain and gives the cost of a move.
8. **Fixes found on the way:** labels of things out of the frame were stacking along its edges during the tour; they now hide. Escape in full screen left the button saying "Close full screen" and threw a page error (the engine's own Escape handler took the full-screen class off the 3D map); the engine's handler now skips the 3D map, and the button always follows the real state.

## Wording that is Claude's (flagged)
All of item 4 and item 7, the bare rock reading (item 5), the rewrites in item 6, "End tour", and the tooltip "Escape also ends the tour". The feasibility sentence paraphrases his paper ("Building resilience in the short or medium term for the emotions of aggression, distrust, and defiance is likely not possible"); he should check it says what he means.

## Tests
- `tests/tour.py` with the 3D: Play opens full screen and the end closes it; the button is 179 × 46 px, centered on the map; every reading visited in order after the two opening stops (11-18: 15 stops, about 1.5 min; clinic: 12; Broadview: 10); a click pauses and the caption holds; Play resumes; Escape ends; the full-screen caption clears the legend; no page errors. Screenshots checked.
- `tests/tour_an.py` (new) with the 3D on 11-18, clinic, and Broadview: the Analysis tour plays its stops and End tour ends it and closes full screen; no page errors.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors.
- `tests/waymoves.py` on 11-18 with the 3D: cards unchanged.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0 in both files.
