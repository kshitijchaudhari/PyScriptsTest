import pandas as pd

df = pd.read_csv('c:/development/excelr/datasets/mtcars.csv')
filter1 = df['cyl']>4
filter2 = df['hp']>100
df.where(filter1 & filter2, inplace=True)
print(df)

