# Default Value Parameter :Write a function that greets user. if no nam eis provided, it should greet with a default name.
def greet(name="User"):
    return "hello, "+ name

print(greet("sandeep"))
print(greet())