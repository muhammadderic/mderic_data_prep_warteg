import os
import zipfile
import subprocess
from typing import List

def download_competition_dataset_colab(competition_name: str) -> List[str]:
    """
    Sets up the Kaggle API in Google Colab, downloads and extracts the dataset.

    Args:
        competition_name (str): The name of the Kaggle competition (e.g., 'titanic').

    Returns:
        List[str]: List of extracted filenames.
    """
    try:
        from google.colab import files
        print("Please upload your kaggle.json file.")
        files.upload()
    except ImportError:
        raise RuntimeError("This function is intended to be used inside Google Colab.")

    kaggle_dir = "/root/.kaggle"
    os.makedirs(kaggle_dir, exist_ok=True)

    if not os.path.exists("kaggle.json"):
        raise FileNotFoundError("kaggle.json not found in working directory after upload.")

    # Move and set permissions
    subprocess.run(["mv", "kaggle.json", f"{kaggle_dir}/kaggle.json"], check=True)
    subprocess.run(["chmod", "600", f"{kaggle_dir}/kaggle.json"], check=True)

    # Download dataset
    print(f"📥 Downloading dataset: {competition_name}")
    subprocess.run(["kaggle", "competitions", "download", "-c", competition_name], check=True)

    # Extract dataset
    zip_file = f"{competition_name}.zip"
    if not os.path.exists(zip_file):
        raise FileNotFoundError(f"Zip file '{zip_file}' not found.")

    extract_dir = competition_name
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

    print("✅ Dataset extracted successfully.")

    # Return list of extracted files
    return os.listdir(extract_dir)
