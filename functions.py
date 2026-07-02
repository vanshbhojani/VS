''' using def to create function
in a function parameters are coll to run the function'''



def function_name():
    print("hello")


function_name()

def frut():
    print("name1:","banana",'apple','orange')
    print("name2:",'vansh','jay','meet')

frut()

def function_frut(name1,name2):
    print("name1:",name1)
    print("name2:",name2)

function_frut(["banana","mango","apple"],["vansh","jay","binod"])


def add(a,b):
    return a+b,a-b,a*b,a/b

xy=add(5,5)
print(xy)


def function_names(names):
    for i in names[1:3]:
        print(i)

my_value=["vansh","jay","meet","man","ram"]
function_names(my_value)
print(my_value)

def function_orange(name="Guest"):
    print("hello",name)

function_orange()
function_orange("vansh")


def function_apple(a,b=10):
    return a+b


asd=function_apple(10,20)
qwe=function_apple(10)
print(asd,qwe)
