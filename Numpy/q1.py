import numpy as np

"""
1.Create an array of 10 student marks using np.array().
2.Generate even numbers from 2 to 50 using np.arange().
3.Create 8 equally spaced values from 100 to 500 using np.linspace().
4.Create a 4*4 matrix of zeros.
5.Create a 5*5 identity matrix.
6.Generate 20 random marks between 35 and 100.
7.Select 3 random fruits using np.random.choice().
8.Use np.random.seed(50) and generate 10 random integers between 1 and 100. Compare the output by running the code twice.
"""

# 1.Create an array of 10 student marks using np.array().

marks = np.array([90, 87, 90, 78, 57, 47, 87, 78, 68, 65])
print(marks)

# 2.Generate even numbers from 2 to 50 using np.arange().

even_numbers = np.arange(2, 51, 2)
print(even_numbers)

# 3.Create 8 equally spaced values from 100 to 500 using np.linspace().

arr= np.linspace(100,500,8)  # linspace can generate the evenly spaced values
print(arr)

# 4.Create a 4*4 matrix of zeros.

m1= np.zeros((4,4))
print(m1)


# 5.Create a 5*5 identity matrix.

m2= np.eye(5) # eye can return when the number is same as the arry rutn
print(m2)

# 6.Generate 20 random marks between 35 and 100.

m3 = np.random.randint(35,100,20)
print(m3)

# 7.Select 3 random fruits using np.random.choice().

fru = np.array([["apple","banana","mangp"],
                ["orange","mango","pich"],
                ["pich","jack","apple"]])

print(np.random.choice(fru.flatten(),3))  #flatten function can select the random value's in array to values

# 8.Use np.random.seed(50) and generate 10 random integers between 1 and 100. Compare the output by running the code twice.

m4 = np.random.seed(50)
arr = np.random.randint(1,101,10)
print(arr)

# 9.Use np.random.seed(10) and generate 10 random integers between 1 and 100. Compare the output by running the code twice.

arr = np.random.seed(10)
arr = np.random.randint(1,101,10)
print(arr)




