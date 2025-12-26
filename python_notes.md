# Q: What is python ?  
Ans : 
- Python is an interpreter dynamically typed object oriented high level programming language.
- it is known for its simple syntax 
- vast library and package support
- case sensitive like Apple and apple both are different. varaible
- rapid app development attract developer
- it is widely used in data science/analytics app development game development mostely in al/ml

# Q: Dynamic Typing 
- Python determines variable types at runtime based on the assigned value, so explicit declaration is not needed.

# Q: how do you work with date and time ?
- simply we import date and time module then.now()
```python
import datetime
now = datetime.datetime.now()
```

# Q: DataType ?
- Python has several built-in data types to cl




assify values/information, which represent what kind of value is stored and what operation can be performed on the data. 
There are following `7` categories: Numeric, Sequence , Mapping, Set, Boolean, NoneType and Binary Types. 

1. Numeric : int, float(decimals), complex
2. Sequence : string("", immutable sequence of character) ,list , tuple
3. Mapping : Dictionary (collection of{"Unique key":"value"},unordered)
4. Settype : set(mutable) , frozenset(immutable)
5. Boolean : True(1) , false(0)
6. NoneType : None
7. Binary Types : bytes

# Q: what is memory address/id() ?
Ans: id() is built-in function which refers tothe memory address(unique identifier of an object) allocated to the object

# Q: what is mutable and immutable

| Parameter | Mutable Data Types | Immutable Data Types |
|---------|-------------------|---------------------|
| Modification | Can be changed after creation | Cannot be changed after creation |
| Memory ID (`id()`) | Remains the same when modified | Changes when a new value is assigned |
| Examples | `list`, `dict`, `set` | `str`, `tuple`, `int`, `float`, `bool` |
| Use Cases | When content needs frequent updates | When data integrity is crucial |
| Thread Safety | Less safe in multi-threaded environments | Inherently thread-safe |

# Q: what is iterator ?
Ans : an iterator is the object that performs the iteration. You get an iterator from an iterable.  iter()
Check for More : check if ``next()` raises StopIteration

# Q: what is class and object ?
### class : in oop class is a blueprint/template for creating object 
- to create class we,uswe class keyword followed by classname :
- inside class you typically define attributes and methods
- The class definition doesn't take up memory until objects are created from it, but each object does.  
### object  : object is the real instanc of that blueprint/template
- To create an object we simply call class like function, and pass the argument require by `def __init__(self,a,b):`

### constructor : all the class have a function  called def __init__(self,a,b):, which is always executed when the obj is being initiated

### self : self is a reference of current instance of class(object), and is used to acces the variable that belongs to the class

### Abstraction : Hiding the implementation details of class and showing the essential feature to the user.

### Encapsulation : wrapping data and function into a single unit(object)

# Q: Map ,filter ,reduce
- map: Applies a function to every item in an iterable. return a map object (an iterator), to see result you must convert explicitly into list(filter(func,iterable)).
- filter: used to extrat element from an iterable based on specific condition. it applies a testing function to each element and keep only those for which the function return true
- reduce: Applies a function to the items of an iterable and accumulate/combine it to a single value.

# Q: Ways to join concatenate string 
ans : using `+` operator , "".join() method & f-strings method f"{str1}{str2}"

# Q: What is virtual enviroment ?
ans : A virtual environment is an **`isolated`** Python environment that allows you to manage dependencies for each project separately 
To create virtual enviroment `python -m venv venv` and to activate `venv\Scripts\activate`
- Prevents package/version conflicts in project
Why do we need a virtual environment? 🤔
Imagine this situation:
Project A needs Django 3.2
Project B needs Django 5.0
If both are installed globally ❌ → version conflict

# Q: what is File I/O in python ?
ans : python can be used to perform operation(read & write) on a file.
text file : .txt,, .doc,.log etc
binary file :.mp4, .jpg, .jpeg etc
#### open ,read and closeFile
``
f= open ("file_name", "r/w")
    f.read()
    f.close()
``
- r : reading only
- w : overwrites existing file (after truncation)
- a : add data at the end
- r+ : reading and writing Pointer starts at beginning
- w+ : Overwrites existing content after truncate
![My Image](./image/Screenshot%202025-12-26%20175505.png)

# Q : create a new file "practice.txt" using python. add the following data 
`hi everyone
we 'r learning File i/o
using java
i like programming in  jave

