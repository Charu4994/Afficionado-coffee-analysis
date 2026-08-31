import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Afficionado Coffee Roasters — Product Analytics", layout="wide")

# Data load karo
df = pd.read_csv("Afficionado Coffee Roasters.xlsx - Transactions.csv")
df["revenue"] = df["transaction_qty"] * df["unit_price"]

st.title("☕ Product Optimization & Revenue Contribution Dashboard")

# --- Sidebar filters ---
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect(
    "Product Category",
    df["product_category"].unique(),
    default=df["product_category"].unique()
)
location_filter = st.sidebar.multiselect(
    "Store Location",
    df["store_location"].unique(),
    default=df["store_location"].unique()
)
top_n = st.sidebar.slider("Top N Products", 5, 30, 10)

# Filter apply karo
filtered = df[
    df["product_category"].isin(category_filter) &
    df["store_location"].isin(location_filter)
]

# --- KPI cards (upar top pe numbers) ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{filtered['revenue'].sum():,.2f}")
col2.metric("Total Transactions", f"{filtered.shape[0]:,}")
col3.metric("Unique Products", filtered["product_type"].nunique())

# --- Module 1: Product ranking ---
st.subheader("Top Products by Revenue & Volume")
ranking = filtered.groupby("product_type").agg(
    total_revenue=("revenue", "sum"),
    total_units=("transaction_qty", "sum")
).reset_index().sort_values("total_revenue", ascending=False).head(top_n)
st.dataframe(ranking, use_container_width=True)

# --- Module 2: Category revenue distribution ---
st.subheader("Category Revenue Distribution")
cat_rev = filtered.groupby("product_category")["revenue"].sum().reset_index()
fig1 = px.pie(cat_rev, names="product_category", values="revenue")
st.plotly_chart(fig1, use_container_width=True)

# --- Module 3: Popularity vs Revenue scatter ---
st.subheader("Popularity vs Revenue")
scatter_data = filtered.groupby("product_type").agg(
    units=("transaction_qty", "sum"),
    revenue=("revenue", "sum")
).reset_index()
fig2 = px.scatter(scatter_data, x="units", y="revenue", text="product_type", size="revenue")
st.plotly_chart(fig2, use_container_width=True)

# --- Module 4: Product drill-down table ---
st.subheader("Product Drill-Down")
drilldown = filtered.groupby(["product_category", "product_type", "product_detail"]).agg(
    total_revenue=("revenue", "sum"),
    total_units=("transaction_qty", "sum")
).reset_index().sort_values("total_revenue", ascending=False)
st.dataframe(drilldown, use_container_width=True)