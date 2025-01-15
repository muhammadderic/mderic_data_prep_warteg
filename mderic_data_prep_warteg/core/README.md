# mderic_data_prep_warteg

**utils** folder


## ✨ Features
- suggest_config automatically generates a recommended preprocessing configuration based on the given data profile dictionary
- run_pipeline applies a sequence of preprocessing steps (defined in a config dictionary) to a given pandas.DataFrame


## 🛠️ Usage
for installing look at the main readme file :)

```python
from mderic_data_prep_warteg import suggest_config, run_pipeline

config = suggest_config(profile)
new_df = run_pipeline(df, config)
```


## 👤 Author
muhammadderic – [@muhammadderic](https://github.com/muhammadderic)