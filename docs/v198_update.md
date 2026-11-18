# v198 update (2026-11-18)

The first pass on Gregory's 11-18 review of v196: the items already decided (Phase 1 of the review plan, kept in the Claude project because it quotes his workbook). Patch: `tools/patches/v198_review_first_pass.py` (engine only).

## 1. What each emotion means
Every emotion button on a note now carries the paper's own definition as a tooltip, and the emotion key under the map has a fold, WHAT EACH EMOTION MEANS, with all five in the paper's order (acceptance, indifference, distrust, aggression, defiance) and the line on how much energy distant moves take. Every definition is a direct quote from Vigneaux (2026), with page numbers. He approved the quotes on 11-18.

## 2. Mapping Context
- The page title, Mapping Context, now sits at the top of the page, not under the goal.
- The goal is headed START HERE · THE GOAL and carries his instruction: "Provide the goal in as much detail as possible that you are working to accomplish."
- WORKING WITH A FRIEND now sits directly under the goal.

## 3. Instruction 10
He flagged it as outdated. The emotional landscape switch only exists on a place map, so the line now says so: on a place map, Show emotional landscape paints how far each emotion reaches toward the change; on the line map, Pattern Synthesis shows it as ground. The switch itself stays, because place maps use it.

## 4. The ground's one-tap question (Pattern Synthesis)
The buttons read Supports and Does Not Support (were Stands for it and Turns away), and the question asks "Does N15 support 'aggressive suppression'?" to match. The question is about the phrase the note negates, not the goal, so "the Goal" is left off the button: "Supports the Goal" would have asked something the engine doesn't use.

## 5. The two pictures
"Put the two pictures together" left Pattern Analysis and now closes Pattern Synthesis, where it is the next step. The Analysis + Synthesis together button at the top shows on Pattern Synthesis only.

## 6. Taking Action
- The Sources list under the program and strategy explanation is gone; its works are in REFERENCES at the foot of the page (Axelrod & Cohen, 2000, added there; the rest were already listed).
- The explanation's last sentence now ends with (Morin & Kern, 1999; Morin, 2008).
- NO RESPONSE YET is now NOTHING YOU WOULD DO ANSWERS THESE YET: the hindering notes that nothing in Q.5–Q.7 answers.

## Wording that is Claude's (flagged)
NOTHING YOU WOULD DO ANSWERS THESE YET; WHAT EACH EMOTION MEANS; instruction 10; "Does N… support '…'?". The emotion definitions are his paper's words.

## Tests
- `tests/matrix.py` on 11-13, Broadview, clinic, empty, 200 notes, hostile, and both maps: no page errors, no script injection.
- `tests/relief_text.py` with the 3D on 11-13, Broadview, and clinic: the method's name, the new heading, and (where a note negates a phrase) Does Not Support are on the page.
- A direct check of the emotion key: the fold and all five tooltips render.
- `grep -c 'AAPK\|AIza'` = 0.
