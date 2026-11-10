import json,sys
W=dict(oppNE=.30,goalNR=.30,condNot=.25,suppNR=.22,saidNM=.18,mapNA=.18,forAg=.15,cross=.15,carry=.10)
GAP=['oppNE','goalNR','condNot','suppNR','saidNM','mapNA']
def order(L,drop=(),gate=None,w=W):
    old=L['old'];g=L['g'];R=L['roles']
    sc={x:sum(w[r] for r in R[x] if r not in drop) for x in old}
    if gate is None:
        return sorted(old,key=lambda x:(-sc[x],-g[x],x))
    gated=[x for x in old if any(r in gate and r not in drop for r in R[x])]
    rest=[x for x in old if x not in gated]
    return sorted(gated,key=lambda x:(-sc[x],-g[x],x))+rest
V={'nogate':dict(),'gate_all':dict(gate=GAP),'drop_said':dict(drop=('saidNM',)),
   'gate_nosaid':dict(drop=('saidNM',),gate=[r for r in GAP if r!='saidNM'])}
for wbn in sys.argv[1:]:
    D=json.load(open('/tmp/lo_%s.json'%wbn))['lo']
    seen={};
    for L in D: seen.setdefault(tuple(L['old']),L)
    L=list(seen.values())
    print('=====',wbn,len(D),'lists',len(L),'distinct')
    for v,kw in V.items():
        ch=sum(1 for l in L if order(l,**kw)[:3]!=l['old'][:3])
        print(v,'changed top3:',ch)
    big=max(L,key=lambda l:len(l['old']))
    print('largest list',len(big['old']))
    for v,kw in V.items():
        o=order(big,**kw);
        for nm in ('cost','dead'):
            c=[x for x in big['old'] if x.startswith(nm)]
            for x in c: print('  ',v,x,'rank',o.index(x)+1,'roles',big['roles'][x])
        print('  ',v,'top5',o[:5])
print()
kw=V['gate_nosaid']
for wbn in sys.argv[1:]:
    D=json.load(open('/tmp/lo_%s.json'%wbn))['lo']
    seen={}
    for L in D: seen.setdefault(tuple(L['old']),L)
    print('=====',wbn)
    for l in sorted(seen.values(),key=lambda l:-len(l['old'])):
        o=order(l,**kw)
        gated=sum(1 for x in l['old'] if any(r in kw['gate'] for r in l['roles'][x]))
        if o[:3]!=l['old'][:3] or len(l['old'])>=15:
            print(len(l['old']),'gated',gated,'| old',l['old'][:3],'| new',o[:3],[ [r for r in l['roles'][x] if r!='saidNM'] for x in o[:3]])
