# v252: every note brings its own emotion color to the ground

His screenshot (11-20 15:45, Pattern Synthesis 3D): "The acceptance emotion doesnt show up on hinder." "It didn't bring its color with it." His call to do it next: 11-24 09:23. Patch: tools/patches/v252_note_color.py (relief.js, plus the label in gsm-readable.js).

## Cause
The ground color at any spot is a blend of every note within reach, with each emotion's weight raised to the power 2.2 (defiance × 1.6). A lone note among many notes of another emotion was outvoted at its own spot. Nothing was side-specific: it showed on the hinder side because acceptance there is usually alone among aggression, distrust, and defiance.

## What changed
- Each note also has a small patch of its own color (radius about 8 map units, roughly the pin's footprint). Where that patch is stronger than what the blend already shows, the note's emotion takes the spot. Where the note's color already wins, nothing changes.
- Inside the patch the rock face and the indifference band step aside, so a lone note in distant ground shows as a small patch ringed by rock. That is the line map's own meaning: two distant emotions meet with no ridge between them.
- Color only. Heights, the goal, the ways, and everything else on the line map are unchanged (his 11-19 rule).
- Applies to every workbook, line and place maps alike. On Broadview the picture is unchanged to the eye (0.04% of pixels).

## 11-20, after
N1 and N8 (acceptance, hinder side) now sit on teal. Aggression on the help side (N12) and among defiance (N38) shows its red. About 1% of the picture changed, all at note spots.

## Tested
matrix.py on 11-20 (trimmed local copy), Broadview, and every mkwb workbook: no errors. 3D screenshots before and after on 11-20, Broadview, big (200 notes), same (12 identical notes), and clinic: no errors. tour.py on 11-20: passes. Key check 0 on both built files.

## Not changed
The emotion definitions for both sides of the line still wait on his redline (claude/emotion_definitions_redline.md).
