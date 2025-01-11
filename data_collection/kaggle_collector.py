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