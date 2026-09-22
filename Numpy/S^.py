import numpy as np
import pandas as pd
# loadtxt 

"""
it can read the data in to txt file and return the array it can read clean data
it can only read numbers 
"""
"""
file_1 = np.loadtxt("Numpay/class.txt" ,skiprows=1)
print(file_1)


# mean ,median ,std ,var , len , reshape

arr_mean_1 = np.mean(file_1)
print(arr_mean_1)

arr_median_1 = np.median(file_1)
print(arr_median_1)

arr_len_1 = len(file_1)  # len are the out of the array function in numpy
print(arr_len_1)

arr_reshape_1 = np.reshape(file_1,(4,2)) # reshape can change the shape of the array
print(arr_reshape_1)

"""
#genfromtxt : 
"""
file_2 = np.genfromtxt("Numpay\class2.txt" ,skip_header=1,delimiter = ",",dtype = None)
print(file_2)

file_2 = np.genfromtxt("Numpay\class2.txt" ,skip_header=1,delimiter = ",",dtype = None,filling_values = 0)
print(file_2)

# np.unique : remove the duplicate value from the array

arr = np.array([1,1,2,3,1,4,3,5,6,7,5,8,9,10,])
print(np.unique(arr))

"""
"""# np.count_nonzero : count the number of non zero value in the array 

arr = np.array([1,0,2,0,3,0,4,5,6,5,0,np.nan,0]) # nan is not a number
np_count =np.count_nonzero(arr)
print("len of array is :",len(arr))
print("after np.count_nonzero :",np_count)
"""

# task :

"""

file_3 = pd.read_excel("Numpay/numpy_dataset.xlsx").to_numpy()
print(file_3)


file_3 = np.genfromtxt("Numpay/numpy_dataset.csv", delimiter=",", dtype=None)
print(file_3)


"""