
import os

myFile = open("example.txt")
print(myFile)
print(myFile.read())
# hero you cannot see anything because the pointer is at the final of the file
print(myFile.read())

# you need yo restore the pointer to the start to the file
myFile.seek(0)
print(myFile.read())
myFile.seek(0)
# creates a list from the file
print(myFile.readlines())

print(os.system("pwd"))


with open("example.txt", mode="w") as f:
    f.write("\nmore rocolino text")


with open("xxx.txt", "w") as target:
    target.write("swww")
