myNumber = 10

if myNumber == 2 and 2 > 1:
    print("gg izi")
elif myNumber > 2:
    print("number is greater than 2")
else:
    print("unkouwn number")


myNumbers = [1, 2, 3, 4, 5]
for element in myNumbers:
    print(element)

myDic = {"k1": 1, "k2": 2}
for key, val in myDic.items():
    print(f"Key:{key} ---- Val:{val}")

myToupleArray = [(1, 2), (3, 4)]

for val0,val1 in myToupleArray:
    print(f"Val0: {val0} | Val1: {val1}")
