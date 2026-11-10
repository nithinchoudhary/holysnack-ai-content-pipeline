"""
Holy Snack Automated Visual Factory (visual_factory.py)
Renders typo-free hooks, body text, and CTAs onto Hiruni's 1080x1350 and 1080x1920 templates.
Author: Nithin Choudhary
"""
from PIL import Image, ImageDraw, ImageFont

BRAND_COLORS = {
    "cream_bg": (249, 246, 242),
    "terracotta": (148, 33, 24),
    "forest_green": (38, 70, 54),
    "charcoal": (35, 35, 35)
}

def render_template_2_card(title: str, main_msg: str, bullets: list, cta: str, out_path: str = "output_card.png"):
    img = Image.new("RGB", (1080, 1350), color=BRAND_COLORS["cream_bg"])
    draw = ImageDraw.Draw(img)
    draw.rectangle([(60, 60), (1020, 220)], fill=BRAND_COLORS["terracotta"])
    draw.text((100, 115), title.upper(), fill=(255, 255, 255))
    draw.text((100, 280), main_msg, fill=BRAND_COLORS["forest_green"])
    y = 400
    for b in bullets:
        draw.text((120, y), f"• {b}", fill=BRAND_COLORS["charcoal"])
        y += 90
    draw.rectangle([(60, 1150), (1020, 1270)], fill=BRAND_COLORS["forest_green"])
    draw.text((100, 1195), cta, fill=(255, 255, 255))
    img.save(out_path)
    return out_path
