# index(value, start, end)
# start: The starting index of the search.
# end: The ending index of the search.

l = [10, 20, 10, 20, 40, 30]
print(l.index(20))
print(l.index(20, 2))  # Search for 20 starting from index 2
print(l.index(40,4,7))

# count(element)
# element: The element to count in the list.

print(l.count(10))

# reverse()
# Reverses the elements of the list in place.

l.reverse()
print(l)

# sort(*, key=None, reverse=False)
# key: A function that serves as a key for the sort comparison.
# reverse: If True, the list elements are sorted in descending order.

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l = ['coat', 'python', 'black', 'cat']
l.sort()
print(l)

l.sort(key = len) # Sort the list based on the length of the elements
print(l)

l = ['apple', 'Bat', 'cat', 'Dog']
l.sort()
print(l) 

l.sort(key = str.lower, reverse = True)
print(l) 