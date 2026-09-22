import numpy as np
"""
# sliceing a numpy array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a[0:5])
print(a[5:10])
print(a[5:10:2])

# slicing a numpy array with a list
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a[[0, 2, 4, 6, 8]])

# # slicing a numpy array with a list and a range
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(a[[0, 2, 4, 6, 8], 1:5])

# slicing a numpy array with a range
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a[1:10])

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]])

print(arr.ndim)
print(type(arr))
print(arr)
print(arr.shape)
"""
arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20]])

# print(arr[::-1,::-1])
# print(arr[1:5:2,0:6:2])
# print(arr[5::-1,4::-2])
# print(arr)
# print(arr[0:6:3,1:7:2])
# print(arr[5:1:-2,5:0:-2])
# print(arr[:4:2,:5:2])
# print(arr[3:0:-1,4:0:-2])
# print(arr[:4:2,4:0:-1])
print(arr[3:0:-2,0:5:2])


arr =np.array([
    [1,2,3,4,5],        # 0 ----> 1
    [6,7,8,9,10],       # 1 ----> 2
    [11,12,13,14,15],   # 2 ----> 3
    [16,17,18,19,20],   # 3 ----> 4
    [21,22,23,24,25]    
]) 

# fancy indexing

# print [[4 ,5] 
#        [14,15]]   
# print(arr[0 : 3 :2,3 :])

#output :  print [[2,8,14,20]]
#          row       col
print(arr[[0,1,2,3],[1,2,3,4]])  


