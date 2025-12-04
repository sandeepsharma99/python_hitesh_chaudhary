# Function with **kwargs : create a function that accept any number of keyword argument nad print them in the format key:value

def display(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} {value}")
display(name="sgaktiman",power="lazer",enemy="Dr.jackaal")