# function

# type of function 
# 1. no arg no return
# 2. no raturn with arg
# 3. with arg no return
# 4. with arg with ruturn

# ex 1. no arg no return

"""def add(): # add() is function name 
    a=int(input("enter the number : ")) #function intigration
    b=int(input("enter the number : "))
    print("sum is : ",a+b)

add() # calling thr function 
add()
add()
print("it was praties")
add()

#in this cans arg is not in code it can given by user

"""

# no arg with return
"""
def function1(): # function name is function1 
    a = int(input("enter the number : ")) #function intigration 
    b = int(input("enter the number : "))
    return a+b

function1()
"""

# with arg no return

"""
def function2(a,b): #fun with arg 
    print("sum is :",a+b) #fun intigration

function2(22,25) # fun can give the arg in number
function2(65,21)    

"""

# with arg with return 
"""
def function3(a,b):
    return a+b

print(function3(20,10))    

#in this case function have arg is 20,10 and return somthing because it can return the a+b

"""

# number is prime or not 
"""
def number_p(n):
    count = 0

    for i in range(1,n+1):
        if n % i ==0 :
            count +=1

    if count == 2:
        return True
    else:
        return False
    
print(number_p(11))
"""

# local variabal
"""
def x():
    z=10
    print(z)
x()

# local varibal can access in to the function you can not print z in out off function
"""

# global varibal 

y=20

def fool():
    global y
    y = 100
    print(y)

fool()

# *args can only taks the *args
"""
def add(*args):
    return sum(args)
    
print(add(23,54))
print(add(10,20))

"""






