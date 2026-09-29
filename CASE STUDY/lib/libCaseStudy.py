# 1. Project Overview

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Dataset

df = pd.DataFrame({
    'Machine_ID' : ['M101','M102','M103','M104','M105','M106','M107','M108','M109','M110'],
    'Temperature' : [78,85,68,75,80,70,65,60,70,75],
    'Speed' : np.random.randint(0,10,10),
    'Torque' : np.random.randint(1400,1600,10),
    'Tool_Wear' : np.random.randint(0,60,10),
    'Machine_Failure' : np.random.randint(0 ,2,10),
})

# print(df)
"""
# TO_csv can create a csv file from a dataFrame
dataset = df.to_csv('dataset.csv',index = False)
print(dataset)
"""

# 3. Phase 1 – Load and Understand Data

dataset = pd.read_csv('CASE STUDY/lib/dataset.csv')
"""
print(dataset.head())
print(dataset.tail())
print(dataset.count())
print(dataset.columns)
print(dataset.dtypes)
print(dataset.value_counts())
# print(dataset.notnull().sum())
print(dataset.isna().sum())
print(dataset.describe())
print(dataset.shape)
"""

# 4. Phase 2 – NumPy Analysis
"""
maen_t = np.mean(dataset['Temperature'])
print("mean temperature is :",maen_t)
max_t = np.max(dataset['Temperature'])
print("max temperature is :",max_t)
min_t = np.min(dataset['Temperature'])
print("min temperature is :",min_t)
std_t = np.std(dataset['Temperature'])
print("std temperature is :",std_t)

arr = np.array(dataset[['Temperature', 'Speed', 'Torque','Tool_Wear']])
print(arr)
print(arr.shape)
print(arr.ndim)
mean_arr = np.mean(arr)
print(mean_arr)
max_arr = np.max(arr)
print(max_arr)
min_arr = np.min(arr)
print(min_arr)
"""

# 5. Phase 3 – Pandas Data Analysis
"""
faa = (dataset['Temperature'].mean(),dataset['Speed'].mean(),dataset['Tool_Wear'].mean())
print(faa)

humm = dataset['Machine_Failure'].value_counts()
print(humm)

hummm = dataset['Machine_Failure'].value_counts(normalize=True)*100
print(hummm)

# haa = dataset['Machine_Failure'].mean()*100
# print(f"{haa:.0f}%")

lol = dataset[(dataset['Temperature']>70)]
print(lol)

ok = dataset[(dataset['Temperature'] > 75 ) | (dataset['Tool_Wear'] > 25)]
print(ok)

humm = dataset['Machine_Failure'].mean()*100
print(humm)
"""

# 6. Phase 4 – Feature Creation


dataset['power'] = dataset['Speed']*dataset['Torque']
print(dataset[['Speed','Torque','power']])
height_power = dataset['power'].max()
low_power = dataset['power'].min()
print(height_power,low_power)
















