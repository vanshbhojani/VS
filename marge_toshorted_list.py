l1 = [1, 2, 4]
l2 = [1, 3, 4]

# combine lists
l3 = l1 + l2

# bubble sort
for i in range(len(l3)):
    for j in range(i + 1, len(l3)):
        if l3[i] > l3[j]:
            l3[i], l3[j] = l3[j], l3[i]

print(l3)

            




        