import pandas as pd

df = pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9,10],
    'name':['beena','badal','chirag','sid','jhon','dipu','alu','arjun','sanju','rashmika'],
    'age':[24,25,26,27,28,28,38,24,25,26],
    'department':['engineering','engineering','it','it','engineering','sales','sales','management','management','management'],
    'salary':[1000,2000,3000,4000,5000,5000,15,1000,2000,3000]
})

print(df)

gpsalary = df.groupby('department')['salary'].sum()
print(gpsalary)

df.sort_values(by=['salary'],ascending=False,inplace=True)
print(df)
print(df.tail(5)[["name"]].reset_index(drop=True))

# df['salary'] = df['salary'].reset_index(drop=True)
# print(df)

# df['date'] = pd.to_datetime(["2020-01-01" , "2021-12-31" , "2022-01-01" , "2023-2-12" , "2024-1-12" , "2025-2-12" , "2026-3-12" , "2027-4-12" , "2028-5-12" , "2029-6-12"])

# print(df['date'])

# df['month'] = df['date'].dt.month
# gp = df.groupby('month')['salary'].sum()

# print(gp)



