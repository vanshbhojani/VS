# l=["vansh",10,10.10,True,"way"]

# print(l)

# l.append("10") # add data in last 
# print(l)

# print(l.count(1)) #count the value in list

# l.insert(2,"python") #add value in that location
# print(l)

# print(l.pop(1)) #show that value in loc

# l.remove("vansh") #remove value in list
# print(l)


# l=[]
# ev=[]
# od=[]

# for i in range(1,31):
#     l.append(i)
#     if i%2==0:
#         ev.append(i)

#     else:
#         od.append(i)



# print(l)
# print(ev)
# print(od)            





# l=[64,54,24,66,23,86,34]

# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]


# print(l)            

# l.sort()

# print("small number : ",l[0])
# print("largert number : ",l[-1])
# print("largert number : ",l[-2])


# lst = [1, 2, 3, 4, 5]
# rev_lst = lst[::-1]
# print(rev_lst)   # [5, 4, 3, 2, 1]



# l=[1,2,3,4,5,6]
# l1=l[::-1]
# print(l1)

# lst = [1, 2, 3, 4, 5 ,6 ,7]
# rev_lst = []

# for i in lst:
#     rev_lst = [i] + rev_lst

# print(rev_lst)   # [5, 4, 3, 2, 1]



# n=int(input("Enter the number : "))


# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("prime")
#     else:
#         print("not prime")
# else:
#     print("number grater then 1")

#-------pointer mathod---------#n
l=[1,2,3,4,5,6]

l1=0
l2=len(l)-1

while(l1<l2):
    l[l1],l[l2]=l[l2],l[l1]
    l1+=1
    l2-=1
print(l)    


