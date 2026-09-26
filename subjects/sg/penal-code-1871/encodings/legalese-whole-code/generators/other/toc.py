import sys,re
rows=[];cur=None;chap=None
for line in open("/Users/mengwong/src/legalese/pc-encode/inputs/PC1871.txt").readlines()[265:455]:
    s=line.strip()
    if not s or "Singapore Statutes Online" in s: continue
    m=re.match(r"Chapter (\S+) — (.*)",s)
    if m: chap=m.group(1); continue
    m=re.match(r"(\d+[A-Z]?) (.*)",s)
    if m:
        cur=[chap,m.group(1),m.group(2)]; rows.append(cur)
    elif cur: cur[2]+=" "+s
print("| Ch | s | heading | disposition | functions |")
print("| --- | --- | --- | --- | --- |")
for c,n,h in rows:
    h=h.replace("’","'").replace("“",'"').replace("”",'"')
    print(f"| {c} | {n} | {h} | deferred | |")
