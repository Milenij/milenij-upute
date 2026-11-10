"""Draws background.png for the share cards (layout: milenij.yml).

Only needed when changing the card's look; run it from the repository root:
    python social-cards/make_background.py
Needs Pillow (installed with mkdocs-material's social plugin).
"""
import os

from PIL import Image, ImageDraw

W, H = 1200, 630
TOP_LEFT, BOTTOM_RIGHT = (0x5c, 0x88, 0xc2), (0x2f, 0x52, 0x86)  # brand blue #5279af, lighter to darker
ORANGE = (0xff, 0x91, 0x00)  # accent colour of the site


def gradient():
    img = Image.new("RGBA", (W, H))
    px = img.load()
    for y in range(H):
        for x in range(W):
            t = (x / W) * 0.6 + (y / H) * 0.4
            px[x, y] = tuple(round(a + (b - a) * t) for a, b in zip(TOP_LEFT, BOTTOM_RIGHT)) + (255,)
    return img


def diamond(size, alpha, radius):
    """A rounded square turned 45°, like the shapes in the logo."""
    tile = Image.new("RGBA", (size, size))
    ImageDraw.Draw(tile).rounded_rectangle((0, 0, size - 1, size - 1), radius, fill=(255, 255, 255, alpha))
    return tile.rotate(45, resample=Image.BICUBIC, expand=True)


def main():
    img = gradient()

    # Faint logo-like diamonds on the right, partly off the card
    for size, alpha, x, y in [(430, 22, 820, 120), (250, 30, 1010, 10), (190, 16, 760, 420)]:
        d = diamond(size, alpha, size // 7)
        img.alpha_composite(d, (x - d.width // 2 + size // 2, y - d.height // 2 + size // 2))

    draw = ImageDraw.Draw(img)
    # White tile behind the logo (the blue logo is hard to see on blue)
    draw.rounded_rectangle((64, 56, 64 + 104, 56 + 96), 22, fill=(255, 255, 255, 255))
    # Short orange accent line above the section name
    draw.rounded_rectangle((64, 212, 64 + 72, 212 + 8), 4, fill=ORANGE + (255,))
    # Darker strip at the bottom for the web address
    strip = Image.new("RGBA", (W, 74), (0, 0, 0, 46))
    img.alpha_composite(strip, (0, H - 74))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "background.png")
    img.convert("RGB").save(out, optimize=True)
    print("Saved", out)


if __name__ == "__main__":
    main()
