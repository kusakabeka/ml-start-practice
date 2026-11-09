import pandas as pd
from load_data import load_df
import matplotlib.pyplot as plt
from pathlib import Path

def get_class_distribution(df: pd.DataFrame) -> pd.Series: return df["class"].value_counts(normalize=True)

def get_class_counts(df: pd.DataFrame): return df["class"].value_counts()

def plot_class_distribution(class_counts: pd.Series, outputh_path: Path) -> None:
    fig, ax = plt.subplots()

    ax.bar(class_counts.index, class_counts.values)
    ax.set_title("class distribution")
    ax.set_xlabel("class")
    ax.set_ylabel("number of objects")

    fig.savefig(outputh_path, dpi=300, bbox_inches="tight")

def plot_feature_boxplot(df: pd.DataFrame, features: list[str], outputh_path: Path) -> None:
    pass

def main() -> None:
    df: pd.DataFrame = load_df().copy()
    project_dir = Path(__file__).resolve().parent.parent
    figures_dir = project_dir / "reports" / "figures"

    class_distribution = get_class_distribution(df)
    class_counts = get_class_counts(df)

    print(class_distribution)
    print(class_counts)

    #outputh_path = figures_dir / "class_distribution.png"
    #plot_class_distribution(class_counts, outputh_path)

main()
