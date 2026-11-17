# v191 (preview only) — 2026-11-17

A2 from the task queue: a coworking-ready workbook. It is additive, so every older file still opens, and the live v92 page ignores the new fields.

**New fields:**
- `sv: 2`: the schema version.
- `wid`: an id made once for each workbook, so a perspective can be traced to the workbook it came from.
- `mt: {noteId: time}`: when each note was last edited (added, moved, text, emotion, source, voice, question). Kept by the existing edit log, for line and place notes alike.
- `gone: {noteId: time}`: when a note was deleted.
- `others[]`: each perspective now also carries `at` (the date combined) and `wid`.

**Combine now:**
- When both people have the same note, the newer edit wins. Before, yours always won and their edit was dropped.
- A note they deleted from their own notes is removed. Your notes are never removed by someone else's deletion.
- A note you deleted stays deleted, unless they edited it after you deleted it.
- The report counts only the notes added, and adds: "1 note they edited more recently now shows their version." and "1 note they deleted was removed." (Claude's wording, for his review.)

**Checked (a coworker "Sam" on both workbooks):**
- 11-13 (line note `nwepcs1`): Sam's newer edit replaced the text, his own note was added, and a second combine after he deleted it removed it.
- Broadview: the same with place note `n8ucdan`.
- Open workbook still works. 13 workbooks: matrix clean.

**For his call:**
- Should a coworker's deletion of one of *your* notes ever remove it? Today it never does.
- Should the newer-edit rule also cover answers (Q.1–Q.7)? Today each person's answers stay separate under their name.
