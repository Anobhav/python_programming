# write a python program to count to no of vowals in a given sentance 

str="this is a sentance"

count =0

for ch in str:
    if(ch.lower()) in ['a','e','i','o','u'] :
        count+=1
    else:
        continue

print(f"no of vowals is the string are: {count}")

