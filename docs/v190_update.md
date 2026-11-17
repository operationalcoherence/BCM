# v190 (preview only) — 2026-11-17

From his report: "it is impossible to open a workbook in the app. I did it once but have not been able to replicate doing so."

**Cause.** There are two Open workbook buttons: one on Mapping Context and one at the bottom of the other tabs. Opening a file while a workbook is already on the device asks "Replace what is on this device with the workbook you opened?". That question lives on Mapping Context. From the second button it appeared on a hidden tab, so nothing seemed to happen, and the file was never loaded. It worked only from the Mapping Context button (or on an empty device).

**Fix.**
- When the question appears, the app goes to Mapping Context and centers the question.
- The same applies to "That file could not be opened…", which is now also shown next to the second button.
- Combine had the same flaw and gets the same fix.

**Checked:**
- Both directions (11-13 to Broadview and back) from both buttons: the question shows, Replace loads the other workbook.
- 13 workbooks: matrix clean.

No new wording.
