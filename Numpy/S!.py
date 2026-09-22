import numpay as np

# data type :
# string  " "
# dict    {}
# tupel   ()
# list    []
# set     ()

# l1 = [1,2,3,4,5]

# print(l1)
# print(l1[2])
# print(l1[1:4]) 
# print(l1[1:5:1])
# print(l1[::2])
# print(l1[::-1])

# print(l1.pop(2))
# print(l1)
# print(l1.remove(4))
# print(l1)
# print(l1.append(6))
# print(l1)
# print(l1.count(3))
# print(l1)
# print(l1.index(4))
# print(l1)
# print(l1.insert(2,3))
# print(l1)
# print(l1.sort())


# tupel

# t1 = (1,2,3,4,5,6,7)

# print(t1)
# print(t1[2])
# print(list(t1))
# print(t1[2:7])
# print(t1[2:7:2])


# dictonary

# dict can be created by using {} or dict() function

# d1 = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight"}

# print(d1)
# print(list(d1.keys()))
# print(list(d1.values()))

# print(d1[1,6]) # This line will raise an error because the key should be a single value, not a tuple.

# print(d1[4])

import numpy as np

arr= np.array([[1,2,3,4,5],
               [6,7,8,9,10],
               [11,12,13,14,15]])

print(arr)
print(arr.ndim) # ndimensions
print(arr.shape) # shape of array
print(arr.itemsize) 
print(arr.dtype)
print(arr.size)