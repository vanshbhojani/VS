# type of loop 
'''
while loop  :  it is used when we don't know the number of iteration.
for loop    :  it is used when we know the number of iteration.
do while loop :  it is used when we want to execute the loop at least once.
'''
"""
for i in range(1,11):
    print(i)
# in loop last variable is stored in memory.
# if you want to go 10 then your loop should be dne with last + 1

# in a loop we can use break and continue or pass statement.

for i in range(1,11):

    if i ==4:
        print("break statement is executed")
        break
    print(i)

# in a break statement is used to terminate the loop when a certaion condition is met. 
# In this case, when the variable i reaches 4, the loop will stop executing and exit the loop. The output will be:

for i in range(1,11):
    if i==4:
        print("continue statement is executed")
        continue
    
    print(i)

# in a continue statement is used to skip the current iteration of the loop and move on to the next iteration.    

for i in range(1,11):
    if i==4:
        pass
        print("pass statement is executed")
    print(i)

# in a pass statement is used as a placeholder for code that will be added later.
# it doed not affect the flow of the program and is often used in situations where a statement is required syntactically but no action is needed.
"""
"""
# while LOOP :

i=1
while i<10:
    print(i)
    i+=1

# while loop can need a stop steatment if not stop then loop continue 
"""
# pattern  : 

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    
"""
for i in range(1,6):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(6,i,-1):
        print("*",end=" ")
    print()    

for i in range(1,6):
    for k in range(1,i):
        print("",end="")
    for j in range(6,i,-1):
        print("*",end=" ")
    print()    

for i in range(6,1,-1):
    for k in range(6,i,-1):
        print(" ",end=" ")
    for i in range(1,i):
        print("*",end=" ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print("@",end=" ")
    print()    

for i in range(6,1,-1):
    for j in range(1,i):
        print("@",end=" ")
    print()    
"""
"""for i in range(1,6):
    for k in range(1,i+1):
        print(" ",end=" ")
    for j in range(6,i,-1):
        print("@",end=" ")
    print()        

for i in range(1,6):
    for k in range(1,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("@",end=" ") 
    print()           """
"""
for i in range(6,1,-1):
    for k in range(1,i):
        print("@",end=" ")
    print()    

for i in range(1,6):
    for j in range(1,i+1):
        print("@",end=" ")    
    print()    


for i in range(6,1,-1):
    for k in range(6,i,-1):
        print(" ",end=" ")
    for j in range(1,i):
        print("#",end=" ")
    print()            

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("#",end=" ")
    print()        
"""

# For i = 1:
# spaces → 4
# # → 1
# For i = 2:
# spaces → 3
# # → 2
# For i = 3:
# spaces → 2
# # → 3

# @ @ @ @ @ @ @ @ @ @
# @ @ @ @     @ @ @ @
# @ @ @         @ @ @
# @ @             @ @
# @                 @
"""
# Top half
for i in range(5, 0, -1):

    # Left side
    for j in range(1, i + 1):
        print("@", end=" ")

    # Center space
    for k in range(1, 2 * (5 - i) + 1):
        print(" ", end=" ")

    # Right side
    for j in range(1, i + 1):
        print("@", end=" ")

    print()


# Middle empty line
print()"""

"""
# @                 @
# @ @             @ @
# @ @ @         @ @ @
# @ @ @ @     @ @ @ @
# @ @ @ @ @ @ @ @ @ @ 

# Bottom half
for i in range(1, 6):

    # Left side
    for j in range(1, i + 1):
        print("@", end=" ")

    # Center space
    for k in range(1, 2 * (5 - i) + 1):
        print(" ", end=" ")

    # Right side
    for j in range(1, i + 1):
        print("@", end=" ")

    print()

"""

# @                 @ 
# @ @             @ @ 
# @ @ @         @ @ @ 
# @ @ @ @     @ @ @ @ 
# @ @ @ @ @ @ @ @ @ @ 
# @ @ @ @ @ @ @ @ @ @ 
# @ @ @ @     @ @ @ @ 
# @ @ @         @ @ @ 
# @ @             @ @ 
# @                 @


# top half


for i in range(1, 6):

    # Left side
    for j in range(1, i + 1):
        print("@", end=" ")

    # Center space
    for k in range(1, 2 * (5 - i) + 1):
        print(" ", end=" ")

    # Right side
    for j in range(1, i + 1):
        print("@", end=" ")

    print()

# bottom half
for i in range(5, 0, -1):

    # Left side
    for j in range(1, i + 1):
        print("@", end=" ")

    # Center space
    for k in range(1, 2 * (5 - i) + 1):
        print(" ", end=" ")

    # Right side
    for j in range(1, i + 1):
        print("@", end=" ")

    print()
