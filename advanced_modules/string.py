
# capitalize makes the first word letter capital

s = "dummy example"

print(s.capitalize())

# upper makes the whole sentence capital (just return a copy with the applied method)

print(s.upper())

# lower makes the whole sentence lower case
print(s.lower())

# return the number of occurrences without overlap
print(s.count("m"))

# return the index of the first occurrence
print(s.find("p"))

# the center method is kind of esoteric, because is rare see it in real code, what it does, center a word
# with a certain length and place a give string around the word
print(s.center(20, "f"))

# expands tabs make the same effect than \t

print(s.expandtabs())


# ? checks if the string is alphanumeric

print(s.isalnum())
# ? checks if the string is alphabetic

print(s.isalpha())

# checks if al the characters of the string are lowecase
print(s.islower())
# checks if al the characters of the string are upper
print(s.isupper())

# checks if the string ends with a certain character

print(s.endswith("w"))

# splits a string at a certain elememt and return the splitted string

print(s.split("d"))

# partition spits the string between before the first occurrence, the occurrence it self or the separator and the after of the occurrence
print(s.partition("d"))
