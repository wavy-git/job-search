#!/usr/bin/env python3
"""Generate banner color variants."""
import subprocess
from pathlib import Path

OUT = Path(__file__).parent

TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1584 436" width="1584" height="436">
  <rect width="1584" height="436" fill="{BG}"/>
  <rect x="500" width="8" height="436" fill="{BAR}"/>
  <g fill="none" stroke="{WAVE}" stroke-width="1.4">
    <path d="M520,120 C700,70 900,170 1100,120 S1400,70 1584,120" stroke-opacity="0.42"/>
    <path d="M520,170 C700,120 900,220 1100,170 S1400,120 1584,170" stroke-opacity="0.30"/>
    <path d="M520,220 C700,170 900,270 1100,220 S1400,170 1584,220" stroke-opacity="0.20"/>
    <path d="M520,270 C700,220 900,320 1100,270 S1400,220 1584,270" stroke-opacity="0.14"/>
    <path d="M520,320 C700,270 900,370 1100,320 S1400,270 1584,320" stroke-opacity="0.09"/>
  </g>
  <g font-family="'Helvetica Neue', Helvetica, Arial, sans-serif">
    <text x="560" y="160" font-size="68" font-weight="800" fill="{TITLE}" letter-spacing="-1.4">Business &amp; Technology Leader</text>
    <text x="564" y="208" font-size="25" font-weight="700" fill="{SUB}" letter-spacing="3.5">PRODUCTS  <tspan font-size="20">•</tspan>  OPERATIONS  <tspan font-size="20">•</tspan>  ENGINEERING  <tspan font-size="20">•</tspan>  MONETIZATION</text>
    <text x="564" y="244" font-size="20" font-weight="700" fill="{SUB}" letter-spacing="1.5">AI-AUGMENTED OPS  <tspan font-size="16">•</tspan>  REGULATED PLATFORMS  <tspan font-size="16">•</tspan>  FINTECH  <tspan font-size="16">•</tspan>  TELECOM  <tspan font-size="16">•</tspan>  ENERGY</text>
    <text x="564" y="302" font-size="26" fill="{TAG}" font-weight="500">Building what doesn&apos;t exist yet,</text>
    <text x="564" y="340" font-size="26" fill="{TAG}" font-weight="500">and solving problems others miss</text>
  </g>
