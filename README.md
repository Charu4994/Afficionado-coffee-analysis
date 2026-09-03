 ☕ Product Optimization & Revenue Contribution Analysis
### Afficionado Coffee Roasters

A data analysis project exploring product popularity, revenue contribution, and menu concentration risk using transaction-level sales data — built with Python, pandas, and Streamlit.

## 📌 Project Overview

Retail success depends on understanding which products customers prefer, which generate the most revenue, and how revenue is distributed across the menu. This project analyzes 149,000+ transactions to answer exactly that for Afficionado Coffee Roasters.

## 🎯 Objectives

- Identify top-selling and least-selling products
- Quantify revenue contribution by product and category
- Measure revenue concentration across the menu (Pareto / 80-20 analysis)
- Support menu simplification and identify high-impact "hero" products

## 📊 Key Findings

- **Total Revenue:** ₹698,812.33 across 149,116 transactions
- **Revenue Concentration:** Just 10 of 29 product types generate ~79% of total revenue
- **Top Category:** Coffee (38.6%) and Tea (28.1%) together account for ~67% of revenue
- **Top Product:** Barista Espresso — highest revenue contributor (13.08%)

## 🗂️ Dataset

Transaction-level sales data with 11 fields: `transaction_id`, `year`, `transaction_time`, `transaction_qty`, `unit_price`, `store_id`, `store_location`, `product_id`, `product_category`, `product_type`, `product_detail`.

## 🛠️ Tech Stack

- **Python** (pandas, matplotlib, seaborn) — data cleaning & EDA
- **Plotly** — interactive visualizations
- **Streamlit** — web dashboard

## 📁 Repository Structure
