# read_csv_test.py

import pandas as pd

# Working URL: Sample Sales Transactions dataset
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

# Load CSV into DataFrame
df = pd.read_csv(url)

# Print first 5 rows
print(df.head())