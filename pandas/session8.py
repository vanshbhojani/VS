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