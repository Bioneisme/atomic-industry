"""Draws icon.png (512x512): a radiation trefoil inside a factory gear, on a dark sky with a warm glow.

    python tools/make_icon.py
"""
import math
import pathlib

from PIL import Image, ImageDraw, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
N = 512
S = 4  # supersampling
W = N * S
C = W / 2


def gear(draw, r_out, r_in, teeth, fill):
    pts = []
    for i in range(teeth * 4):
        a = 2 * math.pi * i / (teeth * 4)
        r = r_out if (i % 4) in (1, 2) else r_in
        pts.append((C + r * math.cos(a), C + r * math.sin(a)))
    draw.polygon(pts, fill=fill)


def main():
    img = Image.new("RGB", (W, W), (14, 17, 30))
    d = ImageDraw.Draw(img)
    for i in range(60):  # vertical gradient: night above, ember below
        t = i / 59
        col = (int(14 + 70 * t * t), int(17 + 22 * t * t), int(30 - 10 * t))
        d.rectangle([0, W * i / 60, W, W * (i + 1) / 60 + 1], fill=col)

    glow = Image.new("L", (W, W), 0)
    ImageDraw.Draw(glow).ellipse([C - 0.42 * W, C - 0.42 * W, C + 0.42 * W, C + 0.42 * W], fill=150)
    glow = glow.filter(ImageFilter.GaussianBlur(W * 0.08))
    img.paste((255, 150, 40), mask=glow)

    d = ImageDraw.Draw(img)
    gear(d, 0.46 * W, 0.40 * W, 12, (52, 56, 66))
    d.ellipse([C - 0.36 * W, C - 0.36 * W, C + 0.36 * W, C + 0.36 * W], fill=(250, 196, 30))
    d.ellipse([C - 0.345 * W, C - 0.345 * W, C + 0.345 * W, C + 0.345 * W], fill=(255, 210, 40))

    ink = (24, 22, 26)
    r1, r2 = 0.075 * W, 0.31 * W
    for k in range(3):  # the three blades of the trefoil
        a0 = math.radians(-90 + 120 * k - 30)
        a1 = math.radians(-90 + 120 * k + 30)
        pts = [(C + r1 * math.cos(a0), C + r1 * math.sin(a0))]
        for j in range(25):
            a = a0 + (a1 - a0) * j / 24
            pts.append((C + r2 * math.cos(a), C + r2 * math.sin(a)))
        pts.append((C + r1 * math.cos(a1), C + r1 * math.sin(a1)))
        d.polygon(pts, fill=ink)
    rc = 0.055 * W
    d.ellipse([C - rc, C - rc, C + rc, C + rc], fill=ink)

    img.resize((N, N), Image.LANCZOS).save(ROOT / "icon.png", optimize=True)
    print("icon.png", (ROOT / "icon.png").stat().st_size, "bytes")


if __name__ == "__main__":
    main()
