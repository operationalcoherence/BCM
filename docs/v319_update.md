# v319: a privacy screen for each role

Gregory, 26 Nov 19:35: "its just general - it pops up but it doesnt have any uniqueness to each function."

- **Working on your own:** stays on this device, nobody signs in; only a file you choose leaves it; clearing the
  browser erases it; outside services.
- **Answering an invite:** names the project and its lead ("Test Lead sees everything you write here", "Before you
  answer “Canyon test”"): what is sent and how often, what the lead can do with it (read it, read it with everyone's,
  save a file), where it is kept and until when, who else can and can't see it, what stays in the person's hands,
  their own workbook stays apart, "Don't write anything you wouldn't want Test Lead to read." Holds the page with
  "Opening the project…" until the invite is read; a bad link leaves no screen.
- **Leading a project:** you hold other people's words (use them for this project only; tell people what you'll do
  with them); deleting the project deletes every workbook; Save as a file copies are yours to look after; anyone with
  the invite link can answer; who else can see it.
- Each role is acknowledged on its own (solo, join, lead; version 2026-11-26.2). The full page has a section per role.

Tests: tests/privacy.py and tests/privacy_lead.py PASS at 390 and 1000 px; other F8 tests and matrix clean.
Patch: tools/patches/v319_privacy_by_role.py.
