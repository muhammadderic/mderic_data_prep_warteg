import pandas as pd
import numpy as np

def run_pipeline(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    df = df.copy()  # Avoid changing original data

    for step in config.get("steps", []):
        for step_name, params in step.items():

            if step_name == "fill_missing":
                columns = params.get("columns", [])
                method = params.get("method", "mean")
                for col in columns:
                    if col not in df.columns:
                        continue
                    if method == "mean":
                        value = df[col].mean()
                    elif method == "median":
                        value = df[col].median()
                    elif method == "mode":
                        value = df[col].mode().iloc[0]
                    else:
                        continue  # Unknown method
                    df[col] = df[col].fillna(value)

            elif step_name == "encode_categorical":
                columns = params.get("columns", [])
                df = pd.get_dummies(df, columns=columns, drop_first=False).astype(int)

            elif step_name == "scale":
                columns = params.get("columns", [])
                method = params.get("method", "minmax")
                for col in columns:
                    if col not in df.columns:
                        continue
                    if method == "minmax":
                        min_val = df[col].min()
                        max_val = df[col].max()
                        if max_val - min_val != 0:
                            df[col] = (df[col] - min_val) / (max_val - min_val)
                        else:
                            df[col] = 0.0
                    elif method == "standard":
                        mean_val = df[col].mean()
                        std_val = df[col].std()
                        if std_val != 0:
                            df[col] = (df[col] - mean_val) / std_val
                        else:
                            df[col] = 0.0

    return df