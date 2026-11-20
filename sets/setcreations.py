# set creation 

s = {1, 2, 4, 5, 6}
print(s)

s = {1.2, 3, 'Jack', True}
print(s)

s = set([1, 2, 3])
s = set('python')
print(s)

s = set()
print(type(s))

s = {} # This creates an empty dictionary, not a set, atlease one element 
       # is needed to create a set
print(type(s)) # <class 'dict'>

# adding elements to a set
s = {1,2,3,4,45,}
s.add(60)
s.add('hi')
s.add((1,2,4,3))
print(s)

# cant add mutable elements like lists or dictionaries to a set
#s.add([1,2,3]) # This will raise a TypeError
#s.add({'a': 1}) # This will also raise a TypeError

# removing elements from a set
s.remove(60) # removes 60 from the set
print(s)

# discard method removes an element if it exists, does nothing if it doesn't
s.discard('hi')
print(s)

# pop method removes and returns an arbitrary element from the set
popped_element = s.pop()
print(popped_element)
print(s)

# set comprehension
s = {x for x in range(1, 5)}
print(s)

s = {x**2 for x in {-2, -1, 0, 1, 2}}
print(s)    

s = {x.lower() for x in 'PhiLiPpineS'}
print(s) 