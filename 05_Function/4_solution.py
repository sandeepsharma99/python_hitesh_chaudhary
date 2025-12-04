#  Returning Multiple value : Create a function that return both are and circumference of a circle gbiven its radius
import math
def radius(r):
    return 2*math.pi*r,math.pi*(r**2)

a,c = radius(3)
print("circumference",a,"area",c)