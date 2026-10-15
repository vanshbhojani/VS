import pandas as pd
import numpy as np

df = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'name' : ["ram","sira","mira","vansh","meet"],
    'salary' : [10000,20000,30000,np.nan,np.nan ]
})

print(df)

lol = df[df.columns].count()
print(lol)

df['salary'] = df['salary'].fillna(df['salary'].mean())
print(df)

lol = df.query('salary >20000')
print(lol)

faa = df.loc[df['id'].isin([2,3,4])]
print(faa)

df.rename(columns = {'name' : 'first_name'},inplace=True)
print(df)




