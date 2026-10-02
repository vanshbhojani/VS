import pandas as pd
import numpy as np

# shot_values , shot_index ,dropna 

df = pd.DataFrame({
    'name': ['Alice', 'Bob', np.nan, 'Charlie', 'Dennis'],
    'age': [20, 21, 18, 19, np.nan],
    'height': [160, 170, 155, 162, 158],
    'weight': [59, np.nan, 58, 55, 56],
    'shoe_size': [10, 11, 12, None, 13],
})
print(df)
"""
lol=df.dropna()
print(lol)

hihi = df.dropna(axis=1)
print(hihi)

hum = df.dropna(subset=['age']) # subset parameter is used to specify the column(s) to consider for dropping rows with NaN values. In this case, it will drop any rows where the 'age' column has NaN values.
print(hum)
""""""
humm = df.sort_values(['age', 'name']) # sort_values() is used to sort the DataFrame by the specified column(s). In this case, it will sort the DataFrame first by the 'age' column in ascending order, and then by the 'name' column in ascending order.
print(humm)"""

lol = df.sort_index(ascending=False) # sort_index() is used to sort the DataFrame by the index. In this case, it will sort the DataFrame in descending order by the index.
print(lol)




