# mderic_data_prep_warteg

**mderic_data_prep_warteg** is a Python library designed to simplify and automate the data preparation process for machine learning and data analysis workflows. Built with flexibility and ease of use in mind, it allows users to prepare their datasets using smart, configurable pipelines. 

The library supports both local and Google Colab environments, and can be installed directly from GitHub via pip. 

Users can automatically analyze their data using the *quick_profile()* function, generate recommended preprocessing configurations with *suggest_config()*, and apply those transformations through *run_pipeline()*. With a modular structure and support for YAML/JSON configs, the library makes the data preparation process easier, more transparent, and adaptable.


## ✨ Features

- Collect datasets and competition data from Kaggle (Colab-ready)


## 🧱 Project Structure

```
my\_pandas\_tools/
├── data\_collection/
|   ├── **init**.py
|   └── kaggle\_collector.py
└── utils/
    └── profiling.py
````

## 🚀 Installation

You can install the package directly from GitHub (if hosted there):

```bash
pip install git+https://github.com/muhammadderic/mderic_data_prep_warteg.git
````

## 🛠️ Usage

```python
from data_collection.kaggle_collector import download_competition_dataset_colab, download_kaggle_dataset_colab
```


## 📋 Requirements

* Python 3.7+
* pandas
* kaggle (only if using Kaggle data)
* Google Colab (for some features like file upload)


## 📄 License

MIT License


## 👤 Author

muhammadderic – [@muhammadderic](https://github.com/muhammadderic)