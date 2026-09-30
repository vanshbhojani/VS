import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name' : ['Alice', 'Bob',np.nan , 'David', 'Eve'],
    'age' : [21,np.nan , 45, 34, 56],
    'salary' : [5000, 4000, 6000, 3000, np.nan]
})

# print(df)

# miss = df.isna().sum()
# print(miss)

# sal_fil = df['salary'].fillna(df['salary'].mean())
# print(sal_fil)

# dr_data = df.dropna()
# print(dr_data)

sal_mor = df.query('salary>3000')[['name','salary']]
print(sal_mor)









