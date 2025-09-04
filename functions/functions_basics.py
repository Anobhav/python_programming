x=10 # global variable 
y=10 # global variable 

def addition_function(x,y):
    result=x+y # local variable 
    print(f"result of addition operation is {result}")

def sub(x,y):
    result=x-y # local variable 
    return result

addition_function(10,10)
print(sub(10,10))

# functions with default arguement 
def default_functions(name="User", message="Good morning"):
    print(name, message)

default_functions("anobhav")

# keyword arguments, this allows to pass arguements in any order opposite to what postional argruments do 
def default_functions2(name="User", message="Good morning"):
    print(name, message)

default_functions2(message="good afternoon", name="anobhav")

# how to take variable number of arguments 
def sum_numbers (*args):
    print(type(args))
    print(args)
    sum=0
    for num in args :
        sum+=num
    return sum

print(sum_numbers(1,2,3,4,5,6))

'''
error case 
def fn(*args,a,b)
    print(a)
    print(b)
    print(args)

fn(1,2,3,4,5)

to solve this error case we can either pass *args after a,b or pass arguments with explicit naming
'''

# how to put arguments of variable length  -> using Kwargs

def display_infor(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, "->", value)

display_infor(name="anobhav", age=100, city="Paris")