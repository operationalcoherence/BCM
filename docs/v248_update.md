# v248: Pattern Analysis, several stories

First build of Several Systems (queue: "Pattern Analysis: several stories, not one", 11-20 19:30).

## What it does
- `gsmSystems()` finds the separate low grounds on a line map from what the workbook already holds: each note's place, side, and emotion. Height uses the terrain's own rule (acceptance − (1.5 × aggression + distrust + 3.4 × defiance)), each note reaching about as far as the terrain's sigma. Hollows that meet at a saddle shallower than 12% of the map's height are one hollow. Indifference notes are never inside a hollow; they are the ridge.
- A hollow counts when its center lies on the side that hinders, it holds 3 or more notes, 2 or more of them on low ground (aggression, distrust, defiance), and it is deeper than 15% of the map's height.
- Several stories when there are 2 or more such hollows and the largest holds under 75% of their notes. Cap 3, largest first.
- YOUR STORY SO FAR then opens with "Your workbook holds N stories", and for each: a short verse (where it is, how deep, what sits inside it, how it gets out), then one line each for what holds it, what helps (nearest notes on the higher ground across the line, each note used once), and where it can cross (indifference notes between the hollow and that help; none means a climb over bare rock). Acceptance on the hinder side inside a hollow is named as holding it in place. A hollow near the goal says it can take hold after the change seems done. The notes in each hollow are folded under it.
- The one-line story and WHERE THIS LEAVES THE WORK are kept, folded under "The whole workbook read as one story".
- No change on place maps, workbooks under 12 placed notes or 8 with an emotion, or a workbook with one structure.

## Tested
- 11-20 (46 notes): three stories, matching the 11-20 review: the present opposition (N1 and N8 acceptance inside it), the job-security hollow (N19, N24, N37, with N26, N38), and the after-adoption hollow near the goal (N10, N11, N27).
- 11-18 (35 notes): two stories (the present hold; entrenchment, climate feedback, and refusal near the goal).
- Broadview, clinic, empty, one-note, hostile, both-maps: unchanged. 200-note: three stories.
- matrix.py on all, ta_flow.py: pass. New: tests/stories.py, tests/storyshot.py.

## Waiting on him
The wording (verse and prose lines) is Claude's. Not on main until he approves.
