from pathlib import Path
import pandas as pd

from src.cleaner import clean_dataframe


class ProjectParser:

    def __init__(self, data_folder="data"):
        self.data_folder = Path(data_folder)

    def load_projects(self):

        projects = []

        excel_files = self.data_folder.glob("*.xlsx")

        for file in excel_files:

            workbook = pd.ExcelFile(file)

            for sheet in workbook.sheet_names:

                # Ignore Summary and Comments sheets
                if sheet.lower() in ["summary", "comments"]:
                    continue

                df = pd.read_excel(file, sheet_name=sheet)

                df = clean_dataframe(df)

                projects.append({

                    "file_name": file.name,

                    "sheet_name": sheet,

                    "data": df

                })

        return projects