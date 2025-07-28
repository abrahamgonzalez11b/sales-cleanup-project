# Clean_sales_data.py

import pandas as pd

# Load the raw CSV file
file_path = "addresses.csv"
df = pd.read_csv(file_path)

# Shoe original data
print("Origial data:")
print(df.head())

# --- Step 1: Drop rows with any missiong values ---
df_clean = df.dropna()

# --- Step 2: Rename columns to lowercase and remove spaces ---
df_clean.columns = [col.strip().lower().replace(" ", "_") for col in df_clean.columns]

# --- Step 3: Reset index after cleaning ---
df_clean.reset_index(drop=True, inplace=True)

# --- Step 4: Save the cleaned data to a new CSV file ---
output_path = "cleaned_sales_data.csv"
df_clean.to_csv(output_path, index=False)

print(f"\nCleaned data saved to: {output_path}")
print(df_clean.head())