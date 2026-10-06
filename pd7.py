import pandas as pd
df = pd.read_csv('example.csv', on_bad_lines='skip')

df=pd.read_csv("example.csv")
print(df.info())
print(df.head())