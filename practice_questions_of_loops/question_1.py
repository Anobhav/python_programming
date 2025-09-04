# write a progeam to find sun of even number from 1 to 20 
sum=int(0)

for i in range(1,21):
    if i%2==0:
        sum+=i
    else:
        continue

print(f"sum of even numbers between 1 to 20 is - {sum}")