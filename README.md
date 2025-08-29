# Liverpool Crime Analysis Project

## 1. Website
The interactive dashboard has been deployed on my website.  
Please click the link below to explore:

👉 [Liverpool Crime Dashboard](https://james-jackson-ds.fly.dev/crime))

## 2. Project Overview
This project analyses Merseyside Police crime data (June 2024 – May 2025) to uncover trends, hotspots, and insights related to public safety. The project includes multiple phases: data cleaning, exploratory data analysis (EDA), interactive dashboarding, and reporting.

All data is pulled directly from **GitHub-hosted ZIP files** so you do **not** need to manually download any files locally.

---

## 3. Data Source
The dataset is sourced from [data.police.uk](https://data.police.uk/), containing all reported crime data for the Merseyside Police region.  
**Timeframe:** June 2024 – May 2025.  

Original raw CSV files have been concatenated and cleaned into the following versions:
- `liverpool_crime_data.zip` – Combined raw dataset  
- `clean_data.zip` – First cleaned version (SQL cleaning)  
- `clean_data_final.zip` – Final cleaned dataset used for EDA & dashboards  

---

## 4. Tools and Technologies
The project was developed entirely in Python using Jupyter notebooks.  
Key libraries include:
- **Data processing:** `pandas`, `numpy`, `sqlalchemy`
- **Visualisation:** `matplotlib`, `seaborn`, `plotly`
- **Geospatial analysis:** `geopandas`, `shapely`
- **Interactivity:** `ipywidgets`
- **Other utilities:** `requests`, `zipfile`, `io`, `os`

A full list of dependencies can be found in **requirements.txt**.

---

## 5. Repository Structure
```
├── data/                # All raw and cleaned datasets (zipped)
├── notebooks/           # 8 Jupyter notebooks (data prep, EDA, dashboards)
├── visualisations/      # Saved PNG/PDF plots from EDA and EDA2
├── tables/              # Exported Excel summary tables (aggregated stats)
├── requirements.txt     # Python dependencies for the project
└── README.md            # This file
```

> 📌 *Each folder has its own `README.md` explaining its contents.*

---

## 6. Notebook Pipeline
There are **8 notebooks**, each documented in `/notebooks/README.md`:
1. **data-concatenation.ipynb** – Merge raw CSVs into a single dataset  
2. **sql-cleaning.ipynb** – SQL-based cleaning → `clean_data.csv`  
3. **py-cleaning.ipynb** – Python validation & datetime conversion → `clean_data_final.csv`  
4. **EDA.ipynb** – First exploratory analysis and visualisations  
5. **excel-data.ipynb** – Export key summary tables for Excel analysis  
6. **EDA2.ipynb** – Secondary EDA (crime & outcome group analysis)  
7. **dashboard.ipynb** – Build individual interactive Plotly & hexbin plots  
8. **final-dashboard.ipynb** – Fully integrated interactive dashboard  

---

## 7. Outputs
- **Plots:** All visualisations are saved in `/visualisations/` (EDA & EDA2)  
- **Excel Tables:** Percentage-based summary tables (by region, crime group, outcome group) in `/tables/`  
- **Interactive Dashboard:** A Plotly dashboard built in `final-dashboard.ipynb`  

---

## 8. Contact
**Author:** James Jackson  
📧 Email: jamesneiljackson@gmail.com  

---
