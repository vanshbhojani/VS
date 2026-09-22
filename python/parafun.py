#2) function with parameter without return type


# def fun1(n):
#     print(n)


# n1=int(input("Enter the value : "))
# fun1(n1)



def right_angel(n):

    for i in range(1,n+1):
        print("*"*i)


n1=int(input("Enter the number : "))
right_angel(n1)        



# def loop(n):
#     i=1
#     while(1<=n):
#         print(i)
#         i=i+1

# n1=int(input("Enter the value : "))
# loop(n1)        


#3)function without parameter with return type


def fact():
    n=int(input("Enteer the value : "))
    fact=1
    
    
    for i in range(1,n+1):
        fact=fact*i

        return fact

result=fact()
print(result)






def fun1():
    n1=10
    n2=20

    return n1+n2

#result=fun1()
#print(result)

print(fun1())



