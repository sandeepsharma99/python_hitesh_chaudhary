# 1.Basic Class Object: creat a car class with attribute like brand and model. then create an instance of this class.
# 2. add a method to car class that display the full name of the car(brand and model)


# class Car:
#     brand = None
#     model = None

# my_car = Car()
# print(my_car)

class Car:
    car_count = 0 # calss Variable : Which is define inside class , can be accessed in all instance(obj) using ClassName.variable
    def __init__(self,brand,model):  # __init__ :constructor which automatically initializes object attributes when an object is created  
        self.__brand = brand # privating
        self.__model = model
        Car.car_count +=1 # No of object created

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    @staticmethod  # decorators restrict thne access for object ,it can only be access 
    def description():
        return "Cars are mean of Transport"
    @property
    def model(self):
        return self.__model
    
    def get_brand(self):    # encapsulation : private method 
        return self.__brand + "!!!"

    def fuel_type(self):  # same function with diff working is polymorphism
        return "petrol or diesel"
    
class Electric_Car(Car):   # Inheritance
    def __init__(self,__brand,model,battery_size):
        super().__init__(__brand,model)
        self.battery_size = battery_size

    def fuel_type(self):   # same function with diff working is polymorphism
        return "Electric"
    
# Multiple Inheritance:
class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "this is Engine info"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

my_tesla = Electric_Car("Tesla","Model S","85KWH")  #Creation of object with values
# print(isinstance(my_tesla, Car))  # return   True 
# print(isinstance(my_tesla, Electric_Car))
# my_tesla.model = "sport's car"
# print(my_tesla.fuel_type())
safari = Car("Tata","safari")
# print(safari.fuel_type())
# print(Car.car_count) # gives count of car objec created
# print(safari.description())
# print(Car.description())   # print description because @staticmethod
# print(my_tesla.model)
# print(my_tesla.full_name())

# my_car = Car("BMW","gran coupe")
# print(my_tesla.__brand) # AttributeError: 'Electric_Car' object has no attribute '__brand'
# print(my_car.full_name())
# print(my_car) # give memory address

# Encapsulation :Modify the car class to encapsulate the brand attrbute, making it private, and provide a getter method for it.

# print(my_tesla.get_brand())