# in python explicit overloading is not possible, we cant call one perticular function explicitly, by default the last defined parameter is taken

class Calculator:
    def add(self, a, b):
        return a+b
    
    def add(self, a, b, c):
        return a+b+c
    
cal = Calculator()

print(cal.add(5,6,4))

# implicit overloading : 

class calculator:
    
    def add(self, a, b, c=0):
        return a+b+c
    
cal = calculator()

print(cal.add(5,6))
