"""Generate the compact decorative terminal and reduced-motion images."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageChops
import json
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
PROOF = ROOT / 'work/animation-proof'
ASSETS.mkdir(exist_ok=True)
PROOF.mkdir(parents=True, exist_ok=True)
FPS, SECONDS = 20, 10
LABELS = ['~/oierdu $ ./portfolio', '> GIPUZKOA 360', '> web & business software', '> backend, data & applied AI']
STARTS = [0.25, 1.8, 3.0, 4.7]

def terminal(theme, mobile=False):
    width, height = (360, 136) if mobile else (500, 145)
    colors = (('#151a22', '#202731', '#e6edf3', '#a3afbc', '#343e4b', '#a7d7b5') if theme == 'dark' else ('#fafaf7', '#eceeea', '#252b34', '#596875', '#d4d9d4', '#276747'))
    background, bar, ink, muted, border, accent = colors
    font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 15 if mobile else 16)
    title_font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 11)
    y_start, line_height = (33, 22) if mobile else (37, 23)
    def draw(seconds, still=False):
        window = Image.new('RGB', (width, height), background)
        pen = ImageDraw.Draw(window)
        pen.rounded_rectangle((0, 0, width-1, height-1), radius=8, fill=background, outline=border)
        pen.rounded_rectangle((1, 1, width-2, 25), radius=7, fill=bar)
        pen.rectangle((1, 18, width-2, 25), fill=bar)
        pen.line((1, 25, width-2, 25), fill=border)
        for x, color in [(13, '#d69c98'), (27, '#cbbc83'), (41, '#98b7a1')]:
            pen.ellipse((x, 9, x+5, 14), fill=color)
        pen.text((width-126, 6), 'oierdu / portfolio', font=title_font, fill=muted)
        empty = window.copy()
        active, shown = 0, []
        for index, label in enumerate(LABELS):
            assert pen.textlength(label, font=font) + 28 < width
            count = len(label) if still else min(len(label), max(0, round((seconds-STARTS[index])*FPS)))
            shown.append(label[:count])
            if count: active = index
            pen.text((16, y_start+index*line_height), label[:count], font=font, fill=accent if index == 0 else ink if index < 3 else muted)
        if not still and seconds >= STARTS[0] and int(seconds*2) % 2 == 0:
            x = 16+pen.textlength(shown[active], font=font)
            y = y_start+active*line_height
            pen.rectangle((x+2, y+3, x+8, y+16), fill=accent)
        # The window stays stable; only its contents fade before the next cycle.
        if not still and seconds >= 8:
            window = Image.blend(empty, window, max(0.0, 1-(seconds-8)/1.5))
        return window
    frames = [draw(i/FPS) for i in range(FPS*SECONDS)]
    name = f'terminal-compact-{theme}' + ('-mobile' if mobile else '')
    frames[0].save(ASSETS/(name+'.gif'), save_all=True, append_images=frames[1:], duration=1000//FPS, loop=0, optimize=True, disposal=1)
    draw(7, still=True).save(ASSETS/(name+'-still.png'), optimize=True)
    gif = Image.open(ASSETS/(name+'.gif'))
    first, total = gif.convert('RGB'), 0
    for index in range(gif.n_frames):
        gif.seek(index)
        total += gif.info['duration']
    seamless = ImageChops.difference(first, gif.convert('RGB')).getbbox() is None
    assert total == SECONDS*1000 and seamless
    for seconds in [1, 4, 7, 9, 11, 24, 31]: draw(seconds % SECONDS).save(PROOF/f'{name}-{seconds}s.png')
    return {'file': name+'.gif', 'dimensions': [width, height], 'bytes': (ASSETS/(name+'.gif')).stat().st_size, 'frames': gif.n_frames, 'duration_ms': total, 'loop': gif.info.get('loop'), 'first_equals_last': seamless}

if __name__ == '__main__':
    qa = [terminal(theme, mobile) for theme in ['dark', 'light'] for mobile in [False, True]]
    (PROOF/'encoding.json').write_text(json.dumps(qa, indent=2), encoding='utf-8')
