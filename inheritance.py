# singlie inheritance

# class A:
#     def forclass(self):
#         print("this is class A")

# class B(A):
#     def forclassb(self):
#         print("this is class b")

# obj=B() 

# obj.forclass()


# multipal inheritance


# class A:
#     def classA(self):
#         print("class A")

# class B:
#     def classB(self):
#         print("class B")


# class C(A,B):
#     def classC():
#         print("show both A and B")

# obj=C()

# obj.classA()
# obj.classC()


# multilevel inheritance


# class A:
#     def classA(self):
#         print("this is class A")

# class B(A):
#     def classB(self):
#         print("this is class B") 

# class C(B):
#     def classC(self):
#         print("this is class C")               

# obj=C()

# obj.classB()
# obj.classA()
# obj.classC()


# hierarchical inheritance

# class parent:
#     def classA(self):
#         print("i am a father")

# class chaild1(parent):
#     def chaild1(self):
#         print("i am chaild")

# class chaild2(parent):
#     def chaild2(self):
#         print("i am scearend born")


# obj1=chaild1()
# obj2=chaild2()

# obj1.classA()
# obj2.classA()



# ------Example-------#
# 1.

# class Animal:
   
#     def __init__(self,name):
#         self.name=name
        

#     def sound(self):
#         return "this is animal sound's"
    

# class Dog(Animal):
#     def speck(self):
#         Dogo_name=input("Enter your dog name :")
#         self.Dogo_name=Dogo_name

#         return "woof woof"
    

# class Cat(Animal):
#     def speck(self):
#         Cat_name=input("Enter your cat name :")
#         self.Cat_name=Cat_name
#         return "meow meow"


# d=Dog("Dog")
# c=Cat("Cat")

# print(d.speck())
# print(c.speck())

# print("dog name : " ,d.Dogo_name)
# print("cat name : " ,c.Cat_name)



# 2.

class payment:
    def __init__(self,ammount):
        self.ammount=ammount
        

    def pay(self):
        return "pending...."    


class cardpayement(payment):
    def __init__(self, ammount,card_number):
        super().__init__(ammount)
        self.card_number=card_number

    def pay(self):
        return f"paid ${self.ammount} using card with {self.card_number[-4]}"
    

class wallatepayment(payment):
    def __init__(self, ammount,walat_id):
        super().__init__(ammount)
        self.walate_id=walat_id

    def pay(self):
        return f"paid {self.ammount} vansh upi{self.walate_id}"    

class upipayment(payment):
    def __init__(self, ammount,UPI_id):
        super().__init__(ammount)
        self.UPI_id=UPI_id


    def pay(self):
        return f"paid {self.ammount} with ({self.UPI_id})"


p1=cardpayement(500,"4465 5465 4654 5654 5454")
p2=upipayment(5000,"vansh@upi.com")

print(p1.pay())
print(p2.pay())