1. replace all occurance of "java" with "python"
2. search if the "learning exist or not"
3. WAF to find  in which line of the file does the word "learning" exist, print -1 if not found.
4. from  a file containing number separeated by comma, print the count of the even numbers.
` 
```python
with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java", "python")
    
with open("practice.txt","w") as f:
    f.write(new_data)
```
```python
def check_word:
    with open("practice.txt","r") as f:
        word = "learning"
        if("learning" in f):
            print("found")
        else:
            print("not found")

check_word()
```
```python
def check_word_inlin-no:
    with open("practice.txt","r") as f:
        data = True
        line-no =1
        data = f.readline()
        if(data in word):
            print(line-no)
            return
            line-no += 1
    return -1

print(check_word_inlin-no())
        
```

# Q: how do you read and write json data ?
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
# Q: String and method " "
Ans : sequence of character , immutable , represent by 'string',"string","""string"""
```python
mystr = "  Python Programming 123  " # creating a string
```
## Methods:
**Accessing character**
```python
mystr.lower() # returns lowercase string
mystr.upper() # returns uppercase string
mystr.title() # returns str object
mystr.capitalize() # returns a new string 
"Python".isalpha() # check and return (True or False)
mystr.strip() # returns a new string,it Removes leading and trailing spaces
mystr.replace("old_substring","new_substring",count) # returns a new string, count(optional)
mystr.split(separator) #  returns a list of substrings separators(optional) | Convert string to a list
mystr.find("",startindex,endindex) # startindex,endindex (optional) return index value or -1
mystr.index("",startindex,endindex) # return index of first occurrence 
mystr.count("") # returns an integer
len(mystr) # returns the total number of characters
mystr.startswith()/endswith() #  return True or False
" ".join(words) # returns a new single string
mystr[index] # return character at that index | **Accessing character**
mystr[start:stop:step] # return a new substring | Slicing | mystr[::]->create shallow copy
for char in s:  # iteration
    print(char) 
repr(),raw strings(r '')
```
- `f-strings` : string literals f"My name is {name},I live in {city}" used to embed variables

- `+` :
- `insert(index,element)`:  modifies the list in-place and returns None
- `.copy()` : returns a shallow copy independent object at the top level 
- `.update()` : return None, used with dictionaries and sets to add items
- `.reverse()` : Returns None syntax: my_list.reverse()
- `.remove(value)` : returns None, remove the first occurring value matching the given parameter from list in place modifies 
- `del a[index]` : Removes the item at index in-place return None
- `.clear()` : return None syntax : MyList.clear()
- `in keyword`: check and return (True or False)

# Q: How can you print a string without resolving escape sequences in Python?
ans : In python repr() function ensure that the escape sequences are displayed as part of the string rather than being processed.

Example:string = "Hello\nWorld\t!"
print(repr(string))  # Output: 'Hello\nWorld\t!'

# Q: List and its method []
Ans : list is a ``mutable & Ordered`` data structure stores mixed datatypes(int, str, bool, and even other lists). it can contain duplicate items 
```Python
    syntax : mylist = [1, 2, 3, 4, 5]
```
### Methods 
```Python
     mylist.append(element) # return None add element at the end
     mylist.extend(iterable) # merge two list retu
     mylist.insert(index,element) #
     mylist.remove(element) #
     mylist.pop() # returns that removed item
     mylist.sort(key=None, reverse=False) #
     mylist.reverse() #
     mylist.copy() #
```
# Q: what is List comprehension
Ans : 
- list comprehension is shortahnd way to create list
- Alternative of for loop or func like map() & filter()
- basic syntax is enclose in square bracket 
`even_no = [x for x in range(10) if x%2==0] `

# Q: Dictionary and method {}
ans : In Python Dictionary is a ``mutable & Ordered`` data structure stores data as unique key-value pairs, can store nested dictionary
- `offering fast lookups` because it uses hasing for quick access
- ## Hashing converts a key into a number (hash value).
This hash value tells Python where to store and find the data in memory.
So Python doesn’t search — it jumps directly to the location.
`dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}`
```python
my_dict = {'Animal': 'Lion', 'Order': 'Carnivora', 'Kingdom': 'Animalia'} # Create a sample dictionary

