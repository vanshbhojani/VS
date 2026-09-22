# from multiprocessing.reduction import _register
import random

ac_no=random.randint(10001,99999)


class Bank:

    def ac_register(self):
        name=input("Enter The Name : ")
        email=input("Enter The Email : ")
        mobile=int(input("Enter The Mobile : "))
        password=input("Enter The Password : ")
        cpassword=input("Enter The Cpassword : ")
        balance=5000

        print("your account number is :",ac_no)
        print("balance is submited ",balance)
        self.balance=balance
        self.ac_no=ac_no


    def deposit(self):
        dammount=int(input("Enter The Dammount :"))
        ac=int(input("Enter The ac :"))

        if ac==self.ac_no:

            self.balance+=dammount

            print(self.balance)
            

    def wiadraw(self):
        wammount=int(input("Enter wiadraw ammount :"))
        ac=int(input("Enter The ac :"))

        if ac==self.ac_no:

            self.balance-=wammount


    def balance_check(self):
        ac=int(input("Enter The ac :"))

        if ac==self.ac_no:
            print(self.balance)


        

    
obj=Bank()

menu="""

    press 1 for account create 
    press 2 for exit

"""
print(menu)

choice=int(input("Enter your choice"))

if choice==1:
    obj.ac_register()

    while True:
        menu1="""

        press 1 for desposit
        press 2 for wiardaw
        press 3 for check balance
        press 4 Exit 

"""
        print(menu1)

        choice1=int(input("Enter your choice1 : "))
        
        if choice1==1:

            obj.deposit()

        
        elif choice1==2:

            obj.wiadraw()

        elif choice1==3:

            obj.balance_check()  

               
                


