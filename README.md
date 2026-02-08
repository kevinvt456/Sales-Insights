# 📊 Sales Insights Dashboard using Python

This project performs exploratory data analysis (EDA) on a sales dataset to generate meaningful business insights. It analyzes revenue, profit, product performance, regional distribution, and sales trends using Python data visualization libraries.

---

## 🚀 Project Overview

The Sales Insights Dashboard helps stakeholders understand:
- Overall business performance
- Monthly sales trends
- Top-selling products
- Region-wise sales contribution
- Relationships between key numerical variables

The project cleans raw data, processes dates, computes key metrics, and visualizes insights in an easy-to-understand manner.

---

## 🗂️ Dataset

- **File Name:** `sales.csv`
- **Key Columns Used:**
  - Order Date
  - Product
  - Sales
  - Profit
  - Units Sold
  - Region
  - Unit Price
  - Unit Cost
  - Sales Channel
  - Order Priority

---

## 🧹 Data Preprocessing Steps

- Cleaned column names (lowercase, removed spaces and underscores)
- Renamed columns for better readability
- Converted order date to datetime format
- Extracted month for trend analysis
- Removed missing values

---

## 📌 Key Business Metrics

- **Total Revenue**
- **Total Profit**

These metrics provide a quick snapshot of overall business performance.

---

## 📈 Visualizations & Insights

### 1. Monthly Sales Trend
- Line chart showing sales growth and seasonality over time

### 2. Top 10 Selling Products
- Bar chart highlighting products with the highest sales contribution

### 3. Region-wise Sales Distribution
- Pie chart showing percentage contribution of each region

### 4. Correlation Heatmap
- Visualizes relationships between:
  - Units Sold
  - Unit Price
  - Unit Cost
  - Sales
  - Profit

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Matplotlib
- Seaborn

---

## ▶️ How to Run the Project

1. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
