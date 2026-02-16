# Generate function with yield :write a generator function that yields even number up to specified limit.

# def even_generator(limit):
#     for i in range(0,limit+1,2):
#         yield i 

# for i in even_generator(10):
#     print(i)


# def even_no_generator(limit):
#     for i in range(0,limit+1,2):
#         yield i

# for i in even_no_generator(20):
#     print(i)


def even_no_generator(limit):
    for i in range(0,limit+1,2):
        yield i

for i in even_no_generator(20):
    print(i,end=" ")