</svg>
'''

VARIANTS = {
    # Harmony with profile photo
    'h1_charcoal_tan': {'BG':'#FFFFFF','BAR':'#2A2E33','WAVE':'#9C7858','TITLE':'#2A2E33','SUB':'#9C7858','TAG':'#2A2E33'},
    'h2_slate_espresso': {'BG':'#FFFFFF','BAR':'#5A6B7E','WAVE':'#3D2E24','TITLE':'#3D2E24','SUB':'#5A6B7E','TAG':'#3D2E24'},
    'h3_suit_copper': {'BG':'#FFFFFF','BAR':'#1A1F26','WAVE':'#A07859','TITLE':'#1A1F26','SUB':'#A07859','TAG':'#1A1F26'},
    # Vibrant
    'v1_royal_gold': {'BG':'#FFFFFF','BAR':'#4B0082','WAVE':'#D4AF37','TITLE':'#4B0082','SUB':'#D4AF37','TAG':'#4B0082'},
    'v2_cobalt_coral': {'BG':'#FFFFFF','BAR':'#0047AB','WAVE':'#FF6F61','TITLE':'#0047AB','SUB':'#E55A4E','TAG':'#0047AB'},
    'v3_emerald_magenta': {'BG':'#FFFFFF','BAR':'#0F8F5C','WAVE':'#C026D3','TITLE':'#0F8F5C','SUB':'#A621B0','TAG':'#0F8F5C'},
    # Gray bg + dark text + OTW green
    'g1_gray_otwgreen': {'BG':'#E5E7EB','BAR':'#2E7D32','WAVE':'#2E7D32','TITLE':'#0F172A','SUB':'#1B5E20','TAG':'#0F172A'},
    # My picks
    'm1_onyx_electric': {'BG':'#FFFFFF','BAR':'#0A0A0A','WAVE':'#0EA5E9','TITLE':'#0A0A0A','SUB':'#0284C7','TAG':'#0A0A0A'},
    'm2_forest_burgundy': {'BG':'#FAF6EC','BAR':'#0F2F22','WAVE':'#7C2D3A','TITLE':'#0F2F22','SUB':'#7C2D3A','TAG':'#0F2F22'},
    'm3_plum_champagne': {'BG':'#FFFFFF','BAR':'#3E1F44','WAVE':'#B89554','TITLE':'#3E1F44','SUB':'#9A7A3D','TAG':'#3E1F44'},
    'm4_ink_saffron': {'BG':'#FFFFFF','BAR':'#0A0A0A','WAVE':'#F0A500','TITLE':'#0A0A0A','SUB':'#C28100','TAG':'#0A0A0A'},
    'm5_navy_rosegold': {'BG':'#FFFFFF','BAR':'#0F172A','WAVE':'#B76E79','TITLE':'#0F172A','SUB':'#9A4E5A','TAG':'#0F172A'},
    'm6_hunter_brass': {'BG':'#FFFFFF','BAR':'#1B4332','WAVE':'#9C7A2E','TITLE':'#1B4332','SUB':'#9C7A2E','TAG':'#1B4332'},
    'm7_steel_terracotta': {'BG':'#FFFFFF','BAR':'#3D5A80','WAVE':'#C76847','TITLE':'#3D5A80','SUB':'#B05435','TAG':'#3D5A80'},
}

# Render all standard variants
for name, c in VARIANTS.items():
    svg = TEMPLATE
    for k, v in c.items():
        svg = svg.replace('{' + k + '}', v)
    (OUT / f'{name}.svg').write_text(svg)

# Freestyle: editorial autumn -- ivory bg, thick burnt orange bar, no waves, top/bottom hairlines, italic tagline
FREESTYLE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1584 436" width="1584" height="436">
  <rect width="1584" height="436" fill="#F5EFE2"/>
  <rect x="500" width="14" height="436" fill="#C24914"/>
  <line x1="540" y1="80" x2="1540" y2="80" stroke="#1B4332" stroke-width="1.2" stroke-opacity="0.4"/>
  <line x1="540" y1="370" x2="1540" y2="370" stroke="#1B4332" stroke-width="1.2" stroke-opacity="0.4"/>
  <g font-family="Georgia, 'Times New Roman', serif">
    <text x="560" y="170" font-size="72" font-weight="700" fill="#1B4332" letter-spacing="-1">Business &amp; Technology Leader</text>
  </g>
  <g font-family="'Helvetica Neue', Helvetica, Arial, sans-serif">
    <text x="564" y="218" font-size="22" font-weight="700" fill="#C24914" letter-spacing="3">PRODUCTS  <tspan font-size="18">•</tspan>  OPERATIONS  <tspan font-size="18">•</tspan>  ENGINEERING  <tspan font-size="18">•</tspan>  MONETIZATION</text>
    <text x="564" y="252" font-size="18" font-weight="600" fill="#1B4332" letter-spacing="2">AI-AUGMENTED OPS  <tspan font-size="14">•</tspan>  REGULATED PLATFORMS  <tspan font-size="14">•</tspan>  FINTECH  <tspan font-size="14">•</tspan>  TELECOM  <tspan font-size="14">•</tspan>  ENERGY</text>
  </g>
  <g font-family="Georgia, serif" font-style="italic" fill="#1B4332">
    <text x="564" y="310" font-size="26" font-weight="400">Building what doesn&apos;t exist yet,</text>
    <text x="564" y="345" font-size="26" font-weight="400">and solving problems others miss.</text>
  </g>
</svg>
'''
(OUT / 'free1_editorial_autumn.svg').write_text(FREESTYLE)

# Render all to PNG
chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
names = list(VARIANTS.keys()) + ['free1_editorial_autumn']
for name in names:
    subprocess.run([chrome, '--headless', '--disable-gpu', '--hide-scrollbars',
                    '--force-device-scale-factor=4', '--window-size=1584,436',
                    f'--screenshot={OUT}/{name}.png',
                    f'file://{OUT}/{name}.svg'],
                   capture_output=True, cwd=OUT)
print(f"Generated {len(names)} variants")
