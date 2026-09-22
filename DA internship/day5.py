  # oop: object oriented programming

# class : blueprint of object
# object : instance of class
# ex 1: frute --> apple ,banana,orange

# calss can create with class name and attribute

# for ex 1:
"""
class frute:
    def f1(self):
        l1 = ["apple","banana","orange"]
        return l1

cl=frute()    
print(cl.f1())

"""
# ex 2:
"""
class phone:
    def phones(self,choice):
        def apple():
            l1= ["iphon12","iphon13","iphon14"]
            return l1

        def sumsung():
            l2= ["sumsung12","sumsung13","sumsung14"]
            return l2

        def vivo():
            l3= ["vivo12","vivo13","vivo14"]
            return l3

        if choice == "apple":
            return apple()
        elif choice == "sumsung":
            return sumsung()
        elif choice == "vivo":
            return vivo()
        elif choice == None:
            return apple(),sumsung(),vivo()
        
p=phone()
# print(p.phones("sumsung"))
print(p.phones(None))
"""
# class tyope public private protected
"""
class f1:
    def names(self):
        dict1 = {"name":"maam","age":25,"gender":"male"}
        return dict1

    def __init__(self):    #salf __init__ method is used to initialize the object 
        self.name= "meet"
        self.age = 25
        self.gender = "male"
        self._first_name = "vansh"
        self.age = 22
        self.gender = "male"

    def data__init__(self):    #if you can create multiple __init__ method then you can use this method to initialize the object  or name the class with __init__
        self.last_name = "Bhojani"
        self.age = 25


F=f1()
print(F.name)
print(F.names())
print(F._first_name)
print(F.age)
print(F.gender)
F.data__init__()      # this method is used to initialize the object and same as __init__ method but without self parameter
print(F.last_name)
"""

# public : can access from anywhere in the class
"""
def public():
    print("public class method")

public()


# private : can access from inside the class

def private():
    __name = "this is private class "   # this variable is private you can use __ before the variable name so it will not be accessed from outside the class and ti can make the variable as private
    print(__name)                       # this variable is private you can use __ before the variable name so it will not be accessed from outside the class and ti can make the variable as private

private()

class private():
    def private_method(self):
        __age = 25
        print(__age)
class private2(private):
    def changes(self):
        print(self.__age)

met=private2()
met.private_method() # if you can type met.changes() then it will not work because changes() is not defined in private class

# protected : can access from inside the class and outside the class

class protected:
    def __init__(self):
        self._name = "this is protected class as"

class protected2(protected):    # this class is inherited from protected class
    def change(self):           # protected method can access from inside the class and outside the class
        print(self._name)

p=protected2()
print(p._name)
"""

# constructer : this is used to initialize the object and same as __init__ method but without self parameter it can call object automatically when we create object

# syntex: 
    # __init__ 

# type of cunstructor

# 1. default constructor
# 2. parameterized constructor
# 3. non parameterized constructor

# what is default constructor ---> when we create object without any parameter then it will call default constructor

# for ex 1:
"""
class f1:
    def __init__(self,name,age,gender): # this is default constructor can call object automatically when we create object and  it will call this constructor
        self.name = name
        self.age = age
        self.gender = gender


f=f1("vansh",25,"male") # f can call the self parameter and  name --> vansh , age --> 25 , gender --> male
print(f.name)
print(f.age)
print(f.gender)


# parameterized constructor

class f2:
    def __init__(self,name,age,gender): # we can define parameter hear name age and gender 
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):   # in this method we can access the object parameter
        print("name is ",self.name) # now we can put the object parameter in the method
        print("age is ",self.age)
        print("gender is ",self.gender)

cf2 = f2("vansh",25,"male") # we can create object with parameter name age and gender 
cf2.display() # call the display method
"""
"""
# non parameterized constructor:

# waht is non parameterized constructor? --> when we create object without any parameter then it will call default constructor

class f3:
    def __init__(self):
        self.vansh = "jay"
        self.meet = "meet"

    def car(self):
        print(self.vansh)

f3=f3()
print(f3.car())

class f4:
    def __init__(self):
        self.vansh = "vansh"
        self.age = 22
        self.city = "Ahmdeabad"
        self.gender = "male"
        print("this line is called when we create object")

    def display(self):
        print("name is ",self.vansh)
        print("age is ",self.age)
        print("city is ",self.city)
        print("gender is ",self.gender)

f4=f4()
f4.display()

# jo non perameterized constructor he vo salf ke saiva koy bhi peremeter nahi hai 
"""
"""
class f5:
    __name = "ram"    # this variable is private you can use __ before the variable name so it will not be accessed from outside the class and ti can make the variable as private
    __age = 25

    def display(self):
        self.name= "mina"
        self.age= 22
        print(self.__name)
        print(self.__age)

f5=f5()
# print(f5.__name)
# print(f5.__age)
f5.display()
# f5.__name = "ramesh"
# f5.__age = 22
# f5.display()

"""

"""
class f6:
    _name = "ram"    # this variable is private you can use __ before the variable name so it will not be accessed from outside the class and ti can make the variable as private
    _age = 25

    def d(self):
        print(self._name)
        print(self._age)

f6=f6()
f6.d()
"""
# protected : can access from inside the class and outside the class 


# inheritance  : when we create child class then it will inherit the parent class

# type of inheritance
# 1. single inheritance
# 2. multiple inheritance
# 3. multiple inheritance with override
# 4. hierchical inheritance
# 5. hybrid inheritance


# 1. single inheritance

# class f7:
#     def f1(self):
#         print("this is f1")

# class f8(f7):
#     def f2(self):
#         print("this is f2")
#         print(self.f1())

# f8=f8()
# f8.f2()


