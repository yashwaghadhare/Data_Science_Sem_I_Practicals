import pandas as pd

df = pd.DataFrame({
    'Name': ['Aanya', 'Diya', 'Aanya', 'Isha', 'Diya'],
    'Score': [88, 92, 95, 80, 85]
})

print(df.groupby('Name')['Score'].mean())

print(df.groupby('Name')['Score'].max())

print(df.groupby('Name')['Score'].min())

print(df.sort_values(by='Score', ascending=False))

print(df)
