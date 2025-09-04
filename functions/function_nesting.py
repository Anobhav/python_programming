#function nesting means -> function inside a function 
def outer():
    print("hello from the outer")

    def inner():
        print("hello from the inner")
    return inner


fn=outer() # called outter, executed outer, returns inner
fn()        # calls inner, executed inner


