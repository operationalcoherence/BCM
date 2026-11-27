# F8 build plan: live projects for leaders

Written 26 Nov 2026, after v303. Based on BCM_ARCHITECTURE.md §12a, the F8 mockup, and Gregory's 11-17 direction.
Estimate: 7 to 10 versions over several desktop sessions. Updated 26 Nov, 21:00, after v322.

## Already done (26 Nov)

- **Security rules:** `firebase/firestore.rules`. Published in the console 26 Nov 12:12; published again with the v314 admin read (13:54).
  47 tests in `firebase/rules.test.mjs` run on GitHub on every change to `firebase/` ("Firebase rules tests"). All pass.
- **Key check:** `sh tools/keycheck.sh` replaces the manual `grep -c 'AAPK\|AIza'`. Esri keys always fail. One Google
  key is allowed only if it is listed in `tools/allowed_keys.txt`, which now holds the Firebase web key (added in v307).
- **Privacy note for the solo version:** the "BCM privacy note (draft)" doc artifact.
- **Firebase console set up (26 Nov, 11:20 to 11:30, done in Gregory's Chrome):**
  - The project lives under **operationalcoherence@gmail.com** (console URL `/u/1/`), project id `the-bear-canyon-method`. 2-step verification is on for that account.
  - Sign-in providers: **Google** and **Anonymous** both enabled. Anonymous **Auto clean-up is off** (it would delete anonymous accounts after 30 days).
  - Authorized domains: `www.operationalcoherence.com` and `operationalcoherence.com` added (plus Firebase's defaults). The workbook script loads from github.io but runs on the Webador page, so github.io isn't needed.
  - A web app **"BCM Preview"** exists; its config is on Project settings → General → Your apps. Copied into the build at v307 (Analytics left out).
  - Browser key (auto created by Firebase): restricted to websites `https://www.operationalcoherence.com/*`, `https://operationalcoherence.com/*`, and `https://the-bear-canyon-method.firebaseapp.com/*` (Firebase's own sign-in pop-up). API list unchanged (25 APIs).
- **Live test passed (26 Nov evening):** project, invite, saving, EVERY WORKBOOK, admin counts, and See everyone's ground together in 3D.

## How the data is laid out

| Path | Who reads | Who writes |
| --- | --- | --- |
| `projects/{pid}` | the lead; the admin | the lead (Google sign-in); can't be handed to another lead |
| `projects/{pid}/keys/{key}` | anyone holding the link (one key, never the list) | the lead; `open: false` stops saving |
| `projects/{pid}/workbooks/{uid}` | that person, the lead, and the admin | that person only, while their key is open |

- **Leads:** sign in with Google.
- **People answering:** Firebase signs them in anonymously in the background, with nothing to type and no account. The link
  carries the key, a random string of at least 20 characters.
- **Admin:** operationalcoherence@gmail.com, Google sign-in, email verified. Read only.
- **Workbook fields:** `uid, key, name, voice, data, saved`. `data` is BCM's own workbook format (schema §11), so moving off
  Firebase later stays easy. Project records may also hold `exports` (count of a lead's Save as a file).

## Risks to test (26 Nov)

- **Google sign-in from the Webador page:** pop-up sign-in. *(Done: v307; Gregory confirmed it works on his phone, 26 Nov 11:57.)*
- **Workbook size:** Firestore allows about 1 MB per record. *(Checked at v307: tens of KB each. No split needed.)*
- **Free write cap:** 20,000 writes a day, about 80 person-hours at one save every 30 seconds. Over the cap, work stays on the device and is sent later (v4).
- **Project at a glance (v321):** how long it takes on real devices (13–16 s in the test browser's software 3D), and whether the Webador page allows the frame.

## Build order

1. **v1, the opening page.** **Done in v306.**
2. **v2, Firebase wired in.** **Done in v307–v308.** Firebase loads only on demand; the solo page never loads it or signs in.
   Test panel: www.operationalcoherence.com/bcm?f8test=1 (or #f8test).
3. **v3, Lead a project.** **Done in v309–v310, shown only with ?f8test=1.** Name, shared goal, voices plus Other, due date, map,
   invite link `<page>#bcmjoin=<pid>.<key>` (copy, email, QR), Delete this project. `tests/f8lead.py`.
   **v322: no TEST label** on the card or in the lead's box (it still shows only with ?f8test=1).
4. **v4, invited person.** **Done in v311.** Name and voice, live saving about every 30 s, Pause sharing, Delete my workbook,
   own workbook parked and brought back. `tests/f8join.py`.
5. **v5, dashboard core.** **Done in v312.** EVERY WORKBOOK table: person and voice, questions, notes, main emotion, last change,
   Open (with Save as a file), Remind, Delete; people started and working now; Stop / Start taking answers. `tests/f8dash.py`.
   **v320 replaced the table with cards (see 7b).**
5b. **Admin page for Gregory.** **Done in v314.** www.operationalcoherence.com/bcm#bcmadmin, admin = operationalcoherence@gmail.com.
   Counts across all projects: projects, leads, people answering, saved workbooks, complete (7 of 7), working now, notes, exports;
   last 7 days; one row per project. Counts only: nobody answering named, no content shown. `tests/f8admin.py`.
   **Decided in the build (Gregory can reverse): no counter in the solo version.** It stays sign-in-free and Firebase-free, and an
   open counter can be filled with junk. Visits come from Webador's own stats.
6. **v6, dashboard reading.** **Done in v313** (v315: "There is no ground yet" when nobody has written a note). READING THEM
   TOGETHER under EVERY WORKBOOK: "Patterns suggests; you decide." once; a voice filter; See everyone's ground together (one
   combined copy, #bcmread=pid); WHERE THEY SPLIT; WHERE THEY AGREE; EMOTION BY VOICE; WHAT NOBODY HAS SAID YET. Phrases only;
   single words never stated there. `tests/f8read.py`. **Since v320 this is the Project at a glance tab (see 7b).**
7. **v7, wrap-up:**
   - **Compare two people or voices: done in v317.** COMPARE TWO, last in READING THEM TOGETHER, shown with 3+ people. `tests/f8cmp.py`.
   - ~~take everyone to Taking Action~~ (covered by See everyone's ground together).
   - a file route kept as a fallback ("Add it" link): waits on Gregory's answer to question 3 below.
   - the full privacy page (needs his short legal look).
   - App Check (console work in his Chrome).
   - deploy the rules.
7b. **Lead dashboard in three levels: done in v320, v321** (Gregory chose mockup B, 26 Nov; design in
   claude/lead_dashboard_design_2026-11-26.md).
   - Tabs **Project at a glance** (opens first since v321) and **People** (cards in Working now, Still going, Finished; a
     seven-step bar; Open, Remind, Delete; "Show all N" past 9).
   - **One person** behind Open: See their ground and their story (their workbook alone as a copy for reading), Save as a
     file, Remind, Delete, how far they have got, NEXT TO THE PROJECT, their answers and notes folded.
   - **Project at a glance (v321):** AT A GLANCE, THE GROUND THEY MAKE TOGETHER (THE BARE LANDSCAPE in 3D with WHAT THIS
     GROUND IS DOING) and THE STORY SO FAR, read from the combined copy in a frame of its own whose storage is kept in memory
     (window.GSM_PEEK), so nothing is saved and the lead's own workbook is untouched. Then the reading: HOW FAR THE PROJECT HAS
     GOT, EMOTION ACROSS THE PROJECT, WHERE THEY SPLIT, WHERE THEY AGREE, WHAT NOBODY HAS SAID YET, COMPARE TWO.
   - **Open for Gregory:** the story says "your workbook" and "your own answers" in a project too.
8. **v8 to v9, test and fix:** with one real team.

## Needed from Gregory

1. ~~Who may lead a project?~~ **Decided 26 Nov: anyone who signs in with Google.**
2. ~~How long answers are kept, and who can delete them?~~ **Decided 26 Nov:** kept until the lead deletes the project; anyone can delete their own workbook; a lead can delete any workbook in their project. Anonymous Auto clean-up stays **off**.
3. Does the file route stay for people who don't want to share live?
4. Which account owns the Firebase project long term? (Today: operationalcoherence@gmail.com.)
5. ~~Admin account and solo counter~~ **Decided 26 Nov:** admin is operationalcoherence@gmail.com; no solo counter (see 5b).
6. ~~Publish the rules again~~ **Done 26 Nov 13:54.**
7. ~~The ~5 minute live test~~ **Passed 26 Nov evening.**

**Before real answers go in:** the full privacy page, with a short legal look. It must say the admin account can read project records and workbooks (the admin page only shows counts).

## Rules for every F8 version

- Stay on the free Spark plan. Never move to Blaze without Gregory's yes. (Google Cloud shows a "$300 free trial" banner: ignore it.)
- Run `sh tools/keycheck.sh` before every push.
- Rule changes ship only with passing tests.
- The solo version must keep working with no sign-in at all.
