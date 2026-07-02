import random

otp=random.randint(1001,9999)

d={}

while True:
    menu="""
    press 1 for signup
    press 2 for login
    press 3 for forgot_password
    press 4 exit

    """
    print(menu)
    choice=int(input("Enter then choice : "))

    if choice==1:
        name= input("Enter name : ")
        email=input("Enter email : ")
        mobile=int(input("Enter number : "))
        password=input("Enter password : ")
        cpassword=input("Enter cpassword : ")

        if password==cpassword:
            d['password']=password
            d['email']=email
            d['mobile']=mobile

            print("signup is ok")

        else:
            print("invalide password")   

  
    elif choice==2:
        email=input("enter email : ")
        password=input("enter password : ")

        if d['email']==email and d['password']==password:
            print("login successfully")

        else:
            print("invalide login")
    

    elif choice==3:
        mobile=int(input("enter mobile number : "))

        if d['mobile']==mobile:
            print("your otp is :",otp)

            uotp=int(input("Enter otp : "))

            if uotp==otp:
                password=input("Enter password : ")

                d['password']=password

                print("password is updated")
            else:
                print("otp is invelide")

        else:
            print("mobile number is not same") 

    elif choice==4:
        print("thainq")
        break

    else:
        print("invalide choice")
        break                       



