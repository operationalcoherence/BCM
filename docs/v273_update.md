# v273 · THE LAY OF THE LAND retired; its numbers move to YOUR LANDSCAPE; v272 fix

His call, 25 Nov 2026 13:48 (option 1): THE BARE LANDSCAPE stays bare; the numbered readings from THE LAY OF THE LAND go onto YOUR LANDSCAPE, ONE QUESTION AT A TIME; THE LAY OF THE LAND goes.

## What changed
- **THE LAY OF THE LAND is gone from Pattern Analysis**, with its patterns row, PATTERNS THAT RUN THROUGH IT, the 2D controls, MODEL A COURSE OF ACTION and its tour. Pattern Analysis has two maps: THE BARE LANDSCAPE and YOUR LANDSCAPE.
- **YOUR LANDSCAPE carries the numbered readings** (line maps only): numbers on the 3D, hover or tap one to read it, and WHAT THE NUMBERS ON THE MAP SAY folded under the map. Its tour now stops at the numbers after its opening. Its legend no longer mentions the brown pattern lines. Place maps are unchanged.
- **Fix to v272:** its BARE flag shared a name with the engine's own BARE color, so every Pattern Analysis map (and every Taking Action card map) behaved as the bare one: notes hidden, question buttons gone, the bare reading repeated. The flag is now BAREH. Only THE BARE LANDSCAPE is bare.
- The old hidden figure inside THE LAY OF THE LAND stays in the page, hidden: Taking Action's WHERE THE READING SPLITS is read from it (removing it emptied the splits on big and clinic; checked restored).
- Wording that pointed to THE LAY OF THE LAND now points to YOUR LANDSCAPE or to the numbers.

## Checks
- `matrix.py` on w20 (trimmed), big, cause, clinic, questions, places_names, empty, one, hostile, legacy, same: no page errors, no injection; Taking Action word counts equal v272.
- WHERE THE READING SPLITS on big (THE HIDDEN CHANNELS) and clinic (ONE IDEA UNDER TWO NAMES) match v272.
- 3D on w20: YOUR LANDSCAPE shows 46 notes and 10 numbers with its tour; THE BARE LANDSCAPE shows no notes, flags, numbers or tour.
