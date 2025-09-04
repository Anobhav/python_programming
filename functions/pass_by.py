# pass by value means that the value itself is not passed, a copy of the value is passed
# pass by value is immutable datetype, number, string, tuple

num = 10
def modified_value(num : int):
    num+=1
    print(f"modified value of function is:{num}")

def origianl_value(num : int) -> int:
    print(f"origianl value of num is:{num}")


modified_value(num)
origianl_value(num)

# pass by reference mean passsing mutable datatype, list dictionary

mylist=[1,2,3,4,5]
def modify_list(li):
    li.append(6)
    print(li)

print("before calling function", mylist)

modify_list(mylist)