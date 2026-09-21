#!/usr/bin/env python3
"""
Render section 390 of the Penal Code 1871 as a ladder diagram (SVG, no deps).

SECOND SOURCE. THIS FIGURE IS DRAWN, NOT GENERATED, AND IT CAN DRIFT.
The authority for the ladder is the generated set beside it -- robbery-390*.{svg,txt,mmd,
sentences}, read out of robbery-390-392.l4 through jl4-lsp by l4-ide's
ts-shared/ladder-svg/demo/robbery.ts. Nothing checks THIS script against the module, so if the
two disagree, the generated files are right. It is kept for one reason the generated set cannot
serve: both subsections on one printable page, with the leaves valued. See README.md.

s 390(1) says robbery is EITHER a theft that has been upgraded by s 390(2) OR an
extortion that has been upgraded by s 390(3). So the whole section is one OR of
two series chains, and the two panels below are those chains.

Leaves are coloured by their value on the facts of Chen Weixiong Jerriek v PP
[2003] SGHC 103 as the corpus encodes them (`Chen Weixiong Jerriek` in
robbery-390-392.l4): green carries current, grey does not. Panel B is entirely
grey because that robbery was a theft-robbery -- which is s 390(1) doing its
work, not a gap in the drawing.

Conventions follow paper/formal-methods-in-law/the-letter-and-the-spirit/
cheating-415-ladder.py in l4-ide: left-to-right, AND in series, OR in parallel
rungs, Tufte hairlines, green live / grey inert.

Regenerate:  python3 robbery-390-ladder.py
"""

GREEN, GREY, RAIL, INK = "#1a7f37", "#9aa0a6", "#3a3a3a", "#222"
W = 1180
svg = []


def rect(x, y, w, h, stroke, fill="#ffffff", op=1.0, rx=7):
    svg.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="1.5" opacity="{op}"/>')


def text(x, y, s, size=13, anchor="middle", fill=INK, op=1.0, weight="400", style=""):
    st = f' font-style="{style}"' if style else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    svg.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="Georgia, serif" font-size="{size}" '
               f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" opacity="{op}"{st}>{s}</text>')


def line(x1, y1, x2, y2, stroke=RAIL, w=1.4, op=1.0):
    svg.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
               f'stroke="{stroke}" stroke-width="{w}" opacity="{op}"/>')


def wrap(label, width_chars):
    words, lines, cur = label.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if len(trial) <= width_chars or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def leaf(xL, cy, w, label, live, call=False):
    """A rung. `call` marks a call to another section's own ladder."""
    lines = wrap(label, int(w / 6.6))
    h = max(38, 16 + 15 * len(lines))
    y = cy - h / 2
    col = GREEN if live else GREY
    rect(xL, y, w, h, col, "#f4f8f5" if call else "#ffffff")
    top = cy - (len(lines) - 1) * 7.5 + 4
    for i, ln in enumerate(lines):
        text(xL + w / 2, top + i * 15, ln, fill=INK)
    return (xL, cy), (xL + w, cy)


def group(xL, cy, w, rungs, gap=52, caption=None, call=False):
    """rungs: [(label, live)]. One rung draws as a plain leaf; more as an OR bus."""
    if len(rungs) == 1:
        pin, pout = leaf(xL, cy, w, rungs[0][0], rungs[0][1], call)
        if caption:
            text(xL + w / 2, cy - 34, caption, size=11, fill="#555", style="italic")
        return pin, pout
    heights = [max(38, 16 + 15 * len(wrap(l, int(w / 6.6)))) for l, _ in rungs]
    ys, run = [], 0.0
    for h in heights:
        ys.append(run + h / 2)
        run += h + gap - 38
    span = run - (gap - 38)
    ys = [cy - span / 2 + y for y in ys]
    busL, busR = xL - 22, xL + w + 22
    for y, (label, live) in zip(ys, rungs):
        pin, pout = leaf(xL, y, w, label, live, call)
        col = GREEN if live else GREY
        line(busL, y, pin[0], y, col, 1.4)
        line(pout[0], y, busR, y, col, 1.4)
    line(busL, ys[0], busL, ys[-1])
    line(busR, ys[0], busR, ys[-1])
    if caption:
        text(xL + w / 2, ys[0] - heights[0] / 2 - 12, caption, size=11, fill="#555", style="italic")
    return (busL, cy), (busR, cy)


