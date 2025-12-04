# Movie ticket Pricikng : Movie ticket are priced based on age: $12 for adults(18 and over),$8 for childrens .  Everyone get a $2 discount on wednesday

age  =  50
day = "wednesday"

price = 12 if age>=18 else 8  # Ternery Operator

if day == "wednesday":
    price -=2

print("Ticket price for you is $", price)