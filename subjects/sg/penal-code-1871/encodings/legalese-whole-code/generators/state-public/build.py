"""Build the state-public group's L4 modules from the part files."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lib
import part_common
import part_contempts

DEP = "/Users/mengwong/src/legalese/pc-encode/deposit/"
MODULES = [
    ("pc-state-public-common.l4", part_common),
    ("pc-state-public-contempts.l4", part_contempts),
]
for mods in ["part_assembly", "part_servants", "part_state"]:
    try:
        m = __import__(mods)
        MODULES.append((f"pc-state-public-{mods[5:]}.l4", m))
    except ImportError:
        pass

tests = []
for fn, m in MODULES:
    m.module()
_fields = {f[0] for fs in lib.FIELDS.values() for f in fs}
_clash = [n for k, n, t in lib.EXPORTS if n in _fields]
assert not _clash, f"rule named like a record field (silent self-recursion): {_clash}"
lib.EXPORTS.clear()
for fn, m in MODULES:
    text = m.module()
    lib.to_ascii(text.replace("§", ""))
    open(DEP + fn, "w").write(text.rstrip() + "\n")
    print("wrote", fn, text.count("\n"), "lines")
    if hasattr(m, "tests"):
        tests.append(m.tests())

try:
    import tests_all
    t = tests_all.module([fn for fn, _ in MODULES], tests)
    open(DEP + "pc-state-public-tests.l4", "w").write(t.rstrip() + "\n")
    print("wrote pc-state-public-tests.l4", t.count("\n"), "lines")
except ImportError:
    pass
