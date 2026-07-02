# Same method name → speak()
# Different classes → Dog, Cat, Cow
# Different output depending on object

# --------Example------------#

# 1.

class Animal:
    def sound(self):
        return "Animal make sound"
    
class Dog(Animal):
    def sound(self):
        return "woof woof!"

class Cat(Animal):
    def sound(self):
        return "meow meow!"

class cow(Animal):
    def sound(self):
        return "moo moo!"


def animal_sound(animal):
    print(animal.sound())



d=Dog()
c=Cat()                    
co=cow()

animal_sound(d)
animal_sound(co)