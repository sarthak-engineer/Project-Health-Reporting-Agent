import pandas as pd
import numpy as np


def clean_dataframe(df):

    if df.empty:
        return df

    # Remove extra spaces from column names
    df.columns = [str(col).strip() for col in df.columns]

    # Replace Excel parsing errors
    df.replace("#UNPARSEABLE", np.nan, inplace=True)

    # Convert % Complete to numeric
    if "% Complete" in df.columns:
        df["% Complete"] = pd.to_numeric(
            df["% Complete"],
            errors="coerce"
        )

        # Convert decimal percentages (0.44) to actual percentages (44)
        mask = df["% Complete"] <= 1
        df.loc[mask, "% Complete"] = df.loc[mask, "% Complete"] * 100

    # Convert date columns
    date_columns = [
        "Start Date",
        "End Date",
        "Baseline Start",
        "Baseline Finish",
        "Baseline Start2",
        "Baseline Finish2"
    ]

    for col in date_columns:

        if col in df.columns:

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    # Fill text columns
    text_columns = [
        "Comments",
        "Status Comment"
    ]

    for col in text_columns:

        if col in df.columns:

            df[col] = df[col].fillna(
                "No comments provided"
            )

    return df