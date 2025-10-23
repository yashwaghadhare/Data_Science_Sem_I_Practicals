import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
df = pd.read_csv("Data/Iris.csv")

# Display basic statistics
print("Summary statistics:")
print(df.describe())

# Univariate analysis - Histogram for SepalWidthCm
plt.hist(df['SepalWidthCm'], edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()
