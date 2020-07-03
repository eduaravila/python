from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

l = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0, 7,  43,
     345, 46, 436, 346, 346, 346, 346, 346, 346]

sentence = "some sentence in english to practice and y can test the counter function"
print(Counter(l))

c = Counter(sentence.split())
print(c)
print(c.most_common(2))


# ? a default dictionary is like a normal dictionary but it does not trow an error when the key is not created instead it create it and assing a default value for it, you can pass a custom function to assign this values

defaultdictbuildin = {"k1": 1}

print(defaultdictbuildin["k1"])

# ! if you try to execute the below code is going to trow an error
# print(defaultdictbuildin["k2"])

customDict = defaultdict(object)  # * you can initialize the dict with a object
# * you can initialize the dict with a custom function
# here you initialize all the keys with a value of 0
customDict2 = defaultdict(lambda: 0)

# even when the keys does not exist the defauldic initialize the key with a 0 value
print(customDict2["notExist"])

d1 = {}
d1["1"] = 1
d1["2"] = 2

d2 = {}
d2["2"] = 2
d2["1"] = 1

# this is true
print(d2 == d1)

ord1 = OrderedDict()
ord1["1"] = 1
ord1["2"] = 2

ord2 = OrderedDict()
ord2["2"] = 2
ord2["1"] = 1

# ! this is false, because in orderedDict the order of how the values where added is important even if they have the save keys and values
print(ord2 == ord1)

Cat = namedtuple("Cat", "age weight color")

myCat = Cat(age=10, weight="10kg", color="brown")

# in a namedtuple you can access the values like in an object or whereas you keep the default method that access the values from the index
print(myCat.age)
print(myCat[0])
