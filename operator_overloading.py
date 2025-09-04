class Num:
    def __init__(self, num):
        self.num= num 
    
    def __add__(self, U):   # magic methord also called dunder method.... Python uses for the + operator
        return self.num + U.num
    
num1 = Num(5)
num2 = Num(7)

res = num1 + num2
print(res)


'''
summary of magic methords 

| Operator | Magic Method | Example Translation      |
| -------- | ------------ | ------------------------ |
| `+`      | `__add__`    | `a + b` → `a.__add__(b)` |
| `-`      | `__sub__`    | `a - b` → `a.__sub__(b)` |
| `*`      | `__mul__`    | `a * b` → `a.__mul__(b)` |
| `==`     | `__eq__`     | `a == b` → `a.__eq__(b)` |
| `str()`  | `__str__`    | `str(a)` → `a.__str__()` |

'''