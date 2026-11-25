import matplotlib.pyplot as plt
import pandas as pd

# d = pd.DataFrame({
#     'company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
#     'salary': [100, 120, 80, 90, 200, 210]
# })

# print(d)

# plt.bar(
#     d['company'], 
#     d['salary'],
#     color=['red', 'blue', 'green', 'orange', 'purple', 'brown']
# )

# print("Bar chart created successfully.")
# plt.show()

'''boxx = pd.DataFrame({
    'company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'salary': [100, 120, 80, 90, 200, 500]
})

plt.boxplot(
    boxx['salary']

)

print("Box plot created successfully.")
plt.show()'''

'''
pai = pd.DataFrame({
    'company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'salary': [100, 120, 80, 90, 200, 500]
})

plt.pie(
    pai['salary'],
    labels=pai['company'],
    autopct='%1.1f%%'
)

print("pie plot created successfully.")
plt.xticks(rotation=45)
plt.show()
'''


'''
lin = pd.DataFrame({
    'company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'salary': [100, 120, 80, 90, 200, 500]
})

plt.plot(
    lin['salary'],
    lin['company'],
    # autopct='%1.1f%%'
)

print("lin plot created successfully.")
plt.xlabel('Salary')
plt.ylabel('Company')
plt.title('Salary vs Company')
plt.show()
'''

# donut
'''
don  = pd.read_csv("matplotlib/student_marks (1).csv")

plt.pie(
    don['marks'],
    labels=don['name'],
    autopct='%1.1f%%',
    wedgeprops={'width': 0.7, 'edgecolor': 'black', 'linewidth': 2}
)

print("lin plot created successfully.")
plt.show()
'''


sup = pd.read_csv("matplotlib/sample superstore.csv",  encoding='latin1')

category_sales = sup.groupby('Category')['Sales'].sum()
'''
bars = plt.bar(
    category_sales.index,
    category_sales.values,
    color=['#FF5733', '#33FF57', '#3357FF']
)

plt.title('Total Sales by Category')

plt.bar_label(
    bars,
    fmt='%.2f',
    fontsize=10,
    padding=2
)

plt.xlabel('Category')
plt.ylabel('Total Sales')

plt.show()
'''

don = plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct='%1.1f%%',
    wedgeprops={'width': 0.7, 'edgecolor': 'black', 'linewidth': 2}
)

plt.title('Sales Distribution by Category')
plt.show()

