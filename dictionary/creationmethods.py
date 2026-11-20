# creating dictionaries using different methods

# iterable pairs 
d = dict([(1, 'one'), (2,'two'), (3, 'three')]) # using a list of tuples
print(d)

# using keyword arguments
d = dict(one=1, two=2, three=3)
print(d)

d = dict([[1, 'one'], [2, 'two'], [3, 'three']]) # using a list of lists
d = dict(((1, 'one'), (2, 'two'), (3, 'three'))) # using a tuple of tuples
d = dict(([1, 'one'], [2, 'two'], [3, 'three'])) # using a tuple of lists

# using zip function 

l = [1, 2, 3]; s = ['one', 'two', 'three']
d = zip(l, s)
d1 = dict(d)
print(d1)

# using enumerate function
l = ['one', 'two', 'three']
d = dict(enumerate(l, start = 1))
print(d)

# using dictionary comprehension
l = [(1, 'one'), (2, 'two'), (3, 'three')]
d = {x:y for x, y in l}
print(d)

# using zip function and comprehension
l = [1, 2, 3]; s = ['one', 'two', 'three']
d = {x:y for x, y in zip(l, s)}
print(d)

# using enumerate and comprehension
l = [ 'one', 'two', 'three']
d = {x:y for x, y in enumerate(l, start = 1)}
print(d)
