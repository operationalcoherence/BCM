# v326 · a sample project in Lead a project (?f8test=1)

After signing in, the list of projects ends with "Upper canyon fuel break (sample)": 20 made-up people (tests/sample_project_fuel_break.json, built by tools/sample/build_sample_project.py from the fuel-break test set, with answers written per voice and a spread of progress: 3 working now, 8 still going, 9 finished). It is read from the site's own files; nothing is written to Firebase, and Save, Delete, and Stop taking answers are blocked for it. Test: tests/samplepj.py (no writes, guard message).
