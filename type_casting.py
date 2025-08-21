''' type castings means converting one data type into another '''
''' 2 types of type casting -> implicit ( automatic ), explicit ( programmers do forcefully ) '''

#implicit 

x=5
y=5.5
total=x+y
print(total)

z = '10'
print(type(z))  # This prints the type of 'z', which is <class 'str'>

int_z = int(z)  # Convert string to integer
print(type(int_z))  # This prints the type of 'int_z', which is <class 'int'>
