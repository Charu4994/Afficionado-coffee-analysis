import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())

print(df.shape)

print(df.dtypes)

print(df.isnull().sum())

print("Duplicate rows:", df.duplicated(subset="transaction_id").sum())

bad_rows = df[(df["transaction_qty"] <= 0) | (df["unit_price"] <= 0)]
print("Bad rows count:", bad_rows.shape[0])
print(bad_rows.head())

print("Unique products:", df["product_id"].nunique())
print("Categories:", df["product_category"].unique())
print("Store locations:", df["store_location"].unique())
