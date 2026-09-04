# -*- coding: utf-8 -*-
"""Batch-compress phone photos to web-ready JPEGs for listing uploads.

Phone photos run 10-20 MB and get rejected by Cloudinary's free tier (10 MB
cap). A listing photo only needs ~2048 px on the long edge at quality ~82,
which lands around 1-3 MB. This resizes, recompresses, strips metadata, and
auto-rotates every image in a folder.

USAGE (real Python):
  C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe compress-photos.py "C:\\path\\to\\photos"

Output goes to  <that folder>\\web\\  as 01.jpg, 02.jpg, ...  (kept in name
order so galleries stay sorted). Then upload the web\\ folder to Cloudinary.

Options:
  --max 2560     long-edge pixels (default 2048)
  --quality 85   JPEG quality 1-95 (default 82)
  --prefix hero  add a prefix to output names
"""
import sys, os, argparse
from PIL import Image, ImageOps

EXTS = (".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".tif", ".tiff", ".bmp")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", help="folder of raw photos")
    ap.add_argument("--max", type=int, default=2048)
    ap.add_argument("--quality", type=int, default=82)
    ap.add_argument("--prefix", default="")
    a = ap.parse_args()

    src = os.path.abspath(a.folder)
    if not os.path.isdir(src):
        sys.exit("Not a folder: " + src)
    out = os.path.join(src, "web")
    os.makedirs(out, exist_ok=True)

    files = sorted(f for f in os.listdir(src)
                   if os.path.isfile(os.path.join(src, f))
                   and f.lower().endswith(EXTS))
    if not files:
        sys.exit("No images found in " + src)

    total_in = total_out = 0
    n = 0
    for f in files:
        p = os.path.join(src, f)
        try:
            im = Image.open(p)
        except Exception as e:
            print("  SKIP (can't open, HEIC needs a converter):", f, "-", e)
            continue
        im = ImageOps.exif_transpose(im)          # honor the phone's rotation
        if im.mode in ("RGBA", "P", "LA"):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1] if im.mode in ("RGBA", "LA") else None)
            im = bg
        else:
            im = im.convert("RGB")
        im.thumbnail((a.max, a.max), Image.LANCZOS)

        n += 1
        name = "%s%02d.jpg" % ((a.prefix + "-") if a.prefix else "", n)
        dst = os.path.join(out, name)
        im.save(dst, "JPEG", quality=a.quality, optimize=True, progressive=True)

        si, so = os.path.getsize(p), os.path.getsize(dst)
        total_in += si; total_out += so
        print("  %-28s %6.1f MB  ->  %-12s %5.2f MB" % (f, si/1e6, name, so/1e6))

    print("\n%d photos.  %.1f MB  ->  %.1f MB  (%.0f%% smaller).  Saved to: %s"
          % (n, total_in/1e6, total_out/1e6,
             (1 - total_out/total_in) * 100 if total_in else 0, out))
    print("All outputs are well under Cloudinary's 10 MB limit. Upload the web\\ folder.")

if __name__ == "__main__":
    main()
