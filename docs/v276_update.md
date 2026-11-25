# v276 · WHO STANDS WHERE (groups across ground)

The next queue item after v275 (his call 25 Nov 2026 14:59, "move on to the next queue item"): the second generation of insight types, item 1 in his order, Groups Across Ground (BCM_TASK_QUEUE.md, 11-20 20:06; layers tracker). It also carries the first piece of item 4, Designer Is the Obstacle. Patch: tools/patches/v276_who_stands_where.py.

## What it does
A card, WHO STANDS WHERE, under WHY IT BEHAVES THIS WAY on Pattern Analysis. It finds the groups of people the notes name, from a general list of words for groups (leadership, managers, staff, supporters, opponents, residents, homeowners, the board, the community, patients, students, and so on: not a list for one subject). For each group named in two or more differently worded notes, it reads where the group stands, and says the first of these that holds:
1. **The plan relies on the people it distrusts.** What you would do (Q.5–Q.7, answers or notes) turns on the group, and distrust is aimed at it where things hinder ("distrust in leadership").
2. **A loop between groups.** A low emotion is aimed at the group ("aggression toward supporters") and also rises among it ("aggression amongst supporters").
3. **Not one block.** The group is named both above and below the line.
4. **One name, two kinds of ground.** Where the group itself holds the emotion (it opens the note, or "among", "from", "by"), it holds both a high and a low one.

Up to three groups, strongest reading first. Note numbers sit behind each line, small and gray; the notes are under "The notes behind it". Words are never merged ("leaders" and "leadership" stay two groups). Taking Action can read the groups from `gsmStructSum.groups` (not used there yet).

## Inactive unless it applies
Silent unless a group is named in two or more differently worded notes and stands in more than one place. "Communities of practice" is not read as a community. A group only mentioned in a note is never said to hold that note's emotion.

## Results
- His 11-20 workbook: leadership (what you would do turns on it, N18 and Q.6, while distrust is aimed at it, N5 and N37) and supporters (aggression aimed at them, N38, and rising among them, N16). Both are insights the 11-20 review found missing (the designers are the obstacle; the loop of aggression between supporters and opponents).
- His 11-13 workbook: the community, named on both sides (N2 hinders; N3 helps).
- Synthetic questions workbook: the board on both sides. Clinic, cause, the 200-note workbook, places, and the edge workbooks: silent.

## Checks
- matrix.py on his 11-20 and 11-13 workbooks (trimmed local copies, kept out of git), w20, big, cause, clinic, questions, places_names, empty, one, hostile, legacy, same, goalonly: no page errors, no injection. Taking Action word counts equal v275 on every workbook.
- ta_flow.py and tour_an.py on 11-20: pass. No keys in the built file.

## Wording to flag (Claude's)
The card title and all four readings.
