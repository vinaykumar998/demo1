import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample Retail Dataset
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet"],
    "Quantity": [5, 10, 7, 3, 8, 4],
    "Price": [50000, 20000, 15000, 50000, 20000, 15000],
    "Payment_Method": ["Card", "UPI", "Cash", "Card", "UPI", "Cash"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Sales
df["Sales"] = df["Quantity"] * df["Price"]

print("\nRetail Sales Data")
print(df)

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales =", total_sales)

# Sales by Product
sales_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product")
print(sales_product)

# Most Profitable Product
best_product = sales_product.idxmax()
print("\nMost Profitable Product:", best_product)

# Average Sales using NumPy
avg_sales = np.mean(df["Sales"])
print("Average Sales:", avg_sales)

# Visualization 1 - Bar Chart
plt.figure(figsize=(6,4))
sales_product.plot(kind="bar", color="skyblue")
plt.title("Sales by Product")
plt.ylabel("Sales")
plt.xlabel("Product")
plt.show()

# Visualization 2 - Pie Chart
plt.figure(figsize=(5,5))
df["Payment_Method"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Payment Method Usage")
plt.ylabel("")
plt.show()

# Recommendation
print("\nRecommendation:")
print(f"Increase stock and marketing for {best_product} as it generates the highest revenue.")