''' sets - all elements are unique, hetrogenious, mutable, un-ordered'''

my_set={1,2,3,4,5,1,2,3,4,5,'anobhav'}
print(my_set)

my_set2=set(my_set)

my_set2.add(10)
print(my_set2)

my_set2.discard(1)
print(my_set2)
