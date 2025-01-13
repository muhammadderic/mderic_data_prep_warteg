import pandas as pd

def quick_profile(df: pd.DataFrame) -> dict:
    profile = {}

    # Basic shape
    profile["shape"] = df.shape

    # Missing values
    profile["missing_values"] = {
        col: df[col].isna().sum()
        for col in df.columns
        if df[col].isna().sum() > 0
    }

    # Data types
    numerical_cols = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    profile["numerical_columns"] = numerical_cols
    profile["categorical_columns"] = categorical_cols

    # High cardinality categorical columns
    high_cardinality = [
        col for col in categorical_cols
        if df[col].nunique() > 20
    ]
    profile["high_cardinality"] = high_cardinality

    # Guess target column
    common_targets = ["target", "label", "Survived", "Target", "Label"]
    found_target = None
    for col in df.columns:
        if col in common_targets:
            found_target = col
            break
    profile["possible_target"] = found_target

    return profile