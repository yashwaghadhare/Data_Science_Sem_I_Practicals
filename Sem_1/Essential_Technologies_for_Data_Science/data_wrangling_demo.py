import pandas as pd

df = pd.read_csv("Iris.csv")
print(df.head())
print(df.shape)
print(df.columns.tolist())

print(df.iloc[:, 0])

print(df['SepalLengthCm'] > 5)

df['SepalArea'] = df['SepalLengthCm'] * df['SepalWidthCm']

print(df.head())
