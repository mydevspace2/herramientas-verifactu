# -*- coding: utf-8 -*-
"""Genera localmente la imagen Open Graph 1200x630 y el logotipo 512x512 (PIL, sin servicios externos)."""
import os
from PIL import Image, ImageDraw, ImageFont

F = "/usr/share/fonts/truetype/dejavu/"
BRAND = (10, 107, 96)
AMBER = (245, 158, 11)
WHITE = (255, 255, 255)


def font(name, size):
    return ImageFont.truetype(os.path.join(F, name), size)


def draw_logo(d, x, y, s, bg=BRAND, fg=WHITE):
    k = s / 32.0
    d.rounded_rectangle([x, y, x + s, y + s], radius=int(8 * k), fill=bg)
    for (px, py) in [(7, 7), (18, 7), (7, 18)]:
        d.rounded_rectangle([x + px * k, y + py * k, x + (px + 7) * k, y + (py + 7) * k], radius=int(1.2 * k), fill=fg)
        d.rectangle([x + (px + 2.2) * k, y + (py + 2.2) * k, x + (px + 4.8) * k, y + (py + 4.8) * k], fill=bg)
    cx, cy, r = x + 22.5 * k, y + 22.5 * k, 5.5 * k
    d.ellipse([cx - r - 1.4 * k, cy - r - 1.4 * k, cx + r + 1.4 * k, cy + r + 1.4 * k], fill=fg)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AMBER)
    d.line([(x + 20 * k, y + 22.6 * k), (x + 21.7 * k, y + 24.3 * k), (x + 24.8 * k, y + 21 * k)], fill=WHITE, width=max(2, int(1.7 * k)), joint="curve")


def og(path):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), BRAND)
    d = ImageDraw.Draw(im)
    d.ellipse([830, -260, 1470, 380], fill=(13, 122, 110))
    d.ellipse([940, 360, 1340, 760], fill=(12, 116, 104))
    draw_logo(d, 80, 70, 96, bg=WHITE, fg=BRAND)
    d.text((196, 84), "Herramientas Verifactu", font=font("DejaVuSans-Bold.ttf", 44), fill=WHITE)
    d.text((198, 140), "gratis · sin registro · en tu navegador", font=font("DejaVuSans.ttf", 26), fill=(206, 238, 233))
    d.text((80, 225), "¿Verifactu es obligatorio?", font=font("DejaVuSans-Bold.ttf", 70), fill=WHITE)
    d.text((80, 315), "QR tributario · huella SHA-256 · XML de ejemplo", font=font("DejaVuSans.ttf", 36), fill=(225, 245, 241))
    d.rounded_rectangle([80, 398, 1060, 480], radius=16, fill=WHITE)
    d.text((108, 418), "BOE: 1/1/2027 y 1/7/2027  ·  anunciado: oct. 2028", font=font("DejaVuSans-Bold.ttf", 32), fill=(15, 23, 42))
    d.text((80, 540), "Fuentes oficiales: BOE y AEAT  ·  sin relación con la Agencia Tributaria", font=font("DejaVuSans.ttf", 25), fill=(206, 238, 233))
    im.save(path, "PNG", optimize=True)


def logo(path, s=512):
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    draw_logo(d, 0, 0, s - 1)
    im.save(path, "PNG", optimize=True)
