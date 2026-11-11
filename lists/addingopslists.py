# Adding only one element to a list using append()
l = [1, 2, 3]
l.append(4) 
print(l)

l = []
l.append(1)
l.append('python')
l.append([2,2])
l[5:5] = [10]
l[len(l): ] = [20]   
print(l)

# example of adding multiple elements to a list using extend() since it takes
# an iterable as an input
l = [1, 2, 3]
l.extend([4,5,6])
l[len(l):] = [7,8,9] 
l.extend('python') # notice this breaks the string into individual characters
print(l)

l = []
l.extend(range(4,8))
print(l)

# using insert() to add an element at a specific position
l = [1, 2, 3]
l.insert(0,50)
l.insert(70, 'python')
l.insert(2, 'random')
print(l)

# using slicing to add elements at a specific position
l[1:1] = ['a', 'b', 'c']
print(l)

# copy function

l = [1, 2, 3]
l2 = l.copy()
print(l2)