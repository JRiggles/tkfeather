from cairosvg import svg2png
from pathlib import Path

icons = Path("icons")

for icon in icons.iterdir():
    print(icon.stem)
    # with open(icon, 'rb') as svgfile:
    # bytestring = bytes(svg2png, 'utf-8')
    svg2png(url=str(icon), write_to=f'icons/{icon.stem}.png', scale=43.0)
