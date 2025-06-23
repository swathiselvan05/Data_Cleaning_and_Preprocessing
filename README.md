# Data_Cleaning_and_Preprocessing
Cleaning and preprocessing Sales data

# 🎯 Objective
The objective of this project is to clean, standardize, and preprocess a raw retail sales dataset (Sales.csv) to prepare it for reliable data analysis and visualization. This includes:

- Generating synthetic fields to simulate real-world inconsistencies.
- Identifying and handling missing or inconsistent data.
- Standardizing textual entries (e.g., gender, country names).
- Ensuring data types are accurate and consistent across numeric and date fields.
- Removing duplicates and renaming columns for uniformity.
- Saving the fully cleaned dataset `Stores_fully_cleaned.csv` in a structured format for downstream tasks such as reporting, machine learning, or dashboarding.

# 🧹 Sales Data Cleaning Script

This project is a Python-based data preprocessing script to clean and standardize a retail sales dataset (`Sales.csv`) and output a clean version as `Stores_fully_cleaned.csv`.

## 📁 Files

- `task1_swathi.py`: Main Python script for data cleaning.
- `Sales.csv`: Raw input dataset (not included here, expected to be in the same directory).
- `Stores_fully_cleaned.csv`: Output file containing cleaned and standardized data.

## 🧪 Features and Operations Performed

### 1. 📥 Data Loading
- Loads the `Sales.csv` file using `pandas`.

### 2. 🏷️ Placeholder Column Generation
Adds synthetic columns to simulate realistic data cleaning scenarios:
- `DATE`: Sequential daily dates starting from Jan 1, 2023.
- `name`: Randomly generated customer names.
- `gender`: Random values with mixed formatting (e.g., `'Male'`, `'FEMALE '`, `'m'`, `'f'`).
- `country_name`: Mixed-format and non-standard country names.
- `age`: Floating-point numbers with some `NaN` values.

### 3. 🧼 Data Cleaning Steps

- **Missing Values Handling:**
  - Detects and fills missing `age` values using the median.
  - Ensures `age` is cast to integer type.
  
- **Duplicate Removal:**
  - Drops duplicate rows from the dataset.

- **Column Renaming:**
  - Standardizes column headers by removing whitespace and converting to lowercase with underscores.

- **Date Formatting:**
  - Converts the `DATE` column to `datetime` type.

- **Data Type Fixing:**
  - Ensures numerical columns are properly cast as integers, filling missing values with medians.

- **Text Standardization:**
  - Cleans and standardizes text in:
    - `gender` (e.g., `'m'`, `'MALE '` → `'male'`)
    - `country_name` (e.g., `'usa '`, `'Uk'` → `'United States'`, `'United Kingdom'`)
    - `name` (title-cased)

### 4. 💾 Output
- The cleaned dataset is saved as `Stores_fully_cleaned.csv`.

## 🛠️ Requirements

- Python 3.x
- pandas
- numpy

# Install dependencies:
```bash
pip install pandas numpy
```
# 🚀 Run the Script
  Place `Sales.csv` in the same directory and run:

```bash
python task1_swathi.py
```
# 📤 Output
The script prints:

- DataFrame info before and after cleaning
- Head of the dataset at each step
- Summary statistics like value counts for cleaned columns

# 🧑‍💻 Author
   #### Swathi Selvan
   #### First Year M.Sc Data Science
   #### Bishop Heber College, Trichy

# 🔍 Summary
The script `task1_swathi.py` is a comprehensive data cleaning and preprocessing pipeline written in Python using pandas and numpy. It loads a dataset `Sales.csv`, adds synthetic placeholder columns for testing, performs missing value treatment, duplicate removal, column renaming, datatype conversions, and standardizes textual entries such as gender and country names.

This is likely a data-cleaning automation task prepared for either academic or organizational use, transforming raw retail data into a clean, analysis-ready format saved as `Stores_fully_cleaned.csv`.
      
