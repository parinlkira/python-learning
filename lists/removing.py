# pop(index) removes and returns the element at the specified index. 
# If no index is specified, it removes and returns the last element.

l = [1, 2, 3, 4, 5]
l.pop()
print(l)  # Output: [1, 2, 3, 4]
l.pop(1)
print(l)  # Output: [1, 3, 4]

# remove(value) removes the first occurrence of the specified value.
l = [1, 3, 2, 3]
l.remove(3)
print(l)  # Output: [1, 2, 3]

# clear() removes all elements from the list.
l = [1, 2, 3]
l.clear()
print(l)  # Output: []

# del statement can also be used to remove elements from a list by index.
l = [1,2,3,4]
del l[2]
print(l)  # Output: [1, 2, 4] 

del l[1:3]
print(l)  # Output: [1]

l = [1, 2, 3, 4, 5]
del l # deletes the entire list and the variable itself
# print(l) would raise a NameError since l no longer exists
# can be also used to delete variables themselves.