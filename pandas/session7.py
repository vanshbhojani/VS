import pandas as pd

df = pd.DataFrame({
    'day' : [1,2,3,4,5,6,7,8,9],
    'salary' : [2000,1500,2800,1200,1000,1270,2500,3400,40000]
})

print(df)

avg = df['salary'].mean().sum()
print(avg)

import pandas as pd
import  numpy as np

df = pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name" :["peter patel","paul nagrani","george sharma","ringo chauhan","mary shah"],
    "salary":[12000,24000,56000,78000,34000],
    "age" :[12,34,56,78,56],
    "department" : ["HR","HR","IT","IT","Finance"]
})

# group by  with  agg : 

"""group_wise_salary_department = df.groupby(
    'department')['salary'].agg(['sum','mean','count','max','min'])

print("group by department : \n",group_wise_salary_department)
"""

# string function  : lower ,upper ,title , replace ,split,partition: 

"""lower_name = df['name'].str.lower()
upper_name = df['name'].str.upper()
title_name = df['name'].str.title()
split_name = df['name'].str.split('a')
partition_name = df['name'].str.partition('a')
print("lower name : \n",lower_name)
print("upper name : \n",upper_name)
print("title name : \n",title_name)
print("split name : \n",split_name)
print("partition name : \n",partition_name)
"""


