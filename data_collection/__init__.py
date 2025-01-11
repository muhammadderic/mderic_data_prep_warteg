"""Package for data collection tools."""

from .kaggle_collector import (
    download_kaggle_dataset_colab,
    download_competition_dataset_colab,
)

__all__ = [
    "download_kaggle_dataset_colab",
    "download_competition_dataset_colab",
]