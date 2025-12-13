# Age group categorization : classify a person age group : Child(<13), teenager(13-19),Adult(20-59),
# Senior(60+)

age = 50

if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")


# a = 2
# b = 2
# a += 1
# print(a)

# str = "sandeep"
# str.capitalize() # change the refreence now str refering to new "sandeep" obj str.capitalize return a new string object.
# print(str.capitalize())
# print(str) 

import datetime

# Getting the current date and time
now = datetime.datetime.now()
print(now)

# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

# Converting the filter object to a list
even_numbers_list = list(even_numbers)
print(even_numbers_list)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# dict1.update(dict2)
merged = {**dict1, **dict2}  # Note: If keys overlap, the value from the right-hand dictionary (dict2) takes precedence. 
merged = dict1 | dict2

print(merged)