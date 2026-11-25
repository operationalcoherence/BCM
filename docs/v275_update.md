# v275 · Pattern Analysis says each thing once

His go-ahead 25 Nov 2026 14:58 ("fix all") on the top-to-bottom read in the Claude project, claude/pattern_analysis_repeats_review_2026-11-25.md. Patch: tools/patches/v275_say_it_once.py.

## What was cut, and where it is still said
- **The plan gap** (things in the way that nothing you would do answers): OPPOSITION NOT YET ENGAGED, the story's NOT YET ANSWERED, and the POSSIBLE PATTERNS pairs "comes up often, but nothing you would design…" and "only ever appears on one side… none of your actions…" are gone. Still said in BIGGEST GAP, the story's WHAT YOU WOULD DO, and "Not in Q.5–Q.7 yet" under WHAT SHAPE THE LINE MAP MAKES.
- **Unused support:** SUPPORT NOT YET REINFORCED, READY TO REINFORCE, "Areas to reinforce", and the unused-support sentence in the story's WHAT IS ALREADY HELPING are gone. Still said in THE OPPORTUNITY and "Unused support" under WHAT SHAPE. Taking Action's seeded card now names that list as its source.
- **What the system is doing:** the story no longer repeats AT A GLANCE's heading.
- **Why the present holds:** WHAT HOLDS THE SITUATION IN PLACE goes when the story already says the present arrangement is taken as the right one; WHY IT BEHAVES THIS WAY goes with it when it is left empty. The other kind of WHAT HOLDS (one connected body) stays.
- **Chapters:** a sentence an earlier chapter already said is not said again (for example "It matters because it stands apart from the others…", "aggression can harden into defiance…", and the closing line on loosening acceptance).
- **The ridge:** WHERE IT CAN CROSS and the "emotion of transition" line are gone (Taking Action still gets the crossing). Still said on THE BARE LANDSCAPE, in the story, in WHAT THIS SUGGESTS, and on the map.
- **The emotion mix:** the "Each ground, side by side" table, the "Emotional disposition" count, and the behaviors-first aside after the emotions-first advice are gone.
- **WHERE THIS LEAVES THE WORK** is gone (THE OPPORTUNITY says it).
- **Both sides of the line:** FOR AND AGAINST ON THE MAP and OTHER SIDE OF THE LINE fold into CROSSES THE GROUND LINE.
- **Answers with no note:** said only in NOT ON THE MAP, not again in WHAT THIS SUGGESTS.
- **Read them in full** is gone from "Your own words", with its second WHERE TO START and NOT YET ANSWERED.

## Fixes
- The story's present/later sentence now says it is about the context you have grasped, and splits the line where NOW AND LATER does; NOW AND LATER says it counts what you would design too. They no longer contradict.
- RUNS TOGETHER reads a note's side from where it sits on the line, not from its symbol (a redesign note above the line was called "hinder side").
- WHAT THE NUMBERS ON THE MAP SAY shows again under YOUR LANDSCAPE (hidden since v273).

## Checks
- matrix.py on w20, big, cause, clinic, questions, places_names, empty, one, hostile, legacy, same, goalonly: no page errors, no injection. Taking Action word counts equal v274. Pattern Analysis shorter on every non-empty workbook (w20 1710 → 1577, big 1691 → 1564, cause 1648 → 1511).
- Full read with every fold open and the 3D loaded (w20, big, clinic, cause, questions): none of the cut text remains; the numbers list shows.
- tour_an.py w20, bare2d.py w20 nogl, ta_flow.py cause: pass. No keys in either built file.
