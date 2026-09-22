# d={}

# for i in range(1,31):
#     d[i]=i*i

# print(d) 


d = {'p':100,'q':600,'r':300}

d1={'p':200,'q':300}

d2={}

for i,j in d.items():
    for l,k in d1.items():
        if i==l:
            d2[i]=j+k


print(d2)            




# l = [6, 8, 10]
# l1 = [31, 14, 16]

# d = {}

# for i in range(len(l)):
#     d[l[i]] = l1[i]

# print(d)
