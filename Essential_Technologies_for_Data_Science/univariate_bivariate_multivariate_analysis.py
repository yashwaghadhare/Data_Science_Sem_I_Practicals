# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Data/Iris.csv")

# -----------------------------------------
# 1. UNIVARIATE ANALYSIS
# -----------------------------------------
print("Summary Statistics:\n", df.describe())

# Example: Histogram for one variable
plt.hist(df['SepalWidthCm'], edgecolor='black')
plt.title("Univariate Analysis - Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------------
# 2. BIVARIATE ANALYSIS
# -----------------------------------------
# Relationship between SepalLength and PetalLength
sns.scatterplot(x='SepalLengthCm', y='PetalLengthCm', data=df, hue='Species')
plt.title("Bivariate Analysis - Sepal Length vs Petal Length")
plt.show()

# -----------------------------------------
# 3. MULTIVARIATE ANALYSIS
# -----------------------------------------
# Pairplot - relationships among all numeric features
sns.pairplot(df, hue='Species')
plt.suptitle("Multivariate Analysis - Pairwise Relationships", y=1.02)
plt.show()

