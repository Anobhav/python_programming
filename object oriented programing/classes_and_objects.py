# classes refered to as blueprint 
# object refered to as specific instance of that blueprint 

class Humans :
    name = "Anobhav"
    age = 20


object = Humans()
print(type(object))
print(object)   # print address of the object 

print(object.name)
print(object.age)

''' using constructor to initialize the values at object level not at the class level like we did above'''

class Person :
    def __init__(self, name, age='0'): # age ='0' is a optional parameter
        self.name = name
        self.age = age
''' if multiple init are defined then the last init is considered by default '''
person1 = Person("a", 1)
person2 = Person("b", 2)
person3 = Person("c")

print(person1.name, person1.age)
print(person2.name, person2.age)
print(person3.name, person3.age)

''' methords / behaviour of objects are of 3 types 1) instance 2) class 3) static '''

# 1 instance methord 
class students :
    def __init__(self, name, id, age='0'): # age ='0' is a optional parameter
        self.name = name
        self.id = id
        self.age = age
    # methord 
    def findage(self):
        return self.age

stud=students("anobhav", 1101, 11)

print(stud.findage())

# 2 class methord 
class person2_class:
    country = "India"
    ''' class methord has access to the class properties not the object properties '''
    @classmethod
    def greet(cls):
        print("hello from the",cls.country)
    
per2 = person2_class()
per2.greet()    


# static methord 


class person3_class:
    country = "India"
    @staticmethod # it does not have access to class or object propertie
    def hello():
        print("hello")
    
per3 = person3_class()
per3.hello()