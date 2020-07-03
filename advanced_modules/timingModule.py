import timeit


print("-".join((str(n) for n in range(100))))

# ? everage of time that takes to execute the function
print(timeit.timeit('"-".join((str(n) for n in range(100)))', number=10000))

# ? here you can see that the map method is faster than the range one
print(timeit.timeit('"-".join(map(str,range(100)))', number=10000))
