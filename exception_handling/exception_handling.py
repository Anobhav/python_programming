str="anobhav singh"

for s in str:
    if s!="o":
        print(s)

arr=["A","B","C"]

try:

    for i in range(4):
        print(arr[i])

except:
    print("exception handled")

print ("this line has to be mandatorily executed")


''' raising exceptions on our own '''
'''
x = -1
if x < 0:
    raise ValueError("x cannot be negative")

'''
def operate(num):
    try :
        result= 5/num
    except ZeroDivisionError :
        print("cant divide a number by 0")
    else :
        print(result)
    finally:
        print("execution ended finally is always executed")
operate(0)

''' custom exception '''

class EmptyException(RuntimeError):
    def __init__(self, arguments):
        self.arguments = arguments

    var =""

try: 
    raise EmptyException("variable cant be empty")
except EmptyException as e:
    print(e.arguments)