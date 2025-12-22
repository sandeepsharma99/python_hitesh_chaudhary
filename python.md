# Q What is python ?  
Ans : 
- Python is an interpreter dynamically typed object oriented high level programming language.
- it is known for its simple syntax 
- vast library and package support
- case sensitive like Apple and apple both are different. varaible
- rapid app development attract developer
- it is widely used in data science/analytics app development game development mostely in al/ml

# Q Dynamic Typing 
- Python determines variable types at runtime based on the assigned value, so explicit declaration is not needed.

# Q how do you work with date and time ?
- simply we import date and time module then.now()
```python
import datetime
now = datetime.datetime.now()
```

# Q DataType ?
- Python has several built-in data types to classify values/information, which represent what kind of value is stored and what operation can be performed on the data. 
The primary categories include Numeric, Sequence , Mapping, Set, Boolean, NoneType and Binary Types. 

1. Numeric : int, float, complex
2. Sequence : string("", immutable sequence of character) ,list , tuple
3. Mapping : Dictionary ({"Unique key":"value"},unordered)
4. Settype : set(mutable) , frozenset(immutable)
5. Boolean : True(1) , false(0)
6. NoneType : None
7. Binary Types : bytes

# what is mutable and immutable

### Key Differences Between Mutable and Immutable Data Types

| Parameter | Mutable Data Types | Immutable Data Types |
|---------|-------------------|---------------------|
| Modification | Can be changed after creation | Cannot be changed after creation |
| Memory ID (`id()`) | Remains the same when modified | Changes when a new value is assigned |
| Examples | `list`, `dict`, `set` | `str`, `tuple`, `int`, `float`, `bool` |
| Use Cases | When content needs frequent updates | When data integrity is crucial |
| Thread Safety | Less safe in multi-threaded environments | Inherently thread-safe |



```python
import datetime
now = datetime.datetime.now()
a =  
```

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1])) 
print(sorted_dict)

```python

name = "Ashish"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
formatted_string_f = f"My name is {name} and I am {age} years old."
```