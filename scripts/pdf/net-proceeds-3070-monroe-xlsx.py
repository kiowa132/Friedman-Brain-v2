# -*- coding: utf-8 -*-
"""Formula-driven net proceeds workbook for 3070 Monroe St (Samuel Watson).
Yellow cells are editable inputs; everything else is a formula.
Run: py scripts/pdf/net-proceeds-3070-monroe-xlsx.py
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\3070-monroe-st\Net-Proceeds-3070-Monroe-St.xlsx"

wb = Workbook(); ws = wb.active; ws.title = "Net Proceeds"
teal = "0F5C63"; gold = "C9A96A"; cream = "FAF8F5"; yellow = "FFF3B0"
HF = Font(bold=True, color="FFFFFF"); H = PatternFill("solid", fgColor=teal)
Y = PatternFill("solid", fgColor=yellow); C = PatternFill("solid", fgColor=cream)
B = Font(bold=True); money = '#,##0;(#,##0)'; pct = '0.00%'
thin = Border(*(Side(style="thin", color="D9D2C4"),)*4)

ws.column_dimensions["A"].width = 46
for col in ("B","C","D"): ws.column_dimensions[col].width = 16

ws["A1"] = "3070 Monroe St, Manchester MD 21102 - Estimated Net Proceeds"; ws["A1"].font = Font(bold=True, size=13, color=teal)
ws["A2"] = "The Friedman Team | Kyle Friedman 443-789-3101 | yellow cells are editable"; ws["A2"].font = Font(italic=True, color="5B6B6E", size=9)

r = 4
ws.cell(r,1,"Scenario").fill = H; ws.cell(r,1).font = HF
for i,c in enumerate(("B","C","D")):
    ws.cell(r,2+i, f"List {i+1}").fill = H; ws.cell(r,2+i).font = HF

r += 1
ws.cell(r,1,"Sale price").font = B
for i,v in enumerate((319900,329900,339900)):
    cell = ws.cell(r,2+i,v); cell.fill = Y; cell.number_format = money
price_row = r

r += 1
ws.cell(r,1,"Commission %").font = B
for i in range(3):
    cell = ws.cell(r,2+i,0.05); cell.fill = Y; cell.number_format = pct
comm_row = r

r += 1
ws.cell(r,1,"Carroll County transfer + recordation, seller share %").font = B
for i in range(3):
    cell = ws.cell(r,2+i,0.009); cell.fill = Y; cell.number_format = pct
xfer_row = r

r += 1
ws.cell(r,1,"Settlement / closing fee")
for i in range(3):
    cell = ws.cell(r,2+i,500); cell.fill = Y; cell.number_format = money
fee_row = r

r += 1
ws.cell(r,1,"Deed & doc prep")
for i in range(3):
    cell = ws.cell(r,2+i,200); cell.fill = Y; cell.number_format = money
deed_row = r

r += 1
ws.cell(r,1,"Payoff processing & lien release")
for i in range(3):
    cell = ws.cell(r,2+i,200); cell.fill = Y; cell.number_format = money
lien_row = r

r += 1
ws.cell(r,1,"Wire, courier & notary")
for i in range(3):
    cell = ws.cell(r,2+i,150); cell.fill = Y; cell.number_format = money
wire_row = r

r += 1
ws.cell(r,1,"Termite / WDI inspection")
for i in range(3):
    cell = ws.cell(r,2+i,100); cell.fill = Y; cell.number_format = money
term_row = r

r += 1
ws.cell(r,1,"Seller concession / repairs / warranty (optional)")
for i in range(3):
    cell = ws.cell(r,2+i,0); cell.fill = Y; cell.number_format = money
conc_row = r

r += 1
ws.cell(r,1,"Total estimated costs").font = B
for i,col in enumerate(("B","C","D")):
    f = (f"={col}{price_row}*{col}{comm_row}+{col}{price_row}*{col}{xfer_row}"
         f"+{col}{fee_row}+{col}{deed_row}+{col}{lien_row}+{col}{wire_row}+{col}{term_row}+{col}{conc_row}")
    cell = ws.cell(r,2+i,f); cell.number_format = money; cell.font = B
tot_row = r

r += 1
ws.cell(r,1,"NET BEFORE LOAN PAYOFF").font = Font(bold=True, color=teal)
for i,col in enumerate(("B","C","D")):
    cell = ws.cell(r,2+i, f"={col}{price_row}-{col}{tot_row}")
    cell.number_format = money; cell.font = Font(bold=True, color=teal); cell.fill = PatternFill("solid", fgColor=gold)
netbp_row = r

r += 1
ws.cell(r,1,"Net as % of sale price")
for i,col in enumerate(("B","C","D")):
    cell = ws.cell(r,2+i, f"={col}{netbp_row}/{col}{price_row}"); cell.number_format = pct
r += 1
ws.cell(r,1,"Estimated loan balance (not a payoff statement)").font = B
for i in range(3):
    cell = ws.cell(r,2+i,109068); cell.fill = Y; cell.number_format = money
payoff_row = r

r += 1
ws.cell(r,1,"ESTIMATED NET TO YOU").font = Font(bold=True, color=teal, size=12)
for i,col in enumerate(("B","C","D")):
    cell = ws.cell(r,2+i, f"={col}{netbp_row}-{col}{payoff_row}")
    cell.number_format = money; cell.font = Font(bold=True, color=teal, size=12); cell.fill = C

r += 2
for line in [
  "Assumptions:",
  "- Estimate only, not a closing disclosure.",
  "- Commission 5.0% is a placeholder, negotiable, set in the listing agreement.",
  "- Carroll County has no local transfer tax; MD state transfer (0.5%) + Carroll recordation ($6.50/$500,",
  "  about 1.3%) shown at seller customary half share (~0.9% combined). Exact split per contract, confirm with title.",
  "- Estimated loan balance: $109,068 (Sept 2026). This is an estimate, not a payoff statement - actual",
  "  payoff may differ slightly with per-diem interest and fees. Confirm with a current statement before closing.",
  "- List range $319,900-$339,900 brackets the market-evidence pricing from 9 Manchester 21102 comps",
  "  (average closed price $342,875, average 99.3% sold-to-list, RPR/Bright MLS, Sept 2026).",
  "- Section 121: primary residence 2 of last 5 yrs excludes first 250k gain (single) / 500k (MFJ) from",
  "  federal tax. Purchased 2010 for $149,900, so gain is well under that threshold at every scenario.",
  "  Confirm with CPA.",
]:
    ws.cell(r,1,line).font = Font(italic=True, color="5B6B6E", size=9); r += 1

wb.save(OUT); print("wrote", OUT)