# Get the dictionary items view object
dict_items_view = my_dict.items() # return view object Each item in the view object is a tuple in the format (key, value)
print(f"The dictionary view object: {dict_items_view}")
# Output: The dictionary view object: dict_items([('Animal', 'Lion'), ('Order', 'Carnivora'), ('Kingdom', 'Animalia')]) 
```
```Python
    syntax : mydict = {"name": "Sandeep", "age": 21, "city": "Delhi"}
```
### Methods 
```Python
    mydict.get("name") #Returns value for specified key    
    mydict.get("salary", defaultvalue) # if the specified key does not exist return none/defaultvalue(optional)
    mydict.keys() #
    mydict.values() #
    mydict.items() #
    mydict.setdefault("gender", "Male") #
    mydict.setdefault("age", 25) #
    update({"age": 22, "country": "India"}) #
    mydict.pop("city")
    mydict.popitem()
    mydict.copy()
    keys = ["a", "b", "c"]
    new_dict = dict.fromkeys(keys, 0)
    mydict.clear()
```
- merge: using .update(), union operator, **unpacing
- mydict.items(): return view object
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

# Q: difference between append and extend
ans :
| Feature | `append()` | `extend()` |
|-------|------------|------------|
| What it does | Adds a **single item** as one element at the end | Adds **each element** from an iterable separately |
| Argument type | Any object (int, str, list, tuple, etc.) | Iterable only (list, tuple, set, string, etc.) |
| Effect on list | Always adds **one element** | Adds **multiple elements** |
| Change in length | Increases list length by **1** | Increases list length by **number of items** |
| Nested list | Creates a nested list if list is passed | Does **not** create nested list |

# Q: how do you reverse a list/string
Ans :
1. using .reverse() method
2. using slicing  reversed_list = list[::-1]

# Q: what is Difference between sort() and sorted()
Ans:

| Feature | `sort()` | `sorted()` |
|------|---------|-----------|
| Syntax | `mylist.sort()` | `sorted(iterable,key=len,reverse = false,)` |
| Type | List method | Built-in function |
| Modifies original list | modifies the originallist | Keep the original same  |
| Return value | `None` | Returns a **new sorted list** |
| Works on |apply Only on lists | Any iterable (string, list, tuple, set, etc.) |
| Memory usage | More efficient (in-place) | Uses extra memory for new list |

# Q: How do you sort a dictionary by value
Ans : 
```python 
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict) 
```
my_dict.items() returns  return dict_item object containing set of key ,value pair in tuple 
item: item[1] represent values of dict_item object

# Q: Frozenset 
Ans: Frozenset is an immutable and hashable version of standard set. it is unordered collection of unique element.
```Python
my_set = {1, 2, 3, 4, 5}
frozen_set = frozenset(my_set)
print(frozen_set)   
```
# Q:How do you find the sum of digits of an integer in Python?
Ans: You can find the sum of digits of an integer by converting it to a string, iterating over each character, and summing their integer values.
```Python
number = 12345
digit_sum = sum(int(digit) for digit in str(number))
print(digit_sum)
```
# Q:How do you flatten a list of lists in Python?
Ans :
```Python
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using list comprehension
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)
```
# Q:How do you find the most common element in a list in Python?
Ans : 
```Python
from collections import Counter # first importing counter from collection

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
most_common_element = Counter(my_list).most_common(1)[0][0]
print(most_common_element)
```
# Q:How do you check if a number is prime in Python?
Ans :
```Python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))
print(is_prime(4))
```

# Q:How do you find the greatest common divisor (GCD) of two numbers in Python?
Ans: 
```Python
import math

gcd = math.gcd(48, 18)
print(gcd)
```
# Q:How do you convert a list of integers to a single integer in Python?
Ans : You can convert a list of integers to a single integer by converting each element to a string and then joining them.
```Python
int_list = [1, 2, 3, 4, 5]
single_integer = int("".join(map(str, int_list))) # str is keyword which is used to typecasting str(--)
print(single_integer)
```
# Q:
# Q:
# Q:
# Q:
# Q:
```Python

```


