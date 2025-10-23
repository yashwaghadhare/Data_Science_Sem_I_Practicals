import pandas as pd

# Load the Iris dataset
df = pd.read_csv("Data/Iris.csv")

# View first 5 rows, shape, and column names
print("First 5 rows:\n", df.head())
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())

# Select a column by index and by name
print("\nFirst column:\n", df.iloc[:, 0])
print("\nSepalLengthCm column:\n", df['SepalLengthCm'])

# Conditional selection
print("\nRows where SepalLengthCm > 5:\n", df[df['SepalLengthCm'] > 5])
print("\nRows where SepalLengthCm > 5 and Species is 'Iris-setosa':\n",
      df[(df['SepalLengthCm'] > 5) & (df['Species'] == 'Iris-setosa')])

# Add a new column and modify existing data
df['SepalArea'] = df['SepalLengthCm'] * df['SepalWidthCm']
df.loc[df['Species'] == 'Iris-setosa', 'SepalLengthCm'] = 0

# View updated dataset
print("\nUpdated dataset:\n", df.head())