
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


data = {
    "Price": [120000, 150000, 180000, 200000, 220000, 250000, 300000, 500000],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", "Delhi", "Chennai", "Mumbai"]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)
plt.title("Histogram of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()


skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("\nStatistical Measures:")
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
if skewness > 0:
    print("The data is Right Skewed.")
elif skewness < 0:
    print("The data is Left Skewed.")
else:
    print("The data is Normally Distributed.")



plt.figure(figsize=(6,4))
sns.countplot(x="City", data=df)
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

df["Log_Price"] = np.log(df["Price"])

plt.figure(figsize=(8,5))
sns.histplot(df["Log_Price"], kde=True)
plt.title("Log Transformed Price Distribution")
plt.xlabel("Log Price")
plt.ylabel("Frequency")
plt.show()

print("\nLog Transformation Applied Successfully.")
