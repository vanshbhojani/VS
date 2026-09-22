# np.arange , reshape . np.ones , np.zeros , np.full , np.eye , np.identity , np.diagonal , np.tril , np.triu , np.diag , np.trace , np.transpose  : 

import numpy as np

"""arr =np.full(9,fill_value=99,dtype=int)  # by default dtype is float 
arr =np.full((3,4),fill_value=99,dtype=int)  # by default dtype is float

print(arr)
"""
"""
# arr = np.arange(1,10)
arr = np.arange(1,20,2)
print(arr)
"""
"""
arr = np.arange(1,10).reshape(3,3)
print(arr)
arr = np.arange(1,33).reshape(8,4)
print(arr)

arr = np.arange(1,33).reshape(2,4,4)
print(arr)

arr = np.arange(1,33).reshape(2,2,2,4)
print(arr)
"""

# np.ones and np.zeros
"""
arr = np.ones(15,dtype=int)
print(arr)
arr = np.zeros(15,dtype=int)
print(arr)

arr = np.ones((3,4),dtype=int)
print(arr)

arr = np.zeros((3,4),dtype=int)
print(arr)
"""

# full and empty
"""
arr = np.full(15,fill_value=92,dtype= int)
print(arr)

arr = np.full((3,4),fill_value=10,dtype=int)
print(arr)

arr= np.empty(15,dtype= int)
print(arr)

arr = np.empty((4,4),dtype=int)
print(arr)
"""

# np.eye : identity  matrix  

"""
arr = np.eye(4,dtype=int)
print(arr)

arr = np.eye(3,4,dtype=int)
print(arr)

arr = np.identity(4)
print(arr)
"""

# np.transpose :
"""
arr= np.array([[1,2,3,4,5],
               [6,7,8,9,10],
                [11,12,13,14,15]])
print(arr)

arr1 = np.transpose(arr)
print(arr1)
"""

# np.linespace 

"""arr = np.linspace(1,20,5) # 1 to 20 in 5 equal parts
print(arr)

arr= np.linspace(1,20,5,retstep=True) # 1 to 20 in 5 equal parts and return step size 
print(arr)
"""

import random 


# random numbers

arr = np.random.rand(5) # 5 random numbers between 0 and 1
print(arr)
arr = random.randrange(1,10) # 5 random numbers between 1 and 10
print(arr)
arr= random.randrange(1,10,2) # 5 random numbers between 1 and 10 with step size 2
print(arr)
arr = random.randint(1,10) # 5 random numbers between 1 and 10
print(arr)
arr = np.random.randint(low = -10 , high = 10,size=(3,4)) # 5 random numbers between -10 and 10 in 3 rows and 4 columns
print(arr)

arr2 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
               [11,12,13,14,15]])

np.random.seed(10)
arr= np.random.randint(1,20,(3,4))  
print(arr)



