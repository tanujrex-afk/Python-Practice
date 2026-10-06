import pandas as pd
data={
    'calories':[600,500,250],
    'time':[120,60,90]
}
df=pd.DataFrame(data)
print(df.loc[1])
