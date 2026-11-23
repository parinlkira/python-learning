# Adding and updating items in a dictionary using the update() method

d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
d2 = {5: 'five'}

d.update(d2)
print(d)

# using the fromkeys() method to create a new dictionary 
# with specified keys and a default value. It uses the dict static class

l = [1, 2, 3, 4]
d = dict.fromkeys(l)
print(d)

d = dict.fromkeys(l, 'unknown')
print(d)

# using copy() method to create a shallow copy of the dictionary

d_copy = d.copy()
print(d_copy)

d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# using pop() method to remove an item by key

print(d.pop(3))

print(d.pop(5, 'Missing')) # returns 'Missing' because key 5 is not 
                           # in the dictionary

# using popitem() method to remove and return the last inserted item
item = d.popitem()
print(item)
print(d)

# using clear() method to remove all items from the dictionary
d.clear()
print(d)