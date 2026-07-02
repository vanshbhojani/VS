# File=open("text1.txt","w")
# File.write("this is fest file!!")
# File.close()


# d={}

# for i in range(1,31):
#     d[i]=i*i


# File=open("text2.txt","w")
# File.write(str(d))
# File.close()    


# write w
# append a
# read r


# file=open("text4.txt","r")
# print(file.read())
# file.close()



# file=open("text3.txt","w+")
# file.write("this is w+ method")
# file.seek(0)
# print(file.read())
# print(file.tell)
# file.close()



# file=open("file1.txt","w+")
# file.write(str(d))
# file.seek(0)
# print(file.read())
# file.close()

# r+
file=open("file2.txt","r+")
file.seek(0)
print(file.read())
print(file.write("hello"))
file.close()



# A+

# file=open("text.txt","a+")
# file.write("\nvansh")
# file.seek(0)
# print(file.read())
# file.close()