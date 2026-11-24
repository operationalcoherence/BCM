# v259 · Taking Action: walk a way, step by step

His ask 11-24 12:39: "not being able to trace where nonlinear strategies go and in what order." Queue item: "VIZ: entangled strategies are unreadable" (added 11-21 09:28). Numbers and arrows were tried and were not enough.

## Claude's call
Of the queued options, two together: step through the way one leg at a time with the rest dimmed, and the way as an ordered list tied to its places. Lines alone can't be followed when a way crosses itself, so the reader no longer has to trace them.

## What it does
- A **Walk way A, step by step** button sits beside Reset view on any card map whose way has stops (it follows the way chosen under Show; "All ways" walks A).
- Each step shows only: where the way has been (thin), the leg it is on now (bright yellow, with an arrow), and a ring on the stop it is heading to. That note's label lights up. Every other line is dimmed.
- The caption says WAY A · STEP 3 OF 20, "From N5 to N29", and the emotion and text of the note it is heading to (the goal's text on the last step).
- A strip lists every stop in order: PRESENT › N6 + N4 › N5 › … › GOAL. Done stops are outlined, the current leg is black and yellow, and the rest are gray. Tap any stop to jump there.
- Back, Next, and the arrow keys step through it. Done, Stop walking, or Escape end it.
- Two notes at the same spot are named together (N6 + N4) instead of one hiding the other.
- The caption moves to whichever corner keeps it off the leg it describes, and checks again after the view is turned.
- On a card shown in the page, the walk opens the card's full screen (as the tour does) and closes it again when the walk ends.

## What did not change
The ways themselves, their order, their scores, the recommendations, and all wording outside the walk. Presentation only. Applies to every workbook's strategy and program cards.

## Checked
tests/walk.py (new): 11-20 card 0 (20 steps, full screen) and card 3 (4 steps, from the page), clinic: Next, Back, arrow keys, strip taps, Done, Escape, the card full screen opening and closing; no page errors. tour.py, ta_flow.py (ALL PASS), waymoves.py, and matrix.py (11-20, Broadview, clinic, big, empty): no errors.

## Files
tools/patches/v259_walk_the_way.py (tools/relief/relief.js; the label bump in gsm-readable.js); tests/walk.py.
