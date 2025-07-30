# Notebooks Folder

This folder contains all **8 Jupyter notebooks** used in the Liverpool Crime Analysis Project.  
Each notebook represents a distinct stage of the pipeline, from raw data ingestion to dashboard creation.  

All notebooks are designed to **pull data directly from the GitHub `data` folder** using `requests` and `zipfile`.  
You do **not** need to download or unzip any files manually.

---

## Notebook Pipeline (Run in Order)

---

### 1. `data-concatenation.ipynb`
**Purpose:**  
- Combine the 12 original monthly CSVs (June 2024 – May 2025) into a single dataset.  
- Maintain chronological order of data.

**Key actions:**  
- Used `os` and `pandas` to loop through and concatenate CSV files.  
- Verified row counts and inspected the combined head/tail.  

**Output:**  
- `liverpool_crime_data.zip` stored in `/data/`.  

---

### 2. `sql-cleaning.ipynb`
**Purpose:**  
- Perform initial data cleaning and column standardisation using SQL (via SQLAlchemy).

**Key actions:**  
- Dropped unused columns: `context`, `reported_by`, `falls_within`.  
- Normalised column names to `snake_case` (e.g., `Crime type` → `crime_type`).  
- Filled missing `crime_id` for Anti-Social Behaviour records with `ASB_FILL`.  
- Validated categorical values for `crime_type` and `last_outcome_category`.  
- Ensured no future-dated months (beyond May 2025).  

**Output:**  
- `clean_data.zip` stored in `/data/`.  

---

### 3. `py-cleaning.ipynb`
**Purpose:**  
- Validate the SQL-cleaned dataset in Python and apply final adjustments.

**Key actions:**  
- Loaded `clean_data.zip` directly from GitHub.  
- Converted the `month` column to datetime format.  
- Ran detailed checks:  
  - Missing values (none unexpected)  
  - Duplicate `crime_id` (none found)  
  - Summary statistics for numerical and categorical fields  
- Exported final cleaned dataset for EDA.  

**Output:**  
- `clean_data_final.zip` stored in `/data/`.  

---

### 4. `EDA.ipynb` (Exploratory Data Analysis Phase 1)
**Purpose:**  
- Conduct the first round of exploratory analysis to identify key patterns and distributions.

**Key actions:**  
- Loaded `clean_data_final.zip`.  
- Plotted:  
  - Crime type distribution (bar chart)  
  - Outcome category distribution (bar chart)  
  - Top 20 crime locations (bar chart)  
  - Top 20 LSOAs (bar chart)  
  - Monthly crime trends with 3-month rolling average  
  - Monthly trend by crime type (multi-line plot)  
  - Outcome vs crime type (stacked bar and heatmap with log scale)  
- Saved all plots as high-resolution `.png` and `.pdf`.  

**Output:**  
- Visualisations saved in `/visualisations/`.  

---

### 5. `excel-data.ipynb`
**Purpose:**  
- Export key summary tables for deeper Excel-based percentage analysis.

**Key actions:**  
- Generated tables aggregating crimes by:  
  - Region  
  - Crime group  
  - Outcome group  
- Exported to Excel with separate sheets for each view.  
- These tables were later colour-coded in Excel to highlight:  
  - 5 key regions  
  - 9 key location types  
  - Monthly variations  

**Output:**  
- Excel summary tables saved in `/tables/`.  

---

### 6. `EDA2.ipynb` (Exploratory Data Analysis Phase 2)
**Purpose:**  
- Conduct a second, more focused EDA based on Excel insights.

**Key actions:**  
- Introduced **crime groups** (e.g., Violent/Sexual, Theft/Burglary/Robbery) and **outcome groups** (Positive, Neutral, Negative).  
- Filtered data to focus on 5 key regions and 9 key locations.  
- Plotted:  
  - Crime group vs outcome group (pie charts and stacked bars)  
  - Positive outcome % by region  
  - % of Violent/Sexual and Theft/Burglary/Robbery crimes by region (highlighting Liverpool vs others)  
  - Grouped bar charts showing crime group distribution by location  
  - Horizontal bar charts ranking locations by positive outcome %  
  - Total monthly crimes with Anti-Social Behaviour % overlay  

**Output:**  
- Visualisations saved in `/visualisations/`.  

---

### 7. `dashboard.ipynb`
**Purpose:**  
- Build individual interactive visualisations using **Plotly** and **ipywidgets**.

**Key actions:**  
- Created filterable charts for:  
  - Monthly crime trends (bar + line overlay)  
  - Positive outcome rates by region (horizontal bar)  
  - Crime group by location (grouped bar)  
  - Crime density (hexbin maps using GeoPandas & Matplotlib)  
- Applied consistent pastel colour schemes across all plots.  
- Added dropdown menus and interactive widgets.  

---

### 8. `final-dashboard.ipynb`
**Purpose:**  
- Combine all interactive visualisations into a single cohesive dashboard.

**Key actions:**  
- Integrated all filters (crime group, location, outcome group, month) into one control panel.  
- Ensured charts dynamically updated together.  
- Streamlined layout and styling for readability.  

**Output:**  
- Final interactive dashboard (Jupyter-based).  

---

## Notes
- Run notebooks in the order above.  
- Outputs (cleaned datasets, plots, Excel tables) are automatically saved to the appropriate folders: `/data/`, `/visualisations/`, `/tables/`.  
- All notebooks pull data directly from the GitHub-hosted ZIP files—**no manual downloads required**.

---
