# v207 update (2026-11-18)

His note (11-18): hovering over strategy titles doesn't work for him; put the whole context in small gray text next to the title ("good fire:" and then the context). And "wildfire management" paired with reducing agency administrator input was not the best context. Patch: `tools/patches/v207_title_context.py` (engine only).

## What changes on Taking Action
1. **Every card title shows its context in small gray text right after it:** the whole sentence it comes from and where it is ("wildfire management: “Aggression towards redesigning the wildfire management system to lean toward the use of good fire whenever possible.” (N33)"). No hover needed. Ground cards keep their titles, which already name their notes.
2. **Thread cards choose that sentence better.** They took the first sentence that happened to use the phrase (N12 for "wildfire management"). Now the engine weighs every sentence that uses the phrase and shows the one that shares the most words with the others (the phrase's common ground), passing over very short sentences and, when there is a choice, the goal. On his 11-18 workbook "wildfire management" now shows N33. Cards titled by a clause from one answer or note show that whole sentence.

## Wording
No new wording; the gray text is his own.

## Tests
- `tests/matrix.py` on 11-18, 11-13, Broadview, clinic, 200 notes, hostile, legacy, empty, and both maps: no page errors, no script injection.
- `tests/relief_text.py` with the 3D on 11-18, clinic, and Broadview: cards and FIRST MOVES present, no page errors.
- `tests/switch.py` and `tests/waymoves.py` on 11-18: the switch saves and undoes; FIRST MOVES follows each way.
- Screenshots of the good fire and wildfire management headers checked.
- `grep -c 'AAPK\|AIza'` = 0.
