my_list = [1, 3, 2, 0]

print(my_list, len(my_list))

# ? sort not return nothing the function hapens in place only in the array where is called
print(my_list.sort())
print(my_list)

doble_array = [123, [1, 2]]

print(doble_array)


object = {'name': "eduardo", 'age': 21}

print(object["name"])
print(object.keys())
print(object.values())

# ? here prints some touples
print(object.items())


# ?touples are similars to the arrays or list but they are inmutable
touple_example = (1, 2)

print(touple_example)
print(touple_example[1])

#? sets are list of unique values
x = set()
x.add(1)
x.add(2)
x.add(2)


print(x)
