
while True:

    menu= """

        1 enter for odd even
        2 enter for nesty
        3 enter for funtoriyal

    """
    print(menu)

    n=int(input("enter the number : "))

    if n==1:
        number=int(input("enter the number : "))

        if number%2==0:
            print("even")
        else:
            print("odd")    

    elif n==2:
        i=1
        fac=1
        number=int(input("Enter the number : "))
        while(i<=number):
            fac=fac*i
            i=i+1
        print(fac)    



            


    