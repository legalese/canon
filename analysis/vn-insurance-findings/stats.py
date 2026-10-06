import re,glob,collections,json,sys
recs=[]
for f in sorted(glob.glob('records-*.md')):
    txt=open(f,encoding='utf-8').read()
    for blk in re.split(r'(?m)^### ',txt)[1:]:
        head,_,body=blk.partition('\n')
        m=re.match(r'(VN-\d+)\s+(Finding \d+|\S+)\s+[—-]\s+(.*)',head)
        if not m: print('UNPARSED',head[:80]); continue
        g=lambda k: (re.search(r'\*\*'+k+r'\*\*:?\s*(.*)',body) or [None,''])[1].strip()
        body=body.split('\n#### ')[0]
        cls=re.search(r'\*\*Class\*\*:?\s*(.*)',body)
        st=re.search(r'\*\*Standing\*\*:?\s*(.*)',body)
        md=re.search(r'\*\*Money direction\*\*:?\s*([^\n]*)',body)
        recs.append(dict(row=m.group(1),fid=m.group(2),title=m.group(3).strip(),cls=cls.group(1).strip() if cls else '',standing=st.group(1).strip() if st else '',money=md.group(1).strip() if md else '',file=f))
json.dump(recs,open('records.json','w'),ensure_ascii=False,indent=0)
print(len(recs),'records')
def first(s,pat): 
    m=re.search(pat,s); return m.group(0) if m else '?'
c=collections.Counter(first(r['cls'],r'T\d+') for r in recs); print('primary class:',sorted(c.items(),key=lambda x:-x[1]))
c2=collections.Counter()
for r in recs:
    for t in set(re.findall(r'T\d+',r['cls'])): c2[t]+=1
print('any class mention:',sorted(c2.items(),key=lambda x:-x[1]))
s=collections.Counter(first(r['standing'].upper(),r'LITERAL|CONTESTED|LAW') for r in recs); print('standing:',s)
m=collections.Counter(('claimant' if 'against the claimant' in r['money'] else 'insurer' if 'against the insurer' in r['money'] else 'no money' if 'no money' in r['money'] else 'unclear') for r in recs); print('money:',m)
