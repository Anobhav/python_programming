'''dictionary -- key value pairs, mutable, hetrogenious data'''

my_details = {
    'name': 'anobhav',
    'age': 21,
    'language': 'hindi, english'
}

print(my_details)

mydet_2=dict(my_details) # constructor methord of defining a dictionary

print(mydet_2['name'])
print(mydet_2['age'])
print(mydet_2.keys())
print(mydet_2.values())

mydet_2['city']='delhi'
print(mydet_2)

dummy_dict={
    'maths' : 10,
    'science' : 20
}

mydet_2.update(dummy_dict)
print(mydet_2)
mydet_2.pop('name')
print(mydet_2)
