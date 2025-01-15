def suggest_config(profile: dict) -> dict:
    config = {"steps": []}

    # Fill missing - numerical
    numerical_missing = [
        col for col in profile["numerical_columns"]
        if col in profile["missing_values"]
    ]
    if numerical_missing:
        config["steps"].append({
            "fill_missing": {
                "columns": numerical_missing,
                "method": "mean"
            }
        })

    # Fill missing - categorical
    categorical_missing = [
        col for col in profile["categorical_columns"]
        if col in profile["missing_values"]
    ]
    if categorical_missing:
        config["steps"].append({
            "fill_missing": {
                "columns": categorical_missing,
                "method": "mode"
            }
        })

    # Encode categorical
    if profile["categorical_columns"]:
        # Exclude high cardinality cols
        to_encode = [
            col for col in profile["categorical_columns"]
            if col not in profile["high_cardinality"]
        ]
        if to_encode:
            config["steps"].append({
                "encode_categorical": {
                    "columns": to_encode,
                    "method": "onehot"
                }
            })

    # Scale numerical
    if profile["numerical_columns"]:
        config["steps"].append({
            "scale": {
                "columns": profile["numerical_columns"],
                "method": "minmax"
            }
        })

    return config