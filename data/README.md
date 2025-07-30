# Data Folder

This folder contains all datasets used in the **Liverpool Crime Analysis Project**.  
All files are stored as **ZIP archives** and are automatically downloaded and extracted by the notebooks – you do **not** need to unzip or move them manually.

---

## Dataset Overview

The dataset consists of **street-level crime data for Merseyside**, sourced from the official [UK Police Open Data portal](https://data.police.uk/data/).  
It spans **June 2024 to May 2025**, covering a full year of recorded crime incidents in the Merseyside Police jurisdiction.

---

## Included Files

### `liverpool_crime_data.zip`
- Combined dataset of all original raw CSVs for June 2024 – May 2025.
- Created by the notebook:  
  ➤ `/notebooks/data-concatenation.ipynb`  
- Replaces storing the original individual monthly CSV files.

### `clean_data.zip`
- First cleaned dataset created in:  
  ➤ `/notebooks/sql-cleaning.ipynb`  
- Contains cleaned, combined data ready for further checks in Python.

### `clean_data_final.zip`
- Final cleaned dataset created in:  
  ➤ `/notebooks/py-cleaning.ipynb`  
- This version is used in all EDA and dashboard notebooks.

---

## Data Processing Notes

- All notebooks pull data directly from these ZIP files using `requests` and `zipfile`.  
- **Do not rename or move these files**, as the notebooks expect these exact paths.  
- The original raw monthly CSVs (from [data.police.uk](https://data.police.uk/data/)) are not stored individually here – they are concatenated into `liverpool_crime_data.zip` to save space.

---

## Source

If you want to download the raw data yourself:  
▶️ [https://data.police.uk/data/](https://data.police.uk/data/)  
- Select **"Merseyside Police"**  
- Choose the date range: **June 2024 – May 2025**

---
