import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
df = pd.read_csv("Data/Iris.csv")

# Compute correlation matrix for numeric columns
corr = df.corr(numeric_only=True)

# Display correlation matrix
print("Correlation Matrix:")
print(corr)

# Plot heatmap
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap - Iris Dataset")
plt.show()