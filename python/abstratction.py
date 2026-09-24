from abc import ABC,abstractmethod

class Employer(ABC):
    def salary(self):
        pass



class Employer1(Employer):
    def salary(self):
        return 30000


class Emoloyer2(Employer):
    def salary(self):
        return 20000


class Employer3(Employer):
    def salary(self):
        return 10000            
    

obj=Employer1()
obj1=Emoloyer2()
obj2=Employer3()


print(obj.salary())
print(obj1.salary())
print(obj2.salary())
