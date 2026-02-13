import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
months = ['Jan', 'Feb', 'Mar', 'Apr']
monthly_sales = [200, 350, 400, 500]
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category-wise Sales")
plt.xlabel("Product Category")
plt.ylabel("Sales")
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()