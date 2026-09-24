import numpy as np
"""
arr = np.array([1,2,4,5,8,5,7,8,9])
print(arr)
print(arr.mean()) # mean can work --> sum of arr / total number of values 
print(arr.var()) # variance can work --> sum of arr squares /total number of values - mean of arr
print(arr.std()) # standard deviation of the array  : square root of variance of the array

print(np.median(arr)) #return mide value it can shot the value and return mide value like a array [1,2,4,5,5,7,8,8,9] so in this mide is 5 

# if in median can have 2 value then n1 + n2 /2

#for example :

arr = np.array([1,2,3,4,5,6,])

print(np.median(arr)) #3+4/2  = 3.5
"""
"""
# np.floro can round the number go to nearest backword round figer like 5.9 come to 5 and 8.6 can go to 8 
# np.ceil can go to next number folat can be like 5.2 6 and 8.4 go to 9 it can complate number in uper number 

arr =np.array([12.34 ,67.89,23.01,45.44])
print(np.floor(arr))
print(np.ceil(arr))


"""
# log 
    # log can work like 10 to the power of x
# What power do I need to raise a number to, to get another number?

arr =np.array([2,3,5,9,10])

print(np.log(arr))
print(np.log10(arr))
print(np.log2(arr))






























