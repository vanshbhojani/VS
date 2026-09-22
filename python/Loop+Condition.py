# for i in range(1,10):
#     if i%2==0:
#         print(i,"Even")
#     else:
#         print(i,"Odd")

# password="vansh@333"

# for i in range(3):
#     user_pass=input("Enter password : ")

#     if user_pass==password:
#         print("login successful")
#         break

#     else:
#         print("invelid password!!")


# num=int(input("Enter the number : "))

# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("prine number")
#             break
#     else:
#         print("not prime")
            
# else:
#     print("prime number is grater then 1")


# lst = [1, 2, 3, 4, 5]
# rev_lst = []

# for i in lst:
#     rev_lst = [i] + rev_lst

# print(rev_lst)   # [5, 4, 3, 2, 1]


# l=[1,2,3,4,5,6,7]
# l1=[]

# for i in l:
#     l1=[i]+l1

# print(l1)



n=int(input("Enter the number : "))

if n>1:
    for i in range(2,n):
        if n%i==0:
            print("prime number")

    else:
        print("not prime")

else:
    print("prime number is grater then 1")


