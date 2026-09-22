# s = input("enter number : ")

# s1=len(s)

# for i in range(0,s1+1):
#     for j in range(i+1,s1+1):
#         s[i],s[j] = s[j],s[i]

# print(s1)        


# s= input("enter number : ")

# rev=""

# for s in range(0,s+1):



# l=['e','t','y','w','q','s'] 


# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         l[i],l[j] = l[j],l[i]


# print(l)        



s= input("Enter name  : ")

center=len(s)//2

if len(s)%2==0:
    print("please enter odd length !!")

else:
    print(s[center-1]+s[center]+s[center+1])    

  