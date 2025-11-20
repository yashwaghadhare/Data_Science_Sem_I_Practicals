import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("Titanic-Dataset.csv")

print(df.isnull().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True) 
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True) 

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['Age'] < Q1 - 1.5*IQR) | (df['Age'] > Q3 + 1.5*IQR)]
print(outliers[['Name', 'Age']])

df['Age'] = np.where(df['Age'] > Q3 + 1.5*IQR, Q3 + 1.5*IQR, df['Age'])
df['Age'] = np.where(df['Age'] < Q1 - 1.5*IQR, Q1 - 1.5*IQR, df['Age'])

print(df.head())
