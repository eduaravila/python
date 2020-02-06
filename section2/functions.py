myList = [1, 2, 3]

help(myList.append)


def someFunction():
    '''
    DOCSTRING: SOME FUNCTIONS COOL
    '''
    return "gg izz"


print(someFunction())


# print(evenOddWord("eeeeeeee"))


print(list(map(lambda x: x.upper(), "seser")))


def just_odd(x):
    if(x % 2 == 0):
        return False
    else:
        return True

# * you can name the lamda functions 


# ? filter just the even values
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))

print(list(filter(just_odd,[1,2,3,4,5,6])))