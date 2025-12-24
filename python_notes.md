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
There are following `7` categories: Numeric, Sequence , Mapping, Set, Boolean, NoneType and Binary Types. 

1. Numeric : int, float(decimals), complex
2. Sequence : string("", immutable sequence of character) ,list , tuple
3. Mapping : Dictionary (collection of{"Unique key":"value"},unordered)
4. Settype : set(mutable) , frozenset(immutable)
5. Boolean : True(1) , false(0)
6. NoneType : None
7. Binary Types : bytes

# Q : what is memory address/id() ?
Ans: id() is built-in function which refers tothe memory address(unique identifier of an object) allocated to the object

# Q what is mutable and immutable

| Parameter | Mutable Data Types | Immutable Data Types |
|---------|-------------------|---------------------|
| Modification | Can be changed after creation | Cannot be changed after creation |
| Memory ID (`id()`) | Remains the same when modified | Changes when a new value is assigned |
| Examples | `list`, `dict`, `set` | `str`, `tuple`, `int`, `float`, `bool` |
| Use Cases | When content needs frequent updates | When data integrity is crucial |
| Thread Safety | Less safe in multi-threaded environments | Inherently thread-safe |

# Q what is iterator ?
Ans : an iterator is the object that performs the iteration. You get an iterator from an iterable.  iter()
Check for More : check if ``next()` raises StopIteration

# Q what is class and object ?
### class : in oop class is a blueprint/template for creating object 
- to create class we,uswe class keyword followed by classname :
- inside class you typically define attributes and methods
- The class definition doesn't take up memory until objects are created from it, but each object does.  
### object  : object is the real instanc of that blueprint/template
- To create an object we simply call class like function, and pass the argument require by `__init__()`

# Q Map ,filter ,reduce
- map: Applies a function to every item in an iterable. return a map object (an iterator), to see result you must convert explicitly into list(filter(func,iterable)).
- filter: used to extrat element from an iterable based on specific condition. it applies a testing function to each element and keep only those for which the function return true
- reduce: Applies a function to the items of an iterable and accumulate/combine it to a single value.

# Q Ways to join concatenate string 
ans : using `+` operator , "".join() method & f-strings method f"{str1}{str2}"

# Q What is virtual enviroment ?
ans : A virtual environment is an **`isolated`** Python environment that allows you to manage dependencies for each project separately 
To create virtual enviroment `python -m venv venv` and to activate `venv\Scripts\activate`
- Prevents package/version conflicts in project
Why do we need a virtual environment? 🤔
Imagine this situation:
Project A needs Django 3.2
Project B needs Django 5.0
If both are installed globally ❌ → version conflict

# how do you read and write json data ?
ans: In Python, the built-in json module is used to work with JSON data, primarily using the     `.load` functions for reading and `.dump` functions for writing
Use a with open() statement to ensure the file is properly closed

```python
import json

with open('data.json', 'r') as file: #ensure file close properly
    # Deserialize the file content into a Python object (e.g., dictionary)
    data = json.load(file)

print(data)
print(type(data))
```
# Q Dictionary and method 
ans : In Python Dictionary is a ``mutable & Ordered`` data structure stores data as unique key-value pairs,
- `offering fast lookups` because it uses hasing for quick access
- ## Hashing converts a key into a number (hash value).
This hash value tells Python where to store and find the data in memory.
So Python doesn’t search — it jumps directly to the location.
`dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}`

## Methods:
- merge: using .update
- .items():
- merge:
- merge:


```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using update() method
dict1.update(dict2) # to merge two dict returns : a new dictionary
print(dict1) # Output: {'a': 1, 'b': 3, 'c': 4}

# Using union operator(|)
merged = d1 | d2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}

# Using ** unpacking operator (Python 3.5+)
merged_dict = {**dict1, **dict2}
print(merged_dict) # Output: {'a': 1, 'b': 3, 'c': 4}
```

#  Q difference between append and extend
ans :

| Feature | `append()` | `extend()` |
|-------|------------|------------|
| What it does | Adds a **single item** as one element at the end | Adds **each element** from an iterable separately |
| Argument type | Any object (int, str, list, tuple, etc.) | Iterable only (list, tuple, set, string, etc.) |
| Effect on list | Always adds **one element** | Adds **multiple elements** |
| Change in length | Increases list length by **1** | Increases list length by **number of items** |
| Nested list | Creates a nested list if list is passed | Does **not** create nested list |

