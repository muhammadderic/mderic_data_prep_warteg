# mderic_data_prep_warteg

**mderic_data_prep_warteg** is a modular Python library for building your own data preparation — from collecting data (e.g., from Kaggle), understanding the structure of dataframes, to handling missing values and other preprocessing tasks.

This toolkit is especially helpful for use in **Google Colab** and supports easy plug-and-play steps, so developers can customize their pipeline like:


## ✨ Features

- Collect datasets and competition data from Kaggle (Colab-ready)


## 🧱 Project Structure

```
my\_pandas\_tools/
└── data\_collection/
    ├── **init**.py
    └── kaggle\_collector.py

````

## 🚀 Installation

You can install the package directly from GitHub (if hosted there):

```bash
pip install git+https://github.com/muhammadderic/mderic_data_prep_warteg.git
````

## 🛠️ Usage

*on progress*


## 📁 Developing Your Own Steps

Each module (`data_collection`, `data_understanding`, `data_preparation`) can have many functions or classes. You can expand the system by:

* Adding new collector functions (e.g., from APIs, Google Sheets, etc.)


## 📋 Requirements

* Python 3.7+
* pandas
* kaggle (only if using Kaggle data)
* Google Colab (for some features like file upload)


## 📄 License

MIT License


## 👤 Author

muhammadderic – [@muhammadderic](https://github.com/muhammadderic)