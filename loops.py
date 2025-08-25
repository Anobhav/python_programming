'''#for loop -> 

fruits = ["apple", "banana", "cherry", "mango"]
for i in fruits :
    print (i)

for i in range(10):         # in built function starts from 0 to n-1 | we can also put start and end-1 range like range(1,10)
    print(i)

print(" ")
for i in range(2,10,2):     # range (start value, end value, increment value)
    print(i)
'''

'''for i in range(12,0,-3):
    print(i)

for i in range (1,13):
    if(i %4 == 0):
        break

    print(i)
'''
for i in range(1,10):
    if(i%2!=0):
        continue
    print (i)


#while loop
num=15

while num>10:
    print(num)
    num-=1