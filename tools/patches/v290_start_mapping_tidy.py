# v290: Start Here and the two Mapping pages, tidy pass (his call 25 Nov 2026 19:34).
# Claude's own text and engine fixes only; his text goes to him as redlines (docs/v290_update.md).
#  1. Bug: on question steps 1-7, the goal's heading, its help line, and WORKING WITH A FRIEND
#     still showed with no goal box under them (the step code hid the first .lab on the page,
#     which is YOUR NAME on Start Here, not the goal's heading).
#  2. Step label "Start here · the goal and a place" -> "the goal" (the place is on Mapping Landscape).
#  3. Mapping Context: the inline "Your answers save on this device ... Save · Open · Combine" line
#     repeated the buttons and the save note at the foot of the page. Hidden (handlers kept).
#  4. Mapping Context name help: its first two sentences repeated WORKING WITH A FRIEND; one line kept.
#  5. WORKING WITH A FRIEND note named the retired figures and the old name "Patterns".
#  6. Place-map hint said "drag around several homes" (wildfire wording); now "several spots".
#  7. The dashed PLACE MAP box repeated the LOCATION help; hidden once the line map has notes.
#  8. Step buttons: when Back and Next wrap on a phone, Next stays on the right.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

# 1
rep('''            var c = N.querySelector(".lab");
            n.push(c);''', '''            var c = document.getElementById("gsm-chain");
            for (c = c && c.nextElementSibling; c && !c.classList.contains("goal"); c = c.nextElementSibling) n.push(c);
            var c2 = document.getElementById("gsm-friend");
            c2 && n.push(c2);''')
# 2
rep('"<b>Start here</b> · the goal and a place"', '"<b>Start here</b> · the goal"')
# 3 and 7 and 8 (CSS, appended to the first stylesheet string)
rep('"#gsm .srdef{', '"#gsm .saved.cx0{display:none!important}#gsm.lmuse .noloc{display:none}#gsm .snav .sb:last-child{margin-left:auto}#gsm .srdef{')
# 7: mark a workbook whose line map has notes
rep('''              (N.classList.toggle("ms1", 1 === e),''', '''              (N.classList.toggle("lmuse", !!document.querySelector("#gsm-marks > *")),
              N.classList.toggle("ms1", 1 === e),''')
# 4
rep("If you work with others, each person writes their name here, answers alone, and saves their workbook. Then combine the workbooks to see everyone\\'s answers side by side. Combining fills WHO DID WHAT, below, with who added what, and when.",
    "Combining workbooks fills WHO DID WHAT, below, with who added what, and when.")
# 5
rep("Moved dots and hidden links in the figures are not carried across. Links added in Patterns are.",
    "Links you drew are carried across.")
# 6
rep("drag around several homes to mark an area", "drag around several spots to mark an area")
# 3b: the inline Combine link is hidden, so name the button at the foot of the page
rep('Your friend chooses Combine with another workbook and picks your file.', 'Your friend chooses Combine workbooks and picks your file.')
# label
rep('t.textContent = "v289"', 't.textContent = "v290"')
open(p, 'w', encoding='utf-8').write(s)
print('v290 applied')
