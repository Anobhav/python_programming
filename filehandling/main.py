file= open(r"filehandling\file.txt","r")

'''for line in file:
    print(line)'''

'''print(file.read())'''

'''with open (r"filehandling\file.txt", 'r') as file:
    data = file.read()
    print(data)'''

# read only the first x no of chat 

with open (r"filehandling\file.txt", 'r') as file:
    data = file.read(5)
    print(data)


''' 
r - read
w - write 
a - append
r+ - read and write 
w+ = write and read
a+ = append and read 
'''

file = open(r"filehandling\file.txt", 'a')
file.write("hello world again")

file.close

with open (r"filehandling\file.txt", 'w') as file:
    file.write("hello everyone")