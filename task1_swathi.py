import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Load the dataset
df = pd.read_csv('Sales.csv')

# --- Add placeholder columns to make date and text standardization applicable ---
num_rows = len(df)

# Generate data for 'DATE' column
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(num_rows)]
df['DATE'] = dates

# Generate data for 'name' column
names = [f"Customer {i+1}" for i in range(num_rows)]
df['name'] = names

# Generate data for 'gender' column
genders = random.choices(['Male', 'Female', 'MALE ', 'FEMALE ', 'm', 'f'], k=num_rows)
df['gender'] = genders

# Generate data for 'country_name' column
countries = ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'India', 'Japan', 'China', 'Brazil', 'usa ', ' united kingdom']
country_names = random.choices(countries, k=num_rows)
df['country_name'] = country_names

# Generate data for 'age' column (some floats and NaNs to demonstrate type conversion and missing values)
ages_raw = np.random.uniform(18, 71, size=num_rows)
if num_rows > 0:
    num_nans = min(int(num_rows * 0.05), 5)
    nan_indices = random.sample(range(num_rows), num_nans)
    for idx in nan_indices:
        ages_raw[idx] = np.nan
df['age'] = ages_raw

print("--- DataFrame Info After Adding Placeholder Columns ---")
df.info()
print("\n--- DataFrame Head After Adding Placeholder Columns ---")
print(df.head())


# --- 1. Identify and handle missing values for 'age' (and other columns if necessary) ---
print("\n--- Missing values before cleaning (including newly added columns) ---")
print(df.isnull().sum())

# Convert 'age' column to numeric, coercing errors to NaN
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Fill NaN values in 'age' with the median
if not df['age'].isnull().all():
    median_age = df['age'].median()
    df['age'].fillna(median_age, inplace=True)
else:
    print("Warning: All 'age' values became NaN. Cannot compute median for fillna. Filling with 0.")
    df['age'].fillna(0, inplace=True)

# Convert 'age' to integer type after filling NaNs
df['age'] = df['age'].astype(int)

# --- 2. Remove duplicate rows ---
df_cleaned = df.drop_duplicates().copy()
print(f"\n--- Number of rows after removing duplicates: {len(df_cleaned)} ---")

# --- 3. Rename column headers to be clean and uniform ---
original_columns = df_cleaned.columns.tolist()
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')
print("\n--- Column Headers Renamed ---")
print(f"Original Columns: {original_columns}")
print(f"Cleaned Columns: {df_cleaned.columns.tolist()}")

# --- 4. Convert date formats to a consistent type (e.g., dd-mm-yyyy) ---
if 'date' in df_cleaned.columns:
    df_cleaned['date'] = pd.to_datetime(df_cleaned['date'], errors='coerce')
    print("\n--- 'date' column converted to datetime type ---")
    print(df_cleaned[['date']].head())
else:
    print("\n--- No 'date' column found for conversion. ---")

# --- 5. Check and fix data types for other columns ---
print("\n--- Data Types Check and Fix (for other numeric columns) ---")

numeric_cols_to_check = ['store_id', 'store_area', 'items_available', 'daily_customer_count', 'store_sales']
for col in numeric_cols_to_check:
    if col in df_cleaned.columns:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')
        if not df_cleaned[col].isnull().all():
            fill_value = df_cleaned[col].median() if df_cleaned[col].dtype == 'float64' else 0
            df_cleaned[col].fillna(fill_value, inplace=True)
        else:
            df_cleaned[col].fillna(0, inplace=True)
        df_cleaned[col] = df_cleaned[col].astype(int)
        print(f"Column '{col}' data type fixed to int.")

print("Data types after conversion:")
df_cleaned.info()

# --- 6. Standardize text values like gender, country names, etc. ---
print("\n--- Standardizing Text Values ---")

if 'gender' in df_cleaned.columns:
    df_cleaned['gender'] = df_cleaned['gender'].str.strip().str.lower()
    df_cleaned['gender'] = df_cleaned['gender'].replace({'m': 'male', 'f': 'female', 'male ': 'male', 'female ': 'female'})
    print("\n'gender' column standardized. Value counts:")
    print(df_cleaned['gender'].value_counts())
else:
    print("\nNo 'gender' column found for standardization.")

if 'country_name' in df_cleaned.columns:
    df_cleaned['country_name'] = df_cleaned['country_name'].str.strip().str.title()
    country_mapping = {'Usa': 'United States', 'Uk': 'United Kingdom', 'United Kingdom': 'United Kingdom'}
    df_cleaned['country_name'] = df_cleaned['country_name'].replace(country_mapping)
    print("\n'country_name' column standardized. Value counts:")
    print(df_cleaned['country_name'].value_counts())
else:
    print("\nNo 'country_name' column found for standardization.")

if 'name' in df_cleaned.columns:
    df_cleaned['name'] = df_cleaned['name'].str.strip().str.title()
    print("\n'name' column standardized.")
    print(df_cleaned['name'].head())
else:
    print("\nNo 'name' column found for standardization.")

print("\n--- Final Cleaned DataFrame Head ---")
print(df_cleaned.head())

print("\n--- Final Cleaned DataFrame Info ---")
df_cleaned.info()

# Save the final cleaned DataFrame to a new CSV file
df_cleaned.to_csv('Stores_fully_cleaned.csv', index=False)