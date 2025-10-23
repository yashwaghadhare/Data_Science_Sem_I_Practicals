import pandas as pd

# Simple DataFrame with Indian girl names and scores
df = pd.DataFrame({
    'Name': ['Aanya', 'Diya', 'Aanya', 'Isha', 'Diya'],
    'Score': [88, 92, 95, 80, 85]
})

# Group by Name and calculate average Score
print("Average Score by Name:")
print(df.groupby('Name')['Score'].mean())

# Maximum and minimum score per Name
print("\nMaximum Score by Name:")
print(df.groupby('Name')['Score'].max())
print("\nMinimum Score by Name:")
print(df.groupby('Name')['Score'].min())

# Sort the DataFrame by Score descending
print("\nData sorted by Score (highest first):")
print(df.sort_values(by='Score', ascending=False))

# Add a new column: Pass/Fail (Score >= 85)
df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 85 else 'Fail')
print("\nUpdated DataFrame with Result column:")
print(df)
