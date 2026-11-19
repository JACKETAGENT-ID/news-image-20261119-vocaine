#!/usr/bin/env python3
"""Generate entry.png: a broadsheet editorial page summing up 19 Nov 2026.

Style: calm navy / cream / gold broadsheet on diplomacy & justice.
Layout: masthead, one large lead story (left), two medium stories
(right), and a horizontal timeline strip with three short items below.
All text is drawn from verified reporting dated 19 November 2026.
Deterministic: no timestamps, no randomness, fixed fonts and geometry.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

CREAM = (247, 242, 231)
NAVY = (27, 42, 74)
NAVY_SOFT = (43, 60, 96)
GOLD = (184, 138, 44)
GOLD_LIGHT = (214, 176, 92)
INK = (30, 32, 38)
GREY = (96, 100, 110)
RULE = (203, 192, 168)
WHITE = (250, 248, 242)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, max_w, fill, leading):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text):
    draw.text((x, y), text.upper(), font=SANS_B(17), fill=GOLD)
    return y + 26


def headline(draw, x, y, text, fnt, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=NAVY)
        y += leading
    return y


def rule(draw, x, y, w, color=GOLD, width=3):
    draw.line([(x, y), (x + w, y)], fill=color, width=width)
    return y + width + 10


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # --- thin gold frame -----------------------------------------------
    d.rectangle([14, 14, W - 15, H - 15], outline=GOLD, width=2)
    d.rectangle([22, 22, W - 23, H - 23], outline=RULE, width=1)

    # --- masthead -------------------------------------------------------
    d.rectangle([22, 22, W - 23, 168], fill=NAVY)
    d.text((512, 48), "THE WORLD", font=SERIF_B(64),
           fill=WHITE, anchor="mt")
    d.text((512, 122), "19 NOVEMBER 2026  ·  DIPLOMACY & JUSTICE",
           font=SANS_B(19), fill=GOLD_LIGHT, anchor="mt")
    d.line([(52, 156), (972, 156)], fill=GOLD, width=2)

    # --- lead story: left, large ---------------------------------------
    lx, lw = 52, 560
    y = 196
    y = kicker(d, lx, y, "Washington — Lead Story")
    y = headline(d, lx, y,
                 "Jeffries set to become first Black Speaker of the House",
                 SERIF_B(44), lw, 52)
    y = rule(d, lx, y, 120)
    y = para(d, (lx, y),
             "Democrats have nominated Hakeem Jeffries to lead the U.S. "
             "House of Representatives. If elected, he would be the first "
             "African-American Speaker in the chamber's history.",
             SERIF(23), lw, INK, 32)
    y += 14
    # small gold seal
    d.ellipse([lx, y, lx + 54, y + 54], outline=GOLD, width=3)
    d.text((lx + 27, y + 27), "HJ", font=SERIF_B(22),
           fill=NAVY, anchor="mm")
    d.text((lx + 70, y + 4), "A historic first for the House:",
           font=SANS_B(19), fill=NAVY)
    d.text((lx + 70, y + 30), "the party's nominee takes the gavel.",
           font=SANS(19), fill=GREY)
    y += 84
    d.line([(lx, y), (lx + lw, y)], fill=RULE, width=2)

    # --- right column: two medium stories ------------------------------
    rx, rw = 652, 320
    y = 196
    y = kicker(d, rx, y, "Brussels — Europe")
    y = headline(d, rx, y,
                 "EU proposes €45bn loan for Ukraine",
                 SERIF_B(30), rw, 37)
    y = para(d, (rx, y),
             "The European Union has proposed a €45 billion loan to "
             "Ukraine, to be repaid once Russia pays war reparations.",
             SERIF(20), rw, INK, 28)
    y += 26
    d.line([(rx, y), (rx + rw, y)], fill=RULE, width=2)
    y += 22
    y = kicker(d, rx, y, "The Hague — Justice")
    y = headline(d, rx, y,
                 "Myanmar faces landmark genocide verdict",
                 SERIF_B(30), rw, 37)
    y = para(d, (rx, y),
             "Myanmar faces a historic ruling at the International Court "
             "of Justice over the mass killing of Rohingya Muslims.",
             SERIF(20), rw, INK, 28)

    # --- divider above timeline ----------------------------------------
    d.line([(52, 726), (972, 726)], fill=NAVY, width=3)
    d.text((52, 742), "THE DAY IN BRIEF", font=SANS_B(20), fill=NAVY)
    d.text((972, 742), "19 NOVEMBER 2026", font=SANS_B(18),
           fill=GREY, anchor="rt")

    # --- timeline strip: three short items ------------------------------
    items = [
        ("CRIMEA", "Crimea bridge attacked again, "
                   "Russian officials say."),
        ("GAZA", "Rare Israeli ground operation in Gaza "
                 "crosses the Yellow Line."),
        ("WEST BANK", "Australia sanctions Israeli settlers "
                     "over West Bank expansion."),
    ]
    x = 52
    col_w = 296
    for i, (tag, text) in enumerate(items):
        if i:
            d.line([(x - 18, 784), (x - 18, 918)], fill=RULE, width=2)
        d.text((x, 780), tag, font=SANS_B(20), fill=GOLD)
        para(d, (x, 810), text, SERIF(21), col_w, INK, 29)
        x += col_w + 16

    d.text((512, 966), "Sources: BBC · NDTV · Reuters — 19 November 2026",
           font=SANS(16), fill=GREY, anchor="mt")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, "PNG", optimize=True)


if __name__ == "__main__":
    main()
