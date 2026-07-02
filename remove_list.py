l = [1, 2, 3, 4, 5, 6, 7, 1, 3]

num = int(input("Enter a number to remove: "))

# if num in l:
#     l = [x for x in l if x != num]   # removes all occurrences
#     print("All {num}'s removed successfully.")
# else:
#     print("{num} not found in the list.")

# print("Updated list:", l)

# print(l.remove(1))

i=0
while(i<len(l)):
    if num==l[i]:
        l.remove(num)
    i=i+1

print(l)


