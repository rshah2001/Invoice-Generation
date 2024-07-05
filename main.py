import pandas as pd
import glob

# glob.glob will return all file paths that match a specific pattern
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # excels have multipe sheets in one document so having the sheet name is mandatory
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
