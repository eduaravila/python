def gen_cubes(n=10):
    for item in range(n):
        # makes a number from a range and gets the cube from the current item
        yield item ** 3


# for x in gen_cubes(10):
#     print(x)


# def fibonacci(n):
#     a = 1
#     b = 1
#     for item in range(n):
#         yield a
#         a, b = b, a+b


# for i in fibonacci(10):
#     print(i)


g = gen_cubes(10)
# ? the next function keeps track of the last value 
print(next(g))
print(next(g))
print(next(g))

name ="Eduardo"

x = iter(name)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# when the string values are done then the compiler trows an StopIterator error
print(next(x))

