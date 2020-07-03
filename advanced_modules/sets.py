
s = set()

# ? adds elements to the set if the value already exist then, anthing happens
s.add(1)
s.add(2)

print(s)

# remove all the elements from the set

# s.clear()

# copy the currents values from one set to other one
s1 = {1, 2, 3, 4}

s2 = s1.copy()

print(s2)

# returns the difference between two or more sets
difference = s.difference(s2)
difference2 = s2.difference(s)
print(difference)
print(difference2)

# removes the different elements from the argument set

s1.difference_update(s)

print(s)

# removes an element from a set if is not a member then do nothing
s1.discard(1)
print(s1)

# returns an intersection between two or more sets or the elements in common

print(s1.intersection(s))

# same as before but this methis will update the set
s1.intersection_update(s)
print(s1)

# this return True if the sets have a null intersection

print(s1.isdisjoint(s))

# if the instance set is inside the param set then return True

print(s1.issubset(s))

# returns the union between two sets
s1.union(s)

# update the instance set with a new union between itself and the param set
s1.update(s)
