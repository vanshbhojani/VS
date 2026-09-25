# loc(),iloc(),query() 

import pandas as pd 

# loc() : lable based indexing
# iloc() : integer based indexing
# query() : querying

df = pd.DataFrame({
    'id' : [1,2,3,4,5,6,7,8,9,10],
    'name' : ["john","peter","paul","george","ringo","mary","sujal","tisha","vansh","nikhil"],
    'age' : [20,30,35,40,45,25,13,10,9,8],
    'salary' : [1000,3000,4000,5000,6000,2000,3000,200,900,800]
    
})

# wtf = df.loc[1:4] 
# wtf = df.iloc[1:4]
# print(wtf)

"""wtf = df.loc[1:4,['name','salary']] # it can use column name
print(wtf)

faa  = df.iloc[1:4,1:3]  # it can not use column name it was using index number 
print(faa)"""


#query() --> it can ues for multiple condition

"""
df['inc_salary'] = df['salary'] + 1000
print(df)

forexp = df.query('age>20 and salary>3000')
print(forexp)


humm = df.query("['age>20 and salary>3000'] & id in[1,6]")
print(humm)
"""
"""
loji = df[
    ((df["age"]>20)&(df["salary"]>3000)|
     (df["id"].isin([1,6])))
]
print(loji)

"""

nahiji = df.query("age>20 and salary>3000 and 1<id<6")
print(nahiji)


# naji = df[
#     ((df["age"]>20)&(df["salary"]>3000)&(df["id"]>1) & (df["id"]<6))
# ]
# print(naji)





