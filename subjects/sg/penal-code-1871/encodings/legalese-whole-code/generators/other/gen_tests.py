import re
D='/Users/mengwong/src/legalese/pc-encode/deposit/'
src=open(D+'pc-body-b-kidnapping.l4').read()+open(D+'pc-body-b-sexual.l4').read()
def fields(rec):
    m=re.search(r'DECLARE `'+re.escape(rec)+r'` HAS\n(.*?)\n\n(?=\S)',src,re.S)
    out=[];name=None
    for line in m.group(1).split('\n'):
        s=line.strip()
        if not s or s.startswith('--'): continue
        if s.startswith('IS A'):
            out.append((name,re.match(r'IS AN? (\w+)',s).group(1))); name=None; continue
        mm=re.match(r'^(`[^`]+`|\w+)\s*(IS AN? (\w+))?',s)
        if mm.group(2): out.append((mm.group(1),mm.group(3)))
        else: name=mm.group(1)
    return out
def q(s): return '"'+s.replace('"','\\"')+'"'
def fixture(name, rec, ov):
    fs=fields(rec)
    names=[n for n,_ in fs]
    res={}
    for k,v in ov.items():
        exact=[n for n in names if n.strip('`')==k]
        cands=exact or [n for n in names if k in n]
        assert len(cands)==1,(name,k,cands)
        res[cands[0]]=v
    lines=[f'`{name}` MEANS `{rec}` WITH']
    w=max(len(n) for n in names)
    for n,t in fs:
        val=res.get(n)
        if val is None:
            if t=='BOOLEAN': val='FALSE'
            elif t=='STRING': val='""'
            elif t=='Particulars': val='`the particulars`'
            elif t=='Person': val='`the victim`'
        elif isinstance(val,bool): val='TRUE' if val else 'FALSE'
        elif not val.startswith('`') and not val.startswith('('): val=q(val)
        lines.append(f'    {n.ljust(w)} IS {val}')
    return '\n'.join(lines)+'\n'
