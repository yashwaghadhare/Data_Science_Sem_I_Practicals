import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

print(df.describe())

plt.hist(df['SepalWidthCm'])
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
