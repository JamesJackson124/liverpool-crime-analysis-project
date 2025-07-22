UK Crime Data Analysis — Notebooks
This folder contains Jupyter notebooks that implement the core data processing and analysis pipeline for the UK crime dataset, focusing on a 12-month period for Liverpool. Each notebook corresponds to a key stage in the workflow: data concatenation, cleaning, and exploratory data analysis (EDA).

Notebooks Overview
1. Data Concatenation (data-concatenation.ipynb)
This notebook loads monthly raw crime CSV files and concatenates them into a single unified dataset.
Key steps:

Reading multiple monthly CSV files into DataFrames

Merging all months into one comprehensive dataset

Basic validation to ensure consistency and completeness

Exporting the combined raw dataset for subsequent processing

2. Data Cleaning (sql-data-cleansing.ipynb)
This notebook performs rigorous data cleaning using SQL to prepare the dataset for analysis.
Key steps:

Handling missing or invalid entries, including missing Crime IDs

Dropping or correcting rows missing critical data like longitude/latitude

Normalizing column names to snake_case

Removing duplicate Crime IDs and unused columns

Ensuring correct data types and trimming whitespace

Fixing inconsistencies in categorical values (crime types, outcome categories)

Validating dates to exclude future or nonsensical entries

Outputting a cleaned, normalized dataset stored in a SQL database

3. Exploratory Data Analysis (EDA.ipynb)
This notebook explores the cleaned data through summary statistics and visualizations to uncover crime patterns.
Key steps:

Loading the cleaned dataset and converting date fields appropriately

Checking data integrity (nulls, duplicates) and summary statistics

Univariate analyses of crime types, outcomes, and locations

Time series analysis of monthly crime trends by type, including rolling averages

Analysis of crime outcomes by type and over time via heatmaps and trends

Spatial summaries using scatter plots and top location counts (without maps)

Creating aggregated tables for further reporting and visualization tools

Usage
To run these notebooks, ensure you have the following prerequisites installed:

Python 3.8+

Jupyter Notebook or JupyterLab

SQLite (recommended) or another SQL database

Python packages: pandas, numpy, matplotlib, seaborn, sqlalchemy

Install dependencies with:

pip install pandas numpy matplotlib seaborn sqlalchemy

Summary
These notebooks collectively provide a reproducible workflow to transform raw UK crime data into actionable insights through cleaning and exploratory analysis. They can be adapted for different regions, periods, or further extended for predictive modeling or advanced visualizations.

If you want, I can also help with the READMEs for the other folders — just let me know!
