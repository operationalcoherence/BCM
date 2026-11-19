# v234: the Synthesis tour opens each act with what it means

Review plan item 4c, captions from his four acts (E8). The tour already grouped its stops under THE HIGH GROUND, THE LOW GROUND, BETWEEN THEM, and WHAT KEEPS IT THIS WAY. Now the first stop of each act opens with one line under the act's name, counted from the workbook's own notes. The wording is Claude's, from his confirmed meanings, and it never cites the paper:

- **The high ground:** "Acceptance: where the goal already has people with it. It takes care to keep, and it is the place to start from. N notes of yours stand here."
- **The low ground:** "Distrust, aggression, and defiance. They are not bad in themselves; what matters is what they are attached to. The deeper the ground, the longer the road back to acceptance, and defiance is the longest. N notes of yours sit here."
- **Between them:** "Indifference: a narrow ridge where people are not yet for or against. Most moves between emotions cross it, and people can stay on it, precariously. N notes of yours carry it." With none, it says there is no ridge to cross by.
- **What keeps it this way:** "What holds the situation in place: patterns in your answers and notes that keep the ground as it is until something changes them."

Those stops hold a little longer, so the extra line can be read. The Analysis tour is unchanged.

Checked: tour.py on 11-18 (four act openers, pause, resume, Escape, full screen, no errors) and tour_an.py. Patch: tools/patches/v234_tour_acts.py (engine `D.actMean`; relief `actOpen()`).
