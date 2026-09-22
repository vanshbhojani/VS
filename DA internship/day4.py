# lambada

# what is lambda?
# lambda is a funcation can write arg and expression 
# syntex :
    # lambda arg : expression
"""
def add(a,b):
    return a+b

print(add(22,25))

a = lambda a,b : a+b
print(a(20,10))
"""
"""
def prime(n):
    count = 0

    for i in range(1,n+1):
        if n % i ==0:
            count+=1

    if count == 2:
        return True
    else:
        return False

print(prime(19))    

prime = lambda n: sum(1 for i in range(1, n + 1) if n % i == 0) == 2

print(prime(19))
"""
"""l1=[1,2,3,4,5,6,7,8,9]

odd =[]
even=[]

for i in l1:
    if i %2 ==0:
        even.append(i)
    else:
        odd.append(i) 

print(odd)
print(even)        

l2=list(filter(lambda x:x %2 == 0 ,l1))
l3=list(filter(lambda x:x %2 == 1, l1))
print(l2,l3)

"""
"""l2=[]
l1=["maam","php","java","c","python","1221"]

for i in l1:
    if i == i[ : :-1]:
        l2.append(i)


print(l2)

l3 = list(filter(lambda x :x == x[::-1],l1))
print(l3)
"""
# recursion function

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return n*fib(n-1)
    
print(fib(5))  


def sum(n):
    if n ==1:
        return 1
    else:
        return n+sum(n-1)

print(sum(10))    








 