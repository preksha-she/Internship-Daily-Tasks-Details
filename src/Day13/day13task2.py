
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Price": [120000, 150000, 180000, 220000, 260000, 300000, 330000, 380000],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", "Delhi", "Chennai", "Mumbai"]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)



plt.figure(figsize=(8,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="City", y="Price", data=df)
plt.title("City vs Price")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()
