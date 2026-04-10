# Sum of Even Number :  
num = int(input("enter a Number")) # taking input from user and typecasting int(input(""))
sum = 0

for i in range(1,num+1):  # looping from 1 to 
    if i%2 == 0:
        sum+=1

print(sum,"sum of even No.")