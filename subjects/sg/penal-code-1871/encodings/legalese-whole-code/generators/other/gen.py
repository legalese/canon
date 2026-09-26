# Expand @@FIX blocks in a tests template into full `Type WITH` literals.
#   @@FIX `name` : Type [< `base`]
#   <prefix of a field to set TRUE>      (must match exactly one field)
#   -<prefix>                            (unset a field inherited from base)
#   =<prefix> => <L4 expression>         (set a field to an expression)
#   @@END
#   @@NONE Type                          (all-FALSE fixture `nothing established - Type`)
import re,sys
sys.path.insert(0,sys.argv[1])
from fields import fields
F=fields(sys.argv[3:])
fix={}
def match(t,pre):
    c=[f for f in F[t] if f==pre] or [f for f in F[t] if f.startswith(pre)]
    if len(c)!=1: sys.exit(f"field prefix {pre!r} for {t}: {len(c)} matches")
    return c[0]
out=[];L=open(sys.argv[2]).read().split('\n');i=0
while i<len(L):
    l=L[i]
    m=re.match(r'^@@NONE (.+)$',l)
    if m:
        t=m.group(1).strip(); name=f'`nothing established - {t}`'
        fix[name]=(t,{})
        out.append(f'{name} MEANS `{t}` WITH')
        for f in F[t]: out.append(f'    `{f}` IS FALSE')
        i+=1; continue
    m=re.match(r'^@@FIX (`[^`]+`) : (.+?)(?: < (`[^`]+`))?$',l)
    if m:
        name,t,base=m.group(1),m.group(2).strip(),m.group(3)
        vals=dict(fix[base][1]) if base else {}
        if base and fix[base][0]!=t: sys.exit('base type mismatch '+name)
        i+=1
        while L[i]!='@@END':
            s=L[i].strip()
            if s.startswith('-'): vals.pop(match(t,s[1:].strip()),None)
            elif s.startswith('='):
                a,b=s[1:].split('=>'); vals[match(t,a.strip())]=b.strip()
            elif s: vals[match(t,s)]='TRUE'
            i+=1
        fix[name]=(t,vals)
        out.append(f'{name} MEANS `{t}` WITH')
        for f in F[t]: out.append(f'    `{f}` IS {vals.get(f,"FALSE")}')
        i+=1; continue
    out.append(l); i+=1
print('\n'.join(out))
