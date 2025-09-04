# lambda functions also called as anmymous functions, can take any no of arguments, its body, expression is in a single line
# syntax : keyword argument : function 

add= lambda a,b,c : a+b+c
print(add(1,2,3))

def myfunc():
    return lambda msg : print(msg)

myfunc()("hello world")