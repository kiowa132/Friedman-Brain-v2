"""
fill-pdf.py — stamp values onto a flat PDF using a field-map.

Works on PDFs that have NO form fields (SkySlope exports). Draws each
value as text on a transparent overlay at mapped coordinates, then merges
onto the template.

Coordinates in the field-map are PDF points, origin BOTTOM-LEFT.

Usage:
  python fill-pdf.py --template T.pdf --map M.json --data V.json --out FILLED.pdf
  python fill-pdf.py --template T.pdf --map M.json --demo --out DEMO.pdf   # placeholder text

field-map format (JSON):
{
  "font": "Helvetica", "size": 10,
  "fields": {
    "property_street": {"page": 1, "x": 180, "y": 632, "size": 10, "max_width": 390},
    "for_sale_check":   {"page": 1, "x": 402, "y": 500, "text": "X", "size": 12}
  }
}
- page is 1-based
- max_width (optional): shrink font to fit that width
- text (optional): fixed text to stamp regardless of data (e.g. an "X")
- align: "left" (default) | "center" | "right"  (x is the anchor)
"""
import sys, json, io
import pypdf
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth


def arg(name, default=None):
    if name in sys.argv:
        i = sys.argv.index(name)
        return sys.argv[i + 1] if i + 1 < len(sys.argv) else True
    return default


def main():
    tmpl = arg("--template")
    mapf = arg("--map")
    dataf = arg("--data")
    out = arg("--out")
    demo = "--demo" in sys.argv
    if not (tmpl and mapf and out):
        sys.exit("need --template --map --out")

    fmap = json.load(open(mapf, encoding="utf-8-sig"))
    default_font = fmap.get("font", "Helvetica")
    default_size = fmap.get("size", 10)
    data = {} if demo else json.load(open(dataf, encoding="utf-8-sig"))

    reader = pypdf.PdfReader(tmpl)
    npages = len(reader.pages)

    # group fields by page
    by_page = {}
    for fname, spec in fmap["fields"].items():
        by_page.setdefault(int(spec["page"]), []).append((fname, spec))

    writer = pypdf.PdfWriter()
    for pidx in range(npages):
        page = reader.pages[pidx]
        pw = float(page.mediabox.width)
        ph = float(page.mediabox.height)
        fields = by_page.get(pidx + 1, [])
        if fields:
            buf = io.BytesIO()
            c = canvas.Canvas(buf, pagesize=(pw, ph))
            for fname, spec in fields:
                val = spec.get("text")
                if val is None:
                    val = data.get(fname, f"[{fname}]" if demo else "")
                val = str(val)
                if val == "":
                    continue
                size = spec.get("size", default_size)
                font = spec.get("font", default_font)
                mw = spec.get("max_width")
                if mw:
                    while size > 5 and stringWidth(val, font, size) > mw:
                        size -= 0.5
                c.setFont(font, size)
                c.setFillColorRGB(0.05, 0.05, 0.35) if demo else c.setFillColorRGB(0, 0, 0)
                x, y = float(spec["x"]), float(spec["y"])
                align = spec.get("align", "left")
                if align == "center":
                    c.drawCentredString(x, y, val)
                elif align == "right":
                    c.drawRightString(x, y, val)
                else:
                    c.drawString(x, y, val)
            c.save()
            buf.seek(0)
            overlay = pypdf.PdfReader(buf).pages[0]
            page.merge_page(overlay)
        writer.add_page(page)

    with open(out, "wb") as f:
        writer.write(f)
    print(f"wrote {out} ({npages} pages, {sum(len(v) for v in by_page.values())} field stamps)")


if __name__ == "__main__":
    main()
