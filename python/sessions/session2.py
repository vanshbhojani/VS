# Input from user

"""name = input("Enter your name : ") # input() function is used to get input from user
age  = int(input("Enter your age : ")) # int() function is used to convert the input to integer
salary = float(input("Enter your salary : ")) # float() function is used to convert the input to float

print(f"hello {name} ,your age is {age} , and your salary is {salary}")
"""
# Type Conversion
"""
s = "100"

print(type(s)) # it will print the type of s which is str

new_s = (int(s)) # it will convert the str to int and print the value 100

print(type(new_s)) # it will print the type of new_s which is int

i = 100

print(type(i)) # it will print the type of i which is int
new_i = (str(i)) # it will convert the int to str and print the value 100
print(type(new_i)) # it will print the type of new_i which is str
# it is also possible to convert the type of the variable
# example:

a = 100
b = str(a)
c = int(b)

print(type(a)) # it will print the type of a which is int
print(type(b)) # it will print the type of b which is str
print(type(c)) # it will print the type of c which is int

name = "vansh"

print("my name is " + name) # it will print the name of the user

x= 10

print(bool(x)) # it will print the boolean value of x which is True because x is not 0

bool(0) # it will print False
bool(1) # it will print True
bool("") # it will print False because the string is empty
bool("hello") # it will print True because the string is not empty
bool(None) # it will print False because None is not 0
bool(0.0) # it will print False because 0.0 is not 0
"""

# Operators in Python

# Type of operators in python

# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Assignment Operators
"""
# 1. Arithmetic Operators
# ---> Arithmetic operators are used to perform mathematical operations on numbers

#example:

a=10
b=20
c=a+b # it will add the value of a and b and print the result
d=a-b # it will subtract the value of b from a and print the result
e=a*b # it will multiply the value of a and b and print the result
f=a/b # it will divide the value of a by b and print the result
g=a//b # it will divide the value of a by b and print the result
h=a%b # it will calculate the remainder of the division of a by b and print the result
i=a**b # it will raise a to the power of b and print the result

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# 2. Comparison Operators
# ---> comparison operators are used to compare two values and return a boolean value

#example:

x=10
y=20
z=30
a=x<y # it will compare the value of x with y and return True because x is less than y
b=x>y # it will compare the value of x with y and return False because x is not greater than y
c=x==y # it will compare the value of x with y and return False because x is not equal to y
d=x!=y # it will compare the value of x with y and return True because x is not equal to y
e=x<=y # it will compare the value of x with y and return True because x is less than or equal to y
f=x>=y # it will compare the value of x with y and return False because x is not greater than or equal to y
k=x==z # it will compare the value of x with z and return False because x is not equal to z
l=x!=z # it will compare the value of x with z and return True because x is not equal to z
m=x<=z # it will compare the value of x with z and return True because x is less than or equal to z
n=x>=z # it will compare the value of x with z and return False because x is not greater than or equal to z

print(a)
print(b)
print(c)
print(d)        
print(e)
print(f)
print(k)
print(l)
print(m)
print(n)

# 3. Logical Operators
# ---> logical operators are used to combine two or more boolean values and return a boolean value

# example:

a=True
b=False
c=a and b # it will combine the value of a and b and return False because a is True and b is False
d=a or b # it will combine the value of a and b and return True because a is True and b is False
e=not a # it will return False because a is True

print(c)
print(d)
print(e)

val_a = 10
val_b = 20
print(val_a>5 and val_b<30) # it will return True because val_a is greater than 5 and val_b is less than 30
print(val_a>5 & val_b<30) # it will return False because val_a is greater than 5 and val_b is less than 30
print(val_a>5 or val_b<30) # it will return True because val_a is greater than 5 or val_b is less than 30
print(val_a>5 | val_b<30) # it will return False because val_a is greater than 5 or val_b is less than 30
print(not val_a>5 or val_b<30) # it will return False because val_a is greater than 5 or val_b is less than 30


# 4. Assignment Operators
# ---> assignment operators are used to assign a value to a variable

# example:

a = 10
b = 20

c = a + b # it will add the value of a and b and assign the result to c
d = a - b # it will subtract the value of b from a and assign the result to d
e = a * b # it will multiply the value of a and b and assign the result to e
f = a / b # it will divide the value of a by b and assign the result to f

print(c)
print(d)
print(e)
print(f)
"""


























