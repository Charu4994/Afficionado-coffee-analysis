import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Afficionado Coffee Roasters — Product Analytics", layout="wide")

df = pd.read_csv("Afficionado Coffee Roasters.xlsx - Transactions.csv")
df["revenue"] = df["transaction_qty"] * df["unit_price"]

st.title("☕ Product Optimization & Revenue Contribution Dashboard")
st.caption("Afficionado Coffee Roasters — Product & Revenue Analytics")


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


filtered = df[
    df["product_category"].isin(category_filter) &
    df["store_location"].isin(location_filter)
]


col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{filtered['revenue'].sum():,.2f}")
col2.metric("Total Transactions", f"{filtered.shape[0]:,}")
col3.metric("Unique Products", filtered["product_type"].nunique())


st.subheader("Top Products by Revenue & Volume")
ranking = filtered.groupby("product_type").agg(
    total_revenue=("revenue", "sum"),
    total_units=("transaction_qty", "sum")
).reset_index().sort_values("total_revenue", ascending=False).head(top_n)
st.dataframe(ranking, use_container_width=True)

st.subheader(f"Top {top_n} Products by Revenue (Bar Chart)")
fig_bar = px.bar(
    ranking.sort_values("total_revenue", ascending=True),
    x="total_revenue",
    y="product_type",
    orientation="h",
    text="total_revenue",
    labels={"total_revenue": "Revenue", "product_type": "Product Type"}
)
fig_bar.update_traces(texttemplate="₹%{text:,.0f}", textposition="outside")
fig_bar.update_layout(height=500, template="plotly_white")
st.plotly_chart(fig_bar, use_container_width=True)


st.subheader("Category Revenue Distribution")
cat_rev = filtered.groupby("product_category")["revenue"].sum().reset_index()
fig1 = px.pie(cat_rev, names="product_category", values="revenue")
st.plotly_chart(fig1, use_container_width=True)


st.subheader("Popularity vs Revenue")
scatter_data = filtered.groupby("product_type").agg(
    units=("transaction_qty", "sum"),
    revenue=("revenue", "sum")
).reset_index().sort_values("revenue", ascending=False).reset_index(drop=True)


scatter_data["label"] = scatter_data["product_type"]
scatter_data.loc[scatter_data.index >= 15, "label"] = ""

fig2 = px.scatter(
    scatter_data, x="units", y="revenue", size="revenue",
    color="product_type", hover_name="product_type", text="label"
)
fig2.update_traces(textposition="top center", textfont=dict(size=9))
fig2.update_layout(height=600, template="plotly_white", showlegend=False)
st.plotly_chart(fig2, use_container_width=True)


st.subheader("Pareto Analysis — Revenue Concentration")
pareto_data = filtered.groupby("product_type")["revenue"].sum().reset_index()
pareto_data = pareto_data.sort_values("revenue", ascending=False).reset_index(drop=True)
pareto_data["cumulative_pct"] = (pareto_data["revenue"].cumsum() / pareto_data["revenue"].sum() * 100).round(2)

fig_pareto = go.Figure()
fig_pareto.add_trace(go.Bar(x=pareto_data["product_type"], y=pareto_data["revenue"], name="Revenue"))
fig_pareto.add_trace(go.Scatter(
    x=pareto_data["product_type"], y=pareto_data["cumulative_pct"],
    name="Cumulative %", yaxis="y2", mode="lines+markers", line=dict(color="red")
))
fig_pareto.add_hline(y=80, line_dash="dash", line_color="green", yref="y2")
fig_pareto.update_layout(
    yaxis=dict(title="Revenue"),
    yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0, 100]),
    height=550, template="plotly_white", xaxis_tickangle=-90
)
st.plotly_chart(fig_pareto, use_container_width=True)

st.subheader("Product Drill-Down")
drilldown = filtered.groupby(["product_category", "product_type", "product_detail"]).agg(
    total_revenue=("revenue", "sum"),
    total_units=("transaction_qty", "sum")
).reset_index().sort_values("total_revenue", ascending=False)
st.dataframe(drilldown, use_container_width=True)
