from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
im = Image.open('../images/2.webp').convert('RGB')      # 2000x676 with baked text
def wipe(im, y0, y1, x0, x1):
    a = np.array(im).astype(float)
    def uf(v,k,axis=0):
        p=np.pad(v,((k//2,k//2),(0,0)),mode='edge'); c=np.cumsum(np.vstack([np.zeros((1,3)),p]),axis=0); return (c[k:]-c[:-k])/k
    top = uf(a[y0-5:y0-1, x0:x1].mean(axis=0), 41, axis=0); bot = uf(a[y1+1:y1+5, x0:x1].mean(axis=0), 41, axis=0)
    for y in range(y0, y1):
        t = (y-y0)/(y1-y0); a[y, x0:x1] = top*(1-t)+bot*t
    o = Image.fromarray(a.astype('uint8'))
    band = o.crop((x0-8, y0-3, x1+8, y1+3)).filter(ImageFilter.GaussianBlur(1.0)); o.paste(band, (x0-8, y0-3)); return o
for r in [(52,112,70,780),(130,148,70,300),(160,262,70,1311),(275,330,70,700),(346,364,70,300),(380,420,70,565)]:
    im = wipe(im, *r)
im.save('plate_clean.png')
# vertical remap: stretch top sky band and bottom lawn band, keep middle 1:1
W, H = im.size; TH = round(W*9/16)
add = TH - H
top_src, bot_src = 150, 130          # source rows stretched
top_out = top_src + int(add*0.42); bot_out = bot_src + (add - int(add*0.42))
mid = im.crop((0, top_src, W, H-bot_src))
t = im.crop((0, 0, W, top_src)).resize((W, top_out), Image.BICUBIC)
b = im.crop((0, H-bot_src, W, H)).resize((W, bot_out), Image.BICUBIC)
c = Image.new('RGB', (W, TH)); c.paste(t,(0,0)); c.paste(mid,(0,top_out)); c.paste(b,(0,top_out+mid.height))
c.save('plate_169.png'); print(c.size, top_out, mid.height, bot_out)
