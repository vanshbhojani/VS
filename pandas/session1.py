import pandas as pd
import mysql.connector


# how to rad csv file,excel file,json file, sql file,etc

# sql file
"""
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vansh#2004",
    database="moviesdb"
)

# Read table
query = "SELECT * FROM movies"

df = pd.read_sql(query, conn)

print(df.head())

# Close connection
conn.close()
"""

# csv file
"""
r = pd.read_csv("pandas/read.csv")
print(r)

print(r.head(2))
print(r.tail(2))
print(r.columns)
print(r.dtypes)
print(r.info())
print(r.isnull().sum())
print(r.describe())

"""

# excel file
"""
e = pd.read_excel("pandas/read.excel")

print(e)  #  it was just damo so it cant loud data so it can be giveing error

"""

# json file
"""
j = pd.read.json("pandas/read.json")
print(j)  #  it was just damo so it cant loud data so it can be giveing error
"""




