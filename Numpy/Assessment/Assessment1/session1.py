import pandas as pd
import numpy as np

# 1) Import pandas and read in the banklist.csv file into a dataframe called banks.

file1 = pd.read_csv("Numpy/Assessment/banklist.csv")
print(file1)


# 2) Show the head of the dataframe

print(file1.head())


# 3) What are the column names?

print(file1.columns) # printing a column name 

# output Index(['Bank Name', 'City', 'ST', 'CERT', 'Acquiring Institution',
#        'Closing Date', 'Updated Date'],
#       dtype='object')


# 4) How many States (ST) are represented in this data set?

print(len(file1['ST']))  # pandas

s =file1['ST'].to_numpy()

us = np.unique(s)
print(us) # numpy


# 5) Get a list or array of all the states in the data set.

print(file1['ST'].unique())  # unique can rerurn unique values in a data set

faa = (len(np.unique(file1['ST'].to_numpy()))) #numpy
print(faa)

# output ['IL' 'WI' 'LA' 'UT' 'NJ' 'AR' 'GA' 'PA' 'TN' 'WA' 'CO' 'PR' 'FL' 'MN'
#  'CA' 'MD' 'OK' 'OH' 'SC' 'VA' 'ID' 'TX' 'CT' 'AZ' 'NV' 'NC' 'KY' 'MO'
#  'KS' 'AL' 'MI' 'IN' 'IA' 'NE' 'MS' 'NM' 'OR' 'NY' 'MA' 'SD' 'WY' 'WV'
#  'NH' 'HI']

# 6) What are the top 5 states with the most failed banks?

print(file1.groupby('ST').value_counts().head(5)) #pandas

faa2 = file1['ST'].dropna().to_numpy()
ufaa = np.unique(faa2,return_counts=True)
ind = np.argsort(ufaa[1])[::-1]
print(ufaa[0][ind])

# 7) What are the top 5 acquiring institutions?

print(file1.groupby('Acquiring Institution').value_counts().head(5))  #pandas

faa3 = file1['Acquiring Institution'].dropna().to_numpy()
ufaa3 = np.unique(faa3,return_counts=True)
ind3 = np.argsort(ufaa3[1])[::-1]
print(ufaa3[0][ind3[:5]])


# 8) How many banks has the State Bank of Texas acquired? How many of them were actually in Texas?

print(file1.loc[file1['ST'] == "Texas"]) #pandas

faa4 = file1.loc[file1['ST'] == "Texas"]['Acquiring Institution'].dropna().to_numpy() # ---> it can find the number of banks acquired in Texas
sat = file1['ST'].to_numpy()   #----> ye state ka value dega 
print(np.sum(faa4))            #---> sum kare ga total of banks acquired 
print(np.sum(faa4 &(sat == 'Texas')))   #---> ye state ka value dega ji texas me he 


# 9) What is the most common city in California for a bank to fail in?

print(file1.groupby(['ST','City']).value_counts().head(5))

faa6 = file1.loc[file1['ST'] == 'California']['City'].dropna().to_numpy()
faa7 = file1['City'].dropna().to_numpy()

# ind6 = np.argsort(faa6)[::-1]
print(faa6)













