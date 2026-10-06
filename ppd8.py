import pandas as pd
df=pd.read_csv("lab1.csv")
print(df.dropna(inplace=True))
print(df.to_string())