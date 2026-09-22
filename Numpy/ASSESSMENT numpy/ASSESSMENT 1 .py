import pandas as pd
import numpy as np


# 1) Import pandas and read in the banklist.csv file into a dataframe called banks.

f1 = pd.read_csv("Numpy/ASSESSMENT numpy/banklist.csv")
print(f1)

# 2) Show the head of the dataframe.

print(f1.head())

print(f1.head(5))

# 3) What are the column names?

print(f1.columns)

# 4) How many States (ST) are represented in this data set?

print(len(f1['ST']))

# 5) Get a list or array of all the states in the data set.

print(f1['ST'].unique())

# 6) What are the top 5 states with the most failed banks?

print(f1.groupby('ST').count())

# 7) What are the top 5 acquiring institutions?

print(f1.groupby('Acquiring Institution').count())

# 8) How many banks has the State Bank of Texas acquired? How many of them were actually in Texas?

print(f1.loc[f1['ST'] == 'Texas'])

# 9) What is the most common city in California for a bank to fail in?

print(f1.groupby(['ST', 'City']).count())

