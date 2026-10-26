import pandas as pd

df = pd.DataFrame({
    'day' : [1,2,3,4,5,6,7,8,9],
    'salary' : [2000,1500,2800,1200,1000,1270,2500,3400,40000]
})

print(df)

avg = df['salary'].mean().sum()
print(avg)

# IQR = Q3 - Q1
# what is IQR? ---> Interquartile Range 0


