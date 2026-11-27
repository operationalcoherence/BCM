# Build the sample project the lead's dashboard can open with ?f8test=1 (v326): 20 made-up people, their own notes from
# tests/fuel_break_20.json, answers written per voice, and a spread of progress. Nothing is sent anywhere.
# python3 tools/sample/build_sample_project.py  ->  tests/sample_project_fuel_break.json
import json, random
random.seed(11)
W = json.load(open('tests/fuel_break_20.json'))['data']
ANS = {
 'Residents': [
  "Nobody on the upper road has been asked what they think, so a plan made elsewhere feels like it's being done to us.",
  "Some of us oppose any cutting we didn't ask for, especially close to the houses, and a few won't let crews on their land.",
  "Most neighbours want the homes above the road protected; several already clear their own brush.",
  "We'd need to see the map, know who decides where the line runs, and believe the money won't stop halfway.",
  "Walk the line with residents before anything is marked, and let each household see what happens on their lot.",
  "Neighbour-to-neighbour visits, the fire department breakfasts, and a chipping day on our road.",
  "A named person to call, a printed map, and dates we can plan around."],
 'Fire crews': [
  "The work keeps getting delayed by access and by people not knowing what a shaded fuel break looks like.",
  "A few landowners refuse access, and some residents are angry about thinning near their homes.",
  "Our crews are already doing the work on the lower road, and some landowners have asked us to come up.",
  "Steady funding for two seasons, signed access agreements, and one decision maker who answers questions.",
  "Start where people already want us, show a finished stretch, then work outward.",
  "Ride-alongs, the station open house, and shared equipment with the land managers.",
  "A shared work calendar between agencies and a weekly note to the neighbourhood."],
 'Land managers': [
  "Past plans were written and shelved, so people expect this one to go the same way.",
  "Opposition comes from distrust of outside agencies and from who decides the route.",
  "Fire crews, a few large landowners, and the county support the break.",
  "Clear ownership maps, agreements that outlast one budget year, and a plan people have actually read.",
  "Phase the break so each section can be finished and shown before the next one starts.",
  "Grazing as a tool on the open ground, and joint planning days with the crews.",
  "A single plan everyone signs, with the funding and the schedule in it."],
 'Other: school board': [
  "Families worry about smoke and the one road out, but nobody has brought the school into the planning.",
  "Some parents distrust the agencies and worry about how the work affects the bus route and school days.",
  "The school nurse, the PTA, and teachers who already run fire-safety lessons.",
  "The school needs to know the schedule, the smoke plan, and who to call.",
  "Plan the work around the school calendar and use the school to share the map with families.",
  "The school newsletter, a joint drill with the fire department, and the evacuation drill map.",
  "A school-year calendar of work days and a smoke plan the nurse can follow."],
}
by = {}
for n in W['m']:
    by.setdefault(n[9], {'voice': n[7], 'm': []})['m'].append(n[:8] + [n[8].split('-', 1)[1], n[9]])
people = []
order = sorted(by, key=lambda s: int(s.split()[1]))
for i, name in enumerate(order):
    P = by[name]
    # progress: 9 finished, 6 still going, 3 working now, 2 just started
    if i < 9: qs, keep, ago = range(7), len(P['m']), random.randint(600, 4000)
    elif i < 15: qs, keep, ago = random.sample(range(7), random.randint(3, 5)), random.randint(5, 9), random.randint(120, 2000)
    elif i < 18: qs, keep, ago = random.sample(range(7), random.randint(2, 4)), random.randint(4, 8), random.randint(1, 4)
    else: qs, keep, ago = [0], 2, random.randint(20, 90)
    a = [''] * 7
    for k in qs: a[k] = ANS[P['voice']][k]
    w = {'goal': W['goal'], 'a': a, 'm': P['m'][:keep], 'p': {'m': []}, 'voices': [P['voice']], 'links': [], 'decisions': {}, 'others': [], 'who': name, 'log': []}
    people.append({'uid': 'sample%02d' % (i + 1), 'name': name, 'voice': P['voice'], 'ago': ago, 'json': json.dumps(w, ensure_ascii=False)})
out = {'project': {'name': 'Upper canyon fuel break (sample)', 'goal': W['goal'], 'voices': list(ANS), 'map': {'kind': 'line'}, 'due': '15 January'},
       'people': people}
json.dump(out, open('tests/sample_project_fuel_break.json', 'w'), ensure_ascii=False)
print(len(people), 'people,', sum(len(json.loads(p['json'])['m']) for p in people), 'notes')
