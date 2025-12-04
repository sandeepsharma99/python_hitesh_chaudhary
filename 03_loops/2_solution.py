# Sum of Even Number :  
num = int(input("enter a Number"))
sum = 0

for i in range(1,num+1):
    if i%2 == 0:
        sum+=1

print(sum,"sum of even No.")