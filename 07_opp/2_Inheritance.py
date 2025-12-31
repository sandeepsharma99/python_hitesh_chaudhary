# class student :
    
#     # Default constructor :Automatic Generation with no argumnet 
#     # def __init__(self):
#     #     print("This is constructor invoke automatically when an object is created whether we write or not")

#     # Parameterized constructor
#     def __init__(self,name,age,city,marks):
#         self.name = name,
#         self.age = age,
#         self.city = city
#         self.marks = marks
#         # print(self)
    
#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         return sum/len(self.marks)
        

# s1 = student("sandeep", 26, "Noida",[94,92,95])
# # s2 = student("mandeep", 20, "Mumbai")
# # print(s2.name,s2.age,s2.city)

# # print(s1.avg())
# s1.name = "mandeep"
# # print(s1.name) # attributes manipulation

# class Account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no
#         print("balance : ",self.balance)
#         print("account_no : ",self.account_no)

#     def debit(self,debit_amt):
#         self.balance -= debit_amt
#         print(f"balance after {debit_amt} debit : ",self.balance)
    
#     def credit(self,credit_amt):
#         self.balance += credit_amt
#         print(f"balance after {credit_amt} credit : ",self.balance)



# acc1 = Account(1000,852369)
# acc1.debit(500)
# acc1.credit(2000)

# # Private attributes

# class user:
#     def __init__(self, acc_no, password):
#         self.acc_no = acc_no,
#         self.__password = password

#     def showPassword(self):
#         print(self.__password)

# user1 = user(921563,"sandeep")
# print(user1.showPassword())

# # Inheritance

#Parent Class
class car:
    wheel = 4

    def __init__(self,type):
        self.type = type

    def start(self):
        print("Car start")

    def stop(self):
        print("Car Stop")

# Child Class
class Toyota(car):

    def __init__(self,name,type):
        self.name = name
        super().__init__(type) # accessing attribute of parent class
        

# Multilevel inheritance
class fortuner(Toyota):
    def __init__(self,type):
        self.type = type


car1 = Toyota("Fortuner","electric")
print(car1.name)
print(car1.type)
# print(car1.wheel)
# print(car1.start())
# print(car1.stop())

# car2 = fortuner("diesel")
# print(car2.type)
# print(car2.start())
# print(car2.stop())

# Super () Method is used to acces the attributes of parent class.

