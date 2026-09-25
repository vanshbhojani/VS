# pandas  

# use :
        # 1. data cleaning 
        # 2. EDA -->exploratory data analysis
        # 3. data visualization
        # 4. data transformation

# pandas use for data Analysis

import pandas as pd
import numpy as np


s1= pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s1)
print(type(s1))

# pandas give defolt index

faa = pd.Series(['vansh',12,'priya',78,87,'mitu'])
print(faa)

# pandas are case sensitive for function

# dictionary
isafaa = pd.Series({
    'vansh':22,
    'priya':33,
    'mitu':44,
    'divya':19,
})

print(isafaa)

# how to give a index 

lol = pd.Series([1,2,3,4,5],index = ['vansh','priya','mitu','divya','asha'])
print(lol)

wtf = pd.Series([1,2,3,4,5],index = ['vansh','priya','mitu','divya','asha'],name = 'lol')
print(wtf)
wtf['priya'] = 22    # ---> you can change the value in side of list using index
print(wtf)

# name --> can give a name to the series
# index --> can give a index to the series

# Series vs DataFrame
# datafram me 2 mathod list or dict















