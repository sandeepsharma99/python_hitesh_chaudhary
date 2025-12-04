# Nested if: Check if a number is positive, and if so, whether it's even or odd.

num = 21

if num > 0:
    if num % 2==0:
        print(num,": Positive even")
    else:
        print(num, ": Positive odd")
else:
    print("Negative No.")