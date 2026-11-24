# v248: Pattern Analysis, several stories

First build of Several Systems (queue: "Pattern Analysis: several stories, not one", 11-20 19:30).

## What it does
- `gsmSystems()` finds the separate low grounds on a line map from what the workbook already holds: each note's place, side, and emotion. Height uses the terrain's own rule (acceptance − (1.5 × aggression + distrust + 3.4 × defiance)), each note reaching about as far as the terrain's sigma. Hollows that meet at a saddle shallower than 12% of the map's height are one hollow. Indifference notes are never inside a hollow; they are the ridge.
- A hollow counts when its center lies on the side that hinders, it holds 3 or more notes, 2 or more of them on low ground (aggression, distrust, defiance), and it is deeper than 15% of the map's height.
- Several stories when there are 2 or more such hollows and the largest holds under 75% of their notes. Cap 3, largest first.
- YOUR STORY SO FAR then opens with "Your workbook holds N stories". Each story is two paragraphs of continuous prose (his brief, 11-24 07:19): the dynamic, why it emerges, what keeps recreating it, what it reveals, why it matters, where it goes if it continues, and what would have to change. No note text and no note numbers in the prose. Each sentence is chosen from what the hollow holds: where it sits in time (start, partway, close to the goal), its emotions, acceptance of the present inside it, aggression answering it from the side that helps (the loop between sides), a ridge of indifference out of it or bare rock, and whether it holds most of the low ground. A sentence already used in an earlier story gives way to a variant. The notes behind each reading are folded under it, with their numbers.
- The first draft's verse and "What holds it / What helps / Where it can cross" lines were dropped at his direction (11-24 07:19).
- The one-line story and WHERE THIS LEAVES THE WORK are kept, folded under "The whole workbook read as one story".
- No change on place maps, workbooks under 12 placed notes or 8 with an emotion, or a workbook with one structure.

## Tested
- 11-20 (46 notes): three stories, matching the 11-20 review: the present opposition (N1 and N8 acceptance inside it), the job-security hollow (N19, N24, N37, with N26, N38), and the after-adoption hollow near the goal (N10, N11, N27).
- 11-18 (35 notes): two stories (the present hold; entrenchment, climate feedback, and refusal near the goal).
- Broadview, clinic, empty, one-note, hostile, both-maps: unchanged. 200-note: three stories.
- matrix.py on all, ta_flow.py: pass. New: tests/stories.py, tests/storyshot.py.

## Waiting on him
The wording (verse and prose lines) is Claude's. Not on main until he approves.
