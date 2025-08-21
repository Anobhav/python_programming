''' there are 6 types of data in python 
Numerical -- int, float, complex  
Sequence - list, tuple, str
Nbolean - t/f
dictionary - like map   
Set 
'''

# numerical

x=5
y=5.5
z=10+15j
power_to_10=3e4
power_to_num=pow(3,3)
print(f' integer x holds {x}, float y holds {y}, complex z holds {z}')
print('power holds : ',power_to_10)
print('power to num : ',power_to_num)
''' in order to find type of we use '''
print(type(x))
print(type(power_to_num))


print(round(y))

nums=[10,20,30,40,50]
print(min(nums))
print(max(nums))
