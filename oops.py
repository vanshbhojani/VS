# oops object oriented programing System

# 5)main

# 1.class - object
# 2.inheritence
# 3.polimorphism
# 4.encaps
# 5.abstraction


# function - blocks

# blocks - class 

# class
#     is a collection of data member and member functions


# object - 
# is instance of class throut the object we can access all the properties of class


# class Myclass:

#     def myfun(self):
#         n=int(input("Enter the number : "))

#         if (n%2==0):
#             print("Even")

#         else:
#             print("Odd") 

#     def myfun1(self):
#         n1=int(input("Enter the number n1: "))
#         n2=int(input("Enter the number n2: "))

#         if(n1>n2):
#             print(n1,"is big") 

#         else:
#             print(n2,"is big")              


# obj=Myclass()
# obj.myfun()
# obj.myfun1()




class Myclass2:
    menu='''
    1. Enter for singin
    2. Enter for Login 
    '''

    print(menu)

    d={}
    while True:

        choice=int(input("Enter your choice : "))

        if choice==1:
            Name=input("Enter the Name : ")
            email=input("Enter the email : ")
            phone=int(input("Enter the phone number : "))
            password=input("Enter the password : ")
            cpassword=input("Enter the cpassword : ")

            if password==cpassword:
                d['name']=Name
                d['email']=email
                d['password']=password
                d['phone']=phone


                print("singing complat!!")

            else:
                print("password is not carect ")    


        elif choice==2:
            email=input("Enter the Email : ")
            password=input("Enter the password : ")

            if d['email']==email and d['password']==password:
                print("Login is complat!!")

            else:
                print("inveled deteais !!")    





#1)singal
#2)multipal
#3)maltilevel
#4)haybride
#5)