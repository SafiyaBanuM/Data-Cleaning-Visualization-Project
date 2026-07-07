#======================================
#Data Cleaning & Visualization Project
# Thiranex Data Science Internship
# Dataset: Maven Fuzzy Factory - Orders
# Author: Safiya Banu M
#======================================
#1.Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
#2.Load Dataset
df=pd.read_csv(r"C:\Users\SAFIYA BANU\Downloads\Maven+Fuzzy+Factory\orders.csv")
print("Dataset Shape:",df.shape)
#3.Data Exploration
print("\nColumns:")
print(df.columns)
print(df.head())
print(df.info())
print(df.describe())
#4.Data Cleaning
print("\nMissing Values")
print(df.isnull().sum())
print("\nDuplicate Rows")
print(df.duplicated().sum())
df["created_at"]=pd.to_datetime(df["created_at"])
df.info()
#5.Data Visualization
#using Box Plot
plt.figure(figsize=(8,5))
plt.boxplot(df["price_usd"])
plt.title("Box Plot of product Prices")
plt.ylabel("price(USD)")
plt.savefig("boxplot_price.png")
plt.show()
#Insight:
#The box plot identified a few outliers in the price_usd column. These represent valid product prices rather than data errors, so no outliers were removed.
#using histograms
plt.figure(figsize=(8,5))
plt.hist(df["price_usd"],bins=10)
plt.title("Distribution of Product Prices")
plt.xlabel("Price(USD)")
plt.ylabel("Number of Orders")
plt.grid(True)
plt.savefig("histogram_price.png")
plt.show()
#insights
#Most customer orders are concentrated around the $49.99 price point, indicating that this is one of the most popular product prices.
#using Bar Chart
product_orders = df["primary_product_id"].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(product_orders.index, product_orders.values)
plt.title("Number of Orders by Product")
plt.xlabel("Product ID")
plt.ylabel("Number of Orders")
plt.grid(True)
plt.savefig("Bar_Chart_price.png")
plt.show()
#Insight:
#Product ID 1 received the highest number of orders, making it the best-selling product in the dataset.
#using Pie Chart
product_orders = df["primary_product_id"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    product_orders.values,
    labels=product_orders.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Product Order Distribution")
plt.savefig("pieChart_orders.png")
plt.show()
#Using Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["price_usd"], df["cogs_usd"],alpha=0.6)
plt.title("Price vs Cost of Goods Sold")
plt.xlabel("Price (USD)")
plt.ylabel("COGS (USD)")
ply.grid(True)
plt.savefig("scatterplots_price.png")
plt.show()
#Insight:
#The scatter plot shows a positive relationship between price_usd and cogs_usd. As the selling price increases, the cost of goods sold also tends to increase.
items = df["items_purchased"].value_counts().sort_index()
plt.figure(figsize=(6,4))
plt.bar(items.index.astype(str), items.values)
plt.title("Items Purchased Per Order")
plt.xlabel("Items Purchased")
plt.ylabel("Number of Orders")
plt.savefig("purchased.png")
plt.show()
#Insights
# Most customers purchased only one item per order,
# while orders containing multiple items were less common.
#Conclusion
print("\n========== CONCLUSION ==========")
print("1. The dataset contained no missing values.")
print("2. No duplicate records were found.")
print("3. The created_at column was converted to datetime format.")
print("4. Product ID 1 had the highest number of orders.")
print("5. Most orders were concentrated around the $49.99 price point.")
print("6. Price and COGS showed a positive relationship.")


