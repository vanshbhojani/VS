# condition
# what is condition
# ---> condition is used to check if a certain condition is true or false and it is used to make decisions in python

# if / elif / else statement

# example:

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


