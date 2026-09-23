import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("sales_data.csv")


data["Total_Sales"] = data["Quantity"] * data["Price"]


print("===== SALES DATA =====")
print(data)


total_sales = data["Total_Sales"].sum()

print("\nTotal Sales: ₹", total_sales)


average_sales = data["Total_Sales"].mean()

print("Average Sale: ₹", round(average_sales, 2))


product_sales = data.groupby("Product")["Total_Sales"].sum()

print("\n===== SALES BY PRODUCT =====")
print(product_sales)


region_sales = data.groupby("Region")["Total_Sales"].sum()

print("\n===== SALES BY REGION =====")
print(region_sales)


highest_product = product_sales.idxmax()
highest_amount = product_sales.max()

print("\nHighest Selling Product:", highest_product)
print("Sales Amount: ₹", highest_amount)


plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")

plt.tight_layout()
plt.show()
