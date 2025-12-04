# Transportation Mode Selection : Choose a mode of tranportation based on distance(e.g., <3km: Walk,3-15: Bike, >15:Car)
Distance = 25

if Distance < 3:
    print("Walk")
elif Distance <= 15:
    print("Bike")
elif Distance > 15:
    print("car")