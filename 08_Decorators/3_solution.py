# Cache Return value : Implement a decorator taht caches the return alue of a function, so that when it's calledwith the same argument,the cached value  is return instead of  re-executing the function.
import time

def cache(fun):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return
        result = fun(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a,b):
    time.sleep(2)
    return a*b

print(long_running_function(2,5))
print(long_running_function(3,5))