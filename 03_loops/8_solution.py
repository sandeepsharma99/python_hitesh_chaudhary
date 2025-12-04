# Prime Number Checker :

# number = int(input("enter a Number : "))
# is_prime = True
# for i in range(2,number):
#     if (number%i)==0:
#         is_prime = False
#         print("Not a prime Number")
#         break
#     else:
#         print("Prime No")


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

count = 0   # to count prime numbers

for num in range(start, end + 1):
    if num > 1:                     # 0 and 1 are not prime
        is_prime = True
        for i in range(2, num):     # check divisors
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

print("Total Prime Numbers:", count)
