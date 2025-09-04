''' encapsulation -> bind the data / state of the object with methord... done to make or to hide the state / data '''
# we use getting / setter methord to define which can be access by whome it can be accessed 
class Person :
    def __init__(self, name, car):
        self.__name = name
        self.__car = car

    #getter and setters - public methord to allow the controlled interactions 
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    def getcar(self):
        return self.__car
    def setcar(self,car):
        self.__car=car

per=Person("ano", "bmw")
print(per.getname())
print(per.getcar())

per.setname("anobhav")
print(per.getname())