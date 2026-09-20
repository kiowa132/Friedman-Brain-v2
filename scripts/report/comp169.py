from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, os
im = Image.open('plate_169.png').convert('RGB'); W,H = im.size
# light left scrim
a = np.array(im).astype(np.float32)
sc = np.clip(1 - np.arange(W)/(W*0.55), 0, 1)**1.4 * 0.42
a *= (1 - sc)[None,:,None]*1.0 + 0*a
a += (sc[None,:,None]*np.array([6,16,18],np.float32))
im = Image.fromarray(a.clip(0,255).astype('uint8'))
d = ImageDraw.Draw(im, 'RGBA')
G = r'C:\Windows\Fonts\georgia.ttf'; GB = r'C:\Windows\Fonts\georgiab.ttf'; GI = r'C:\Windows\Fonts\georgiai.ttf'
def line(txt, y, font, fill, track=0, x=100):
    for dx,dy in [(3,3)]:
        xx=x
        for ch in txt:
            d.text((xx+dx,yy:=y+dy), ch, font=font, fill=(0,0,0,120)); xx += d.textlength(ch,font=font)+track
    xx=x
    for ch in txt:
        d.text((xx,y), ch, font=font, fill=fill); xx += d.textlength(ch,font=font)+track
gold=(201,169,106,255); cream=(250,248,245,255)
k=ImageFont.truetype(G,36); h=ImageFont.truetype(GB,110); s=ImageFont.truetype(GI,42); w=ImageFont.truetype(G,34)
y=120
line('THE FRIEDMAN REPORT', y, k, gold, 11); y+=78
d.rectangle([100,y,300,y+2], fill=gold); y+=34
line('Prices Held.', y, h, cream); y+=128
line("The Clock Didn't.", y, h, cream); y+=150
line('Week of September 14-20, 2026', y, s, gold); y+=80
d.rectangle([100,y,300,y+2], fill=gold); y+=30
line('THE FRIEDMAN TEAM', y, w, cream, 9)
im.save('hero_169_final.png')
out=r'C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\drafts\friedman-report\2026-09-14-to-09-20\images'
slug='maryland-real-estate-market-report-week-of-september-14-20-2026'
im.save(f'{out}\{slug}-hero-16x9.png'); im.resize((1600,900),Image.LANCZOS).save(f'{out}\{slug}-hero-16x9.jpg',quality=88)
