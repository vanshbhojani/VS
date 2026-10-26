# outlier  : 
"""
days     sales 

1        2000
2        1500
3        2800
4        1200
5        1000
6        1270
7        2500 
8        3400
9        40000
        =========

avg sales : 6850  ------> per day  6850 , ----->  1960 


outlier 2 methods 

1.IQR : inter quartile range
    formula  : IQR = Q3 - Q1
               Q3 = sales * 0.75 
               Q1 = sales * 0.25
               
    lower bound : Q1 -1.5 * IQR
    upper bound : Q3 + 1.5 * IQR

2. z -score : 
    from scipy.stats import zscore  

"""

import  pandas as pd 

"""df=pd.DataFrame({
    'days':[1,2,3,4,5,6,7,8,9],
    'sales' :[2000,1500,2800,1200,1000,1270,2500,3400,40000]
})

print(df)
"""
# IQR : Q3 - Q1
# what is IQR? ---> Interquartile Range 0

"""Q3 = df['sales'].quantile(0.75)
Q1 = df['sales'].quantile(0.25)
IQR = Q3 -Q1

print("IQR : \n",IQR) 

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("lower bound : \n",lower_bound)
print("upper bound : \n",upper_bound)

outlier_days = df[(df['sales'] < lower_bound) | (df['sales'] > upper_bound)][['days','sales']]
print("outlier days : \n",outlier_days)

# outlier fill method  : clip
df['sales'] = df['sales'].clip(lower_bound, upper_bound)
print("sales after outlier fill : \n",df['sales'])
"""

# z-score : 

from scipy.stats import zscore
"""
z_score = zscore(df['sales'])
print("z-score : \n",z_score) 

outlier_days = df[(z_score < -2.5) | (z_score > 2.5)][['days','sales']]
print("outlier days : \n",outlier_days)
"""

# date : 

df = pd.DataFrame({
    'joining_date':['2023-01-01',
                    '2020-02-02',
                    '2021-03-12',
                    '2009-04-05',
                    '2011-05-11',
                    '2001-06-19',
                    '2022-02-17',
                    '2023-03-21',
                    '2025-09-12'],
    
    'name' :["vansh","sujal","mayank","tisha","roshni","krunal","dhruv","sahil","ankit"],
    "salary":[12000,24000,56000,78000,34000,12000,24000,56000,78000]
})
print(df)
df['joining_date'] = pd.to_datetime(df['joining_date'])

df['days'] =df['joining_date'].dt.day
df['month'] =df['joining_date'].dt.month
df['year'] =df['joining_date'].dt.year

print(df)

"""
HW : 

1. year wise total salary  
    ex :sum of all the salary of year 2023 : 68000 
"""

df['year_salary'] = df.groupby('year')['salary'].transform('sum')
year_2023_salary = df[df['year'] == 2023]['salary'].sum()
print(df)
print("year_2023_salary : \n",year_2023_salary)

"""
2. month wise total salary
    ex : march  : sum of all the salary of march  
"""

march_salary = df[df['month'] == 3]['salary'].sum()
print("march_salary : \n",march_salary)