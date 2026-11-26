# v314: F8 step 5b, the admin page

Open www.operationalcoherence.com/bcm#bcmadmin and sign in with operationalcoherence@gmail.com.

- Counts across every F8 project: projects, leads, people answering, saved workbooks, complete (7 of 7), working now, notes, exports. In the last 7 days: new projects and workbooks saved to.
- One row per project: name and lead, started, people, complete, notes, exports, last change. Phones: stacked cards.
- Counts only: nobody answering is named, and no answers or notes are shown.
- Exports: a lead's Save as a file now adds one to `exports` on the project record (one write; nothing is lost if it fails).
- Any other account sees "This page is only for the BCM administrator."
- Firebase loads only on this address. Reads: every project and every workbook, once on opening and on Refresh.

Decided here (Gregory can reverse it): **no counter in the solo version.** Its workbooks never leave the device, it never loads Firebase, and a counter that anyone can write to without signing in can be filled with junk. Visits come from Webador's own statistics.

Rules: `isAdmin()` = Google sign-in, email operationalcoherence@gmail.com, email verified. Admin may get and list projects and read every workbook (collection group). Read only: no writes, no invite keys. 13 new tests in firebase/rules.test.mjs.
**The rules must be published again in the Firebase console** before the admin page can read anything.

Privacy note: the privacy page must say that Operational Coherence's admin account can read project records and workbooks (the page only shows counts).

Tests: tests/f8admin.py (fake Firebase) at 1000 and 390 px, as the admin and as another account; f8read, f8dash, f8lead, f8join, matrix.py clean. Key check OK.
Patch: tools/patches/v314_admin_page.py.
