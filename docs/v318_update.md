# v318: the privacy screen (F8 step 7, part 2)

Gregory, 26 Nov 19:26: "it needs to be mandatory - you can't work until you have acknowledged it."

- A screen covers the workbook until "I understand" is pressed. No close button; Escape, clicks outside, and Tab
  can't get past it (the workbook is inert behind it).
- **Solo** (first open): stays on this device; you choose where it goes; outside services; what we don't do.
- **Live** (an invite link, or Lead a project, even after the solo one): saved online in Google Firebase in the US;
  who can see it (the person, the lead, and the BCM administrator); what is kept; how long and how to delete it;
  your own workbook stays apart; outside services; "Don't write anything you wouldn't want the lead to read."
- "Read the full privacy page" from the screen, and a **Privacy** link at the bottom of the workbook any time.
- Asked again only when the text's version (a date, now 2026-11-26) changes.
- Recorded on the device (groundsmith-web-privacy); on a live project also in the workbook record (data.privacy)
  and the lead's project record (privacy). No rule change needed: `data` is a map and project fields aren't limited.
- Not on #bcmadmin.

Tests: tests/privacy.py (solo, full page, Escape/outside/Tab, version change, invite link, record) and
tests/privacy_lead.py (Lead a project asks first, project record) at 390 and 1000 px. All other tests now set the
acknowledgement in their start-up script; f8read, f8cmp, f8dash, f8lead, f8join, f8admin, matrix clean. Key check OK.
Patch: tools/patches/v318_privacy_gate.py.

Still needs Gregory's short legal look at the wording.
