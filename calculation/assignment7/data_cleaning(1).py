import pandas as pd
from exceptions import DataCleaningError

def load_data(file_name):
    try:
        df = pd.read_csv(file_name)
        return df
    except pd.errors.EmptyDataError:
        raise DataCleaningError("No data in the file.")
    except pd.errors.ParserError:
        raise DataCleaningError("Error parsing the file.")
    except FileNotFoundError:
        raise DataCleaningError(f"File {file_name} not found.")

def clean_data(df):
    print("Missing values per column:")
    print(df.isna().sum())
    print("Number of duplicate rows:")
    print(df.duplicated().sum())
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df
