# v232: Mapping Context, step 9 part 1 (instructions on their pages, emotion meanings on every note)

Phase 2 step 9 of the v196 review plan, the part that doesn't touch his wording (his yes, 11-19 06:53: "Yes, afterwards" to the redlines coming after). His text is moved word for word. Nothing of his is reworded.

## What changed
- **Start here** keeps the method: old 01–03 and 06–08, now numbered 01–06. IN THIS WORKBOOK is now one line: "Each page has its own instructions, in a drop-down at its top." (Claude's wording.) THE FIVE PAGES and WORDS USED HERE stay. The page drops from 1,051 words to 671.
- **Mapping Landscape, step 1 (mark the map):** the existing MAPPING LANDSCAPE: INSTRUCTION drop-down now opens with HOW TO MAP, which is old 04, 05, and 10.
- **Mapping Landscape, step 2 (describe your notes):** one line, "Every note you placed is here, in one place, to describe and edit." (Claude's wording, plan item 2j.) Under it is a closed DESCRIBE YOUR NOTES: INSTRUCTION drop-down with old 09, 11, and 12.
- **Every note shows its emotion's meaning:** the approved quote from Vigneaux (2026), with its page number, in small gray text under the emotion buttons (plan item 2g). It changes as soon as another emotion is picked and disappears when the note is set to Not marked. It's on line-map and place-map notes alike. The tooltips stay, but the meaning no longer depends on hover.
- **Pattern Analysis** has a closed PATTERN ANALYSIS: INSTRUCTION drop-down under the opening note, holding old 13. **Pattern Synthesis** has PATTERN SYNTHESIS: INSTRUCTION, holding old 14 and 15. Each shows on its own tab only. The tab switch sets `onan` and `onsy` on #gsm.
- **Mapping Context:** the name help now ends "Combining fills WHO DID WHAT, below, with who added what, and when." (Claude's wording, plan item 2d.)

## Still to come (part 2, his redlines, one at a time)
1a–1e (Start here), 2f (instruction 09), 2i (11 and 12), and 2k (LOCATION). The Project Leader and twenty people text waits for F8.

Also for his redline: WORDS USED HERE still says "How a note **feels**" under Emotion, source, voice. His rule is "emotion", never "feeling". The text was left alone here.

## Checked
- `tests/step9.py` (new) on 11-18, Broadview, clinic, and empty. It checks that Start here keeps the method, HOW TO MAP sits in the step-1 drop-down, and the step-2 help shows only on step 2. It checks that every note with an emotion shows exactly one definition, that clicking Defiance shows its quote, that Not marked clears it, that the WHO DID WHAT line shows, and that each reading-page instruction shows on its own tab only. All pass.
- `matrix.py` on 11-18, Broadview, and every mkwb workbook: no errors, and every tab except Start here is within a few words of v231. `ta_flow.py` passes on 11-18 and Broadview. The key check is 0 on both built files.

Patch: tools/patches/v232_mapping_context.py.
