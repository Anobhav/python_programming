# write a program if the number is prime or not 

num=int(input("enter a number"))
isprime=True
if num<=1:
    print("invald input")

else:
    for i in range(2,num):
        if(num%i==0):
            isprime=False
            break

print(f"number entered is: {isprime}")