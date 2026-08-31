import pandas as pd

# apni CSV file ka naam yahan daalo
df = pd.read_csv("dataset.csv")

# pehle 5 rows dekho
print(df.head())

# total kitni rows/columns hain
print(df.shape)

# har column ka naam aur type
print(df.dtypes)

# 1. Missing values check karo
print(df.isnull().sum())

# 2. Duplicate transactions check karo
print("Duplicate rows:", df.duplicated(subset="transaction_id").sum())

# 3. Negative ya zero quantity/price check karo (galat data)
bad_rows = df[(df["transaction_qty"] <= 0) | (df["unit_price"] <= 0)]
print("Bad rows count:", bad_rows.shape[0])
print(bad_rows.head())

# 4. Unique products, categories check karo
print("Unique products:", df["product_id"].nunique())
print("Categories:", df["product_category"].unique())
print("Store locations:", df["store_location"].unique())