import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# glob.glob will return all file paths that match a specific pattern
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # excels have multiple sheets in one document so having the sheet name is mandatory
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # P stands for portrait
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, invoice_date = filename.split("-")

    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}", ln=1)

    # Header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Adding rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/Invoice {invoice_nr}.pdf")
