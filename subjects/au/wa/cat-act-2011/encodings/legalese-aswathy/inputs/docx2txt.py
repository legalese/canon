import sys, zipfile, re
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
z=zipfile.ZipFile(sys.argv[1]); root=ET.fromstring(z.read('word/document.xml'))
out=[]
for p in root.iter(W+'p'):
    s=[]
    for el in p.iter():
        if el.tag==W+'t': s.append(el.text or '')
        elif el.tag==W+'tab': s.append('\t')
        elif el.tag in (W+'br',W+'cr'): s.append('\n')
        elif el.tag==W+'noBreakHyphen': s.append('-')
        elif el.tag==W+'sym': s.append('?')
    out.append(''.join(s))
txt='\n'.join(out)
txt=re.sub(r'\n{3,}','\n\n',txt)
sys.stdout.write(txt)
