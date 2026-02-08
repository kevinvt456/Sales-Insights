import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("sales.csv")

# -------------------------------
# 2. Clean Column Names
# -------------------------------
df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(" ", "")
    .str.replace("_", "")
)

# -------------------------------
# 3. Rename Columns
# -------------------------------
df = df.rename(columns={
    "orderdate": "order_date",
    "itemtype": "product",
    "totalrevenue": "sales",
    "totalprofit": "profit",
    "unitsold": "units_sold",
    "saleschannel": "sales_channel",
    "orderpriority": "order_priority"
})

# -------------------------------
# 4. Date Processing
# -------------------------------
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M")

df.dropna(inplace=True)

# -------------------------------
# 5. Key Business Metrics
# -------------------------------
print("Total Revenue:", df["sales"].sum())
print("Total Profit:", df["profit"].sum())

# -------------------------------
# 6. Monthly Sales Trend
# -------------------------------
monthly_sales = df.groupby("month")["sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 7. Top-Selling Products
# -------------------------------
top_products = (
    df.groupby("product")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 8. Region-wise Performance
# -------------------------------
region_sales = df.groupby("region")["sales"].sum()

plt.figure(figsize=(6,6))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region-wise Sales Distribution")
plt.ylabel("")
plt.show()

# -------------------------------
# 9. Correlation Heatmap
# -------------------------------
plt.figure(figsize=(10,6))
sns.heatmap(
    df[["units_sold", "unitprice", "unitcost", "sales", "profit"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

print("\nSales Insights Dashboard executed successfully!")
