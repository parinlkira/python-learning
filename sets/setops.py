# add operations on sets
s = {10, 20, 30, 40, 50}
# add an element to the set
s.add(60)
s.add((60, 70))
print('Set after adding an element:', s)

# update the set with another set
s.update({70, 80})
s.update((21, 31))
s.update('abc')
print('Set after updating:', s)

# copy the set
s_copy = s.copy()
print('Copied set:', s_copy)

# its a shallow copy, changes to the original set won't affect the copy
print('ID of original set:', id(s))
print('ID of copied set:', id(s_copy))

# removing methods of sets
# remove an element from the set
s.remove(30)
print('s after removing 30:', s)

# discard an element from the set (doesn't raise an error if the 
# element is not present)
s.discard(10)
print('s after discarding 10:', s)    

# pop an element from the set (removes and returns an arbitrary element)
popped_element = s.pop()
print('Popped element:', popped_element)
print('s after popping an element:', s)

# clear the set (removes all elements)
s.clear()
print('s after clearing all elements:', s)


s1 = {1, 2, 3, 5, 7}
s2 = {5, 7, 9, 10, 11}

# union of sets
print('Union:', s1 | s2)
print('Union:', s1.union(s2))

# intersection of sets
print('Intersection:', s1 & s2)
print('Intersection:', s1.intersection(s2))

# intersection_update() updates the set with the 
# intersection of itself and another set
print('Intersection Update:', s1.intersection_update(s2))
print('s1 after Intersection Update:', s1)
s1 = {1, 2, 3, 5, 7}
s1 &= s2
print('s1 after Intersection Update with &=:', s1)

s1 = {1, 2, 3, 5, 7} # resetting s1 for further operations

# difference of sets
print('Difference:', s1 - s2)
print('Difference:', s1.difference(s2))

# difference_update() updates the set with the 
# difference of itself and another set
print('Difference Update:', s1.difference_update(s2))
print('s1 after Difference Update:', s1)

s1 = {1, 2, 3, 5, 7} # resetting s1 for further operations
# difference_update() with -= operator
s1 -= s2
print('s1 after Difference Update with -=:', s1)

# symmetric difference of sets
s1 = {1, 2, 3, 5, 7} # resetting s1 for further operations
print('Symmetric Difference:', s1 ^ s2)
print('Symmetric Difference:', s1.symmetric_difference(s2))

# symmetric_difference_update() updates the set with the 
# symmetric difference of itself and another set
print('Symmetric Difference Update:', s1.symmetric_difference_update(s2))
print('s1 after Symmetric Difference Update:', s1)

# symmetric_difference_update() with ^= operator
s1 = {1, 2, 3, 5, 7} # resetting s1 for further operations
s1 ^= s2
print('s1 after Symmetric Difference Update with ^=: ', s1)