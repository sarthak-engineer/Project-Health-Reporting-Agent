import pandas as pd
from pathlib import Path
from src.cleaner import clean_dataframe

DATA_FOLDER = Path("data")

excel_files = list(DATA_FOLDER.glob("*.xlsx"))

print("=" * 80)
print("PROJECT HEALTH REPORTING AGENT")
print("=" * 80)

for file in excel_files:

    print(f"\n📄 File: {file.name}")

    workbook = pd.ExcelFile(file)

    print("\nAvailable Sheets:")
    for sheet in workbook.sheet_names:
        print(f"   • {sheet}")

    print("\n" + "-" * 80)

    for sheet in workbook.sheet_names:

        print(f"\n📑 Sheet: {sheet}")

        df = pd.read_excel(file, sheet_name=sheet)

        df = clean_dataframe(df)
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        for column in df.columns:
            print(f"   - {column}")

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\n" + "=" * 80)