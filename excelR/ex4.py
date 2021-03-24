import pandas as pd

df = pd.read_csv('c:/development/excelr/datasets/salaries.csv')
print(df.describe())
print(df.phd.describe())
print(df.phd.count())
print(df.phd.mean())

