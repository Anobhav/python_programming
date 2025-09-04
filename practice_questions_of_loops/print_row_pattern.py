# print the following patter

'''
*
**
***
****
*****
'''

row=int(input("enter the no of rows for this pattern"))

for i in range(1,row+1):
    for j in range(1,i):
        print("*", end=" ")
    print("")