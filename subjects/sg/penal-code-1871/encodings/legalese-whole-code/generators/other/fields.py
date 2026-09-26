import re,sys
def fields(paths):
    out={}
    for p in paths:
        cur=None
        for l in open(p):
            m=re.match(r'^DECLARE `([^`]+)` HAS',l)
            if m: cur=m.group(1); out[cur]=[]; continue
            if cur is None: continue
            if re.match(r'^\S',l) and not l.startswith('--'): cur=None; continue
            m=re.match(r'^    `([^`]+)`',l)
            if m: out[cur].append(m.group(1))
    return out
if __name__=='__main__':
    for k,v in fields(sys.argv[1:]).items(): print(k,len(v))
