import pandas as pd

df = pd.read_csv('c:/development/excelr/datasets/salaries.csv')
print(df.columns)
print(df.groupby(['rank'], sort=False)['salary'].mean())
print(df.salary > 25000)
print(df.iloc[3])