# single inheritance can be used when we have only one parent class


# 2. multiple inheritance

# class f9:
#     def f1(self):
#         print("this is f1")

# class f10:
#     def f2(self):
#         print("this is f2")

# class f11(f9,f10):
#     def f3(self):
#         print("this is f3 function and it can inherited f1 and f2 function")
#         self.f1()
#         self.f2()

# f11=f11()
# f11.f3()

# it can be used when we have more than one parent class to inherit the function

# 3 . multiple inheritance 
"""
class f12:
    def f1(self):
        self._name = "ram"
        print("this is f1")

    def f2(self):
        print("this is f2")
        
class f13(f12):
    def f3(self):
        print("this is f3 class")
        self.f1()

class f14(f13):
    def f4(self):
        print("this is class f4")

        self.f1()
        print(self._name)
        self.f2()
        self.f3()

f14=f14()
f14.f4()
"""
"""
class f12:
    def f1(self):
        self.name = "ram"
        self.age = 22
        self._gender = "male"
        self.id = 1001
        self.roll_no = 21

class f13(f12):
    def f2(self):
        self.teacher_name = "gita"
        self.teacher_classes = 5
        self.teacher_dept = "computer"
        self.teacher_id = 1001

class f14(f13):
    def f3(self):
        print("student information")
        self.f1()
        # print(self.name)
        # print(self.age)
        # print(self._gender)
        # print(self.id)
        # print(self.roll_no)
        # print("teacher information")
        self.f2()
        # print(self.teacher_name)
        # print(self.teacher_classes)
        # print(self.teacher_dept)
        # print(self.teacher_id)
        print(self.__dict__) # this is the dictionary of the object it can gve the all the variable of the object
        print(self.__class__) # this is the class of the object 

f14=f14()
f14.f3()
"""
"""
class f12:
    def f1(self,name,age,gender,id,roll_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id
        self.roll_no = roll_no

class f13(f12):
    def f2(self,teacher_name,teacher_classes,teacher_dept,teacher_id):
        self.teacher_name = teacher_name
        self.teacher_classes = teacher_classes
        self.teacher_dept = teacher_dept
        self.teacher_id = teacher_id

class f14(f13):
    def f3(self):
        print("student information")
        self.f1(
            name="vansh",
            age=23,
            gender="male",
            id=101,
            roll_no=21)
        print("student name is ",self.name)
        print("student age is ",self.age)
        print("student gender is ",self.gender)
        print("studdnt id is ",self.id)
        print("student roll no is ",self.roll_no)
        
        print("teacher information")
        self.f2(
            teacher_name="mirabai",
            teacher_classes=2,
            teacher_dept="matches",
            teacher_id=1001)
        print("teacher name is ",self.teacher_name)
        print("teacher classes is ",self.teacher_classes)
        print("teacher dept is ",self.teacher_dept)
        print("teacher id is ",self.teacher_id)

f14=f14()
f14.f3()
"""
"""
class f12:
    def f1(self,name,age,gender,id,roll_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id
        self.roll_no = roll_no

class f13(f12):
    def f2(self,teacher_name,teacher_classes,teacher_dept,teacher_id):
        self.teacher_name = teacher_name
        self.teacher_classes = teacher_classes
        self.teacher_dept = teacher_dept
        self.teacher_id = teacher_id

class f14(f13,f12):
    def f3(self):
        # self.f1()
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.id)
        print(self.roll_no)
        print(self.teacher_name)
        print(self.teacher_classes)
        print(self.teacher_dept)
        print(self.teacher_id)

        
f14=f14()
f14.f1(name="ram",
       age=22,
       gender="male",
       id=1001,
       roll_no=21)  # it can call the object
f14.f2(teacher_name="gita",
       teacher_classes=5,
       teacher_dept="computer",
       teacher_id=1001)   # it can call the object
# it can store the object in the list and can use the list to call the object 

f14.f3()  # it can call the object so we can put the object parameter in the method so the values are print at the time of call the object f3 method
"""
"""
class f12:
    def __init__(self):
        self.name = "vansh"
        self.id = 78610
        self.age = 22
        self.gender = "male"
        self.roll_no = 21
        self._teacher_name = "dishant saha"
        self._teacher_classes = 5
        self._teacher_dept = "DA"


class f13(f12):

    def teacher(self):
            print(self._teacher_name)
            print(self._teacher_classes)
            print(self._teacher_dept)
            

class f14(f13,f12):
     def f3(self):
            print(self.name)
            print(self.age)
            print(self.gender)
            print(self.id)
            print(self.roll_no)

f14=f14()
f14.teacher()
f14.f3()
"""

class f12:
    _name = "vansh"
    _age = 22
    _gender = "male"
    _id = 78610
    _roll_no = 21
    _teacher_name = "dishant saha"
    _teacher_classes = 5
    _teacher_dept = "DA"

    def sel_mat(self,name,id,age,gender,roll_no,teacher_name,teacher_classes):
        self.var1=(name,
                  id,
                  age,
                  gender,
                  roll_no,
                  teacher_name,
                  teacher_classes
                  )

        return self.var1
        
class f13(f12):
    def __init__(self):
        self.var =(self._name,
                   self._age,
                   self._gender,
                   self._id,
                   self._roll_no,
                   self._teacher_name,
                   self._teacher_classes
                   )

class f14(f13,f12):
    def call(self):

        print("---------- private ----------")
        print(self.var)

        print("\n---------- self ----------")

        print(self.sel_mat(
            name = "meet",
            id= 1102,
            age = 15,
            gender = "male",
            roll_no = 1234567890,
            teacher_name = "mirabai",
            teacher_classes = 2,
        ))


f14=f14()
f14.call()




















