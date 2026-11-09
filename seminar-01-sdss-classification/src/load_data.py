import pandas as pd
from pathlib import Path
from functools import cache

PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "star_classification.csv"

def load_df() -> pd.DataFrame: return pd.read_csv(PATH)

def dimension_of_dataset() -> tuple[int, int]: return load_df().shape

def columns_names() -> list[str]: return load_df().columns.tolist()

def data_types_columns() -> pd.Series: return load_df().dtypes

def first_five_rows() -> pd.DataFrame: return load_df().head()

def describe_dataset() -> pd.DataFrame: return load_df().describe(include='all')

def missing_value() -> pd.Series: return load_df().isna().sum()

def count_dublicates() -> pd.Series: return load_df().duplicated().sum()