def chain(cy, stations, x0=64, gap=40):
    """stations: [(width, [(label, live)], caption, is_call)] drawn in series."""
    x, ports = x0, []
    for wdt, rungs, caption, is_call in stations:
        pin, pout = group(x, cy, wdt, rungs, caption=caption, call=is_call)
        ports.append((pin, pout))
        x = pout[0] + gap
    for i in range(len(ports) - 1):
        line(ports[i][1][0], cy, ports[i + 1][0][0], cy)
    line(40, cy, ports[0][0][0], cy)
    line(ports[-1][1][0], cy, W - 40, cy)
    svg.append(f'<circle cx="44" cy="{cy:.0f}" r="3.5" fill="{RAIL}"/>')
    svg.append(f'<circle cx="{W-44}" cy="{cy:.0f}" r="3.5" fill="{RAIL}"/>')


# --- s 390(2): when theft is robbery -----------------------------------------
PANEL_A = [
    (176, [("commits theft (s 378)", True)], "s 390(1): there is a theft", True),
    (188, [("in order to commit theft", False),
           ("in committing the theft", True),
           ("in carrying away or attempting to carry away property obtained by the theft", False)],
     "“in order to … or in …”", False),
    (128, [("for that end", True)], "the purposive link", False),
    (150, [("voluntarily causes", True), ("attempts to cause", False)], "causes or attempts", False),
    (176, [("death", False), ("hurt", True), ("wrongful restraint", True),
           ("fear of instant death", False), ("fear of instant hurt", True),
           ("fear of instant wrongful restraint", False)], "… to any person", False),
]

# --- s 390(3): when extortion is robbery -------------------------------------
PANEL_B = [
    (176, [("commits extortion (s 383)", False)], "s 390(1): there is an extortion", True),
    (188, [("in the presence of the person put in fear", False)], "Explanation: near enough", False),
    (150, [("instant death", False), ("instant hurt", False), ("instant wrongful restraint", False)],
     "by putting in fear of …", False),
    (150, [("to that person", False), ("to some other person", False)], "… to whom", False),
    (128, [("then and there", False)], "delivers up on the spot", False),
]


def panel(top, heading, subtitle, stations, height):
    cy = top + height / 2 + 12
    text(40, top + 22, heading, size=17, anchor="start", weight="700")
    text(40, top + 41, subtitle, size=12, anchor="start", fill="#555", style="italic")
    chain(cy, stations)
    return top + height


H_A, H_B = 420, 300
H = 76 + H_A + 40 + H_B + 60
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
svg.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
text(W / 2, 30, "Penal Code 1871, s 390 — when a theft or an extortion becomes robbery",
     size=17, weight="700")
text(W / 2, 52,
     "s 390(1): “In all robbery there is either theft or extortion.”  The two panels are the "
     "two subsections, and they are in PARALLEL — either one makes out robbery.",
     size=12, fill="#444", style="italic")
text(W / 2, 70,
     "Green carries current on the facts of Chen Weixiong Jerriek v PP [2003] SGHC 103, as encoded. "
     "Grey does not.",
     size=12, fill="#444", style="italic")

end_a = panel(86, "s 390(2) — when theft is robbery",
              "In series: the theft, then WHEN, then the purpose, then the act, then the harm.",
              PANEL_A, H_A)
line(40, end_a + 20, W - 40, end_a + 20, "#e2e4e7", 1)
panel(end_a + 40, "s 390(3) — when extortion is robbery",
      "Wholly grey: this was a theft-robbery, so the other limb of s 390(1) is unused.",
      PANEL_B, H_B)
text(W / 2, H - 26,
     "Turn off any one green box above and the robbery withdraws to plain theft under s 379: "
     "the s 379 / s 392 boundary, drawn.",
     size=12.5, fill="#444", style="italic")
svg.append("</svg>")

open("robbery-390-ladder.svg", "w").write("\n".join(svg))
print("wrote robbery-390-ladder.svg")
