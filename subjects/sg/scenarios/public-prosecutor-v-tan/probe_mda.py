import sys
sys.path.insert(0,'../../misuse-of-drugs-act-1973/encodings/generators')
from fixtures import Types, Out
T=Types('../../misuse-of-drugs-act-1973/encodings/mda-types.l4')
o=Out(T,"IMPORT prelude\nIMPORT `mda-types`\nIMPORT `mda-punishment`\n")
o.case('qty','Drug Quantity Facts',the__weight__of__diamorphine__in__grammes=4) if False else None
print(T.records['Antecedent Facts'][-6:])
