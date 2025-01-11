import os
import zipfile
import subprocess
from typing import List

def download_competition_dataset_colab(competition_name: str) -> List[str]:
    """
    Downloads a Kaggle competition dataset in Google Colab, extracts it,
    and recursively extracts any nested zip files until raw CSV/XLSX files are exposed.

    Args:
        competition_name (str): The name of the Kaggle competition.

    Returns:
        List[str]: List of final extracted data file paths (csv/xlsx).
    """
    try:
        from google.colab import files
        print("📎 Please upload your kaggle.json file.")
        files.upload()
    except ImportError:
        raise RuntimeError("This function is intended to be used inside Google Colab.")

    kaggle_dir = "/root/.kaggle"
    os.makedirs(kaggle_dir, exist_ok=True)

    if not os.path.exists("kaggle.json"):
        raise FileNotFoundError("❌ kaggle.json not found in working directory after upload.")

    subprocess.run(["mv", "kaggle.json", f"{kaggle_dir}/kaggle.json"], check=True)
    subprocess.run(["chmod", "600", f"{kaggle_dir}/kaggle.json"], check=True)

    print(f"📥 Downloading dataset: {competition_name}")
    subprocess.run(["kaggle", "competitions", "download", "-c", competition_name], check=True)

    zip_file = f"{competition_name}.zip"
    if not os.path.exists(zip_file):
        raise FileNotFoundError(f"❌ Zip file '{zip_file}' not found.")

    extract_dir = competition_name
    os.makedirs(extract_dir, exist_ok=True)

    # Extract main zip
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_dir)
    print("✅ Main dataset zip extracted.")

    # Recursively extract all zip files inside (into their parent folder)
    for root, _, files in os.walk(extract_dir):
        for file in files:
            if file.endswith(".zip"):
                nested_zip_path = os.path.join(root, file)
                parent_dir = root  # extract here, not into a subfolder
                with zipfile.ZipFile(nested_zip_path, "r") as zip_ref:
                    zip_ref.extractall(parent_dir)
                print(f"📦 Extracted nested zip: {file} into {parent_dir}")
                os.remove(nested_zip_path)  # Optional cleanup

    # Collect final CSV/XLSX files
    extracted_data_files = []
    for root, _, files in os.walk(extract_dir):
        for file in files:
            if file.endswith((".csv", ".xlsx")):
                extracted_data_files.append(os.path.join(root, file))

    if not extracted_data_files:
        print("⚠️ No data files (.csv/.xlsx) found after extraction.")
    else:
        print("📄 Extracted data files:", extracted_data_files)

    return extracted_data_files


def download_kaggle_dataset_colab(dataset: str, extract_path: str = "/content/data") -> List[str]:
    """
    Download and extract a dataset from Kaggle inside Google Colab.

    Parameters:
        dataset (str): Kaggle dataset slug (e.g., 'zynicide/wine-reviews').
        extract_path (str): Path to extract dataset contents. Defaults to /content/data.

    Returns:
        List[str]: List of extracted filenames.
    """
    try:
        from google.colab import files
    except ImportError:
        raise RuntimeError("This function is intended to be used inside Google Colab.")

    print("📎 Please upload your kaggle.json file.")
    files.upload()

    kaggle_dir = "/root/.kaggle"
    os.makedirs(kaggle_dir, exist_ok=True)

    if not os.path.exists("kaggle.json"):
        raise FileNotFoundError("❌ kaggle.json not found in current Colab directory.")

    subprocess.run(["mv", "kaggle.json", os.path.join(kaggle_dir, "kaggle.json")], check=True)
    subprocess.run(["chmod", "600", os.path.join(kaggle_dir, "kaggle.json")], check=True)

    # Download dataset
    dataset_slug = dataset.split("/")[-1]
    zip_file = f"{dataset_slug}.zip"
    print(f"📥 Downloading dataset: {dataset}")
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset], check=True)

    # Extract the zip
    os.makedirs(extract_path, exist_ok=True)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zip_file)

    # Unzip inner zip files (flat into extract_path)
    for file in os.listdir(extract_path):
        file_path = os.path.join(extract_path, file)
        if file.endswith(".zip"):
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(extract_path)
            os.remove(file_path)

    extracted = sorted(os.listdir(extract_path))
    print("✅ Extracted files:", extracted)
    return extracted
