import pandas as pd
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "star_classification.csv"

def load_df() -> pd.DataFrame: return pd.read_csv(PATH)

df: pd.DataFrame = load_df()
def get_dataset_shape(df: pd.DataFrame) -> tuple[int, int]: return df.shape

def get_column_names(df: pd.DataFrame) -> list[str]: return df.columns.tolist()

def get_column_types(df: pd.DataFrame) -> pd.Series: return df.dtypes

def get_head(df: pd.DataFrame) -> pd.DataFrame: return df.head()

def describe_dataset(df: pd.DataFrame) -> pd.DataFrame: return df.describe(include='all')

def count_missing_value(df: pd.DataFrame) -> pd.Series: return df.isna().sum()

def count_dublicates(df: pd.DataFrame) -> int: return df.duplicated().sum()
