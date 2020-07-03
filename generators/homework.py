import random


def genSquare(n):
    for x in range(n):
        yield x ** 2


for item in genSquare(10):
    print(item)


def genRandom(n, min, max):
    for x in range(n):
        yield random.randrange(min, max)


for randItem in genRandom(10, 0, 10):
    print(randItem)

s = "Eduardo"
sIter = iter(s)

for sItem in sIter:
    print(sItem)
