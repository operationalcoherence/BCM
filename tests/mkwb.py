import json, random, sys, copy
def wb(d): return {"app":"groundsmith","v":1,"saved":"2026-11-07T00:00:00Z","data":d}
def base(goal="", a=None, m=None, p=None, **kw):
    d={"goal":goal,"a":a or [""]*7,"m":m or [],"p":p or {"m":[],"c":[39.5,-98.5,4]},
       "voices":[],"links":[],"decisions":{},"others":[],"who":"","fig":{},"log":[]}
    d.update(kw); return wb(d)

# 1 empty
json.dump(base(), open('wb_empty.json','w'))

# 2 goal only
json.dump(base(goal="Open a clinic."), open('wb_goalonly.json','w'))

# 3 one note, one answer
json.dump(base(goal="Keep the clinic open.",
    a=["Funding dried up."]+[""]*6,
    m=[[1,100,60,"The lease is the problem.",None,0,0,None,"na"]]), open('wb_one.json','w'))

# 4 clinic, non-wildfire, 8 notes
cl_a=["The clinic lost its anchor tenant and the lease rose. Residents drive 40 minutes for primary care.",
 "The hospital board opposes a satellite site. They say it splits referrals.",
 "The school nurse already refers families and that works.",
 "A stable lease and a standing shuttle would change it.",
 "Design a shuttle route and a shared intake form.",
 "Redesign the referral path so the school nurse can book directly.",
 "Reinforce the school nurse relationship with paid hours."]
cl_m=[[2,30,150,"Hospital board sees the satellite clinic as a threat to referrals.",None,3,0,None,"c1"],
 [2,70,170,"Residents distrust a clinic that may close again.",None,4,None,None,"c2"],
 [3,60,60,"School nurse refers families already.",None,1,0,"Mine","c3"],
 [3,120,70,"Pharmacy owner offers space.",None,1,None,None,"c4"],
 [4,180,80,"A stable lease would let staff be hired.",None,1,None,None,"c5"],
 [5,220,70,"Design a shuttle route with the senior center.",None,1,None,"Mine","c6"],
 [6,250,90,"Redesign intake so the school nurse books directly.",None,1,None,None,"c7"],
 [2,200,180,"Lease renewal is month to month.",None,3,None,None,"c8"]]
json.dump(base(goal="To have the Broad Street clinic open five days a week within a year, with primary care for residents who now drive 40 minutes.",a=cl_a,m=cl_m,voices=["Mine"]), open('wb_clinic.json','w'))

# 5 legacy 9-element notes (his older saves) -- same as above but trimmed to 9
leg=[r[:9] for r in cl_m]
json.dump(base(goal="Legacy nine element notes.",a=cl_a,m=leg), open('wb_legacy.json','w'))

# 6 hostile text: html, quotes, unicode, very long
hostile=[[1,50,50,'<script>window.XSS=1</script> & "quotes" <b>bold</b>',None,0,0,None,"h1"],
 [2,90,150,"emoji 🔥🔥 and ünïcödé and a very long word "+("x"*300),None,1,None,None,"h2"],
 [3,150,60,"</text><circle r=\"999\"/>",None,2,None,None,"h3"],
 [4,200,160,"   ",None,None,None,None,"h4"]]
json.dump(base(goal='<img src=x onerror="window.XSS2=1"> & more',a=['<b>a</b>']+["word "*40]*6,m=hostile), open('wb_hostile.json','w'))

# 7 large: 200 notes
random.seed(7)
words="access funding lease shuttle referral staffing intake outreach training policy transport housing data equity".split()
big=[]
for i in range(200):
    big.append([random.randint(1,7),random.randint(10,330),random.randint(10,220),
        " ".join(random.choice(words) for _ in range(random.randint(8,30)))+".",None,
        random.choice([0,1,2,3,4,None]),random.choice([0,1,None]),random.choice(["Mine","Them",None]),"b%d"%i])
json.dump(base(goal="Scale access across the county. "+" ".join(words),
    a=[" ".join(random.choice(words) for _ in range(120))+"." for _ in range(7)],
    m=big,voices=["Mine","Them"]), open('wb_big.json','w'))

# 8 all notes identical
same=[[2,100+i,100,"Tradition.",None,0,None,None,"s%d"%i] for i in range(12)]
json.dump(base(goal="Tradition.",a=["Tradition."]*7,m=same), open('wb_same.json','w'))

# 9 place map + line map together
rj=json.load(open('real.json'))['data']  # supplied by him; not stored here
bv=json.load(open('broadview.json'))['data']
mix=copy.deepcopy(rj); mix['p']=copy.deepcopy(bv['p'])
json.dump(wb(mix), open('wb_both.json','w'))
print("written")
