# v290: Start Here and the two Mapping pages, tidy pass

His call (25 Nov 2026 19:34): go on to Start Here and the two Mapping pages; his own text comes to him as redlines. This version is Claude's text and engine fixes only. Patch: tools/patches/v290_start_mapping_tidy.py.

## Fixed
1. **Bug:** on Mapping Context questions 1 to 7, the goal's heading ("START HERE · THE GOAL"), its help line, and WORKING WITH A FRIEND still showed with no goal box under them. The step code hid the first `.lab` on the page, which is YOUR NAME on Start Here. Now everything from the step chain down to the goal box, plus the friend fold, belongs to the goal step.
2. Step label "Start here · the goal and a place" is now "Start here · the goal" (the place is added on Mapping Landscape).
3. Mapping Context: the inline line "Your answers save on this device as you type. To move them or share them: Save workbook · Open workbook · Combine with another workbook" repeated the buttons and the save note at the foot of the same page. Hidden; its handlers are kept.
4. Mapping Context name help: its first two sentences repeated WORKING WITH A FRIEND. One line kept: "Combining workbooks fills WHO DID WHAT, below, with who added what, and when."
5. WORKING WITH A FRIEND: "Moved dots and hidden links in the figures are not carried across. Links added in Patterns are." named retired figures and the old page name. Now "Links you drew are carried across." Step 4 names the button that is on screen: "Combine workbooks".
6. Place-map hint: "drag around several homes" was wildfire wording in every workbook; now "several spots".
7. The dashed PLACE MAP box repeated the LOCATION help right above it. It is hidden once the line map has notes (`#gsm.lmuse`), and still shows on a new workbook.
8. Step buttons: when Back and Next wrap on a phone, Next stays on the right.

## Checks
- matrix.py on 11-13, Broadview, 11-20 (trimmed) and every mkwb workbook: no page errors, no injection.
- New tests/pagewalk.py walks Start Here, Mapping Context steps 0 to 7, and Mapping Landscape steps 1 and 2 with every fold open, printing text and saving phone-width screenshots. Run on 11-13, Broadview, and clinic.
- Checked against the engine: Pattern Analysis does open only once the goal and all seven answers are in ("Patterns need a goal and all seven answers."), so that instruction is true; only its grammar is off (redline R6). The dashed ring on a dot no longer renders anywhere (redline R1).
- `grep -c 'AAPK\|AIza'` = 0 on both built files.

## Redlines sent to him (his text, not changed)
See the Claude project, claude/start_mapping_redlines_2026-11-25.md.
