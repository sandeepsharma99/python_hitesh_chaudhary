
# # a = 2
# # b = 2
# # a += 1
# # print(a)

# # str = "sandeep"
# # str.capitalize() # change the refreence now str refering to new "sandeep" obj str.capitalize return a new string object.
# # print(str.capitalize())
# # print(str) 

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


my_dict = {'name': 'Ashish', 'age': 25}

# Checking if key exists
if 'name' in my_dict:  # You can check if a key exists in a dictionary using the in keyword.
    print("Key exists!")
else:
    print("Key does not exist!")

# my_dict = {'a': 3, 'b': 1, 'c': 2}
# print(my_dict.items()) # return dict_item object containing set of key ,value pair in tuple # Converts dict → (key, value) tuples

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)

#36. How do you remove an element from a list by index in Python?
# Answer: You can remove an element from a list by index using the pop() method.
my_list = [1, 2, 3, 4, 5]

# Remove element at index 2
removed_element = my_list.pop(2)

print(removed_element)
print(my_list)

# 38. How do you create a list of even numbers using list comprehension?
# Answer: You can create a list of even numbers using list comprehension with a conditional statement.
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)