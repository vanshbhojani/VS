# condition
# what is condition
# ---> condition is used to check if a certain condition is true or false and it is used to make decisions in python

# if / elif / else statement

# example:
"""
for i in range(1,11):
    if i==4:
        print("break statement is executed")
        break
    print(i)

a = 10
b = 20
c = 30

if a>b:
    print("a is greater than b")
    if a>c:
        print(" a is grater than c")

    else:
        print(" c is grater than a")

else:
    print("b is greater than a")
    if b>c:
        print("b is grater than c")

    else:
        print("c is grater than b")


if a>b and a>c:
    print("a is greater ")
elif b>a and b>c:
    print("b is greater ")
else:
    print("c is greater ")    

"""

# Nested if Statements in Python
# ---> nested if statements are used to check multiple conditions in python and it is used to make decisions in python 
"""
a = 10
b = 20 
c = 30

if a>b:
    print("a is big")
    if a>c:
        print("a is big")
    else:
        print("c is big")
else:
    print("b is big")            

username = input("Enter Your Username: ")

if username == "admin":
    password = input("Enter Your Password: ")

    if password == "admin":
        print("Login Successful")

    else:
        print("Invalid Password")
else:
    print("Invalid Username")

"""

# while with user input
"""
username = input("Enter yout username : ")

if username == "admin":
    password = input("Enter your Password : ")
    
    if password == "vansh123":
        print("Login Successful")
    else:
        while password != "vansh123":
            print("Invalid Password")
            password = input("Enter your password : ")

            if password == "vansh123":
                print("login complate")
            
else:
    print("Invalid Username")
"""

# break and continue
"""
for i in range(1,11):
    if i == 5:
        # print(i)
        print("break statement is executed")
        break
    print(i)

for i in range(1,11):
    if i == 5:
        # print(i)
        print("continue statement is executed")
        continue
    print(i)

for i in range(1,11):
    if i == 5:
        # print(i)
        print("pass statement is executed")
        pass
    print(i)

# example

numbers = [10, 20, 30, 40, 50]

for number in numbers:

    if number == 30:
        print("Number found!")
        break

    print(number)
"""












