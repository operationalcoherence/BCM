# v321: Project at a glance opens first, with the ground in 3D and the story

Gregory, 26 Nov 20:16: "it should open on "project at a glance" with graphics, and include a story like the one in
Patttern Analysis".

- The lead's dashboard opens on **Project at a glance** (tabs now: Project at a glance, People).
- At the top of it, read from everyone's workbooks together (or one voice's, with the voice filter):
  - **AT A GLANCE**, as Pattern Analysis has it (WHAT THE SYSTEM IS DOING and the rest).
  - **THE GROUND THEY MAKE TOGETHER**: THE BARE LANDSCAPE in 3D with its own reading, WHAT THIS GROUND IS DOING (force,
    lean, what holds it, what can move, what is less likely, what is out of reach). Tapping the ground still reads it.
  - **THE STORY SO FAR**: Pattern Analysis's YOUR STORY SO FAR, open.
  - "Read from N workbooks at 8:28 PM. Read again". It is read once, and again only on Read again or a new voice, so
    the 3D doesn't reload every minute while people work.
- Then, as before: Open everyone's workbooks together in full (was See everyone's ground together), HOW FAR THE PROJECT
  HAS GOT, EMOTION ACROSS THE PROJECT, WHERE THEY SPLIT, WHERE THEY AGREE, WHAT NOBODY HAS SAID YET, COMPARE TWO.
- Shown once each of the seven questions has an answer from someone; until then a line says how many do.

How: the dashboard opens the combined copy in a frame of its own (srcdoc, window.GSM_PEEK). In that frame storage is a
plain object, so nothing is saved on the device or sent, and the lead's own workbook is never touched (checked in the
test). Pattern Analysis runs there as it does on the page, so the story and the ground are the engine's own. Only
THE BARE LANDSCAPE is built in the frame (the other maps never are). The dashboard keeps the frame where it is when it
redraws; a frame that has to move is read again.

Not changed: the story's wording says "your workbook" and "your own answers", as it does for one person. In a project
it means the group's.

Tests: f8dash.py checks the glance (AT A GLANCE, 3D canvas, story), that the lead's own workbook and storage are
untouched, that Refresh keeps the frame, and that reopening a project reads it again; f8read.py and f8cmp.py read
.rdg2. All F8 and privacy tests clean at 390 and 1000 px; matrix equals v320.
Patch: tools/patches/v321_glance_story_ground.py.
