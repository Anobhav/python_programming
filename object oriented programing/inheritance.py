class Animal :
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name + " animal is eating")

class Dog(Animal): # dog is the child of animal 
    def __init__(self, name, type):
        Animal.__init__(self,name)
        self.type=type

dog=Dog("Simba", "Dobberman")
dog.eat()

#super keyword is used to access the parent property 

class Parent:
    property = 90

class Child(Parent):  # Inheriting from Parent
    property = 99

    def printing_property(self):
        print("child property -", self.property)
        print("parent property -", super().property)

child = Child()
child.printing_property()
