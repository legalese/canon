import re, sys, json
probe = open(sys.argv[1]).read().splitlines()
run = open(sys.argv[2]).read()
# map #EVAL line -> case id (nearest preceding "-- CASE Cnn")
line2case = {}
cur = None
for i, l in enumerate(probe, 1):
    m = re.match(r'^-- CASE (C\d\d)', l)
    if m: cur = m.group(1)
    if l.startswith('#EVAL'): line2case[i] = cur
# Evaluation blocks
blocks = re.split(r'\n(?=Evaluation\[\d+\] @ )', run)
out = {}
for b in blocks:
    m = re.match(r'Evaluation\[\d+\] @ \S+?:(\d+):', b)
    if not m: continue
    ln = int(m.group(1))
    r = re.search(r'\nResult:\n(.*?)\n\n\nTrace:', b, re.S)
    txt = r.group(1) if r else b
    txt = '\n'.join(x[2:] if x.startswith('  ') else x for x in txt.splitlines())
    out[line2case.get(ln, f'line{ln}')] = txt
for k in sorted(out): print(k, '|', out[k])
print(len(out), 'evaluations;', len(line2case), '#EVAL lines')
