# 📂 Data Directory

This folder was intended to contain the data used throughout the Liverpool Crime Analysis project, as well as any acquisation or concatenation processes.

---

## Dataset Overview

The primary dataset used in this project is **street-level crime data for Liverpool** sourced from the official UK Police API and Open Data portal. It spans **June 2024 through May 2025**, covering a full year of recorded incidents.

---

## Why the Data Isn’t Included

The combined CSV file (`liverpool_crime_data.csv`) exceeds GitHub’s 25MB file size limit and therefore is **not included** in this repository.

---

## How to Access the Data

You can obtain the same data directly from the official police data website:

▶️ [https://data.police.uk/data/](https://data.police.uk/data/)

When downloading:

- Select **"Merseyside Police"**
- Choose date range: **June 2024 – May 2025**
- Download the **street-level crime data (CSV format)**

Once downloaded, save the files in this `/data` folder and run the provided preprocessing script (`crime_data_concatenation.py`) to combine them into a single dataset.

---


