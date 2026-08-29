"""
render-grid.py — render each page of a PDF to a PNG with a coordinate grid,
so field positions can be mapped by eye.

Grid + labels are in PDF points (72 pt = 1 inch), origin BOTTOM-LEFT —
the same coordinate space the fill script (reportlab) uses.

Usage:
  python render-grid.py <input.pdf> <out_dir> [--dpi 150] [--step 25]
"""
import sys, os
import pymupdf  # PyMuPDF

def main():
    src = sys.argv[1]
    out_dir = sys.argv[2]
    dpi = 150
    step = 25
    for i, a in enumerate(sys.argv):
        if a == "--dpi": dpi = int(sys.argv[i + 1])
        if a == "--step": step = int(sys.argv[i + 1])
    os.makedirs(out_dir, exist_ok=True)

    scale = dpi / 72.0
    doc = pymupdf.open(src)
    for pno in range(doc.page_count):
        page = doc[pno]
        W, H = page.rect.width, page.rect.height

        # base render
        pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale))
        # draw grid onto a fresh page overlay via a temp pixmap -> use PIL
        from PIL import Image, ImageDraw, ImageFont
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        d = ImageDraw.Draw(img, "RGBA")
        try:
            font = ImageFont.truetype("arial.ttf", 11)
        except Exception:
            font = ImageFont.load_default()

        def X(x_pt): return x_pt * scale
        def Y(y_pt): return (H - y_pt) * scale  # flip: PDF y from bottom -> image y from top

        # minor + labeled lines
        x = 0
        while x <= W:
            major = (x % 100 == 0)
            col = (0, 90, 200, 120) if major else (0, 90, 200, 45)
            d.line([(X(x), 0), (X(x), pix.height)], fill=col, width=2 if major else 1)
            if major:
                d.text((X(x) + 2, 2), str(int(x)), fill=(0, 60, 160, 255), font=font)
            x += step
        y = 0
        while y <= H:
            major = (y % 100 == 0)
            col = (200, 40, 40, 120) if major else (200, 40, 40, 45)
            d.line([(0, Y(y)), (pix.width, Y(y))], fill=col, width=2 if major else 1)
            if major:
                d.text((2, Y(y) + 2), str(int(y)), fill=(160, 20, 20, 255), font=font)
            y += step

        out = os.path.join(out_dir, f"p{pno + 1:02d}.png")
        img.save(out)
        print(f"  {out}  ({int(W)}x{int(H)} pt)")

    doc.close()

if __name__ == "__main__":
    main()
