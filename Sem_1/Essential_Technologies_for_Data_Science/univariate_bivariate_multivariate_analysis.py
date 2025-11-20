import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

print(df.describe())

plt.hist(df['SepalWidthCm'])
plt.title("Univariate Analysis - Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")

sns.scatterplot(x='SepalLengthCm', y='PetalLengthCm', data=df)
plt.title("Bivariate Analysis")

sns.pairplot(df)
plt.suptitle("Multivariate Analysis")
plt.show()
