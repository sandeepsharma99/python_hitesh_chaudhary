# Validate the Input : Keep asking the user for input untill they enter a no between 1-100

while True:
    number = int(input("enter a no. b/w 1-100 : "))
    if 1<=number<=100:
        print("Thanks")
        break
    else:
        print("Invalid number Try again")