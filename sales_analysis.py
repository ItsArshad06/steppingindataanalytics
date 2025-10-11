
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create dataset
data = {
    "Product": ["Shoes", "Shirt", "Jacket", "Shoes", "Shirt"],
    "Region": ["East", "West", "North", "South", "East"],
    "Sales": [200, 150, 400, 300, 250]
}

df = pd.DataFrame(data)

# Step 2: Total Sales per Product
product_sales = df.groupby("Product")["Sales"].sum().reset_index()

# Step 3: Total Sales per Region
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

# Step 4: Bar chart for Product Sales
plt.figure(figsize=(6, 4))
plt.bar(product_sales["Product"], product_sales["Sales"], color="black")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Step 5: Pie chart for Region Sales
plt.figure(figsize=(5, 5))
plt.pie(region_sales["Sales"], labels=region_sales["Region"], autopct='%1.1f%%')
plt.title("Sales by Region")
plt.show()
