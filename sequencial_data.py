''' list -> can store different type of data together, mutable, supports indexing '''

list_nums=[1,2,3,4,5,6,7,8,9,0]

print(list_nums)

list_nums2=list(list_nums)

print(list_nums2)

mix=[1,2,3,'anobhav']

list3=list(mix)

print(list3)

# we can use the index to print elements 

print(list_nums[3])

# adding elements to a list 

list_nums.append(100) # inserts at the last index
print(list_nums)

list_nums.insert(3,100)
print(list_nums) #inserts at a perticular index 

temp_list=['a','b','c']

list_nums.extend(temp_list)
print(list_nums)

# removing elements from the list 
# pop - removes from the last or at a perticular index
# remove - removes a perticular element 
list_nums.remove(100)

list_nums.pop()
list_nums.pop(3)
list_nums.pop()
list_nums.pop()
list_nums.pop()
print(list_nums)

#how to replace values in list 
list_nums[8]=0
list_nums[1:4]=['a','b','c']


''' string - sequence of characters, immutable  '''

first_name='anobhav'

print(first_name[4])
print(first_name[-4])

last_name='singh'

complete_name=first_name+" "+last_name
print(complete_name)
print(len(complete_name))

# slicing in string 

print(complete_name[2:8])
print(complete_name[2:])
print(complete_name[:10])

# replace in string 

dummy_string='i am good \ni am very good \n i am extra good'

print(dummy_string.replace("i am", "we are"))
print(dummy_string.replace("i am", "they are",1))



''' tuples --> ordered, immutable, different types of data'''

tup_1=(100,200,300,400,500)
tup_2=tuple([1,2,3,4,5,6])
tup_3=tuple('anobhav')
print(tup_1)
print(tup_2)
print(tup_3)

print(tup_3.count('a'))
print(tup_3.index('a'))
print(tup_3[3])
print(tup_3[2:5])