# 1. What is pythion 
# ---> pythin is a hight level programming language that is widely used for web development, data analysis, artificial intelligence,
#      scientific computing, and many other applications. It is known for its simplicity, readability, and ease of use.

# how to print in python
# ---> you can use print() function to print the data in python

# example:
print("hello world")

# What is Variables
# ---> variables are used to store data in python and they can be changed during the execution of the program

# example:

a= 10 #this is a variable that is used to store the value 10 and it can be changed during the execution of the program
b=20
c=a+b
print(c)

# python data type
# ---> python has many data types
# 1. int --> integer data type is a hole number
print(type(1))

# 2. float --> float data type is a number but it can be decimal number
print(type(1.0))

# 3. str --- > str data type is a string data type that is used to store text data
print(type("hello world"))

s= "Python Programing"

print(s.capitalize())  #it can capital the fast later
print(s.casefold())
print(s.center(40,"*")) #it can the string to center with argumat
print(s.count('t')) #it can count the text later in string
print(s.format("python=10")) 
print(s.encode())
print(s.upper()) #change the char to upper case
print(s.lower()) #change the char to lower case
print(s.swapcase()) #change upper to lower and lower to upper
print(s.isalnum()) #is give boolen value for number or not
print(s.replace('P','R')) #replace the later or word


# 4. bool ---> boolian data type is a contains only two values true or false ,0 or 1
print(type(True))

# 5. list ---> list data type is a collection of data that is ordered and changeable
print(type([1, 2, 3]))

# 6. tuple ---> tuple data is a collection of data that is ordered and unchangeable
print(type((1, 2, 3)))

# 7. dict ---> dict data type is a collection of data that is unordered,changeable and indexed by a key-value pair
print(type({"name": "alice", "age": 20}))

# 8. set ---> set is a samilar to list but it is unordered and unindexed and it is used to store unique values
print(type({1, 2, 3}))

# 9. None ---> it can be used to represent the absence of a value or a null value.
print(type(None))

# 10. function ---> function is a block of code that is used to perform a specific task and it can be called multiple times in the program
def add(a, b):
    return a + b

print(type(add))

# 11. class ---> cass is a blueprint for creating objects and it can contain attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
