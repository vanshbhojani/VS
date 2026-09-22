"""
Session 9 - Cleaning & Saving Scraped Data Save as: CSV Excel JSON Handle missing values Practical: Clean scraped dataset using pandas.

id    name    age    salary   
101   tisha   20      90000 
102           19      80000
103   vansh           70000 
104   sujal   22      95000
105   mayank  21    

# insights  : 
function  : 
1. missing value : df.isnull()
2. fill missing value : df.fillna()
"""

# read csv file  : 
# import pandas as pd

# df =pd.read_csv("customer_data.csv")
# print(df)
'''
missing_value = df.isnull().sum()
print(missing_value)
"""
Customer_ID        1
Gender             1
City               1
Age                0
Purchase_Amount    1
Orders             0
"""

df['Customer_ID']=df['Customer_ID'].fillna("C020")
df['Gender']=df['Gender'].fillna("UNKNOWN")
df['City']=df['City'].fillna("UNKNOWN")

df['Purchase_Amount']=df['Purchase_Amount'].fillna(df['Purchase_Amount'].mean()).astype(int)

# print(df.info())

print(df.head())  # default 5 rows  first 5 rows

df.to_csv("cleaned_data.csv",index=False)
df.to_excel("cleaned_data.xlsx",index=False)

df.to_json("cleaned_data.json",orient="records",indent=4)
'''

import pandas as pd


'''
df = pd.read_csv("WEB_SCRAP\cleaned_data.csv")

df.info()

# df.notnull()
notfind = df.isnull().sum()
print(notfind)


df['Orders']=df['Orders'].fillna(df['Orders'].mean()).astype(int)
df['Purchase_Amount']=df['Purchase_Amount'].fillna(df['Purchase_Amount'].mean()).astype(int)

print(df)

'''


df =pd.read_csv("WEB_SCRAP\hamon_googlefit_medical_realistic .xls")

nulll_valu =df.isnull().sum()
print(nulll_valu)

df['bp_systolic']= df['bp_systolic'].fillna(df['bp_systolic'].mean()).astype(int)

# print(df.info())

print(df)
