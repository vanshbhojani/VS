class A:
    def fast(self):
        num=int(input("Enter the number : "))
        if num>1:    
            for i in range(2,num):
                if num%i==0:
                    print("prime")
            else:
                print("not prime")
        else:
            print("number is garater then 1")


class B:
    def secand(self):
        l=[1,3,4,5,6,7,8]
        l1=[]
        for i in l:
            l1=[i]+l1
        print(l1)

class c(A,B):
    def theard(self):
        num=int(input("Enter the number : "))
        l=[1,2,3,4,5,6,1,2,3,4]
        i=0
        while(i<num):
            if num==l[i]:
                l.remove(num)
            i+=1
        print(l) 

obj=c()
obj.fast()  
obj.secand()
obj.theard()      

