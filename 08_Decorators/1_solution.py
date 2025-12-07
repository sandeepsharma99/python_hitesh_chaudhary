# Decorators 
# Timing function Execution :Write a decorators that measures the time a function takes to execute.
import time

def timer(func):     # General defination : timer is a higher-order function (a function that accepts another function).It takes one argument: func, which will be the function you want to decorate.
    def wrapper(*args,**kwargs):
        start = time.time()          # you note the current time before execution
        result = func(*args,**kwargs)
        end = time.time()            # you note the current time after execution
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer      
def example_func(n):
    time.sleep(n)

example_func(2)

    