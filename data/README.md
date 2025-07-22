# Data Directory

This folder contains the data used in the **Liverpool Crime Analysis** project, including both raw and cleaned versions, saved in compressed `.zip` format due to GitHub file size constraints.

---

## Dataset Overview

The dataset consists of **street-level crime data for Liverpool**, sourced from the official UK Police Open Data portal.  
It spans **June 2024 to May 2025**, covering a full year of recorded crime incidents in the Merseyside Police jurisdiction.

---

## Included Files

### `raw_data.zip`
- Contains the original monthly CSVs as downloaded from the UK Police data portal.
- Used as the starting point for data cleaning and concatenation.

### `clean_data.csv`
- Fully cleaned, combined dataset used for EDA and Power BI.
- Cleaned steps included:
  - Normalized column names (snake_case)
  - Dropped irrelevant fields (`context`, `reported_by`, `falls_within`)
  - Handled missing values (`ASB_FILL` placeholder used for missing IDs as all instances are anti-social behaviour)
  - Ensured consistent values and formats
  - Parsed `month` field as datetime

### `clean_data.zip`
- Compressed version of `clean_data.csv` for GitHub storage.

---

## Data Processing Notes

- Data contatenation is handled in the notebook:  
  ➤ `/notebooks/data-contatenation.ipynb`

- All data processing and cleaning is handled in the notebook:  
  ➤ `/notebooks/sql-data-cleansing.ipynb`

---

## Source

If you'd like to download the raw data yourself, use:  
▶️ [https://data.police.uk/data/](https://data.police.uk/data/)

- Select **"Merseyside Police"**
- Choose the date range: **June 2024 – May 2025**

---



