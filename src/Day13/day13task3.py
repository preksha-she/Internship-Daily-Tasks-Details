
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 5, 5],
    "Bathrooms": [1, 2, 2, 2, 3, 3, 3, 4],
    "Price": [120000, 150000, 180000, 220000, 260000, 300000, 330000, 500000]  # 500000 may act as outlier
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)


correlation_matrix = df.corr()

print("\nCorrelation Matrix:\n")
print(correlation_matrix)


plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


print("\nHighly Correlated Pairs (Correlation > 0.8):\n")

for i in correlation_matrix.columns:
    for j in correlation_matrix.columns:
        if i != j and abs(correlation_matrix.loc[i, j]) > 0.8:
            print(f"{i} and {j} -> {correlation_matrix.loc[i, j]}")


plt.figure(figsize=(6,4))
sns.boxplot(y="Price", data=df)
plt.title("Boxplot of Price")
plt.show()
