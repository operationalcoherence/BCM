# v296: his 11 redlines on Start Here and the Mapping pages, all approved (25 Nov 2026 22:33)
# Source: claude/start_mapping_redlines_2026-11-25.md (project doc). Also renames the Mapping Context
# "Combine with another workbook" link to "Combine workbooks", so R11's reason holds on screen.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
# R1 (glossary and hover)
rep(' A dashed ring on a dot means it is not associated with other answers or notes by a thread.', '', 2)
# R2
rep('A line of text with corresponding data points tied to a symbol on a map, represented as N1, N2, and so on, is a note pinned on the place map; numbered notes are on the line map.',
    'A line of text tied to a symbol on a map, numbered N1, N2, and so on.')
# R3
rep("Write the goal on the first page of the method\\'s workbook.", 'Write the goal on Mapping Context.')
# R4
rep('Each page has its own instructions, in a drop-down at its top.',
    'Mapping Landscape and Pattern Analysis have instructions in a drop-down at the top.')
# R5
rep('Write the goal, answer the seven questions, and add a place if the goal has one, otherwise, use the mapping space.',
    'Write the goal and answer the seven questions.')
rep('<b>Mapping Landscape.</b> Mark the information',
    '<b>Mapping Landscape.</b> Add a place if the goal has one; otherwise, use the line map. Mark the information')
# R6
rep('Pattern Analysis opens once you have answered all seven questions, but are supported heavily by notes.',
    'Pattern Analysis opens once you have answered all seven questions; notes add a great deal to what it finds.')
# R7
rep('Your links will be shown independently, and part of the larger pattern your answers and notes form, shown in Pattern Analysis.',
    'Your links show in Pattern Analysis, under WHAT YOU LINKED, as part of the larger pattern your answers and notes form.')
# R8
rep(' This technique can be iteratively applied in stages until the whole goal is accomplished, or as much of it as reasonably can be.', '')
# R9 (line notes and place notes)
rep('Patterns use these to show what the visualizations rest on and indicate whose voice is missing, and those which may be dominant.',
    'Pattern Analysis uses these to show what the maps rest on, whose voice is missing, and whose may dominate.', 2)
# R10
rep('Provide the goal in as much detail as possible that you are working to accomplish.',
    'Describe the goal you are working to accomplish, in as much detail as you can.')
# R11 (instruction text, and the Mapping Context link)
rep('choose Combine with another workbook:', 'choose Combine workbooks:')
rep('id="gsm-comb">Combine with another workbook</button>', 'id="gsm-comb">Combine workbooks</button>')
rep('t.textContent = "v295"', 't.textContent = "v296"')
open(p, 'w', encoding='utf-8').write(s)
print('v296 applied')
