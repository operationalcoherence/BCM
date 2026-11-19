# v233: tap the ground on YOUR LANDSCAPE to read what gathers there (plan item 3c)

Phase 3, item 3c (his go-ahead, 11-19 07:08). Decision E6 from the review plan: clicking the map with no question selected says what's concentrated there.

## What it does
On Pattern Analysis, YOUR LANDSCAPE, ONE QUESTION AT A TIME, with **All notes** shown, a tap on bare ground pins a box headed WHAT GATHERS HERE. A tap on a note, a question, or a number does what it did before, and so does any tap with a question selected.

The box reads the spot (all of it is Claude's wording):
- How many notes shape the ground there, and which questions they come from. The reach is 2.2 × the terrain's sigma, which is how far a note's color shows, so the reading agrees with the color under the tap. If none sits close, it says "though none sits right on this spot".
- Which side of the line it's on (help or hinder), and whether it's near the present, midway, or near the goal.
- The emotion that colors it, weighted by distance as the ground's color is, and what kind of ground that makes. In the paper's order: acceptance is the highest ground, indifference the ridge, distrust low ground, aggression lower ground, and defiance the lowest ground. Nearly equal shares are named together.
- Where acceptance meets aggression, defiance, or distrust with no indifference between them: "getting across is a climb" (the bare rock face, consistent with the paper). Where indifference is present but doesn't lead: it's a ridge most moves cross.
- How what you would design (Q.5–Q.7) relates to the context you have grasped (Q.1–Q.4) on that ground:
  - Both on hard ground: it meets these emotions first.
  - Both on high ground: a place where it can be seen to work.
  - Both on the ridge: people can still tip either way.
  - Only context on hard ground: what holds here is unresolved.
  - Only context on high ground: nothing yet uses it.
  - Only design: nothing of the context nearby to test it against.
- Under that: up to four of the nearest notes, with their emotion and opening words.
- Bare ground with no notes in reach: "the ground here carries no information yet" (his plain-ground rule).

The line under the map now ends: "With all notes shown, tap the ground to read what gathers there."

## How
- Engine: `ANGROUND(x, y)` inside the Analysis block of the terrain module. The 3D relief asks for it through `D.onGround` (Analysis only, not In Parallel). The flat fallback finds the nearest grid point from the projected vertices (`SXA`/`SYA`), and `GPIN` keeps the box open until the pointer moves away.
- Relief: `groundAt(ev)` raycasts onto the ground mesh and returns the engine's own coordinates. The tip allows longer text for this box (`info.long`).

## Checked
- `tests/groundtap.py` (new), with the 3D and then without WebGL. On 11-18 it passed with 5 of 9 3D taps and 6 of 9 flat taps reading the ground (the rest landed on notes or numbers). It also checks: a question selected turns the reading off, All notes turns it back on, the line under the map, no "feeling", and no page errors. It passed on clinic and hostile. On the 200-note workbook most taps land on a note, as they should.
- `tour_an.py` on 11-18: the tour plays and ends, and End tour closes full screen. `matrix.py` on 11-18, Broadview, and every mkwb workbook: no errors. The key check is 0 on both built files.

Patch: tools/patches/v233_ground_click.py (engine and relief).
