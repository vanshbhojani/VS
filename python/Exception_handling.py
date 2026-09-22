# 1)developer
# -output-

# 2)User 
# name 446546

# run time errors 

# When error occurs at runtime it is called Exception
# hendel that exception called exception handling 

# -imp-



# try    code excecut

# except throw the error 

# else try exception

# finally finally message you want





# try:
#     n=int(input("Enter the number : "))

#     if(n%2==0):
#         print("Even!!")

#     else:
#         print("Odd!!")

# except ValueError as e:
#     print(e)

# else:
#     print("try executed!!")

# finally:
#     print("dinally!!")


# try:
#     n1=int(input("Enter the value n1 : "))
#     n2=int(input("Enter the value n2 : "))

#     print("Division",n1/n2)        

# except ZeroDivisionError as e:
#     print(e)

# try:
#     n=int(input("Enter the number : "))

#     if(n%n==0):
#         print("Even!!")

#     else:
#         print("Odd!!")

# except:
#     print("invelede input!!")            


import random

otp=random.randint(1001,9999)

d={}


while True:
    menu='''
    press 1 for signup
    press 2 for login
    press 3 for forgot_password
    prees 3 exit
    '''

    print(menu)
    

    choice=int(input("enter choice : "))

    if choice==1:
        try:    
            Name=input("Enter the Name : ")
            email=input("Enter the Email : ")
            mobile=int(input("Enter the Mobile : "))
            password=input("Enter the password : ")
            cpassword=input("Enter the Cpassword : ")
            

            if password==cpassword:
                d['password']=password
                d['email']=email
                d['mobile']=mobile

                print("signup is ok ")
            else:
                print("invelide password ") 

        except ZeroDivisionError and ValueError as e:
            print(e)               

