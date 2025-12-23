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


