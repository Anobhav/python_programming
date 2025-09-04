''' 
mainly 2 access modifiers 1) public 2) private 
public -> by default classes, variables, etc all are defined as public 
private -> we need to explicitly define it by using double underscore 
'''

class Person:
    def __init__(self,name, salary):
        self.name= name
        self.__salary=salary

    def name_is(self):
        return self.name
    def getsalary(self):
        return self.__salary # inside the class we can read, outside we cant 
        
per=Person("Ano",10000000)
print(per.name_is())
print(per.getsalary())


''' one & the only way to read a private variable from outside the class '''
print(per._Person__salary)