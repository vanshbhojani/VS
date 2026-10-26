import pandas as pd

# join in pandas
# left join in sql
# right join in sql
# full join in sql
# inner join in sql
# outer join in sql
# cross join in sql
# anti join in sql
# semi join in sql
# left = pd.DataFrame({'id':[1,2,3,4,5],'name':['ram','sira','mira','vansh','meet'],'salary':[10000,20000,30000,40000,50000]})
# right = pd.DataFrame({'id':[1,2,3,4,5],'name':['ram','sira','mira','vansh','meet'],'salary':[10000,20000,30000,40000,50000]})
# left.join(right,on='id')
# left.merge(right,on='id')
# left.merge(right,on='id',how='left')
# left.merge(right,on='id',how='right')

# what is semi join ? -- > it is a join operation that returns all rows from the left table and all rows from the right table. The result of the join is the 
#                        Cartesian product of the rows from both tables.
# what is anti join ? -- > it is a join operation that returns all rows from the left table and all rows from the right table. The result of the join is the 
#                        Cartesian product of the rows from both tables.

# what is concat ? -- > it is a function that concatenates two or more dataframes. It takes two or more dataframes as input and returns a single dataframe that contains 
                       # all the rows from the input dataframes.


movies = pd.read_csv('pandas/movies.csv')
directorys = pd.read_csv('pandas/directors.csv')

# print(movies.head())
# print(directorys.head())

directorys = directorys.rename(columns = {'id':'director_id'})

mar = pd.merge(
    movies,
    directorys,
    on='director_id',
    how='left'
)
print(mar)


top5 = (movies['revenue']).sort_values(ascending=False)
print(top5.head(5))

# how to drop a unnamed column in pandas --> df.drop(columns=['column_name'],inplace=True) 

# d_c = movies.drop(columns =[None])
# print(d_c)
# print(d_c.columns)

movies = movies.loc[:, movies.columns.notna() & (movies.columns != '')]

print(movies)


# merge  : 
"""
1. inner join   :
2. left join    : 
3. right join   : 
4. outer join   :  

"""

import pandas as pd

# First DataFrame
"""df_customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

# Second DataFrame
df_orders = pd.DataFrame({
    'customer_id': [1, 2, 2, 4],
    'order_id': [101, 102, 103, 104],
    'amount': [250, 100, 150, 300]
})

print(df_customers)
print(df_orders)
"""
# inner join : 
"""inner_join =pd.merge(
    df_customers,
    df_orders,
    on='customer_id',
    how = 'inner'
)
print("inner join \n", inner_join)
"""
# left_join : left table  saare aayge right table matching value ayegi 

"""
left_join = pd.merge(
    df_customers,  
    df_orders,  
    how = 'left',
    on='customer_id'
)
print("left join \n", left_join)
"""
"""
left join 
    customer_id     name  order_id  amount
0            1    Alice     101.0   250.0
1            2      Bob     102.0   100.0
2            2      Bob     103.0   150.0
3            3  Charlie       NaN     NaN
4            4    David     104.0   300.0
"""
"""right_join = pd.merge(
    df_customers,  
    df_orders,  
    how = 'right',
    on='customer_id'
)
print("right join \n", right_join)
"""
"""
right join 
    customer_id   name  order_id  amount
0            1  Alice       101     250
1            2    Bob       102     100
2            2    Bob       103     150
3            4  David       104     300
"""

# outer join :
"""outer_join = pd.merge(
    df_customers,
    df_orders,
    how = 'outer',
    on='customer_id'
)
print("outer join \n", outer_join)
"""

# concat : 
"""
two_tables_concat = pd.concat([df_customers, df_orders], axis=1)
two_tables_concat = pd.concat([df_customers, df_orders], axis=0)

print("concat \n", two_tables_concat)
"""
# tasks  
"""
1. movies and directors ------> merge -----> movies ----> director_id  directos ----> id 
2. unamed col  drop  with  both movies and directors
3. top 5 movie name earns  highest revenue
"""

movies = pd.read_csv('pandas/movies.csv')
print(movies.head())