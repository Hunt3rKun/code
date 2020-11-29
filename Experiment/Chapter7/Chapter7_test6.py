import pandas as pd
data = [['Tom',3],['Jerry',6]]
df = pd.DataFrame(data,columns= ['name','age'])
print(df)
print(df[1:2])
print(df[['name']])
print(df.loc[0,'name'])