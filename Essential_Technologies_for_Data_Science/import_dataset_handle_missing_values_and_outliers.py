import pandas as pd
import numpy as np
from scipy import stats

# Load the Titanic dataset
df = pd.read_csv("Data/Titanic-Dataset.csv")

# 1. Identify missing values
print("Missing values in each column:\n", df.isnull().sum())

# 2. Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)      # Fill missing Age with mean
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill missing Embarked with mode

# 3. Detect outliers using IQR
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Age'] < Q1 - 1.5*IQR) | (df['Age'] > Q3 + 1.5*IQR)]
print("\nOutliers in Age:\n", outliers[['Name', 'Age']])

# 4. Handle outliers by capping
df['Age'] = np.where(df['Age'] > Q3 + 1.5*IQR, Q3 + 1.5*IQR, df['Age'])
df['Age'] = np.where(df['Age'] < Q1 - 1.5*IQR, Q1 - 1.5*IQR, df['Age'])

print("\nDataset after handling missing values and outliers:\n", df.head())
