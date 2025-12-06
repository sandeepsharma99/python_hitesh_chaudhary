# scoping / closure /factory function

def parent(power):
    def child(x):
        return x**power
    return child

a1 =parent(2)
print(a1)
print(a1(2))