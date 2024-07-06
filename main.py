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
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}")
    pdf.output(f"PDFs/Invocie {invoice_nr}.pdf")

