from random import randint

myName = "Eduardo"

for index, val in enumerate(myName):
    print(f"index {index} val {val}")

# ? this is the same like the upper example
print("___________________________")
index = 0
for val in myName:
    print(f"index {index} val {val}")
    index = index+1


# * makes touples from list, combines it respectively
arr1 = [1, 2, 3, 4, 5]
arr2 = ["eee", "aaaa", "zzzz"]

arr3 = list(zip(arr1, arr2))
# ! result : [(1, 'eee'), (2, 'aaaa'), (3, 'zzzz')]

print(arr3)


# ? in reserved keyword is to know if a value is in an array or in an object
print("Is 1 in the arr1 ?")
print(1 in arr1)
# ? in reserved keyword is to know if a value is in an array or in an object
print("Is 10 in the arr1 ?")
print(10 in arr1)
# work in dicctionary and strings
exampleDicctionary = {"k1": 1, "k2": 2}

exampleKey = "k1"
exampleVal = 2

print(("Dicctionary example key"))
print(exampleKey in exampleDicctionary)

print(("Dicctionary example value"))
print(exampleVal in exampleDicctionary.values())

# makes a random int from 2 limits
print(randint(10, 100))

# ? gets user input

# userSays = input("What up?")
# print(userSays)


# * list comprehenison

comprehensionArr = [z for z in myName]
print(comprehensionArr)

# ? omits the "d" letter
comprehensionArr = [z for z in myName if(z != "d")]
print(comprehensionArr)

celcius = [0, 10, 20, 43, 3.3]

fahrenheit = [(9/5)*x + 32 for x in celcius]
print(fahrenheit)

fahrenheitSteroids = [(9/5)*x + 32 if x > 1 else "cero" for x in celcius]
print(fahrenheitSteroids)


rangeArr = [x for x in range(0, 100, 2)]
print(rangeArr)
