
import numpy as np

# aithematic  : + - * / % // 
"""
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
b= np.array([[9,8,7],[6,5,4],[3,2,1]])

print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
"""
# matrix multiplication : np.matmul ,np.dot , a@b

# If matrix A is \(m\times n\), and matrix B is \(n\times p\), then multiplication is possible:
# (m×n​)(n​×p)=m×p
"""
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
b= np.array([[9,8,7],[6,5,4],[3,2,1]])

print(np.matmul(a,b))
print(np.dot(a,b))
print(a@b)
"""

# rowwise and  col wise sum  : 

"""a= np.array([[1,2,3],
             [6,5,4],
             [7,8,9]])"""
"""
print(np.sum(a)) # total sum

print(np.sum(a,axis=0))  # col wise sum
print(np.sum(a,axis=1))  # row wise sum

print(np.min(a)) # total min
print(np.min(a,axis=0))  # col wise min
print(np.min(a,axis=1))  # row wise min

print(np.max(a)) # total max
print(np.max(a,axis=0))  # col wise max
print(np.max(a,axis=1))  # row wise max

"""
"""
print(np.argmin(a)) # total min index
print(np.argmin(a,axis=1))  # row wise min index
print(np.argmin(a,axis=0))  # col wise min index

print(np.argmax(a)) # total max index
print(np.argmax(a,axis=1))  # row wise max index
print(np.argmax(a,axis=0))  # col wise max index

"""
"""
a= np.array([[1,2,3],
             [6,5,4],
             [7,8,9]])

print(np.sort(a)) # total sort
print(np.sort(a,axis=0))  # col wise sort
print(np.sort(a,axis=1))  # row wise sort

print(np.argsort(a)) # total sort index
print(np.argsort(a,axis=0))  # col wise sort index
"""

"""
student = np.array(80,87,90,78,57,47,87,78,68,65)
print(student)
"""
"""
for i in range(1,51):
    if i % 2 == 0:
        print(np.array(i))
    # print()

"""

"""
a= np.linspace(100,500,num = 8)
print(a)

"""
"""

# matrix can parfom the max min zeros ones etc function are part of matrix

matrix =np.zeros((4,4))
print(matrix)

eye= np.eye(4)
print(eye) #eye can return when the number is same as the arry rutn
"""

"""

# randint can ganrate the random number's beatwin two value 

mark = np.random.randint(35,100,20)
print(mark)
"""
"""
fru = np.array([["apple","banana"],
               ["orange","mango"],
               ["pich","jack"]])

print(np.random.choice(fru.flatten(),3))

# choice funcation can work the to select the iteam in array to select the how many item can you want to select in a array 
# flatten function can select the random value's in array to values 
"""


np.random.seed(50) # random number generator ko ek starting point (seed) deta hai.
arr=np.random.randint(1,101,10) # 1 --> is starting 101 --> is ending 10 --> is number you want 
print(arr)

np.random.seed(10)
arr=np.random.randint(0,10,(3,3))# it can make it in array
print(arr)