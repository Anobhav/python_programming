#abstraction -> showing only the information which is necessary to show and hiding the rest of the information 

'''
abstract class 
1. cant be initialized 
2. atleast 1 abstract methord 
'''

from abc import ABC, abstractmethod

class Animal(ABC) :
    @abstractmethod
    def eat(self):
        pass

#a=Animal()

class Dog(Animal):
    def sleep(self):
        print("Dog is sleeping")

    def eat(self):
        print("Dog is eating")

d=Dog()