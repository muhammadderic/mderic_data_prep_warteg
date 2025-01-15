# mderic_data_prep_warteg

**utils** folder


## ✨ Features
- quick_profile simply analyzes a DataFrame and returns metadata


## 🛠️ Usage
for installing look at the main readme file :)

```python
from mderic_data_prep_warteg import quick_profile

profile = quick_profile(df)
```

## Example Output
```python
{
    'shape': (rows, cols),
    'missing_values': {'col1': count, ...},
    'numerical_columns': [...],
    'categorical_columns': [...],
    'high_cardinality': [...],
    'possible_target': 'Survived'  # if exists, otherwise None
}
```


## 👤 Author
muhammadderic – [@muhammadderic](https://github.com/muhammadderic)