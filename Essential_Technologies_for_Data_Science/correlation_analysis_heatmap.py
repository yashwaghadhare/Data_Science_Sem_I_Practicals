import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Iris.csv")
corr = df.corr(numeric_only=True)
print(corr)

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap - Iris Dataset")
plt.show()
